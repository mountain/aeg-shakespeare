"""Backend-neutral JSON expression IR.

The IR deliberately separates a finite expression DAG from a symbolic-height
iteration request.  ``SymbolicIterate`` is not traversed as a finite unrolling;
doing so would violate the evidence firewall in issue #142.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable, Mapping


class IRValidationError(ValueError):
    """The supplied object is not a well-formed ScaleExpr."""


def _fraction(value: int | str | Fraction) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise IRValidationError(f"invalid rational {value!r}") from exc


class ScaleExpr:
    """Marker base class for the closed finite research grammar."""

    def to_data(self) -> dict[str, Any]:
        raise NotImplementedError


@dataclass(frozen=True)
class Const(ScaleExpr):
    value: Fraction

    def __init__(self, value: int | str | Fraction):
        object.__setattr__(self, "value", _fraction(value))

    def to_data(self) -> dict[str, Any]:
        return {"op": "const", "value": str(self.value)}


@dataclass(frozen=True)
class Symbol(ScaleExpr):
    name: str

    def __post_init__(self) -> None:
        if not self.name or not self.name.isidentifier():
            raise IRValidationError("symbol name must be a nonempty identifier")

    def to_data(self) -> dict[str, Any]:
        return {"op": "symbol", "name": self.name}


@dataclass(frozen=True)
class Add(ScaleExpr):
    terms: tuple[ScaleExpr, ...]

    def __init__(self, *terms: ScaleExpr):
        if not terms:
            raise IRValidationError("add requires at least one term")
        object.__setattr__(self, "terms", tuple(terms))

    def to_data(self) -> dict[str, Any]:
        return {"op": "add", "terms": [term.to_data() for term in self.terms]}


@dataclass(frozen=True)
class Mul(ScaleExpr):
    factors: tuple[ScaleExpr, ...]

    def __init__(self, *factors: ScaleExpr):
        if not factors:
            raise IRValidationError("mul requires at least one factor")
        object.__setattr__(self, "factors", tuple(factors))

    def to_data(self) -> dict[str, Any]:
        return {"op": "mul", "factors": [factor.to_data() for factor in self.factors]}


@dataclass(frozen=True)
class Pow(ScaleExpr):
    base: ScaleExpr
    exponent: Fraction

    def __init__(self, base: ScaleExpr, exponent: int | str | Fraction):
        object.__setattr__(self, "base", base)
        object.__setattr__(self, "exponent", _fraction(exponent))

    def to_data(self) -> dict[str, Any]:
        return {"op": "pow", "base": self.base.to_data(), "exponent": str(self.exponent)}


@dataclass(frozen=True)
class Exp(ScaleExpr):
    argument: ScaleExpr

    def to_data(self) -> dict[str, Any]:
        return {"op": "exp", "argument": self.argument.to_data()}


@dataclass(frozen=True)
class Log(ScaleExpr):
    argument: ScaleExpr

    def to_data(self) -> dict[str, Any]:
        return {"op": "log", "argument": self.argument.to_data()}


@dataclass(frozen=True)
class GeneralizedPolynomial(ScaleExpr):
    """A finite ordered-monomial sum with rational exponents.

    This is finite C1f syntax, not a Hahn-series or field implementation.
    Exponents are sorted during serialization so certificates are deterministic.
    """

    terms: tuple[tuple[Fraction, Fraction], ...]
    scale_symbol: str = "N"

    def __init__(
        self,
        terms: Mapping[int | str | Fraction, int | str | Fraction],
        scale_symbol: str = "N",
    ):
        if not scale_symbol.isidentifier():
            raise IRValidationError("scale symbol must be an identifier")
        parsed = tuple(sorted(((_fraction(e), _fraction(c)) for e, c in terms.items()), key=lambda x: x[0]))
        if not parsed:
            raise IRValidationError("GeneralizedPolynomial must contain at least one monomial")
        if any(coefficient == 0 for _, coefficient in parsed):
            raise IRValidationError("zero coefficients must be removed")
        object.__setattr__(self, "terms", parsed)
        object.__setattr__(self, "scale_symbol", scale_symbol)

    def to_data(self) -> dict[str, Any]:
        return {
            "op": "generalized-polynomial",
            "scale_symbol": self.scale_symbol,
            "terms": [[str(e), str(c)] for e, c in self.terms],
        }


@dataclass(frozen=True)
class SymbolicIterate(ScaleExpr):
    """Uniform, symbolic-height iteration; never represented by unrolling."""

    function: str
    seed: ScaleExpr
    height_symbol: str

    def __post_init__(self) -> None:
        if self.function not in {"exp", "log"}:
            raise IRValidationError("symbolic iteration supports only exp or log requests")
        if not self.height_symbol.isidentifier():
            raise IRValidationError("height symbol must be an identifier")

    def to_data(self) -> dict[str, Any]:
        return {
            "op": "symbolic-iterate",
            "function": self.function,
            "seed": self.seed.to_data(),
            "height_symbol": self.height_symbol,
        }


@dataclass(frozen=True)
class AbelTask(ScaleExpr):
    """A task for F(x+1)=exp(F(x)), not an assumed solution oracle."""

    variable: str = "x"
    normalization: str | None = None

    def __post_init__(self) -> None:
        if not self.variable.isidentifier():
            raise IRValidationError("Abel variable must be an identifier")

    def to_data(self) -> dict[str, Any]:
        return {"op": "abel-task", "variable": self.variable, "normalization": self.normalization}


def children(expr: ScaleExpr) -> tuple[ScaleExpr, ...]:
    if isinstance(expr, Add):
        return expr.terms
    if isinstance(expr, Mul):
        return expr.factors
    if isinstance(expr, Pow):
        return (expr.base,)
    if isinstance(expr, (Exp, Log)):
        return (expr.argument,)
    if isinstance(expr, SymbolicIterate):
        return (expr.seed,)
    return ()


def walk(expr: ScaleExpr, path: str = "root") -> Iterable[tuple[str, ScaleExpr]]:
    yield path, expr
    for index, child in enumerate(children(expr)):
        yield from walk(child, f"{path}.{index}")


def expr_from_data(data: Mapping[str, Any]) -> ScaleExpr:
    """Strict decoder used by the corpus runner and independent replay."""

    op = data.get("op")
    if op == "const":
        return Const(data["value"])
    if op == "symbol":
        return Symbol(str(data["name"]))
    if op == "add":
        return Add(*(expr_from_data(item) for item in data["terms"]))
    if op == "mul":
        return Mul(*(expr_from_data(item) for item in data["factors"]))
    if op == "pow":
        return Pow(expr_from_data(data["base"]), data["exponent"])
    if op == "exp":
        return Exp(expr_from_data(data["argument"]))
    if op == "log":
        return Log(expr_from_data(data["argument"]))
    if op == "generalized-polynomial":
        return GeneralizedPolynomial({e: c for e, c in data["terms"]}, str(data["scale_symbol"]))
    if op == "symbolic-iterate":
        return SymbolicIterate(str(data["function"]), expr_from_data(data["seed"]), str(data["height_symbol"]))
    if op == "abel-task":
        return AbelTask(str(data.get("variable", "x")), data.get("normalization"))
    raise IRValidationError(f"unknown ScaleExpr operation {op!r}")
