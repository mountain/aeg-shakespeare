import math

import sympy as sp

from aeg_shakespeare.presentation.search import (
    PresentationCandidate,
    PresentationCost,
    SearchBudget,
    evaluate_exact_reconstruction_presentation,
    pareto_frontier,
    search_exact_reconstruction_presentations,
)
from aeg_shakespeare.process.local import ProcessSystem


def recurrent_system():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="R")


def test_generic_pareto_frontier_preserves_tradeoffs_and_rejects_dominated_costs():
    left = PresentationCandidate(
        payload="left",
        cost=PresentationCost(grammar=1, history=2),
    )
    right = PresentationCandidate(
        payload="right",
        cost=PresentationCost(grammar=2, history=1),
    )
    dominated = PresentationCandidate(
        payload="dominated",
        cost=PresentationCost(grammar=3, history=3),
    )
    insufficient = PresentationCandidate(
        payload="invalid",
        cost=PresentationCost(grammar=0, history=0),
        sufficient=False,
    )

    frontier = pareto_frontier((left, right, dominated, insufficient))
    assert {candidate.payload for candidate in frontier} == {"left", "right"}


def test_exact_reconstruction_search_exposes_seed_width_vs_history_depth_tradeoff():
    x, p, system = recurrent_system()
    budget = SearchBudget(
        max_history_depth=4,
        max_expression_degree=1,
        max_relation_order=4,
        max_new_primitives=4,
    )

    result = search_exact_reconstruction_presentations(
        system,
        seed_proposals=((x,), (x, p), (x, p, x + p)),
        targets=(x, p),
        budget=budget,
    )

    assert all(candidate.sufficient for candidate in result.evaluated)
    assert {candidate.label for candidate in result.pareto} == {
        "proposal-0",
        "proposal-1",
    }

    costs = {candidate.label: candidate.cost for candidate in result.evaluated}
    # One seed uses a narrower grammar description but discovers the second
    # direction one process step later.
    assert costs["proposal-0"].grammar < costs["proposal-1"].grammar
    assert costs["proposal-0"].history > costs["proposal-1"].history
    # Adding a redundant seed is strictly worse than the two-seed proposal.
    assert costs["proposal-1"].dominates(costs["proposal-2"])


def test_exact_reconstruction_marks_a_closed_but_task_insufficient_grammar():
    x, p, system = recurrent_system()
    candidate = evaluate_exact_reconstruction_presentation(
        system,
        proposal_seeds=(x**2,),
        targets=(x,),
        budget=SearchBudget(
            max_history_depth=6,
            max_expression_degree=2,
            max_relation_order=6,
            max_new_primitives=6,
        ),
    )

    assert not candidate.sufficient
    assert candidate.failure is not None

    result = search_exact_reconstruction_presentations(
        system,
        seed_proposals=((x**2,), (x,)),
        targets=(x,),
        budget=SearchBudget(
            max_history_depth=6,
            max_expression_degree=2,
            max_relation_order=6,
            max_new_primitives=6,
        ),
    )
    assert len(result.rejected) == 1
    rejected = result.rejected[0]
    assert math.isinf(rejected.cost.task_error)
    assert {candidate.label for candidate in result.pareto} == {"proposal-1"}
