"""Exact real continued-fraction and Farey-path positive control.

This executable essay compiles one finite regular continued fraction through
four representations:

1. a literal innermost-to-outermost right-reciprocal ProcessWord;
2. the standard product of two-by-two projective matrices;
3. convergents and their exact Farey-neighbour determinants;
4. the run-length-expanded left/right path in the Stern--Brocot tree.

The Stern--Brocot word is the finite combinatorial shadow of the cutting
sequence used for geodesics in the Farey tessellation.  No floating-point
geodesic flow or p-adic digit selector is implemented here.

Mathematical lineage: [Series-1985] and [Reutenauer-2019] in
docs/REFERENCES.md.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd

import pytest

from process_geometry.process.history import ProcessWord, interpret_history


_Matrix = tuple[tuple[int, int], tuple[int, int]]
_IDENTITY: _Matrix = ((1, 0), (0, 1))


def _validate_digits(
    digits: tuple[int, ...],
    *,
    require_canonical_terminal: bool = False,
) -> None:
    if not digits:
        raise ValueError("continued fraction needs at least one digit")
    if digits[0] < 0:
        raise ValueError("the first regular digit must be nonnegative")
    if any(digit < 1 for digit in digits[1:]):
        raise ValueError("tail digits must be positive")
    if require_canonical_terminal and len(digits) > 1 and digits[-1] <= 1:
        raise ValueError("a canonical rational expansion must end above one")
    if require_canonical_terminal and len(digits) == 1 and digits[0] < 1:
        raise ValueError("this positive-rational control excludes zero")


def _continued_fraction_value(digits: tuple[int, ...]) -> Fraction:
    _validate_digits(digits)
    value = Fraction(digits[-1])
    for digit in reversed(digits[:-1]):
        if value == 0:
            raise ZeroDivisionError("right reciprocal reached zero")
        value = Fraction(digit) + 1 / value
    return value


def _canonical_rational_continued_fraction(value: Fraction) -> tuple[int, ...]:
    value = Fraction(value)
    if value <= 0:
        raise ValueError("Stern--Brocot control requires a positive rational")
    numerator, denominator = value.numerator, value.denominator
    digits = []
    while denominator:
        digit, remainder = divmod(numerator, denominator)
        digits.append(digit)
        numerator, denominator = denominator, remainder
    result = tuple(digits)
    _validate_digits(result, require_canonical_terminal=True)
    return result


def _matmul(left: _Matrix, right: _Matrix) -> _Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def _digit_matrix(digit: int) -> _Matrix:
    return ((digit, 1), (1, 0))


def _continued_fraction_matrix(digits: tuple[int, ...]) -> _Matrix:
    _validate_digits(digits)
    matrix = _IDENTITY
    for digit in digits:
        matrix = _matmul(matrix, _digit_matrix(digit))
    return matrix


def _matrix_affine(matrix: _Matrix, value: Fraction) -> Fraction:
    numerator = matrix[0][0] * value + matrix[0][1]
    denominator = matrix[1][0] * value + matrix[1][1]
    if denominator == 0:
        raise ZeroDivisionError("projective action reached infinity")
    return numerator / denominator


def _right_reciprocal_history_value(digits: tuple[int, ...]) -> Fraction:
    """Evaluate the literal right expansion from the innermost digit out."""

    _validate_digits(digits)
    history = ProcessWord(tuple(reversed(digits[:-1])))
    return interpret_history(
        history,
        Fraction(digits[-1]),
        lambda state, digit: Fraction(digit) + 1 / state,
    )


def _right_reciprocal_history_matrix(digits: tuple[int, ...]) -> _Matrix:
    """Lower the same chronological ProcessWord to projective matrices."""

    _validate_digits(digits)
    history = ProcessWord(tuple(reversed(digits[:-1])))
    return interpret_history(
        history,
        _IDENTITY,
        lambda prefix, digit: _matmul(_digit_matrix(digit), prefix),
    )


def _convergents(digits: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    _validate_digits(digits)
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    result = []
    for digit in digits:
        p_current = digit * p_previous + p_previous_previous
        q_current = digit * q_previous + q_previous_previous
        result.append((p_current, q_current))
        p_previous_previous, p_previous = p_previous, p_current
        q_previous_previous, q_previous = q_previous, q_current
    return tuple(result)


def _stern_brocot_word(digits: tuple[int, ...]) -> str:
    """Expand continued-fraction digits into unit left/right tree moves."""

    _validate_digits(digits)
    if _continued_fraction_value(digits) <= 0:
        raise ValueError("Stern--Brocot control requires a positive value")
    moves = []
    for index, digit in enumerate(digits):
        run_length = digit - (index == len(digits) - 1)
        if run_length < 0:
            raise ValueError("terminal run length became negative")
        direction = "R" if index % 2 == 0 else "L"
        moves.append(direction * run_length)
    return "".join(moves)


def _stern_brocot_bracket(word: str) -> tuple[tuple[int, int], tuple[int, int]]:
    left = (0, 1)
    right = (1, 0)
    for direction in word:
        mediant = (left[0] + right[0], left[1] + right[1])
        if direction == "L":
            right = mediant
        elif direction == "R":
            left = mediant
        else:
            raise ValueError("Stern--Brocot word uses only L and R")
    return left, right


def _stern_brocot_endpoint(word: str) -> Fraction:
    left, right = _stern_brocot_bracket(word)
    return Fraction(left[0] + right[0], left[1] + right[1])


def _stern_brocot_trace(word: str) -> tuple[Fraction, ...]:
    return tuple(
        _stern_brocot_endpoint(word[:depth])
        for depth in range(len(word) + 1)
    )


def _cylinder_interval(digits: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Return the open real cylinder determined by one finite prefix."""

    convergents = _convergents(digits)
    current_numerator, current_denominator = convergents[-1]
    if len(convergents) == 1:
        previous_numerator, previous_denominator = 1, 0
    else:
        previous_numerator, previous_denominator = convergents[-2]
    current = Fraction(current_numerator, current_denominator)
    adjacent = Fraction(
        current_numerator + previous_numerator,
        current_denominator + previous_denominator,
    )
    return min(current, adjacent), max(current, adjacent)


