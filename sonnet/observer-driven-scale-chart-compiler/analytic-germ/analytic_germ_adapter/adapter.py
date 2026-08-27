"""Bounded elementary analytic-phase to exact polynomial-germ adapter.

The module intentionally knows nothing about Bessel, Airy, or any named normal
form.  A special-function expression is rejected at the boundary.  Successful
output is passed to the already-frozen exact monomial balance solver.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from typing import Mapping, Sequence

import sympy as sp

from scale_compiler import BalanceResult, Scale, infer_distinguished_scaling
from scale_compiler.balance import (
    BalanceError,
    InconsistentBalanceError,
    UnderdeterminedBalanceError,
)
from scale_compiler.ir import Const, Expr, Var


@dataclass(frozen=True)
class LocalCoordinate:
    """One source symbol, its expansion centre, and its local chart name."""

    symbol: sp.Symbol
    center: sp.Expr
    local_name: str
    role: str = "parameter"

    def __post_init__(self) -> None:
        if self.role not in {"state", "parameter"}:
            raise ValueError("coordinate role must be 'state' or 'parameter'")
        if not self.local_name or not self.local_name.isidentifier():
            raise ValueError("local_name must be a nonempty identifier")


@dataclass(frozen=True)
class GermBudget:
    max_input_ops: int = 256
    max_total_degree: int = 7
    max_expanded_terms: int = 128
    max_subset_candidates: int = 128

    def __post_init__(self) -> None:
        if min(
            self.max_input_ops,
            self.max_total_degree,
            self.max_expanded_terms,
            self.max_subset_candidates,
        ) < 1:
            raise ValueError("all germ budgets must be positive")


@dataclass(frozen=True)
class GermFailure:
    code: str
    message: str


@dataclass(frozen=True)
class GermTerm:
    expression: sp.Expr
    coefficient: sp.Expr
    powers: Mapping[str, int]
    total_local_degree: int


@dataclass(frozen=True)
class GermCertificate:
    source_digest: str
    shifted_phase: sp.Expr
    truncated_phase: sp.Expr
    selected_phase: sp.Expr
    known_residual_phase: sp.Expr
    selected_degree: int
    formal_tail_total_degree: int
    formal_tail_order_bound: Scale
    known_residual_orders: tuple[Scale, ...]
    classification: str
    balance: BalanceResult
    checks: tuple[tuple[str, bool], ...]

    @property
    def certified(self) -> bool:
        return self.balance.certified and all(ok for _, ok in self.checks)


@dataclass(frozen=True)
class GermReport:
    status: str
    certificate: GermCertificate | None
    failures: tuple[GermFailure, ...]
    input_ops: int
    expanded_terms: int
    subset_candidates: int

    @property
    def certified(self) -> bool:
        return self.status == "ok" and self.certificate is not None and self.certificate.certified


_ALLOWED_ANALYTIC_FUNCTIONS = {
    sp.sin,
    sp.cos,
    sp.sinh,
    sp.cosh,
    sp.exp,
    sp.log,
}


def adapt_phase_to_germ(
    phase: sp.Expr,
    *,
    coordinates: Sequence[LocalCoordinate],
    fixed_scales: Mapping[str, Scale],
    target_order: Scale | None = None,
    budget: GermBudget | None = None,
    require_degenerate: bool = False,
) -> GermReport:
    """Adapt a declared elementary analytic phase to the frozen balance solver.

    This is a total, typed-report boundary: expected research failures are
    returned as data and never silently replaced by a heuristic chart.
    """

    target_order = target_order or Scale(0)
    budget = budget or GermBudget()
    expression = sp.sympify(phase)
    input_ops = int(sp.count_ops(expression, visual=False))
    if input_ops > budget.max_input_ops:
        return _failed("resource-budget-exceeded", "input operation count exceeds the germ budget", input_ops)
    if not coordinates:
        return _failed("missing-coordinate", "at least one local coordinate is required", input_ops)
    names = [coordinate.local_name for coordinate in coordinates]
    if len(names) != len(set(names)):
        return _failed("duplicate-coordinate", "local coordinate names must be unique", input_ops)

    if expression.has(sp.Abs, sp.sign, sp.Piecewise):
        return _failed("non-analytic-germ", "Abs, sign, and Piecewise are outside the analytic germ", input_ops)
    unsupported = sorted(
        {
            str(function.func)
            for function in expression.atoms(sp.Function)
            if function.func not in _ALLOWED_ANALYTIC_FUNCTIONS
        }
    )
    if unsupported:
        return _failed(
            "special-function-oracle-required",
            "phase extraction from unsupported functions is outside discovery: " + ", ".join(unsupported),
            input_ops,
        )
    local_symbols = {coordinate.local_name: sp.Symbol(coordinate.local_name) for coordinate in coordinates}
    substitution = {
        coordinate.symbol: sp.sympify(coordinate.center) + local_symbols[coordinate.local_name]
        for coordinate in coordinates
    }
    shifted = sp.expand(expression.subs(substitution))
    # SymPy symbols with the same printed name but different assumptions are
    # distinct objects.  The frozen scale contract is name-based, so normalize
    # declared fixed symbols before polynomial extraction and certificate replay.
    canonical_fixed = {name: sp.Symbol(name) for name in fixed_scales}
    shifted = shifted.xreplace(
        {
            symbol: canonical_fixed[str(symbol)]
            for symbol in shifted.free_symbols
            if str(symbol) in canonical_fixed and symbol not in local_symbols.values()
        }
    )
    fixed_symbol_set = set(canonical_fixed.values())
    if any(
        argument.free_symbols & fixed_symbol_set
        for function in shifted.atoms(sp.Function)
        for argument in function.args
    ):
        return _failed(
            "fixed-scale-inside-analytic-function",
            "formal tail certification forbids fixed-scale symbols inside analytic-function arguments",
            input_ops,
        )
    epsilon = sp.Dummy("germ_epsilon")
    scaled = shifted.subs({symbol: epsilon * symbol for symbol in local_symbols.values()})
    try:
        truncated_epsilon = sp.series(
            scaled,
            epsilon,
            0,
            budget.max_total_degree + 1,
        ).removeO()
    except (NotImplementedError, PoleError, ValueError) as error:
        return _failed("non-analytic-germ", f"bounded Taylor expansion failed: {error}", input_ops)
    truncated = sp.expand(truncated_epsilon.subs(epsilon, 1))

    allowed_symbols = set(local_symbols.values()) | fixed_symbol_set
    if not truncated.free_symbols <= allowed_symbols:
        extra = sorted(str(symbol) for symbol in truncated.free_symbols - allowed_symbols)
        return _failed(
            "undeclared-symbol",
            "germ contains symbols without local or fixed scales: " + ", ".join(extra),
            input_ops,
        )
    try:
        terms = _extract_terms(truncated, local_symbols, fixed_scales)
    except sp.PolynomialError as error:
        return _failed("non-polynomial-germ", f"Taylor germ is not polynomial in declared symbols: {error}", input_ops)
    if len(terms) > budget.max_expanded_terms:
        return _failed("resource-budget-exceeded", "expanded germ exceeds the term budget", input_ops, len(terms))

    active = [term for term in terms if any(term.powers.get(name, 0) for name in names)]
    if not active:
        return _failed("insufficient-rank", "germ has no coordinate-dependent monomials", input_ops, len(terms))

    subset_candidates = 0
    for selected_degree in sorted({term.total_local_degree for term in active}):
        prefix = [term for term in active if term.total_local_degree <= selected_degree]
        if _rank(prefix, names) < len(names):
            continue
        selected_phase = sp.expand(sum((term.expression for term in prefix), sp.S.Zero))
        try:
            balance = infer_distinguished_scaling(
                _sympy_polynomial_to_ir(selected_phase),
                unknown_scales=tuple(names),
                fixed_scales=fixed_scales,
                target_order=target_order,
            )
        except InconsistentBalanceError:
            ambiguity, used = _detect_ambiguity(
                prefix,
                active,
                names,
                fixed_scales,
                target_order,
                budget.max_subset_candidates,
            )
            subset_candidates += used
            if ambiguity:
                return _failed(
                    "ambiguous-germ",
                    "competing rank-complete monomial subsets induce distinct admissible charts",
                    input_ops,
                    len(terms),
                    subset_candidates,
                )
            return _failed(
                "inconsistent-germ",
                "the first rank-completing degree prefix has inconsistent balance equations",
                input_ops,
                len(terms),
                subset_candidates,
            )
        except UnderdeterminedBalanceError:
            continue
        except BalanceError as error:
            return _failed(error.code, str(error), input_ops, len(terms), subset_candidates)

        residual_terms = [term for term in active if term.total_local_degree > selected_degree]
        residual_orders = tuple(_term_order(term, balance.scales, fixed_scales) for term in residual_terms)
        if any(order >= target_order for order in residual_orders):
            return _failed(
                "unsafe-residual",
                "a known higher-degree germ term is not below the declared target order",
                input_ops,
                len(terms),
                subset_candidates,
            )
        tail_bound = _formal_tail_bound(
            budget.max_total_degree + 1,
            balance.scales,
            fixed_scales,
            terms,
        )
        if tail_bound >= target_order:
            return _failed(
                "unsafe-formal-tail",
                "the conservative formal Taylor-tail order is not below target",
                input_ops,
                len(terms),
                subset_candidates,
            )

        classification = _classify(prefix, coordinates)
        if require_degenerate and not classification.startswith("degenerate-order-"):
            return _failed(
                "regular-saddle",
                f"declared turning-point task received structural class {classification}",
                input_ops,
                len(terms),
                subset_candidates,
            )
        known_residual = sp.expand(sum((term.expression for term in residual_terms), sp.S.Zero))
        source_digest = sha256(sp.srepr(expression).encode("utf-8")).hexdigest()
        checks = (
            ("balance-replay", balance.certified),
            ("minimal-rank-prefix", _rank([term for term in active if term.total_local_degree < selected_degree], names) < len(names)),
            ("known-residual-below-target", all(order < target_order for order in residual_orders)),
            ("formal-tail-below-target", tail_bound < target_order),
            ("polynomial-reconstruction", sp.expand(selected_phase + known_residual - sum((term.expression for term in active), sp.S.Zero)) == 0),
        )
        certificate = GermCertificate(
            source_digest=source_digest,
            shifted_phase=shifted,
            truncated_phase=truncated,
            selected_phase=selected_phase,
            known_residual_phase=known_residual,
            selected_degree=selected_degree,
            formal_tail_total_degree=budget.max_total_degree + 1,
            formal_tail_order_bound=tail_bound,
            known_residual_orders=residual_orders,
            classification=classification,
            balance=balance,
            checks=checks,
        )
        return GermReport("ok", certificate, (), input_ops, len(terms), subset_candidates)

    return _failed(
        "insufficient-rank",
        "bounded germ does not determine every requested scale",
        input_ops,
        len(terms),
        subset_candidates,
    )


def _failed(
    code: str,
    message: str,
    input_ops: int,
    expanded_terms: int = 0,
    subset_candidates: int = 0,
) -> GermReport:
    return GermReport("failed", None, (GermFailure(code, message),), input_ops, expanded_terms, subset_candidates)


def _extract_terms(
    expression: sp.Expr,
    local_symbols: Mapping[str, sp.Symbol],
    fixed_scales: Mapping[str, Scale],
) -> list[GermTerm]:
    symbols = [sp.Symbol(name) for name in fixed_scales] + list(local_symbols.values())
    polynomial = sp.Poly(expression, *symbols)
    terms: list[GermTerm] = []
    for powers_tuple, coefficient in polynomial.terms():
        powers = {str(symbol): int(power) for symbol, power in zip(symbols, powers_tuple) if power}
        term = sp.sympify(coefficient)
        for symbol, power in zip(symbols, powers_tuple):
            term *= symbol ** power
        degree = sum(powers.get(name, 0) for name in local_symbols)
        terms.append(GermTerm(sp.expand(term), coefficient, powers, degree))
    return sorted(
        terms,
        key=lambda term: (term.total_local_degree, tuple(sorted(term.powers.items())), sp.srepr(term.coefficient)),
    )


def _rank(terms: Sequence[GermTerm], names: Sequence[str]) -> int:
    if not terms:
        return 0
    return int(sp.Matrix([[term.powers.get(name, 0) for name in names] for term in terms]).rank())


def _term_order(
    term: GermTerm,
    unknown_scales: Mapping[str, Scale],
    fixed_scales: Mapping[str, Scale],
) -> Scale:
    total = Fraction(0)
    for name, power in term.powers.items():
        if name in unknown_scales:
            total += power * unknown_scales[name].power
        elif name in fixed_scales:
            total += power * fixed_scales[name].power
        else:
            raise ValueError(f"missing scale for {name}")
    return Scale(total)


def _formal_tail_bound(
    tail_total_degree: int,
    unknown_scales: Mapping[str, Scale],
    fixed_scales: Mapping[str, Scale],
    observed_terms: Sequence[GermTerm],
) -> Scale:
    slowest_local = max(scale.power for scale in unknown_scales.values())
    # The elementary analytic coefficient may carry the same fixed-scale
    # prefactor seen in the finite germ.  Taking its maximum is conservative
    # within this explicitly restricted polynomial-coefficient grammar.
    fixed_bound = Fraction(0)
    for term in observed_terms:
        fixed_order = sum(
            power * fixed_scales[name].power
            for name, power in term.powers.items()
            if name in fixed_scales
        )
        fixed_bound = max(fixed_bound, fixed_order)
    return Scale(fixed_bound + tail_total_degree * slowest_local)


def _classify(terms: Sequence[GermTerm], coordinates: Sequence[LocalCoordinate]) -> str:
    states = [coordinate.local_name for coordinate in coordinates if coordinate.role == "state"]
    parameters = {coordinate.local_name for coordinate in coordinates if coordinate.role == "parameter"}
    if len(states) != 1:
        return "unclassified-multistate"
    state = states[0]
    pure_orders = [
        term.powers.get(state, 0)
        for term in terms
        if term.powers.get(state, 0) > 0
        and all(term.powers.get(parameter, 0) == 0 for parameter in parameters)
    ]
    if not pure_orders:
        return "coupled-no-pure-state-term"
    order = min(pure_orders)
    if order == 2:
        return "regular-quadratic"
    if order >= 3:
        return f"degenerate-order-{order}"
    return f"nonstationary-order-{order}"


def _detect_ambiguity(
    prefix: Sequence[GermTerm],
    all_terms: Sequence[GermTerm],
    names: Sequence[str],
    fixed_scales: Mapping[str, Scale],
    target_order: Scale,
    max_candidates: int,
) -> tuple[bool, int]:
    solutions: set[tuple[Fraction, ...]] = set()
    used = 0
    for subset in combinations(prefix, len(names)):
        if used >= max_candidates:
            break
        if _rank(subset, names) < len(names):
            continue
        used += 1
        try:
            result = infer_distinguished_scaling(
                _sympy_polynomial_to_ir(sum((term.expression for term in subset), sp.S.Zero)),
                unknown_scales=tuple(names),
                fixed_scales=fixed_scales,
                target_order=target_order,
            )
        except BalanceError:
            continue
        omitted = [term for term in all_terms if term not in subset]
        if any(_term_order(term, result.scales, fixed_scales) > target_order for term in omitted):
            continue
        solutions.add(tuple(result.scales[name].power for name in names))
        if len(solutions) > 1:
            return True, used
    return False, used


def _sympy_polynomial_to_ir(expression: sp.Expr) -> Expr:
    expression = sp.sympify(expression)
    if expression.is_Number:
        return Const(expression)
    if isinstance(expression, sp.Symbol):
        return Var(str(expression))
    if isinstance(expression, sp.Add):
        result: Expr = Const(0)
        for argument in expression.args:
            result = result + _sympy_polynomial_to_ir(argument)
        return result
    if isinstance(expression, sp.Mul):
        result = Const(1)
        for argument in expression.args:
            result = result * _sympy_polynomial_to_ir(argument)
        return result
    if isinstance(expression, sp.Pow) and expression.exp.is_Integer and int(expression.exp) >= 0:
        return _sympy_polynomial_to_ir(expression.base) ** int(expression.exp)
    raise ValueError(f"unsupported polynomial coefficient/node: {expression}")


def germ_summary(report: GermReport) -> dict[str, object]:
    """Return a deterministic JSON-compatible replay ledger."""

    summary: dict[str, object] = {
        "status": report.status,
        "certified": report.certified,
        "failures": [asdict(failure) for failure in report.failures],
        "cost": {
            "input_ops": report.input_ops,
            "expanded_terms": report.expanded_terms,
            "subset_candidates": report.subset_candidates,
        },
    }
    if report.certificate is None:
        return summary
    certificate = report.certificate
    summary["certificate"] = {
        "source_digest": certificate.source_digest,
        "shifted_phase": str(certificate.shifted_phase),
        "truncated_phase": str(certificate.truncated_phase),
        "selected_phase": str(certificate.selected_phase),
        "known_residual_phase": str(certificate.known_residual_phase),
        "selected_degree": certificate.selected_degree,
        "formal_tail_total_degree": certificate.formal_tail_total_degree,
        "formal_tail_order_bound": str(certificate.formal_tail_order_bound),
        "known_residual_orders": [str(order) for order in certificate.known_residual_orders],
        "classification": certificate.classification,
        "scales": {name: str(scale) for name, scale in certificate.balance.scales.items()},
        "normalized_phase": str(certificate.balance.normalized_phase),
        "checks": [{"name": name, "passed": passed} for name, passed in certificate.checks],
    }
    return summary
