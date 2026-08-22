"""Local center-2 -> center-3 semantic refinement without full center-3 census.

This script uses only the already-objectified center-2 pair-difference geometry,
its certified first-witness contact prefixes, and the newly introduced center-3
contact events.  It predicts which old task-safe parents must be reopened, then
refines only the corresponding full sign systems.

Phase 8A first produced a three-way local behavioral classification

    stable              = not forced_earlier and not unresolved_crossing
    nonbranching_update = forced_earlier and not unresolved_crossing
    completion_required = unresolved_crossing

before any center-3 child semantics were examined.

Phase 8B red-teamed the middle class.  In both cases the canonical witness
boundary and mode remain identical; only the event index shifts by two because
newly admitted contacts are inserted earlier in the history.  They are therefore
history/decoder reindexing inside the renormalizable sector, not observer motion.

Phase 8C now treats the six genuinely branching parents constructively.  For
each one it searches the complete local center-3 child geometry for the smallest
set of process-generated pair/contact-wall signs whose joint values determine
the child task exactly.  No known five-wall answer or target residual signature
is supplied to the search.

The script deliberately does *not* enumerate all 72,241 center-3 realizable
systems.  The frozen full-census numbers are used only as assertions/red-team
targets.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

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
class ResidualCoordinate:
    """One process-generated pair/contact wall retained by a completion signature."""

    pair: tuple[int, int]
    ratio: Fraction
    new_at_center3: bool


@dataclass(frozen=True)
class CompletionResidualCaseAnalysis:
    """Minimum exact wall-sign signature for one branching parent."""

    parent: tuple[int, ...]
    child_system_count: int
    semantic_count: int
    coordinates: tuple[ResidualCoordinate, ...]
    residual_class_count: int

    @property
    def coordinate_count(self) -> int:
        return len(self.coordinates)


@dataclass(frozen=True)
class LocalRefinementAnalysis:
    """Exact center-2 -> center-3 local classification and red-team counts."""

    parent_count: int
    stable_parents: frozenset[tuple[int, ...]]
    history_reindex_parents: frozenset[tuple[int, ...]]
    completion_required_parents: frozenset[tuple[int, ...]]
    history_reindex_cases: tuple[HistoryReindexCaseAnalysis, ...]
    completion_residual_cases: tuple[CompletionResidualCaseAnalysis, ...]
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
        return arbitrary_relation(
            old_strata[old_system[pd.PAIR_INDEX[pair]]],
            ratio,
        )

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


def _minimum_task_separating_coordinates(
    children: tuple[tuple[int, ...], ...],
    tasks: tuple[tuple[object, ...], ...],
    ratios2: tuple[Fraction, ...],
    ratios3: tuple[Fraction, ...],
    strata3,
) -> tuple[tuple[int, ...], int]:
    """Return a minimum sign-coordinate set whose key determines task exactly.

    The finite optimization is formulated as exact conflict cover.  Every pair
    of children with different tasks must be separated by at least one selected
    wall-sign coordinate.  A feature covers exactly the cross-task pairs on
    which its sign differs.  Dynamic programming over the uncovered conflict
    bitset returns a minimum-cardinality feature set, with lexicographic tie
    breaking for reproducibility.
    """

    signatures = tuple(
        pd.full_signature(child, ratios3, strata3)
        for child in children
    )
    assert len(signatures) == len(tasks)
    feature_count = len(signatures[0])
    assert all(len(signature) == feature_count for signature in signatures)

    conflicts = tuple(
        (left, right)
        for left in range(len(children))
        for right in range(left + 1, len(children))
        if tasks[left] != tasks[right]
    )
    if not conflicts:
        return (), 1

    conflict_count = len(conflicts)
    full_mask = (1 << conflict_count) - 1

    coverage_to_feature: dict[int, int] = {}
    for feature in range(feature_count):
        values = {signature[feature] for signature in signatures}
        if len(values) <= 1:
            continue
        coverage = 0
        for conflict_index, (left, right) in enumerate(conflicts):
            if signatures[left][feature] != signatures[right][feature]:
                coverage |= 1 << conflict_index
        if coverage == 0:
            continue
        previous = coverage_to_feature.get(coverage)
        if previous is None or feature < previous:
            coverage_to_feature[coverage] = feature

    feature_masks = tuple(
        sorted(
            (feature, coverage)
            for coverage, feature in coverage_to_feature.items()
        )
    )
    assert feature_masks

    coverers: dict[int, tuple[tuple[int, int], ...]] = {}
    for conflict_index in range(conflict_count):
        bit = 1 << conflict_index
        options = tuple(
            (feature, coverage)
            for feature, coverage in feature_masks
            if coverage & bit
        )
        assert options
        coverers[conflict_index] = options

    @lru_cache(maxsize=None)
    def solve(uncovered: int) -> tuple[int, ...]:
        if uncovered == 0:
            return ()

        remaining_conflicts = [
            index
            for index in range(conflict_count)
            if uncovered & (1 << index)
        ]
        pivot = min(
            remaining_conflicts,
            key=lambda index: sum(
                bool(coverage & uncovered)
                for _feature, coverage in coverers[index]
            ),
        )

        best: tuple[int, ...] | None = None
        for feature, coverage in coverers[pivot]:
            reduced = uncovered & ~coverage
            tail = solve(reduced)
            candidate = tuple(sorted((feature, *tail)))
            if best is None or (len(candidate), candidate) < (len(best), best):
                best = candidate
        assert best is not None
        return best

    selected = solve(full_mask)

    task_by_key: dict[tuple[int, ...], tuple[object, ...]] = {}
    for signature, task in zip(signatures, tasks):
        key = tuple(signature[index] for index in selected)
        previous = task_by_key.get(key)
        if previous is not None:
            assert previous == task
        task_by_key[key] = task

    # Minimality certificate: no signature with one fewer selected coordinate
    # can classify all tasks.  The dynamic program proves this by construction;
    # this explicit deletion red team makes the witness local and reviewable.
    if selected:
        for removed in selected:
            reduced = tuple(index for index in selected if index != removed)
            seen: dict[tuple[int, ...], tuple[object, ...]] = {}
            has_conflict = False
            for signature, task in zip(signatures, tasks):
                key = tuple(signature[index] for index in reduced)
                previous = seen.get(key)
                if previous is not None and previous != task:
                    has_conflict = True
                    break
                seen[key] = task
            assert has_conflict

    return selected, len(task_by_key)


def analyze_center2_to_center3() -> LocalRefinementAnalysis:
    """Classify old task states, red-team updates, then discover completions."""

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

    local_children: dict[
        tuple[int, ...],
        list[tuple[tuple[int, ...], tuple[object, ...]]],
    ] = defaultdict(list)
    local_new_tasks: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
    for child in refined_children:
        task, _history = pd.first_witness(child, 3, ratios3, strata3)
        parent_system = tuple(new_to_old[index] for index in child)
        parent_signature = pd.full_signature(parent_system, ratios2, strata2)
        parent = tuple(parent_signature[position] for position in old_relevant)
        assert parent in affected
        local_children[parent].append((child, task))
        local_new_tasks[parent].add(task)

    assert set(local_new_tasks) == affected
    assert sorted(len(tasks) for tasks in local_new_tasks.values()) == [1, 1, 3, 3, 5, 5, 5, 7]

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
    assert all(case.same_boundary for case in history_reindex_cases)
    assert all(case.same_mode for case in history_reindex_cases)
    assert all(case.event_index_shift == 2 for case in history_reindex_cases)

    # PHASE 8C: discover a minimum exact residual signature independently for
    # each genuinely branching parent.  Candidate features are *all* center-3
    # pair/contact wall signs that vary among that parent's locally possible
    # children; the search is not handed the five globally known new walls.
    completion_residual_cases = []
    ratio2_set = set(ratios2)
    for parent in sorted(completion_required):
        entries = tuple(local_children[parent])
        children = tuple(child for child, _task in entries)
        tasks = tuple(task for _child, task in entries)
        selected, residual_class_count = _minimum_task_separating_coordinates(
            children,
            tasks,
            ratios2,
            ratios3,
            strata3,
        )
        assert selected
        coordinates = []
        for feature in selected:
            pair_index, ratio_index = divmod(feature, len(ratios3))
            ratio = ratios3[ratio_index]
            coordinates.append(
                ResidualCoordinate(
                    pair=pd.PAIRS[pair_index],
                    ratio=ratio,
                    new_at_center3=ratio not in ratio2_set,
                )
            )
        semantic_count = len(set(tasks))
        assert residual_class_count >= semantic_count
        completion_residual_cases.append(
            CompletionResidualCaseAnalysis(
                parent=parent,
                child_system_count=len(children),
                semantic_count=semantic_count,
                coordinates=tuple(coordinates),
                residual_class_count=residual_class_count,
            )
        )

    assert len(completion_residual_cases) == 6

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
        completion_residual_cases=tuple(completion_residual_cases),
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
    print("Phase 8C minimum completion residuals")
    for case in result.completion_residual_cases:
        print(f"  parent:                {case.parent}")
        print(f"    local children:      {case.child_system_count}")
        print(f"    task semantics:      {case.semantic_count}")
        print(f"    residual classes:    {case.residual_class_count}")
        print(f"    minimum walls:       {case.coordinate_count}")
        for coordinate in case.coordinates:
            provenance = "new@center3" if coordinate.new_at_center3 else "latent-old"
            print(
                f"      u{coordinate.pair[1]+1}/u{coordinate.pair[0]+1}"
                f" ? {coordinate.ratio}  [{provenance}]"
            )
    print()
    print("full center-3 census avoided: 72,241 systems")
    print(f"local semantic evaluation:     {result.refined_child_count:,} systems")
    print(f"reduction factor:              {72_241/result.refined_child_count:.1f}x")


if __name__ == "__main__":
    main()
