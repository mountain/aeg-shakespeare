"""Phase 9: A/M--Bruhat carrier with real and p-adic place shadows.

This executable essay tests a deliberately limited mother-carrier claim.  A
literal rational projective history retains its chronological word, oriented
matrix frame, marked origin, and a declared vector cost.  The same rational
matrix then has a real upper/lower-half-plane shadow and finite p-adic lattice
shadows.  Precision, horizon, scalar policy, and terminal decoding remain
downstream task projections.

The positive result is not an identification of the hyperbolic plane with a
Bruhat--Tits tree, an adelic completion, or a new process rank.  The negative
controls show that a bare endpoint, matrix, or local lattice vertex forgets
history data used by continuation and decoding.

All arithmetic is exact.  Phase 2, Phase 3, Phase 6, and Phase 7 research
owners are imported by path; no package API is introduced.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from fractions import Fraction
import importlib.util
from itertools import product
from pathlib import Path
import sys
from typing import Literal

import sympy as sp


def _load_research_module(name: str, filename: str) -> object:
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_PHASE2 = _load_research_module(
    "_phase2_real_continued_fraction_geodesic_control",
    "test_real_continued_fraction_geodesic_control.py",
)
_PHASE3 = _load_research_module(
    "_phase3_padic_continued_fraction_selector_comparison",
    "test_padic_continued_fraction_selector_comparison.py",
)
_PHASE7 = _load_research_module(
    "_phase7_for_am_bruhat_place_carrier",
    "test_padic_selector_structural_law.py",
)
_PHASE6 = _PHASE7._PHASE6


_Matrix = tuple[
    tuple[Fraction, Fraction],
    tuple[Fraction, Fraction],
]
_IDENTITY: _Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
_WEYL: _Matrix = (
    (Fraction(0), Fraction(-1)),
    (Fraction(1), Fraction(0)),
)
_RECIPROCAL: _Matrix = (
    (Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0)),
)


def _matrix(
    a: int | Fraction,
    b: int | Fraction,
    c: int | Fraction,
    d: int | Fraction,
) -> _Matrix:
    return (
        (Fraction(a), Fraction(b)),
        (Fraction(c), Fraction(d)),
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


def _determinant(matrix: _Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def _translation(value: int | Fraction) -> _Matrix:
    return _matrix(1, value, 0, 1)


def _dilation(value: int | Fraction) -> _Matrix:
    value = Fraction(value)
    if value == 0:
        raise ValueError("a projective dilation must be nonzero")
    return _matrix(value, 0, 0, 1)


def _digit_matrix(value: int | Fraction) -> _Matrix:
    return _matrix(value, 1, 1, 0)


def _matrix_affine(matrix: _Matrix, value: Fraction) -> Fraction | None:
    numerator = matrix[0][0] * value + matrix[0][1]
    denominator = matrix[1][0] * value + matrix[1][1]
    if denominator == 0:
        return None
    return numerator / denominator


def _columns(matrix: _Matrix) -> tuple[tuple[Fraction, Fraction], ...]:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def _real_shadow(matrix: _Matrix) -> tuple[Fraction, Fraction]:
    """Return the exact real and imaginary parts of g(i)."""

    a, b = matrix[0]
    c, d = matrix[1]
    denominator = c * c + d * d
    if denominator == 0:
        raise ValueError("a nonsingular real matrix cannot have zero bottom row")
    return ((a * c + b * d) / denominator, _determinant(matrix) / denominator)


def _real_action(
    matrix: _Matrix,
    point: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Apply a real Mobius matrix to x+i*y without complex arithmetic."""

    a, b = matrix[0]
    c, d = matrix[1]
    x, y = point
    denominator = (c * x + d) ** 2 + (c * y) ** 2
    if denominator == 0:
        raise ZeroDivisionError("real projective action reached a pole")
    return (
        ((a * x + b) * (c * x + d) + a * c * y**2) / denominator,
        _determinant(matrix) * y / denominator,
    )


def _vertex_key(vertex: object) -> tuple[object, ...]:
    return (vertex.prime, vertex.depth, vertex.chart, vertex.coordinate)


def _matrix_size(matrix: _Matrix) -> tuple[int, int]:
    numerators = [abs(entry.numerator) for row in matrix for entry in row]
    denominators = [entry.denominator for row in matrix for entry in row]
    return max(numerators), max(denominators)


@dataclass(frozen=True)
class _Letter:
    name: str
    matrix: _Matrix


_BOREL_WEYL_ALPHABET = (
    _Letter("T-1", _translation(-1)),
    _Letter("T1", _translation(1)),
    _Letter("D-1", _dilation(-1)),
    _Letter("D2", _dilation(2)),
    _Letter("D3", _dilation(3)),
    _Letter("D5", _dilation(5)),
    _Letter("D7", _dilation(7)),
    _Letter("W", _WEYL),
)


