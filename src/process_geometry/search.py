"""Costed search over reusable process-presentation candidates.

The search layer does not define one universal scalar objective. It evaluates
candidate presentations into the public multi-axis ``PresentationCost`` and
returns the Pareto frontier. The symbolic adapters implement exact
reconstruction tasks over ``GeneratedPresentation`` objects; downstream users
can reuse the generic candidate/frontier machinery for history codes, task
quotients, or other presentation families.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Generic, Sequence, TypeVar

import sympy as sp

from .construction import PrimitiveProposal
from .cost import PresentationCost
from .grammar import GeneratedPresentation, discover_generated_presentation
from .presentation.budget import SearchBudget
from .process.local import ProcessSystem
from .relations import decompose

PayloadT = TypeVar("PayloadT")


@dataclass(frozen=True)
class PresentationCandidate(Generic[PayloadT]):
    """One evaluated representation candidate."""

    payload: PayloadT
    cost: PresentationCost
    sufficient: bool = True
    label: str | None = None
    certificate: object | None = None


@dataclass(frozen=True)
class PresentationSearchResult(Generic[PayloadT]):
    """All evaluated candidates and the task-sufficient Pareto frontier."""

    evaluated: tuple[PresentationCandidate[PayloadT], ...]
    pareto: tuple[PresentationCandidate[PayloadT], ...]

    @property
    def rejected(self) -> tuple[PresentationCandidate[PayloadT], ...]:
        return tuple(candidate for candidate in self.evaluated if not candidate.sufficient)


def pareto_frontier(
    candidates: Sequence[PresentationCandidate[PayloadT]],
    *,
    require_sufficient: bool = True,
) -> tuple[PresentationCandidate[PayloadT], ...]:
    """Return candidates not Pareto-dominated by another admissible candidate."""
    admissible = tuple(
        candidate
        for candidate in candidates
        if candidate.sufficient or not require_sufficient
    )
    frontier: list[PresentationCandidate[PayloadT]] = []
    for candidate in admissible:
        if any(
            other is not candidate and other.cost.dominates(candidate.cost)
            for other in admissible
        ):
            continue
        frontier.append(candidate)
    return tuple(frontier)


@dataclass(frozen=True)
class ExactReconstructionPresentation:
    """Generated symbolic presentation evaluated for exact target decoding."""

    proposal_seeds: tuple[sp.Expr, ...]
    targets: tuple[sp.Expr, ...]
    presentation: GeneratedPresentation
    target_coordinates: tuple[tuple[sp.Expr, ...], ...]
    failure: str | None = None

    @property
    def sufficient(self) -> bool:
        return self.failure is None and len(self.target_coordinates) == len(self.targets)


@dataclass(frozen=True)
class ConstructedPrimitivePresentation:
    """One construction-history-preserving primitive proposal after evaluation."""

    proposal: PrimitiveProposal
    evaluation: ExactReconstructionPresentation

    @property
    def sufficient(self) -> bool:
        return self.evaluation.sufficient


def _expression_complexity(expr: sp.Expr) -> float:
    """Small structural proxy used only by the default search cost model."""
    expr = sp.expand(sp.sympify(expr))
    return float(int(sp.count_ops(expr, visual=False)) + 1)


def structural_exact_reconstruction_cost(
    candidate: ExactReconstructionPresentation,
) -> PresentationCost:
    """Default transparent structural cost for exact symbolic candidates."""
    presentation = candidate.presentation
    grammar_cost = sum(_expression_complexity(seed) for seed in candidate.proposal_seeds)
    grammar_cost += sum(_expression_complexity(item) for item in presentation.primitives)

    relation_cost = 0.0
    if presentation.relations is not None:
        relation_cost += sum(
            1.0
            for coefficient in presentation.relations.global_relation.coefficients
            if sp.simplify(coefficient) != 0
        )
        for component in presentation.relations.components:
            relation_cost += sum(
                1.0
                for coefficient in component.coefficients
                if sp.simplify(coefficient) != 0
            )

    history_cost = float(sum(presentation.grammar.depths))
    decoder_cost = float(
        sum(
            1
            for coordinates in candidate.target_coordinates
            for coefficient in coordinates
            if sp.simplify(coefficient) != 0
        )
    )

    return PresentationCost(
        grammar=grammar_cost,
        relations=relation_cost,
        history=history_cost,
        decoder=decoder_cost,
        task_error=0.0 if candidate.sufficient else math.inf,
    )


def construction_aware_exact_reconstruction_cost(
    candidate: ConstructedPrimitivePresentation,
) -> PresentationCost:
    """Baseline exact-reconstruction cost including proposal construction depth."""
    base = structural_exact_reconstruction_cost(candidate.evaluation)
    return PresentationCost(
        grammar=base.grammar + candidate.proposal.cost,
        relations=base.relations,
        history=base.history,
        decoder=base.decoder,
        task_error=base.task_error,
    )


def evaluate_exact_reconstruction_presentation(
    system: ProcessSystem,
    proposal_seeds: Sequence[sp.Expr],
    targets: Sequence[sp.Expr],
    *,
    budget: SearchBudget | None = None,
) -> ExactReconstructionPresentation:
    """Build one generated presentation and certify exact target reconstruction."""
    normalized_seeds = tuple(sp.expand(sp.sympify(seed)) for seed in proposal_seeds)
    normalized_targets = tuple(sp.expand(sp.sympify(target)) for target in targets)
    if not normalized_targets:
        raise ValueError("at least one reconstruction target is required")

    presentation = discover_generated_presentation(system, normalized_seeds, budget=budget)
    if not presentation.complete:
        return ExactReconstructionPresentation(
            proposal_seeds=normalized_seeds,
            targets=normalized_targets,
            presentation=presentation,
            target_coordinates=(),
            failure="generated presentation is incomplete",
        )

    coordinates: list[tuple[sp.Expr, ...]] = []
    try:
        for target in normalized_targets:
            coordinates.append(
                decompose(target, presentation.primitives, system.assignments)
            )
    except ValueError as exc:
        return ExactReconstructionPresentation(
            proposal_seeds=normalized_seeds,
            targets=normalized_targets,
            presentation=presentation,
            target_coordinates=tuple(coordinates),
            failure=str(exc),
        )

    return ExactReconstructionPresentation(
        proposal_seeds=normalized_seeds,
        targets=normalized_targets,
        presentation=presentation,
        target_coordinates=tuple(coordinates),
    )


def search_exact_reconstruction_presentations(
    system: ProcessSystem,
    seed_proposals: Sequence[Sequence[sp.Expr]],
    targets: Sequence[sp.Expr],
    *,
    budget: SearchBudget | None = None,
    cost_model: Callable[[ExactReconstructionPresentation], PresentationCost] | None = None,
) -> PresentationSearchResult[ExactReconstructionPresentation]:
    """Evaluate caller-proposed seed grammars and return their Pareto frontier."""
    if not seed_proposals:
        raise ValueError("at least one seed proposal is required")
    score = cost_model or structural_exact_reconstruction_cost

    evaluated: list[PresentationCandidate[ExactReconstructionPresentation]] = []
    for index, proposal in enumerate(seed_proposals):
        payload = evaluate_exact_reconstruction_presentation(
            system,
            proposal,
            targets,
            budget=budget,
        )
        cost = score(payload)
        evaluated.append(
            PresentationCandidate(
                payload=payload,
                cost=cost,
                sufficient=payload.sufficient,
                label=f"proposal-{index}",
                certificate=payload.failure or payload.target_coordinates,
            )
        )

    evaluated_tuple = tuple(evaluated)
    return PresentationSearchResult(
        evaluated=evaluated_tuple,
        pareto=pareto_frontier(evaluated_tuple),
    )


def search_primitive_proposals(
    system: ProcessSystem,
    proposals: Sequence[PrimitiveProposal],
    targets: Sequence[sp.Expr],
    *,
    budget: SearchBudget | None = None,
    cost_model: Callable[[ConstructedPrimitivePresentation], PresentationCost] | None = None,
) -> PresentationSearchResult[ConstructedPrimitivePresentation]:
    """Evaluate construction-preserving primitive proposals as one-seed grammars."""
    if not proposals:
        raise ValueError("at least one primitive proposal is required")
    score = cost_model or construction_aware_exact_reconstruction_cost

    evaluated: list[PresentationCandidate[ConstructedPrimitivePresentation]] = []
    for proposal in proposals:
        evaluation = evaluate_exact_reconstruction_presentation(
            system,
            (proposal.expression,),
            targets,
            budget=budget,
        )
        payload = ConstructedPrimitivePresentation(
            proposal=proposal,
            evaluation=evaluation,
        )
        evaluated.append(
            PresentationCandidate(
                payload=payload,
                cost=score(payload),
                sufficient=payload.sufficient,
                label=proposal.construction.recipe(),
                certificate=evaluation.failure or evaluation.target_coordinates,
            )
        )

    evaluated_tuple = tuple(evaluated)
    return PresentationSearchResult(
        evaluated=evaluated_tuple,
        pareto=pareto_frontier(evaluated_tuple),
    )
