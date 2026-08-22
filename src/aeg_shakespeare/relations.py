"""Relation discovery for bounded process presentations.

The routines in this module use linear algebra as a search backend for short
process relations. The returned objects are explicit process recurrences; the
linear representation is not treated as the ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd
from typing import Sequence

import sympy as sp

from .core import ProcessSystem


@dataclass(frozen=True)
class ReturnRelation:
    """A constant-coefficient return relation ``sum c_i D^i(f) = 0``."""

    expression: sp.Expr
    coefficients: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        """Return the polynomial in a formal process symbol."""
        z = symbol or sp.Symbol("D")
        return sp.expand(sum(c * z**i for i, c in enumerate(self.coefficients)))


@dataclass(frozen=True)
class ReturnSector:
    """A subgrammar satisfying ``D^2 f + rate^2 f = 0``."""

    rate: int
    primitives: tuple[sp.Expr, ...]


def _monomial_key(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> tuple[int, ...]:
    poly = sp.Poly(expr, *variables)
    monoms = poly.monoms()
    if len(monoms) != 1:
        raise ValueError(f"expected monomial, got {expr}")
    return monoms[0]


def coefficient_vector(
    expr: sp.Expr,
    basis: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> sp.Matrix:
    poly = sp.Poly(sp.expand(expr), *variables)
    keys = [_monomial_key(b, variables) for b in basis]
    return sp.Matrix([poly.coeff_monomial(k) for k in keys])


def action_matrix(system: ProcessSystem, basis: Sequence[sp.Expr]) -> sp.Matrix:
    """Matrix backend for the process action on a declared finite grammar."""
    columns = [coefficient_vector(system.derive(b), basis, system.assignments) for b in basis]
    return sp.Matrix.hstack(*columns)


def _primitive_integer_vector(v: sp.Matrix) -> sp.Matrix:
    rationals = [sp.Rational(x) for x in v]
    denominators = [q.q for q in rationals]
    lcm = sp.ilcm(*denominators) if denominators else 1
    ints = [int(q * lcm) for q in rationals]
    nonzero = [abs(i) for i in ints if i]
    common = reduce(gcd, nonzero) if nonzero else 1
    ints = [i // common for i in ints]
    first = next((i for i in ints if i), 1)
    if first < 0:
        ints = [-i for i in ints]
    return sp.Matrix(ints)


def discover_return_relation(
    system: ProcessSystem,
    expr: sp.Expr,
    max_order: int = 8,
) -> ReturnRelation | None:
    """Find the first constant-coefficient relation among ``D^i(expr)``.

    The search is bounded and exact. It is a process-history recurrence finder,
    with Krylov/nullspace computation used only as the backend.
    """
    orbit = system.iterate(expr, max_order)
    monomials: set[tuple[int, ...]] = set()
    polys: list[sp.Poly] = []
    for item in orbit:
        poly = sp.Poly(item, *system.assignments)
        polys.append(poly)
        monomials.update(poly.monoms())
    monomial_list = sorted(monomials, reverse=True)

    for order in range(1, max_order + 1):
        cols = [
            sp.Matrix([polys[i].coeff_monomial(m) for m in monomial_list])
            for i in range(order + 1)
        ]
        matrix = sp.Matrix.hstack(*cols)
        nullspace = matrix.nullspace()
        if not nullspace:
            continue
        candidates = [v for v in nullspace if v[-1] != 0]
        if not candidates:
            continue
        v = _primitive_integer_vector(candidates[0])
        relation = sp.expand(sum(v[i] * orbit[i] for i in range(order + 1)))
        if relation != 0:
            raise AssertionError("internal relation verification failed")
        return ReturnRelation(sp.expand(expr), tuple(v))
    return None


def discover_quadratic_return_sectors(
    system: ProcessSystem,
    basis: Sequence[sp.Expr],
    max_rate: int = 8,
) -> list[ReturnSector]:
    """Find low-cost subgrammars satisfying ``D^2 f + k^2 f = 0``.

    This deliberately searches *return relations*, not eigenvectors. A matrix
    nullspace is used as an implementation technique.
    """
    A = action_matrix(system, basis)
    sectors: list[ReturnSector] = []
    for rate in range(1, max_rate + 1):
        kernel = (A * A + rate**2 * sp.eye(len(basis))).nullspace()
        if not kernel:
            continue
        primitives: list[sp.Expr] = []
        for raw in kernel:
            v = _primitive_integer_vector(raw)
            expr = sp.expand(sum(v[i] * basis[i] for i in range(len(basis))))
            if expr not in primitives:
                primitives.append(expr)
        sectors.append(ReturnSector(rate=rate, primitives=tuple(primitives)))
    return sectors


def decompose(
    target: sp.Expr,
    primitives: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> tuple[sp.Expr, ...]:
    """Express ``target`` in a declared primitive grammar, if possible."""
    monomials: set[tuple[int, ...]] = set()
    all_exprs = list(primitives) + [target]
    polys = [sp.Poly(sp.expand(e), *variables) for e in all_exprs]
    for poly in polys:
        monomials.update(poly.monoms())
    monomial_list = sorted(monomials, reverse=True)
    M = sp.Matrix.hstack(
        *[
            sp.Matrix([poly.coeff_monomial(m) for m in monomial_list])
            for poly in polys[:-1]
        ]
    )
    b = sp.Matrix([polys[-1].coeff_monomial(m) for m in monomial_list])
    solution = sp.linsolve((M, b))
    if solution is sp.EmptySet or not solution:
        raise ValueError("target is not in the supplied primitive grammar")
    row = next(iter(solution))
    if any(getattr(value, "free_symbols", set()) for value in row):
        raise ValueError("decomposition is not unique")
    return tuple(sp.simplify(value) for value in row)
