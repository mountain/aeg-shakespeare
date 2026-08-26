"""Blind Phase-1B discovery of collision-compatible covector laws.

Discovery sees exact Multiplication histories, pair-product fibres, Addition of
one-site covector values, and positive-rational order.  It does not receive a
logarithm, an entropy formula, a Maxwellian, or held-out counterexamples.

The post-hoc continuous-character oracle is kept in a separate function and is
called only after the finite survivor and simplicity selector are frozen.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
import inspect
import math

import sympy as sp


Exponent = tuple[int, ...]


@dataclass(frozen=True)
class MultiplicativeWorld:
    primes: tuple[int, ...]
    bound: int

    @property
    def points(self) -> tuple[Exponent, ...]:
        coordinates = range(-self.bound, self.bound + 1)
        return tuple(product(coordinates, repeat=len(self.primes)))

    def value(self, exponent: Exponent) -> Fraction:
        if len(exponent) != len(self.primes):
            raise ValueError("exponent dimension must match the prime alphabet")
        result = Fraction(1)
        for prime, power in zip(self.primes, exponent):
            result *= Fraction(prime) ** power
        return result


TRAIN_ONE = MultiplicativeWorld((2,), 2)
TRAIN_TWO = MultiplicativeWorld((2, 3), 2)
HOLDOUT_ORDER = MultiplicativeWorld((2, 3), 3)
HOLDOUT_SIGN = MultiplicativeWorld((2, 3), 4)
HOLDOUT_ALPHABET = MultiplicativeWorld((2, 3, 5), 1)


def _pair_fibre_data(world: MultiplicativeWorld):
    points = world.points
    fibres: dict[Exponent, list[tuple[int, int]]] = {}
    for left, right in combinations_with_replacement(range(len(points)), 2):
        product_exponent = tuple(
            points[left][axis] + points[right][axis]
            for axis in range(len(world.primes))
        )
        fibres.setdefault(product_exponent, []).append((left, right))

    rows: list[list[int]] = []
    for pairs in fibres.values():
        reference = pairs[0]
        for pair in pairs[1:]:
            row = [0] * len(points)
            row[reference[0]] += 1
            row[reference[1]] += 1
            row[pair[0]] -= 1
            row[pair[1]] -= 1
            rows.append(row)

    matrix = sp.Matrix(rows)
    return fibres, matrix


def _affine_value_vectors(world: MultiplicativeWorld) -> tuple[sp.Matrix, ...]:
    points = world.points
    vectors = [sp.Matrix([1] * len(points))]
    vectors.extend(
        sp.Matrix([point[axis] for point in points])
        for axis in range(len(world.primes))
    )
    return tuple(vectors)


def _degree_two_monomials(dimension: int) -> tuple[tuple[int, ...], ...]:
    monomials = [(0,) * dimension]
    for axis in range(dimension):
        powers = [0] * dimension
        powers[axis] = 1
        monomials.append(tuple(powers))
    for left in range(dimension):
        for right in range(left, dimension):
            powers = [0] * dimension
            powers[left] += 1
            powers[right] += 1
            monomials.append(tuple(powers))
    return tuple(monomials)


def _monomial_value(exponent: Exponent, powers: tuple[int, ...]) -> int:
    result = 1
    for coordinate, power in zip(exponent, powers):
        result *= coordinate**power
    return result


def _am_polynomial_basis(world: MultiplicativeWorld):
    monomials = _degree_two_monomials(len(world.primes))
    values = sp.Matrix(
        [
            [_monomial_value(point, powers) for powers in monomials]
            for point in world.points
        ]
    )
    return monomials, values


def _survivor_report(world: MultiplicativeWorld):
    fibres, constraints = _pair_fibre_data(world)
    unrestricted_nullity = len(world.points) - constraints.rank()

    monomials, basis_values = _am_polynomial_basis(world)
    coefficient_constraints = constraints * basis_values
    coefficient_survivors = tuple(coefficient_constraints.nullspace())
    value_survivors = tuple(
        basis_values * survivor for survivor in coefficient_survivors
    )
    native_value_rank = (
        sp.Matrix.hstack(*value_survivors).rank()
        if value_survivors
        else 0
    )
    return {
        "points": len(world.points),
        "unordered_pairs": len(world.points) * (len(world.points) + 1) // 2,
        "fibres": len(fibres),
        "constraint_rank": constraints.rank(),
        "unrestricted_nullity": unrestricted_nullity,
        "monomials": monomials,
        "coefficient_survivors": coefficient_survivors,
        "native_value_rank": native_value_rank,
        "constraints": constraints,
    }


def _strict_order_bounds(world: MultiplicativeWorld) -> tuple[Fraction, Fraction]:
    if world.primes != (2, 3):
        raise ValueError("the normalized two-prime selector expects primes 2 and 3")

    lower: Fraction | None = None
    upper: Fraction | None = None
    points = world.points
    for first, second in combinations(points, 2):
        first_value = world.value(first)
        second_value = world.value(second)
        if first_value == second_value:
            continue
        smaller, larger = (
            (first, second)
            if first_value < second_value
            else (second, first)
        )
        delta_two = larger[0] - smaller[0]
        delta_three = larger[1] - smaller[1]

        # Strict order requires delta_two + r * delta_three > 0.
        if delta_three > 0:
            candidate = Fraction(-delta_two, delta_three)
            lower = candidate if lower is None or candidate > lower else lower
        elif delta_three < 0:
            candidate = Fraction(-delta_two, delta_three)
            upper = candidate if upper is None or candidate < upper else upper
        elif delta_two <= 0:
            raise AssertionError("exact rational order contradicted the 2 direction")

    if lower is None or upper is None or not lower < upper:
        raise AssertionError("training world did not produce a bounded order cone")
    return lower, upper


def _select_simple_rational_weight(
    world: MultiplicativeWorld,
    *,
    numerator_bound: int = 8,
    denominator_bound: int = 8,
) -> Fraction:
    lower, upper = _strict_order_bounds(world)
    candidates = {
        Fraction(numerator, denominator)
        for numerator in range(1, numerator_bound + 1)
        for denominator in range(1, denominator_bound + 1)
        if lower < Fraction(numerator, denominator) < upper
    }
    if not candidates:
        raise ValueError("bounded rational selector found no strict-order candidate")
    return min(
        candidates,
        key=lambda value: (
            value.numerator + value.denominator,
            max(value.numerator, value.denominator),
            value.numerator,
            value.denominator,
        ),
    )


def _character_value(exponent: Exponent, weights) -> object:
    return sum(
        weight * coordinate
        for coordinate, weight in zip(exponent, weights)
    )


def _order_violations(world: MultiplicativeWorld, weights) -> tuple[tuple, ...]:
    violations = []
    for first, second in combinations(world.points, 2):
        first_value = world.value(first)
        second_value = world.value(second)
        if first_value == second_value:
            continue
        smaller, larger = (
            (first, second)
            if first_value < second_value
            else (second, first)
        )
        smaller_character = _character_value(smaller, weights)
        larger_character = _character_value(larger, weights)
        if not smaller_character < larger_character:
            violations.append(
                (
                    smaller,
                    larger,
                    world.value(smaller),
                    world.value(larger),
                    smaller_character,
                    larger_character,
                )
            )
    return tuple(violations)


def _pair_affinity(covector, pair: tuple[int, int]) -> object:
    return covector[pair[0]] + covector[pair[1]]


def _continuous_character_oracle_ratio() -> float:
    """Post-hoc classical oracle; forbidden to discovery and selection."""

    return math.log(3) / math.log(2)


VELOCITIES = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
)
COMPLEXES = ((0, 3), (1, 4), (2, 5))
CHANNEL_COMPLEXES = ((0, 1), (1, 2), (2, 0))


def _stoichiometric_matrix() -> sp.Matrix:
    columns = []
    for incoming_complex, outgoing_complex in CHANNEL_COMPLEXES:
        column = [0] * len(VELOCITIES)
        for species in COMPLEXES[incoming_complex]:
            column[species] -= 1
        for species in COMPLEXES[outgoing_complex]:
            column[species] += 1
        columns.append(column)
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))


def _channel_affinities(covector: sp.Matrix) -> tuple[object, ...]:
    return tuple(
        _pair_affinity(covector, COMPLEXES[outgoing])
        - _pair_affinity(covector, COMPLEXES[incoming])
        for incoming, outgoing in CHANNEL_COMPLEXES
    )


def test_unrestricted_fibre_search_discovers_only_affine_characters():
    expected = (
        (TRAIN_ONE, 5, 15, 9, 3, 2),
        (TRAIN_TWO, 25, 325, 81, 22, 3),
        (HOLDOUT_ALPHABET, 27, 378, 125, 23, 4),
    )
    for world, points, pairs, fibres, rank, nullity in expected:
        report = _survivor_report(world)
        assert report["points"] == points
        assert report["unordered_pairs"] == pairs
        assert report["fibres"] == fibres
        assert report["constraint_rank"] == rank
        assert report["unrestricted_nullity"] == nullity

        affine_vectors = _affine_value_vectors(world)
        constraints = report["constraints"]
        assert all(constraints * vector == sp.zeros(constraints.rows, 1) for vector in affine_vectors)
        assert sp.Matrix.hstack(*affine_vectors).rank() == nullity


def test_degree_two_am_grammar_covers_the_unrestricted_survivor_space():
    expected_monomials_and_survivors = (
        (TRAIN_ONE, 3, 2),
        (TRAIN_TWO, 6, 3),
        (HOLDOUT_ALPHABET, 10, 4),
    )
    for world, monomial_count, survivor_count in expected_monomials_and_survivors:
        report = _survivor_report(world)
        assert len(report["monomials"]) == monomial_count
        assert len(report["coefficient_survivors"]) == survivor_count
        assert report["native_value_rank"] == report["unrestricted_nullity"]

        linear_cutoff = 1 + len(world.primes)
        for survivor in report["coefficient_survivors"]:
            assert all(
                coefficient == 0
                for coefficient in survivor[linear_cutoff:, :]
            )


def test_discovery_source_is_separate_from_the_continuous_log_oracle():
    discovery_functions = (
        _pair_fibre_data,
        _affine_value_vectors,
        _degree_two_monomials,
        _am_polynomial_basis,
        _survivor_report,
        _strict_order_bounds,
        _select_simple_rational_weight,
        _character_value,
        _order_violations,
    )
    source = "\n".join(inspect.getsource(function) for function in discovery_functions)
    assert "math.log" not in source
    assert "_continuous_character_oracle_ratio" not in source


def test_frozen_training_selector_is_unique_but_fails_held_out_order():
    assert _strict_order_bounds(TRAIN_TWO) == (Fraction(3, 2), Fraction(2))
    selected = _select_simple_rational_weight(TRAIN_TWO)
    assert selected == Fraction(5, 3)
    assert _order_violations(TRAIN_TWO, (Fraction(1), selected)) == ()

    equality_witness = ((-2, 3), (3, 0))
    smaller, larger = equality_witness
    assert HOLDOUT_ORDER.value(smaller) < HOLDOUT_ORDER.value(larger)
    assert _character_value(smaller, (Fraction(1), selected)) == _character_value(
        larger, (Fraction(1), selected)
    )
    assert equality_witness in {
        (violation[0], violation[1])
        for violation in _order_violations(
            HOLDOUT_ORDER, (Fraction(1), selected)
        )
    }


def test_frozen_training_selector_produces_a_positive_h_rate_on_larger_holdout():
    selected = _select_simple_rational_weight(TRAIN_TWO)
    smaller = (-4, 1)
    larger = (4, -4)
    assert HOLDOUT_SIGN.value(smaller) < HOLDOUT_SIGN.value(larger)

    smaller_character = _character_value(
        smaller, (Fraction(1), selected)
    )
    larger_character = _character_value(
        larger, (Fraction(1), selected)
    )
    assert smaller_character > larger_character

    incoming_activity = HOLDOUT_SIGN.value(smaller)
    outgoing_activity = HOLDOUT_SIGN.value(larger)
    flux_affinity_product = (
        (incoming_activity - outgoing_activity)
        * (smaller_character - larger_character)
    )
    h_rate = -flux_affinity_product
    assert flux_affinity_product < 0
    assert h_rate > 0


def test_nested_exact_order_cones_tighten_without_finite_uniqueness():
    expected = {
        1: (Fraction(1), Fraction(2)),
        2: (Fraction(3, 2), Fraction(2)),
        3: (Fraction(3, 2), Fraction(5, 3)),
        4: (Fraction(3, 2), Fraction(8, 5)),
        5: (Fraction(3, 2), Fraction(8, 5)),
        6: (Fraction(11, 7), Fraction(8, 5)),
    }
    actual = {
        bound: _strict_order_bounds(MultiplicativeWorld((2, 3), bound))
        for bound in expected
    }
    assert actual == expected
    assert all(lower < upper for lower, upper in actual.values())


def test_post_hoc_continuous_character_oracle_lies_in_every_order_cone():
    oracle_ratio = _continuous_character_oracle_ratio()
    for bound in range(1, 7):
        lower, upper = _strict_order_bounds(MultiplicativeWorld((2, 3), bound))
        assert float(lower) < oracle_ratio < float(upper)

    assert _order_violations(
        HOLDOUT_SIGN, (1.0, oracle_ratio)
    ) == ()

    for exponent in HOLDOUT_ALPHABET.points:
        via_weights = sum(
            coordinate * math.log(prime)
            for coordinate, prime in zip(exponent, HOLDOUT_ALPHABET.primes)
        )
        via_value = math.log(float(HOLDOUT_ALPHABET.value(exponent)))
        assert abs(via_weights - via_value) < 1e-12


def test_conserved_affine_gauge_is_exactly_mass_plus_three_momenta():
    stoichiometry = _stoichiometric_matrix()
    left_kernel = tuple(stoichiometry.T.nullspace())
    assert stoichiometry.rank() == 2
    assert len(left_kernel) == 4

    declared = (
        sp.Matrix([1] * 6),
        *(sp.Matrix([velocity[axis] for velocity in VELOCITIES]) for axis in range(3)),
    )
    assert all(stoichiometry.T * vector == sp.zeros(3, 1) for vector in declared)
    assert sp.Matrix.hstack(*declared).rank() == 4

    raw_covector = sp.Matrix((2, 3, 5, 7, 11, 13))
    raw_affinities = _channel_affinities(raw_covector)
    for gauge in declared:
        assert _channel_affinities(raw_covector + gauge) == raw_affinities


def test_constant_and_positive_scale_are_distinct_covector_gauges():
    covector = sp.Matrix((1, 4, 2, 8, 3, 9))
    constant_shift = sp.Matrix([7] * 6)
    affinities = _channel_affinities(covector)

    assert _channel_affinities(covector + constant_shift) == affinities
    assert _channel_affinities(3 * covector) == tuple(
        3 * affinity for affinity in affinities
    )


def test_negative_character_orientation_reverses_the_h_sign():
    incoming_activity = Fraction(1)
    outgoing_activity = Fraction(2)
    positive_incoming_covector = Fraction(0)
    positive_outgoing_covector = Fraction(1)

    positive_pairing = (
        (incoming_activity - outgoing_activity)
        * (positive_incoming_covector - positive_outgoing_covector)
    )
    negative_pairing = (
        (incoming_activity - outgoing_activity)
        * (-positive_incoming_covector + positive_outgoing_covector)
    )
    assert positive_pairing > 0
    assert -positive_pairing < 0
    assert negative_pairing < 0
    assert -negative_pairing > 0

