"""Phase 8D: attach objectified completion decoders to the frozen center-2 tree.

The construction is intentionally conservative.  It reuses the exact center-2
68-label persistent Hauffman tree unchanged, treats the two Phase-8B history
reindex cases as decoder/provenance updates with zero new wall queries, and
replaces only the six genuine completion leaves by their Phase-8C.2 local
adaptive decoders.

Terminal nodes with the same final first-witness task are shared when counting
the persistent DAG.  No additional cross-parent sharing of internal decoder
subgraphs is assumed, so the resulting node count is an explicit auditable
construction rather than an optimistic graph-minimization claim.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import local_contact_refinement as lcr
import pair_difference_refinement as pd
import residual_objectification as ro


@dataclass(frozen=True)
class PersistentDagIncrementAnalysis:
    old_persistent_labels: int
    old_tree_nodes: int
    old_internal_nodes: int
    old_terminal_merged_dag_nodes: int
    old_peak_frontier: int
    old_worst_depth: int
    old_weighted_depth: int
    updated_semantics: int
    new_completion_internal_nodes: int
    updated_tree_nodes: int
    updated_internal_nodes: int
    updated_terminal_merged_dag_nodes: int
    incremental_tree_nodes: int
    incremental_dag_nodes: int
    updated_peak_frontier: int
    updated_worst_depth: int
    updated_widths: tuple[int, ...]
    training_completion_inputs: int
    training_history_reindex_inputs: int
    training_extra_queries: int
    training_updated_depth: int

    @property
    def training_incremental_mean_depth(self) -> Fraction:
        return Fraction(self.training_extra_queries, 55)

    @property
    def training_updated_mean_depth(self) -> Fraction:
        return Fraction(self.training_updated_depth, 55)


def _center2_persistent_tree(base: lcr.LocalRefinementAnalysis):
    ratios2 = pd.contact_ratios(2)
    strata2 = pd.strata(ratios2)
    systems2 = pd.enumerate_systems(strata2)
    assert len(systems2) == 5_823

    tasks2 = tuple(
        pd.first_witness(system, 2, ratios2, strata2)[0]
        for system in systems2
    )
    signatures2 = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in systems2
    )
    relevant2 = pd.relevant_walls(systems2, tasks2, ratios2)
    assert len(relevant2) == 21

    reduced_tasks: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
    for signature, task in zip(signatures2, tasks2):
        parent = tuple(signature[index] for index in relevant2)
        reduced_tasks[parent].add(task)
    assert len(reduced_tasks) == 849
    assert all(len(tasks) == 1 for tasks in reduced_tasks.values())
    assert set(base.affected_parents) <= set(reduced_tasks)

    task_by_parent = {
        parent: next(iter(tasks))
        for parent, tasks in reduced_tasks.items()
    }
    persistent_label_by_parent = {
        parent: (
            ("residual", parent)
            if parent in base.affected_parents
            else ("task", task_by_parent[parent])
        )
        for parent in reduced_tasks
    }
    labels = sorted(set(persistent_label_by_parent.values()), key=repr)
    assert len(labels) == 68
    label_id = {label: index for index, label in enumerate(labels)}

    reduced_signatures = tuple(reduced_tasks)
    item_labels = tuple(
        label_id[persistent_label_by_parent[parent]]
        for parent in reduced_signatures
    )
    reduced_index = {parent: index for index, parent in enumerate(reduced_signatures)}

    all_walls2 = tuple(
        (i, j, ratio)
        for i, j in pd.PAIRS
        for ratio in ratios2
    )
    relevant_walls2 = tuple(all_walls2[index] for index in relevant2)
    training = pd.integer_quadruples(8)
    assert len(training) == 55
    weights = [0] * len(reduced_signatures)
    parent_for_quad = {}
    for values in training:
        full = pd.signs_for_quad(values, all_walls2)
        parent = tuple(full[index] for index in relevant2)
        assert parent in reduced_index
        parent_for_quad[values] = parent
        weights[reduced_index[parent]] += 1

    tree, cost = pd.build_tree(
        reduced_signatures,
        item_labels,
        tuple(weights),
    )
    assert cost == (135, 328, 9, 109)
    assert relevant_walls2[tree.predicate] == (0, 3, Fraction(4))

    histories = {
        parent: tuple(("old", predicate, sign) for predicate, sign in pd.tree_history(tree, parent))
        for parent in reduced_signatures
    }
    widths = pd.widths(tuple(histories.values()))
    assert widths == (1, 3, 3, 9, 27, 48, 63, 69, 72, 33)

    return {
        "tree": tree,
        "cost": cost,
        "widths": widths,
        "task_by_parent": task_by_parent,
        "histories": histories,
        "training": training,
        "parent_for_quad": parent_for_quad,
    }


def _decoder_history(root: ro.DecoderNode, key: ro.RawKey):
    result = []
    node = root
    while not node.is_leaf:
        assert node.coordinate is not None
        value = key[node.coordinate]
        result.append((node.coordinate, value))
        node = dict(node.children)[value]
    assert node.task is not None
    return tuple(result), node.task


def _sign(values: tuple[int, int, int, int], coordinate: lcr.ResidualCoordinate) -> int:
    i, j = coordinate.pair
    ratio = Fraction(values[j], values[i])
    return -1 if ratio < coordinate.ratio else (1 if ratio > coordinate.ratio else 0)


def analyze_persistent_dag_increment() -> PersistentDagIncrementAnalysis:
    base = lcr.analyze_center2_to_center3()
    old = _center2_persistent_tree(base)

    ratios3, strata3, local = ro._reconstruct_local_completion_children(
        base.completion_required_parents
    )
    completion_by_parent = {
        case.parent: case
        for case in base.completion_residual_cases
    }

    decoders = {}
    raw_records = {}
    decoder_internal_total = 0
    decoder_path_leaf_total = 0
    for parent in sorted(base.completion_required_parents):
        completion = completion_by_parent[parent]
        selected_features = tuple(
            ro._feature_index(coordinate, ratios3)
            for coordinate in completion.coordinates
        )
        records = ro._unique_raw_records(
            tuple(local[parent]),
            selected_features,
            ratios3,
            strata3,
        )
        root, internal, worst, weighted, path_leaves = ro._optimal_decoder(records)
        del worst, weighted
        decoders[parent] = root
        raw_records[parent] = records
        decoder_internal_total += internal
        decoder_path_leaf_total += path_leaves

    assert decoder_internal_total == 16
    assert decoder_path_leaf_total == 38

    # Build the persistent updated prefix histories without expanding unrelated
    # center-3 sign states.  Stable and history-reindex parents reuse their old
    # paths exactly; completion parents append only locally required decoder
    # queries.  Parent identity is included in a local query token because this
    # construction does not assume cross-parent internal sharing.
    updated_histories = []
    final_tasks = set()
    reindex_new_task = {
        case.parent: case.new_task
        for case in base.history_reindex_cases
    }

    for parent in sorted(base.stable_parents):
        updated_histories.append(old["histories"][parent])
        final_tasks.add(old["task_by_parent"][parent])

    for parent in sorted(base.history_reindex_parents):
        updated_histories.append(old["histories"][parent])
        final_tasks.add(reindex_new_task[parent])

    for parent in sorted(base.completion_required_parents):
        root = decoders[parent]
        old_history = old["histories"][parent]
        for key, task, _weight in raw_records[parent]:
            local_history, decoded = _decoder_history(root, key)
            assert decoded == task
            appended = tuple(
                ("completion", parent, coordinate, sign)
                for coordinate, sign in local_history
            )
            updated_histories.append(old_history + appended)
            final_tasks.add(task)

    assert len(final_tasks) == 75
    updated_widths = pd.widths(tuple(updated_histories))
    updated_tree_nodes = sum(updated_widths)
    updated_worst_depth = len(updated_widths) - 1
    updated_peak = max(updated_widths)

    # A tree node count is the boundary volume.  Six old completion terminal
    # leaves are replaced by local decoder trees.  The history calculation is an
    # independent certificate of the same arithmetic.
    expected_tree_nodes = 328 - 6 + decoder_internal_total + decoder_path_leaf_total
    assert updated_tree_nodes == expected_tree_nodes

    updated_internal_nodes = 109 + decoder_internal_total
    assert updated_internal_nodes == 125

    # Terminal-merged persistent DAG: no internal cross-parent sharing is
    # assumed, but all equal final task terminals share one object.
    old_dag_nodes = 109 + 68
    updated_dag_nodes = updated_internal_nodes + len(final_tasks)

    # Exact incremental execution on the frozen 55-input usage distribution.
    completion_inputs = 0
    reindex_inputs = 0
    extra_queries = 0
    updated_depth = 0
    for values in old["training"]:
        parent = old["parent_for_quad"][values]
        old_depth = len(old["histories"][parent])
        local_depth = 0

        if parent in base.history_reindex_parents:
            reindex_inputs += 1
            predicted = reindex_new_task[parent]
        elif parent in base.completion_required_parents:
            completion_inputs += 1
            completion = completion_by_parent[parent]
            key = tuple(_sign(values, coordinate) for coordinate in completion.coordinates)
            history, predicted = _decoder_history(decoders[parent], key)
            local_depth = len(history)
        else:
            predicted = old["task_by_parent"][parent]

        actual = pd.direct_task(values)
        assert predicted == actual
        extra_queries += local_depth
        updated_depth += old_depth + local_depth

    assert updated_depth == 135 + extra_queries

    return PersistentDagIncrementAnalysis(
        old_persistent_labels=68,
        old_tree_nodes=328,
        old_internal_nodes=109,
        old_terminal_merged_dag_nodes=old_dag_nodes,
        old_peak_frontier=max(old["widths"]),
        old_worst_depth=len(old["widths"]) - 1,
        old_weighted_depth=135,
        updated_semantics=len(final_tasks),
        new_completion_internal_nodes=decoder_internal_total,
        updated_tree_nodes=updated_tree_nodes,
        updated_internal_nodes=updated_internal_nodes,
        updated_terminal_merged_dag_nodes=updated_dag_nodes,
        incremental_tree_nodes=updated_tree_nodes - 328,
        incremental_dag_nodes=updated_dag_nodes - old_dag_nodes,
        updated_peak_frontier=updated_peak,
        updated_worst_depth=updated_worst_depth,
        updated_widths=updated_widths,
        training_completion_inputs=completion_inputs,
        training_history_reindex_inputs=reindex_inputs,
        training_extra_queries=extra_queries,
        training_updated_depth=updated_depth,
    )


def main() -> None:
    result = analyze_persistent_dag_increment()
    print("Phase 8D persistent DAG increment")
    print("  center-2 persistent tree")
    print(f"    labels:                 {result.old_persistent_labels}")
    print(f"    tree nodes / internals: {result.old_tree_nodes} / {result.old_internal_nodes}")
    print(f"    terminal-merged DAG:    {result.old_terminal_merged_dag_nodes}")
    print(f"    peak / worst:           {result.old_peak_frontier} / {result.old_worst_depth}")
    print(f"    weighted depth (55):    {result.old_weighted_depth}")
    print("  center-3 persistent update")
    print(f"    final semantics:        {result.updated_semantics}")
    print(f"    new completion internals:{result.new_completion_internal_nodes}")
    print(f"    tree nodes / internals: {result.updated_tree_nodes} / {result.updated_internal_nodes}")
    print(f"    terminal-merged DAG:    {result.updated_terminal_merged_dag_nodes}")
    print(f"    incremental tree nodes: {result.incremental_tree_nodes}")
    print(f"    incremental DAG nodes:  {result.incremental_dag_nodes}")
    print(f"    peak / worst:           {result.updated_peak_frontier} / {result.updated_worst_depth}")
    print(f"    width profile:          {result.updated_widths}")
    print("  frozen 55-input execution")
    print(f"    completion inputs:      {result.training_completion_inputs}")
    print(f"    history-reindex inputs: {result.training_history_reindex_inputs}")
    print(f"    extra wall queries:     {result.training_extra_queries}")
    print(f"    updated weighted depth: {result.training_updated_depth}")
    print(f"    incremental mean depth: {float(result.training_incremental_mean_depth):.6f}")
    print(f"    updated mean depth:     {float(result.training_updated_mean_depth):.6f}")


if __name__ == "__main__":
    main()
