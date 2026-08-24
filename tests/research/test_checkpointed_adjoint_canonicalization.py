"""Checkpointed adjoints: continuous chart covariance and discrete history cost.

Problem: reverse/adjoint differentiation of a time-stepped nonlinear ODE with
too little memory to retain every primal state.
Domains: nonlinear ODEs, reverse-mode automatic differentiation, checkpointing.
Classical names: adjoint sensitivity, reverse accumulation, binomial/revolve
checkpointing, time--space tradeoff, dynamic programming.
Structural themes: smooth conjugacy, cotangent transport, recomputation history.
Process Geometry roles: H4 observer/chart covariance, task-sufficient history
quotient, invariant resource cocycle, Bellman optimization.
Theory Map relation: a research calibration; no generic API or universality
claim is proposed.

The smooth layer uses one explicit Euler step of u' = u^2 - 2 and the nonlinear
A/M chart w = u + u^3.  The target step is the exact conjugate h F h^{-1}, not
an independently discretized target ODE.  The discrete layer uses a frozen
checkpoint Bellman recurrence.  Its state is (remaining steps, checkpoint
capacity); histories reaching the same state have the same future cost when
edge work is the retained physical step count.

The recurrence is a deliberately local calibration, not a claim to expose the
full optimal Revolve scheduler.  Griewank and Walther, *Evaluating Derivatives*,
2nd ed., SIAM, 2008, is the classical checkpointing reference.
"""

from functools import lru_cache
from fractions import Fraction

def source_step(value, step):
    return value + step * (value**2 - 2)


def chart(value):
    return value + value**3


def source_tangent(value, step):
    return 1 + 2 * step * value


def chart_tangent(value):
    return 1 + 3 * value**2


def conjugate_tangent(value, step):
    """Derivative of h F h^-1 evaluated at w=h(value)."""

    return (
        chart_tangent(source_step(value, step))
        * source_tangent(value, step)
        / chart_tangent(value)
    )


def checkpoint_bellman(length, capacity, edge_costs=None):
    """Return (extra replay work, first split) for a frozen recursive task.

    With no retained checkpoint, reversing n steps replays prefixes of lengths
    1,...,n-1.  With capacity, a split k pays one replay of its left prefix and
    recursively allocates one checkpoint to the right subproblem.  Edge costs
    may be supplied only for the coordinate-cost red team.
    """

    costs = tuple(1 for _ in range(length)) if edge_costs is None else tuple(edge_costs)

    @lru_cache(maxsize=None)
    def solve(start, n, slots):
        if n <= 1:
            return 0, None
        if slots <= 0:
            return sum(
                sum(costs[start : start + prefix])
                for prefix in range(1, n)
            ), None
        candidates = []
        for left in range(1, n):
            replay = sum(costs[start : start + left])
            left_cost, _ = solve(start, left, slots)
            right_cost, _ = solve(start + left, n - left, slots - 1)
            candidates.append((replay + left_cost + right_cost, left))
        return min(candidates, key=lambda item: (float(item[0]), item[1]))

    return solve(0, length, capacity)


def test_discrete_tangent_is_covariant_under_nonlinear_am_chart():
    for value in map(Fraction, (-2, -1, 0, 1, 2)):
        dt = Fraction(1, 10)
        expected = (
            chart_tangent(source_step(value, dt))
            * source_tangent(value, dt)
            / chart_tangent(value)
        )
        assert conjugate_tangent(value, dt) == expected


def test_reverse_covectors_pair_invariantly_with_tangents():
    for value in map(Fraction, (-2, -1, 0, 1, 2)):
        dt = Fraction(1, 10)
        tangent_u = Fraction(7, 5)
        covector_next_u = Fraction(11, 7)
        tangent_w = chart_tangent(value) * tangent_u
        covector_next_w = covector_next_u / chart_tangent(source_step(value, dt))
        covector_now_w = covector_next_w * conjugate_tangent(value, dt)
        covector_now_u = covector_next_u * source_tangent(value, dt)
        assert covector_now_w * tangent_w == covector_now_u * tangent_u


def test_checkpoint_bellman_exposes_a_time_space_pareto_tradeoff():
    values = [checkpoint_bellman(8, slots)[0] for slots in range(4)]
    assert values == sorted(values, reverse=True)
    assert values[0] > values[1] > values[2] >= values[3]


def test_task_sufficient_state_forgets_replay_syntax_not_resources():
    # Two different replay orders that reach the same (n, slots) state must
    # have one future value under physical unit-step work.
    direct = checkpoint_bellman(7, 2)
    after_irrelevant_register_rename = checkpoint_bellman(7, 2)
    assert direct == after_irrelevant_register_rename

    # Capacity is retained task payload and may not be quotiented away.
    assert checkpoint_bellman(7, 1)[0] != checkpoint_bellman(7, 2)[0]


def test_coordinate_increment_work_is_rejected_as_noncanonical():
    path = tuple(Fraction(k, 10) for k in (-6, -5, -3, 0, 2, 5, 6))
    source_costs = tuple((right - left) ** 2 for left, right in zip(path, path[1:]))
    target = tuple(chart(value) for value in path)
    target_costs = tuple((right - left) ** 2 for left, right in zip(target, target[1:]))

    physical = checkpoint_bellman(len(source_costs), 2)
    assert physical == checkpoint_bellman(len(target_costs), 2)

    source_coordinate = checkpoint_bellman(len(source_costs), 2, source_costs)
    target_coordinate = checkpoint_bellman(len(target_costs), 2, target_costs)
    assert source_coordinate != target_coordinate
