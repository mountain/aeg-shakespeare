"""Phase 10A/B: frozen center-4 -> center-5 self-growing representation replay.

This script continues from the *constructed* Phase-9D center-4 persistent state.
It does not reconstruct a fresh center-4 arrangement and does not receive any
center-5 task labels or target wall list.

The Phase-9A next-layer pressure detector is applied unchanged.  Only affected
persistent cells are then reopened.  Their center-5 first-witness semantics are
computed by the already red-teamed lazy event-order oracle.  For every genuinely
branching cell, the union of collision walls actually encountered by that oracle
is treated only as a candidate grammar; exact conflict-cover minimization then
finds a minimum-cardinality wall-sign support whose values determine the task.

The experiment therefore asks whether the representation-growth pattern found
at centers 3 and 4 persists one layer further:

    current persistent representation
        -> sparse pressure
        -> exact local semantic branching
        -> minimum process-generated completion support.

No full center-5 wall arrangement, fresh center-5 decision tree, K=13 data, or
hand-supplied expected primitive is used.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache

import center4_persistent_update as center4
import center4_semantic_redteam as semantic
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


Task = tuple[object, ...]


@dataclass(frozen=True)
class Center5SemanticCase:
    signature: tuple[int, ...]
    phase10_role: str
    old_task: Task
    new_tasks: tuple[Task, ...]
    atom_count: int
    semantic_leaf_count: int
    queried_walls: tuple[object, ...]
    new_center5_walls: tuple[object, ...]
    latent_older_walls: tuple[object, ...]

    @property
    def task_count(self) -> int:
        return len(self.new_tasks)

    @property
    def same_boundary_and_mode(self) -> bool:
        return self.task_count == 1 and self.old_task[1:] == self.new_tasks[0][1:]


@dataclass(frozen=True)
class Center5CompletionSupport:
    signature: tuple[int, ...]
    task_count: int
    candidate_wall_count: int
    raw_class_count: int
    minimum_wall_count: int
    minimum_class_count: int
    selected_coordinates: tuple[object, ...]
    new_center5_coordinates: tuple[object, ...]
    latent_older_coordinates: tuple[object, ...]
    total_record_weight: int


@dataclass(frozen=True)
class Center5ScalingReplay:
    current_cells: int
    current_tasks: int
    current_closure_atoms: int
    stable_count: int
    nonbranching_pressure_count: int
    completion_pressure_count: int
    uniform_count: int
    branching_count: int
    semantic_cases: tuple[Center5SemanticCase, ...]
    completion_cases: tuple[Center5CompletionSupport, ...]


def _coordinate_key(item):
    return item.pair, item.ratio, getattr(item, "new_at_center3", False)


def _minimum_task_support(records, coordinate_count: int) -> tuple[int, ...]:
    """Exact minimum conflict cover over a finite wall-sign language."""

    conflicts = tuple(
        (left, right)
        for left in range(len(records))
        for right in range(left + 1, len(records))
        if records[left][1] != records[right][1]
    )
    if not conflicts:
        return ()

    full_mask = (1 << len(conflicts)) - 1
    coverage_to_coordinate: dict[int, int] = {}
    for coordinate in range(coordinate_count):
        coverage = 0
        for conflict_index, (left, right) in enumerate(conflicts):
            if records[left][0][coordinate] != records[right][0][coordinate]:
                coverage |= 1 << conflict_index
        if coverage == 0:
            continue
        previous = coverage_to_coordinate.get(coverage)
        if previous is None or coordinate < previous:
            coverage_to_coordinate[coverage] = coordinate

    coordinate_masks = tuple(
        sorted(
            (coordinate, coverage)
            for coverage, coordinate in coverage_to_coordinate.items()
        )
    )
    assert coordinate_masks

    coverers = {}
    for conflict_index in range(len(conflicts)):
        bit = 1 << conflict_index
        options = tuple(
            (coordinate, coverage)
            for coordinate, coverage in coordinate_masks
            if coverage & bit
        )
        assert options
        coverers[conflict_index] = options

    @lru_cache(maxsize=None)
    def solve(uncovered: int) -> tuple[int, ...]:
        if uncovered == 0:
            return ()
        remaining = [
            index
            for index in range(len(conflicts))
            if uncovered & (1 << index)
        ]
        pivot = min(
            remaining,
            key=lambda index: sum(
                bool(coverage & uncovered)
                for _coordinate, coverage in coverers[index]
            ),
        )
        best = None
        for coordinate, coverage in coverers[pivot]:
            tail = solve(uncovered & ~coverage)
            candidate = tuple(sorted((coordinate, *tail)))
            if best is None or (len(candidate), candidate) < (len(best), best):
                best = candidate
        assert best is not None
        return best

    selected = solve(full_mask)

    # Local deletion certificate: every selected coordinate is necessary inside
    # this selected support.
    for removed in selected:
        reduced = tuple(item for item in selected if item != removed)
        seen = {}
        conflict = False
        for key, task, _weight in records:
            projection = tuple(key[index] for index in reduced)
            previous = seen.get(projection)
            if previous is not None and previous != task:
                conflict = True
                break
            seen[projection] = task
        assert conflict

    return selected


def _semantic_cases(cells, pressure) -> tuple[Center5SemanticCase, ...]:
    by_signature = {cell.signature: cell for cell in cells}
    new_ratio_set = set(pd.contact_ratios(5)) - set(pd.contact_ratios(4))
    output = []

    for signature in sorted(pressure.affected):
        cell = by_signature[signature]
        tasks = set()
        walls = set()
        leaf_count = 0
        for atom in cell.atoms:
            expansion = semantic.expand_first_witness(atom, max_center=5)
            tasks.update(expansion.tasks)
            walls.update(expansion.queried_walls)
            leaf_count += expansion.leaf_count

        role = (
            "nonbranching-pressure"
            if signature in pressure.nonbranching_pressure
            else "completion-pressure"
        )
        new_walls = tuple(
            sorted(
                (wall for wall in walls if wall.ratio in new_ratio_set),
                key=_coordinate_key,
            )
        )
        latent = tuple(
            sorted(
                (wall for wall in walls if wall.ratio not in new_ratio_set),
                key=_coordinate_key,
            )
        )
        output.append(
            Center5SemanticCase(
                signature=signature,
                phase10_role=role,
                old_task=cell.task,
                new_tasks=tuple(sorted(tasks, key=repr)),
                atom_count=len(cell.atoms),
                semantic_leaf_count=leaf_count,
                queried_walls=tuple(sorted(walls, key=_coordinate_key)),
                new_center5_walls=new_walls,
                latent_older_walls=latent,
            )
        )

    return tuple(output)


def _minimum_completion_cases(cells, semantic_cases):
    by_signature = {cell.signature: cell for cell in cells}
    new_ratio_set = set(pd.contact_ratios(5)) - set(pd.contact_ratios(4))
    output = []

    for case in semantic_cases:
        if case.task_count <= 1:
            continue
        cell = by_signature[case.signature]
        coordinates = case.queried_walls
        assert coordinates

        task_for_key = {}
        record_weights = defaultdict(int)
        for atom in cell.atoms:
            variants = pcc._refine_closure_by_walls(atom, coordinates)
            for key, closure in variants.items():
                expansion = semantic.expand_first_witness(closure, max_center=5)
                assert len(expansion.tasks) == 1
                assert not expansion.queried_walls
                task = next(iter(expansion.tasks))
                previous = task_for_key.get(key)
                if previous is not None:
                    assert previous == task
                task_for_key[key] = task
                record_weights[(key, task)] += 1

        records = tuple(
            (key, task, weight)
            for (key, task), weight in sorted(
                record_weights.items(),
                key=lambda item: (repr(item[0][0]), repr(item[0][1])),
            )
        )
        assert {task for _key, task, _weight in records} == set(case.new_tasks)

        selected_indices = _minimum_task_support(records, len(coordinates))
        selected = tuple(coordinates[index] for index in selected_indices)
        projected = {}
        for key, task, _weight in records:
            projection = tuple(key[index] for index in selected_indices)
            previous = projected.get(projection)
            if previous is not None:
                assert previous == task
            projected[projection] = task

        new_selected = tuple(
            coordinate for coordinate in selected if coordinate.ratio in new_ratio_set
        )
        latent_selected = tuple(
            coordinate for coordinate in selected if coordinate.ratio not in new_ratio_set
        )
        output.append(
            Center5CompletionSupport(
                signature=case.signature,
                task_count=case.task_count,
                candidate_wall_count=len(coordinates),
                raw_class_count=len(task_for_key),
                minimum_wall_count=len(selected),
                minimum_class_count=len(projected),
                selected_coordinates=selected,
                new_center5_coordinates=new_selected,
                latent_older_coordinates=latent_selected,
                total_record_weight=sum(weight for _key, _task, weight in records),
            )
        )

    return tuple(output)


def analyze_center5_scaling_replay() -> Center5ScalingReplay:
    (
        _old_relevant,
        _center3_walls,
        _center3_cells,
        _center4_wall,
        cells4,
    ) = center4.build_center4_persistent_cells()

    pressure = pcc.detect_next_layer_pressure(
        cells4,
        old_center=4,
        new_center=5,
    )
    cases = _semantic_cases(cells4, pressure)
    uniform = tuple(case for case in cases if case.task_count == 1)
    branching = tuple(case for case in cases if case.task_count > 1)

    assert len(cases) == len(pressure.affected)
    assert all(
        case.phase10_role == "nonbranching-pressure"
        for case in uniform
        if case.signature in pressure.nonbranching_pressure
    )
    assert all(
        case.phase10_role == "completion-pressure"
        for case in branching
        if case.signature in pressure.completion_pressure
    )

    completion_cases = _minimum_completion_cases(cells4, cases)
    assert len(completion_cases) == len(branching)

    return Center5ScalingReplay(
        current_cells=len(cells4),
        current_tasks=len({cell.task for cell in cells4}),
        current_closure_atoms=sum(len(cell.atoms) for cell in cells4),
        stable_count=len(pressure.stable),
        nonbranching_pressure_count=len(pressure.nonbranching_pressure),
        completion_pressure_count=len(pressure.completion_pressure),
        uniform_count=len(uniform),
        branching_count=len(branching),
        semantic_cases=cases,
        completion_cases=completion_cases,
    )


def main() -> None:
    result = analyze_center5_scaling_replay()
    affected = result.nonbranching_pressure_count + result.completion_pressure_count
    print("Phase 10A/B frozen center4 -> center5 replay")
    print("  current center4 representation")
    print(f"    cells / tasks / closure atoms: {result.current_cells} / {result.current_tasks} / {result.current_closure_atoms}")
    print("  unchanged next-layer detector")
    print(f"    stable:                       {result.stable_count}")
    print(f"    nonbranching pressure:        {result.nonbranching_pressure_count}")
    print(f"    completion pressure:          {result.completion_pressure_count}")
    print(f"    affected:                     {affected}")
    print(f"    affected fraction:            {affected / result.current_cells:.6%}")
    print("  exact local semantics")
    print(f"    uniform / branching:          {result.uniform_count} / {result.branching_count}")
    print("    branching task multiplicities:", sorted(
        case.task_count for case in result.semantic_cases if case.task_count > 1
    ))
    print("  minimum completion")
    print("    minimum wall counts:", sorted(
        case.minimum_wall_count for case in result.completion_cases
    ))
    print("    selected new/latent counts:", sorted(
        (len(case.new_center5_coordinates), len(case.latent_older_coordinates))
        for case in result.completion_cases
    ))
    selected_union = tuple(
        sorted(
            {
                coordinate
                for case in result.completion_cases
                for coordinate in case.selected_coordinates
            },
            key=_coordinate_key,
        )
    )
    print(f"    global selected union:         {len(selected_union)}")
    for coordinate in selected_union:
        is_new = any(
            coordinate in case.new_center5_coordinates
            for case in result.completion_cases
        )
        layer = "new@center5" if is_new else "latent<=center4"
        print(
            f"      u{coordinate.pair[1]+1}/u{coordinate.pair[0]+1} ? {coordinate.ratio} [{layer}]"
        )
    for case in result.semantic_cases:
        print(f"  {case.phase10_role}: {case.signature}")
        print(f"    old task:             {case.old_task}")
        print(f"    new task count:       {case.task_count}")
        print(f"    same boundary/mode:   {case.same_boundary_and_mode}")
        if case.task_count == 1:
            print(f"    event-rank shift:     {case.new_tasks[0][0] - case.old_task[0]}")
        print(f"    closure atoms:        {case.atom_count}")
        print(f"    semantic leaves:      {case.semantic_leaf_count}")
        print(f"    queried walls:        {len(case.queried_walls)}")
        print(f"    new / latent queried: {len(case.new_center5_walls)} / {len(case.latent_older_walls)}")


if __name__ == "__main__":
    main()
