"""Gate 6A for the finite p-adic selector-policy Bellman task.

The Phase 6 contract deliberately separates task validation from transition,
decoding, graph exhaustion, and optimization.  This executable essay owns only
the first gate:

* enumerate the frozen coefficient grammar exactly and quotient duplicate
  syntactic coefficient tuples by their rational action value;
* certify that Ruban and Browkin I actions are admitted on a tiny baseline
  reachability corpus;
* freeze an exact, hashable state key that retains the complete quotient,
  chronological matrix payload, standard-frame lattice value, and visited
  complete-quotient witness;
* distinguish invalid parameters, invalid grammar, malformed state, and an
  explicitly bounded enumeration from an empty or negative optimization
  result.
* certify the exact transition order and the shared exact/precision decoders.

No reachable-graph census, Bellman recursion, policy comparison, or preferred
p-adic section is implemented here.  All arithmetic is exact over
``Fraction``.  The code remains research-local and introduces no package API.

Mathematical lineage: [Ruban-1970], [Browkin-1978], and
[Serre-Trees-1980] in ``docs/REFERENCES.md``.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from time import perf_counter
from typing import Literal

import pytest


_Selector = Literal["ruban", "browkin"]
_Matrix = tuple[
    tuple[Fraction, Fraction],
    tuple[Fraction, Fraction],
]
_IDENTITY: _Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)


class _InvalidTaskParameter(ValueError):
    """The declared finite task is not defined for the supplied parameter."""


class _InvalidActionGrammar(RuntimeError):
    """The frozen action grammar fails one of its semantic obligations."""


class _ArithmeticOrStateFailure(RuntimeError):
    """An exact arithmetic invariant or state-record invariant failed."""


class _InconclusiveWithinResourceBudget(RuntimeError):
    """A declared finite enumeration was not attempted beyond its budget."""


_Outcome = Literal[
    "live",
    "success_exact",
    "success_precision",
    "cycle",
    "horizon",
]


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def _validate_prime(prime: int) -> None:
    if not _is_prime(prime):
        raise _InvalidTaskParameter("prime must be prime")
    if prime == 2:
        raise _InvalidTaskParameter("the frozen task requires an odd prime")


def _valuation(value: Fraction, prime: int) -> int:
    """Return ``v_p(value)`` and reject the undefined valuation of zero."""

    _validate_prime(prime)
    value = Fraction(value)
    if value == 0:
        raise _InvalidTaskParameter("the valuation of zero is not finite")
    numerator = abs(value.numerator)
    denominator = value.denominator
    result = 0
    while numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def _prime_power(prime: int, exponent: int) -> Fraction:
    _validate_prime(prime)
    if exponent >= 0:
        return Fraction(prime**exponent)
    return Fraction(1, prime ** (-exponent))


def _rational_mod(value: Fraction, modulus: int) -> int:
    value = Fraction(value)
    if modulus <= 0:
        raise _InvalidTaskParameter("modulus must be positive")
    if gcd(value.denominator, modulus) != 1:
        raise _InvalidTaskParameter("the denominator is not a modular unit")
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def _padic_floor(value: Fraction, prime: int, selector: _Selector) -> Fraction:
    """Return the exact Ruban or Browkin-I Laurent truncation."""

    _validate_prime(prime)
    if selector not in ("ruban", "browkin"):
        raise _InvalidTaskParameter("unknown p-adic floor selector")
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
        coefficient = _rational_mod(remainder / place, prime)
        if selector == "browkin" and coefficient > prime // 2:
            coefficient -= prime
        digit += coefficient * place
        remainder -= coefficient * place
    return digit


def _coefficient_tuple_count(value: Fraction, prime: int) -> int:
    """Return the Cartesian-product size before semantic filtering."""

    value = Fraction(value)
    if value == 0:
        return 1
    first_exponent = min(_valuation(value, prime), 0)
    number_of_places = 1 - first_exponent
    return (2 * prime - 1) ** number_of_places


def _raw_admissible_actions(
    value: Fraction,
    prime: int,
    *,
    max_candidates: int,
) -> tuple[Fraction, ...]:
    """Enumerate admissible values before quotienting syntactic duplicates."""

    _validate_prime(prime)
    if max_candidates <= 0:
        raise _InvalidTaskParameter("max_candidates must be positive")
    value = Fraction(value)
    if value == 0:
        return (Fraction(0),)

    candidate_count = _coefficient_tuple_count(value, prime)
    if candidate_count > max_candidates:
        raise _InconclusiveWithinResourceBudget(
            f"action grammar needs {candidate_count} coefficient tuples, "
            f"above budget {max_candidates}"
        )

    first_exponent = min(_valuation(value, prime), 0)
    exponents = tuple(range(first_exponent, 1))
    coefficient_range = range(-(prime - 1), prime)
    admissible = []
    for coefficients in product(coefficient_range, repeat=len(exponents)):
        action = sum(
            (
                Fraction(coefficient) * _prime_power(prime, exponent)
                for coefficient, exponent in zip(coefficients, exponents)
            ),
            start=Fraction(0),
        )
        remainder = value - action
        if remainder == 0 or _valuation(remainder, prime) >= 1:
            admissible.append(action)
    return tuple(admissible)


def _admissible_actions(
    value: Fraction,
    prime: int,
    *,
    max_candidates: int = 100_000,
) -> tuple[Fraction, ...]:
    """Return the frozen action grammar as sorted distinct rationals."""

    raw_actions = _raw_admissible_actions(
        value,
        prime,
        max_candidates=max_candidates,
    )
    actions = tuple(sorted(set(raw_actions)))
    if not actions:
        raise _InvalidActionGrammar("the frozen grammar produced no action")
    if any(
        value != action and _valuation(Fraction(value) - action, prime) < 1
        for action in actions
    ):
        raise _InvalidActionGrammar("an action violates floor-contact semantics")
    return actions


@dataclass(frozen=True, order=True)
class _LatticeVertex:
    """One exact Phase-1 standard-root lattice class."""

    prime: int
    depth: int
    chart: Literal["root", "affine", "infinity"]
    coordinate: int

    def __post_init__(self) -> None:
        _validate_prime(self.prime)
        if self.depth < 0:
            raise _ArithmeticOrStateFailure("lattice depth must be nonnegative")
        if self.depth == 0:
            if (self.chart, self.coordinate) != ("root", 0):
                raise _ArithmeticOrStateFailure(
                    "depth zero has only the standard root"
                )
            return
        if self.chart == "affine":
            bound = self.prime**self.depth
        elif self.chart == "infinity":
            bound = self.prime ** (self.depth - 1)
        else:
            raise _ArithmeticOrStateFailure(
                "positive-depth class needs a projective chart"
            )
        if not 0 <= self.coordinate < bound:
            raise _ArithmeticOrStateFailure(
                "lattice coordinate is outside its canonical range"
            )

    @property
    def parent(self) -> "_LatticeVertex":
        if self.depth == 0:
            raise _ArithmeticOrStateFailure("the standard root has no parent")
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

    def ancestor_at_depth(self, depth: int) -> "_LatticeVertex":
        if not 0 <= depth <= self.depth:
            raise _ArithmeticOrStateFailure(
                "requested ancestor depth is outside the root path"
            )
        cursor = self
        while cursor.depth > depth:
            cursor = cursor.parent
        return cursor

    def is_ancestor_of(self, descendant: "_LatticeVertex") -> bool:
        if self.prime != descendant.prime or self.depth > descendant.depth:
            return False
        return descendant.ancestor_at_depth(self.depth) == self


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


def _determinant(matrix: _Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def _matrix_affine(matrix: _Matrix, value: Fraction) -> Fraction:
    numerator = matrix[0][0] * value + matrix[0][1]
    denominator = matrix[1][0] * value + matrix[1][1]
    if denominator == 0:
        raise _ArithmeticOrStateFailure("projective decoder reached infinity")
    return numerator / denominator


def _matrix_affine_preimage(matrix: _Matrix, image: Fraction) -> Fraction:
    """Recover the rational complete quotient from payload and episode input."""

    image = Fraction(image)
    denominator = image * matrix[1][0] - matrix[0][0]
    if denominator == 0:
        raise _ArithmeticOrStateFailure("inverse projective decoder reached infinity")
    value = (matrix[0][1] - image * matrix[1][1]) / denominator
    if _matrix_affine(matrix, value) != image:
        raise _ArithmeticOrStateFailure("inverse projective round trip failed")
    return value


def _lowest_common_ancestor(
    left: _LatticeVertex,
    right: _LatticeVertex,
) -> _LatticeVertex:
    if left.prime != right.prime:
        raise _ArithmeticOrStateFailure("tree vertices use different primes")
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


def _rational_bits(value: Fraction) -> int:
    value = Fraction(value)
    return (
        max(1, abs(value.numerator).bit_length())
        + value.denominator.bit_length()
    )


def _minimum_exact_bits(number_of_states: int) -> int:
    if number_of_states <= 0:
        raise _InvalidTaskParameter("a finite label set must be nonempty")
    return (number_of_states - 1).bit_length()


def _matrix_lattice_vertex(matrix: _Matrix, prime: int) -> _LatticeVertex:
    """Evaluate a prefix matrix in the Phase-1 standard lattice frame."""

    _validate_prime(prime)
    nonzero_entries = [entry for row in matrix for entry in row if entry != 0]
    if not nonzero_entries:
        raise _ArithmeticOrStateFailure("the zero matrix has no lattice class")
    minimum = min(_valuation(entry, prime) for entry in nonzero_entries)
    scale = _prime_power(prime, -minimum)
    normalized = tuple(
        tuple(entry * scale for entry in row)
        for row in matrix
    )
    determinant = _determinant(normalized)  # type: ignore[arg-type]
    if determinant == 0:
        raise _ArithmeticOrStateFailure(
            "a singular matrix has no Bruhat--Tits vertex"
        )
    depth = _valuation(determinant, prime)
    if depth < 0:
        raise _ArithmeticOrStateFailure(
            "entry normalization produced a negative lattice depth"
        )
    if depth == 0:
        return _LatticeVertex(prime, 0, "root", 0)

    adjugate_rows = (
        (normalized[1][1], -normalized[0][1]),
        (-normalized[1][0], normalized[0][0]),
    )
    primitive = next(
        (
            row
            for row in adjugate_rows
            if any(
                entry != 0 and _valuation(entry, prime) == 0
                for entry in row
            )
        ),
        None,
    )
    if primitive is None:
        raise _ArithmeticOrStateFailure("no primitive adjugate row exists")
    first, second = primitive
    modulus = prime**depth
    if second != 0 and _valuation(second, prime) == 0:
        coordinate = _rational_mod(first / second, modulus)
        return _LatticeVertex(prime, depth, "affine", coordinate)

    if first == 0 or _valuation(first, prime) != 0:
        raise _ArithmeticOrStateFailure("adjugate row has no unit coordinate")
    normalized_second = _rational_mod(second / first, modulus)
    if normalized_second % prime:
        raise _ArithmeticOrStateFailure("infinity-chart coordinate is malformed")
    return _LatticeVertex(
        prime,
        depth,
        "infinity",
        normalized_second // prime,
    )


@dataclass(frozen=True)
class _ControlState:
    """The exact pre-action state frozen by the Phase 6 contract."""

    step: int
    complete_quotient: Fraction
    prefix_matrix: _Matrix
    lattice_vertex: _LatticeVertex
    visited_complete_quotients: frozenset[Fraction]

    @property
    def key(self) -> tuple[object, ...]:
        return (
            self.step,
            self.complete_quotient,
            self.prefix_matrix,
            self.lattice_vertex,
            self.visited_complete_quotients,
        )


@dataclass(frozen=True)
class _Task:
    """One finite task instance; the frozen workload uses depth 4, horizon 16."""

    prime: int
    initial: Fraction
    precision: int = 4
    horizon: int = 16
    max_action_candidates: int = 100_000
    max_states: int = 100_000
    max_transitions: int = 200_000

    def __post_init__(self) -> None:
        _validate_prime(self.prime)
        if self.precision <= 0:
            raise _InvalidTaskParameter("precision must be positive")
        if self.horizon <= 0:
            raise _InvalidTaskParameter("horizon must be positive")
        if self.max_action_candidates <= 0:
            raise _InvalidTaskParameter("action budget must be positive")
        if self.max_states <= 0:
            raise _InvalidTaskParameter("state budget must be positive")
        if self.max_transitions <= 0:
            raise _InvalidTaskParameter("transition budget must be positive")
        object.__setattr__(self, "initial", Fraction(self.initial))


@dataclass(frozen=True)
class _Transition:
    """One exact transition result before any cost or Bellman ledger."""

    outcome: _Outcome
    action: Fraction
    prefix_matrix: _Matrix
    lattice_vertex: _LatticeVertex
    next_complete_quotient: Fraction | None
    next_state: _ControlState | None
    cylinder: _LatticeVertex | None = None
    repeated_complete_quotient: Fraction | None = None


@dataclass(frozen=True)
class _GraphCensus:
    """Exact finite graph coverage and a separate compilation-cost ledger."""

    states: int
    enumerated_actions: int
    success_exact: int
    success_precision: int
    cycles: int
    horizons: int
    maximum_live_step: int
    states_by_step: tuple[int, ...]
    maximum_coefficient_tuples: int
    single_action_states: int
    two_action_states: int
    states_with_nonbaseline_action: int
    compilation_seconds: float


@dataclass(frozen=True, order=True)
class _Cost:
    """The four separately ruled online axes from the frozen contract."""

    digit_steps: int = 0
    tree_edges: int = 0
    digit_bits: int = 0
    decoder_bits: int = 0

    def __add__(self, other: "_Cost") -> "_Cost":
        return _Cost(
            self.digit_steps + other.digit_steps,
            self.tree_edges + other.tree_edges,
            self.digit_bits + other.digit_bits,
            self.decoder_bits + other.decoder_bits,
        )


@dataclass(frozen=True)
class _ParetoValue:
    """One replayable successful Bellman value."""

    outcome: Literal["success_exact", "success_precision"]
    cost: _Cost
    actions: tuple[Fraction, ...]


@dataclass(frozen=True)
class _BellmanResult:
    """A Pareto frontier plus a compilation/storage ledger."""

    frontier: tuple[_ParetoValue, ...]
    solved_states: int
    stored_values: int
    candidate_values: int
    compilation_seconds: float


@dataclass(frozen=True)
class _PolicyRun:
    """One fixed-policy outcome under the shared task contract."""

    outcome: Literal[
        "success_exact",
        "success_precision",
        "cycle",
        "horizon",
    ]
    actions: tuple[Fraction, ...]
    cost: _Cost | None
    evaluation_seconds: float


@dataclass(frozen=True)
class _PolicyTableLedger:
    """A reproducible storage proxy, separate from online geometry cost."""

    axis: Literal["digit_steps", "tree_edges", "digit_bits", "decoder_bits"]
    entries: int
    serialized_bits: int
    exact_terminals: int
    precision_terminals: int
    compilation_seconds: float


def _validate_state(
    state: _ControlState,
    prime: int,
    *,
    initial: Fraction | None = None,
) -> None:
    """Certify representation invariants without claiming task minimality."""

    _validate_prime(prime)
    if state.step < 0:
        raise _ArithmeticOrStateFailure("state step must be nonnegative")
    if state.lattice_vertex.prime != prime:
        raise _ArithmeticOrStateFailure("state and lattice use different primes")
    if state.complete_quotient not in state.visited_complete_quotients:
        raise _ArithmeticOrStateFailure(
            "visited-state witness omits the current complete quotient"
        )
    if len(state.visited_complete_quotients) != state.step + 1:
        raise _ArithmeticOrStateFailure(
            "a live state must contain one distinct quotient per prefix step"
        )
    if _determinant(state.prefix_matrix) != Fraction((-1) ** state.step):
        raise _ArithmeticOrStateFailure(
            "prefix determinant disagrees with matrix chronology"
        )
    if _matrix_lattice_vertex(state.prefix_matrix, prime) != state.lattice_vertex:
        raise _ArithmeticOrStateFailure(
            "cached lattice value disagrees with the prefix matrix"
        )

    if initial is not None and _matrix_affine(
        state.prefix_matrix,
        state.complete_quotient,
    ) != Fraction(initial):
        raise _ArithmeticOrStateFailure(
            "prefix matrix and complete quotient do not reconstruct the input"
        )


def _initial_state(value: Fraction, prime: int) -> _ControlState:
    _validate_prime(prime)
    value = Fraction(value)
    return _ControlState(
        0,
        value,
        _IDENTITY,
        _LatticeVertex(prime, 0, "root", 0),
        frozenset({value}),
    )


def _advance(
    task: _Task,
    state: _ControlState,
    action: Fraction,
    *,
    admitted_actions: tuple[Fraction, ...] | None = None,
) -> _Transition:
    """Apply the exact Phase-6 precedence without running optimization."""

    _validate_state(state, task.prime, initial=task.initial)
    action = Fraction(action)
    actions = admitted_actions
    if actions is None:
        actions = _admissible_actions(
            state.complete_quotient,
            task.prime,
            max_candidates=task.max_action_candidates,
        )
    if action not in actions:
        raise _InvalidActionGrammar("selected action is outside the frozen grammar")

    prefix_matrix = _matmul(state.prefix_matrix, _digit_matrix(action))
    if _determinant(prefix_matrix) != Fraction((-1) ** (state.step + 1)):
        raise _ArithmeticOrStateFailure(
            "transition matrix violates chronological determinant parity"
        )
    lattice_vertex = _matrix_lattice_vertex(prefix_matrix, task.prime)
    remainder = state.complete_quotient - action

    if remainder == 0:
        result = _Transition(
            "success_exact",
            action,
            prefix_matrix,
            lattice_vertex,
            None,
            None,
        )
        _decode_success(task, result)
        return result

    next_complete_quotient = 1 / remainder
    if lattice_vertex.depth >= task.precision:
        cylinder = lattice_vertex.ancestor_at_depth(task.precision)
        result = _Transition(
            "success_precision",
            action,
            prefix_matrix,
            lattice_vertex,
            next_complete_quotient,
            None,
            cylinder,
        )
        _decode_success(task, result)
        return result

    if next_complete_quotient in state.visited_complete_quotients:
        return _Transition(
            "cycle",
            action,
            prefix_matrix,
            lattice_vertex,
            next_complete_quotient,
            None,
            repeated_complete_quotient=next_complete_quotient,
        )

    if state.step + 1 == task.horizon:
        return _Transition(
            "horizon",
            action,
            prefix_matrix,
            lattice_vertex,
            next_complete_quotient,
            None,
        )

    next_state = _ControlState(
        state.step + 1,
        next_complete_quotient,
        prefix_matrix,
        lattice_vertex,
        state.visited_complete_quotients | {next_complete_quotient},
    )
    _validate_state(next_state, task.prime, initial=task.initial)
    return _Transition(
        "live",
        action,
        prefix_matrix,
        lattice_vertex,
        next_complete_quotient,
        next_state,
    )


def _decode_success(task: _Task, result: _Transition) -> Fraction | _LatticeVertex:
    """Run the policy-independent exact or fixed-precision decoder."""

    if result.outcome == "success_exact":
        denominator = result.prefix_matrix[1][0]
        if denominator == 0:
            raise _ArithmeticOrStateFailure(
                "exact decoder first column has zero denominator"
            )
        reconstructed = result.prefix_matrix[0][0] / denominator
        if reconstructed != task.initial:
            raise _ArithmeticOrStateFailure(
                "exact terminal first column does not reconstruct the input"
            )
        if result.next_complete_quotient is not None or result.cylinder is not None:
            raise _ArithmeticOrStateFailure(
                "exact terminal record contains precision-only decoder data"
            )
        return reconstructed

    if result.outcome == "success_precision":
        if result.next_complete_quotient is None or result.cylinder is None:
            raise _ArithmeticOrStateFailure(
                "precision terminal record omits decoder residuals"
            )
        if result.cylinder.depth != task.precision:
            raise _ArithmeticOrStateFailure(
                "terminal cylinder has the wrong declared precision"
            )
        if not result.cylinder.is_ancestor_of(result.lattice_vertex):
            raise _ArithmeticOrStateFailure(
                "terminal cylinder is not an ancestor of the lattice value"
            )
        if _matrix_affine(
            result.prefix_matrix,
            result.next_complete_quotient,
        ) != task.initial:
            raise _ArithmeticOrStateFailure(
                "precision decoder does not reconstruct the input"
            )
        return result.cylinder

    raise _ArithmeticOrStateFailure("decoder accepts only successful outcomes")


def _stage_cost(state: _ControlState, transition: _Transition) -> _Cost:
    return _Cost(
        digit_steps=1,
        tree_edges=_tree_distance(
            state.lattice_vertex,
            transition.lattice_vertex,
        ),
        digit_bits=_rational_bits(transition.action),
    )


def _terminal_decoder_cost(task: _Task, transition: _Transition) -> _Cost:
    _decode_success(task, transition)
    if transition.outcome == "success_exact":
        return _Cost(
            decoder_bits=(
                _rational_bits(transition.prefix_matrix[0][0])
                + _rational_bits(transition.prefix_matrix[1][0])
            )
        )
    if transition.outcome == "success_precision":
        assert transition.next_complete_quotient is not None
        frontier_size = (task.prime + 1) * task.prime ** (task.precision - 1)
        return _Cost(
            decoder_bits=(
                sum(
                    _rational_bits(entry)
                    for row in transition.prefix_matrix
                    for entry in row
                )
                + _rational_bits(transition.next_complete_quotient)
                + _minimum_exact_bits(frontier_size)
            )
        )
    raise _ArithmeticOrStateFailure("decoder cost needs a successful outcome")


def _dominates(left: _Cost, right: _Cost) -> bool:
    left_axes = (
        left.digit_steps,
        left.tree_edges,
        left.digit_bits,
        left.decoder_bits,
    )
    right_axes = (
        right.digit_steps,
        right.tree_edges,
        right.digit_bits,
        right.decoder_bits,
    )
    return all(a <= b for a, b in zip(left_axes, right_axes)) and any(
        a < b for a, b in zip(left_axes, right_axes)
    )


def _pareto_frontier(
    candidates: tuple[_ParetoValue, ...],
) -> tuple[_ParetoValue, ...]:
    """Keep distinct success modes but one deterministic witness per value."""

    unique: dict[
        tuple[Literal["success_exact", "success_precision"], _Cost],
        _ParetoValue,
    ] = {}
    for candidate in candidates:
        key = (candidate.outcome, candidate.cost)
        incumbent = unique.get(key)
        if incumbent is None or candidate.actions < incumbent.actions:
            unique[key] = candidate

    values = tuple(unique.values())
    frontier = tuple(
        value
        for value in values
        if not any(
            other != value and _dominates(other.cost, value.cost)
            for other in values
        )
    )
    return tuple(
        sorted(
            frontier,
            key=lambda value: (value.cost, value.outcome, value.actions),
        )
    )


def _replay_actions(task: _Task, actions: tuple[Fraction, ...]) -> _Transition:
    """Replay a supplied witness until it terminates or the witness ends."""

    state = _initial_state(task.initial, task.prime)
    result: _Transition | None = None
    for action in actions:
        result = _advance(task, state, action)
        if result.outcome != "live":
            return result
        assert result.next_state is not None
        state = result.next_state
    if result is None:
        raise _InvalidTaskParameter("a replay witness must contain an action")
    return result


def _replay_value(task: _Task, actions: tuple[Fraction, ...]) -> _ParetoValue:
    """Independently replay one successful policy witness and all four costs."""

    state = _initial_state(task.initial, task.prime)
    cost = _Cost()
    for index, action in enumerate(actions):
        transition = _advance(task, state, action)
        cost += _stage_cost(state, transition)
        if transition.outcome in ("success_exact", "success_precision"):
            if index + 1 != len(actions):
                raise _ArithmeticOrStateFailure(
                    "policy witness contains actions after task success"
                )
            cost += _terminal_decoder_cost(task, transition)
            return _ParetoValue(transition.outcome, cost, actions)
        if transition.outcome != "live" or transition.next_state is None:
            raise _ArithmeticOrStateFailure(
                "policy witness ended in a non-success outcome"
            )
        state = transition.next_state
    raise _ArithmeticOrStateFailure("policy witness ended before task success")


def _enumerate_reachable_graph(task: _Task) -> _GraphCensus:
    """Exhaust the exact live-state graph or return an explicit budget failure."""

    started = perf_counter()
    initial = _initial_state(task.initial, task.prime)
    frontier = [initial]
    seen = {initial.key}
    states_by_step = [1]
    enumerated_actions = 0
    maximum_coefficient_tuples = 0
    single_action_states = 0
    two_action_states = 0
    states_with_nonbaseline_action = 0
    outcome_counts = {
        "success_exact": 0,
        "success_precision": 0,
        "cycle": 0,
        "horizon": 0,
    }

    while frontier:
        state = frontier.pop()
        candidate_count = _coefficient_tuple_count(
            state.complete_quotient,
            task.prime,
        )
        maximum_coefficient_tuples = max(
            maximum_coefficient_tuples,
            candidate_count,
        )
        actions = _admissible_actions(
            state.complete_quotient,
            task.prime,
            max_candidates=task.max_action_candidates,
        )
        if len(actions) == 1:
            single_action_states += 1
        elif len(actions) == 2:
            two_action_states += 1
        else:
            raise _InvalidActionGrammar(
                "the frozen coefficient interval produced more than two values"
            )
        baseline_actions = {
            _padic_floor(state.complete_quotient, task.prime, selector)
            for selector in ("ruban", "browkin")
        }
        states_with_nonbaseline_action += bool(set(actions) - baseline_actions)
        enumerated_actions += len(actions)
        if enumerated_actions > task.max_transitions:
            raise _InconclusiveWithinResourceBudget(
                "reachable graph exceeded the transition budget"
            )

        for action in actions:
            transition = _advance(
                task,
                state,
                action,
                admitted_actions=actions,
            )
            if transition.outcome != "live":
                outcome_counts[transition.outcome] += 1
                continue

            if transition.next_state is None:
                raise _ArithmeticOrStateFailure(
                    "a live transition omitted its next state"
                )
            next_state = transition.next_state
            if next_state.key in seen:
                continue
            seen.add(next_state.key)
            if len(seen) > task.max_states:
                raise _InconclusiveWithinResourceBudget(
                    "reachable graph exceeded the state budget"
                )
            frontier.append(next_state)
            while len(states_by_step) <= next_state.step:
                states_by_step.append(0)
            states_by_step[next_state.step] += 1

    return _GraphCensus(
        states=len(seen),
        enumerated_actions=enumerated_actions,
        success_exact=outcome_counts["success_exact"],
        success_precision=outcome_counts["success_precision"],
        cycles=outcome_counts["cycle"],
        horizons=outcome_counts["horizon"],
        maximum_live_step=len(states_by_step) - 1,
        states_by_step=tuple(states_by_step),
        maximum_coefficient_tuples=maximum_coefficient_tuples,
        single_action_states=single_action_states,
        two_action_states=two_action_states,
        states_with_nonbaseline_action=states_with_nonbaseline_action,
        compilation_seconds=perf_counter() - started,
    )


def _solve_pareto_bellman(task: _Task) -> _BellmanResult:
    """Run exact set-valued Bellman recursion after the feasibility gate."""

    _enumerate_reachable_graph(task)
    started = perf_counter()
    memo: dict[tuple[object, ...], tuple[_ParetoValue, ...]] = {}
    candidate_values = 0

    def solve(state: _ControlState) -> tuple[_ParetoValue, ...]:
        nonlocal candidate_values
        cached = memo.get(state.key)
        if cached is not None:
            return cached

        actions = _admissible_actions(
            state.complete_quotient,
            task.prime,
            max_candidates=task.max_action_candidates,
        )
        candidates = []
        for action in actions:
            transition = _advance(
                task,
                state,
                action,
                admitted_actions=actions,
            )
            stage_cost = _stage_cost(state, transition)
            if transition.outcome in ("success_exact", "success_precision"):
                candidate_values += 1
                candidates.append(
                    _ParetoValue(
                        transition.outcome,
                        stage_cost + _terminal_decoder_cost(task, transition),
                        (action,),
                    )
                )
                continue
            if transition.outcome != "live":
                continue
            if transition.next_state is None:
                raise _ArithmeticOrStateFailure(
                    "a live Bellman edge omitted its next state"
                )
            for suffix in solve(transition.next_state):
                candidate_values += 1
                candidates.append(
                    _ParetoValue(
                        suffix.outcome,
                        stage_cost + suffix.cost,
                        (action,) + suffix.actions,
                    )
                )

        frontier = _pareto_frontier(tuple(candidates))
        memo[state.key] = frontier
        return frontier

    frontier = solve(_initial_state(task.initial, task.prime))
    if not frontier:
        raise _ArithmeticOrStateFailure(
            "the initial state has no successful Bellman value"
        )
    for value in frontier:
        if _replay_value(task, value.actions) != value:
            raise _ArithmeticOrStateFailure("Bellman witness replay disagrees")
    return _BellmanResult(
        frontier=frontier,
        solved_states=len(memo),
        stored_values=sum(len(values) for values in memo.values()),
        candidate_values=candidate_values,
        compilation_seconds=perf_counter() - started,
    )


def _run_baseline(task: _Task, selector: _Selector) -> _PolicyRun:
    """Replay one rule-defined baseline through the shared evaluator."""

    started = perf_counter()
    state = _initial_state(task.initial, task.prime)
    actions = []
    cost = _Cost()
    while True:
        action = _padic_floor(state.complete_quotient, task.prime, selector)
        transition = _advance(task, state, action)
        actions.append(action)
        cost += _stage_cost(state, transition)
        if transition.outcome in ("success_exact", "success_precision"):
            cost += _terminal_decoder_cost(task, transition)
            return _PolicyRun(
                transition.outcome,
                tuple(actions),
                cost,
                perf_counter() - started,
            )
        if transition.outcome in ("cycle", "horizon"):
            return _PolicyRun(
                transition.outcome,
                tuple(actions),
                None,
                perf_counter() - started,
            )
        if transition.next_state is None:
            raise _ArithmeticOrStateFailure(
                "a live baseline transition omitted its next state"
            )
        state = transition.next_state


def _baseline_relation(
    run: _PolicyRun,
    frontier: tuple[_ParetoValue, ...],
) -> Literal["equal", "dominated", "incomparable", "failure"]:
    if run.cost is None:
        return "failure"
    if any(
        value.outcome == run.outcome and value.cost == run.cost
        for value in frontier
    ):
        return "equal"
    if any(_dominates(value.cost, run.cost) for value in frontier):
        return "dominated"
    return "incomparable"


def _validate_source(
    values: tuple[Fraction, ...],
    weights: dict[Fraction, Fraction],
) -> None:
    if set(weights) != set(values):
        raise _InvalidTaskParameter("source support differs from the corpus")
    if any(weight <= 0 for weight in weights.values()):
        raise _InvalidTaskParameter("source weights must be positive")
    if sum(weights.values(), start=Fraction(0)) != 1:
        raise _InvalidTaskParameter("source weights must sum to one")


def _conditional_expected_cost(
    values: tuple[Fraction, ...],
    runs: tuple[_PolicyRun, ...],
    weights: dict[Fraction, Fraction],
    *,
    outcome: Literal["success_exact", "success_precision"] | None = None,
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction, Fraction]]:
    """Return success mass and exact conditional expectation by named axes."""

    if len(values) != len(runs):
        raise _InvalidTaskParameter("source values and policy runs differ in size")
    _validate_source(values, weights)
    selected = tuple(
        (weights[value], run.cost)
        for value, run in zip(values, runs)
        if run.cost is not None and (outcome is None or run.outcome == outcome)
    )
    mass = sum((weight for weight, _ in selected), start=Fraction(0))
    if mass == 0:
        raise _InvalidTaskParameter("conditional source event has zero mass")
    axes = ("digit_steps", "tree_edges", "digit_bits", "decoder_bits")
    expected = tuple(
        sum(
            (
                weight * getattr(cost, axis)
                for weight, cost in selected
                if cost is not None
            ),
            start=Fraction(0),
        )
        / mass
        for axis in axes
    )
    return mass, expected  # type: ignore[return-value]


def _choose_scalar_value(
    frontier: tuple[_ParetoValue, ...],
    axis: Literal["digit_steps", "tree_edges", "digit_bits", "decoder_bits"],
) -> _ParetoValue:
    if not frontier:
        raise _ArithmeticOrStateFailure("cannot scalarize an empty frontier")
    return min(
        frontier,
        key=lambda value: (
            getattr(value.cost, axis),
            value.cost,
            value.outcome,
            value.actions,
        ),
    )


def _uses_nonbaseline_action(task: _Task, value: _ParetoValue) -> bool:
    """Detect a local lift that neither named baseline selects at that state."""

    state = _initial_state(task.initial, task.prime)
    for action in value.actions:
        baseline_actions = {
            _padic_floor(state.complete_quotient, task.prime, selector)
            for selector in ("ruban", "browkin")
        }
        if action not in baseline_actions:
            return True
        transition = _advance(task, state, action)
        if transition.outcome != "live":
            break
        if transition.next_state is None:
            raise _ArithmeticOrStateFailure(
                "a live witness edge omitted its next state"
            )
        state = transition.next_state
    return False


def _state_action_serialized_bits(
    state: _ControlState,
    action: Fraction,
) -> int:
    """One declared exact table-layout proxy; not an online cost axis."""

    chart_bits = 2
    return (
        max(1, state.step.bit_length())
        + state.lattice_vertex.prime.bit_length()
        + _rational_bits(state.complete_quotient)
        + sum(
            _rational_bits(entry)
            for row in state.prefix_matrix
            for entry in row
        )
        + max(1, state.lattice_vertex.depth.bit_length())
        + chart_bits
        + max(1, state.lattice_vertex.coordinate.bit_length())
        + max(1, len(state.visited_complete_quotients).bit_length())
        + sum(
            _rational_bits(value)
            for value in sorted(state.visited_complete_quotients)
        )
        + _rational_bits(action)
    )


def _compile_scalar_policy_table(
    prime: int,
    values: tuple[Fraction, ...],
    results: tuple[_BellmanResult, ...],
    axis: Literal["digit_steps", "tree_edges", "digit_bits", "decoder_bits"],
) -> _PolicyTableLedger:
    """Compile one corpus controller and charge its exact retained state keys."""

    if len(values) != len(results):
        raise _InvalidTaskParameter("Bellman results do not cover the corpus")
    started = perf_counter()
    table: dict[tuple[object, ...], tuple[_ControlState, Fraction]] = {}
    exact_terminals = 0
    precision_terminals = 0
    for initial, result in zip(values, results):
        task = _Task(prime, initial)
        value = _choose_scalar_value(result.frontier, axis)
        exact_terminals += value.outcome == "success_exact"
        precision_terminals += value.outcome == "success_precision"
        state = _initial_state(initial, prime)
        for action in value.actions:
            incumbent = table.get(state.key)
            if incumbent is not None and incumbent[1] != action:
                raise _ArithmeticOrStateFailure(
                    "scalar controller assigns two actions to one exact state"
                )
            table[state.key] = (state, action)
            transition = _advance(task, state, action)
            if transition.outcome != "live":
                break
            if transition.next_state is None:
                raise _ArithmeticOrStateFailure(
                    "compiled live policy edge omitted its next state"
                )
            state = transition.next_state

    return _PolicyTableLedger(
        axis,
        entries=len(table),
        serialized_bits=sum(
            _state_action_serialized_bits(state, action)
            for state, action in table.values()
        ),
        exact_terminals=exact_terminals,
        precision_terminals=precision_terminals,
        compilation_seconds=perf_counter() - started,
    )


def _baseline_complete_quotients(
    value: Fraction,
    prime: int,
    selector: _Selector,
    *,
    horizon: int,
) -> tuple[Fraction, ...]:
    """Materialize only the tiny baseline states needed by Gate 6A."""

    if horizon <= 0:
        raise _InvalidTaskParameter("horizon must be positive")
    state = Fraction(value)
    visited = set()
    states = []
    for _ in range(horizon):
        if state in visited:
            break
        visited.add(state)
        states.append(state)
        action = _padic_floor(state, prime, selector)
        remainder = state - action
        if remainder == 0:
            break
        state = 1 / remainder
    return tuple(states)


def _certify_baseline_inclusion(
    value: Fraction,
    prime: int,
    *,
    admitted_actions: tuple[Fraction, ...] | None = None,
) -> None:
    actions = (
        _admissible_actions(value, prime)
        if admitted_actions is None
        else admitted_actions
    )
    for selector in ("ruban", "browkin"):
        baseline_action = _padic_floor(value, prime, selector)
        if baseline_action not in actions:
            raise _InvalidActionGrammar(
                f"{selector} action {baseline_action} is outside the grammar"
            )


@pytest.fixture(scope="module")
def _frozen_values() -> tuple[Fraction, ...]:
    values = tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, 13)
                for numerator in range(-12, 13)
                if numerator != 0 and gcd(abs(numerator), denominator) == 1
            }
        )
    )
    assert len(values) == 182
    return values


@pytest.fixture(scope="module")
def _frozen_bellman_results(
    _frozen_values: tuple[Fraction, ...],
) -> dict[int, tuple[_BellmanResult, ...]]:
    return {
        prime: tuple(
            _solve_pareto_bellman(_Task(prime, value))
            for value in _frozen_values
        )
        for prime in (3, 5, 7)
    }


def test_action_grammar_is_exact_finite_and_quotients_syntactic_duplicates():
    raw = _raw_admissible_actions(
        Fraction(-1, 9),
        3,
        max_candidates=1_000,
    )
    actions = _admissible_actions(Fraction(-1, 9), 3)

    assert raw == (
        Fraction(-1, 9),
        Fraction(-1, 9),
        Fraction(-1, 9),
        Fraction(26, 9),
    )
    assert actions == (Fraction(-1, 9), Fraction(26, 9))
    assert len(actions) == len(set(actions))
    assert all(
        Fraction(-1, 9) == action
        or _valuation(Fraction(-1, 9) - action, 3) >= 1
        for action in actions
    )

    assert _admissible_actions(Fraction(0), 5) == (Fraction(0),)
    assert _admissible_actions(Fraction(5), 5) == (Fraction(0),)


def test_frozen_grammar_contains_both_baselines_on_tiny_reachable_corpus():
    tiny_inputs = (Fraction(-1), Fraction(3), Fraction(2, 7))
    for prime in (3, 5, 7):
        reached = set(tiny_inputs)
        for value in tiny_inputs:
            for selector in ("ruban", "browkin"):
                reached.update(
                    _baseline_complete_quotients(
                        value,
                        prime,
                        selector,
                        horizon=4,
                    )
                )

        for complete_quotient in sorted(reached):
            _certify_baseline_inclusion(complete_quotient, prime)
            actions = _admissible_actions(complete_quotient, prime)
            assert actions == tuple(sorted(set(actions)))
            assert all(
                complete_quotient == action
                or _valuation(complete_quotient - action, prime) >= 1
                for action in actions
            )


def test_state_key_retains_every_frozen_semantic_and_decoder_field():
    state = _initial_state(Fraction(-1), 5)
    _validate_state(state, 5)
    assert state.key == _initial_state(Fraction(-1), 5).key
    assert hash(state.key) == hash(_initial_state(Fraction(-1), 5).key)

    same_set_different_order = replace(
        state,
        step=1,
        prefix_matrix=_digit_matrix(Fraction(4)),
        lattice_vertex=_matrix_lattice_vertex(_digit_matrix(Fraction(4)), 5),
        complete_quotient=Fraction(-1, 5),
        visited_complete_quotients=frozenset((Fraction(-1, 5), Fraction(-1))),
    )
    reordered = replace(
        same_set_different_order,
        visited_complete_quotients=frozenset((Fraction(-1), Fraction(-1, 5))),
    )
    _validate_state(same_set_different_order, 5)
    assert same_set_different_order.key == reordered.key

    variants = (
        replace(state, step=1),
        replace(state, complete_quotient=Fraction(4)),
        replace(state, prefix_matrix=_digit_matrix(Fraction(-1))),
        replace(state, lattice_vertex=_LatticeVertex(5, 1, "affine", 0)),
        replace(
            state,
            visited_complete_quotients=frozenset(
                {Fraction(-1), Fraction(-1, 5)}
            ),
        ),
    )
    assert all(variant.key != state.key for variant in variants)

    same_contact = _initial_state(Fraction(4), 5)
    assert same_contact.lattice_vertex == state.lattice_vertex
    assert same_contact.key != state.key


def test_gate6a_failure_semantics_are_explicit_and_nonoptimizing():
    with pytest.raises(_InvalidTaskParameter, match="odd prime"):
        _admissible_actions(Fraction(1), 2)
    with pytest.raises(_InvalidTaskParameter, match="must be prime"):
        _admissible_actions(Fraction(1), 9)
    with pytest.raises(_InvalidTaskParameter, match="positive"):
        _admissible_actions(Fraction(1), 3, max_candidates=0)
    with pytest.raises(_InconclusiveWithinResourceBudget, match="above budget"):
        _admissible_actions(Fraction(-1, 9), 3, max_candidates=100)

    with pytest.raises(_InvalidActionGrammar, match="outside the grammar"):
        _certify_baseline_inclusion(
            Fraction(-1),
            5,
            admitted_actions=(Fraction(4),),
        )

    valid = _initial_state(Fraction(-1), 5)
    malformed_states = (
        replace(valid, step=-1),
        replace(valid, complete_quotient=Fraction(1)),
        replace(valid, step=1),
        replace(valid, prefix_matrix=((Fraction(1), Fraction(0)),) * 2),
        replace(valid, lattice_vertex=_LatticeVertex(5, 1, "affine", 0)),
    )
    for malformed in malformed_states:
        with pytest.raises(_ArithmeticOrStateFailure):
            _validate_state(malformed, 5)


def test_gate6b_exact_and_precision_decoders_share_one_transition_contract():
    exact_task = _Task(5, Fraction(-1))
    exact = _replay_actions(exact_task, (Fraction(-1),))
    assert exact.outcome == "success_exact"
    assert exact.lattice_vertex == _LatticeVertex(5, 0, "root", 0)
    assert _decode_success(exact_task, exact) == Fraction(-1)

    precision_task = _Task(3, Fraction(-12))
    precision = _replay_actions(
        precision_task,
        (Fraction(0), Fraction(2, 3), Fraction(5, 3)),
    )
    assert precision.outcome == "success_precision"
    assert precision.lattice_vertex.depth == 4
    assert precision.cylinder == precision.lattice_vertex
    assert precision.next_complete_quotient == Fraction(-1, 3)
    assert _decode_success(precision_task, precision) == precision.cylinder


def test_gate6b_outcome_precedence_keeps_success_cycle_and_horizon_distinct():
    precision_before_cycle = _Task(5, Fraction(-1), precision=2, horizon=16)
    success = _replay_actions(
        precision_before_cycle,
        (Fraction(4), Fraction(24, 5)),
    )
    assert success.outcome == "success_precision"
    assert success.next_complete_quotient == Fraction(-1, 5)

    frozen_precision = _Task(5, Fraction(-1), precision=4, horizon=16)
    cycle = _replay_actions(
        frozen_precision,
        (Fraction(4), Fraction(24, 5)),
    )
    assert cycle.outcome == "cycle"
    assert cycle.repeated_complete_quotient == Fraction(-1, 5)
    with pytest.raises(_ArithmeticOrStateFailure, match="successful"):
        _decode_success(frozen_precision, cycle)

    one_step = _Task(5, Fraction(-1), precision=4, horizon=1)
    horizon = _replay_actions(one_step, (Fraction(4),))
    assert horizon.outcome == "horizon"
    assert horizon.repeated_complete_quotient is None


def test_gate6b_rejects_inadmissible_actions_and_tampered_decoders():
    task = _Task(5, Fraction(-1))
    initial = _initial_state(task.initial, task.prime)
    with pytest.raises(_InvalidActionGrammar, match="outside"):
        _advance(task, initial, Fraction(0))

    exact = _replay_actions(task, (Fraction(-1),))
    bad_exact = replace(
        exact,
        prefix_matrix=(
            (Fraction(1), Fraction(1)),
            (Fraction(1), Fraction(0)),
        ),
    )
    with pytest.raises(_ArithmeticOrStateFailure, match="reconstruct"):
        _decode_success(task, bad_exact)

    precision_task = _Task(3, Fraction(-12))
    precision = _replay_actions(
        precision_task,
        (Fraction(0), Fraction(2, 3), Fraction(5, 3)),
    )
    assert precision.cylinder is not None
    bad_cylinder = replace(
        precision,
        cylinder=precision.cylinder.parent,
    )
    with pytest.raises(_ArithmeticOrStateFailure, match="wrong declared"):
        _decode_success(precision_task, bad_cylinder)

    bad_residual = replace(
        precision,
        next_complete_quotient=Fraction(-2, 3),
    )
    with pytest.raises(_ArithmeticOrStateFailure, match="reconstruct"):
        _decode_success(precision_task, bad_residual)


def test_gate6c_frozen_reachable_graph_is_exactly_exhaustible(
    _frozen_values: tuple[Fraction, ...],
):
    expected = {
        3: {
            "states": 682,
            "actions": 1316,
            "success_exact": 370,
            "success_precision": 434,
            "cycles": 12,
            "max_candidates": 625,
            "single_action_states": 48,
            "two_action_states": 634,
            "nonbaseline_action_states": 317,
        },
        5: {
            "states": 838,
            "actions": 1646,
            "success_exact": 448,
            "success_precision": 522,
            "cycles": 20,
            "max_candidates": 729,
            "single_action_states": 30,
            "two_action_states": 808,
            "nonbaseline_action_states": 404,
        },
        7: {
            "states": 880,
            "actions": 1738,
            "success_exact": 450,
            "success_precision": 564,
            "cycles": 26,
            "max_candidates": 2197,
            "single_action_states": 22,
            "two_action_states": 858,
            "nonbaseline_action_states": 429,
        },
    }

    for prime in (3, 5, 7):
        censuses = tuple(
            _enumerate_reachable_graph(_Task(prime, value))
            for value in _frozen_values
        )
        observed = {
            "states": sum(census.states for census in censuses),
            "actions": sum(census.enumerated_actions for census in censuses),
            "success_exact": sum(census.success_exact for census in censuses),
            "success_precision": sum(
                census.success_precision for census in censuses
            ),
            "cycles": sum(census.cycles for census in censuses),
            "max_candidates": max(
                census.maximum_coefficient_tuples for census in censuses
            ),
            "single_action_states": sum(
                census.single_action_states for census in censuses
            ),
            "two_action_states": sum(
                census.two_action_states for census in censuses
            ),
            "nonbaseline_action_states": sum(
                census.states_with_nonbaseline_action for census in censuses
            ),
        }
        assert observed == expected[prime]
        assert max(census.states for census in censuses) == 7
        assert max(census.enumerated_actions for census in censuses) == 14
        assert max(census.maximum_live_step for census in censuses) == 2
        assert sum(census.horizons for census in censuses) == 0


def test_gate6c_resource_exhaustion_is_inconclusive_not_a_negative_result():
    with pytest.raises(_InconclusiveWithinResourceBudget, match="state budget"):
        _enumerate_reachable_graph(
            _Task(5, Fraction(-12), max_states=1)
        )
    with pytest.raises(
        _InconclusiveWithinResourceBudget,
        match="transition budget",
    ):
        _enumerate_reachable_graph(
            _Task(5, Fraction(-12), max_transitions=1)
        )


def test_gate6d_hand_checkable_bellman_frontier_and_witness_replay():
    task = _Task(5, Fraction(-1))
    result = _solve_pareto_bellman(task)
    assert result.frontier == (
        _ParetoValue(
            "success_exact",
            _Cost(
                digit_steps=1,
                tree_edges=0,
                digit_bits=2,
                decoder_bits=4,
            ),
            (Fraction(-1),),
        ),
    )
    assert result.solved_states == 2
    assert result.stored_values == 2
    assert _replay_value(task, result.frontier[0].actions) == result.frontier[0]


def test_gate6d_full_frozen_workload_returns_replayable_pareto_values(
    _frozen_values: tuple[Fraction, ...],
    _frozen_bellman_results: dict[int, tuple[_BellmanResult, ...]],
):
    expected = {
        3: {
            "frontier_values": 202,
            "maximum_frontier": 3,
            "solved_states": 682,
            "stored_values": 758,
            "candidate_values": 1360,
            "exact_values": 186,
            "precision_values": 16,
            "nonbaseline_values": 43,
        },
        5: {
            "frontier_values": 182,
            "maximum_frontier": 1,
            "solved_states": 838,
            "stored_values": 850,
            "candidate_values": 1638,
            "exact_values": 182,
            "precision_values": 0,
            "nonbaseline_values": 28,
        },
        7: {
            "frontier_values": 182,
            "maximum_frontier": 1,
            "solved_states": 880,
            "stored_values": 882,
            "candidate_values": 1714,
            "exact_values": 182,
            "precision_values": 0,
            "nonbaseline_values": 24,
        },
    }

    for prime in (3, 5, 7):
        results = _frozen_bellman_results[prime]
        all_values = tuple(
            frontier_value
            for result in results
            for frontier_value in result.frontier
        )
        observed = {
            "frontier_values": len(all_values),
            "maximum_frontier": max(len(result.frontier) for result in results),
            "solved_states": sum(result.solved_states for result in results),
            "stored_values": sum(result.stored_values for result in results),
            "candidate_values": sum(
                result.candidate_values for result in results
            ),
            "exact_values": sum(
                value.outcome == "success_exact" for value in all_values
            ),
            "precision_values": sum(
                value.outcome == "success_precision" for value in all_values
            ),
            "nonbaseline_values": sum(
                _uses_nonbaseline_action(_Task(prime, initial), frontier_value)
                for initial, result in zip(_frozen_values, results)
                for frontier_value in result.frontier
            ),
        }
        assert observed == expected[prime]
        assert all(
            _replay_value(_Task(prime, initial), frontier_value.actions)
            == frontier_value
            for initial, result in zip(_frozen_values, results)
            for frontier_value in result.frontier
        )

    p3_example = _solve_pareto_bellman(_Task(3, Fraction(-10, 11)))
    assert len(p3_example.frontier) == 3
    assert {
        value.outcome for value in p3_example.frontier
    } == {"success_exact", "success_precision"}
    assert not any(
        _dominates(left.cost, right.cost)
        for left in p3_example.frontier
        for right in p3_example.frontier
        if left != right
    )


def test_gate6e_fixed_baselines_use_the_shared_contract_and_frontier(
    _frozen_values: tuple[Fraction, ...],
    _frozen_bellman_results: dict[int, tuple[_BellmanResult, ...]],
):
    expected_outcomes = {
        (3, "ruban"): {
            "success_exact": 48,
            "success_precision": 130,
            "cycle": 4,
        },
        (3, "browkin"): {
            "success_exact": 168,
            "success_precision": 14,
        },
        (5, "ruban"): {
            "success_exact": 36,
            "success_precision": 140,
            "cycle": 6,
        },
        (5, "browkin"): {
            "success_exact": 180,
            "success_precision": 2,
        },
        (7, "ruban"): {
            "success_exact": 38,
            "success_precision": 136,
            "cycle": 8,
        },
        (7, "browkin"): {
            "success_exact": 176,
            "success_precision": 6,
        },
    }
    expected_relations = {
        (3, "ruban"): {"equal": 54, "dominated": 124, "failure": 4},
        (3, "browkin"): {"equal": 126, "dominated": 56},
        (5, "ruban"): {"equal": 36, "dominated": 140, "failure": 6},
        (5, "browkin"): {"equal": 144, "dominated": 38},
        (7, "ruban"): {"equal": 38, "dominated": 136, "failure": 8},
        (7, "browkin"): {"equal": 144, "dominated": 38},
    }

    for prime in (3, 5, 7):
        for selector in ("ruban", "browkin"):
            runs = tuple(
                _run_baseline(_Task(prime, value), selector)
                for value in _frozen_values
            )
            outcomes = dict(Counter(run.outcome for run in runs))
            relations = dict(
                Counter(
                    _baseline_relation(run, result.frontier)
                    for run, result in zip(
                        runs,
                        _frozen_bellman_results[prime],
                    )
                )
            )
            assert outcomes == expected_outcomes[(prime, selector)]
            assert relations == expected_relations[(prime, selector)]
            assert "horizon" not in outcomes
            assert "incomparable" not in relations

    ruban_negative = _run_baseline(_Task(5, Fraction(-1)), "ruban")
    browkin_negative = _run_baseline(_Task(5, Fraction(-1)), "browkin")
    assert ruban_negative.outcome == "cycle"
    assert browkin_negative.outcome == "success_exact"

    ruban_three = _run_baseline(_Task(5, Fraction(3)), "ruban")
    browkin_three = _run_baseline(_Task(5, Fraction(3)), "browkin")
    assert ruban_three.cost == _Cost(1, 0, 3, 5)
    assert browkin_three.cost == _Cost(2, 2, 7, 9)
    assert _dominates(ruban_three.cost, browkin_three.cost)


def test_gate6e_source_and_scalar_choices_change_the_selected_economy(
    _frozen_values: tuple[Fraction, ...],
    _frozen_bellman_results: dict[int, tuple[_BellmanResult, ...]],
):
    prime = 5
    runs = {
        selector: tuple(
            _run_baseline(_Task(prime, value), selector)
            for value in _frozen_values
        )
        for selector in ("ruban", "browkin")
    }
    uniform = {
        value: Fraction(1, len(_frozen_values))
        for value in _frozen_values
    }
    skewed = {
        value: Fraction(1, 2 * (len(_frozen_values) - 1))
        for value in _frozen_values
    }
    skewed[Fraction(3)] = Fraction(1, 2)

    uniform_ruban = _conditional_expected_cost(
        _frozen_values,
        runs["ruban"],
        uniform,
    )
    uniform_browkin = _conditional_expected_cost(
        _frozen_values,
        runs["browkin"],
        uniform,
    )
    skewed_ruban = _conditional_expected_cost(
        _frozen_values,
        runs["ruban"],
        skewed,
    )
    skewed_browkin = _conditional_expected_cost(
        _frozen_values,
        runs["browkin"],
        skewed,
    )
    assert uniform_ruban == (
        Fraction(88, 91),
        (
            Fraction(221, 88),
            Fraction(315, 88),
            Fraction(1321, 88),
            Fraction(7789, 176),
        ),
    )
    assert uniform_browkin == (
        Fraction(1),
        (
            Fraction(29, 13),
            Fraction(264, 91),
            Fraction(135, 13),
            Fraction(1165, 91),
        ),
    )
    assert skewed_ruban == (
        Fraction(178, 181),
        (
            Fraction(311, 178),
            Fraction(315, 178),
            Fraction(1591, 178),
            Fraction(8689, 356),
        ),
    )
    assert skewed_browkin == (
        Fraction(1),
        (
            Fraction(383, 181),
            Fraction(444, 181),
            Fraction(1575, 181),
            Fraction(1975, 181),
        ),
    )
    assert uniform_browkin[1][0] < uniform_ruban[1][0]
    assert skewed_ruban[1][0] < skewed_browkin[1][0]
    assert uniform_browkin[1][1] < uniform_ruban[1][1]
    assert skewed_ruban[1][1] < skewed_browkin[1][1]
    assert uniform_ruban[0] < uniform_browkin[0]
    assert skewed_ruban[0] < skewed_browkin[0]

    p3_results = _frozen_bellman_results[3]
    assert sum(
        _choose_scalar_value(result.frontier, "digit_steps")
        != _choose_scalar_value(result.frontier, "decoder_bits")
        for result in p3_results
    ) == 12
    digit_table = _compile_scalar_policy_table(
        3,
        _frozen_values,
        p3_results,
        "digit_steps",
    )
    decoder_table = _compile_scalar_policy_table(
        3,
        _frozen_values,
        p3_results,
        "decoder_bits",
    )
    assert digit_table.entries == 364
    assert digit_table.serialized_bits == 13264
    assert (digit_table.exact_terminals, digit_table.precision_terminals) == (
        174,
        8,
    )
    assert decoder_table.entries == 372
    assert decoder_table.serialized_bits == 13611
    assert (decoder_table.exact_terminals, decoder_table.precision_terminals) == (
        182,
        0,
    )


def test_gate6e_residual_payload_and_backtracking_red_teams():
    task = _Task(5, Fraction(-1))
    same_contact_actions = _admissible_actions(Fraction(-1), 5)
    assert same_contact_actions == (Fraction(-1), Fraction(4))
    exact = _advance(
        task,
        _initial_state(task.initial, task.prime),
        Fraction(-1),
    )
    continued = _advance(
        task,
        _initial_state(task.initial, task.prime),
        Fraction(4),
    )
    assert exact.outcome == "success_exact"
    assert continued.outcome == "live"
    assert continued.next_complete_quotient == Fraction(-1, 5)

    stabilizer = (
        (Fraction(6), Fraction(1)),
        (Fraction(-25), Fraction(-4)),
    )
    alpha = Fraction(-1, 5)
    assert _matrix_affine(stabilizer, alpha) == alpha
    assert _matrix_lattice_vertex(stabilizer, 5) == _matrix_lattice_vertex(
        _IDENTITY,
        5,
    )
    visited = frozenset({alpha, Fraction(2), Fraction(3)})
    plain_state = _ControlState(
        2,
        alpha,
        _IDENTITY,
        _LatticeVertex(5, 0, "root", 0),
        visited,
    )
    loaded_state = replace(plain_state, prefix_matrix=stabilizer)
    precision_task = _Task(5, alpha, precision=2)
    plain_terminal = _advance(precision_task, plain_state, Fraction(24, 5))
    loaded_terminal = _advance(precision_task, loaded_state, Fraction(24, 5))
    assert plain_terminal.outcome == loaded_terminal.outcome == "success_precision"
    assert plain_terminal.lattice_vertex == loaded_terminal.lattice_vertex
    assert _terminal_decoder_cost(
        precision_task,
        plain_terminal,
    ) != _terminal_decoder_cost(precision_task, loaded_terminal)

    cycle_witness = frozenset(
        {Fraction(-1), Fraction(-1, 5), Fraction(2)}
    )
    no_cycle_witness = frozenset({Fraction(-1), Fraction(2), Fraction(3)})
    cycle_state = _ControlState(
        2,
        Fraction(-1),
        _IDENTITY,
        _LatticeVertex(5, 0, "root", 0),
        cycle_witness,
    )
    no_cycle_state = replace(
        cycle_state,
        visited_complete_quotients=no_cycle_witness,
    )
    cycle_result = _advance(task, cycle_state, Fraction(4))
    live_result = _advance(task, no_cycle_state, Fraction(4))
    assert cycle_result.outcome == "cycle"
    assert live_result.outcome == "live"

    for state in (plain_state, loaded_state, cycle_state, no_cycle_state):
        assert _matrix_affine_preimage(
            state.prefix_matrix,
            _matrix_affine(state.prefix_matrix, state.complete_quotient),
        ) == state.complete_quotient

    root = _LatticeVertex(3, 0, "root", 0)
    left = _LatticeVertex(3, 2, "affine", 1)
    right = _LatticeVertex(3, 2, "affine", 4)
    traveled = _tree_distance(root, left) + _tree_distance(left, right)
    net = _tree_distance(root, right)
    assert (traveled, net, (traveled - net) // 2) == (4, 2, 1)
