"""Task-covariant complexity coarea: executable theorem candidates.

This research essay strengthens the repository's process-volume/coarea line in
four deliberately separate directions:

1. the pendulum action--period identity is made covariant when its natural
   energy, time, and action units vary;
2. expected stopping cost is identified exactly with a probability-weighted
   live-frontier volume, including non-unit edge costs;
3. task-visible connection holonomy forces continuation-stable memory, while
   task-invisible holonomy does not;
4. a nonintegrable clock distribution blocks a global time/space foliation.

The tests are theorem-shaped finite and symbolic calibrations.  They do not
define a framework API, prove a continuous coarea theorem, or claim that every
process has a canonical complexity ruler or polarization.
"""

from dataclasses import dataclass
from fractions import Fraction

import sympy as sp


def _directional_derivative(expression, variables, rates):
    return sp.expand(
        sum(
            sp.diff(expression, variable) * rate
            for variable, rate in zip(variables, rates)
        )
    )


def test_pendulum_action_period_identity_has_a_scale_covariant_form():
    mass, length, gravity, epsilon = sp.symbols(
        "m ell g epsilon", positive=True
    )
    mass_rate, length_rate, gravity_rate, epsilon_rate = sp.symbols(
        "m_dot ell_dot g_dot epsilon_dot", real=True
    )
    variables = (mass, length, gravity, epsilon)
    rates = (mass_rate, length_rate, gravity_rate, epsilon_rate)

    energy_unit = mass * gravity * length
    time_unit = sp.sqrt(length / gravity)
    action_unit = energy_unit * time_unit

    # One explicit shape function is enough to verify the bundle algebra for
    # arbitrary scale variables and arbitrary tangent rates.  The proof uses
    # only Omega=A0*V(epsilon), E=E0*epsilon, T=t0*V'(epsilon).
    shape_volume = epsilon**3 + 2 * epsilon
    energy = energy_unit * epsilon
    action_volume = action_unit * shape_volume
    period = time_unit * sp.diff(shape_volume, epsilon)

    energy_connection = _directional_derivative(
        sp.log(energy_unit), variables, rates
    )
    action_connection = _directional_derivative(
        sp.log(action_unit), variables, rates
    )
    covariant_energy = (
        _directional_derivative(energy, variables, rates)
        - energy * energy_connection
    )
    covariant_action = (
        _directional_derivative(action_volume, variables, rates)
        - action_volume * action_connection
    )

    time_connection = _directional_derivative(
        sp.log(time_unit), variables, rates
    )
    assert sp.simplify(
        action_connection - (energy_connection + time_connection)
    ) == 0
    assert sp.simplify(covariant_action - period * covariant_energy) == 0


def test_raw_action_energy_slope_fails_when_the_local_unit_moves():
    scale = sp.symbols("s", positive=True)

    # A path through the family of frozen pendulum leaves.  This is not a
    # claim about the dynamics of a physically driven variable-length
    # pendulum; it isolates the geometry of changing local units.
    mass = scale
    length = scale**2
    gravity = scale**3
    epsilon = scale
    energy_unit = mass * gravity * length
    time_unit = sp.sqrt(length / gravity)
    action_unit = energy_unit * time_unit
    shape_volume = epsilon**2
    energy = energy_unit * epsilon
    action_volume = action_unit * shape_volume
    period = time_unit * 2 * epsilon

    raw_slope = sp.diff(action_volume, scale) / sp.diff(energy, scale)
    assert sp.simplify(raw_slope.subs(scale, 1) - sp.Rational(15, 14)) == 0
    assert sp.simplify(period.subs(scale, 1) - 2) == 0
    assert sp.simplify(raw_slope - period) != 0

    energy_connection = sp.diff(sp.log(energy_unit), scale)
    action_connection = sp.diff(sp.log(action_unit), scale)
    covariant_energy = sp.diff(energy, scale) - energy * energy_connection
    covariant_action = (
        sp.diff(action_volume, scale) - action_volume * action_connection
    )
    assert sp.simplify(covariant_action / covariant_energy - period) == 0


@dataclass(frozen=True)
class _TreeEdge:
    cost: Fraction
    descendant_leaves: tuple[int, ...]


def _path_costs(edges, leaf_count):
    return tuple(
        sum(edge.cost for edge in edges if leaf in edge.descendant_leaves)
        for leaf in range(leaf_count)
    )


def _edge_frontier_volume(edges, probabilities):
    """Integral of live probability mass over costed tree edges."""

    return sum(
        edge.cost
        * sum(probabilities[leaf] for leaf in edge.descendant_leaves)
        for edge in edges
    )


def _survival_frontier_integral(stopping_costs, probabilities):
    """Exact integral of P(T_stop > tau) over piecewise-constant cuts."""

    breakpoints = sorted({Fraction(0), *stopping_costs})
    volume = Fraction(0)
    for left, right in zip(breakpoints, breakpoints[1:]):
        live_mass = sum(
            probability
            for cost, probability in zip(stopping_costs, probabilities)
            if cost > left
        )
        volume += (right - left) * live_mass
    return volume


