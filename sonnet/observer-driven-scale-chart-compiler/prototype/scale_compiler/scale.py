"""Scale, observer, residual, and finite asymptotic-series types.

The convention is ``N -> +infinity`` and ``Scale(p) == N**p``.  This first
prototype intentionally handles the polynomial layer exactly and represents
log/exp structure in the expression IR.  Unsupported exponential growth is a
typed failure rather than a guessed answer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Iterable, Mapping

import sympy as sp


def _fraction(value: int | Fraction | sp.Rational) -> Fraction:
    if isinstance(value, float):
        raise TypeError("Scale requires an exact int, Fraction, or SymPy Rational")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, sp.Rational):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


@dataclass(frozen=True, order=True)
class Scale:
    """A polynomial asymptotic scale ``N**power``."""

    power: Fraction

    def __init__(self, power: int | Fraction | sp.Rational):
        object.__setattr__(self, "power", _fraction(power))

    def __add__(self, other: "Scale") -> "Scale":
        return Scale(self.power + other.power)

    def __sub__(self, other: "Scale") -> "Scale":
        return Scale(self.power - other.power)

    def __str__(self) -> str:
        return f"N^{self.power}"


@dataclass(frozen=True)
class Observer:
    """Declares what the caller intends to observe and certify."""

    visible_at_or_above: Scale = field(default_factory=lambda: Scale(0))
    require_remainder_below: Scale = field(default_factory=lambda: Scale(-2))
    initial_taylor_order: int = 2
    max_taylor_order: int = 32
    max_input_nodes: int = 256
    max_live_terms: int = 4096

    def __post_init__(self) -> None:
        if self.initial_taylor_order < 1:
            raise ValueError("initial_taylor_order must be positive")
        if self.max_taylor_order < self.initial_taylor_order:
            raise ValueError("max_taylor_order must not be smaller than initial")
        if self.max_input_nodes < 1 or self.max_live_terms < 1:
            raise ValueError("resource budgets must be positive")

    def is_visible(self, scale: Scale) -> bool:
        return scale >= self.visible_at_or_above


@dataclass(frozen=True)
class Residual:
    source: str
    order: Scale
    visible: bool
    reason: str


@dataclass(frozen=True)
class VisibilityEvent:
    source: str
    hidden_input: Scale
    amplifier: Scale
    output_effect: Scale
    rescued: bool
    explanation: str


@dataclass(frozen=True)
class Obligation:
    """A backward precision/visibility obligation on one child edge."""

    path: str
    operator: str
    child: str
    parent_required: Scale
    child_required: Scale
    rule: str


@dataclass(frozen=True)
class Series:
    """Finite generalized power series with an optional big-O remainder."""

    terms: Mapping[Fraction, sp.Expr]
    remainder: Scale | None = None

    def __post_init__(self) -> None:
        cleaned: dict[Fraction, sp.Expr] = {}
        for power, coefficient in self.terms.items():
            p = _fraction(power)
            c = sp.simplify(coefficient)
            if c != 0:
                cleaned[p] = sp.simplify(cleaned.get(p, 0) + c)
        cleaned = {p: c for p, c in cleaned.items() if sp.simplify(c) != 0}
        object.__setattr__(self, "terms", cleaned)

    @classmethod
    def constant(cls, value: object) -> "Series":
        coefficient = sp.sympify(value)
        return cls({Fraction(0): coefficient} if coefficient != 0 else {})

    @classmethod
    def monomial(cls, power: int | Fraction, coefficient: object = 1) -> "Series":
        return cls({Fraction(power): sp.sympify(coefficient)})

    @property
    def leading_scale(self) -> Scale | None:
        if not self.terms:
            return self.remainder
        return Scale(max(self.terms))

    @property
    def constant_coefficient(self) -> sp.Expr:
        return self.terms.get(Fraction(0), sp.S.Zero)

    @property
    def term_count(self) -> int:
        return len(self.terms)

    def nonconstant(self) -> "Series":
        return Series({p: c for p, c in self.terms.items() if p != 0}, self.remainder)

    def add(self, other: "Series") -> "Series":
        terms = dict(self.terms)
        for power, coefficient in other.terms.items():
            terms[power] = sp.simplify(terms.get(power, 0) + coefficient)
        return Series(terms, _max_remainder(self.remainder, other.remainder))

    def scale_by(self, coefficient: object) -> "Series":
        c = sp.sympify(coefficient)
        if c == 0:
            return Series.constant(0)
        return Series({p: sp.simplify(c * a) for p, a in self.terms.items()}, self.remainder)

    def mul(self, other: "Series") -> "Series":
        terms: dict[Fraction, sp.Expr] = {}
        for left_power, left_coefficient in self.terms.items():
            for right_power, right_coefficient in other.terms.items():
                power = left_power + right_power
                terms[power] = sp.simplify(
                    terms.get(power, 0) + left_coefficient * right_coefficient
                )

        candidates: list[Scale] = []
        left_lead = self.leading_scale
        right_lead = other.leading_scale
        if self.remainder is not None and right_lead is not None:
            candidates.append(self.remainder + right_lead)
        if other.remainder is not None and left_lead is not None:
            candidates.append(other.remainder + left_lead)
        if self.remainder is not None and other.remainder is not None:
            candidates.append(self.remainder + other.remainder)
        remainder = max(candidates) if candidates else None
        return Series(terms, remainder)

    def truncate_below(self, threshold: Scale) -> tuple["Series", Scale | None]:
        kept: dict[Fraction, sp.Expr] = {}
        dropped: list[Scale] = []
        for power, coefficient in self.terms.items():
            scale = Scale(power)
            if scale >= threshold:
                kept[power] = coefficient
            else:
                dropped.append(scale)
        remainder = self.remainder
        if dropped:
            remainder = _max_remainder(remainder, max(dropped))
        return Series(kept, remainder), (max(dropped) if dropped else None)

    def ordered_terms(self) -> tuple[tuple[Scale, sp.Expr], ...]:
        return tuple(
            (Scale(power), self.terms[power])
            for power in sorted(self.terms, reverse=True)
        )


def _max_remainder(left: Scale | None, right: Scale | None) -> Scale | None:
    if left is None:
        return right
    if right is None:
        return left
    return max(left, right)


def max_scale(scales: Iterable[Scale]) -> Scale | None:
    values = list(scales)
    return max(values) if values else None
