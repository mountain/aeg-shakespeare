"""Exact algebraic constraints and quotient reduction.

Many process systems are not naturally expressed on a free assignment algebra.
Rigid bodies, constrained mechanics, algebraic state models, and quotient
representations carry polynomial relations that must be preserved explicitly.

``AlgebraicConstraintSet`` is intentionally generic.  It supplies exact ideal
membership/reduction through a Groebner backend without turning any named
mechanical problem into a package abstraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Sequence

import sympy as sp


@dataclass(frozen=True)
class AlgebraicConstraintSet:
    """A polynomial quotient specified by generators of an algebraic ideal."""

    variables: tuple[sp.Symbol, ...]
    relations: tuple[sp.Expr, ...]
    order: str = "grevlex"

    def __post_init__(self) -> None:
        if not self.variables:
            raise ValueError("constraint set requires at least one variable")
        variables = tuple(self.variables)
        if len(set(variables)) != len(variables):
            raise ValueError("constraint variables must be distinct")
        relations = tuple(sp.expand(sp.sympify(relation)) for relation in self.relations)
        if any(relation == 0 for relation in relations):
            relations = tuple(relation for relation in relations if relation != 0)
        object.__setattr__(self, "variables", variables)
        object.__setattr__(self, "relations", relations)

    @cached_property
    def groebner_basis(self) -> sp.GroebnerBasis | None:
        if not self.relations:
            return None
        try:
            return sp.groebner(self.relations, *self.variables, order=self.order)
        except sp.PolynomialError as exc:
            raise ValueError("constraints must be polynomial in the declared variables") from exc

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        """Return the exact normal remainder modulo the constraint ideal."""

        expr = sp.expand(sp.sympify(expr))
        if self.groebner_basis is None:
            return expr
        try:
            _quotients, remainder = self.groebner_basis.reduce(expr)
        except sp.PolynomialError as exc:
            raise ValueError("expression must be polynomial in the declared variables") from exc
        return sp.expand(remainder)

    def contains(self, expr: sp.Expr) -> bool:
        """Whether ``expr = 0`` follows from the declared algebraic relations."""

        return self.reduce(expr) == 0

    def equivalent(self, left: sp.Expr, right: sp.Expr) -> bool:
        """Whether two expressions agree in the quotient algebra."""

        return self.contains(sp.expand(sp.sympify(left) - sp.sympify(right)))

    def adjoin(self, *relations: sp.Expr) -> "AlgebraicConstraintSet":
        """Return the quotient obtained by adding more exact relations."""

        return AlgebraicConstraintSet(
            variables=self.variables,
            relations=self.relations + tuple(relations),
            order=self.order,
        )


def constraint_prolongation(
    derive,
    relation: sp.Expr,
    *,
    order: int,
) -> tuple[sp.Expr, ...]:
    """Return ``relation, D relation, ..., D^order relation``.

    ``derive`` is caller-supplied so this utility can be used with
    ``ProcessSystem``, ``ProcessFrame`` generators, or future process backends.
    No dynamics-specific multiplier model is assumed here.
    """

    if order < 0:
        raise ValueError("order must be non-negative")
    values = [sp.expand(sp.sympify(relation))]
    for _ in range(order):
        values.append(sp.expand(sp.sympify(derive(values[-1]))))
    return tuple(values)
