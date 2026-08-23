"""Phase 10A: frozen-rule center-4 -> center-5 pressure probe.

Reconstruct the certified Phase-9D center-4 persistent state from the same
process-generated 29-predicate language, then apply the unchanged generic
next-layer pressure detector to the center-5 contact layer.  No center-5 task
labels, full center-5 arrangement, or center-5 completion wall is supplied.
"""

from __future__ import annotations

from collections import defaultdict

import center4_minimal_completion as completion
import center4_semantic_redteam as semantic
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


def build_center4_persistent_cells():
    old_relevant, center3_walls, center3_cells = pcc.build_center3_persistent_cells()
    pressure4 = pcc.detect_next_layer_pressure(
        center3_cells,
        old_center=3,
        new_center=4,
    )
    semantics4 = semantic.analyze_center4_semantic_redteam()
    semantic_by_signature = {case.signature: case for case in semantics4.cases}

    minimum = completion.analyze_center4_minimal_completion()
    supports = {case.selected_coordinates for case in minimum.cases}
    assert len(supports) == 1
    support = next(iter(supports))
    assert len(support) == 1
    wall = support[0]

    atom_groups = defaultdict(list)
    provenance = defaultdict(int)
    task_by_signature = {}

    for cell in center3_cells:
        case = semantic_by_signature.get(cell.signature)
        for atom in cell.atoms:
            variants = pcc._refine_closure_by_walls(atom, (wall,))
            for key, closure in variants.items():
                signature = cell.signature + (key[0],)
                if cell.signature in pressure4.stable:
                    task = cell.task
                elif cell.signature in pressure4.nonbranching_pressure:
                    assert case is not None and case.task_count == 1
                    task = case.new_tasks[0]
                else:
                    assert cell.signature in pressure4.completion_pressure
                    expansion = semantic.expand_first_witness(closure, max_center=4)
                    assert len(expansion.tasks) == 1
                    task = next(iter(expansion.tasks))

                previous = task_by_signature.get(signature)
                if previous is not None:
                    assert previous == task
                task_by_signature[signature] = task
                atom_groups[signature].append(closure)
                provenance[signature] += 1

    cells = tuple(
        pcc.PersistentConstraintCell(
            signature=signature,
            task=task_by_signature[signature],
            atoms=tuple(dict.fromkeys(atom_groups[signature])),
            provenance_count=provenance[signature],
        )
        for signature in sorted(atom_groups)
    )

    assert len(cells) == 3_067
    assert len({cell.task for cell in cells}) == 81
    assert sum(len(cell.atoms) for cell in cells) == 14_967
    assert sum(cell.provenance_count for cell in cells) == 14_967
    return old_relevant, center3_walls + (wall,), cells


def analyze_center5_pressure():
    _old, _generated, cells = build_center4_persistent_cells()
    pressure = pcc.detect_next_layer_pressure(
        cells,
        old_center=4,
        new_center=5,
    )
    return cells, pressure


def main() -> None:
    cells, pressure = analyze_center5_pressure()
    print("Phase 10A frozen-rule center4 -> center5 pressure")
    print(f"  current persistent cells:          {len(cells)}")
    print(f"  current task semantics:            {len({cell.task for cell in cells})}")
    print(f"  exact closure atoms:               {sum(len(cell.atoms) for cell in cells)}")
    print(f"  stable:                            {len(pressure.stable)}")
    print(f"  nonbranching pressure:             {len(pressure.nonbranching_pressure)}")
    print(f"  completion pressure:               {len(pressure.completion_pressure)}")
    print(f"  affected total:                    {len(pressure.affected)}")
    print(f"  affected fraction:                 {len(pressure.affected) / len(cells):.8f}")


if __name__ == "__main__":
    main()