def test_unit_cost_huffman_depth_is_a_discrete_frontier_volume():
    probabilities = (Fraction(6, 10), Fraction(3, 10), Fraction(1, 10))
    edges = (
        _TreeEdge(Fraction(1), (0,)),
        _TreeEdge(Fraction(1), (1, 2)),
        _TreeEdge(Fraction(1), (1,)),
        _TreeEdge(Fraction(1), (2,)),
    )
    stopping_costs = _path_costs(edges, len(probabilities))
    expected_depth = sum(
        probability * cost
        for probability, cost in zip(probabilities, stopping_costs)
    )

    assert stopping_costs == (1, 2, 2)
    assert expected_depth == Fraction(7, 5)
    assert _edge_frontier_volume(edges, probabilities) == expected_depth
    assert (
        _survival_frontier_integral(stopping_costs, probabilities)
        == expected_depth
    )


def test_nonunit_bellman_cost_is_still_exactly_weighted_frontier_volume():
    probabilities = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    edges = (
        _TreeEdge(Fraction(2), (0,)),
        _TreeEdge(Fraction(1, 2), (1, 2)),
        _TreeEdge(Fraction(3, 2), (1,)),
        _TreeEdge(Fraction(5, 2), (2,)),
    )
    stopping_costs = _path_costs(edges, len(probabilities))
    expected_cost = sum(
        probability * cost
        for probability, cost in zip(probabilities, stopping_costs)
    )

    assert stopping_costs == (2, 2, 3)
    assert expected_cost == Fraction(13, 6)
    assert _edge_frontier_volume(edges, probabilities) == expected_cost
    assert (
        _survival_frontier_integral(stopping_costs, probabilities)
        == expected_cost
    )


def _continuation_signatures(holonomies, futures, observation):
    return {
        holonomy: tuple(
            observation((holonomy + future) % 4)
            for future in futures
        )
        for holonomy in holonomies
    }


def _minimum_exact_memory_bits(signatures):
    continuation_classes = len(set(signatures.values()))
    return (continuation_classes - 1).bit_length()


def test_task_visible_holonomy_forces_continuation_stable_memory():
    # Four lifted histories return to the same visible base state.  Their C4
    # connection holonomies cyclically transport the resource frame.
    holonomies = range(4)
    visible_endpoints = {holonomy: "x" for holonomy in holonomies}
    assert len(set(visible_endpoints.values())) == 1

    full_signatures = _continuation_signatures(
        holonomies,
        range(4),
        observation=lambda transported_frame: transported_frame,
    )
    parity_signatures = _continuation_signatures(
        holonomies,
        range(2),
        observation=lambda transported_frame: transported_frame % 2,
    )
    invariant_signatures = _continuation_signatures(
        holonomies, range(4), observation=lambda _transported_frame: "accepted"
    )

    # Exact frame reconstruction needs four residual states/two bits.  A
    # parity task needs only two states/one bit.  A holonomy-invariant task can
    # forget the entire residual.  Topology alone is therefore not the bound;
    # task-visible continuation classes are.
    assert len(set(full_signatures.values())) == 4
    assert _minimum_exact_memory_bits(full_signatures) == 2
    assert len(set(parity_signatures.values())) == 2
    assert _minimum_exact_memory_bits(parity_signatures) == 1
    assert len(set(invariant_signatures.values())) == 1
    assert _minimum_exact_memory_bits(invariant_signatures) == 0

    # Every pair merged by the visible endpoint quotient has a future witness
    # when the full transported frame is task observable.
    for left in holonomies:
        for right in holonomies:
            if left == right:
                continue
            assert any(
                full_signatures[left][future] != full_signatures[right][future]
                for future in range(4)
            )


def test_complexity_volume_alone_does_not_choose_time_space_polarization():
    physical_time = Fraction(6)
    physical_frontier = Fraction(10)
    time_unit = Fraction(2)
    space_unit = Fraction(5)

    time_count = physical_time / time_unit
    space_count = physical_frontier / space_unit
    volume_count = time_count * space_count

    # Reciprocal rescaling leaves the volume unit fixed while changing both
    # factors.  A process direction, task frontier, and connection are needed
    # to select a time/space split rather than only their product.
    gauge_scale = Fraction(2)
    transformed_time_unit = gauge_scale * time_unit
    transformed_space_unit = space_unit / gauge_scale
    transformed_time_count = physical_time / transformed_time_unit
    transformed_space_count = physical_frontier / transformed_space_unit

    assert transformed_time_count != time_count
    assert transformed_space_count != space_count
    assert transformed_time_count * transformed_space_count == volume_count == 6


def test_nonintegrable_clock_distribution_blocks_global_stopping_slices():
    x, y, z = sp.symbols("x y z", real=True)
    coordinates = (x, y, z)

    # The contact form theta=dz-x*dy annihilates X and Y, but their Lie
    # bracket leaves ker(theta).  By Frobenius, ker(theta) is not tangent to a
    # foliation by global simultaneous/stopping surfaces.
    theta = sp.Matrix([0, -x, 1])
    field_x = sp.Matrix([1, 0, 0])
    field_y = sp.Matrix([0, 1, x])
    bracket = field_y.jacobian(coordinates) * field_x - field_x.jacobian(
        coordinates
    ) * field_y

    assert sp.simplify(theta.dot(field_x)) == 0
    assert sp.simplify(theta.dot(field_y)) == 0
    assert bracket == sp.Matrix([0, 0, 1])
    assert sp.simplify(theta.dot(bracket)) == 1
