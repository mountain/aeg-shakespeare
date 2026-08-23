"""Independent process red team for pairwise clean-separability.

Four point particles move freely on a line until the first adjacent contact.
Assume

    x0 < x1 < x2 < x3
    v0 > v1 > v2 > v3,

so all three adjacent gaps are closing.  Before the first event, the candidate
contact times are

    tau_i = (x_{i+1} - x_i) / (v_i - v_{i+1}),  i=0,1,2.

The task is only the nonempty set of adjacent contacts attaining the minimum
candidate time.  Simultaneous multi-particle contact is allowed because the task
stops at the first event; no post-collision resolution rule is needed.

This calibration is intentionally independent of Lonely Runner geometry.  It
uses the research-local Phase-13 clean-separability checker only as a red-team
criterion.  No public API is exercised or extended.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import importlib.util
from itertools import permutations, product
from pathlib import Path
import sys


@dataclass(frozen=True)
class FreeFlightState:
    positions: tuple[Fraction, ...]
    velocities: tuple[Fraction, ...]


def state_from_candidate_times(times: tuple[Fraction, Fraction, Fraction]) -> FreeFlightState:
    """Embed arbitrary positive candidate collision times in a physical state.

    Use adjacent relative closing speeds all equal to one:

        v = (3,2,1,0).

    Then choosing consecutive gaps equal to ``times`` realizes exactly those
    candidate first-contact times.
    """

    if any(time <= 0 for time in times):
        raise ValueError("candidate collision times must be positive")

    velocities = tuple(map(Fraction, (3, 2, 1, 0)))
    positions = [Fraction(0)]
    for gap in times:
        positions.append(positions[-1] + Fraction(gap))
    return FreeFlightState(tuple(positions), velocities)


def candidate_collision_times(state: FreeFlightState) -> tuple[Fraction, ...]:
    result = []
    for index in range(3):
        gap = state.positions[index + 1] - state.positions[index]
        closing = state.velocities[index] - state.velocities[index + 1]
        assert gap > 0 and closing > 0
        result.append(gap / closing)
    return tuple(result)


def next_collision_group(state: FreeFlightState) -> tuple[int, ...]:
    times = candidate_collision_times(state)
    minimum = min(times)
    return tuple(index for index, time in enumerate(times) if time == minimum)


def pairwise_signs(times: tuple[Fraction, ...]) -> tuple[int, int, int]:
    pairs = ((0, 1), (0, 2), (1, 2))
    return tuple(
        -1 if times[first] < times[second] else (
            1 if times[first] > times[second] else 0
        )
        for first, second in pairs
    )


def witnesses_for_minimum_group(group: tuple[int, ...]):
    """Exact finite witnesses for every forced / unforced pair relation.

    Members of ``group`` receive time 1.  Nonmembers receive distinct values
    2,3 in every possible order.  Thus a pair of nonminimal events is explicitly
    realized in both loser orders, while all relations involving a minimum event
    are fixed by the task stratum itself.
    """

    group_set = set(group)
    losers = tuple(index for index in range(3) if index not in group_set)
    if len(losers) <= 1:
        assignments = (tuple(range(2, 2 + len(losers))),)
    else:
        assignments = tuple(permutations(range(2, 2 + len(losers))))

    states = []
    for values in assignments:
        times = [Fraction(1)] * 3
        for runner, value in zip(losers, values):
            times[runner] = Fraction(value)
        state = state_from_candidate_times(tuple(times))
        assert next_collision_group(state) == group
        states.append(state)
    return tuple(states)


def partial_signature_for_group(group: tuple[int, ...]):
    signatures = tuple(
        pairwise_signs(candidate_collision_times(state))
        for state in witnesses_for_minimum_group(group)
    )
    result = []
    for coordinate in range(3):
        values = {signature[coordinate] for signature in signatures}
        result.append(next(iter(values)) if len(values) == 1 else None)
    return tuple(result)


def load_clean_separator_theory():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "clean_separator_theory.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "hard_particle_clean_separator_redteam",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def all_nonempty_groups():
    return tuple(
        tuple(index for index in range(3) if mask & (1 << index))
        for mask in range(1, 1 << 3)
    )


def test_arbitrary_positive_collision_times_have_exact_physical_embeddings():
    examples = (
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(7, 5), Fraction(4, 3), Fraction(11, 7)),
        (Fraction(5, 2), Fraction(5, 2), Fraction(9, 2)),
        (Fraction(8, 3), Fraction(8, 3), Fraction(8, 3)),
    )
    for times in examples:
        state = state_from_candidate_times(times)
        assert candidate_collision_times(state) == times


def test_every_nonempty_first_collision_group_is_physically_realizable():
    for group in all_nonempty_groups():
        witnesses = witnesses_for_minimum_group(group)
        assert witnesses
        assert all(next_collision_group(state) == group for state in witnesses)


def test_physical_task_regions_rederive_the_three_event_argmin_partial_geometry():
    expected = {
        (0,): (-1, -1, None),
        (1,): (1, None, -1),
        (2,): (None, 1, 1),
        (0, 1): (0, -1, -1),
        (0, 2): (-1, 0, 1),
        (1, 2): (1, 1, 0),
        (0, 1, 2): (0, 0, 0),
    }
    actual = {
        group: partial_signature_for_group(group)
        for group in all_nonempty_groups()
    }
    assert actual == expected


def test_next_collision_task_is_pairwise_sufficient_but_not_clean_separable():
    clean = load_clean_separator_theory()
    regions = tuple(
        clean.PartialRegion(
            name=group,
            task=group,
            signs=partial_signature_for_group(group),
        )
        for group in all_nonempty_groups()
    )

    assert clean.pairwise_task_separable(regions)
    result = clean.analyze_clean_separability(regions)
    assert not result.clean
    assert result.obstruction is not None
    assert result.obstruction.atomic
    assert clean.verify_obstruction(regions, result.obstruction)


def test_completing_pairwise_orders_creates_13_states_for_only_7_collision_tasks():
    records = {}
    # Enumerating small integer candidate times generates every weak total order
    # on three events.  Each record is physically embedded before classification.
    for values in product((1, 2, 3), repeat=3):
        times = tuple(Fraction(value) for value in values)
        state = state_from_candidate_times(times)
        signature = pairwise_signs(times)
        task = next_collision_group(state)
        previous = records.get(signature)
        if previous is not None:
            assert previous == task
        records[signature] = task

    assert len(records) == 13
    assert len(set(records.values())) == 7
