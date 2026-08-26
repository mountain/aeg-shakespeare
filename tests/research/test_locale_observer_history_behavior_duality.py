"""Phase 12A: strict descent obstructions and fibred finite parts.

This exact executable essay records two minimal failures of strict semantic
descent and the task-relative repairs:

* ordinary addition is not a frame-forgetting PGL_2-equivariant operation;
* a finite part is not invariant under forgetting a singularity chart;
* frame-indexed addition transports exactly;
* a bounded principal part and chart jet transport a bounded-pole finite part;
* Bernoulli values arise as exponential-chart coefficients for the rational
  power-sum germs;
* the fixed-contract finite part is linear but not a global arithmetic map.

All arithmetic is exact and research-local.  No zeta continuation theorem,
vertical objectification, or package API is claimed.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial


_ProjectivePoint = Fraction | None
_Mobius = tuple[Fraction, Fraction, Fraction, Fraction]
_Series = dict[int, Fraction]


def _mobius(matrix: _Mobius, point: _ProjectivePoint) -> _ProjectivePoint:
    a, b, c, d = matrix
    if point is None:
        return None if c == 0 else a / c
    denominator = c * point + d
    if denominator == 0:
        return None
    return (a * point + b) / denominator


def _inverse(matrix: _Mobius) -> _Mobius:
    a, b, c, d = matrix
    if a * d - b * c == 0:
        raise ValueError("a projective transformation must be nonsingular")
    return (d, -b, -c, a)


def _transported_addition(
    matrix: _Mobius,
    left: _ProjectivePoint,
    right: _ProjectivePoint,
) -> _ProjectivePoint:
    inverse = _inverse(matrix)
    source_left = _mobius(inverse, left)
    source_right = _mobius(inverse, right)
    if source_left is None or source_right is None:
        raise ValueError("addition is defined only on the transported affine chart")
    return _mobius(matrix, source_left + source_right)


def _bernoulli_numbers(count: int) -> tuple[Fraction, ...]:
    values = [Fraction(1)]
    for n in range(1, count):
        values.append(
            -sum(comb(n + 1, k) * values[k] for k in range(n))
            / Fraction(n + 1)
        )
    return tuple(values)


def _second_order_finite_part(
    pole_two: Fraction,
    pole_one: Fraction,
    finite: Fraction,
    alpha: Fraction,
    beta: Fraction,
    gamma: Fraction,
) -> Fraction:
    """Transport a finite part through u=alpha*t+beta*t^2+gamma*t^3+O(t^4)."""

    if alpha == 0:
        raise ValueError("a chart transition must have a nonzero linear term")
    inverse_constant = -beta / alpha**2
    inverse_square_constant = 3 * beta**2 / alpha**4 - 2 * gamma / alpha**3
    return finite + pole_one * inverse_constant + pole_two * inverse_square_constant


def _add(left: _Series, right: _Series) -> _Series:
    result = {
        exponent: left.get(exponent, Fraction(0))
        + right.get(exponent, Fraction(0))
        for exponent in left.keys() | right.keys()
    }
    return {exponent: value for exponent, value in result.items() if value}


def _scale(series: _Series, scalar: Fraction) -> _Series:
    return {
        exponent: scalar * value
        for exponent, value in series.items()
        if scalar * value
    }


def _multiply(
    left: _Series,
    right: _Series,
    minimum: int,
    maximum: int,
) -> _Series:
    result: _Series = {}
    for left_exponent, left_value in left.items():
        for right_exponent, right_value in right.items():
            exponent = left_exponent + right_exponent
            if minimum <= exponent <= maximum:
                result[exponent] = result.get(exponent, Fraction(0)) + (
                    left_value * right_value
                )
    return {exponent: value for exponent, value in result.items() if value}


def _derivative(series: _Series) -> _Series:
    return {
        exponent - 1: exponent * value
        for exponent, value in series.items()
        if exponent and exponent * value
    }


def _substitute_linear_scale(series: _Series, scalar: Fraction) -> _Series:
    return {
        exponent: value * scalar**exponent
        for exponent, value in series.items()
    }


def _inverse_series(series: _Series, maximum: int) -> _Series:
    """Invert a one-variable formal Laurent series through ``maximum``."""

    lead = min(exponent for exponent, value in series.items() if value)
    leading_value = series[lead]
    normalized_degree = maximum + lead
    coefficients = [
        series.get(lead + degree, Fraction(0))
        for degree in range(normalized_degree + 1)
    ]
    inverse_coefficients = [Fraction(1, 1) / leading_value]
    for degree in range(1, normalized_degree + 1):
        inverse_coefficients.append(
            -sum(
                coefficients[index] * inverse_coefficients[degree - index]
                for index in range(1, degree + 1)
            )
            / leading_value
        )
    return {
        degree - lead: value
        for degree, value in enumerate(inverse_coefficients)
        if value
    }


def _exponential(sign: int, maximum: int) -> _Series:
    return {
        degree: Fraction(sign**degree, factorial(degree))
        for degree in range(maximum + 1)
    }


def _constant_term(series: _Series) -> Fraction:
    return series.get(0, Fraction(0))


def _series_equal(
    left: _Series,
    right: _Series,
    minimum: int,
    maximum: int,
) -> bool:
    return all(
        left.get(k, Fraction(0)) == right.get(k, Fraction(0))
        for k in range(minimum, maximum + 1)
    )


def _regularized_germs(maximum: int = 12) -> tuple[_Series, _Series, _Series, _Series]:
    exp_positive = _exponential(1, maximum + 4)
    exp_negative = _exponential(-1, maximum + 4)
    one_minus_exp_negative = _add({0: Fraction(1)}, _scale(exp_negative, Fraction(-1)))
    exp_positive_minus_one = _add(exp_positive, {0: Fraction(-1)})
    inverse_filter = _inverse_series(one_minus_exp_negative, maximum + 2)
    geometric_sum = _inverse_series(exp_positive_minus_one, maximum + 2)
    denominator_square = _multiply(inverse_filter, inverse_filter, -2, maximum + 2)
    power_sum = _multiply(exp_negative, denominator_square, -2, maximum)
    return exp_positive, exp_negative, geometric_sum, power_sum


def test_projective_frame_forgetting_blocks_strict_addition_descent():
    infinity = None
    g_zero: _Mobius = tuple(map(Fraction, (0, 1, 1, 0)))
    g_one: _Mobius = tuple(map(Fraction, (0, 1, 1, -1)))

    assert (_mobius(g_zero, Fraction(0)), _mobius(g_zero, Fraction(1))) == (
        infinity,
        Fraction(1),
    )
    assert _mobius(g_zero, Fraction(0) + Fraction(1)) == Fraction(1)

    assert (_mobius(g_one, Fraction(1)), _mobius(g_one, Fraction(2))) == (
        infinity,
        Fraction(1),
    )
    assert _mobius(g_one, Fraction(1) + Fraction(2)) == Fraction(1, 2)

    # The unmarked input is the same, but the two frame lifts demand
    # incompatible outputs.  Hence addition is not constant on forgetting
    # fibres and cannot descend to an unmarked PGL_2-equivariant operation.
    assert Fraction(1) != Fraction(1, 2)


def test_frame_indexed_addition_is_exactly_covariant():
    matrices = tuple(
        tuple(map(Fraction, entries))
        for entries in product(range(-2, 3), repeat=4)
        if entries[0] * entries[3] - entries[1] * entries[2] != 0
    )
    inputs = tuple(map(Fraction, range(-2, 3)))
    assert len(matrices) == 496

    for matrix, left, right in product(matrices, inputs, inputs):
        transported_left = _mobius(matrix, left)
        transported_right = _mobius(matrix, right)
        assert _transported_addition(
            matrix, transported_left, transported_right
        ) == _mobius(matrix, left + right)

    # Scaling changes the mark called one but not the additive law.  Addition
    # needs the ordered zero/infinity affine frame; joint addition and
    # multiplication need the third unit mark.
    for scale, left, right in product((Fraction(2), Fraction(3)), inputs, inputs):
        dilation: _Mobius = (scale, Fraction(0), Fraction(0), Fraction(1))
        assert _transported_addition(dilation, left, right) == left + right
        assert _mobius(dilation, Fraction(1)) == scale


def test_finite_part_changes_under_chart_for_the_same_singular_germ():
    in_u = {-2: Fraction(1), -1: Fraction(-1)}
    _, _, _, in_t = _regularized_germs()
    assert _constant_term(in_u) == 0
    observed = {
        exponent: in_t.get(exponent, Fraction(0))
        for exponent in (-2, -1, 0, 1, 2)
    }
    assert observed == {
        -2: Fraction(1),
        -1: Fraction(0),
        0: Fraction(-1, 12),
        1: Fraction(0),
        2: Fraction(1, 240),
    }

    # u=1-exp(-t)=t-t^2/2+t^3/6+O(t^4).  The exact second-order transport
    # formula shows which retained principal part and chart jet create the
    # finite correction.
    assert _second_order_finite_part(
        Fraction(1),
        Fraction(-1),
        Fraction(0),
        Fraction(1),
        Fraction(-1, 2),
        Fraction(1, 6),
    ) == Fraction(-1, 12)


def test_bernoulli_values_are_exponential_chart_transition_coefficients():
    _, _, geometric_sum, _ = _regularized_germs()
    bernoulli = _bernoulli_numbers(11)
    assert bernoulli[:3] == (Fraction(1), Fraction(-1, 2), Fraction(1, 6))

    observed = {}
    exponential_germ = geometric_sum
    for power in range(1, 9):
        exponential_germ = _scale(_derivative(exponential_germ), Fraction(-1))
        finite_part = _constant_term(exponential_germ)
        expected = Fraction((-1) ** power) * bernoulli[power + 1] / Fraction(
            power + 1
        )
        assert finite_part == expected
        observed[power] = expected

    assert observed[1] == Fraction(-1, 12)
    assert observed[2] == 0
    assert observed[3] == Fraction(1, 120)


def test_fixed_chart_finite_part_has_composition_boundaries():
    exp_positive, exp_negative, geometric_sum, power_sum = _regularized_germs()

    # Linear for a fixed chart and subtraction convention.
    assert _constant_term(_add(power_sum, geometric_sum)) == (
        _constant_term(power_sum) + _constant_term(geometric_sum)
    ) == Fraction(-7, 12)

    # Linear rescaling does not mix Laurent degrees in this log-free model.
    assert _constant_term(
        _substitute_linear_scale(power_sum, Fraction(2))
    ) == Fraction(-1, 12)

    # It is neither multiplicative nor compatible with differentiation as a
    # scalar operation.
    inverse_t = {-1: Fraction(1)}
    t = {1: Fraction(1)}
    assert _constant_term(inverse_t) * _constant_term(t) == 0
    assert _constant_term(_multiply(inverse_t, t, 0, 0)) == 1
    assert _constant_term(_derivative(t)) == 1
    assert _derivative({0: _constant_term(t)}) == {}

    # Reindexing is sound only with the boundary term retained.
    shifted_direct = _add(power_sum, geometric_sum)
    shifted_reindexed = _multiply(
        exp_positive,
        _add(power_sum, _scale(exp_negative, Fraction(-1))),
        -2,
        4,
    )
    assert _series_equal(shifted_direct, shifted_reindexed, -2, 4)
    assert _constant_term(shifted_direct) == Fraction(-7, 12)
    assert _constant_term(_multiply(exp_positive, power_sum, -2, 4)) == Fraction(5, 12)

    # Filtering terms before grouping and filtering zero-valued pairs after
    # grouping are different schemes, even for the same Grandi history.
    one_plus_exp_negative = _add({0: Fraction(1)}, exp_negative)
    termwise_abel = _inverse_series(one_plus_exp_negative, 4)
    filter_after_pairing: _Series = {}
    assert _constant_term(termwise_abel) == Fraction(1, 2)
    assert _constant_term(filter_after_pairing) == 0


def test_phase12a_does_not_claim_strict_or_vertical_objectification():
    classification = {
        "ordinary_sum_of_positive_integers": "diverges_to_positive_infinity",
        "zeta_or_heat_kernel_value": Fraction(-1, 12),
        "full_germ_transport": "exact_after_chart_is_retained",
        "finite_part_after_chart_forgetting": "not_well_defined",
        "new_free_composition": False,
        "all_composites_lower": False,
        "public_api_pressure": False,
    }
    assert classification["ordinary_sum_of_positive_integers"] != (
        classification["zeta_or_heat_kernel_value"]
    )
    assert classification["finite_part_after_chart_forgetting"] == (
        "not_well_defined"
    )
    assert not classification["new_free_composition"]
    assert not classification["all_composites_lower"]
    assert not classification["public_api_pressure"]