def _word_matrix(word: tuple[_Letter, ...]) -> _Matrix:
    result = _IDENTITY
    for letter in word:
        result = _matmul(result, letter.matrix)
    return result


def _all_words(maximum_depth: int) -> tuple[tuple[_Letter, ...], ...]:
    return tuple(
        word
        for depth in range(maximum_depth + 1)
        for word in product(_BOREL_WEYL_ALPHABET, repeat=depth)
    )


@dataclass(frozen=True, order=True)
class _HistoryCost:
    literal_steps: int = 0
    rational_bits: int = 0

    def __add__(self, other: "_HistoryCost") -> "_HistoryCost":
        return _HistoryCost(
            self.literal_steps + other.literal_steps,
            self.rational_bits + other.rational_bits,
        )


@dataclass(frozen=True)
class _RationalHistory:
    """One task-independent marked rational reciprocal history."""

    origin: Fraction
    actions: tuple[Fraction, ...]
    matrices: tuple[_Matrix, ...]
    complete_quotients: tuple[Fraction | None, ...]
    cost: _HistoryCost

    @classmethod
    def compile(
        cls,
        origin: int | Fraction,
        actions: tuple[int | Fraction, ...] = (),
    ) -> "_RationalHistory":
        origin = Fraction(origin)
        rational_actions = tuple(Fraction(action) for action in actions)
        matrices = [_IDENTITY]
        quotients: list[Fraction | None] = [origin]
        current: Fraction | None = origin
        cost = _HistoryCost()
        for action in rational_actions:
            if current is None:
                raise ValueError("a rational history cannot continue past exactness")
            next_matrix = _matmul(matrices[-1], _digit_matrix(action))
            remainder = current - action
            next_quotient = None if remainder == 0 else 1 / remainder
            matrices.append(next_matrix)
            quotients.append(next_quotient)
            cost += _HistoryCost(1, _PHASE6._rational_bits(action))
            if next_quotient is None:
                assert next_matrix[1][0] != 0
                assert next_matrix[0][0] / next_matrix[1][0] == origin
            else:
                assert _matrix_affine(next_matrix, next_quotient) == origin
            current = next_quotient
        return cls(
            origin,
            rational_actions,
            tuple(matrices),
            tuple(quotients),
            cost,
        )

    @property
    def matrix(self) -> _Matrix:
        return self.matrices[-1]

    @property
    def current(self) -> Fraction | None:
        return self.complete_quotients[-1]

    def prefix(self, length: int) -> "_RationalHistory":
        if not 0 <= length <= len(self.actions):
            raise ValueError("history prefix lies outside the literal word")
        return _RationalHistory.compile(self.origin, self.actions[:length])

    def extend(self, suffix: tuple[int | Fraction, ...]) -> "_RationalHistory":
        return _RationalHistory.compile(self.origin, self.actions + tuple(suffix))


def _action_for_bit(value: Fraction, prime: int, bit: int) -> Fraction | None:
    actions = _PHASE7._closed_admissible_actions(value, prime)
    return next(
        (
            action
            for action in actions
            if _PHASE7._lift_bit(value, prime, action) == bit
        ),
        None,
    )


def _history_from_bits(
    origin: int | Fraction,
    prime: int,
    bits: tuple[int, ...],
) -> _RationalHistory:
    history = _RationalHistory.compile(origin)
    for bit in bits:
        if history.current is None:
            raise ValueError("a bit history continued past exactness")
        action = _action_for_bit(history.current, prime, bit)
        if action is None:
            raise ValueError("a bit is invalid in the declared local grammar")
        history = history.extend((action,))
    return history


@dataclass(frozen=True)
class _TaskView:
    prime: int
    precision: int
    horizon: int
    full_decoder: bool


@dataclass(frozen=True)
class _ObservedStep:
    bit: int | None
    action: Fraction
    matrix: _Matrix
    vertex: tuple[object, ...] | None
    next_complete_quotient: Fraction | None
    outcome: str
    cost: tuple[int, int, int, int] | None
    terminal_payload: object | None


@dataclass(frozen=True)
class _TaskResponse:
    origin: Fraction
    trace: tuple[_ObservedStep, ...]
    outcome: str


