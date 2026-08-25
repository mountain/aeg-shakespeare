"""Costed search over first-order observable algebraic-image presentations.

This module connects the discovery front-end to Process Geometry's multi-axis
presentation search. The task here is deliberately narrow: among a
caller-declared family of observable candidates, find those whose first-order
observable pair ``(F, D F)`` closes by certified algebraic relations on a
declared leaf, and compare the resulting presentations without imposing a
universal scalar objective.

This is not a search over task/process quotients in the sense of
``H(P)/~_Q``. Historical observer/quotient names remain 0.0.x aliases.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Sequence

import sympy as sp

from ..presentation.constraints import AlgebraicConstraintSet
from ..presentation.search import (
    PresentationCandidate,
    PresentationCost,
    PresentationSearchResult,
    pareto_frontier,
)
from ..process.local import ProcessSystem
from .polynomial import (
    ObservableAlgebraicImage,
    discover_first_order_observable_image,
)


@dataclass(frozen=True)
class FirstOrderObservablePresentation:
    """One observable together with its discovered first-order algebraic presentation."""

    observable: sp.Expr
    derivative: sp.Expr
    image: ObservableAlgebraicImage

    @property
    def quotient(self) -> ObservableAlgebraicImage:
        """Historical 0.0.x spelling retained for executable provenance."""

        return self.image

    @property
    def algebraically_closed(self) -> bool:
        return bool(self.image.relations) and self.image.complete_certificates


def _expression_complexity(expr: sp.Expr) -> float:
    expr = sp.expand(sp.sympify(expr))
    return float(int(sp.count_ops(expr, visual=False)) + 1)


def _relation_complexity(
    relation: sp.Expr,
    variables: Sequence[sp.Symbol],
) -> float:
    """Transparent degree-plus-support proxy for one algebraic relation."""
    try:
        polynomial = sp.Poly(sp.expand(relation), *variables, domain="EX")
    except sp.PolynomialError as exc:
        raise ValueError("algebraic-image relation must be polynomial") from exc
    return float(int(polynomial.total_degree()) + len(polynomial.terms()))


def structural_first_order_observable_presentation_cost(
    presentation: FirstOrderObservablePresentation,
) -> PresentationCost:
    """Default multi-axis cost for a first-order observable presentation."""
    relation_variables = (
        presentation.image.symbols + presentation.image.parameters
    )
    relation_cost = sum(
        _relation_complexity(item.relation, relation_variables)
        for item in presentation.image.relations
    )
    return PresentationCost(
        grammar=(
            _expression_complexity(presentation.observable)
            + _expression_complexity(presentation.derivative)
        ),
        relations=float(relation_cost),
        history=1.0,
        decoder=0.0,
        task_error=0.0 if presentation.algebraically_closed else math.inf,
    )


def _fresh_symbol(base: str, forbidden: set[sp.Symbol]) -> sp.Symbol:
    candidate = sp.Symbol(base)
    suffix = 0
    while candidate in forbidden:
        suffix += 1
        candidate = sp.Symbol(f"{base}_{suffix}")
    forbidden.add(candidate)
    return candidate


def search_first_order_observable_presentations(
    system: ProcessSystem,
    observable_candidates: Sequence[sp.Expr],
    *,
    constraints: AlgebraicConstraintSet,
    parameters: Sequence[sp.Symbol] = (),
    cost_model: Callable[
        [FirstOrderObservablePresentation], PresentationCost
    ] | None = None,
) -> PresentationSearchResult[FirstOrderObservablePresentation]:
    """Compare candidate observables by certified first-order algebraic closure."""
    observable_candidates = tuple(
        sp.expand(sp.sympify(candidate)) for candidate in observable_candidates
    )
    if not observable_candidates:
        raise ValueError("at least one observable candidate is required")

    score = cost_model or structural_first_order_observable_presentation_cost
    forbidden = set(constraints.variables)
    evaluated: list[PresentationCandidate[FirstOrderObservablePresentation]] = []

    for index, observable in enumerate(observable_candidates):
        observable_symbol = _fresh_symbol(f"U{index}", forbidden)
        derivative_symbol = _fresh_symbol(f"Y{index}", forbidden)
        image = discover_first_order_observable_image(
            system,
            observable,
            observable_symbol=observable_symbol,
            derivative_symbol=derivative_symbol,
            constraints=constraints,
            parameters=parameters,
        )
        payload = FirstOrderObservablePresentation(
            observable=observable,
            derivative=system.derive(observable),
            image=image,
        )
        evaluated.append(
            PresentationCandidate(
                payload=payload,
                cost=score(payload),
                sufficient=payload.algebraically_closed,
                label=str(observable),
                certificate=tuple(
                    relation.relation for relation in image.relations
                ),
            )
        )

    evaluated_tuple = tuple(evaluated)
    return PresentationSearchResult(
        evaluated=evaluated_tuple,
        pareto=pareto_frontier(evaluated_tuple),
    )


# Historical 0.0.x names.
structural_first_order_observer_presentation_cost = (
    structural_first_order_observable_presentation_cost
)
structural_first_order_quotient_cost = structural_first_order_observable_presentation_cost
search_first_order_observer_presentations = search_first_order_observable_presentations
search_first_order_process_quotients = search_first_order_observable_presentations
