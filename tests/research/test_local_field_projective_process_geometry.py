"""Exact finite certificates for local-field projective process geometry.

The primitive history language is deliberately small: rational Addition,
Multiplication, and right-slot reciprocal maps.  The tests ask what changes
when the *observer* changes from the Archimedean absolute value to one
``p``-adic valuation.  They do not implement a p-adic continued-fraction
algorithm, construct the full Bruhat--Tits tree, or propose a framework API.

Mathematical lineage: [Series-1985], [Bruhat-Tits-1972],
[Serre-Trees-1980], and [Hirsh-Washington-2011] in ``docs/REFERENCES.md``.
All executable claims below are elementary exact identities over ``Fraction``;
the cited sources support the surrounding geometric interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import inf

from process_geometry.process.history import ProcessWord, interpret_history


def _p_valuation(value: int | Fraction, prime: int) -> int | float:
    """Return the normalized valuation with ``v_p(p) = 1`` exactly."""

    if prime < 2:
        raise ValueError("prime must be at least two")
    value = Fraction(value)
    if value == 0:
        return inf

    def exponent(integer: int) -> int:
        integer = abs(integer)
        count = 0
        while integer % prime == 0:
            count += 1
            integer //= prime
        return count

    return exponent(value.numerator) - exponent(value.denominator)


def _p_norm(value: int | Fraction, prime: int) -> Fraction:
    valuation = _p_valuation(value, prime)
    if valuation == inf:
        return Fraction(0)
    if valuation >= 0:
        return Fraction(1, prime**valuation)
    return Fraction(prime ** (-valuation))


@dataclass(frozen=True)
class _Mobius:
    """A research-local exact representative of one projective process."""

    a: Fraction
    b: Fraction
    c: Fraction
    d: Fraction

    @classmethod
    def of(cls, a: int, b: int, c: int, d: int) -> "_Mobius":
        return cls(*(Fraction(value) for value in (a, b, c, d)))

    @property
    def determinant(self) -> Fraction:
        return self.a * self.d - self.b * self.c

    def after(self, earlier: "_Mobius") -> "_Mobius":
        """Compose chronologically: apply ``earlier`` and then ``self``."""

        return _Mobius(
            self.a * earlier.a + self.b * earlier.c,
            self.a * earlier.b + self.b * earlier.d,
            self.c * earlier.a + self.d * earlier.c,
            self.c * earlier.b + self.d * earlier.d,
        )

    def affine(self, value: int | Fraction) -> Fraction:
        value = Fraction(value)
        denominator = self.c * value + self.d
        if denominator == 0:
            raise ZeroDivisionError("affine chart reaches the projective pole")
        return (self.a * value + self.b) / denominator

    def projective(self, point: tuple[int | Fraction, int | Fraction]):
        u, v = (Fraction(coordinate) for coordinate in point)
        return self.a * u + self.b * v, self.c * u + self.d * v


_IDENTITY = _Mobius.of(1, 0, 0, 1)


def _projectively_equal(left, right) -> bool:
    return left[0] * right[1] == left[1] * right[0]


def _right_reciprocal(partial_quotient: int, numerator: int = 1) -> _Mobius:
    # z |-> a + b/z has matrix [[a, b], [1, 0]].
    return _Mobius.of(partial_quotient, numerator, 1, 0)


def _history_matrix(history: ProcessWord[_Mobius]) -> _Mobius:
    return interpret_history(
        history,
        _IDENTITY,
        lambda prefix, step: step.after(prefix),
    )


def _digits(value: int, prime: int, precision: int, *, balanced: bool):
    """Choose a finite digit section and retain its induced carry history."""

    current = value
    result = []
    for _ in range(precision):
        digit = current % prime
        if balanced and digit > prime // 2:
            digit -= prime
        result.append(digit)
        current = (current - digit) // prime
    return tuple(result)


def _reconstruct_digits(digits, prime: int) -> int:
    return sum(digit * prime**place for place, digit in enumerate(digits))


def test_one_rational_multiplication_history_has_place_relative_convergence():
    """The process is fixed; only the scale observer changes."""

    prime = 3
    endpoints = []
    for depth in range(1, 7):
        history = ProcessWord((prime,) * depth)
        endpoints.append(
            interpret_history(history, Fraction(1), lambda state, step: state * step)
        )

    assert endpoints == [Fraction(prime**depth) for depth in range(1, 7)]
    assert all(left < right for left, right in zip(endpoints, endpoints[1:]))
    assert [_p_valuation(value, prime) for value in endpoints] == list(range(1, 7))
    assert [_p_norm(value, prime) for value in endpoints] == [
        Fraction(1, prime**depth) for depth in range(1, 7)
    ]


def test_mod_pn_distinguishability_forms_a_nested_p_ary_refinement():
    prime = 3
    maximum_precision = 5
    universe = range(prime**maximum_precision)

    for precision in range(1, maximum_precision + 1):
        quotient = {value % prime**precision for value in universe}
        assert len(quotient) == prime**precision

    # A level-(n+1) observation always refines the level-n observation.
    for x in universe:
        for y in range(0, prime**maximum_precision, 17):
            for precision in range(1, maximum_precision):
                if (x - y) % prime ** (precision + 1) == 0:
                    assert (x - y) % prime**precision == 0

    # Standard base-p digits are one section of the same quotient tower.
    value = 137
    full = _digits(value, prime, maximum_precision, balanced=False)
    for precision in range(1, maximum_precision + 1):
        prefix = full[:precision]
        assert _reconstruct_digits(prefix, prime) % prime**precision == (
            value % prime**precision
        )


def test_addition_is_isometric_and_multiplication_transports_the_p_ruler():
    prime = 5
    x = Fraction(7, 3)
    y = Fraction(2, 9)
    translation = Fraction(11, 4)

    assert _p_valuation((x + translation) - (y + translation), prime) == (
        _p_valuation(x - y, prime)
    )

    for scale in (Fraction(2), Fraction(5), Fraction(25, 3)):
        assert _p_valuation(scale * x - scale * y, prime) == (
            _p_valuation(scale, prime) + _p_valuation(x - y, prime)
        )


def test_left_affine_sector_and_right_inversion_share_projective_semantics():
    infinity = (Fraction(1), Fraction(0))
    zero = (Fraction(0), Fraction(1))
    translation = _Mobius.of(1, 7, 0, 1)
    dilation = _Mobius.of(3, 0, 0, 1)
    inversion = _Mobius.of(0, -1, 1, 0)

    assert _projectively_equal(translation.projective(infinity), infinity)
    assert _projectively_equal(dilation.projective(infinity), infinity)
    assert _projectively_equal(inversion.projective(infinity), zero)
    assert _projectively_equal(inversion.projective(zero), infinity)


def test_right_reciprocal_history_lowers_exactly_to_convergent_matrices():
    history = ProcessWord(tuple(_right_reciprocal(1) for _ in range(4)))
    initial = Fraction(1)

    literal_endpoint = interpret_history(
        history,
        initial,
        lambda state, step: step.affine(state),
    )
    lowered_endpoint = _history_matrix(history).affine(initial)

    assert literal_endpoint == lowered_endpoint == Fraction(8, 5)

    expected_prefixes = (Fraction(2), Fraction(3, 2), Fraction(5, 3), Fraction(8, 5))
    for depth, expected in enumerate(expected_prefixes, start=1):
        prefix = ProcessWord(history.steps[:depth])
        assert _history_matrix(prefix).affine(initial) == expected


def test_mobius_action_transports_p_adic_resolution_by_exact_denominator_law():
    transformation = _Mobius.of(2, 1, 5, 3)
    x = Fraction(1, 7)
    y = Fraction(4, 9)

    assert transformation.determinant == 1
    assert transformation.c * x + transformation.d != 0
    assert transformation.c * y + transformation.d != 0

    for prime in (2, 3, 5, 7):
        observed = _p_valuation(
            transformation.affine(x) - transformation.affine(y), prime
        )
        transported = (
            _p_valuation(transformation.determinant, prime)
            + _p_valuation(x - y, prime)
            - _p_valuation(transformation.c * x + transformation.d, prime)
            - _p_valuation(transformation.c * y + transformation.d, prime)
        )
        assert observed == transported


def test_digit_sections_expose_a_canonicalization_defect():
    """Two exact sections win under different declared cost rulers."""

    prime = 5
    precision = 3
    value = 4
    standard = _digits(value, prime, precision, balanced=False)
    balanced = _digits(value, prime, precision, balanced=True)

    assert standard == (4, 0, 0)
    assert balanced == (-1, 1, 0)
    modulus = prime**precision
    assert _reconstruct_digits(standard, prime) % modulus == value
    assert _reconstruct_digits(balanced, prime) % modulus == value

    nonzero_cost = lambda expansion: sum(digit != 0 for digit in expansion)
    amplitude_cost = lambda expansion: sum(abs(digit) for digit in expansion)

    assert nonzero_cost(standard) < nonzero_cost(balanced)
    assert amplitude_cost(balanced) < amplitude_cost(standard)