def _project_task(history: _RationalHistory, view: _TaskView) -> _TaskResponse:
    previous_vertex = _PHASE6._matrix_lattice_vertex(_IDENTITY, view.prime)
    seen = {history.origin}
    trace = []
    current = history.origin
    terminal_outcome = "live"
    for index, action in enumerate(history.actions, start=1):
        actions = _PHASE7._closed_admissible_actions(current, view.prime)
        if action not in actions:
            trace.append(
                _ObservedStep(
                    None,
                    action,
                    history.matrices[index],
                    None,
                    history.complete_quotients[index],
                    "invalid",
                    None,
                    None,
                )
            )
            terminal_outcome = "invalid"
            break
        bit = _PHASE7._lift_bit(current, view.prime, action)

        matrix = history.matrices[index]
        vertex = _PHASE6._matrix_lattice_vertex(matrix, view.prime)
        next_quotient = history.complete_quotients[index]
        stage = _PHASE6._Cost(
            digit_steps=1,
            tree_edges=_PHASE6._tree_distance(previous_vertex, vertex),
            digit_bits=_PHASE6._rational_bits(action),
        )
        payload: object | None = None
        if next_quotient is None:
            outcome = "success_exact"
            decoder = _PHASE6._Cost(
                decoder_bits=(
                    _PHASE6._rational_bits(matrix[0][0])
                    + _PHASE6._rational_bits(matrix[1][0])
                )
            )
            stage += decoder
            if view.full_decoder:
                payload = matrix[0][0] / matrix[1][0]
        elif vertex.depth >= view.precision:
            outcome = "success_precision"
            cylinder = vertex.ancestor_at_depth(view.precision)
            frontier_size = (
                (view.prime + 1) * view.prime ** (view.precision - 1)
            )
            decoder = _PHASE6._Cost(
                decoder_bits=(
                    sum(
                        _PHASE6._rational_bits(entry)
                        for row in matrix
                        for entry in row
                    )
                    + _PHASE6._rational_bits(next_quotient)
                    + _PHASE6._minimum_exact_bits(frontier_size)
                )
            )
            stage += decoder
            if view.full_decoder:
                payload = _vertex_key(cylinder)
        elif next_quotient in seen:
            outcome = "cycle"
            if view.full_decoder:
                payload = next_quotient
        elif index == view.horizon:
            outcome = "horizon"
            if view.full_decoder:
                payload = next_quotient
        else:
            outcome = "live"

        trace.append(
            _ObservedStep(
                bit,
                action,
                matrix,
                _vertex_key(vertex),
                next_quotient,
                outcome,
                (
                    stage.digit_steps,
                    stage.tree_edges,
                    stage.digit_bits,
                    stage.decoder_bits,
                ),
                payload,
            )
        )
        terminal_outcome = outcome
        if outcome != "live":
            break
        assert next_quotient is not None
        seen.add(next_quotient)
        current = next_quotient
        previous_vertex = vertex
    return _TaskResponse(history.origin, tuple(trace), terminal_outcome)


def _forget_decoder(response: _TaskResponse) -> _TaskResponse:
    return _TaskResponse(
        response.origin,
        tuple(replace(step, terminal_payload=None) for step in response.trace),
        response.outcome,
    )


def _coarsen_response(
    response: _TaskResponse,
    coarse_view: _TaskView,
) -> _TaskResponse:
    history = _RationalHistory.compile(
        response.origin,
        tuple(step.action for step in response.trace),
    )
    return _project_task(history, coarse_view)


def _control_state(history: _RationalHistory, prime: int) -> object:
    if history.current is None:
        raise ValueError("an exact terminal is not a live control state")
    quotients = history.complete_quotients
    if len(set(quotients)) != len(quotients):
        raise ValueError("the Phase 6 live state stops before a repeated quotient")
    return _PHASE6._ControlState(
        len(history.actions),
        history.current,
        history.matrix,
        _PHASE6._matrix_lattice_vertex(history.matrix, prime),
        frozenset(quotients),
    )


def _task_state_frontier(
    origin: Fraction,
    *,
    precision: int,
    horizon: int,
) -> tuple[object, dict[tuple[object, ...], tuple[object, tuple[object, ...]]]]:
    task = _PHASE6._Task(
        3,
        origin,
        precision=precision,
        horizon=horizon,
        max_states=50_000,
        max_transitions=100_000,
    )
    _, states = _PHASE7._enumerate_closed_graph(task)
    solution = _PHASE7._solve_closed(task, graph_certified=True)
    frontiers = {state.key: (state, frontier) for state, frontier in solution.state_values}
    assert set(frontiers) == {state.key for state in states}
    return task, frontiers


