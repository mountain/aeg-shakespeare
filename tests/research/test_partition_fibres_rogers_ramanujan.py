"""Phase 12B: partition fibres and the Rogers--Ramanujan bridge.

The executable essay has three deliberately ordered parts:

* B0 treats the Rogers--Ramanujan continued fraction as a nonhomogeneous
  projective recursion and keeps its root cover explicit;
* B1 proves that compositions abelianize to the free commutative partition
  monoid and that total weight is a strict all-composite lowering;
* B2 checks bounded Rogers--Ramanujan coefficient identities while refusing to
  infer a uniform bijection or preservation of native composition.

All calculations use integers and ``Fraction``.  Infinite identities and
convergence remain cited classical controls rather than claims of this file.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


_Composition = tuple[int, ...]
_Partition = tuple[int, ...]
_Polynomial = dict[int, int]
_PolyMatrix = tuple[
    tuple[_Polynomial, _Polynomial],
    tuple[_Polynomial, _Polynomial],
]

_ZERO_POLY: _Polynomial = {}
_ONE_POLY: _Polynomial = {0: 1}


def _poly_add(left: _Polynomial, right: _Polynomial) -> _Polynomial:
    result = {
        exponent: left.get(exponent, 0) + right.get(exponent, 0)
        for exponent in left.keys() | right.keys()
    }
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient
    }


def _poly_mul(
    left: _Polynomial,
    right: _Polynomial,
    maximum: int | None = None,
) -> _Polynomial:
    result: _Polynomial = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            if maximum is None or exponent <= maximum:
                result[exponent] = result.get(exponent, 0) + (
                    left_coefficient * right_coefficient
                )
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient
    }


def _poly_shift(polynomial: _Polynomial, shift: int) -> _Polynomial:
    return {
        exponent + shift: coefficient
        for exponent, coefficient in polynomial.items()
    }


def _matmul(left: _PolyMatrix, right: _PolyMatrix) -> _PolyMatrix:
    return (
        (
            _poly_add(
                _poly_mul(left[0][0], right[0][0]),
                _poly_mul(left[0][1], right[1][0]),
            ),
            _poly_add(
                _poly_mul(left[0][0], right[0][1]),
                _poly_mul(left[0][1], right[1][1]),
            ),
        ),
        (
            _poly_add(
                _poly_mul(left[1][0], right[0][0]),
                _poly_mul(left[1][1], right[1][0]),
            ),
            _poly_add(
                _poly_mul(left[1][0], right[0][1]),
                _poly_mul(left[1][1], right[1][1]),
            ),
        ),
    )


def _step_matrix(depth: int) -> _PolyMatrix:
    return (
        (_ONE_POLY, {depth: 1}),
        (_ONE_POLY, _ZERO_POLY),
    )


def _matrix_convergent(depth: int) -> tuple[_Polynomial, _Polynomial]:
    matrix: _PolyMatrix = (
        (_ONE_POLY, _ZERO_POLY),
        (_ZERO_POLY, _ONE_POLY),
    )
    for index in range(1, depth + 1):
        matrix = _matmul(matrix, _step_matrix(index))
    numerator = _poly_add(matrix[0][0], matrix[0][1])
    denominator = _poly_add(matrix[1][0], matrix[1][1])
    return numerator, denominator


def _tail_convergent(depth: int) -> tuple[_Polynomial, _Polynomial]:
    numerator = _ONE_POLY
    denominator = _ONE_POLY
    for index in range(depth, 0, -1):
        numerator, denominator = (
            _poly_add(numerator, _poly_shift(denominator, index)),
            numerator,
        )
    return numerator, denominator


def _continuant_convergent(depth: int) -> tuple[_Polynomial, _Polynomial]:
    numerator_two_back, numerator_one_back = _ONE_POLY, _ONE_POLY
    denominator_two_back, denominator_one_back = _ZERO_POLY, _ONE_POLY
    for index in range(1, depth + 1):
        numerator = _poly_add(
            numerator_one_back,
            _poly_shift(numerator_two_back, index),
        )
        denominator = _poly_add(
            denominator_one_back,
            _poly_shift(denominator_two_back, index),
        )
        numerator_two_back, numerator_one_back = numerator_one_back, numerator
        denominator_two_back, denominator_one_back = (
            denominator_one_back,
            denominator,
        )
    return numerator_one_back, denominator_one_back


def _rational_series(
    numerator: _Polynomial,
    denominator: _Polynomial,
    maximum: int,
) -> tuple[Fraction, ...]:
    constant = denominator.get(0, 0)
    if constant == 0:
        raise ValueError("the denominator must have a nonzero constant term")
    output: list[Fraction] = []
    for degree in range(maximum + 1):
        known = sum(
            Fraction(denominator.get(index, 0)) * output[degree - index]
            for index in range(1, degree + 1)
        )
        output.append((Fraction(numerator.get(degree, 0)) - known) / constant)
    return tuple(output)


def _compositions(weight: int) -> tuple[_Composition, ...]:
    if weight == 0:
        return ((),)
    return tuple(
        (first, *tail)
        for first in range(1, weight + 1)
        for tail in _compositions(weight - first)
    )


def _partitions(weight: int, maximum: int | None = None) -> tuple[_Partition, ...]:
    if weight == 0:
        return ((),)
    upper = weight if maximum is None else min(weight, maximum)
    return tuple(
        (first, *tail)
        for first in range(upper, 0, -1)
        for tail in _partitions(weight - first, first)
    )


def _abelianize(composition: _Composition) -> _Partition:
    return tuple(sorted(composition, reverse=True))


def _union(left: _Partition, right: _Partition) -> _Partition:
    return tuple(sorted((*left, *right), reverse=True))


def _weight(partition: _Partition) -> int:
    return sum(partition)


def _conjugate(partition: _Partition) -> _Partition:
    if not partition:
        return ()
    return tuple(
        sum(part >= column for part in partition)
        for column in range(1, partition[0] + 1)
    )


def _multiplicities(partition: _Partition) -> tuple[tuple[int, int], ...]:
    return tuple(
        (part, partition.count(part))
        for part in sorted(set(partition))
    )


def _occupation_coefficients(
    maximum: int,
    allowed_parts: tuple[int, ...] | None = None,
) -> tuple[int, ...]:
    coefficients = [1] + [0] * maximum
    parts = allowed_parts if allowed_parts is not None else tuple(range(1, maximum + 1))
    for part in parts:
        for total in range(part, maximum + 1):
            coefficients[total] += coefficients[total - part]
    return tuple(coefficients)


def _shifted_sum(
    target: list[int],
    source: tuple[int, ...],
    shift: int,
) -> None:
    for degree, coefficient in enumerate(source):
        if shift + degree < len(target):
            target[shift + degree] += coefficient


def _rogers_ramanujan_series(maximum: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    first = [0] * (maximum + 1)
    second = [0] * (maximum + 1)
    for index in range(maximum + 1):
        if index * index > maximum and index * (index + 1) > maximum:
            break
        bounded = _occupation_coefficients(maximum, tuple(range(1, index + 1)))
        _shifted_sum(first, bounded, index * index)
        _shifted_sum(second, bounded, index * (index + 1))
    return tuple(first), tuple(second)


def _difference_two(partition: _Partition) -> bool:
    return all(left - right >= 2 for left, right in zip(partition, partition[1:]))


def _residue_allowed(partition: _Partition, residues: frozenset[int]) -> bool:
    return all(part % 5 in residues for part in partition)


def test_b0_nonhomogeneous_matrix_tail_and_continuant_recursions_agree():
    for depth in range(1, 13):
        matrix = _matrix_convergent(depth)
        tail = _tail_convergent(depth)
        continuant = _continuant_convergent(depth)
        assert matrix == tail == continuant

    assert _matrix_convergent(1) == ({0: 1, 1: 1}, {0: 1})
    assert _matrix_convergent(2) == (
        {0: 1, 1: 1, 2: 1},
        {0: 1, 2: 1},
    )


def test_b0_projective_ratio_and_root_cover_are_typed_separately():
    # On r=q^(1/60), Phi=(r^-1 G(r^60), r^11 H(r^60)).  The ratio forgets a
    # common scale and has exponent difference 12, i.e. q^(1/5).
    phi_exponents = (-1, 11)
    assert phi_exponents[1] - phi_exponents[0] == 12
    assert Fraction(12, 60) == Fraction(1, 5)
    for common_scale in (-7, 0, 13):
        shifted = tuple(exponent + common_scale for exponent in phi_exponents)
        assert shifted[1] - shifted[0] == 12

    # The finite projective readout B_N/A_N approaches H/G formally.  The first
    # omitted contribution occurs at triangular degree (N+1)(N+2)/2; agreement
    # of a long prefix still does not identify the history or lifted carrier.
    maximum = 40
    first, second = _rogers_ramanujan_series(maximum)
    infinite_ratio = _rational_series(
        dict(enumerate(second)),
        dict(enumerate(first)),
        maximum,
    )
    for depth in range(1, 13):
        numerator, denominator = _matrix_convergent(depth)
        finite_ratio = _rational_series(denominator, numerator, maximum)
        first_omitted = (depth + 1) * (depth + 2) // 2
        compared = min(first_omitted, maximum + 1)
        assert finite_ratio[:compared] == infinite_ratio[:compared]
        if first_omitted <= maximum:
            assert finite_ratio[first_omitted] != infinite_ratio[first_omitted]


def test_b1_compositions_abelianize_to_a_free_commutative_partition_monoid():
    for weight in range(13):
        compositions = _compositions(weight)
        partitions = _partitions(weight)
        if weight:
            assert len(compositions) == 2 ** (weight - 1)
        else:
            assert compositions == ((),)
        assert {_abelianize(item) for item in compositions} == set(partitions)
        assert all(_weight(partition) == weight for partition in partitions)
        assert len({_multiplicities(partition) for partition in partitions}) == len(
            partitions
        )

    corpus = tuple(
        partition
        for weight in range(7)
        for partition in _partitions(weight)
    )
    for left, right in product(corpus, repeat=2):
        assert _weight(_union(left, right)) == _weight(left) + _weight(right)

    compositions = tuple(
        composition
        for weight in range(7)
        for composition in _compositions(weight)
    )
    for left, right in product(compositions, repeat=2):
        assert _abelianize(left + right) == _union(
            _abelianize(left),
            _abelianize(right),
        )


def test_b1_euler_pushforward_and_shape_observer_boundaries():
    maximum = 30
    fibre_counts = tuple(len(_partitions(weight)) for weight in range(maximum + 1))
    occupation_counts = _occupation_coefficients(maximum)
    assert fibre_counts == occupation_counts
    assert fibre_counts[:11] == (1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42)

    same_weight = ((4,), (2, 1, 1))
    assert {_weight(partition) for partition in same_weight} == {4}
    assert {len(partition) for partition in same_weight} == {1, 3}
    assert {partition[0] for partition in same_weight} == {2, 4}

    for weight in range(13):
        for partition in _partitions(weight):
            conjugate = _conjugate(partition)
            assert _conjugate(conjugate) == partition
            assert _weight(conjugate) == weight
            if partition:
                assert len(conjugate) == partition[0]
                assert conjugate[0] == len(partition)

    left, right = (2,), (1,)
    assert _conjugate(_union(left, right)) != _union(
        _conjugate(left),
        _conjugate(right),
    )


def test_b2_restricted_fibres_match_counts_but_not_native_composition():
    maximum = 30
    difference_one = []
    product_one = []
    difference_two = []
    product_two = []
    for weight in range(maximum + 1):
        partitions = _partitions(weight)
        difference_one.append(sum(_difference_two(item) for item in partitions))
        product_one.append(
            sum(_residue_allowed(item, frozenset({1, 4})) for item in partitions)
        )
        difference_two.append(
            sum(
                _difference_two(item) and (not item or item[-1] >= 2)
                for item in partitions
            )
        )
        product_two.append(
            sum(_residue_allowed(item, frozenset({2, 3})) for item in partitions)
        )

    assert difference_one == product_one
    assert difference_two == product_two

    # Product-side residue families are free commutative submonoids.  The
    # difference-side families are not closed under their native union.
    assert _residue_allowed(_union((1,), (4,)), frozenset({1, 4}))
    assert _residue_allowed(_union((2,), (3,)), frozenset({2, 3}))
    assert _difference_two((1,)) and not _difference_two(_union((1,), (1,)))
    assert _difference_two((2,)) and not _difference_two(_union((2,), (2,)))


def test_b2_q_series_products_and_projective_shadow_agree_on_frozen_degree():
    maximum = 40
    first_series, second_series = _rogers_ramanujan_series(maximum)
    first_product = _occupation_coefficients(
        maximum,
        tuple(part for part in range(1, maximum + 1) if part % 5 in {1, 4}),
    )
    second_product = _occupation_coefficients(
        maximum,
        tuple(part for part in range(1, maximum + 1) if part % 5 in {2, 3}),
    )
    assert first_series == first_product
    assert second_series == second_product

    ratio = _rational_series(
        dict(enumerate(second_series)),
        dict(enumerate(first_series)),
        maximum,
    )
    assert ratio[:10] == tuple(
        map(Fraction, (1, -1, 1, 0, -1, 1, -1, 1, 0, -1))
    )


def test_b2_claim_strength_and_objectification_boundary_are_explicit():
    verdict = {
        "bounded_scalar_presentations_match": True,
        "bounded_fibre_cardinalities_match": True,
        "uniform_explicit_fibre_bijection_supplied": False,
        "native_composition_preserved_across_restricted_families": False,
        "partition_is_free_commutative": True,
        "weight_lowering_is_all_composite": True,
        "strict_compositional_quotient": True,
        "fibred_task_exact_objectification": True,
        "strict_conservative_objectification": False,
        "new_vertical_rank_earned": False,
        "public_api_pressure": False,
    }
    assert verdict["bounded_scalar_presentations_match"]
    assert verdict["bounded_fibre_cardinalities_match"]
    assert not verdict["uniform_explicit_fibre_bijection_supplied"]
    assert not verdict["native_composition_preserved_across_restricted_families"]
    assert verdict["strict_compositional_quotient"]
    assert verdict["fibred_task_exact_objectification"]
    assert not verdict["strict_conservative_objectification"]
    assert not verdict["new_vertical_rank_earned"]
    assert not verdict["public_api_pressure"]
