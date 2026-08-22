"""Bounded polynomial discovery for process observables, invariants, and quotients.

Mathematical pressure
---------------------
The first Shakespeare layers can preserve ordered histories, exact constraints,
finite grammars, and presentation costs once a useful representation has been
proposed. A remaining gap appears earlier: classical analysis often hands the
solver a good observable or first integral before the real calculation begins.

This module provides a deliberately small exact backend for removing part of
that prior choice. It searches a bounded polynomial observer grammar, discovers
first integrals as null directions of the represented process modulo declared
constraints, and eliminates source assignments to expose exact relations among
chosen process observables.

The polynomial grammar is a search proposal language, not a claim that every
useful observer is polynomial. Likewise Groebner elimination and exact linear
algebra are discovery/certificate backends rather than Shakespeare's ontology
of process equality.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import sympy as sp

from ..core import homogeneous_monomials
from ..presentation.constraints import AlgebraicConstraintSet
from ..process.local import ProcessSystem


def _polynomial_dict(
    expr: sp.Expr,
    variables: Sequence[sp.Symbol],
) -> dict[tuple[int, ...], sp.Expr]:
    try:
        return sp.Poly(
            sp.expand(sp.sympify(expr)),
            *variables,
            domain="EX",
        ).as_dict()
    except sp.PolynomialError as exc:
        raise ValueError(
            "discovery expressions must be polynomial in the declared variables"
        ) from exc


def _coefficient_matrix(
    expressions: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> sp.Matrix:
    dictionaries = [_polynomial_dict(expression, variables) for expression in expressions]
    monomials = sorted(
        set().union(*(set(dictionary) for dictionary in dictionaries)),
        reverse=True,
    )
    if not monomials:
        return sp.zeros(0, len(expressions))
    return sp.Matrix(
        [
            [dictionary.get(monomial, sp.S.Zero) for dictionary in dictionaries]
            for monomial in monomials
        ]
    )


def _independent_polynomials(
    expressions: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> tuple[sp.Expr, ...]:
    basis: list[sp.Expr] = []
    rank = 0
    for expression in expressions:
        expression = sp.expand(sp.sympify(expression))
        if expression == 0:
            continue
        candidate = basis + [expression]
        candidate_rank = int(_coefficient_matrix(candidate, variables).rank())
        if candidate_rank > rank:
            basis.append(expression)
            rank = candidate_rank
    return tuple(basis)


@dataclass(frozen=True)
class PolynomialObserverBasis:
    expressions: tuple[sp.Expr, ...]
    max_degree: int
    raw_candidate_count: int
    quotient_reduced: bool

    def __post_init__(self) -> None:
        if self.max_degree < 0:
            raise ValueError("max_degree must be non-negative")
        if self.raw_candidate_count < len(self.expressions):
            raise ValueError(
                "raw_candidate_count cannot be smaller than the retained basis"
            )


def generate_polynomial_observer_basis(
    assignments: Sequence[sp.Symbol],
    *,
    max_degree: int,
    constraints: AlgebraicConstraintSet | None = None,
    include_constant: bool = False,
) -> PolynomialObserverBasis:
    if max_degree < 0:
        raise ValueError("max_degree must be non-negative")
    assignments = tuple(assignments)
    if not assignments and max_degree > 0:
        raise ValueError("at least one assignment is required for positive degree")

    if constraints is not None:
        unknown = set(assignments) - set(constraints.variables)
        if unknown:
            raise ValueError(
                "assignments missing from constraint variables: "
                f"{sorted(map(str, unknown))}"
            )
        coordinate_variables = constraints.variables
    else:
        coordinate_variables = assignments

    raw: list[sp.Expr] = []
    start_degree = 0 if include_constant else 1
    for degree in range(start_degree, max_degree + 1):
        raw.extend(homogeneous_monomials(assignments, degree))

    reduced = [
        constraints.reduce(expression)
        if constraints is not None
        else sp.expand(expression)
        for expression in raw
    ]
    independent = _independent_polynomials(reduced, coordinate_variables)
    return PolynomialObserverBasis(
        expressions=independent,
        max_degree=max_degree,
        raw_candidate_count=len(raw),
        quotient_reduced=constraints is not None,
    )


@dataclass(frozen=True)
class PolynomialInvariant:
    expression: sp.Expr
    coordinates: tuple[sp.Expr, ...]
    derivative_remainder: sp.Expr

    @property
    def certified(self) -> bool:
        return sp.expand(self.derivative_remainder) == 0


@dataclass(frozen=True)
class PolynomialInvariantDiscovery:
    observer_basis: PolynomialObserverBasis
    invariants: tuple[PolynomialInvariant, ...]
    derivative_rank: int

    @property
    def nullity(self) -> int:
        return len(self.observer_basis.expressions) - self.derivative_rank


def discover_polynomial_invariants(
    system: ProcessSystem,
    *,
    constraints: AlgebraicConstraintSet | None = None,
    max_degree: int,
    include_constant: bool = True,
) -> PolynomialInvariantDiscovery:
    basis = generate_polynomial_observer_basis(
        system.assignments,
        max_degree=max_degree,
        constraints=constraints,
        include_constant=include_constant,
    )
    coordinate_variables = constraints.variables if constraints is not None else system.assignments

    derivatives = tuple(
        constraints.reduce(system.derive(expression))
        if constraints is not None
        else sp.expand(system.derive(expression))
        for expression in basis.expressions
    )
    derivative_matrix = _coefficient_matrix(derivatives, coordinate_variables)
    assignment_set = set(system.assignments)

    invariants: list[PolynomialInvariant] = []
    for vector in derivative_matrix.nullspace():
        coordinates = tuple(sp.simplify(value) for value in vector)
        expression = sp.expand(
            sum(
                coefficient * basis_expression
                for coefficient, basis_expression in zip(coordinates, basis.expressions)
            )
        )
        reduced_expression = constraints.reduce(expression) if constraints is not None else expression
        if reduced_expression.free_symbols.isdisjoint(assignment_set):
            continue
        derivative_remainder = (
            constraints.reduce(system.derive(expression))
            if constraints is not None
            else sp.expand(system.derive(expression))
        )
        invariants.append(
            PolynomialInvariant(
                expression=sp.factor(reduced_expression),
                coordinates=coordinates,
                derivative_remainder=sp.factor(derivative_remainder),
            )
        )

    return PolynomialInvariantDiscovery(
        observer_basis=basis,
        invariants=tuple(invariants),
        derivative_rank=int(derivative_matrix.rank()),
    )


@dataclass(frozen=True)
class ObservableRelation:
    relation: sp.Expr
    pullback_remainder: sp.Expr

    @property
    def certified(self) -> bool:
        return sp.expand(self.pullback_remainder) == 0


@dataclass(frozen=True)
class ObservableQuotient:
    symbols: tuple[sp.Symbol, ...]
    observables: tuple[sp.Expr, ...]
    parameters: tuple[sp.Symbol, ...]
    eliminated_variables: tuple[sp.Symbol, ...]
    relations: tuple[ObservableRelation, ...]

    @property
    def complete_certificates(self) -> bool:
        return all(relation.certified for relation in self.relations)


def discover_observable_relations(
    observables: Sequence[sp.Expr],
    symbols: Sequence[sp.Symbol],
    *,
    constraints: AlgebraicConstraintSet,
    source_variables: Sequence[sp.Symbol],
    parameters: Sequence[sp.Symbol] = (),
) -> ObservableQuotient:
    observables = tuple(sp.expand(sp.sympify(item)) for item in observables)
    symbols = tuple(symbols)
    source_variables = tuple(source_variables)
    parameters = tuple(parameters)

    if not observables or len(observables) != len(symbols):
        raise ValueError("observables and symbols must be non-empty and have equal length")
    if len(set(symbols)) != len(symbols):
        raise ValueError("observable symbols must be distinct")
    if len(set(source_variables)) != len(source_variables):
        raise ValueError("source variables must be distinct")
    if len(set(parameters)) != len(parameters):
        raise ValueError("parameters must be distinct")

    constraint_variables = set(constraints.variables)
    source_set = set(source_variables)
    parameter_set = set(parameters)
    symbol_set = set(symbols)
    if source_set & parameter_set:
        raise ValueError("source variables and parameters must be disjoint")
    if symbol_set & constraint_variables:
        raise ValueError("observable symbols must be fresh relative to constraint variables")
    if source_set | parameter_set != constraint_variables:
        missing = constraint_variables - (source_set | parameter_set)
        extra = (source_set | parameter_set) - constraint_variables
        raise ValueError(
            "source_variables + parameters must partition constraint variables; "
            f"missing={sorted(map(str, missing))}, extra={sorted(map(str, extra))}"
        )

    generator_order = source_variables + symbols + parameters
    defining_relations = list(constraints.relations)
    defining_relations.extend(
        sp.expand(symbol - observable)
        for symbol, observable in zip(symbols, observables)
    )
    try:
        elimination_basis = sp.groebner(
            defining_relations,
            *generator_order,
            order="lex",
        )
    except sp.PolynomialError as exc:
        raise ValueError("observable elimination requires polynomial relations") from exc

    substitutions = dict(zip(symbols, observables))
    relation_certificates: list[ObservableRelation] = []
    for polynomial in elimination_basis.polys:
        relation = sp.expand(polynomial.as_expr())
        if relation.free_symbols & source_set:
            continue
        if not relation.free_symbols & symbol_set:
            continue
        relation = sp.factor(relation)
        pullback = sp.expand(relation.subs(substitutions))
        relation_certificates.append(
            ObservableRelation(
                relation=relation,
                pullback_remainder=sp.factor(constraints.reduce(pullback)),
            )
        )

    return ObservableQuotient(
        symbols=symbols,
        observables=observables,
        parameters=parameters,
        eliminated_variables=source_variables,
        relations=tuple(relation_certificates),
    )


def discover_first_order_process_quotient(
    system: ProcessSystem,
    observable: sp.Expr,
    *,
    observable_symbol: sp.Symbol,
    derivative_symbol: sp.Symbol,
    constraints: AlgebraicConstraintSet,
    parameters: Sequence[sp.Symbol] = (),
) -> ObservableQuotient:
    return discover_observable_relations(
        (sp.sympify(observable), system.derive(observable)),
        (observable_symbol, derivative_symbol),
        constraints=constraints,
        source_variables=system.assignments,
        parameters=parameters,
    )