def _envelope(
    origins: tuple[Fraction, ...],
    primes: tuple[int, ...],
    maximum_depth: int,
) -> frozenset[_RationalHistory]:
    histories = {_RationalHistory.compile(origin) for origin in origins}
    frontier = {
        (prime, _RationalHistory.compile(origin))
        for prime in primes
        for origin in origins
    }
    for _ in range(maximum_depth):
        next_frontier = set()
        for prime, history in frontier:
            if history.current is None:
                continue
            for bit in (0, 1):
                action = _action_for_bit(history.current, prime, bit)
                if action is None:
                    continue
                extended = history.extend((action,))
                histories.add(extended)
                next_frontier.add((prime, extended))
        frontier = next_frontier
    return frozenset(histories)


def _valid_at_place(history: _RationalHistory, prime: int) -> bool:
    current = history.origin
    for index, action in enumerate(history.actions):
        if action not in _PHASE7._closed_admissible_actions(current, prime):
            return False
        remainder = current - action
        if remainder == 0:
            return index + 1 == len(history.actions)
        current = 1 / remainder
    return True


def _scalar_curvature(metric: sp.Matrix, coordinates: tuple[sp.Symbol, ...]) -> sp.Expr:
    dimension = len(coordinates)
    inverse = sp.simplify(metric.inv())
    christoffel = [
        [
            [
                sp.simplify(
                    sum(
                        inverse[k, ell]
                        * (
                            sp.diff(metric[ell, j], coordinates[i])
                            + sp.diff(metric[ell, i], coordinates[j])
                            - sp.diff(metric[i, j], coordinates[ell])
                        )
                        / 2
                        for ell in range(dimension)
                    )
                )
                for j in range(dimension)
            ]
            for i in range(dimension)
        ]
        for k in range(dimension)
    ]
    ricci = sp.zeros(dimension)
    for i in range(dimension):
        for j in range(dimension):
            ricci[i, j] = sp.simplify(
                sum(
                    sp.diff(christoffel[k][i][j], coordinates[k])
                    - sp.diff(christoffel[k][i][k], coordinates[j])
                    + sum(
                        christoffel[k][k][ell] * christoffel[ell][i][j]
                        - christoffel[k][j][ell] * christoffel[ell][i][k]
                        for ell in range(dimension)
                    )
                    for k in range(dimension)
                )
            )
    return sp.simplify(
        sum(
            inverse[i, j] * ricci[i, j]
            for i in range(dimension)
            for j in range(dimension)
        )
    )


def test_gate9a_am_group_inversion_intertwines_the_two_hyperbolic_charts():
    a, v, c = sp.symbols("a v c", real=True, positive=True)
    left_chart = sp.Matrix((a, sp.exp(v)))
    inverse = sp.Matrix((-a * sp.exp(-v), -v))
    right_chart = sp.Matrix((-a * sp.exp(-v), sp.exp(-v)))
    assert left_chart.subs({a: inverse[0], v: inverse[1]}, simultaneous=True) == right_chart
    assert sp.simplify(a + sp.exp(v) * inverse[0]) == 0
    assert sp.simplify(v + inverse[1]) == 0

    coordinates = (a, v)
    jacobian_right = right_chart.jacobian(coordinates)
    hyperbolic_right = sp.diag(*(sp.exp(2 * v),) * 2)
    pulled_right = sp.simplify(jacobian_right.T * hyperbolic_right * jacobian_right)
    process_metric = sp.Matrix(((1, -a), (-a, a**2 + 1)))
    assert sp.simplify(pulled_right - process_metric) == sp.zeros(2)

    u, w = sp.symbols("u w", real=True)
    left_metric = sp.diag(sp.exp(-2 * w), 1)
    inverse_jacobian = inverse.jacobian(coordinates)
    inverse_pullback = sp.simplify(
        inverse_jacobian.T
        * left_metric.subs({u: inverse[0], w: inverse[1]}, simultaneous=True)
        * inverse_jacobian
    )
    assert sp.simplify(inverse_pullback - process_metric) == sp.zeros(2)

    weighted_metric = sp.Matrix(((1, -a), (-a, a**2 + c)))
    assert sp.simplify(_scalar_curvature(weighted_metric, coordinates) + 2 / c) == 0

    # In x=-a*e^-v, y=e^-v and then X=x/sqrt(c), g_c is c times
    # (dX^2+dy^2)/y^2.  Hence K=-1/c; c is a declared ruler, not canonical.
    x, y, X = sp.symbols("x y X", positive=True)
    chart_metric = sp.diag(1 / y**2, c / y**2)
    rescale_jacobian = sp.Matrix(((sp.sqrt(c), 0), (0, 1)))
    assert sp.simplify(
        rescale_jacobian.T * chart_metric * rescale_jacobian
        - c * sp.diag(1 / y**2, 1 / y**2)
    ) == sp.zeros(2)


