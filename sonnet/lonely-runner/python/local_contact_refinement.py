"""Local center-2 -> center-3 semantic refinement without full center-3 census.

This script uses only the already-objectified center-2 pair-difference geometry,
its certified first-witness contact prefixes, and the newly introduced center-3
contact events.  It predicts which old task-safe parents must be reopened, then
refines only the corresponding full sign systems.

It deliberately does *not* enumerate all 72,241 center-3 realizable systems.
The frozen full-census numbers are used only as assertions/red-team targets.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

import pair_difference_refinement as pd


def alpha(event: tuple[int, int, str]) -> Fraction:
    _runner, center, kind = event
    return (
        Fraction(center) + pd.DELTA
        if kind == "exit"
        else Fraction(center) - pd.DELTA
    )


def arbitrary_relation(stratum, threshold: Fraction) -> int | None:
    """Return sign(q-threshold), or None when the old stratum crosses it."""

    if threshold <= 1:
        return 1
    if threshold >= pd.RMAX:
        return -1
    kind, lower, upper = stratum
    if kind == "E":
        return -1 if lower < threshold else (1 if lower > threshold else 0)
    if upper is not None and upper <= threshold:
        return -1
    if lower >= threshold:
        return 1
    return None


def event_time_relation(old_system, old_strata, left, right) -> int | None:
    """Sign(t_left-t_right) under an old sign system; None means unresolved."""

    i, _ni, _ki = left
    j, _nj, _kj = right
    a = alpha(left)
    b = alpha(right)
    if i == j:
        return -1 if a < b else (1 if a > b else 0)

    if i < j:
        ratio = b / a
        pair = (i, j)
        relation = arbitrary_relation(
            old_strata[old_system[pd.PAIR_INDEX[pair]]],
            ratio,
        )
        return relation

    ratio = a / b
    pair = (j, i)
    relation = arbitrary_relation(
        old_strata[old_system[pd.PAIR_INDEX[pair]]],
        ratio,
    )
    return None if relation is None else -relation


def collision_wall(left, right):
    """Pair-difference wall where two contact events have equal time."""

    i = left[0]
    j = right[0]
    if i == j:
        return None
    if i < j:
        ratio = alpha(right) / alpha(left)
        pair = (i, j)
    else:
        ratio = alpha(left) / alpha(right)
        pair = (j, i)
    if not (1 < ratio < pd.RMAX):
        return None
    return pair[0], pair[1], ratio


def main() -> None:
    ratios2 = pd.contact_ratios(2)
    ratios3 = pd.contact_ratios(3)
    strata2 = pd.strata(ratios2)
    strata3 = pd.strata(ratios3)
    genuinely_new_ratios = set(ratios3) - set(ratios2)

    # This is the only complete geometry enumerated by the algorithm.
    old_systems = pd.enumerate_systems(strata2)
    assert len(old_systems) == 5_823

    old_tasks = []
    old_histories = []
    for system in old_systems:
        task, history = pd.first_witness(system, 2, ratios2, strata2)
        old_tasks.append(task)
        old_histories.append(history)

    old_signatures = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in old_systems
    )
    old_relevant = pd.relevant_walls(old_systems, tuple(old_tasks), ratios2)
    assert len(old_relevant) == 21

    parents: dict[tuple[int, ...], list[int]] = defaultdict(list)
    parent_task: dict[tuple[int, ...], tuple[object, ...]] = {}
    for index, (signature, task) in enumerate(zip(old_signatures, old_tasks)):
        parent = tuple(signature[position] for position in old_relevant)
        parents[parent].append(index)
        previous = parent_task.get(parent)
        if previous is not None:
            assert previous == task
        parent_task[parent] = task
    assert len(parents) == 849

    new_events = tuple(
        (runner, 3, kind)
        for runner in range(pd.K)
        for kind in ("enter", "exit")
    )

    def forced_earlier(parent) -> bool:
        """A new contact is already forced into the old witness prefix."""

        witness_event = parent_task[parent][1][0]
        for system_index in parents[parent]:
            system = old_systems[system_index]
            for new_event in new_events:
                relation = event_time_relation(
                    system,
                    strata2,
                    new_event,
                    witness_event,
                )
                if relation is not None and relation <= 0:
                    return True
        return False

    def effective_unresolved_crossing(parent) -> bool:
        """A genuinely new non-enter/enter wall can change the causal prefix."""

        for system_index in parents[parent]:
            system = old_systems[system_index]
            history = old_histories[system_index]
            old_prefix_events = tuple(
                event
                for step in history
                for event in step[0]
            )
            for new_event in new_events:
                for old_event in old_prefix_events:
                    # Two enter events only make the safe set smaller after the
                    # first crossing.  If all other runners were safe just before
                    # them, the first witness would already have occurred.  Their
                    # unresolved order cannot create the first safe time.
                    if new_event[2] == "enter" and old_event[2] == "enter":
                        continue

                    wall = collision_wall(new_event, old_event)
                    if wall is None or wall[2] not in genuinely_new_ratios:
                        continue
                    pair = wall[:2]
                    relation = arbitrary_relation(
                        strata2[system[pd.PAIR_INDEX[pair]]],
                        wall[2],
                    )
                    if relation is None:
                        return True
        return False

    affected = {
        parent
        for parent in parents
        if forced_earlier(parent) or effective_unresolved_crossing(parent)
    }
    assert len(affected) == 8

    affected_full_indices = sorted(
        index
        for parent in affected
        for index in parents[parent]
    )
    assert len(affected_full_indices) == 26
    affected_old_systems = tuple(old_systems[index] for index in affected_full_indices)

    # Refine only the 26 full systems carried by the eight affected task-safe
    # parents.  No other center-2 state is reopened.
    refined_children = pd.refine_systems(
        affected_old_systems,
        strata2,
        strata3,
    )
    assert len(refined_children) == 298

    child_map = pd.refinement_map(strata2, strata3)
    new_to_old = {}
    for old_index, children in enumerate(child_map):
        for new_index in children:
            assert new_index not in new_to_old
            new_to_old[new_index] = old_index
    assert len(new_to_old) == len(strata3)

    local_new_tasks: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
    for child in refined_children:
        task, _history = pd.first_witness(child, 3, ratios3, strata3)
        parent_system = tuple(new_to_old[index] for index in child)
        parent_signature = pd.full_signature(parent_system, ratios2, strata2)
        parent = tuple(parent_signature[position] for position in old_relevant)
        assert parent in affected
        local_new_tasks[parent].add(task)

    assert set(local_new_tasks) == affected
    assert sorted(len(tasks) for tasks in local_new_tasks.values()) == [1, 1, 3, 3, 5, 5, 5, 7]

    # Reuse all 841 unaffected old semantics and replace/refine only the eight
    # affected parents.  The local update already recovers the complete final
    # center-3 witness-semantic count from the frozen full-census oracle.
    updated_semantics = set()
    for parent, task in parent_task.items():
        if parent in affected:
            updated_semantics.update(local_new_tasks[parent])
        else:
            updated_semantics.add(task)
    assert len(updated_semantics) == 75

    split_count = sum(len(tasks) > 1 for tasks in local_new_tasks.values())
    replacement_count = sum(
        len(tasks) == 1 and next(iter(tasks)) != parent_task[parent]
        for parent, tasks in local_new_tasks.items()
    )
    unchanged_affected_count = sum(
        len(tasks) == 1 and next(iter(tasks)) == parent_task[parent]
        for parent, tasks in local_new_tasks.items()
    )
    assert split_count == 6
    assert replacement_count == 2
    assert unchanged_affected_count == 0

    print("local contact-refinement update")
    print(f"  old task-safe parents:       {len(parents):,}")
    print(f"  detected affected parents:   {len(affected):,}")
    print(f"    semantic splits:           {split_count}")
    print(f"    uniform replacements:      {replacement_count}")
    print(f"  old full systems reopened:   {len(affected_old_systems):,} / {len(old_systems):,}")
    print(f"  refined center-3 children:   {len(refined_children):,}")
    print(f"  recovered center-3 semantics:{len(updated_semantics):,}")
    print()
    print("full center-3 census avoided: 72,241 systems")
    print(f"local semantic evaluation:     {len(refined_children):,} systems")
    print(f"reduction factor:              {72_241/len(refined_children):.1f}x")


if __name__ == "__main__":
    main()
