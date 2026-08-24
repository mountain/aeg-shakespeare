"""Exact depth-two A/M presentation census and monotonicity certificates."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement
from math import comb

import sympy as sp


@dataclass(frozen=True)
class AMPresentation:
    operation: str
    arguments: tuple["AMPresentation", ...] = ()
    atom: sp.Expr | None = None

    @classmethod
    def constant(cls, value: int) -> "AMPresentation":
        return cls("constant", atom=sp.Integer(value))

    @classmethod
    def coordinate(cls) -> "AMPresentation":
        return cls("coordinate")

    @property
    def depth(self) -> int:
        if not self.arguments:
            return 0
        return 1 + max(argument.depth for argument in self.arguments)

    def evaluate(self, coordinate: sp.Symbol) -> sp.Expr:
        if self.operation == "constant":
            return sp.sympify(self.atom)
        if self.operation == "coordinate":
            return coordinate
        left = self.arguments[0].evaluate(coordinate)
        right = self.arguments[1].evaluate(coordinate)
        if self.operation == "add":
            return sp.expand(left + right)
        if self.operation == "mul":
            return sp.expand(left * right)
        raise ValueError(f"unknown A/M operation: {self.operation}")


@dataclass(frozen=True)
class MonotonicityCertificate:
    presentation: sp.Expr
    derivative: sp.Expr
    left_value: sp.Expr
    right_value: sp.Expr
    derivative_root_count: int
    sample_value: sp.Expr

    @property
    def certified(self) -> bool:
        return (
            self.derivative != 0
            and self.left_value != 0
            and self.right_value != 0
            and self.derivative_root_count == 0
            and self.sample_value.is_positive is True
        )


@dataclass(frozen=True)
class PresentationCensus:
    exact_depth_counts: tuple[int, ...]
    literal_count: int
    semantic_presentations: tuple[sp.Expr, ...]
    monotone_certificates: tuple[MonotonicityCertificate, ...]


def literal_am_grammar(max_depth: int = 2) -> tuple[AMPresentation, ...]:
    """Enumerate commutative literal trees without semantic quotienting."""

    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    exact_levels: list[list[AMPresentation]] = [[
        AMPresentation.constant(-1),
        AMPresentation.constant(0),
        AMPresentation.constant(1),
        AMPresentation.coordinate(),
    ]]
    cumulative = list(exact_levels[0])
    for depth in range(1, max_depth + 1):
        level: list[AMPresentation] = []
        for left, right in combinations_with_replacement(cumulative, 2):
            if max(left.depth, right.depth) != depth - 1:
                continue
            level.extend((
                AMPresentation("add", (left, right)),
                AMPresentation("mul", (left, right)),
            ))
        exact_levels.append(level)
        cumulative.extend(level)
    return tuple(cumulative)


def literal_depth_counts(max_depth: int) -> tuple[int, ...]:
    """Count literal commutative trees exactly without materializing them."""

    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    exact = [4]
    cumulative_before_previous = 0
    cumulative_previous = 4
    for _depth in range(1, max_depth + 1):
        count = 2 * (
            comb(cumulative_previous + 1, 2)
            - comb(cumulative_before_previous + 1, 2)
        )
        exact.append(count)
        cumulative_before_previous = cumulative_previous
        cumulative_previous += count
    return tuple(exact)


def semantic_am_grammar(max_depth: int) -> tuple[sp.Expr, ...]:
    """Complete exact semantic closure using one representative per value."""

    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    u = sp.Symbol("u", real=True)
    semantic = {sp.Integer(-1), sp.Integer(0), sp.Integer(1), u}
    for _depth in range(1, max_depth + 1):
        basis = tuple(semantic)
        generated: set[sp.Expr] = set()
        for left, right in combinations_with_replacement(basis, 2):
            generated.add(sp.expand(left + right))
            generated.add(sp.expand(left * right))
        semantic.update(generated)
    return tuple(sorted(semantic, key=sp.srepr))


def certify_strict_increase(
    presentation: sp.Expr,
    coordinate: sp.Symbol,
) -> MonotonicityCertificate:
    """Certify ``h'(u)>0`` on the closed rational interval ``[-1,1]``."""

    derivative = sp.expand(sp.diff(presentation, coordinate))
    if derivative == 0:
        root_count = 0
    else:
        polynomial = sp.Poly(derivative, coordinate, domain=sp.QQ)
        root_count = int(polynomial.count_roots(-1, 1))
    return MonotonicityCertificate(
        presentation=sp.expand(presentation),
        derivative=derivative,
        left_value=sp.expand(derivative.subs(coordinate, -1)),
        right_value=sp.expand(derivative.subs(coordinate, 1)),
        derivative_root_count=root_count,
        sample_value=sp.expand(derivative.subs(coordinate, 0)),
    )


def depth_two_presentation_census() -> PresentationCensus:
    coordinate = sp.Symbol("u", real=True)
    literal = literal_am_grammar(max_depth=2)
    exact_depth_counts = tuple(
        sum(presentation.depth == depth for presentation in literal)
        for depth in range(3)
    )
    semantic = {
        sp.expand(presentation.evaluate(coordinate))
        for presentation in literal
    }
    ordered = tuple(sorted(semantic, key=sp.srepr))
    certificates = tuple(
        certificate
        for presentation in ordered
        if (certificate := certify_strict_increase(presentation, coordinate)).certified
    )
    return PresentationCensus(
        exact_depth_counts=exact_depth_counts,
        literal_count=len(literal),
        semantic_presentations=ordered,
        monotone_certificates=certificates,
    )


def depth_three_presentation_census() -> PresentationCensus:
    """Execute the frozen semantic depth-three enlargement."""

    coordinate = sp.Symbol("u", real=True)
    ordered = semantic_am_grammar(3)
    certificates = tuple(
        certificate
        for presentation in ordered
        if (certificate := certify_strict_increase(presentation, coordinate)).certified
    )
    counts = literal_depth_counts(3)
    return PresentationCensus(
        exact_depth_counts=counts,
        literal_count=sum(counts),
        semantic_presentations=ordered,
        monotone_certificates=certificates,
    )


__all__ = [
    "AMPresentation",
    "MonotonicityCertificate",
    "PresentationCensus",
    "certify_strict_increase",
    "depth_two_presentation_census",
    "depth_three_presentation_census",
    "literal_depth_counts",
    "literal_am_grammar",
    "semantic_am_grammar",
]