def test_gate9b_borel_and_weyl_construct_every_frozen_projective_frame():
    matrices = tuple(
        _matrix(a, b, c, d)
        for a, b, c, d in product(range(-2, 3), repeat=4)
        if a * d - b * c != 0
    )
    assert len(matrices) == 496
    for matrix in matrices:
        a, b = matrix[0]
        c, d = matrix[1]
        determinant = _determinant(matrix)
        if c == 0:
            assert matrix[1][0] == 0
            continue
        left = _matrix(determinant / c, a / c, 0, 1)
        right = _matrix(c, d, 0, 1)
        assert _matmul(_matmul(left, _WEYL), right) == matrix

    words = _all_words(5)
    assert len(words) == 37_449
    maximum_numerator = maximum_denominator = 0
    local_depths = {prime: Counter() for prime in (3, 5, 7)}
    for word in words:
        matrix = _word_matrix(word)
        assert _determinant(matrix) != 0
        numerator, denominator = _matrix_size(matrix)
        maximum_numerator = max(maximum_numerator, numerator)
        maximum_denominator = max(maximum_denominator, denominator)
        for prime in (3, 5, 7):
            vertex = _PHASE3._matrix_lattice_vertex(matrix, prime)
            local_depths[prime][vertex.depth] += 1

    assert (maximum_numerator, maximum_denominator) == (16807, 1)
    assert {
        prime: dict(sorted(counts.items()))
        for prime, counts in local_depths.items()
    } == {
        3: {0: 20000, 1: 13602, 2: 3357, 3: 456, 4: 33, 5: 1},
        5: {0: 20000, 1: 13602, 2: 3357, 3: 456, 4: 33, 5: 1},
        7: {0: 20000, 1: 13602, 2: 3357, 3: 456, 4: 33, 5: 1},
    }

    frame = _matrix(2, 3, 5, 7)
    first, second = _columns(frame)
    assert _columns(_matmul(frame, _WEYL)) == (second, (-first[0], -first[1]))
    assert _columns(_matmul(frame, _RECIPROCAL)) == (second, first)
    assert _determinant(_matmul(frame, _WEYL)) == _determinant(frame)
    assert _determinant(_matmul(frame, _RECIPROCAL)) == -_determinant(frame)
    assert _matrix_affine(_WEYL, Fraction(0)) is None

    # Matrix lowering is semantic, not the literal-history carrier.
    assert _word_matrix(()) == _word_matrix(
        (_BOREL_WEYL_ALPHABET[1], _BOREL_WEYL_ALPHABET[0])
    )
    assert () != (_BOREL_WEYL_ALPHABET[1], _BOREL_WEYL_ALPHABET[0])


def test_gate9c_regular_continued_fractions_replay_with_orientation_retained():
    audited = 0
    maximum_matrix_entry = 0
    for length in range(9):
        for letters in product("LR", repeat=length):
            stern_word = "".join(letters)
            endpoint = _PHASE2._stern_brocot_endpoint(stern_word)
            digits = _PHASE2._canonical_rational_continued_fraction(endpoint)
            phase2_matrix = tuple(
                tuple(Fraction(entry) for entry in row)
                for row in _PHASE2._continued_fraction_matrix(digits)
            )
            through_reciprocal = _IDENTITY
            through_weyl = _IDENTITY
            for digit in digits:
                through_reciprocal = _matmul(
                    through_reciprocal,
                    _matmul(_translation(digit), _RECIPROCAL),
                )
                through_weyl = _matmul(
                    through_weyl,
                    _matmul(
                        _matmul(_translation(digit), _dilation(-1)),
                        _WEYL,
                    ),
                )
            assert phase2_matrix == through_reciprocal == through_weyl
            assert _PHASE2._right_reciprocal_history_value(digits) == endpoint
            literal_matrix = tuple(
                tuple(Fraction(entry) for entry in row)
                for row in _PHASE2._right_reciprocal_history_matrix(digits)
            )
            assert _matrix_affine(literal_matrix, Fraction(digits[-1])) == endpoint
            assert _PHASE2._stern_brocot_word(digits) == stern_word
            assert _determinant(phase2_matrix) == Fraction((-1) ** len(digits))

            convergents = _PHASE2._convergents(digits)
            current = convergents[-1]
            previous = (1, 0) if len(convergents) == 1 else convergents[-2]
            assert _columns(phase2_matrix) == (current, previous)
            lower, upper = _PHASE2._cylinder_interval(digits)
            assert lower <= endpoint <= upper
            maximum_matrix_entry = max(
                maximum_matrix_entry,
                *(
                    abs(entry.numerator)
                    for row in phase2_matrix
                    for entry in row
                ),
            )
            audited += 1

    assert (audited, maximum_matrix_entry) == (511, 55)
    assert _matmul(_dilation(-1), _WEYL) == _RECIPROCAL
    assert _real_shadow(_WEYL) == (Fraction(0), Fraction(1))
    assert _real_shadow(_RECIPROCAL) == (Fraction(0), Fraction(-1))

    # Equal endpoints do not make a continuation-stable source quotient.
    canonical = _RationalHistory.compile(Fraction(3, 2), ())
    assert canonical.origin == _PHASE2._continued_fraction_value((1, 2))
    assert canonical.origin == _PHASE2._continued_fraction_value((1, 1, 1))
    assert _PHASE2._continued_fraction_matrix((1, 2)) != (
        _PHASE2._continued_fraction_matrix((1, 1, 1))
    )


