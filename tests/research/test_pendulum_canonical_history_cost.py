"""Pendulum: canonical clock as the cost measure on a task history quotient.

This essay is the first narrow bridge between two existing research lines:

* pendulum canonicalization produces the observable carrier
  ``Y**2 = 2*(E-U)*(1-U**2)`` with marked clock form ``omega=dU/Y``;
* Huffman history geometry first quotients histories by task semantics and
  then optimizes a stopping tree/DAG with declared edge costs.

The bridge tested here is deliberately weaker than an observer/HJB theorem.
Canonicalization supplies a presentation-invariant *cost measure* on history
edges.  It does not select a globally optimal stopping policy.

Passing this file certifies:

1. ``dU/Y`` is unchanged by an invertible observable reparameterization;
2. raw coordinate increments are not unchanged, so they cannot be canonical
   history-edge costs;
3. clock cost is additive under history refinement;
4. task quotienting must precede prefix optimization: the pendulum reflection
   bit is removable for reduced-carrier tasks but necessary for Cartesian
   reconstruction;
5. ordinary unit-cost Huffman depth is only a special case of costed Bellman
   planning.  With unequal canonical edge costs it can choose the wrong root.

No generic history-cost API or continuous-Huffman theorem is proposed.
"""

from functools import lru_cache
from itertools import combinations

import sympy as sp


def test_pendulum_clock_form_is_observer_reparameterization_invariant():
    U, Y = sp.symbols("U Y")

    # A non-affine but globally monotone polynomial reparameterization.
    X = 2 * U + U**3
    dX_dU = sp.diff(X, U)
    Z = dX_dU * Y  # Z = D X because Y = D U.

    pulled_back_clock_coefficient = sp.simplify(dX_dU / Z)
    assert pulled_back_clock_coefficient == 1 / Y

    # The bare coordinate increment changes and therefore is presentation
    # baggage rather than an intrinsic history cost.
    assert sp.simplify(dX_dU - 1) != 0


def test_canonical_clock_cost_is_additive_under_history_refinement():
    u0, u1, u2 = sp.symbols("u0 u1 u2", real=True)
    tau = sp.Function("tau")

    # On any regular branch tau is a local primitive of omega=dU/Y.
    # Writing costs as primitive differences avoids asking the CAS to choose
    # branches for the elliptic integral.
    whole = tau(u2) - tau(u0)
    refined = (tau(u1) - tau(u0)) + (tau(u2) - tau(u1))

    assert sp.simplify(whole - refined) == 0


def test_task_quotient_decides_whether_the_reflection_bit_survives():
    # Two lifted histories differ only by the local Cartesian reconstruction
    # bit sigma.  They have the same reduced observable state (U,Y).
    histories = (("U0", "Y0", -1), ("U0", "Y0", +1))

    reduced_task = lambda history: history[:2]
    cartesian_task = lambda history: history

    assert len({reduced_task(history) for history in histories}) == 1
    assert len({cartesian_task(history) for history in histories}) == 2


def _optimal_expected_cost(weights, query_costs):
    """Exact Bellman value for subset-splitting queries on a tiny task world."""

    full = frozenset(range(len(weights)))

    @lru_cache(maxsize=None)
    def value(state):
        if len(state) <= 1:
            return sp.Rational(0)
        mass = sum(weights[index] for index in state)
        candidates = []
        for left_size in range(1, len(state)):
            for left_tuple in combinations(sorted(state), left_size):
                left = frozenset(left_tuple)
                # Avoid evaluating both a split and its complement.
                if min(state) not in left:
                    continue
                right = state - left
                split = frozenset((left, right))
                cost = query_costs[split]
                continuation = (
                    sum(weights[index] for index in left) * value(left)
                    + sum(weights[index] for index in right) * value(right)
                ) / mass
                candidates.append((sp.simplify(cost + continuation), split))
        return min(candidates, key=lambda item: (item[0], sorted(map(sorted, item[1]))))[0]

    return value(full)


def test_unit_cost_bellman_value_matches_the_known_huffman_calibration():
    weights = tuple(map(sp.Rational, (6, 3, 1)))
    states = (frozenset((0,)), frozenset((1,)), frozenset((2,)))
    splits = {
        frozenset((states[0], frozenset((1, 2)))): sp.Rational(1),
        frozenset((states[1], frozenset((0, 2)))): sp.Rational(1),
        frozenset((states[2], frozenset((0, 1)))): sp.Rational(1),
        frozenset((states[0], states[1])): sp.Rational(1),
        frozenset((states[0], states[2])): sp.Rational(1),
        frozenset((states[1], states[2])): sp.Rational(1),
    }

    # Unit query costs recover the usual expected-depth objective: isolate the
    # most probable task first, giving 1 + (4/10)*1 = 7/5.
    assert _optimal_expected_cost(weights, splits) == sp.Rational(7, 5)

    # A long first-hit interval for that split changes the optimum.  This is
    # the continuous-history red team: topology cannot be optimized before the
    # canonical edge measure is supplied.
    expensive = dict(splits)
    expensive[frozenset((states[0], frozenset((1, 2))))] = sp.Rational(3)
    assert _optimal_expected_cost(weights, expensive) == sp.Rational(17, 10)
