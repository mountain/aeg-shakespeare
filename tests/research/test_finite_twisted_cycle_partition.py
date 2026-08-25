"""Exact finite-graph calibration for character-twisted cycle series.

This proves only finite matrix and formal-series identities.  It does not
construct a Markov partition, a transfer operator for a continuous flow, or a
Ruelle zeta function for the PCR3BP.
"""

from itertools import product

import sympy as sp


RHO = {
    "a": sp.ImmutableMatrix(((1, 2), (0, 1))),
    "b": sp.ImmutableMatrix(((1, 0), (-2, 1))),
}


def _holonomy(word):
    result = sp.eye(2)
    for letter in word:
        result = result * RHO[letter]
    return result


def _scalar_weight(word, left_weight, right_weight):
    weights = {"a": left_weight, "b": right_weight}
    return sp.prod(weights[letter] for letter in word)


def _truncate(expression, variable, degree):
    return sp.series(
        expression, variable, 0, degree + 1
    ).removeO().expand()


def test_gamma2_character_detects_order_erased_by_scalar_augmentation():
    left_weight, right_weight, cost_weight = sp.symbols("x y q")
    grouped, alternating = "aabb", "abab"

    assert (
        _scalar_weight(grouped, left_weight, right_weight)
        == _scalar_weight(alternating, left_weight, right_weight)
        == left_weight**2 * right_weight**2
    )
    costs = {"a": 2, "b": 3}
    assert (
        cost_weight ** sum(costs[letter] for letter in grouped)
        == cost_weight ** sum(costs[letter] for letter in alternating)
        == cost_weight**10
    )
    assert RHO["a"] * RHO["b"] != RHO["b"] * RHO["a"]
    assert _holonomy(grouped) == sp.ImmutableMatrix(((-15, 4), (-4, 1)))
    assert _holonomy(alternating) == sp.ImmutableMatrix(((5, -4), (4, -3)))
    assert _holonomy(grouped).trace() == -14
    assert _holonomy(alternating).trace() == 2

    # A cyclic shift changes the based word but not the closed-cycle
    # character.  The trace is supposed to forget a cycle's base point.
    assert _holonomy("abba").trace() == _holonomy(grouped).trace()


def test_twisted_trace_powers_enumerate_based_closed_words_exactly():
    left_weight, right_weight = sp.symbols("x y")
    transfer = left_weight * RHO["a"] + right_weight * RHO["b"]

    for length in range(1, 5):
        enumerated = sp.Integer(0)
        for letters in product("ab", repeat=length):
            word = "".join(letters)
            enumerated += (
                _scalar_weight(word, left_weight, right_weight)
                * _holonomy(word).trace()
            )
        assert sp.expand((transfer**length).trace() - enumerated) == 0

    # Four cyclic placements have the grouped character and two have the
    # alternating character.
    mixed_coefficient = (
        sp.expand((transfer**4).trace())
        .coeff(left_weight, 2)
        .coeff(right_weight, 2)
    )
    assert mixed_coefficient == 4 * (-14) + 2 * 2


def test_twisted_cycle_exponential_equals_reciprocal_determinant():
    left_weight, right_weight, cycle_marker = sp.symbols("x y z")
    symbolic_transfer = left_weight * RHO["a"] + right_weight * RHO["b"]
    symbolic_determinant = (
        sp.eye(2) - cycle_marker * symbolic_transfer
    ).det().expand()

    expected_determinant = (
        1
        - 2 * (left_weight + right_weight) * cycle_marker
        + (
            left_weight**2
            + 6 * left_weight * right_weight
            + right_weight**2
        )
        * cycle_marker**2
    )
    assert sp.expand(symbolic_determinant - expected_determinant) == 0

    # Keep the formal-series gate exact but specialize the two edge weights to
    # integers.  The preceding symbolic determinant and trace-power test carry
    # the generic x,y dependence; this avoids a slow multivariate expansion in
    # the default CI matrix.
    transfer = symbolic_transfer.subs({left_weight: 2, right_weight: 3})
    determinant = (sp.eye(2) - cycle_marker * transfer).det().expand()
    degree = 6
    trace_log = sum(
        cycle_marker**length * (transfer**length).trace() / sp.Integer(length)
        for length in range(1, degree + 1)
    )
    via_determinant = _truncate(1 / determinant, cycle_marker, degree)
    via_closed_walks = _truncate(sp.exp(trace_log), cycle_marker, degree)
    assert sp.simplify(via_determinant - via_closed_walks) == 0
