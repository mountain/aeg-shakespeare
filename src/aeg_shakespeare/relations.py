"""Generic relation discovery for bounded process presentations.

Linear algebra is used only as a computational backend for discovering exact
relations among process-generated expressions.  The public results are process
relations and relation kernels, not eigenspaces or benchmark-specific sectors.
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
    """A constant-coefficient process relation ``sum c_i D^i(f) = 0``."""

    expression: sp.Expr
    coefficients: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        z = symbol or sp.Symbol("D")
        return sp.expand(sum(c * z**i for i, c in enumerate(self.coefficients)))


@dataclass(frozen=True)
class RelationKernel:
    """Primitive expressions satisfying one declared process relation.

    ``coefficients`` encode ``sum c_i D^i(f) = 0``.  No interpretation such as
    frequency, spectrum, or a named physical sector is attached by the library.
    """

    coefficients: tuple[sp.Expr, ...]
    primitives: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        z = symbol or sp.Symbol("D")
        return sp.expand(sum(c * z**i for i, c in enumerate(self.coefficients)))


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
    """Represent a polynomial expression in a declared monomial basis."""

    poly = sp.Poly(sp.expand(expr), *variables)
    keys = [_monomial_key(b, variables) for b in basis]
    return sp.Matrix([poly.coeff_monomial(k) for k in keys])


def action_matrix(system: ProcessSystem, basis: Sequence[sp.Expr]) -> sp.Matrix:
    """Matrix backend for process action on a declared finite grammar.

    The basis must be closed under the represented process action.  Failure to
    close is reported rather than silently projected away.
    """

    columns: list[sp.Matrix] = []
    for item in basis:
        derived = sp.expand(system.derive(item))
        vec = coefficient_vector(derived, basis, system.assignments)
        reconstructed = sp.expand(sum(vec[i] * basis[i] for i in range(len(basis))))
        if sp.expand(reconstructed - derived) != 0:
            raise ValueError("declared basis is not closed under the process action")
        columns.append(vec)
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


def _apply_relation(
    system: ProcessSystem,
    expr: sp.Expr,
    coefficients: Sequence[sp.Expr],
) -> sp.Expr:
    orbit = system.iterate(expr, len(coefficients) - 1)
    return sp.expand(sum(c * orbit[i] for i, c in enumerate(coefficients)))


def discover_return_relation(
    system: ProcessSystem,
    expr: sp.Expr,
    max_order: int = 8,
) -> ReturnRelation | None:
    """Find the first exact constant-coefficient relation among ``D^i(expr)``."""

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
        candidates = [v for v in matrix.nullspace() if v[-1] != 0]
        if not candidates:
            continue
        v = _primitive_integer_vector(candidates[0])
        coefficients = tuple(v)
        if _apply_relation(system, expr, coefficients) != 0:
            raise AssertionError("internal relation verification failed")
        return ReturnRelation(sp.expand(expr), coefficients)
    return None


def discover_relation_kernel(
    system: ProcessSystem,
    basis: Sequence[sp.Expr],
    coefficients: Sequence[sp.Expr],
) -> RelationKernel:
    """Discover all primitives in ``span(basis)`` satisfying a process relation.

    Parameters
    ----------
    system:
        Process generator representation.
    basis:
        A finite grammar closed under ``system``.
    coefficients:
        Coefficients ``(c_0, ..., c_n)`` for the relation
        ``sum_i c_i D^i(f) = 0``.

    This is deliberately relation-generic.  Callers, tests, or downstream
    packages decide which relation families are worth searching.
    """

    if not coefficients:
        raise ValueError("relation coefficients must be non-empty")
    coeffs = tuple(sp.sympify(c) for c in coefficients)
    if all(c == 0 for c in coeffs):
        raise ValueError("the zero relation is not informative")

    A = action_matrix(system, basis)
    operator = sp.zeros(len(basis))
    power = sp.eye(len(basis))
    for coefficient in coeffs:
        operator += coefficient * power
        power = power * A

    primitives: list[sp.Expr] = []
    for raw in operator.nullspace():
        vector = _primitive_integer_vector(raw)
        expr = sp.expand(sum(vector[i] * basis[i] for i in range(len(basis))))
        if _apply_relation(system, expr, coeffs) != 0:
            raise AssertionError("relation-kernel verification failed")
        if expr not in primitives:
            primitives.append(expr)
    return RelationKernel(coefficients=coeffs, primitives=tuple(primitives))


def decompose(
    target: sp.Expr,
    primitives: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> tuple[sp.Expr, ...]:
    """Express ``target`` in a declared primitive grammar, if uniquely possible."""

    if not primitives:
        raise ValueError("primitive grammar must be non-empty")
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
