"""Bounded discovery of process-generated finite grammars.

This module moves Shakespeare one step earlier than relation decomposition. A
caller supplies seed expressions and a process action; the library grows the
smallest exact process span it can find within an explicit search budget. If the
span closes, the existing template-free relation machinery is applied to that
discovered grammar.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Sequence

import sympy as sp

from .presentation.budget import SearchBudget
from .process.local import ProcessSystem
from .relations import (
    RelationDecomposition,
    coefficient_vector,
    decompose,
    discover_relation_decomposition,
)


@dataclass(frozen=True)
class GeneratedGrammar:
    """A finite grammar generated from seed expressions by process action.

    ``basis`` contains only expressions that added a new exact direction to the
    current span. ``depths`` records the process depth at which each basis item
    first appeared. ``residuals`` are process images that escaped the discovered
    span because a search bound was reached.
    """

    seeds: tuple[sp.Expr, ...]
    basis: tuple[sp.Expr, ...]
    depths: tuple[int, ...]
    residuals: tuple[sp.Expr, ...]

    @property
    def closed(self) -> bool:
        return not self.residuals

    @property
    def dimension(self) -> int:
        return len(self.basis)

    @property
    def max_depth(self) -> int:
        return max(self.depths, default=0)

    def growth_profile(self) -> tuple[int, ...]:
        """Cumulative number of independent grammar directions by depth."""
        if not self.depths:
            return ()
        return tuple(
            sum(depth <= level for depth in self.depths)
            for level in range(self.max_depth + 1)
        )


@dataclass(frozen=True)
class GeneratedPresentation:
    """A generated grammar plus its discovered relation presentation."""

    grammar: GeneratedGrammar
    relations: RelationDecomposition | None
    seed_coordinates: tuple[tuple[sp.Expr, ...], ...] = ()

    @property
    def complete(self) -> bool:
        return (
            self.grammar.closed
            and self.relations is not None
            and self.relations.complete
            and len(self.seed_coordinates) == len(self.grammar.seeds)
        )

    @property
    def primitives(self) -> tuple[sp.Expr, ...]:
        if self.relations is None:
            return ()
        return self.relations.primitives


def _in_span(
    expr: sp.Expr,
    basis: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> bool:
    expr = sp.expand(sp.sympify(expr))
    if expr == 0:
        return True
    if not basis:
        return False
    try:
        coefficient_vector(expr, basis, variables)
    except ValueError:
        return False
    return True


def _polynomial_degree(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> int:
    try:
        degree = sp.Poly(sp.expand(expr), *variables).total_degree()
    except sp.PolynomialError as exc:
        raise ValueError(
            "generated-grammar discovery currently requires polynomial expressions"
        ) from exc
    if degree is sp.S.NegativeInfinity:
        return 0
    return int(degree)


def _append_unique(residuals: list[sp.Expr], expr: sp.Expr) -> None:
    expr = sp.expand(expr)
    if all(sp.expand(expr - current) != 0 for current in residuals):
        residuals.append(expr)


def discover_generated_grammar(
    system: ProcessSystem,
    seeds: Sequence[sp.Expr],
    budget: SearchBudget | None = None,
) -> GeneratedGrammar:
    """Grow a finite process grammar from caller-supplied seed expressions.

    The algorithm performs an exact, bounded closure search. It repeatedly
    applies the represented process generator and adds an expression only when
    it lies outside the current span. Search stops locally when history depth,
    polynomial degree, or the primitive-addition budget is exceeded; escaping
    expressions are returned as residual certificates rather than projected
    away.

    ``max_new_primitives`` counts new directions added *after* the independent
    seed directions.
    """

    budget = budget or SearchBudget()
    normalized_seeds = tuple(sp.expand(sp.sympify(seed)) for seed in seeds)
    if not normalized_seeds:
        raise ValueError("at least one seed expression is required")

    basis: list[sp.Expr] = []
    depths: list[int] = []
    queue: deque[tuple[sp.Expr, int]] = deque()

    for seed in normalized_seeds:
        _polynomial_degree(seed, system.assignments)
        if not _in_span(seed, basis, system.assignments):
            basis.append(seed)
            depths.append(0)
            queue.append((seed, 0))

    if not basis:
        raise ValueError("at least one nonzero independent seed is required")

    additions = 0
    residuals: list[sp.Expr] = []

    while queue:
        expression, depth = queue.popleft()
        derived = sp.expand(system.derive(expression))
        if _in_span(derived, basis, system.assignments):
            continue

        if depth >= budget.max_history_depth:
            _append_unique(residuals, derived)
            continue
        if _polynomial_degree(derived, system.assignments) > budget.max_expression_degree:
            _append_unique(residuals, derived)
            continue
        if additions >= budget.max_new_primitives:
            _append_unique(residuals, derived)
            continue

        basis.append(derived)
        depths.append(depth + 1)
        queue.append((derived, depth + 1))
        additions += 1

    for expression in basis:
        derived = sp.expand(system.derive(expression))
        if not _in_span(derived, basis, system.assignments):
            _append_unique(residuals, derived)

    return GeneratedGrammar(
        seeds=normalized_seeds,
        basis=tuple(basis),
        depths=tuple(depths),
        residuals=tuple(residuals),
    )


def discover_generated_presentation(
    system: ProcessSystem,
    seeds: Sequence[sp.Expr],
    budget: SearchBudget | None = None,
) -> GeneratedPresentation:
    """Discover a finite grammar, its relation factors, primitives, and decoder."""
    budget = budget or SearchBudget()
    grammar = discover_generated_grammar(system, seeds, budget=budget)
    if not grammar.closed:
        return GeneratedPresentation(grammar=grammar, relations=None)

    relations = discover_relation_decomposition(
        system,
        grammar.basis,
        max_order=budget.max_relation_order,
    )
    if relations is None or not relations.complete:
        return GeneratedPresentation(grammar=grammar, relations=relations)

    seed_coordinates = tuple(
        decompose(seed, relations.primitives, system.assignments)
        for seed in grammar.seeds
    )
    return GeneratedPresentation(
        grammar=grammar,
        relations=relations,
        seed_coordinates=seed_coordinates,
    )
