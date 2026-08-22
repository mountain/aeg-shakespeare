"""Local center-2 -> center-3 semantic refinement without full center-3 census.

This script uses only the already-objectified center-2 pair-difference geometry,
its certified first-witness contact prefixes, and the newly introduced center-3
contact events.  It predicts which old task-safe parents must be reopened, then
refines only the corresponding full sign systems.

Phase 8A first produced a three-way local classification

    stable              = not forced_earlier and not unresolved_crossing
    nonbranching_update = forced_earlier and not unresolved_crossing
    completion_required = unresolved_crossing

before any center-3 child semantics were examined.

The Phase-8B witness probe then red-teamed the middle class.  In both cases the
canonical witness boundary and mode remain *identical*; only the event index is
shifted by two because newly admitted contacts are inserted earlier in the
history.  Therefore these cases are now named ``history_reindex`` rather than
``transport``.  They remain inside the current representation and belong to the
renormalizable sector of the generic ``CanonicalDecomposition``.  No discrete
observer-connection sector has yet been observed in this calibration.

The script deliberately does *not* enumerate all 72,241 center-3 realizable
systems.  The frozen full-census numbers are used only as assertions/red-team
targets.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import pair_difference_refinement as pd


@dataclass(frozen=True)
class HistoryReindexCaseAnalysis:
    """Post-classification witness record for one nonbranching history update."""

    parent: tuple[int, ...]
    old_task: tuple[object, ...]
    new_task: tuple[object, ...]
    old_full_system_count: int

    @property
    def event_index_shift(self) -> int:
        return int(self.new_task[0]) - int(self.old_task[0])

    @property
    def same_boundary(self) -> bool:
        return self.new_task[1] == self.old_task[1]

    @property
    def same_mode(self) -> bool:
        return self.new_task[2] == self.old_task[2]


@dataclass(frozen=True)
class LocalRefinementAnalysis:
    """Exact center-2 -> center-3 local classification and red-team counts."""

    parent_count: int
    stable_parents: frozenset[tuple[int, ...]]
    history_reindex_parents: frozenset[tuple[int, ...]]
    completion_required_parents: frozenset[tuple[int, ...]]
    history_reindex_cases: tuple[HistoryReindexCaseAnalysis, ...]
    affected_full_system_count: int
    refined_child_count: int
    recovered_semantic_count: int
    verified_split_count: int
    verified_reindex_count: int

    @property
    def renormalizable_parents(self) -> frozenset[tuple[int, ...]]:
        """States that remain in the current task representation."""

        return self.stable_parents | self.history_reindex_parents

    @property
    def resonant_parents(self) -> frozenset[tuple[int, ...]]:
        """No genuine same-family observer-transport sector is known here."""

        return frozenset()

    @property
    def affected_parents(self) -> frozenset[tuple[int, ...]]:
        return self.history_reindex_parents | self.completion_required_parents


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


def analyze_center2_to_center3() -> LocalRefinementAnalysis:
    """Classify old task states locally, then red-team only affected states.

    The stable / nonbranching-update / completion-required partition is
    determined solely from center-2 task states and newly admitted center-3
    contact events.  Center-3 child semantics are evaluated only afterwards.
    The middle class is then further audited to decide *what* changed.
    """

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
                    # first crossing. If all other runners were safe just before
                    # them, the first witness would already have occurred. Their
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

    # PHASE 8A LOCAL PARTITION: no center-3 child semantics have been evaluated.
    forced = {parent for parent in parents if forced_earlier(parent)}
    unresolved = {
        parent
        for parent in parents
        if effective_unresolved_crossing(parent)
    }
    stable = set(parents) - forced - unresolved
    nonbranching_update = forced - unresolved
    completion_required = unresolved

    assert len(stable) == 841
    assert len(nonbranching_update) == 2
    assert len(completion_required) == 6
    assert not stable & nonbranching_update
    assert not stable & completion_required
    assert not nonbranching_update & completion_required
    assert stable | nonbranching_update | completion_required == set(parents)

    affected = nonbranching_update | completion_required
    assert len(affected) == 8

    affected_full_indices = sorted(
        index
        for parent in affected
        for index in parents[parent]
    )
    assert len(affected_full_indices) == 26
    affected_old_systems = tuple(old_systems[index] for index in affected_full_indices)

    # Refine only the 26 full systems carried by the eight affected task-safe
    # parents. No other center-2 state is reopened.
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

    # RED TEAM: only now inspect new semantics.  The pre-refinement local
    # partition must predict nonbranching update versus genuine splitting.
    assert all(
        len(local_new_tasks[parent]) == 1
        and next(iter(local_new_tasks[parent])) != parent_task[parent]
        for parent in nonbranching_update
    )
    assert all(
        len(local_new_tasks[parent]) > 1
        for parent in completion_required
    )

    history_reindex_cases = tuple(
        HistoryReindexCaseAnalysis(
            parent=parent,
            old_task=parent_task[parent],
            new_task=next(iter(local_new_tasks[parent])),
            old_full_system_count=len(parents[parent]),
        )
        for parent in sorted(nonbranching_update)
    )
    assert len(history_reindex_cases) == 2

    # PHASE 8B RED TEAM: the two nonbranching changes do not move the canonical
    # witness geometry at all.  They only reindex the same witness in the deeper
    # contact history, so they belong to the renormalizable/decoder sector, not a
    # genuine observer-transport/resonance sector.
    assert all(case.same_boundary for case in history_reindex_cases)
    assert all(case.same_mode for case in history_reindex_cases)
    assert all(case.event_index_shift == 2 for case in history_reindex_cases)

    updated_semantics = set()
    for parent, task in parent_task.items():
        if parent in affected:
            updated_semantics.update(local_new_tasks[parent])
        else:
            updated_semantics.add(task)
    assert len(updated_semantics) == 75

    split_count = sum(len(tasks) > 1 for tasks in local_new_tasks.values())
    reindex_count = sum(
        len(tasks) == 1 and next(iter(tasks)) != parent_task[parent]
        for parent, tasks in local_new_tasks.items()
    )
    unchanged_affected_count = sum(
        len(tasks) == 1 and next(iter(tasks)) == parent_task[parent]
        for parent, tasks in local_new_tasks.items()
    )
    assert split_count == 6
    assert reindex_count == 2
    assert unchanged_affected_count == 0

    return LocalRefinementAnalysis(
        parent_count=len(parents),
        stable_parents=frozenset(stable),
        history_reindex_parents=frozenset(nonbranching_update),
        completion_required_parents=frozenset(completion_required),
        history_reindex_cases=history_reindex_cases,
        affected_full_system_count=len(affected_old_systems),
        refined_child_count=len(refined_children),
        recovered_semantic_count=len(updated_semantics),
        verified_split_count=split_count,
        verified_reindex_count=reindex_count,
    )


def main() -> None:
    result = analyze_center2_to_center3()

    print("local contact-refinement canonical decomposition")
    print(f"  old task-safe parents:       {result.parent_count:,}")
    print(f"    stable identity:           {len(result.stable_parents):,}")
    print(f"    history reindex:           {len(result.history_reindex_parents):,}")
    print(f"    completion-required:       {len(result.completion_required_parents):,}")
    print(f"  canonical renormalizable:    {len(result.renormalizable_parents):,}")
    print(f"  canonical resonant:          {len(result.resonant_parents):,}")
    print(f"  old full systems reopened:   {result.affected_full_system_count:,} / 5,823")
    print(f"  refined center-3 children:   {result.refined_child_count:,}")
    print(f"  recovered center-3 semantics:{result.recovered_semantic_count:,}")
    print()
    print("history-reindex witness records")
    for case in result.history_reindex_cases:
        print(f"  parent:                {case.parent}")
        print(f"    old task:            {case.old_task}")
        print(f"    new task:            {case.new_task}")
        print(f"    event-index shift:   {case.event_index_shift}")
        print(f"    same boundary:       {case.same_boundary}")
        print(f"    same mode:           {case.same_mode}")
        print(f"    old full systems:    {case.old_full_system_count}")
    print()
    print("full center-3 census avoided: 72,241 systems")
    print(f"local semantic evaluation:     {result.refined_child_count:,} systems")
    print(f"reduction factor:              {72_241/result.refined_child_count:.1f}x")


if __name__ == "__main__":
    main()