def test_gate9d_one_rational_frame_has_distinct_compatible_place_shadows():
    words = _all_words(4)
    assert len(words) == 4_681
    depth_histograms = {prime: Counter() for prime in (3, 5, 7)}
    for word in words:
        matrix = _word_matrix(word)
        real_x, real_y = _real_shadow(matrix)
        assert real_x.denominator > 0
        assert (real_y > 0) - (real_y < 0) == (
            (_determinant(matrix) > 0) - (_determinant(matrix) < 0)
        )
        direct_real = (Fraction(0), Fraction(1))
        for letter in reversed(word):
            direct_real = _real_action(letter.matrix, direct_real)
        assert direct_real == (real_x, real_y)

        direct_matrix = _IDENTITY
        for prime in (3, 5, 7):
            direct_matrix = _IDENTITY
            for letter in word:
                direct_matrix = _matmul(direct_matrix, letter.matrix)
            assert direct_matrix == matrix
            lowered = _PHASE3._matrix_lattice_vertex(matrix, prime)
            assert lowered.prime == prime
            depth_histograms[prime][lowered.depth] += 1

    assert {prime: dict(sorted(counts.items())) for prime, counts in depth_histograms.items()} == {
        3: {0: 2826, 1: 1536, 2: 291, 3: 27, 4: 1},
        5: {0: 2826, 1: 1536, 2: 291, 3: 27, 4: 1},
        7: {0: 2826, 1: 1536, 2: 291, 3: 27, 4: 1},
    }

    # The sign unit fixes the root but acts nontrivially on outgoing affine
    # directions.  Root quotient and projective-contact interfaces differ.
    for prime in (3, 5, 7):
        root = _PHASE3._matrix_lattice_vertex(_IDENTITY, prime)
        sign_root = _PHASE3._matrix_lattice_vertex(_dilation(-1), prime)
        positive = _PHASE3._projective_contact(Fraction(1), prime)
        negative = _PHASE3._projective_contact(Fraction(-1), prime)
        assert sign_root == root
        assert positive.depth == negative.depth == 1
        assert positive.coordinate == 1
        assert negative.coordinate == prime - 1
        assert positive != negative

    # The ordinary reciprocal and Weyl operation are identical only after a
    # sign dilation; their real orientation components remain opposite.
    assert _matmul(_dilation(-1), _WEYL) == _RECIPROCAL
    assert _real_shadow(_WEYL)[1] > 0 > _real_shadow(_RECIPROCAL)[1]


