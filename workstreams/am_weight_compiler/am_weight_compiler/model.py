from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import gcd
from typing import Any, Iterable, Mapping


def parse_fraction(value: object, *, field: str = "value") -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{field} must be rational") from exc
    raise ValueError(f"{field} must be rational")


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest_json(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def lcm(left: int, right: int) -> int:
    return abs(left * right) // gcd(left, right) if left and right else 0


@dataclass(frozen=True)
class ExpQCoefficient:
    """An exact finite sum of rational multiples of formal exp(q) atoms."""

    terms: tuple[tuple[Fraction, Fraction], ...]

    @classmethod
    def from_items(
        cls, items: Iterable[tuple[Fraction, Fraction]]
    ) -> "ExpQCoefficient":
        combined: dict[Fraction, Fraction] = {}
        for exponent, coefficient in items:
            combined[exponent] = combined.get(exponent, Fraction(0)) + coefficient
        return cls(tuple(sorted((q, c) for q, c in combined.items() if c)))

    @classmethod
    def zero(cls) -> "ExpQCoefficient":
        return cls(())

    @classmethod
    def rational(cls, value: Fraction | int) -> "ExpQCoefficient":
        coefficient = Fraction(value)
        return cls(()) if not coefficient else cls(((Fraction(0), coefficient),))

    @classmethod
    def exp_atom(cls, exponent: Fraction) -> "ExpQCoefficient":
        return cls(((exponent, Fraction(1)),))

    @property
    def is_zero(self) -> bool:
        return not self.terms

    @property
    def is_rational(self) -> bool:
        return not self.terms or all(exponent == 0 for exponent, _ in self.terms)

    def rational_value(self) -> Fraction:
        if not self.is_rational:
            raise ValueError("coefficient is not rational")
        return self.terms[0][1] if self.terms else Fraction(0)

    def __add__(self, other: "ExpQCoefficient") -> "ExpQCoefficient":
        return self.from_items((*self.terms, *other.terms))

    def __neg__(self) -> "ExpQCoefficient":
        return self.from_items((q, -c) for q, c in self.terms)

    def __sub__(self, other: "ExpQCoefficient") -> "ExpQCoefficient":
        return self + (-other)

    def __mul__(self, other: "ExpQCoefficient") -> "ExpQCoefficient":
        return self.from_items(
            (left_q + right_q, left_c * right_c)
            for left_q, left_c in self.terms
            for right_q, right_c in other.terms
        )

    def divide_rational(self, divisor: Fraction | int) -> "ExpQCoefficient":
        divisor = Fraction(divisor)
        if not divisor:
            raise ZeroDivisionError("coefficient division by zero")
        return self.from_items((q, c / divisor) for q, c in self.terms)

    def scale_rational(self, scalar: Fraction | int) -> "ExpQCoefficient":
        scalar = Fraction(scalar)
        return self.from_items((q, scalar * c) for q, c in self.terms)

    def to_text(self) -> str:
        if not self.terms:
            return "0"
        pieces: list[str] = []
        for exponent, coefficient in self.terms:
            if exponent == 0:
                term = fraction_text(abs(coefficient))
            else:
                atom = f"exp({fraction_text(exponent)})"
                magnitude = abs(coefficient)
                term = atom if magnitude == 1 else f"{fraction_text(magnitude)}*{atom}"
            if not pieces:
                pieces.append(f"-{term}" if coefficient < 0 else term)
            else:
                pieces.append((" - " if coefficient < 0 else " + ") + term)
        return "".join(pieces)


@dataclass(frozen=True)
class Budgets:
    max_nodes: int = 1024
    max_lattice_denominator: int = 24
    max_abs_power: int = 256
    max_target_weight: int = 256
    max_coefficient_operations: int = 100_000
    max_certificate_bytes: int = 65_536

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> "Budgets":
        values = {name: int(data[name]) for name in cls.__dataclass_fields__}
        return cls(**values)

    def as_dict(self) -> dict[str, int]:
        return {
            name: getattr(self, name)
            for name in self.__dataclass_fields__
        }


class EvaluationFailure(Exception):
    def __init__(self, status: str, code: str):
        super().__init__(code)
        self.status = status
        self.code = code


class Meter:
    def __init__(self, budgets: Budgets):
        self.budgets = budgets
        self.nodes = 0
        self.coefficient_operations = 0
        self.dependencies: set[tuple[str, Fraction]] = set()

    def bump_operation(self, amount: int = 1) -> None:
        self.coefficient_operations += amount
        if self.coefficient_operations > self.budgets.max_coefficient_operations:
            raise EvaluationFailure(
                "resource_exceeded", "coefficient-operation-budget-exceeded"
            )

    def visit(self, node_key: str, weight: Fraction) -> None:
        self.dependencies.add((node_key, weight))

    def dependency_summary(self) -> dict[str, object]:
        weights = sorted({weight for _, weight in self.dependencies})
        return {
            "request_count": len(self.dependencies),
            "weight_count": len(weights),
            "weights": [fraction_text(weight) for weight in weights],
        }


def without_expected(case: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in case.items() if key != "expected"}
