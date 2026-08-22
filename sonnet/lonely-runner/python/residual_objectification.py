"""Phase 8C.2: task-relative objectification of raw completion signatures.

Phase 8C found minimum-cardinality sets of center-3 contact-wall signs that are
sufficient to determine the exact first-witness task below each genuinely
branching center-2 parent.  Four such signatures already have exactly one raw
sign class per task class.  Two are over-refined: several raw sign tuples encode
the same task.

This script performs the next representation step without promoting a package
API.  It independently reconstructs the local children below the six completion
parents, projects each child to the Phase-8C minimum raw signature, then quotients
raw signatures by exact task semantics.  An exact adaptive decoder over only the
selected completion walls certifies that the quotient can be evaluated without
reading the full child sign system.

The task quotient is deliberately task-relative.  It is not claimed to be a
canonical quotient for every future refinement task.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

import local_contact_refinement as lcr
import pair_difference_refinement as pd


Task = tuple[object, ...]
RawKey = tuple[int, ...]


@dataclass(frozen=True)
class DecoderNode:
    """Finite adaptive decoder using only local completion-wall coordinates."""

    coordinate: int | None = None
    task: Task | None = None
    children: tuple[tuple[int, "DecoderNode"], ...] = ()

    @property
    def is_leaf(self) -> bool:
        return self.coordinate is None


@dataclass(frozen=True)
class ResidualObjectificationCase:
    """Exact task quotient and decoder statistics for one completion parent."""

    parent: tuple[int, ...]
    coordinate_count: int
    child_system_count: int
    raw_class_count: int
    quotient_class_count: int
    decoder_internal_nodes: int
    decoder_path_leaves: int
    decoder_unique_nodes: int
    decoder_worst_depth: int
    decoder_weighted_depth: Fraction

    @property
    def over_refined_raw_signature(self) -> bool:
        return self.raw_class_count > self.quotient_class_count


@dataclass(frozen=True)
class ResidualObjectificationAnalysis:
    cases: tuple[ResidualObjectificationCase, ...]

    @property
    def over_refined_cases(self) -> tuple[ResidualObjectificationCase, ...]:
        return tuple(case for case in self.cases if case.over_refined_raw_signature)


def _feature_index(coordinate: lcr.ResidualCoordinate, ratios3: tuple[Fraction, ...]) -> int:
    return (
        pd.PAIR_INDEX[coordinate.pair] * len(ratios3)
        + ratios3.index(coordinate.ratio)
    )


def _reconstruct_local_completion_children(
    completion_parents: frozenset[tuple[int, ...]],
):
    """Independent reconstruction of only the six completion-parent children."""

    ratios2 = pd.contact_ratios(2)
    ratios3 = pd.contact_ratios(3)
    strata2 = pd.strata(ratios2)
    strata3 = pd.strata(ratios3)

    old_systems = pd.enumerate_systems(strata2)
    assert len(old_systems) == 5_823
    old_tasks = tuple(
        pd.first_witness(system, 2, ratios2, strata2)[0]
        for system in old_systems
    )
    old_signatures = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in old_systems
    )
    old_relevant = pd.relevant_walls(old_systems, old_tasks, ratios2)
    assert len(old_relevant) == 21

    parent_of_old: dict[tuple[int, ...], tuple[int, ...]] = {}
    old_by_parent: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for system, signature in zip(old_systems, old_signatures):
        parent = tuple(signature[position] for position in old_relevant)
        parent_of_old[system] = parent
        if parent in completion_parents:
            old_by_parent[parent].append(system)

    assert set(old_by_parent) == set(completion_parents)
    completion_old_systems = tuple(
        system
        for parent in sorted(completion_parents)
        for system in old_by_parent[parent]
    )
    refined = pd.refine_systems(completion_old_systems, strata2, strata3)

    child_map = pd.refinement_map(strata2, strata3)
    new_to_old: dict[int, int] = {}
    for old_index, children in enumerate(child_map):
        for new_index in children:
            assert new_index not in new_to_old
            new_to_old[new_index] = old_index

    local: dict[
        tuple[int, ...],
        list[tuple[tuple[int, ...], Task]],
    ] = defaultdict(list)
    for child in refined:
        parent_system = tuple(new_to_old[index] for index in child)
        parent = parent_of_old[parent_system]
        assert parent in completion_parents
        task = pd.first_witness(child, 3, ratios3, strata3)[0]
        local[parent].append((child, task))

    assert set(local) == set(completion_parents)
    return ratios3, strata3, local


def _unique_raw_records(
    entries: tuple[tuple[tuple[int, ...], Task], ...],
    selected_features: tuple[int, ...],
    ratios3: tuple[Fraction, ...],
    strata3,
):
    """Compress child systems to raw selected-wall keys with multiplicities."""

    task_by_key: dict[RawKey, Task] = {}
    weight_by_key: dict[RawKey, int] = defaultdict(int)
    for child, task in entries:
        signature = pd.full_signature(child, ratios3, strata3)
        key = tuple(signature[index] for index in selected_features)
        previous = task_by_key.get(key)
        if previous is not None:
            assert previous == task
        task_by_key[key] = task
        weight_by_key[key] += 1

    records = tuple(
        (key, task_by_key[key], weight_by_key[key])
        for key in sorted(task_by_key)
    )
    assert sum(weight for _key, _task, weight in records) == len(entries)
    return records


def _optimal_decoder(records):
    """Exact adaptive decision tree over the coordinates of a raw signature.

    Objective order is structural first: minimum internal tree nodes, then
    minimum worst depth, then minimum weighted path length.  Task leaves with the
    same value are later merged when counting the structural DAG.
    """

    coordinate_count = len(records[0][0])
    assert coordinate_count > 0

    @lru_cache(maxsize=None)
    def solve(indices: tuple[int, ...], remaining: tuple[int, ...]):
        tasks = {records[index][1] for index in indices}
        if len(tasks) == 1:
            task = next(iter(tasks))
            node = DecoderNode(task=task)
            return node, 0, 0, 0, 1

        best = None
        state_weight = sum(records[index][2] for index in indices)
        for coordinate in remaining:
            groups: dict[int, list[int]] = defaultdict(list)
            for index in indices:
                groups[records[index][0][coordinate]].append(index)
            if len(groups) <= 1:
                continue

            next_remaining = tuple(item for item in remaining if item != coordinate)
            children = []
            internal_nodes = 1
            worst_depth = 0
            weighted_depth = state_weight
            path_leaves = 0
            possible = True
            for value in sorted(groups):
                child_indices = tuple(groups[value])
                child_result = solve(child_indices, next_remaining)
                if child_result is None:
                    possible = False
                    break
                child, child_internal, child_worst, child_weighted, child_leaves = child_result
                children.append((value, child))
                internal_nodes += child_internal
                worst_depth = max(worst_depth, child_worst)
                weighted_depth += child_weighted
                path_leaves += child_leaves
            if not possible:
                continue

            node = DecoderNode(coordinate=coordinate, children=tuple(children))
            score = (
                internal_nodes,
                1 + worst_depth,
                weighted_depth,
                path_leaves,
                coordinate,
                repr(node),
            )
            candidate = (node, internal_nodes, 1 + worst_depth, weighted_depth, path_leaves)
            if best is None or score < best[0]:
                best = (score, candidate)

        assert best is not None, "raw completion signature failed to decode its task"
        return best[1]

    return solve(tuple(range(len(records))), tuple(range(coordinate_count)))


def _decode(node: DecoderNode, key: RawKey) -> Task:
    cursor = node
    while not cursor.is_leaf:
        assert cursor.coordinate is not None
        value = key[cursor.coordinate]
        branches = dict(cursor.children)
        assert value in branches
        cursor = branches[value]
    assert cursor.task is not None
    return cursor.task


def _unique_node_count(root: DecoderNode) -> int:
    nodes: set[DecoderNode] = set()

    def visit(node: DecoderNode) -> None:
        if node in nodes:
            return
        nodes.add(node)
        for _value, child in node.children:
            visit(child)

    visit(root)
    return len(nodes)


def analyze_residual_objectification() -> ResidualObjectificationAnalysis:
    base = lcr.analyze_center2_to_center3()
    ratios3, strata3, local = _reconstruct_local_completion_children(
        base.completion_required_parents
    )

    by_parent = {case.parent: case for case in base.completion_residual_cases}
    assert set(by_parent) == set(base.completion_required_parents)

    results = []
    for parent in sorted(base.completion_required_parents):
        completion = by_parent[parent]
        selected_features = tuple(
            _feature_index(coordinate, ratios3)
            for coordinate in completion.coordinates
        )
        entries = tuple(local[parent])
        records = _unique_raw_records(
            entries,
            selected_features,
            ratios3,
            strata3,
        )
        raw_class_count = len(records)
        task_count = len({task for _key, task, _weight in records})
        assert raw_class_count == completion.residual_class_count
        assert task_count == completion.semantic_count

        root, internal_nodes, worst_depth, weighted_depth, path_leaves = _optimal_decoder(records)
        for key, task, _weight in records:
            assert _decode(root, key) == task

        total_weight = sum(weight for _key, _task, weight in records)
        results.append(
            ResidualObjectificationCase(
                parent=parent,
                coordinate_count=completion.coordinate_count,
                child_system_count=len(entries),
                raw_class_count=raw_class_count,
                quotient_class_count=task_count,
                decoder_internal_nodes=internal_nodes,
                decoder_path_leaves=path_leaves,
                decoder_unique_nodes=_unique_node_count(root),
                decoder_worst_depth=worst_depth,
                decoder_weighted_depth=Fraction(weighted_depth, total_weight),
            )
        )

    result = ResidualObjectificationAnalysis(cases=tuple(results))
    assert len(result.cases) == 6
    assert len(result.over_refined_cases) == 2
    assert sorted(
        (case.raw_class_count, case.quotient_class_count)
        for case in result.over_refined_cases
    ) == [(11, 7), (13, 3)]
    return result


def main() -> None:
    analysis = analyze_residual_objectification()
    print("Phase 8C.2 task-relative residual objectification")
    for case in analysis.cases:
        print(f"  parent:                 {case.parent}")
        print(f"    completion walls:     {case.coordinate_count}")
        print(f"    local children:       {case.child_system_count}")
        print(f"    raw sign classes:     {case.raw_class_count}")
        print(f"    task quotient classes:{case.quotient_class_count}")
        print(f"    decoder internals:    {case.decoder_internal_nodes}")
        print(f"    decoder path leaves:  {case.decoder_path_leaves}")
        print(f"    decoder DAG nodes:    {case.decoder_unique_nodes}")
        print(f"    decoder worst depth:  {case.decoder_worst_depth}")
        print(f"    weighted mean depth:  {float(case.decoder_weighted_depth):.6f}")
        print(f"    raw over-refined:     {case.over_refined_raw_signature}")


if __name__ == "__main__":
    main()