def test_right_history_matrix_convergents_and_farey_frames_commute():
    examples = (
        (0, 2),
        (1,),
        (1, 2),
        (1, 1, 1, 2),
        (3, 4, 2),
        (0, 1, 2, 3),
    )
    for digits in examples:
        convergents = _convergents(digits)
        final_numerator, final_denominator = convergents[-1]
        full_matrix = _continued_fraction_matrix(digits)
        literal = _right_reciprocal_history_value(digits)
        lowered = _right_reciprocal_history_matrix(digits)

        assert literal == _continued_fraction_value(digits)
        assert literal == Fraction(final_numerator, final_denominator)
        assert literal == _matrix_affine(lowered, Fraction(digits[-1]))

        if len(convergents) == 1:
            previous = (1, 0)
        else:
            previous = convergents[-2]
        assert full_matrix == (
            (final_numerator, previous[0]),
            (final_denominator, previous[1]),
        )

        for earlier, later in zip(convergents, convergents[1:]):
            determinant = later[0] * earlier[1] - earlier[0] * later[1]
            assert abs(determinant) == 1


def test_run_lengths_give_the_unique_nonbacktracking_stern_brocot_path():
    for length in range(9):
        for letters in product("LR", repeat=length):
            word = "".join(letters)
            endpoint = _stern_brocot_endpoint(word)
            digits = _canonical_rational_continued_fraction(endpoint)
            trace = _stern_brocot_trace(word)

            assert _stern_brocot_word(digits) == word
            assert _continued_fraction_value(digits) == endpoint
            assert len(trace) == length + 1
            assert len(set(trace)) == len(trace)
            assert len(word) == sum(digits) - 1


def test_prefix_cylinders_are_exact_farey_intervals():
    prefixes = (
        (0, 2),
        (1,),
        (1, 1),
        (1, 2),
        (2, 3, 1),
    )
    for digits in prefixes:
        lower, upper = _cylinder_interval(digits)
        convergents = _convergents(digits)
        current_numerator, current_denominator = convergents[-1]
        if len(convergents) == 1:
            previous_numerator, previous_denominator = 1, 0
        else:
            previous_numerator, previous_denominator = convergents[-2]

        adjacent_numerator = current_numerator + previous_numerator
        adjacent_denominator = current_denominator + previous_denominator
        determinant = (
            current_numerator * adjacent_denominator
            - adjacent_numerator * current_denominator
        )
        assert abs(determinant) == 1
        assert upper - lower == Fraction(
            1,
            current_denominator * adjacent_denominator,
        )

        samples = set()
        for denominator in range(1, 31):
            first_numerator = int(lower * denominator)
            last_numerator = int(upper * denominator) + 1
            for numerator in range(max(1, first_numerator), last_numerator + 1):
                if gcd(numerator, denominator) != 1:
                    continue
                candidate = Fraction(numerator, denominator)
                if lower < candidate < upper:
                    samples.add(candidate)
                    candidate_digits = _canonical_rational_continued_fraction(
                        candidate
                    )
                    assert candidate_digits[: len(digits)] == digits
        assert samples


def test_terminal_split_is_endpoint_equal_but_not_continuation_stable():
    canonical = (1, 2)
    split_terminal = (1, 1, 1)
    endpoint = Fraction(3, 2)

    assert _continued_fraction_value(canonical) == endpoint
    assert _continued_fraction_value(split_terminal) == endpoint
    assert _stern_brocot_word(canonical) == _stern_brocot_word(split_terminal)
    assert _continued_fraction_matrix(canonical) != (
        _continued_fraction_matrix(split_terminal)
    )

    canonical_cylinder = _cylinder_interval(canonical)
    split_cylinder = _cylinder_interval(split_terminal)
    assert canonical_cylinder[1] == split_cylinder[0] == endpoint
    assert canonical_cylinder[0] < endpoint < split_cylinder[1]

    same_suffix = (2,)
    assert _continued_fraction_value(canonical + same_suffix) != (
        _continued_fraction_value(split_terminal + same_suffix)
    )


def test_digit_steps_are_run_length_compression_not_free_unit_moves():
    examples = (
        (0, 7),
        (1, 1, 1, 2),
        (2, 5, 3),
        (7,),
    )
    for digits in examples:
        word = _stern_brocot_word(digits)
        assert len(word) == sum(digits) - 1
        assert len(digits) <= len(word) + 1

    assert len(_stern_brocot_word((0, 7))) == 6
    assert len(_stern_brocot_word((0, 2))) == 1


def test_real_positive_control_rejects_undefined_inputs():
    with pytest.raises(ValueError, match="at least one"):
        _continued_fraction_value(())
    with pytest.raises(ValueError, match="nonnegative"):
        _continued_fraction_value((-1, 2))
    with pytest.raises(ValueError, match="positive"):
        _continued_fraction_value((1, 0))
    with pytest.raises(ValueError, match="positive rational"):
        _canonical_rational_continued_fraction(Fraction(0))
    with pytest.raises(ValueError, match="only L and R"):
        _stern_brocot_endpoint("LX")