def test_gate9e_marked_rational_envelope_projects_to_tasks_without_task_tags():
    origins = tuple(
        map(
            Fraction,
            (-11, Fraction(-7, 8), Fraction(-1, 5), -12,
             Fraction(-6, 5), Fraction(3, 11), Fraction(-8, 11),
             Fraction(17, 7)),
        )
    )
    envelope = _envelope(origins, (3, 5, 7), 4)
    assert all(len(history.actions) <= 4 for history in envelope)
    assert len(envelope) == 438
    assert Counter(len(history.actions) for history in envelope) == {
        0: 8,
        1: 42,
        2: 82,
        3: 138,
        4: 168,
    }
    assert max(_matrix_size(history.matrix)[0] for history in envelope) == 3_804_769
    assert max(_matrix_size(history.matrix)[1] for history in envelope) == 2_401
    assert max(history.cost.rational_bits for history in envelope) == 36

    coarse = _TaskView(3, 6, 24, True)
    fine = _TaskView(3, 8, 24, True)
    scalar_fine = _TaskView(3, 8, 24, False)
    short_horizon = _TaskView(3, 100, 2, True)
    long_horizon = _TaskView(3, 100, 4, True)
    for history in envelope:
        # Literal concatenation, matrix lowering, and the declared vector cost
        # all compose before a task chooses a stopping section.
        for split in range(len(history.actions) + 1):
            prefix = history.prefix(split)
            suffix = history.actions[split:]
            assert prefix.extend(suffix) == history
            suffix_cost = _RationalHistory.compile(
                prefix.current if prefix.current is not None else prefix.origin,
                suffix,
            ).cost if suffix else _HistoryCost()
            if prefix.current is not None:
                assert prefix.cost + suffix_cost == history.cost

            prefix_response = _project_task(prefix, fine)
            full_response = _project_task(history, fine)
            if prefix_response.outcome != "live":
                assert prefix_response == full_response
            else:
                assert prefix_response.trace == full_response.trace[:split]

        # The fine response retains enough stopped trace for the depth-eight
        # to depth-six comparison map; the task-refinement triangle commutes.
        fine_response = _project_task(history, fine)
        assert _coarsen_response(fine_response, coarse) == _project_task(
            history, coarse
        )
        assert _forget_decoder(fine_response) == _project_task(
            history, scalar_fine
        )
        assert _coarsen_response(
            _project_task(history, long_horizon), short_horizon
        ) == _project_task(history, short_horizon)

        # Independent Phase 3 prefix replay gives the same local lattice
        # shadow as lowering the final rational matrix and then changing place.
        for prime in (3, 5, 7):
            direct = _PHASE3._prefix_path_metric(history.actions, prime).vertices[-1]
            lowered = _PHASE3._matrix_lattice_vertex(history.matrix, prime)
            assert direct == lowered

    assert Counter(_project_task(history, coarse).outcome for history in envelope) == {
        "cycle": 9,
        "invalid": 293,
        "live": 60,
        "success_exact": 36,
        "success_precision": 40,
    }
    assert Counter(_project_task(history, fine).outcome for history in envelope) == {
        "cycle": 26,
        "invalid": 293,
        "live": 73,
        "success_exact": 39,
        "success_precision": 7,
    }

    # Literal extension is injective upstairs.  Merging appears only after
    # projection to the local lattice interface: at p=3, 137 distinct child
    # histories occupy 48 (bit, target-vertex) slots, and ten slots even merge
    # distinct source vertices.  The 293 invalid D6/D8 responses above are
    # exactly histories generated at another place and rejected by p=3.
    assert sum(_valid_at_place(history, 3) for history in envelope) == 145
    local_preimages: dict[tuple[object, ...], set[tuple[object, ...]]] = defaultdict(set)
    local_source_vertices: dict[
        tuple[object, ...], set[tuple[object, ...]]
    ] = defaultdict(set)
    child_parents = {}
    for history in envelope:
        if (
            len(history.actions) == 4
            or history.current is None
            or not _valid_at_place(history, 3)
        ):
            continue
        for bit in (0, 1):
            action = _action_for_bit(history.current, 3, bit)
            if action is None:
                continue
            child = history.extend((action,))
            assert child in envelope
            child_key = (child.origin, child.actions)
            parent_key = (history.origin, history.actions)
            assert child_parents.setdefault(child_key, parent_key) == parent_key
            target_vertex = _vertex_key(
                _PHASE3._matrix_lattice_vertex(child.matrix, 3)
            )
            source_vertex = _vertex_key(
                _PHASE3._matrix_lattice_vertex(history.matrix, 3)
            )
            local_key = (bit, target_vertex)
            local_preimages[local_key].add(parent_key)
            local_source_vertices[local_key].add(source_vertex)
    assert (len(child_parents), len(local_preimages)) == (137, 48)
    assert sum(len(values) > 1 for values in local_preimages.values()) == 36
    assert sum(len(values) > 1 for values in local_source_vertices.values()) == 10


