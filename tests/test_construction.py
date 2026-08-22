import sympy as sp

from aeg_shakespeare import ProcessSystem, SearchBudget
from aeg_shakespeare.construction import (
    SymbolicOperation,
    generate_primitive_proposals,
)
from aeg_shakespeare.search import search_primitive_proposals


def test_semantically_equal_proposals_keep_distinct_construction_trees():
    x, y, z = sp.symbols("x y z")
    add = SymbolicOperation(
        "add",
        2,
        lambda a, b: a + b,
        cost=1.0,
        commutative=True,
    )

    result = generate_primitive_proposals(
        (x, y, z),
        (add,),
        variables=(x, y, z),
        max_depth=2,
        max_degree=1,
        max_candidates=128,
    )

    same_expression = [
        proposal
        for proposal in result.proposals
        if sp.expand(proposal.expression - (x + y + z)) == 0
    ]
    recipes = {proposal.construction.recipe() for proposal in same_expression}

    # Commutativity removes argument reversal at each node, but associativity is
    # not silently imposed. The construction histories remain distinct.
    assert len(recipes) >= 2
    assert any(recipe.startswith("add(add(") for recipe in recipes)
    assert all(proposal.cost == 2.0 for proposal in same_expression)


def test_declared_commutativity_removes_only_argument_permutations():
    x, y = sp.symbols("x y")
    add = SymbolicOperation("add", 2, lambda a, b: a + b, commutative=True)
    result = generate_primitive_proposals(
        (x, y),
        (add,),
        variables=(x, y),
        max_depth=1,
        max_degree=1,
        max_candidates=16,
        include_atoms=False,
    )

    xy = [
        proposal
        for proposal in result.proposals
        if sp.expand(proposal.expression - (x + y)) == 0
    ]
    assert len(xy) == 1
    assert xy[0].construction.recipe() == "add(x, y)"


def test_degree_bound_returns_rejected_construction_certificate():
    x, y = sp.symbols("x y")
    multiply = SymbolicOperation("mul", 2, lambda a, b: a * b, commutative=True)
    result = generate_primitive_proposals(
        (x, y),
        (multiply,),
        variables=(x, y),
        max_depth=1,
        max_degree=1,
        max_candidates=16,
        include_atoms=False,
    )

    assert not result.proposals
    assert result.rejected
    assert any("degree 2 exceeds bound 1" in item.reason for item in result.rejected)


def test_candidate_bound_is_explicit_and_atoms_do_not_consume_it():
    x, y = sp.symbols("x y")
    add = SymbolicOperation("add", 2, lambda a, b: a + b, commutative=True)
    result = generate_primitive_proposals(
        (x, y),
        (add,),
        variables=(x, y),
        max_depth=2,
        max_degree=1,
        max_candidates=0,
        include_atoms=True,
    )

    assert result.truncated
    assert [proposal.expression for proposal in result.proposals] == [x, y]


def test_operation_generated_proposals_feed_the_common_presentation_search():
    x, p = sp.symbols("x p")
    system = ProcessSystem((x, p), {x: p, p: -x}, name="R")
    multiply = SymbolicOperation("mul", 2, lambda a, b: a * b, commutative=True)

    generated = generate_primitive_proposals(
        (x, p),
        (multiply,),
        variables=(x, p),
        max_depth=2,
        max_degree=3,
        max_candidates=128,
        include_atoms=True,
    )
    search = search_primitive_proposals(
        system,
        generated.proposals,
        targets=(x**3,),
        budget=SearchBudget(
            max_history_depth=8,
            max_expression_degree=3,
            max_relation_order=8,
            max_new_primitives=8,
        ),
    )

    sufficient = [candidate for candidate in search.evaluated if candidate.sufficient]
    assert sufficient
    assert search.pareto
    assert any(
        sp.expand(candidate.payload.proposal.expression - x**3) == 0
        and "mul" in (candidate.label or "")
        for candidate in sufficient
    )
    # Degree-one atoms cannot decode a cubic target under the recurrent process;
    # task failure stays explicit rather than being hidden by the cost model.
    assert any(
        candidate.payload.proposal.expression in (x, p) and not candidate.sufficient
        for candidate in search.evaluated
    )
