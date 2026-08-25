"""Phase 8D.2 probe: separate current-usage and refinement-aware placement weights.

All local representation semantics are frozen from Phases 8A--8D.  This script
changes only the ordering of the *old center-2 task-relevant walls* used to reach
the 68 persistent terminal labels.  The six Phase-8C.2 completion decoders are
then grafted unchanged.

Two distributions are mixed explicitly rather than conflated:

1. the historical 55-input current-task usage weights;
2. a continuation workload supported on the six completion parents, weighted by
   the number of locally realizable center-3 completion children below each
   parent (288 children in total).

For a mixing parameter lambda in [0,1], the old-tree search uses

    (1-lambda) * current_usage / 55
      + lambda * completion_child_mass / 288.

The resulting tree is evaluated under both distributions separately and after
attaching the frozen completion decoders.  This is a placement probe, not a new
completion search and not yet a proposed universal cost scalarization.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import local_contact_refinement as lcr
import pair_difference_refinement as pd
import residual_objectification as ro


@dataclass(frozen=True)
class PlacementCandidate:
    mixture: Fraction
    root_wall: tuple[int, int, Fraction]
    current_weighted_depth: int
    completion_old_path_depth: int
    completion_final_depth: int
    old_tree_nodes: int
    old_internal_nodes: int
    updated_tree_nodes: int
    updated_internal_nodes: int
    updated_peak: int
    updated_worst: int
    updated_widths: tuple[int, ...]

    @property
    def current_mean_depth(self) -> Fraction:
        return Fraction(self.current_weighted_depth, 55)

    @property
    def completion_mean_final_depth(self) -> Fraction:
        return Fraction(self.completion_final_depth, 288)


@dataclass(frozen=True)
class PlacementProbe:
    candidates: tuple[PlacementCandidate, ...]
    pareto: tuple[PlacementCandidate, ...]


def _dominates(left: PlacementCandidate, right: PlacementCandidate) -> bool:
    a = (
        left.current_weighted_depth,
        left.completion_final_depth,
        left.updated_tree_nodes,
        left.updated_peak,
        left.updated_worst,
    )
    b = (
        right.current_weighted_depth,
        right.completion_final_depth,
        right.updated_tree_nodes,
        right.updated_peak,
        right.updated_worst,
    )
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


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


def analyze_refinement_aware_placement() -> PlacementProbe:
    base = lcr.analyze_center2_to_center3()

    # Reconstruct only the center-2 persistent decision problem.
    ratios2 = pd.contact_ratios(2)
    strata2 = pd.strata(ratios2)
    systems2 = pd.enumerate_systems(strata2)
    tasks2 = tuple(
        pd.first_witness(system, 2, ratios2, strata2)[0]
        for system in systems2
    )
    signatures2 = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in systems2
    )
    relevant2 = pd.relevant_walls(systems2, tasks2, ratios2)
    assert len(systems2) == 5_823 and len(relevant2) == 21

    task_sets: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
    for signature, task in zip(signatures2, tasks2):
        parent = tuple(signature[index] for index in relevant2)
        task_sets[parent].add(task)
    assert len(task_sets) == 849
    assert all(len(tasks) == 1 for tasks in task_sets.values())

    task_by_parent = {
        parent: next(iter(tasks))
        for parent, tasks in task_sets.items()
    }
    persistent_label = {
        parent: (
            ("residual", parent)
            if parent in base.affected_parents
            else ("task", task_by_parent[parent])
        )
        for parent in task_sets
    }
    labels = sorted(set(persistent_label.values()), key=repr)
    assert len(labels) == 68
    label_id = {label: index for index, label in enumerate(labels)}

    parents = tuple(task_sets)
    parent_index = {parent: index for index, parent in enumerate(parents)}
    item_labels = tuple(label_id[persistent_label[parent]] for parent in parents)

    all_walls2 = tuple(
        (i, j, ratio)
        for i, j in pd.PAIRS
        for ratio in ratios2
    )
    kept_walls2 = tuple(all_walls2[index] for index in relevant2)

    usage_weights = [0] * len(parents)
    training = pd.integer_quadruples(8)
    assert len(training) == 55
    for values in training:
        full = pd.signs_for_quad(values, all_walls2)
        parent = tuple(full[index] for index in relevant2)
        usage_weights[parent_index[parent]] += 1
    assert sum(usage_weights) == 55

    # Reconstruct only completion children and freeze their Phase-8C.2 decoders.
    ratios3, strata3, local = ro._reconstruct_local_completion_children(
        base.completion_required_parents
    )
    completion_by_parent = {
        case.parent: case
        for case in base.completion_residual_cases
    }
    decoders = {}
    raw_records = {}
    completion_mass = [0] * len(parents)
    fixed_decoder_weighted_depth = 0
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
        root, _internal, _worst, weighted, _path_leaves = ro._optimal_decoder(records)
        decoders[parent] = root
        raw_records[parent] = records
        mass = sum(weight for _key, _task, weight in records)
        completion_mass[parent_index[parent]] = mass
        fixed_decoder_weighted_depth += weighted

    assert sum(completion_mass) == 288
    assert fixed_decoder_weighted_depth == 544

    mixtures = (
        Fraction(0),
        Fraction(1, 16),
        Fraction(1, 8),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1),
    )

    candidates = []
    for mixture in mixtures:
        weights = tuple(
            (1 - mixture) * Fraction(usage, 55)
            + mixture * Fraction(refinement, 288)
            for usage, refinement in zip(usage_weights, completion_mass)
        )
        tree, cost = pd.build_tree(parents, item_labels, weights)
        old_histories = {
            parent: tuple(
                ("old", predicate, sign)
                for predicate, sign in pd.tree_history(tree, parent)
            )
            for parent in parents
        }
        old_widths = pd.widths(tuple(old_histories.values()))
        assert sum(old_widths) == cost[1]

        current_depth = sum(
            usage_weights[index] * len(old_histories[parent])
            for index, parent in enumerate(parents)
        )
        completion_old_depth = sum(
            completion_mass[index] * len(old_histories[parent])
            for index, parent in enumerate(parents)
        )

        updated_histories = []
        for parent in sorted(base.stable_parents | base.history_reindex_parents):
            updated_histories.append(old_histories[parent])
        for parent in sorted(base.completion_required_parents):
            old_history = old_histories[parent]
            root = decoders[parent]
            for key, _task, _weight in raw_records[parent]:
                local_history, _decoded = _decoder_history(root, key)
                updated_histories.append(
                    old_history
                    + tuple(
                        ("completion", parent, coordinate, sign)
                        for coordinate, sign in local_history
                    )
                )

        updated_widths = pd.widths(tuple(updated_histories))
        candidates.append(
            PlacementCandidate(
                mixture=mixture,
                root_wall=kept_walls2[tree.predicate],
                current_weighted_depth=current_depth,
                completion_old_path_depth=completion_old_depth,
                completion_final_depth=completion_old_depth + fixed_decoder_weighted_depth,
                old_tree_nodes=sum(old_widths),
                old_internal_nodes=cost[3],
                updated_tree_nodes=sum(updated_widths),
                updated_internal_nodes=cost[3] + 16,
                updated_peak=max(updated_widths),
                updated_worst=len(updated_widths) - 1,
                updated_widths=updated_widths,
            )
        )

    candidates = tuple(candidates)
    pareto = tuple(
        candidate
        for candidate in candidates
        if not any(
            other is not candidate and _dominates(other, candidate)
            for other in candidates
        )
    )
    return PlacementProbe(candidates=candidates, pareto=pareto)


def main() -> None:
    result = analyze_refinement_aware_placement()
    print("Phase 8D.2 refinement-aware Huffman placement probe")
    for candidate in result.candidates:
        print(
            "  lambda={:<5} root={} current={}/55={:.4f} "
            "completion={}/288={:.4f} old_nodes={} updated={} peak={} worst={}".format(
                str(candidate.mixture),
                candidate.root_wall,
                candidate.current_weighted_depth,
                float(candidate.current_mean_depth),
                candidate.completion_final_depth,
                float(candidate.completion_mean_final_depth),
                candidate.old_tree_nodes,
                candidate.updated_tree_nodes,
                candidate.updated_peak,
                candidate.updated_worst,
            )
        )
    print("  Pareto mixtures:", tuple(str(item.mixture) for item in result.pareto))


if __name__ == "__main__":
    main()