def test_gate9e_phase7_and_phase8_witnesses_have_exact_upstairs_provenance():
    provenance = {
        "immediate_residual": "place_observer_forgets_complete_quotient",
        "transported_future": "rational_history_precedes_local_projection",
        "changed_stopping": "precision_projection",
        "full_decoder": "marked_rational_frame",
    }

    # Immediate Phase 7 residual: one local S2 class, three rational states,
    # and disjoint decoder-optimal future bits under the same task contract.
    immediate = (
        (Fraction(-11), Fraction(-1, 12), frozenset({0})),
        (Fraction(-7, 8), Fraction(-8, 15), frozenset({1})),
        (Fraction(-1, 5), Fraction(-5, 6), frozenset({0})),
    )
    signatures = []
    for origin, alpha, expected_bits in immediate:
        history = _RationalHistory.compile(origin, (Fraction(1),))
        assert history.current == alpha
        task, frontiers = _task_state_frontier(origin, precision=4, horizon=16)
        state = _control_state(history, 3)
        stored_state, frontier = frontiers[state.key]
        signatures.append(_PHASE7._signature(task, stored_state, 2))
        assert _PHASE7._optimal_bits(
            task, stored_state, frontier, "decoder_bits"
        ) == expected_bits
    assert len(set(signatures)) == 1

    # Equal current policy does not identify transported rational futures.
    transported_histories = []
    transported_signatures = []
    for origin, reached in (
        (Fraction(-12), Fraction(-4, 3)),
        (Fraction(-6, 5), Fraction(-2, 3)),
    ):
        task, frontiers = _task_state_frontier(origin, precision=4, horizon=16)
        initial = _PHASE6._initial_state(origin, 3)
        _, frontier = frontiers[initial.key]
        assert _PHASE7._optimal_bits(
            task, initial, frontier, "decoder_bits"
        ) == frozenset({0})
        transported_signatures.append(_PHASE7._signature(task, initial, 2))
        history = _history_from_bits(origin, 3, (0, 0))
        assert history.current == reached
        assert _project_task(history, _TaskView(3, 4, 16, True)).outcome == "live"
        transported_histories.append((task, history))
    assert transported_signatures[0] == transported_signatures[1]
    reached_signatures = [
        _PHASE7._signature(task, _control_state(history, 3), 2)
        for task, history in transported_histories
    ]
    assert reached_signatures[0] != reached_signatures[1]
    assert tuple(
        _PHASE6._padic_floor(history.current, 3, "ruban")
        for _, history in transported_histories
    ) == (Fraction(5, 3), Fraction(7, 3))

    # One untruncated arithmetic history has two task shadows.  D6 makes the
    # fourth edge terminal; D8 keeps exactly the same rational edge live.
    stopping_history = _history_from_bits(Fraction(3, 11), 3, (0, 1, 0, 0))
    d6 = _TaskView(3, 6, 24, True)
    d8 = _TaskView(3, 8, 24, True)
    d6_response = _project_task(stopping_history, d6)
    d8_response = _project_task(stopping_history, d8)
    assert d6_response.outcome == "success_precision"
    assert d8_response.outcome == "live"
    assert d6_response.trace[-1].cost == (1, 2, 5, 50)
    assert d8_response.trace[-1].cost == (1, 2, 5, 0)
    assert _coarsen_response(d8_response, d6) == d6_response

    # Full decoding distinguishes two scalar-identical exact edges.  The
    # rational prefix frame and its origin mark retain what the local S2
    # interface forgot; the final exact column reconstructs each origin.
    exact_records = []
    for origin in (Fraction(-8, 11), Fraction(17, 7)):
        task, frontiers = _task_state_frontier(origin, precision=6, horizon=24)
        match = next(
            (state, frontier)
            for state, frontier in frontiers.values()
            if state.step == 2 and state.complete_quotient == Fraction(1, 3)
        )
        state, _ = match
        bits = next(
            bit_word
            for bit_word in product((0, 1), repeat=2)
            if (
                (candidate := _history_from_bits(origin, 3, bit_word)).current
                == Fraction(1, 3)
                and candidate.matrix == state.prefix_matrix
            )
        )
        history = _history_from_bits(origin, 3, bits + (0,))
        full = _project_task(history, _TaskView(3, 6, 24, True))
        scalar = _project_task(history, _TaskView(3, 6, 24, False))
        assert full.outcome == scalar.outcome == "success_exact"
        assert full.trace[-1].cost == scalar.trace[-1].cost == (1, 2, 3, 16)
        assert full.trace[-1].terminal_payload == origin
        assert _forget_decoder(full) == scalar
        exact_records.append((task, state, full))
    assert _PHASE7._signature(exact_records[0][0], exact_records[0][1], 2) == (
        _PHASE7._signature(exact_records[1][0], exact_records[1][1], 2)
    )
    assert exact_records[0][2].trace[-1].terminal_payload != (
        exact_records[1][2].trace[-1].terminal_payload
    )

    assert provenance == {
        "immediate_residual": "place_observer_forgets_complete_quotient",
        "transported_future": "rational_history_precedes_local_projection",
        "changed_stopping": "precision_projection",
        "full_decoder": "marked_rational_frame",
    }


def test_gate9e_common_carrier_is_horizontal_not_vertical_objectification():
    lower_generators = {letter.name for letter in _BOREL_WEYL_ALPHABET}
    proposed_new_generators: set[str] = set()
    lowering_domain = {letter.name for letter in _BOREL_WEYL_ALPHABET}

    assert lower_generators == lowering_domain
    assert proposed_new_generators == set()
    assert not (
        proposed_new_generators
        and proposed_new_generators <= lowering_domain
    )

    # Phase 9 supplies comparison maps between a marked rational source and
    # local/task shadows.  It supplies no new free alphabet and therefore
    # cannot satisfy the separate V3/V4 generation-and-lowering gate.
