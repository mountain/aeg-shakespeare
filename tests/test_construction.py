import sympy as sp

from aeg_shakespeare.construction import (
    SymbolicOperation,
    generate_primitive_proposals,
)


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
    # not silently imposed. The two construction histories remain distinct.
    assert len(recipes) >= 2
    assert any(recipe.startswith("add(add(") for recipe in recipes)
    assert any("add(y, z)" in recipe or "add(x, z)" in recipe for recipe in recipes)
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
