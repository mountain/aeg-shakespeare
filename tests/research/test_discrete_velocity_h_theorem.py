"""Exact Phase-1A calibration for a finite discrete-velocity H theorem.

The frozen six-velocity network is a reversible mass-action calibration, not
finite-N hard-sphere dynamics.  The relative H functional is supplied to this
phase, so these tests establish reexpression and red-team boundaries only;
they do not establish discovery, molecular chaos, or a Boltzmann-Grad limit.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

import pytest
import sympy as sp


Velocity = tuple[int, int, int]
Pair = tuple[int, int]


VELOCITIES: tuple[Velocity, ...] = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
)
PAIR_X = (0, 3)
PAIR_Y = (1, 4)
PAIR_Z = (2, 5)
REFERENCE = tuple(map(Fraction, (1, 2, 3, 6, 3, 2)))


@dataclass(frozen=True)
class CollisionChannel:
    incoming: Pair
    outgoing: Pair
    conductance: Fraction

    def reversed(self) -> "CollisionChannel":
        return CollisionChannel(
            incoming=self.outgoing,
            outgoing=self.incoming,
            conductance=self.conductance,
        )


CHANNELS = (
    CollisionChannel(PAIR_X, PAIR_Y, Fraction(1)),
    CollisionChannel(PAIR_Y, PAIR_Z, Fraction(2)),
    CollisionChannel(PAIR_Z, PAIR_X, Fraction(3)),
)


def _pair_product(values, pair: Pair):
    return values[pair[0]] * values[pair[1]]


def _pair_momentum(pair: Pair) -> Velocity:
    return tuple(
        VELOCITIES[pair[0]][axis] + VELOCITIES[pair[1]][axis]
        for axis in range(3)
    )


def _pair_kinetic_label(pair: Pair) -> int:
    return sum(
        sum(component * component for component in VELOCITIES[index])
        for index in pair
    )


def _validate_reference(
    channels: tuple[CollisionChannel, ...],
    reference: tuple[Fraction, ...],
) -> None:
    if len(reference) != len(VELOCITIES) or any(weight <= 0 for weight in reference):
        raise ValueError("reference weights must be positive on all velocities")
    for channel in channels:
        if _pair_product(reference, channel.incoming) != _pair_product(
            reference, channel.outgoing
        ):
            raise ValueError("reference weights violate channel detailed balance")


def _relative_activities(
    populations: tuple[Fraction, ...],
    reference: tuple[Fraction, ...] = REFERENCE,
) -> tuple[Fraction, ...]:
    if len(populations) != len(reference):
        raise ValueError("population and reference dimensions must agree")
    if any(population < 0 for population in populations):
        raise ValueError("populations must be nonnegative")
    return tuple(
        population / weight
        for population, weight in zip(populations, reference)
    )


def _channel_flux(
    populations: tuple[Fraction, ...],
    channel: CollisionChannel,
    reference: tuple[Fraction, ...] = REFERENCE,
) -> Fraction:
    activities = _relative_activities(populations, reference)
    incoming = _pair_product(activities, channel.incoming)
    outgoing = _pair_product(activities, channel.outgoing)
    return channel.conductance * (incoming - outgoing)


def _collision_derivative(
    populations: tuple[Fraction, ...],
    channels: tuple[CollisionChannel, ...] = CHANNELS,
    reference: tuple[Fraction, ...] = REFERENCE,
) -> tuple[Fraction, ...]:
    derivative = [Fraction(0) for _ in populations]
    for channel in channels:
        flux = _channel_flux(populations, channel, reference)
        for index in channel.incoming:
            derivative[index] -= flux
        for index in channel.outgoing:
            derivative[index] += flux
    return tuple(derivative)


def _dissipation_terms(
    populations: tuple[Fraction, ...],
    channels: tuple[CollisionChannel, ...] = CHANNELS,
    reference: tuple[Fraction, ...] = REFERENCE,
) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    if any(population <= 0 for population in populations):
        raise ValueError("the logarithmic dissipation certificate is interior-only")
    activities = _relative_activities(populations, reference)
    return tuple(
        (
            channel.conductance,
            _pair_product(activities, channel.incoming),
            _pair_product(activities, channel.outgoing),
        )
        for channel in channels
    )


def _log_monotonicity_certificate(left: Fraction, right: Fraction) -> bool:
    """Certify ``(left-right)(log(left)-log(right)) >= 0`` by exact order."""

    if left <= 0 or right <= 0:
        raise ValueError("logarithmic activities must be positive")
    if left == right:
        return True
    larger, smaller = (left, right) if left > right else (right, left)
    ratio = sp.Rational(larger.numerator, larger.denominator) / sp.Rational(
        smaller.numerator, smaller.denominator
    )
    return ratio > 1 and sp.log(ratio).is_positive is True


def _h_rate_expression(
    populations: tuple[Fraction, ...],
    channels: tuple[CollisionChannel, ...] = CHANNELS,
    reference: tuple[Fraction, ...] = REFERENCE,
):
    result = sp.Integer(0)
    for conductance, incoming, outgoing in _dissipation_terms(
        populations, channels, reference
    ):
        c = sp.Rational(conductance.numerator, conductance.denominator)
        left = sp.Rational(incoming.numerator, incoming.denominator)
        right = sp.Rational(outgoing.numerator, outgoing.denominator)
        result -= c * (left - right) * (sp.log(left) - sp.log(right))
    return sp.expand_log(result, force=True)


def _componentwise_activity_equality(
    populations: tuple[Fraction, ...],
    channels: tuple[CollisionChannel, ...],
    reference: tuple[Fraction, ...] = REFERENCE,
) -> bool:
    activities = _relative_activities(populations, reference)
    pair_activities = {
        pair: _pair_product(activities, pair)
        for channel in channels
        for pair in (channel.incoming, channel.outgoing)
    }
    adjacency = {pair: set() for pair in pair_activities}
    for channel in channels:
        adjacency[channel.incoming].add(channel.outgoing)
        adjacency[channel.outgoing].add(channel.incoming)

    unseen = set(adjacency)
    while unseen:
        seed = unseen.pop()
        stack = [seed]
        component = {seed}
        while stack:
            current = stack.pop()
            for neighbour in adjacency[current]:
                if neighbour not in component:
                    component.add(neighbour)
                    unseen.discard(neighbour)
                    stack.append(neighbour)
        if len({pair_activities[pair] for pair in component}) != 1:
            return False
    return True


def _populations_from_relative(
    activities: tuple[int | Fraction, ...],
    reference: tuple[Fraction, ...] = REFERENCE,
) -> tuple[Fraction, ...]:
    return tuple(
        weight * Fraction(activity)
        for weight, activity in zip(reference, activities)
    )


def test_frozen_velocity_channels_are_reversible_and_conservative():
    assert len(VELOCITIES) == 6
    assert len(CHANNELS) == 3
    assert {channel.incoming for channel in CHANNELS} == {PAIR_X, PAIR_Y, PAIR_Z}

    for channel in CHANNELS:
        assert channel.conductance > 0
        assert channel.reversed().reversed() == channel
        assert _pair_momentum(channel.incoming) == _pair_momentum(channel.outgoing)
        assert _pair_kinetic_label(channel.incoming) == _pair_kinetic_label(
            channel.outgoing
        )
        assert len(set((*channel.incoming, *channel.outgoing))) == 4

    populations = _populations_from_relative((1, 2, 3, 4, 5, 6))
    derivative = _collision_derivative(populations)
    assert sum(derivative) == 0
    for axis in range(3):
        assert sum(
            derivative[index] * VELOCITIES[index][axis]
            for index in range(len(VELOCITIES))
        ) == 0
    assert sum(
        derivative[index]
        * sum(component * component for component in VELOCITIES[index])
        for index in range(len(VELOCITIES))
    ) == 0


def test_frozen_reference_has_exact_detailed_balance():
    _validate_reference(CHANNELS, REFERENCE)
    assert {
        _pair_product(REFERENCE, pair)
        for pair in (PAIR_X, PAIR_Y, PAIR_Z)
    } == {Fraction(6)}


def test_reversing_channel_orientation_preserves_the_vector_field():
    samples = (
        _populations_from_relative((1, 2, 3, 4, 5, 6)),
        _populations_from_relative((2, 3, 5, 15, 10, 6)),
        tuple(map(Fraction, (1, 0, 2, 3, 4, 5))),
    )
    reversed_channels = tuple(channel.reversed() for channel in CHANNELS)
    for populations in samples:
        assert _collision_derivative(populations) == _collision_derivative(
            populations, reversed_channels
        )


def test_symbolic_channel_derivative_is_flux_times_affinity():
    q_a, q_b, q_c, q_d, conductance = sp.symbols(
        "q_a q_b q_c q_d c", positive=True
    )
    incoming = q_a * q_b
    outgoing = q_c * q_d
    flux = conductance * (incoming - outgoing)
    via_covector = flux * (
        sp.log(q_c) + sp.log(q_d) - sp.log(q_a) - sp.log(q_b)
    )
    expected = -conductance * (incoming - outgoing) * (
        sp.log(incoming) - sp.log(outgoing)
    )
    assert sp.simplify(
        via_covector - sp.expand_log(expected, force=True)
    ) == 0


def test_exact_rational_h_rate_is_nonpositive_with_componentwise_equality():
    nonstationary = _populations_from_relative((1, 2, 3, 4, 5, 6))
    terms = _dissipation_terms(nonstationary)
    assert all(
        _log_monotonicity_certificate(incoming, outgoing)
        for _, incoming, outgoing in terms
    )
    assert any(incoming != outgoing for _, incoming, outgoing in terms)
    assert _h_rate_expression(nonstationary).is_negative is True
    assert not _componentwise_activity_equality(nonstationary, CHANNELS)

    stationary = _populations_from_relative((2, 3, 5, 15, 10, 6))
    assert {
        _pair_product(_relative_activities(stationary), pair)
        for pair in (PAIR_X, PAIR_Y, PAIR_Z)
    } == {Fraction(30)}
    assert _collision_derivative(stationary) == (Fraction(0),) * 6
    assert _h_rate_expression(stationary) == 0
    assert _componentwise_activity_equality(stationary, CHANNELS)


def test_red_team_two_way_rates_without_detailed_balance_can_increase_h():
    incoming = Fraction(1)
    outgoing = Fraction(3, 2)
    forward_rate = Fraction(2)
    reverse_rate = Fraction(1)
    flux = forward_rate * incoming - reverse_rate * outgoing
    h_rate = sp.Rational(flux.numerator, flux.denominator) * sp.log(
        sp.Rational(outgoing.numerator, outgoing.denominator)
        / sp.Rational(incoming.numerator, incoming.denominator)
    )

    assert forward_rate > 0 and reverse_rate > 0
    assert flux == Fraction(1, 2)
    assert outgoing > incoming
    assert h_rate.is_positive is True


def test_red_team_mismatched_reference_is_rejected():
    bad_reference = list(REFERENCE)
    bad_reference[5] = Fraction(1)
    assert _pair_product(tuple(bad_reference), PAIR_Z) == 3
    assert _pair_product(tuple(bad_reference), PAIR_X) == 6
    with pytest.raises(ValueError, match="detailed balance"):
        _validate_reference(CHANNELS, tuple(bad_reference))


def test_red_team_equality_is_only_componentwise_when_graph_is_disconnected():
    disconnected = (CHANNELS[0],)
    populations = _populations_from_relative((1, 1, 1, 2, 2, 5))
    relative = _relative_activities(populations)
    assert _pair_product(relative, PAIR_X) == _pair_product(relative, PAIR_Y) == 2
    assert _pair_product(relative, PAIR_Z) == 5
    assert _collision_derivative(populations, disconnected) == (Fraction(0),) * 6
    assert _componentwise_activity_equality(populations, disconnected)
    assert _collision_derivative(populations, CHANNELS) != (Fraction(0),) * 6
    assert not _componentwise_activity_equality(populations, CHANNELS)


def test_red_team_zero_population_faces_have_inward_vector_field():
    for raw_populations in product(range(3), repeat=6):
        populations = tuple(map(Fraction, raw_populations))
        derivative = _collision_derivative(populations)
        for population, rate in zip(populations, derivative):
            if population == 0:
                assert rate >= 0

    with pytest.raises(ValueError, match="interior-only"):
        _dissipation_terms(tuple(map(Fraction, (0, 1, 1, 1, 1, 1))))


def test_entropy_sign_is_opposite_to_h_sign():
    populations = _populations_from_relative((1, 2, 3, 4, 5, 6))
    h_rate = _h_rate_expression(populations)
    boltzmann_constant = sp.Rational(3, 2)
    entropy_rate = -boltzmann_constant * h_rate

    assert h_rate.is_negative is True
    assert entropy_rate.is_positive is True

