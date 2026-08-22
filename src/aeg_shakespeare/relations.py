"""Generic relation discovery for bounded process presentations.

Linear algebra is used only as a computational backend for discovering exact
relations among process-generated expressions. The public results are process
relations, relation kernels, and decompositions of finite process grammars; no
spectral interpretation is required by the API.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd
from typing import Sequence

import sympy as sp

from .process.local import ProcessSystem


@dataclass(frozen=True)
class ProcessPolynomialRelation:
    """A constant-coefficient process relation ``sum c_i D^i = 0``.

    Coefficients are stored in ascending process order: ``(c_0, ..., c_n)``.
    The relation is an algebraic certificate; callers may interpret it further,
    but Shakespeare does not attach eigenvalue/frequency semantics to it.
    """

    coefficients: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        z = symbol or sp.Symbol("D")
        return sp.expand(sum(c * z**i for i, c in enumerate(self.coefficients)))


@dataclass(frozen=True)
class ReturnRelation:
    """A process polynomial relation attached to one expression."""

    expression: sp.Expr
    coefficients: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    @property
    def relation(self) -> ProcessPolynomialRelation:
        return ProcessPolynomialRelation(self.coefficients)

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        return self.relation.as_expr(symbol)


@dataclass(frozen=True)
class RelationKernel:
    """Primitive expressions satisfying one discovered or declared relation."""

    coefficients: tuple[sp.Expr, ...]
    primitives: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    @property
    def relation(self) -> ProcessPolynomialRelation:
        return ProcessPolynomialRelation(self.coefficients)

    def as_expr(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        return self.relation.as_expr(symbol)


@dataclass(frozen=True)
class RelationDecomposition:
    """Template-free relation decomposition of a finite closed grammar."""

    global_relation: ProcessPolynomialRelation
    components: tuple[RelationKernel, ...]
    complete: bool

    @property
    def primitives(self) -> tuple[sp.Expr, ...]:
        return tuple(
            primitive
            for component in self.components
            for primitive in component.primitives
        )


def _normalize_coordinate_vector(v: Sequence[sp.Expr] | sp.Matrix) -> sp.Matrix:
    """Normalize a coordinate vector without changing its length."""
    values = [sp.simplify(sp.sympify(value)) for value in list(v)]
    if not values or all(value == 0 for value in values):
        return sp.Matrix(values)

    if all(value.is_Rational is True for value in values):
        rationals = [sp.Rational(value) for value in values]
        denominators = [q.q for q in rationals]
        lcm = sp.ilcm(*denominators) if denominators else 1
        ints = [int(q * lcm) for q in rationals]
        nonzero = [abs(value) for value in ints if value]
        common = reduce(gcd, nonzero) if nonzero else 1
        ints = [value // common for value in ints]
        first = next((value for value in ints if value), 1)
        if first < 0:
            ints = [-value for value in ints]
        return sp.Matrix([sp.Integer(value) for value in ints])

    pivot = next(value for value in values if value != 0)
    return sp.Matrix([sp.simplify(value / pivot) for value in values])


def _normalize_relation_coefficients(
    coefficients: Sequence[sp.Expr] | sp.Matrix,
) -> tuple[sp.Expr, ...]:
    """Normalize a relation up to nonzero scalar multiplication."""
    values = [sp.simplify(sp.sympify(value)) for value in list(coefficients)]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    if not values or all(value == 0 for value in values):
        raise ValueError("the zero relation is not informative")

    if all(value.is_Rational is True for value in values):
        return tuple(_normalize_coordinate_vector(values))

    leading = values[-1]
    return tuple(sp.simplify(value / leading) for value in values)


def _ambient_monomials(
    expressions: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> list[tuple[int, ...]]:
    monomials: set[tuple[int, ...]] = set()
    for expression in expressions:
        poly = sp.Poly(sp.expand(expression), *variables)
        monomials.update(poly.monoms())
    return sorted(monomials, reverse=True)


def _ambient_column(
    expr: sp.Expr,
    monomials: Sequence[tuple[int, ...]],
    variables: Sequence[sp.Symbol],
) -> sp.Matrix:
    poly = sp.Poly(sp.expand(expr), *variables)
    return sp.Matrix([poly.coeff_monomial(monomial) for monomial in monomials])


def coefficient_vector(
    expr: sp.Expr,
    basis: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Return exact coordinates of ``expr`` in an arbitrary polynomial basis."""
    basis = tuple(sp.expand(sp.sympify(item)) for item in basis)
    if not basis:
        raise ValueError("basis must be non-empty")

    monomials = _ambient_monomials((*basis, sp.expand(sp.sympify(expr))), variables)
    matrix = sp.Matrix.hstack(
        *[_ambient_column(item, monomials, variables) for item in basis]
    )
    if matrix.rank() < len(basis):
        raise ValueError("basis expressions are linearly dependent")

    target = _ambient_column(expr, monomials, variables)
    solution = sp.linsolve((matrix, target))
    if solution is sp.EmptySet or not solution:
        raise ValueError("expression is not in the supplied basis span")
    row = next(iter(solution))
    return sp.Matrix([sp.simplify(value) for value in row])


