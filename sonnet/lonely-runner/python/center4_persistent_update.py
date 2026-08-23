"""Phase 9D: materialize and place the center-4 persistent representation.

Phase 9C discovers, rather than receives, a single common minimum completion
predicate for all seven branching cells: u4/u3 ? 19/11.  This script appends
that process-generated predicate to the entire Phase-8E 28-predicate language,
refines the exact closure provenance accordingly, assigns the certified
center-4 task semantics, and rebuilds the task decision geometry over the joint
29-predicate representation.

The purpose is to distinguish representation content from placement again at the
next contact layer.  No fresh center-4 decision tree or full global center-4
arrangement is supplied.

``build_center4_persistent_cells`` is intentionally research-local.  It exposes
the certified center-4 persistent state so the next contact layer can continue
from the representation actually constructed here rather than reconstructing a
fresh center-4 arrangement.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import center4_minimal_completion as completion
import center4_semantic_redteam as semantic
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


@dataclass(frozen=True)
class Center4PersistentUpdate:
    center3_cells: int
    center3_tasks: int
    center3_tree_nodes: int
    center3_internal_nodes: int
    center3_dag_nodes: int
    center3_peak: int
    center3_worst: int
    center3_weighted_depth: int
    completion_coordinate: object
    center4_cells: int
    center4_tasks: int
    center4_closure_atoms: int
    center4_provenance_atoms: int
    center4_tree_nodes: int
    center4_internal_nodes: int
    center4_dag_nodes: int
    center4_peak: int
    center4_worst: int
    center4_weighted_depth: int
    center4_widths: tuple[int, ...]
    new_wall_internal_nodes: int
    cross_parent_new_wall_nodes: int
    earliest_new_wall_depth: int | None


def _sign(values: tuple[int, int, int, int], coordinate) -> int:
    first, second = coordinate.pair
    ratio = Fraction(values[second], values[first])
    return -1 if ratio < coordinate.ratio else (1 if ratio > coordinate.ratio else 0)


def _usage_weights(old_relevant, center3_walls, cells, extra_wall=None):
    ratios2 = pd.contact_ratios(2)
    all_walls2 = tuple(
        (i, j, ratio)
        for i, j in pd.PAIRS
        for ratio in ratios2
    )
    index = {cell.signature: position for position, cell in enumerate(cells)}
    weights = [0] * len(cells)
    for values in pd.integer_quadruples(8):
        full = pd.signs_for_quad(values, all_walls2)
        signature = tuple(full[item] for item in old_relevant)
        signature += tuple(_sign(values, wall) for wall in center3_walls)
        if extra_wall is not None:
            signature += (_sign(values, extra_wall),)
        weights[index[signature]] += 1
    assert sum(weights) == 55
    return tuple(weights)


def _tree_metrics(cells, weights):
    task_values = sorted({cell.task for cell in cells}, key=repr)
    task_id = {task: index for index, task in enumerate(task_values)}
    signatures = tuple(cell.signature for cell in cells)
    task_ids = tuple(task_id[cell.task] for cell in cells)
    tree, cost = pd.build_tree(signatures, task_ids, weights)
    histories = tuple(pd.tree_history(tree, signature) for signature in signatures)
    widths = pd.widths(histories)
    assert sum(widths) == cost[1]
    return tree, cost, widths, signatures, len(task_values)


def _new_wall_placement(tree, signatures, old_length: int):
    occurrences = 0
    cross_parent = 0
    earliest = None

    def visit(node, item_indices, depth):
        nonlocal occurrences, cross_parent, earliest
        if node.predicate is None:
            return
        groups = defaultdict(list)
        for index in item_indices:
            groups[signatures[index][node.predicate]].append(index)
        if node.predicate == old_length:
            occurrences += 1
            earliest = depth if earliest is None else min(earliest, depth)
            parent_count = len({signatures[index][:old_length] for index in item_indices})
            if parent_count > 1:
                cross_parent += 1
        for sign, child in node.children:
            visit(child, tuple(groups[sign]), depth + 1)

    visit(tree, tuple(range(len(signatures))), 0)
    return occurrences, cross_parent, earliest


def build_center4_persistent_cells():
    """Return the certified center-4 state built from the Phase-8E state.

    The return value is

        old center-2 relevant-coordinate indices,
        seven center-3 completion walls,
        center-3 persistent cells,
        the unique center-4 completion wall,
        center-4 persistent cells.

    No fresh center-4 arrangement is constructed.
    """

    old_relevant, center3_walls, center3_cells = pcc.build_center3_persistent_cells()
    pressure = pcc.detect_next_layer_pressure(
        center3_cells,
        old_center=3,
        new_center=4,
    )
    semantics = semantic.analyze_center4_semantic_redteam()
    semantic_by_signature = {case.signature: case for case in semantics.cases}

    completion_result = completion.analyze_center4_minimal_completion()
    selected_sets = {case.selected_coordinates for case in completion_result.cases}
    assert len(selected_sets) == 1
    selected = next(iter(selected_sets))
    assert len(selected) == 1
    new_wall = selected[0]
    assert new_wall.pair == (2, 3)
    assert new_wall.ratio == Fraction(19, 11)
    assert all(case.new_center4_coordinates == selected for case in completion_result.cases)
    assert all(not case.latent_older_coordinates for case in completion_result.cases)

    atom_groups = defaultdict(list)
    provenance = defaultdict(int)
    task_by_signature = {}

    for cell in center3_cells:
        case = semantic_by_signature.get(cell.signature)
        for atom in cell.atoms:
            variants = pcc._refine_closure_by_walls(atom, (new_wall,))
            for key, closure in variants.items():
                sign = key[0]
                signature4 = cell.signature + (sign,)

                if cell.signature in pressure.stable:
                    task = cell.task
                elif cell.signature in pressure.nonbranching_pressure:
                    assert case is not None and case.task_count == 1
                    task = case.new_tasks[0]
                else:
                    assert cell.signature in pressure.completion_pressure
                    expansion = semantic.expand_first_witness(closure, max_center=4)
                    assert len(expansion.tasks) == 1
                    task = next(iter(expansion.tasks))

                previous = task_by_signature.get(signature4)
                if previous is not None:
                    assert previous == task
                task_by_signature[signature4] = task
                atom_groups[signature4].append(closure)
                provenance[signature4] += 1

    cells4 = tuple(
        pcc.PersistentConstraintCell(
            signature=signature,
            task=task_by_signature[signature],
            atoms=tuple(dict.fromkeys(atom_groups[signature])),
            provenance_count=provenance[signature],
        )
        for signature in sorted(atom_groups)
    )
    assert len(cells4) == 3_067
    assert len({cell.task for cell in cells4}) == 81

    return old_relevant, center3_walls, center3_cells, new_wall, cells4


def analyze_center4_persistent_update() -> Center4PersistentUpdate:
    (
        old_relevant,
        center3_walls,
        center3_cells,
        new_wall,
        cells4,
    ) = build_center4_persistent_cells()

    # Freeze the center-3 baseline from the same persistent-cell artifact.
    weights3 = _usage_weights(old_relevant, center3_walls, center3_cells)
    tree3, cost3, widths3, signatures3, tasks3 = _tree_metrics(center3_cells, weights3)
    del tree3, signatures3
    assert cost3 == (135, 376, 10, 125)
    assert max(widths3) == 72
    assert tasks3 == 75

    weights4 = _usage_weights(old_relevant, center3_walls, cells4, new_wall)
    tree4, cost4, widths4, signatures4, tasks4 = _tree_metrics(cells4, weights4)
    new_nodes, cross_nodes, earliest = _new_wall_placement(
        tree4,
        signatures4,
        old_length=len(center3_cells[0].signature),
    )

    return Center4PersistentUpdate(
        center3_cells=len(center3_cells),
        center3_tasks=tasks3,
        center3_tree_nodes=cost3[1],
        center3_internal_nodes=cost3[3],
        center3_dag_nodes=cost3[3] + tasks3,
        center3_peak=max(widths3),
        center3_worst=cost3[2],
        center3_weighted_depth=cost3[0],
        completion_coordinate=new_wall,
        center4_cells=len(cells4),
        center4_tasks=tasks4,
        center4_closure_atoms=sum(len(cell.atoms) for cell in cells4),
        center4_provenance_atoms=sum(cell.provenance_count for cell in cells4),
        center4_tree_nodes=cost4[1],
        center4_internal_nodes=cost4[3],
        center4_dag_nodes=cost4[3] + tasks4,
        center4_peak=max(widths4),
        center4_worst=cost4[2],
        center4_weighted_depth=cost4[0],
        center4_widths=widths4,
        new_wall_internal_nodes=new_nodes,
        cross_parent_new_wall_nodes=cross_nodes,
        earliest_new_wall_depth=earliest,
    )


def main() -> None:
    result = analyze_center4_persistent_update()
    wall = result.completion_coordinate
    print("Phase 9D center4 persistent update")
    print("  center3 baseline")
    print(f"    cells / tasks:           {result.center3_cells} / {result.center3_tasks}")
    print(f"    tree / internal / DAG:   {result.center3_tree_nodes} / {result.center3_internal_nodes} / {result.center3_dag_nodes}")
    print(f"    peak / worst / weighted: {result.center3_peak} / {result.center3_worst} / {result.center3_weighted_depth}")
    print("  discovered center4 primitive")
    print(f"    u{wall.pair[1]+1}/u{wall.pair[0]+1} ? {wall.ratio}")
    print("  center4 joint representation")
    print(f"    cells / tasks:           {result.center4_cells} / {result.center4_tasks}")
    print(f"    closure / provenance:    {result.center4_closure_atoms} / {result.center4_provenance_atoms}")
    print(f"    tree / internal / DAG:   {result.center4_tree_nodes} / {result.center4_internal_nodes} / {result.center4_dag_nodes}")
    print(f"    peak / worst / weighted: {result.center4_peak} / {result.center4_worst} / {result.center4_weighted_depth}")
    print(f"    widths:                  {result.center4_widths}")
    print(f"    new-wall nodes:          {result.new_wall_internal_nodes}")
    print(f"    cross-parent new nodes:  {result.cross_parent_new_wall_nodes}")
    print(f"    earliest new-wall depth: {result.earliest_new_wall_depth}")


if __name__ == "__main__":
    main()
