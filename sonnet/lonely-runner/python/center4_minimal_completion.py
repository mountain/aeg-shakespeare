"""Phase 9C: minimum task-separating supports for seven center-4 completions.

Phase 9B identifies seven genuinely branching persistent cells and records every
collision wall encountered by its lazy exact first-witness oracle.  This script
does not treat that encountered union as minimal.

For one completion cell, refine each exact closure atom only by the encountered
wall union, enumerate the resulting feasible ternary wall-sign records, and ask
the already-certified first-witness oracle for the unique task of each refined
record.  Then brute-force every wall subset (at most ten candidate walls in the
current bounded cases) and choose the minimum-cardinality subset whose projected
sign record uniquely determines task semantics.

The selected support is classified into genuinely new center-4 walls and latent
older walls.  This directly tests whether future completion can be generated
from the new process layer alone, or whether a task-minimal completion also
needs distinctions carried only by persistent constraint provenance.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

import center4_semantic_redteam as semantic
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


Task = tuple[object, ...]


@dataclass(frozen=True)
class Center4CompletionSupport:
    signature: tuple[int, ...]
    task_count: int
    candidate_wall_count: int
    raw_class_count: int
    minimum_wall_count: int
    minimum_class_count: int
    selected_coordinates: tuple[object, ...]
    new_center4_coordinates: tuple[object, ...]
    latent_older_coordinates: tuple[object, ...]
    total_record_weight: int


@dataclass(frozen=True)
class Center4CompletionAnalysis:
    cases: tuple[Center4CompletionSupport, ...]


def _minimum_task_support(records, coordinate_count: int):
    """Lexicographically first minimum coordinate subset separating tasks."""

    for size in range(coordinate_count + 1):
        for subset in combinations(range(coordinate_count), size):
            seen = {}
            valid = True
            for key, task, _weight in records:
                projection = tuple(key[index] for index in subset)
                previous = seen.get(projection)
                if previous is not None and previous != task:
                    valid = False
                    break
                seen[projection] = task
            if valid:
                return subset
    raise AssertionError("complete wall record must separate exact task semantics")


def analyze_center4_minimal_completion() -> Center4CompletionAnalysis:
    semantic_result = semantic.analyze_center4_semantic_redteam()
    cells, _pressure = pcc.probe_center3_to_center4_pressure()
    by_signature = {cell.signature: cell for cell in cells}
    new_ratio_set = set(pd.contact_ratios(4)) - set(pd.contact_ratios(3))

    output = []
    for case in semantic_result.branching_cases:
        cell = by_signature[case.signature]
        coordinates = tuple(case.queried_walls)
        assert 1 <= len(coordinates) <= 10

        task_for_key = {}
        weight_for_record = defaultdict(int)
        for atom in cell.atoms:
            variants = pcc._refine_closure_by_walls(atom, coordinates)
            for key, closure in variants.items():
                expansion = semantic.expand_first_witness(closure, max_center=4)
                assert len(expansion.tasks) == 1
                # Every wall that the lazy oracle needed in the unrefined atom
                # is already fixed by this complete candidate-wall record.
                assert not expansion.queried_walls
                task = next(iter(expansion.tasks))
                previous = task_for_key.get(key)
                if previous is not None:
                    assert previous == task
                task_for_key[key] = task
                weight_for_record[(key, task)] += 1

        records = tuple(
            (key, task, weight)
            for (key, task), weight in sorted(
                weight_for_record.items(),
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
            coordinate
            for coordinate in selected
            if coordinate.ratio in new_ratio_set
        )
        latent_selected = tuple(
            coordinate
            for coordinate in selected
            if coordinate.ratio not in new_ratio_set
        )

        output.append(
            Center4CompletionSupport(
                signature=case.signature,
                task_count=case.task_count,
                candidate_wall_count=len(coordinates),
                raw_class_count=len(task_for_key),
                minimum_wall_count=len(selected),
                minimum_class_count=len(projected),
                selected_coordinates=selected,
                new_center4_coordinates=new_selected,
                latent_older_coordinates=latent_selected,
                total_record_weight=sum(weight for _key, _task, weight in records),
            )
        )

    result = Center4CompletionAnalysis(cases=tuple(output))
    assert len(result.cases) == 7
    return result


def main() -> None:
    result = analyze_center4_minimal_completion()
    print("Phase 9C minimum center4 completion supports")
    print("  cases:", len(result.cases))
    print("  minimum wall counts:", sorted(case.minimum_wall_count for case in result.cases))
    print("  new/latent selected counts:", sorted(
        (len(case.new_center4_coordinates), len(case.latent_older_coordinates))
        for case in result.cases
    ))
    for case in result.cases:
        print(f"  {case.signature}")
        print(f"    tasks:                 {case.task_count}")
        print(f"    candidate walls:       {case.candidate_wall_count}")
        print(f"    complete raw classes:  {case.raw_class_count}")
        print(f"    minimum walls:         {case.minimum_wall_count}")
        print(f"    minimum sign classes:  {case.minimum_class_count}")
        print(f"    total exact records:   {case.total_record_weight}")
        print(f"    selected new/latent:   {len(case.new_center4_coordinates)} / {len(case.latent_older_coordinates)}")
        for coordinate in case.selected_coordinates:
            layer = "new@center4" if coordinate in case.new_center4_coordinates else "latent<=center3"
            print(
                f"      u{coordinate.pair[1]+1}/u{coordinate.pair[0]+1} ? {coordinate.ratio} [{layer}]"
            )


if __name__ == "__main__":
    main()