def action_matrix(system: ProcessSystem, basis: Sequence[sp.Expr]) -> sp.Matrix:
    """Matrix backend for process action on a declared finite grammar."""
    basis = tuple(basis)
    columns: list[sp.Matrix] = []
    for item in basis:
        derived = sp.expand(system.derive(item))
        try:
            vector = coefficient_vector(derived, basis, system.assignments)
        except ValueError as exc:
            raise ValueError(
                "declared basis is not closed under the process action"
            ) from exc
        columns.append(vector)
    return sp.Matrix.hstack(*columns)


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
        columns = [
            sp.Matrix([polys[i].coeff_monomial(m) for m in monomial_list])
            for i in range(order + 1)
        ]
        matrix = sp.Matrix.hstack(*columns)
        candidates = [
            vector
            for vector in matrix.nullspace()
            if sp.simplify(vector[-1]) != 0
        ]
        if not candidates:
            continue
        coefficients = _normalize_relation_coefficients(candidates[0])
        if sp.simplify(_apply_relation(system, expr, coefficients)) != 0:
            raise AssertionError("internal relation verification failed")
        return ReturnRelation(sp.expand(expr), coefficients)
    return None


def discover_operator_relation(
    operator: sp.Matrix,
    max_order: int | None = None,
) -> ProcessPolynomialRelation | None:
    """Discover the shortest polynomial relation satisfied by a finite action."""
    operator = sp.Matrix(operator)
    if operator.rows != operator.cols:
        raise ValueError("operator must be square")
    if operator.rows == 0:
        raise ValueError("operator must be non-empty")

    size = operator.rows
    bound = size if max_order is None else min(max_order, size)
    if bound < 1:
        return None

    powers = [sp.eye(size)]
    columns = [sp.Matrix(list(powers[0]))]
    for _order in range(1, bound + 1):
        powers.append(sp.expand(powers[-1] * operator))
        columns.append(sp.Matrix(list(powers[-1])))
        matrix = sp.Matrix.hstack(*columns)
        candidates = [
            vector
            for vector in matrix.nullspace()
            if sp.simplify(vector[-1]) != 0
        ]
        if not candidates:
            continue

        coefficients = _normalize_relation_coefficients(candidates[0])
        certificate = sp.zeros(size)
        for index, coefficient in enumerate(coefficients):
            certificate += coefficient * powers[index]
        certificate = certificate.applyfunc(sp.simplify)
        if certificate != sp.zeros(size):
            raise AssertionError("operator-relation verification failed")
        return ProcessPolynomialRelation(coefficients)
    return None


def factor_process_relation(
    relation: ProcessPolynomialRelation,
) -> tuple[ProcessPolynomialRelation, ...]:
    """Factor a process relation into pairwise-coprime primary factors."""
    symbol = sp.Symbol("_D")
    expression = relation.as_expr(symbol)
    _unit, factors = sp.factor_list(expression, symbol)
    if not factors:
        return (relation,)

    result: list[ProcessPolynomialRelation] = []
    for factor, multiplicity in factors:
        primary = sp.Poly(sp.expand(factor**multiplicity), symbol)
        coefficients = tuple(reversed(primary.all_coeffs()))
        result.append(
            ProcessPolynomialRelation(_normalize_relation_coefficients(coefficients))
        )
    return tuple(result)


def discover_relation_kernel(
    system: ProcessSystem,
    basis: Sequence[sp.Expr],
    coefficients: Sequence[sp.Expr],
) -> RelationKernel:
    """Discover all primitives in ``span(basis)`` satisfying a process relation."""
    coefficients = _normalize_relation_coefficients(coefficients)
    action = action_matrix(system, basis)
    operator = sp.zeros(len(basis))
    power = sp.eye(len(basis))
    for coefficient in coefficients:
        operator += coefficient * power
        power = power * action

    primitives: list[sp.Expr] = []
    for raw in operator.nullspace():
        vector = _normalize_coordinate_vector(raw)
        expr = sp.expand(sum(vector[i] * basis[i] for i in range(len(basis))))
        if sp.simplify(_apply_relation(system, expr, coefficients)) != 0:
            raise AssertionError("relation-kernel verification failed")
        if expr not in primitives:
            primitives.append(expr)
    return RelationKernel(coefficients=coefficients, primitives=tuple(primitives))


def discover_relation_decomposition(
    system: ProcessSystem,
    basis: Sequence[sp.Expr],
    max_order: int | None = None,
) -> RelationDecomposition | None:
    """Discover relation factors and their primitive subgrammars jointly."""
    basis = tuple(basis)
    if not basis:
        raise ValueError("basis must be non-empty")

    action = action_matrix(system, basis)
    global_relation = discover_operator_relation(action, max_order=max_order)
    if global_relation is None:
        return None

    components = tuple(
        discover_relation_kernel(system, basis, factor.coefficients)
        for factor in factor_process_relation(global_relation)
    )
    primitives = tuple(
        primitive
        for component in components
        for primitive in component.primitives
    )

    complete = False
    if primitives:
        coordinate_columns = [
            coefficient_vector(primitive, basis, system.assignments)
            for primitive in primitives
        ]
        complete = sp.Matrix.hstack(*coordinate_columns).rank() == len(basis)

    return RelationDecomposition(
        global_relation=global_relation,
        components=components,
        complete=complete,
    )


def decompose(
    target: sp.Expr,
    primitives: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> tuple[sp.Expr, ...]:
    """Express ``target`` uniquely in a supplied primitive grammar."""
    vector = coefficient_vector(target, primitives, variables)
    return tuple(sp.simplify(value) for value in vector)
