"""Exact matched-task comparison of Ruban and Browkin I selectors.

Phase 0 showed that standard and balanced residue sections reconstruct the
same finite p-adic observation.  Phase 1 embedded those observations in the
two-chart finite Bruhat--Tits lattice ball.  Phase 2 supplied the separate
real continued-fraction/Farey-path positive control.

This executable essay now lets two classical p-adic floor sections drive the
same reciprocal process

    a_n = s(alpha_n),    alpha_{n+1} = 1 / (alpha_n - a_n).

Ruban uses residues 0, ..., p - 1.  Browkin I uses balanced residues
-(p - 1)/2, ..., (p - 1)/2.  Every calculation below is exact over Fraction.
The finite oracle records termination, an exact repeated rational state, or
horizon exhaustion as three different outcomes; it never turns a finite
horizon into a nontermination theorem.

Phase 4 adds the exact finite-tree ledger around the standard lattice root:
lowest common ancestors, pairwise distance, traveled versus net displacement,
and cancelled backtracking.  It also compares every Ruban prefix with every
Browkin prefix for the same bounded input.  Zero observed backtracking is kept
separate from any Bellman, Huffman, or infinite-boundary claim.

Mathematical lineage: [Ruban-1970], [Browkin-1978], and
[Capuano-Murru-Terracini-2022] in docs/REFERENCES.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt
from typing import Literal

import pytest

from process_geometry.process.history import ProcessWord, interpret_history


_Selector = Literal["ruban", "browkin"]
_Status = Literal["terminated", "cycle", "horizon"]
_Matrix = tuple[
    tuple[Fraction, Fraction],
    tuple[Fraction, Fraction],
]
_IDENTITY: _Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def _validate_prime(prime: int) -> None:
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if prime == 2:
        raise ValueError("the balanced Browkin control requires an odd prime")


def _valuation(value: Fraction, prime: int) -> int:
    """Return v_p(value), rejecting the undefined valuation of zero."""

    _validate_prime(prime)
    value = Fraction(value)
    if value == 0:
        raise ValueError("the valuation of zero is not finite")
    numerator = abs(value.numerator)
    denominator = value.denominator
    valuation = 0
    while numerator % prime == 0:
        numerator //= prime
        valuation += 1
    while denominator % prime == 0:
        denominator //= prime
        valuation -= 1
    return valuation


def _prime_power(prime: int, exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(prime**exponent)
    return Fraction(1, prime ** (-exponent))


def _rational_mod(value: Fraction, modulus: int) -> int:
    """Reduce a rational whose denominator is a unit modulo ``modulus``."""

    value = Fraction(value)
    if gcd(value.denominator, modulus) != 1:
        raise ValueError("the denominator is not a unit modulo the modulus")
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def _padic_floor(
    value: Fraction,
    prime: int,
    selector: _Selector,
) -> Fraction:
    """Truncate the selected Laurent expansion through exponent zero."""

    _validate_prime(prime)
    if selector not in ("ruban", "browkin"):
        raise ValueError("unknown p-adic floor selector")
    value = Fraction(value)
    if value == 0:
        return Fraction(0)

    first_exponent = _valuation(value, prime)
    if first_exponent > 0:
        return Fraction(0)

    remainder = value
    digit = Fraction(0)
    for exponent in range(first_exponent, 1):
        place = _prime_power(prime, exponent)
        scaled_remainder = remainder / place
        coefficient = _rational_mod(scaled_remainder, prime)
        if selector == "browkin" and coefficient > prime // 2:
            coefficient -= prime
        digit += coefficient * place
        remainder -= coefficient * place
    return digit


@dataclass(frozen=True, order=True)
class _LatticeVertex:
    """One Phase-1 standard-root lattice class or the root itself."""

    prime: int
    depth: int
    chart: Literal["root", "affine", "infinity"]
    coordinate: int

    def __post_init__(self) -> None:
        _validate_prime(self.prime)
        if self.depth < 0:
            raise ValueError("lattice depth must be nonnegative")
        if self.depth == 0:
            if (self.chart, self.coordinate) != ("root", 0):
                raise ValueError("depth zero has only the standard root")
            return
        if self.chart == "affine":
            bound = self.prime**self.depth
        elif self.chart == "infinity":
            bound = self.prime ** (self.depth - 1)
        else:
            raise ValueError("contact needs a projective chart")
        if not 0 <= self.coordinate < bound:
            raise ValueError("contact coordinate is outside its residue range")

    @property
    def parent(self) -> "_LatticeVertex":
        if self.depth == 0:
            raise ValueError("the standard root has no parent")
        if self.depth == 1:
            return _LatticeVertex(self.prime, 0, "root", 0)
        if self.chart == "affine":
            modulus = self.prime ** (self.depth - 1)
        else:
            modulus = self.prime ** (self.depth - 2)
        return _LatticeVertex(
            self.prime,
            self.depth - 1,
            self.chart,
            self.coordinate % modulus,
        )

    def is_ancestor_of(self, descendant: "_LatticeVertex") -> bool:
        if self.prime != descendant.prime or self.depth > descendant.depth:
            return False
        cursor = descendant
        while cursor.depth > self.depth:
            cursor = cursor.parent
        return cursor == self


def _projective_contact(value: Fraction, prime: int) -> _LatticeVertex:
    """Expose exactly the finite projective contact fixed by one floor digit.

    Integral values use the affine first sphere.  If v_p(value) = -r < 0,
    the homogeneous point [value:1] is normalized to [1:1/value], hence its
    first floor-visible label is the infinity-chart class

        [1 : p*t],    t = 1/(p*value) mod p**r

    at depth r + 1.
    """

    _validate_prime(prime)
    value = Fraction(value)
    if value == 0 or _valuation(value, prime) >= 0:
        return _LatticeVertex(
            prime,
            1,
            "affine",
            _rational_mod(value, prime),
        )

    negative_depth = -_valuation(value, prime)
    modulus = prime**negative_depth
    return _LatticeVertex(
        prime,
        negative_depth + 1,
        "infinity",
        _rational_mod(1 / (prime * value), modulus),
    )


def _phase1_sphere(prime: int, depth: int) -> set[_LatticeVertex]:
    """Reproduce the two finite normal-form charts from the Phase-1 oracle."""

    if depth <= 0:
        raise ValueError("sphere depth must be positive")
    return {
        *(
            _LatticeVertex(prime, depth, "affine", coordinate)
            for coordinate in range(prime**depth)
        ),
        *(
            _LatticeVertex(prime, depth, "infinity", coordinate)
            for coordinate in range(prime ** (depth - 1))
        ),
    }


@dataclass(frozen=True)
class _Expansion:
    selector: _Selector
    prime: int
    initial: Fraction
    digits: tuple[Fraction, ...]
    states: tuple[Fraction, ...]
    status: _Status
    cycle_start: int | None = None

    @property
    def cycle_length(self) -> int | None:
        if self.cycle_start is None:
            return None
        return len(self.states) - self.cycle_start


def _expand(
    value: Fraction,
    prime: int,
    selector: _Selector,
    *,
    max_steps: int,
) -> _Expansion:
    """Run a finite exact rational oracle with explicit outcome semantics."""

    _validate_prime(prime)
    if selector not in ("ruban", "browkin"):
        raise ValueError("unknown p-adic floor selector")
    if max_steps <= 0:
        raise ValueError("max_steps must be positive")

    initial = Fraction(value)
    state = initial
    digits: list[Fraction] = []
    states: list[Fraction] = []
    first_visit: dict[Fraction, int] = {}

    for _ in range(max_steps):
        if state in first_visit:
            return _Expansion(
                selector,
                prime,
                initial,
                tuple(digits),
                tuple(states),
                "cycle",
                first_visit[state],
            )
        first_visit[state] = len(states)
        states.append(state)

        digit = _padic_floor(state, prime, selector)
        digits.append(digit)
        remainder = state - digit
        if remainder == 0:
            return _Expansion(
                selector,
                prime,
                initial,
                tuple(digits),
                tuple(states),
                "terminated",
            )
        state = 1 / remainder

    return _Expansion(
        selector,
        prime,
        initial,
        tuple(digits),
        tuple(states),
        "horizon",
    )


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


def _digit_matrix(digit: Fraction) -> _Matrix:
    return (
        (Fraction(digit), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )


def _history_matrix(digits: tuple[Fraction, ...]) -> _Matrix:
    history = ProcessWord(digits)
    return interpret_history(
        history,
        _IDENTITY,
        lambda matrix, digit: _matmul(matrix, _digit_matrix(digit)),
    )


def _matrix_affine(matrix: _Matrix, value: Fraction) -> Fraction:
    numerator = matrix[0][0] * value + matrix[0][1]
    denominator = matrix[1][0] * value + matrix[1][1]
    if denominator == 0:
        raise ZeroDivisionError("projective action reached infinity")
    return numerator / denominator


def _matrix_lattice_vertex(matrix: _Matrix, prime: int) -> _LatticeVertex:
    """Map a prefix matrix to its exact standard-root lattice class.

    The columns span a Z_p-lattice.  Scalar multiplication does not change
    its homothety class, so first make the minimum entry valuation zero.  A
    primitive two-by-two matrix with determinant valuation ``depth`` spans an
    index-p**depth lattice; a primitive row of its adjugate is the Phase-1
    kernel covector modulo p**depth.
    """

    _validate_prime(prime)
    nonzero_entries = [entry for row in matrix for entry in row if entry != 0]
    if not nonzero_entries:
        raise ValueError("the zero matrix has no lattice class")
    minimum = min(_valuation(entry, prime) for entry in nonzero_entries)
    scale = _prime_power(prime, -minimum)
    normalized = tuple(
        tuple(entry * scale for entry in row)
        for row in matrix
    )
    determinant = (
        normalized[0][0] * normalized[1][1]
        - normalized[0][1] * normalized[1][0]
    )
    if determinant == 0:
        raise ValueError("a singular matrix has no Bruhat--Tits vertex")
    depth = _valuation(determinant, prime)
    if depth < 0:
        raise AssertionError("entry normalization must make integral determinant")
    if depth == 0:
        return _LatticeVertex(prime, 0, "root", 0)

    adjugate_rows = (
        (normalized[1][1], -normalized[0][1]),
        (-normalized[1][0], normalized[0][0]),
    )
    primitive = next(
        row
        for row in adjugate_rows
        if any(
            entry != 0 and _valuation(entry, prime) == 0
            for entry in row
        )
    )
    first, second = primitive
    modulus = prime**depth
    if second != 0 and _valuation(second, prime) == 0:
        coordinate = _rational_mod(first / second, modulus)
        return _LatticeVertex(prime, depth, "affine", coordinate)

    assert first != 0 and _valuation(first, prime) == 0
    normalized_second = _rational_mod(second / first, modulus)
    assert normalized_second % prime == 0
    return _LatticeVertex(
        prime,
        depth,
        "infinity",
        normalized_second // prime,
    )


@dataclass(frozen=True)
class _ResourceCost:
    digit_steps: int
    contact_resolution: int
    rational_bits: int


def _resource_cost(expansion: _Expansion) -> _ResourceCost:
    bit_cost = sum(
        max(1, abs(digit.numerator).bit_length())
        + digit.denominator.bit_length()
        for digit in expansion.digits
    )
    return _ResourceCost(
        len(expansion.digits),
        sum(
            _projective_contact(state, expansion.prime).depth
            for state in expansion.states
        ),
        bit_cost,
    )


def _lowest_common_ancestor(
    left: _LatticeVertex,
    right: _LatticeVertex,
) -> _LatticeVertex:
    """Return the exact common ancestor nearest two finite-ball vertices."""

    if left.prime != right.prime:
        raise ValueError("tree vertices must use the same prime")

    left_cursor = left
    right_cursor = right
    while left_cursor.depth > right_cursor.depth:
        left_cursor = left_cursor.parent
    while right_cursor.depth > left_cursor.depth:
        right_cursor = right_cursor.parent
    while left_cursor != right_cursor:
        left_cursor = left_cursor.parent
        right_cursor = right_cursor.parent
    return left_cursor


def _tree_distance(left: _LatticeVertex, right: _LatticeVertex) -> int:
    ancestor = _lowest_common_ancestor(left, right)
    return left.depth + right.depth - 2 * ancestor.depth


@dataclass(frozen=True)
class _PrefixPathMetric:
    """Finite tree ledger for one materialized continued-fraction history.

    ``excess_travel`` charges both directions of every cancelled excursion.
    ``backtracked_edges`` counts one direction from every cancelled edge pair;
    for a rooted prefix path these are precisely the moves back toward root.
    """

    vertices: tuple[_LatticeVertex, ...]
    common_ancestors: tuple[_LatticeVertex, ...]
    step_distances: tuple[int, ...]
    traveled_distance: int
    net_displacement: int
    excess_travel: int
    backtracked_edges: int

    @property
    def is_nondecreasing_ray(self) -> bool:
        return all(
            earlier.is_ancestor_of(later)
            for earlier, later in zip(self.vertices, self.vertices[1:])
        )


def _tree_path_metric(
    vertices: tuple[_LatticeVertex, ...],
) -> _PrefixPathMetric:
    """Audit a nonempty sequence of vertices in one finite tree oracle."""

    if not vertices:
        raise ValueError("a tree path needs at least one vertex")
    common_ancestors = tuple(
        _lowest_common_ancestor(left, right)
        for left, right in zip(vertices, vertices[1:])
    )
    step_distances = tuple(
        _tree_distance(left, right)
        for left, right in zip(vertices, vertices[1:])
    )
    traveled_distance = sum(step_distances)
    net_displacement = _tree_distance(vertices[0], vertices[-1])
    excess_travel = traveled_distance - net_displacement
    if excess_travel < 0 or excess_travel % 2:
        raise AssertionError("a tree walk must have even nonnegative excess")

    return _PrefixPathMetric(
        vertices,
        common_ancestors,
        step_distances,
        traveled_distance,
        net_displacement,
        excess_travel,
        excess_travel // 2,
    )


def _prefix_path_metric(
    digits: tuple[Fraction, ...],
    prime: int,
) -> _PrefixPathMetric:
    """Materialize root and prefix lattices, then audit their exact tree path."""

    _validate_prime(prime)
    matrix = _IDENTITY
    vertices = [_matrix_lattice_vertex(matrix, prime)]
    for digit in digits:
        matrix = _matmul(matrix, _digit_matrix(digit))
        vertices.append(_matrix_lattice_vertex(matrix, prime))
    return _tree_path_metric(tuple(vertices))


def test_floor_sections_are_exact_locally_constant_projective_contacts():
    samples = (
        Fraction(-7, 5),
        Fraction(-1),
        Fraction(-1, 25),
        Fraction(0),
        Fraction(2, 7),
        Fraction(3),
        Fraction(17, 6),
    )
    for prime in (3, 5, 7):
        for value in samples:
            ruban = _padic_floor(value, prime, "ruban")
            browkin = _padic_floor(value, prime, "browkin")

            assert Fraction(0) <= ruban < prime
            assert Fraction(-prime, 2) < browkin < Fraction(prime, 2)
            assert _projective_contact(value, prime) == (
                _projective_contact(ruban, prime)
            )
            assert _projective_contact(value, prime) == (
                _projective_contact(browkin, prime)
            )

            difference = ruban - browkin
            assert difference == 0 or _valuation(difference, prime) >= 1
            for integral_shift in range(-3, 4):
                shifted = value + prime * integral_shift
                assert _padic_floor(shifted, prime, "ruban") == ruban
                assert _padic_floor(shifted, prime, "browkin") == browkin


def test_every_digit_is_certified_by_the_phase1_two_chart_sphere():
    for prime in (3, 5):
        for value in (
            Fraction(-1),
            Fraction(2, 7),
            Fraction(7, 5),
            Fraction(17, 6),
        ):
            for selector in ("ruban", "browkin"):
                expansion = _expand(
                    value,
                    prime,
                    selector,
                    max_steps=16,
                )
                for state, digit in zip(expansion.states, expansion.digits):
                    contact = _projective_contact(state, prime)
                    assert contact in _phase1_sphere(prime, contact.depth)
                    assert _projective_contact(digit, prime) == contact
                    remainder = state - digit
                    assert remainder == 0 or _valuation(remainder, prime) >= 1


def test_processword_matrices_reconstruct_every_finite_prefix():
    for prime in (3, 5, 7):
        for value in (
            Fraction(-1),
            Fraction(-2, 5),
            Fraction(2, 7),
            Fraction(17, 6),
        ):
            for selector in ("ruban", "browkin"):
                expansion = _expand(
                    value,
                    prime,
                    selector,
                    max_steps=16,
                )
                for index, (state, digit) in enumerate(
                    zip(expansion.states, expansion.digits)
                ):
                    prefix = expansion.digits[: index + 1]
                    matrix = _history_matrix(prefix)
                    determinant = (
                        matrix[0][0] * matrix[1][1]
                        - matrix[0][1] * matrix[1][0]
                    )
                    assert determinant == (-1) ** len(prefix)

                    remainder = state - digit
                    if remainder == 0:
                        assert matrix[1][0] != 0
                        assert matrix[0][0] / matrix[1][0] == value
                    else:
                        next_state = 1 / remainder
                        assert _matrix_affine(matrix, next_state) == value

                for digit in expansion.digits[1:]:
                    assert _valuation(digit, prime) < 0


def test_prefix_matrices_land_in_the_phase1_lattice_ball_oracle():
    for prime in (3, 5, 7):
        for value in (
            Fraction(-1),
            Fraction(-2, 5),
            Fraction(2, 7),
            Fraction(3),
        ):
            for selector in ("ruban", "browkin"):
                expansion = _expand(
                    value,
                    prime,
                    selector,
                    max_steps=16,
                )
                for prefix_length in range(1, len(expansion.digits) + 1):
                    matrix = _history_matrix(expansion.digits[:prefix_length])
                    vertex = _matrix_lattice_vertex(matrix, prime)
                    nonzero_entries = [
                        entry
                        for row in matrix
                        for entry in row
                        if entry != 0
                    ]
                    minimum = min(
                        _valuation(entry, prime)
                        for entry in nonzero_entries
                    )
                    assert vertex.depth == -2 * minimum
                    if vertex.depth == 0:
                        assert vertex == _LatticeVertex(prime, 0, "root", 0)
                    else:
                        assert vertex in _phase1_sphere(prime, vertex.depth)


def test_ruban_negative_one_cycle_exposes_a_growing_lattice_ray_prefix():
    for prime in (3, 5, 7):
        periodic_digit = Fraction(prime**2 - 1, prime)
        digits = (Fraction(prime - 1),) + (periodic_digit,) * 5
        metric = _prefix_path_metric(digits, prime)

        assert tuple(vertex.depth for vertex in metric.vertices) == (
            0,
            0,
            2,
            4,
            6,
            8,
            10,
        )
        assert all(
            vertex.chart == "affine" and vertex.coordinate == 1
            for vertex in metric.vertices[2:]
        )
        assert metric.step_distances == (0, 2, 2, 2, 2, 2)
        assert metric.is_nondecreasing_ray
        assert metric.traveled_distance == metric.net_displacement == 10
        assert metric.excess_travel == metric.backtracked_edges == 0


def test_bounded_rational_oracle_separates_browkin_finiteness_from_ruban_cycles():
    values = sorted(
        {
            Fraction(numerator, denominator)
            for denominator in range(1, 13)
            for numerator in range(-12, 13)
            if numerator != 0 and gcd(abs(numerator), denominator) == 1
        }
    )
    assert len(values) == 182

    expected_ruban = {
        3: {"terminated": 48, "cycle": 134},
        5: {"terminated": 36, "cycle": 146},
        7: {"terminated": 38, "cycle": 144},
    }
    for prime in (3, 5, 7):
        ruban_counts = {"terminated": 0, "cycle": 0, "horizon": 0}
        browkin_lengths = []
        for value in values:
            ruban = _expand(value, prime, "ruban", max_steps=16)
            browkin = _expand(value, prime, "browkin", max_steps=16)
            ruban_counts[ruban.status] += 1
            assert browkin.status == "terminated"
            browkin_lengths.append(len(browkin.digits))

        assert ruban_counts["horizon"] == 0
        assert {
            "terminated": ruban_counts["terminated"],
            "cycle": ruban_counts["cycle"],
        } == expected_ruban[prime]
        assert max(browkin_lengths) == 4


def test_negative_one_is_same_contact_but_cycle_versus_terminal():
    for prime in (3, 5, 7, 11):
        ruban = _expand(Fraction(-1), prime, "ruban", max_steps=8)
        browkin = _expand(Fraction(-1), prime, "browkin", max_steps=8)

        assert _projective_contact(ruban.initial, prime) == (
            _projective_contact(ruban.digits[0], prime)
        )
        assert _projective_contact(browkin.initial, prime) == (
            _projective_contact(browkin.digits[0], prime)
        )
        assert ruban.digits == (
            Fraction(prime - 1),
            Fraction(prime**2 - 1, prime),
        )
        assert ruban.states == (Fraction(-1), Fraction(-1, prime))
        assert ruban.status == "cycle"
        assert ruban.cycle_start == 1
        assert ruban.cycle_length == 1

        assert browkin.digits == (Fraction(-1),)
        assert browkin.states == (Fraction(-1),)
        assert browkin.status == "terminated"


def test_no_task_free_selector_survives_totality_and_cost_red_teams():
    prime = 5

    short_input = Fraction(3)
    ruban_short = _expand(short_input, prime, "ruban", max_steps=8)
    browkin_long = _expand(short_input, prime, "browkin", max_steps=8)
    assert ruban_short.digits == (Fraction(3),)
    assert browkin_long.digits == (Fraction(-2), Fraction(1, 5))
    assert ruban_short.status == browkin_long.status == "terminated"
    ruban_cost = _resource_cost(ruban_short)
    browkin_cost = _resource_cost(browkin_long)
    assert ruban_cost.digit_steps < browkin_cost.digit_steps
    assert ruban_cost.contact_resolution < browkin_cost.contact_resolution
    assert ruban_cost.rational_bits < browkin_cost.rational_bits
    ruban_terminal_vertex = _matrix_lattice_vertex(
        _history_matrix(ruban_short.digits),
        prime,
    )
    browkin_terminal_vertex = _matrix_lattice_vertex(
        _history_matrix(browkin_long.digits),
        prime,
    )
    assert ruban_terminal_vertex.depth == 0
    assert browkin_terminal_vertex.depth == 2
    assert ruban_terminal_vertex != browkin_terminal_vertex

    totality_input = Fraction(-1)
    ruban_cycle = _expand(totality_input, prime, "ruban", max_steps=8)
    browkin_terminal = _expand(totality_input, prime, "browkin", max_steps=8)
    assert ruban_cycle.status == "cycle"
    assert browkin_terminal.status == "terminated"


def test_tree_metric_uses_common_ancestors_and_detects_cancelled_travel():
    root = _LatticeVertex(3, 0, "root", 0)
    common = _LatticeVertex(3, 1, "affine", 1)
    left = _LatticeVertex(3, 2, "affine", 1)
    right = _LatticeVertex(3, 2, "affine", 4)
    other_chart = _LatticeVertex(3, 1, "infinity", 0)

    assert _lowest_common_ancestor(left, right) == common
    assert _tree_distance(left, right) == 2
    assert _lowest_common_ancestor(left, other_chart) == root
    assert _tree_distance(left, other_chart) == 3

    sibling_turn = _tree_path_metric((root, left, right))
    assert sibling_turn.common_ancestors == (root, common)
    assert sibling_turn.step_distances == (2, 2)
    assert sibling_turn.traveled_distance == 4
    assert sibling_turn.net_displacement == 2
    assert sibling_turn.excess_travel == 2
    assert sibling_turn.backtracked_edges == 1
    assert not sibling_turn.is_nondecreasing_ray

    with pytest.raises(ValueError, match="same prime"):
        _tree_distance(left, _LatticeVertex(5, 0, "root", 0))
    with pytest.raises(ValueError, match="at least one"):
        _tree_path_metric(())


def test_bounded_selector_prefixes_are_exact_nondecreasing_tree_rays():
    values = sorted(
        {
            Fraction(numerator, denominator)
            for denominator in range(1, 13)
            for numerator in range(-12, 13)
            if numerator != 0 and gcd(abs(numerator), denominator) == 1
        }
    )
    expected_aggregates = {
        (3, "ruban"): (996, 12, 180),
        (3, "browkin"): (716, 6, 180),
        (5, "ruban"): (912, 10, 178),
        (5, "browkin"): (532, 6, 178),
        (7, "ruban"): (892, 10, 176),
        (7, "browkin"): (496, 6, 176),
    }

    for prime in (3, 5, 7):
        for selector in ("ruban", "browkin"):
            metrics = []
            for value in values:
                expansion = _expand(value, prime, selector, max_steps=16)
                metric = _prefix_path_metric(expansion.digits, prime)
                expected_steps = tuple(
                    0
                    if digit == 0
                    else max(0, -2 * _valuation(digit, prime))
                    for digit in expansion.digits
                )

                assert metric.step_distances == expected_steps
                assert metric.common_ancestors == metric.vertices[:-1]
                assert metric.is_nondecreasing_ray
                assert metric.traveled_distance == metric.net_displacement
                assert metric.net_displacement == metric.vertices[-1].depth
                assert metric.excess_travel == metric.backtracked_edges == 0
                metrics.append(metric)

            aggregate = (
                sum(metric.traveled_distance for metric in metrics),
                max(metric.net_displacement for metric in metrics),
                sum(metric.net_displacement > 0 for metric in metrics),
            )
            assert aggregate == expected_aggregates[(prime, selector)]


def test_bounded_selector_pairs_stay_on_one_input_ray_at_different_depths():
    values = sorted(
        {
            Fraction(numerator, denominator)
            for denominator in range(1, 13)
            for numerator in range(-12, 13)
            if numerator != 0 and gcd(abs(numerator), denominator) == 1
        }
    )
    expected_relations = {
        3: {"equal": 55, "ruban_shallower": 14, "browkin_shallower": 113},
        5: {"equal": 40, "ruban_shallower": 5, "browkin_shallower": 137},
        7: {"equal": 44, "ruban_shallower": 5, "browkin_shallower": 133},
    }
    expected_distance_counts = {
        3: {0: 55, 2: 90, 4: 32, 6: 4, 8: 1},
        5: {0: 40, 2: 100, 4: 28, 6: 12, 8: 2},
        7: {0: 44, 2: 86, 4: 37, 6: 12, 8: 3},
    }

    for prime in (3, 5, 7):
        relations = {"equal": 0, "ruban_shallower": 0, "browkin_shallower": 0}
        distance_counts: dict[int, int] = {}
        for value in values:
            ruban = _expand(value, prime, "ruban", max_steps=16)
            browkin = _expand(value, prime, "browkin", max_steps=16)
            ruban_path = _prefix_path_metric(ruban.digits, prime)
            browkin_path = _prefix_path_metric(browkin.digits, prime)
            ruban_final = ruban_path.vertices[-1]
            browkin_final = browkin_path.vertices[-1]

            assert all(
                ruban_vertex.is_ancestor_of(browkin_vertex)
                or browkin_vertex.is_ancestor_of(ruban_vertex)
                for ruban_vertex in ruban_path.vertices
                for browkin_vertex in browkin_path.vertices
            )
            distance = _tree_distance(ruban_final, browkin_final)
            assert distance == abs(ruban_final.depth - browkin_final.depth)
            distance_counts[distance] = distance_counts.get(distance, 0) + 1

            if ruban_final == browkin_final:
                relations["equal"] += 1
            elif ruban_final.is_ancestor_of(browkin_final):
                relations["ruban_shallower"] += 1
            else:
                assert browkin_final.is_ancestor_of(ruban_final)
                relations["browkin_shallower"] += 1

        assert relations == expected_relations[prime]
        assert distance_counts == expected_distance_counts[prime]


def test_path_geometry_does_not_collapse_outcome_or_local_cost_red_teams():
    prime = 5

    ruban_short = _expand(Fraction(3), prime, "ruban", max_steps=8)
    browkin_long = _expand(Fraction(3), prime, "browkin", max_steps=8)
    ruban_short_path = _prefix_path_metric(ruban_short.digits, prime)
    browkin_long_path = _prefix_path_metric(browkin_long.digits, prime)
    assert tuple(vertex.depth for vertex in ruban_short_path.vertices) == (0, 0)
    assert tuple(vertex.depth for vertex in browkin_long_path.vertices) == (
        0,
        0,
        2,
    )
    assert ruban_short_path.traveled_distance == 0
    assert browkin_long_path.traveled_distance == 2
    assert ruban_short_path.is_nondecreasing_ray
    assert browkin_long_path.is_nondecreasing_ray

    ruban_cycle = _expand(Fraction(-1), prime, "ruban", max_steps=8)
    browkin_terminal = _expand(Fraction(-1), prime, "browkin", max_steps=8)
    ruban_cycle_path = _prefix_path_metric(ruban_cycle.digits, prime)
    browkin_terminal_path = _prefix_path_metric(browkin_terminal.digits, prime)
    assert ruban_cycle.status == "cycle"
    assert browkin_terminal.status == "terminated"
    assert ruban_cycle_path.is_nondecreasing_ray
    assert browkin_terminal_path.is_nondecreasing_ray
    assert ruban_cycle_path.traveled_distance == 2
    assert browkin_terminal_path.traveled_distance == 0


def test_selector_oracle_rejects_undefined_inputs_and_preserves_horizon():
    with pytest.raises(ValueError, match="odd prime"):
        _padic_floor(Fraction(1), 2, "browkin")
    with pytest.raises(ValueError, match="must be prime"):
        _padic_floor(Fraction(1), 9, "ruban")
    with pytest.raises(ValueError, match="unknown"):
        _padic_floor(Fraction(1), 3, "nearest")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="positive"):
        _expand(Fraction(1), 3, "ruban", max_steps=0)
    with pytest.raises(ValueError, match="valuation of zero"):
        _valuation(Fraction(0), 3)
    with pytest.raises(ValueError, match="not a unit"):
        _rational_mod(Fraction(1, 3), 9)
    with pytest.raises(ZeroDivisionError, match="infinity"):
        _matrix_affine(
            ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
            Fraction(1),
        )
    with pytest.raises(ValueError, match="zero matrix"):
        _matrix_lattice_vertex(
            ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))),
            3,
        )
    with pytest.raises(ValueError, match="singular"):
        _matrix_lattice_vertex(
            ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
            3,
        )

    horizon = _expand(Fraction(-1), 5, "ruban", max_steps=1)
    assert horizon.status == "horizon"
    assert horizon.cycle_start is None
    assert horizon.digits == (Fraction(4),)
