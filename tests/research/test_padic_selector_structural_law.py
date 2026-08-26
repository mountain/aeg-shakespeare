"""Phase 7: a binary normal form for the finite p-adic lift grammar.

Phase 6 deliberately enumerated the coefficient grammar before quotienting
syntactic collisions.  That was the right audit order, but its census exposed
a sharper arithmetic structure: every semantic action is either the Ruban
contact representative ``r`` or the translated lift ``r - p``.  This
executable essay certifies that normal form, replays the complete Phase 6 task
through it, and then asks a different question:

    does the scalar-optimal lift bit descend through contact, evaluated
    geometry, or locally visible cost data?

The answer is exact and negative on every declared workload.  Equal local
signatures can retain different sets of optimal first bits, so the binary
alphabet does not make the controller a local geometric rule.  Complete-
quotient history and decoder residuals still matter through continuation.

The stress workloads move the stopping surface from depth four to depths six
and eight, add the previously unseen primes 11 and 13, and reserve
``X_18 - X_12`` as an input holdout.  All arithmetic remains over ``Fraction``;
the implementation imports the Phase 6 research owner by path and creates no
package API.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import importlib.util
from itertools import product
from math import gcd
from pathlib import Path
import sys
from time import perf_counter
from typing import Literal

import pytest


_PHASE6_PATH = Path(__file__).with_name(
    "test_padic_selector_policy_bellman.py"
)
_SPEC = importlib.util.spec_from_file_location(
    "_phase6_padic_selector_policy_bellman",
    _PHASE6_PATH,
)
assert _SPEC is not None and _SPEC.loader is not None
_PHASE6 = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _PHASE6
_SPEC.loader.exec_module(_PHASE6)


_Axis = Literal["digit_steps", "decoder_bits"]
_SignatureLevel = Literal[0, 1, 2]


@dataclass(frozen=True)
class _StructuralSolution:
    """All successful state values, not only the initial frontier."""

    frontier: tuple[object, ...]
    state_values: tuple[tuple[object, tuple[object, ...]], ...]
    candidate_values: int
    compilation_seconds: float


@dataclass(frozen=True)
class _WorkloadRecord:
    task: object
    census: object
    solution: _StructuralSolution


@dataclass(frozen=True)
class _Aggregate:
    inputs: int
    states: int
    actions: int
    exact_edges: int
    precision_edges: int
    cycles: int
    horizons: int
    maximum_states: int
    maximum_actions: int
    maximum_live_step: int
    frontier_records: int
    maximum_frontier: int
    exact_frontiers: int
    precision_frontiers: int


@dataclass(frozen=True)
class _SignatureAudit:
    records: int
    groups: int
    collisions: int
    digit_collisions: int
    decoder_collisions: int
    disjoint_collisions: int
    witness: tuple[object, ...] | None


@dataclass(frozen=True)
class _BinaryPolicyLedger:
    prime: int
    axis: _Axis
    entries: int
    state_bits: int
    rational_action_bits: int
    choice_bits: int
    normal_form_metadata_bits: int
    rational_table_bits: int
    binary_table_bits: int


def _corpus(bound: int) -> tuple[Fraction, ...]:
    if bound <= 0:
        raise _PHASE6._InvalidTaskParameter("corpus bound must be positive")
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, bound + 1)
                for numerator in range(-bound, bound + 1)
                if numerator != 0 and gcd(abs(numerator), denominator) == 1
            }
        )
    )


def _closed_admissible_actions(
    value: Fraction,
    prime: int,
    *,
    max_candidates: int = 100_000,
) -> tuple[Fraction, ...]:
    """Evaluate the candidate normal form without coefficient enumeration."""

    _PHASE6._validate_prime(prime)
    if max_candidates <= 0:
        raise _PHASE6._InvalidTaskParameter("max_candidates must be positive")
    value = Fraction(value)
    if value == 0:
        return (Fraction(0),)

    first_exponent = min(_PHASE6._valuation(value, prime), 0)
    grid_unit = _PHASE6._prime_power(prime, first_exponent)
    ruban = _PHASE6._padic_floor(value, prime, "ruban")
    actions = [ruban]
    if ruban >= grid_unit:
        actions.append(ruban - prime)
    return tuple(sorted(actions))


def _lift_bit(value: Fraction, prime: int, action: Fraction) -> int:
    """Decode one admitted action as ``r - epsilon p``."""

    ruban = _PHASE6._padic_floor(value, prime, "ruban")
    if action == ruban:
        return 0
    if action == ruban - prime:
        return 1
    raise _PHASE6._InvalidActionGrammar(
        "action has no Ruban-reference lift-bit representation"
    )


def _coefficient_image(prime: int, first_exponent: int) -> set[Fraction]:
    """Materialize a bounded raw coefficient image for the proof red team."""

    exponents = tuple(range(first_exponent, 1))
    coefficients = range(-(prime - 1), prime)
    return {
        sum(
            (
                Fraction(coefficient)
                * _PHASE6._prime_power(prime, exponent)
                for coefficient, exponent in zip(values, exponents)
            ),
            start=Fraction(0),
        )
        for values in product(coefficients, repeat=len(exponents))
    }


def _enumerate_closed_graph(task: object) -> tuple[object, tuple[object, ...]]:
    """Exhaust live states with the closed action evaluator and frozen budgets."""

    started = perf_counter()
    initial = _PHASE6._initial_state(task.initial, task.prime)
    frontier = [initial]
    states = {initial.key: initial}
    states_by_step = [1]
    enumerated_actions = 0
    maximum_coefficient_tuples = 0
    single_action_states = 0
    two_action_states = 0
    states_with_nonbaseline_action = 0
    outcomes = {
        "success_exact": 0,
        "success_precision": 0,
        "cycle": 0,
        "horizon": 0,
    }

    while frontier:
        state = frontier.pop()
        maximum_coefficient_tuples = max(
            maximum_coefficient_tuples,
            _PHASE6._coefficient_tuple_count(
                state.complete_quotient,
                task.prime,
            ),
        )
        actions = _closed_admissible_actions(
            state.complete_quotient,
            task.prime,
        )
        if len(actions) == 1:
            single_action_states += 1
        elif len(actions) == 2:
            two_action_states += 1
        else:
            raise _PHASE6._InvalidActionGrammar(
                "closed action normal form is not binary"
            )

        baseline_actions = {
            _PHASE6._padic_floor(
                state.complete_quotient,
                task.prime,
                selector,
            )
            for selector in ("ruban", "browkin")
        }
        if not baseline_actions <= set(actions):
            raise _PHASE6._InvalidActionGrammar(
                "closed action normal form omits a baseline"
            )
        states_with_nonbaseline_action += bool(set(actions) - baseline_actions)
        enumerated_actions += len(actions)
        if enumerated_actions > task.max_transitions:
            raise _PHASE6._InconclusiveWithinResourceBudget(
                "closed graph exceeded the transition budget"
            )

        for action in actions:
            transition = _PHASE6._advance(
                task,
                state,
                action,
                admitted_actions=actions,
            )
            if transition.outcome != "live":
                outcomes[transition.outcome] += 1
                continue
            if transition.next_state is None:
                raise _PHASE6._ArithmeticOrStateFailure(
                    "live closed transition omitted its state"
                )
            next_state = transition.next_state
            if next_state.key in states:
                continue
            states[next_state.key] = next_state
            if len(states) > task.max_states:
                raise _PHASE6._InconclusiveWithinResourceBudget(
                    "closed graph exceeded the state budget"
                )
            frontier.append(next_state)
            while len(states_by_step) <= next_state.step:
                states_by_step.append(0)
            states_by_step[next_state.step] += 1

    census = _PHASE6._GraphCensus(
        states=len(states),
        enumerated_actions=enumerated_actions,
        success_exact=outcomes["success_exact"],
        success_precision=outcomes["success_precision"],
        cycles=outcomes["cycle"],
        horizons=outcomes["horizon"],
        maximum_live_step=len(states_by_step) - 1,
        states_by_step=tuple(states_by_step),
        maximum_coefficient_tuples=maximum_coefficient_tuples,
        single_action_states=single_action_states,
        two_action_states=two_action_states,
        states_with_nonbaseline_action=states_with_nonbaseline_action,
        compilation_seconds=perf_counter() - started,
    )
    return census, tuple(states.values())


def _replay_closed_value(task: object, value: object) -> object:
    state = _PHASE6._initial_state(task.initial, task.prime)
    cost = _PHASE6._Cost()
    for index, action in enumerate(value.actions):
        actions = _closed_admissible_actions(
            state.complete_quotient,
            task.prime,
        )
        transition = _PHASE6._advance(
            task,
            state,
            action,
            admitted_actions=actions,
        )
        cost += _PHASE6._stage_cost(state, transition)
        if transition.outcome in ("success_exact", "success_precision"):
            if index + 1 != len(value.actions):
                raise _PHASE6._ArithmeticOrStateFailure(
                    "closed witness continued after task success"
                )
            cost += _PHASE6._terminal_decoder_cost(task, transition)
            return _PHASE6._ParetoValue(
                transition.outcome,
                cost,
                value.actions,
            )
        if transition.outcome != "live" or transition.next_state is None:
            raise _PHASE6._ArithmeticOrStateFailure(
                "closed witness reached a nonsuccess terminal"
            )
        state = transition.next_state
    raise _PHASE6._ArithmeticOrStateFailure(
        "closed witness ended before success"
    )


def _solve_closed(
    task: object,
    *,
    graph_certified: bool = False,
) -> _StructuralSolution:
    """Return every state frontier so signature descent can be audited."""

    if not graph_certified:
        _enumerate_closed_graph(task)
    started = perf_counter()
    memo: dict[tuple[object, ...], tuple[object, tuple[object, ...]]] = {}
    candidate_values = 0

    def solve(state: object) -> tuple[object, ...]:
        nonlocal candidate_values
        cached = memo.get(state.key)
        if cached is not None:
            return cached[1]

        candidates = []
        actions = _closed_admissible_actions(
            state.complete_quotient,
            task.prime,
        )
        for action in actions:
            transition = _PHASE6._advance(
                task,
                state,
                action,
                admitted_actions=actions,
            )
            stage_cost = _PHASE6._stage_cost(state, transition)
            if transition.outcome in ("success_exact", "success_precision"):
                candidate_values += 1
                candidates.append(
                    _PHASE6._ParetoValue(
                        transition.outcome,
                        stage_cost
                        + _PHASE6._terminal_decoder_cost(task, transition),
                        (action,),
                    )
                )
                continue
            if transition.outcome != "live":
                continue
            if transition.next_state is None:
                raise _PHASE6._ArithmeticOrStateFailure(
                    "live closed Bellman edge omitted its state"
                )
            for suffix in solve(transition.next_state):
                candidate_values += 1
                candidates.append(
                    _PHASE6._ParetoValue(
                        suffix.outcome,
                        stage_cost + suffix.cost,
                        (action,) + suffix.actions,
                    )
                )

        result = _PHASE6._pareto_frontier(tuple(candidates))
        memo[state.key] = (state, result)
        return result

    initial = _PHASE6._initial_state(task.initial, task.prime)
    frontier = solve(initial)
    if not frontier:
        raise _PHASE6._ArithmeticOrStateFailure(
            "closed initial state has no successful value"
        )
    if any(_replay_closed_value(task, value) != value for value in frontier):
        raise _PHASE6._ArithmeticOrStateFailure(
            "closed Bellman witness replay disagrees"
        )
    return _StructuralSolution(
        frontier,
        tuple(memo.values()),
        candidate_values,
        perf_counter() - started,
    )


def _aggregate(records: tuple[_WorkloadRecord, ...]) -> _Aggregate:
    return _Aggregate(
        inputs=len(records),
        states=sum(record.census.states for record in records),
        actions=sum(record.census.enumerated_actions for record in records),
        exact_edges=sum(record.census.success_exact for record in records),
        precision_edges=sum(
            record.census.success_precision for record in records
        ),
        cycles=sum(record.census.cycles for record in records),
        horizons=sum(record.census.horizons for record in records),
        maximum_states=max(record.census.states for record in records),
        maximum_actions=max(
            record.census.enumerated_actions for record in records
        ),
        maximum_live_step=max(
            record.census.maximum_live_step for record in records
        ),
        frontier_records=sum(
            len(record.solution.frontier) for record in records
        ),
        maximum_frontier=max(
            len(record.solution.frontier) for record in records
        ),
        exact_frontiers=sum(
            value.outcome == "success_exact"
            for record in records
            for value in record.solution.frontier
        ),
        precision_frontiers=sum(
            value.outcome == "success_precision"
            for record in records
            for value in record.solution.frontier
        ),
    )


def _optimal_bits(
    task: object,
    state: object,
    frontier: tuple[object, ...],
    axis: _Axis,
) -> frozenset[int]:
    minimum = min(getattr(value.cost, axis) for value in frontier)
    return frozenset(
        _lift_bit(
            state.complete_quotient,
            task.prime,
            value.actions[0],
        )
        for value in frontier
        if getattr(value.cost, axis) == minimum
    )


def _signature(task: object, state: object, level: _SignatureLevel) -> object:
    alpha = state.complete_quotient
    first_exponent = min(_PHASE6._valuation(alpha, task.prime), 0)
    ruban = _PHASE6._padic_floor(alpha, task.prime, "ruban")
    base = (
        task.prime,
        first_exponent,
        ruban,
        (alpha > 0) - (alpha < 0),
        alpha == ruban,
        task.horizon - state.step,
    )
    if level == 0:
        return base

    geometry = []
    local_costs = []
    actions = _closed_admissible_actions(alpha, task.prime)
    for action in actions:
        transition = _PHASE6._advance(
            task,
            state,
            action,
            admitted_actions=actions,
        )
        bit = _lift_bit(alpha, task.prime, action)
        geometry.append(
            (
                bit,
                transition.lattice_vertex,
                _PHASE6._tree_distance(
                    state.lattice_vertex,
                    transition.lattice_vertex,
                ),
                transition.outcome,
            )
        )
        cost = _PHASE6._stage_cost(state, transition)
        if transition.outcome in ("success_exact", "success_precision"):
            cost += _PHASE6._terminal_decoder_cost(task, transition)
        local_costs.append((bit, cost))

    evaluated = (
        base
        + (
            state.lattice_vertex,
            tuple(sorted(geometry)),
        )
    )
    if level == 1:
        return evaluated
    return evaluated + (tuple(sorted(local_costs)),)


def _audit_signatures(
    records: tuple[_WorkloadRecord, ...],
    level: _SignatureLevel,
) -> _SignatureAudit:
    groups: dict[tuple[object, ...], list[tuple[object, ...]]] = defaultdict(list)
    number_of_records = 0
    for record in records:
        for state, frontier in record.solution.state_values:
            if not frontier:
                continue
            for axis in ("digit_steps", "decoder_bits"):
                number_of_records += 1
                groups[
                    (
                        axis,
                        _signature(record.task, state, level),
                    )
                ].append(
                    (
                        record.task,
                        state,
                        _optimal_bits(
                            record.task,
                            state,
                            frontier,
                            axis,
                        ),
                        frontier,
                    )
                )

    collisions = []
    for key, items in groups.items():
        bit_sets = {item[2] for item in items}
        if len(bit_sets) > 1:
            collisions.append((key, tuple(items)))
    disjoint = tuple(
        collision
        for collision in collisions
        if not set.intersection(
            *(set(item[2]) for item in collision[1])
        )
    )
    witness_source = disjoint or tuple(collisions)
    witness = witness_source[0] if witness_source else None
    return _SignatureAudit(
        records=number_of_records,
        groups=len(groups),
        collisions=len(collisions),
        digit_collisions=sum(
            key[0] == "digit_steps" for key, _ in collisions
        ),
        decoder_collisions=sum(
            key[0] == "decoder_bits" for key, _ in collisions
        ),
        disjoint_collisions=len(disjoint),
        witness=witness,
    )


def _compile_binary_policy(
    prime: int,
    axis: _Axis,
    records: tuple[_WorkloadRecord, ...],
) -> _BinaryPolicyLedger:
    table: dict[tuple[object, ...], tuple[object, Fraction]] = {}
    for record in records:
        value = _PHASE6._choose_scalar_value(record.solution.frontier, axis)
        state = _PHASE6._initial_state(
            record.task.initial,
            record.task.prime,
        )
        for action in value.actions:
            incumbent = table.get(state.key)
            if incumbent is not None and incumbent[1] != action:
                raise _PHASE6._ArithmeticOrStateFailure(
                    "binary controller assigns two actions to one state"
                )
            table[state.key] = (state, action)
            actions = _closed_admissible_actions(
                state.complete_quotient,
                prime,
            )
            transition = _PHASE6._advance(
                record.task,
                state,
                action,
                admitted_actions=actions,
            )
            if transition.outcome != "live":
                break
            if transition.next_state is None:
                raise _PHASE6._ArithmeticOrStateFailure(
                    "compiled binary policy omitted a live state"
                )
            state = transition.next_state

    state_bits = sum(
        _PHASE6._state_action_serialized_bits(state, action)
        - _PHASE6._rational_bits(action)
        for state, action in table.values()
    )
    rational_action_bits = sum(
        _PHASE6._rational_bits(action)
        for _, action in table.values()
    )
    choice_bits = sum(
        len(_closed_admissible_actions(state.complete_quotient, prime)) == 2
        for state, _ in table.values()
    )
    # One fixed-prime table stores p once and one tag bit selecting this
    # normal-form layout.  The arithmetic theorem/decoder is shared code, not
    # silently charged once per state.
    normal_form_metadata_bits = prime.bit_length() + 1
    return _BinaryPolicyLedger(
        prime,
        axis,
        entries=len(table),
        state_bits=state_bits,
        rational_action_bits=rational_action_bits,
        choice_bits=choice_bits,
        normal_form_metadata_bits=normal_form_metadata_bits,
        rational_table_bits=state_bits + rational_action_bits,
        binary_table_bits=(
            state_bits + choice_bits + normal_form_metadata_bits
        ),
    )


@pytest.fixture(scope="module")
def _phase7_workloads() -> dict[tuple[str, int, int], tuple[_WorkloadRecord, ...]]:
    x12 = _corpus(12)
    x18_holdout = tuple(sorted(set(_corpus(18)) - set(x12)))
    assert (len(x12), len(x18_holdout)) == (182, 224)
    workloads: dict[tuple[str, int, int], tuple[Fraction, ...]] = {}
    for prime in (3, 5, 7):
        workloads[("R", prime, 4)] = x12
        for precision in (6, 8):
            workloads[("D", prime, precision)] = x12
        workloads[("I", prime, 6)] = x18_holdout
    for prime in (11, 13):
        for precision in (4, 6):
            workloads[("P", prime, precision)] = x12

    result = {}
    for key, values in workloads.items():
        label, prime, precision = key
        horizon = 16 if label == "R" else 24
        records = []
        for value in values:
            task = _PHASE6._Task(
                prime,
                value,
                precision=precision,
                horizon=horizon,
                max_states=50_000,
                max_transitions=100_000,
            )
            census, _ = _enumerate_closed_graph(task)
            records.append(
                _WorkloadRecord(
                    task,
                    census,
                    _solve_closed(task, graph_certified=True),
                )
            )
        result[key] = tuple(records)
    return result


def _select_workload(
    workloads: dict[tuple[str, int, int], tuple[_WorkloadRecord, ...]],
    label: str,
) -> tuple[_WorkloadRecord, ...]:
    return tuple(
        record
        for key in sorted(workloads)
        if key[0] == label
        for record in workloads[key]
    )


def test_gate7a_coefficient_box_is_the_complete_declared_grid():
    cases = (
        (3, -4),
        (5, -3),
        (7, -3),
        (11, -2),
        (13, -2),
    )
    for prime, first_exponent in cases:
        unit = _PHASE6._prime_power(prime, first_exponent)
        bound = Fraction(prime) - unit
        radius = prime ** (1 - first_exponent) - 1
        expected = {
            integer * unit
            for integer in range(-radius, radius + 1)
        }
        observed = _coefficient_image(prime, first_exponent)
        assert observed == expected
        assert min(observed) == -bound
        assert max(observed) == bound


def test_gate7a_binary_normal_form_matches_bounded_raw_enumeration():
    cases = (
        (3, -4),
        (5, -3),
        (7, -3),
        (11, -2),
        (13, -2),
    )
    for prime, first_exponent in cases:
        unit = _PHASE6._prime_power(prime, first_exponent)
        bound = Fraction(prime) - unit
        values = {
            Fraction(prime),
            Fraction(-prime),
            unit,
            -unit,
            unit + prime,
            unit - prime,
            bound,
            -bound,
            bound + prime,
            -bound + prime,
        }
        for value in values:
            raw = _PHASE6._admissible_actions(
                value,
                prime,
                max_candidates=250_000,
            )
            closed = _closed_admissible_actions(value, prime)
            assert closed == raw
            assert len(closed) <= 2
            assert all(
                action
                == _PHASE6._padic_floor(value, prime, "ruban")
                - _lift_bit(value, prime, action) * prime
                for action in closed
            )
            assert all(
                _PHASE6._padic_floor(value, prime, selector) in closed
                for selector in ("ruban", "browkin")
            )


def test_gate7b_closed_evaluator_reproduces_phase6(
    _phase7_workloads: dict[
        tuple[str, int, int],
        tuple[_WorkloadRecord, ...],
    ],
):
    expected = {
        3: _Aggregate(182, 682, 1316, 370, 434, 12, 0, 7, 14, 2, 202, 3, 186, 16),
        5: _Aggregate(182, 838, 1646, 448, 522, 20, 0, 7, 14, 2, 182, 1, 182, 0),
        7: _Aggregate(182, 880, 1738, 450, 564, 26, 0, 7, 14, 2, 182, 1, 182, 0),
    }
    for prime in (3, 5, 7):
        records = _phase7_workloads[("R", prime, 4)]
        assert _aggregate(records) == expected[prime]
        for record in records:
            for state, _ in record.solution.state_values:
                actions = _closed_admissible_actions(
                    state.complete_quotient,
                    prime,
                )
                assert all(
                    _PHASE6._padic_floor(
                        state.complete_quotient,
                        prime,
                        selector,
                    )
                    in actions
                    for selector in ("ruban", "browkin")
                )
            assert all(
                _replay_closed_value(record.task, value) == value
                for value in record.solution.frontier
            )


def test_gate7c_local_signatures_have_exact_policy_collisions(
    _phase7_workloads: dict[
        tuple[str, int, int],
        tuple[_WorkloadRecord, ...],
    ],
):
    records = _select_workload(_phase7_workloads, "R")
    expected = {
        0: (4800, 866, 96, 48, 48, 78),
        1: (4800, 3840, 86, 44, 42, 66),
        2: (4800, 3840, 86, 44, 42, 66),
    }
    for level in (0, 1, 2):
        audit = _audit_signatures(records, level)
        assert (
            audit.records,
            audit.groups,
            audit.collisions,
            audit.digit_collisions,
            audit.decoder_collisions,
            audit.disjoint_collisions,
        ) == expected[level]
        assert audit.witness is not None


def test_gate7d_precision_prime_and_input_transfer_are_exactly_exhaustible(
    _phase7_workloads: dict[
        tuple[str, int, int],
        tuple[_WorkloadRecord, ...],
    ],
):
    expected = {
        ("D", 3, 6): _Aggregate(182, 988, 1928, 662, 384, 76, 0, 12, 24, 3, 188, 2, 188, 0),
        ("D", 3, 8): _Aggregate(182, 1168, 2288, 842, 204, 256, 0, 17, 34, 4, 188, 2, 188, 0),
        ("D", 5, 6): _Aggregate(182, 1248, 2466, 806, 480, 114, 0, 13, 26, 3, 182, 1, 182, 0),
        ("D", 5, 8): _Aggregate(182, 1506, 2982, 1050, 280, 328, 0, 19, 38, 4, 182, 1, 182, 0),
        ("D", 7, 6): _Aggregate(182, 1330, 2638, 816, 540, 134, 0, 14, 28, 3, 182, 1, 182, 0),
        ("D", 7, 8): _Aggregate(182, 1678, 3334, 1122, 392, 324, 0, 23, 46, 4, 182, 1, 182, 0),
        ("P", 11, 4): _Aggregate(182, 886, 1750, 446, 574, 26, 0, 7, 14, 2, 182, 1, 182, 0),
        ("P", 11, 6): _Aggregate(182, 1342, 2662, 810, 548, 144, 0, 14, 28, 3, 182, 1, 182, 0),
        ("P", 13, 4): _Aggregate(182, 1056, 2112, 456, 758, 24, 0, 7, 14, 2, 184, 2, 178, 6),
        ("P", 13, 6): _Aggregate(182, 1716, 3432, 944, 832, 122, 0, 15, 30, 3, 182, 1, 182, 0),
        ("I", 3, 6): _Aggregate(224, 1552, 3048, 812, 868, 40, 0, 13, 26, 3, 256, 2, 256, 0),
        ("I", 5, 6): _Aggregate(224, 1922, 3810, 1044, 1008, 60, 0, 14, 28, 3, 224, 1, 224, 0),
        ("I", 7, 6): _Aggregate(224, 2066, 4106, 1072, 1118, 74, 0, 15, 30, 3, 224, 1, 224, 0),
    }
    transfer_keys = {
        key for key in _phase7_workloads if key[0] in {"D", "P", "I"}
    }
    assert transfer_keys == set(expected)
    for key in sorted(transfer_keys):
        records = _phase7_workloads[key]
        assert _aggregate(records) == expected[key]

    signature_expected = {
        "D": {
            0: (15836, 1092, 102, 53, 49, 98),
            1: (15836, 9876, 106, 63, 43, 88),
            2: (15836, 10104, 106, 63, 43, 88),
        },
        "P": {
            0: (10000, 862, 60, 31, 29, 52),
            1: (10000, 7336, 44, 22, 22, 38),
            2: (10000, 7488, 44, 22, 22, 38),
        },
        "I": {
            0: (11080, 1486, 206, 107, 99, 183),
            1: (11080, 9256, 181, 96, 85, 167),
            2: (11080, 9392, 181, 96, 85, 167),
        },
    }
    for label, levels in signature_expected.items():
        records = _select_workload(_phase7_workloads, label)
        for level, expected_audit in levels.items():
            audit = _audit_signatures(records, level)
            assert (
                audit.records,
                audit.groups,
                audit.collisions,
                audit.digit_collisions,
                audit.decoder_collisions,
                audit.disjoint_collisions,
            ) == expected_audit


def test_gate7e_binary_action_payload_reduces_complete_table_storage(
    _phase7_workloads: dict[
        tuple[str, int, int],
        tuple[_WorkloadRecord, ...],
    ],
):
    expected = {
        (3, "digit_steps"): (364, 11802, 1462, 316, 3, 13264, 12121),
        (3, "decoder_bits"): (372, 12139, 1472, 324, 3, 13611, 12466),
        (5, "digit_steps"): (372, 13124, 1746, 342, 4, 14870, 13470),
        (5, "decoder_bits"): (372, 13124, 1746, 342, 4, 14870, 13470),
        (7, "digit_steps"): (366, 13250, 1776, 344, 4, 15026, 13598),
        (7, "decoder_bits"): (366, 13250, 1776, 344, 4, 15026, 13598),
    }
    for prime in (3, 5, 7):
        records = _phase7_workloads[("R", prime, 4)]
        for axis in ("digit_steps", "decoder_bits"):
            ledger = _compile_binary_policy(prime, axis, records)
            assert (
                ledger.entries,
                ledger.state_bits,
                ledger.rational_action_bits,
                ledger.choice_bits,
                ledger.normal_form_metadata_bits,
                ledger.rational_table_bits,
                ledger.binary_table_bits,
            ) == expected[(prime, axis)]
            assert ledger.rational_table_bits == (
                ledger.state_bits + ledger.rational_action_bits
            )
            assert ledger.binary_table_bits == (
                ledger.state_bits
                + ledger.choice_bits
                + ledger.normal_form_metadata_bits
            )
            assert ledger.binary_table_bits < ledger.rational_table_bits
            assert ledger.choice_bits <= ledger.entries
