"""Costed search over first-order algebraic observer quotients.

This module connects the new discovery front-end to Shakespeare's existing
multi-axis presentation search. The task here is deliberately narrow: among a
caller-declared family of observer candidates, find those whose first process
jet ``(F, D F)`` closes by certified algebraic relations on a declared leaf,
and compare the resulting presentations without imposing a universal scalar
objective.

The caller still declares the candidate family. In particular, this layer does
not yet infer vector roles such as position versus velocity from bare assignment
symbols. That earlier proposal problem belongs to future observer-construction
machinery.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Sequence

import sympy as sp

from ..constraints import AlgebraicConstraintSet
from ..core import ProcessSystem
from ..cost import PresentationCost
from ..search import PresentationCandidate, PresentationSearchResult, pareto_frontier
from .polynomial import ObservableQuotient, discover_first_order_process_quotient


@dataclass(frozen=True)
class FirstOrderObservablePresentation:
    """One observer together with its discovered first-order algebraic quotient."""

    observable: sp.Expr
    derivative: sp.Expr
    quotient: ObservableQuotient

    @property
    def algebraically_closed(self) -> bool:
        return bool(self.quotient.relations) and self.quotient.complete_certificates


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
        raise ValueError("quotient relation must be polynomial") from exc
    return float(int(polynomial.total_degree()) + len(polynomial.terms()))


def structural_first_order_quotient_cost(
    presentation: FirstOrderObservablePresentation,
) -> PresentationCost:
    """Default multi-axis cost for a first-order algebraic observer presentation.

    ``grammar`` prices the observer and its first process derivative.
    ``relations`` is the sum of total degree plus monomial support for all
    discovered relations. ``history`` is one because the presentation uses the
    first process jet ``(F, D F)``. ``task_error`` is zero exactly when a
    certified algebraic closure relation was found; otherwise it is infinite.

    This proxy is intentionally replaceable. It is a transparent baseline for
    comparing observer quotients, not a canonical mathematical complexity.
    """

    relation_variables = (
        presentation.quotient.symbols + presentation.quotient.parameters
    )
    relation_cost = sum(
        _relation_complexity(item.relation, relation_variables)
        for item in presentation.quotient.relations
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


def search_first_order_process_quotients(
    system: ProcessSystem,
    observer_candidates: Sequence[sp.Expr],
    *,
    constraints: AlgebraicConstraintSet,
    parameters: Sequence[sp.Symbol] = (),
    cost_model: Callable[
        [FirstOrderObservablePresentation], PresentationCost
    ] | None = None,
) -> PresentationSearchResult[FirstOrderObservablePresentation]:
    """Compare candidate observers by certified first-order algebraic closure.

    The fixed task is *first-order algebraic quotient closure*: each candidate
    ``F`` is mapped to fresh coordinates ``(U,Y)=(F,D F)``, source assignments
    are eliminated on the declared constraint leaf, and candidates with at least
    one certified relation are admitted to the Pareto frontier.

    No candidate is silently dropped because it looks expensive. The result
    retains every evaluated presentation and its exact quotient certificate.
    """

    observer_candidates = tuple(
        sp.expand(sp.sympify(candidate)) for candidate in observer_candidates
    )
    if not observer_candidates:
        raise ValueError("at least one observer candidate is required")

    score = cost_model or structural_first_order_quotient_cost
    forbidden = set(constraints.variables)
    evaluated: list[PresentationCandidate[FirstOrderObservablePresentation]] = []

    for index, observable in enumerate(observer_candidates):
        observable_symbol = _fresh_symbol(f"U{index}", forbidden)
        derivative_symbol = _fresh_symbol(f"Y{index}", forbidden)
        quotient = discover_first_order_process_quotient(
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
            quotient=quotient,
        )
        evaluated.append(
            PresentationCandidate(
                payload=payload,
                cost=score(payload),
                sufficient=payload.algebraically_closed,
                label=str(observable),
                certificate=tuple(
                    relation.relation for relation in quotient.relations
                ),
            )
        )

    evaluated_tuple = tuple(evaluated)
    return PresentationSearchResult(
        evaluated=evaluated_tuple,
        pareto=pareto_frontier(evaluated_tuple),
    )
