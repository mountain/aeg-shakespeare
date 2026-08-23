"""Phase 8E probe: controlled interleaving of frozen old and new wall predicates.

This experiment relaxes the old-prefix-first architecture without importing the
full center-3 arrangement.  The old representation contributes its 849
center-2 persistent parents and 21 task-relevant wall signs.  Phase 8C contributes
exactly seven frozen new completion walls.  For every old full sign system, exact
multiplicative difference constraints determine all feasible sign combinations
on those seven walls; no other center-3 wall is enumerated.

Stable parents assign the same task to every feasible new-wall variant.  The two
history-reindex parents use their already-certified new task.  Completion parents
are decoded by the frozen Phase-8C.2 local decoders.  Thus a joint 28-predicate
decision problem is built entirely from old geometry plus the previously
objectified completion semantics.

The exact tree search may now place a new completion wall before full old-parent
resolution.  Such an occurrence is recorded with the set of old parents still
alive at that node, giving a concrete activation/cross-parent-sharing witness.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import local_contact_refinement as lcr
import pair_difference_refinement as pd
import residual_objectification as ro


@dataclass(frozen=True)
class InterleavingCandidate:
    mixture: Fraction
    expanded_items: int
    final_tasks: int
    current_weighted_depth: int
    completion_weighted_depth: int
    tree_nodes: int
    internal_nodes: int
    terminal_merged_dag_nodes: int
    peak_frontier: int
    worst_depth: int
    widths: tuple[int, ...]
    new_wall_internal_nodes: int
    cross_parent_new_wall_nodes: int
    earliest_new_wall_depth: int | None
    new_wall_activation: tuple[tuple[tuple[int, int, Fraction], int, int], ...]


@dataclass(frozen=True)
class InterleavingProbe:
    new_walls: tuple[lcr.ResidualCoordinate, ...]
    candidates: tuple[InterleavingCandidate, ...]


def _sign_edges(coordinate: lcr.ResidualCoordinate, sign: int):
    first, second = coordinate.pair
    ratio = coordinate.ratio
    if sign < 0:
        return ((first, second, ratio, True),)
    if sign > 0:
        return ((second, first, Fraction(1, 1) / ratio, True),)
    return (
        (first, second, ratio, False),
        (second, first, Fraction(1, 1) / ratio, False),
    )


def _feasible_new_signatures(system, strata2, new_walls):
    closure = pd.initial_closure()
    for pair in pd.PAIRS:
        closure = pd.add_edges(
            closure,
            pd.stratum_edges(pair, strata2[system[pd.PAIR_INDEX[pair]]]),
        )
        assert closure is not None

    signs: list[int | None] = [None] * len(new_walls)
    unresolved = []
    for index, coordinate in enumerate(new_walls):
        relation = lcr.arbitrary_relation(
            strata2[system[pd.PAIR_INDEX[coordinate.pair]]],
            coordinate.ratio,
        )
        if relation is None:
            unresolved.append(index)
        else:
            signs[index] = relation

    result = set()

    def visit(depth, state):
        if depth == len(unresolved):
            signature = tuple(signs)
            assert all(value is not None for value in signature)
            result.add(tuple(int(value) for value in signature))
            return
        index = unresolved[depth]
        coordinate = new_walls[index]
        for sign in (-1, 0, 1):
            next_state = pd.add_edges(state, _sign_edges(coordinate, sign))
            if next_state is None:
                continue
            signs[index] = sign
            visit(depth + 1, next_state)
        signs[index] = None

    visit(0, closure)
    assert result
    return tuple(sorted(result))


def _decoder_task(root: ro.DecoderNode, key: ro.RawKey):
    node = root
    while not node.is_leaf:
        assert node.coordinate is not None
        node = dict(node.children)[key[node.coordinate]]
    assert node.task is not None
    return node.task


def _walk_activation(tree, signatures, parent_by_item, old_predicate_count, new_walls):
    earliest: dict[int, int] = {}
    occurrences: dict[int, int] = defaultdict(int)
    cross_parent_nodes = 0
    new_nodes = 0

    def visit(node, item_indices, depth):
        nonlocal cross_parent_nodes, new_nodes
        if node.predicate is None:
            return
        predicate = node.predicate
        groups = defaultdict(list)
        for index in item_indices:
            groups[signatures[index][predicate]].append(index)

        if predicate >= old_predicate_count:
            new_index = predicate - old_predicate_count
            earliest[new_index] = min(earliest.get(new_index, depth), depth)
            occurrences[new_index] += 1
            new_nodes += 1
            parent_count = len({parent_by_item[index] for index in item_indices})
            if parent_count > 1:
                cross_parent_nodes += 1

        for sign, child in node.children:
            visit(child, tuple(groups[sign]), depth + 1)

    visit(tree, tuple(range(len(signatures))), 0)
    activation = tuple(
        (
            (new_walls[index].pair[0], new_walls[index].pair[1], new_walls[index].ratio),
            earliest.get(index, -1),
            occurrences.get(index, 0),
        )
        for index in range(len(new_walls))
    )
    depths = [depth for _wall, depth, count in activation if count and depth >= 0]
    return new_nodes, cross_parent_nodes, (min(depths) if depths else None), activation


def analyze_controlled_interleaving() -> InterleavingProbe:
    base = lcr.analyze_center2_to_center3()

    ratios2 = pd.contact_ratios(2)
    strata2 = pd.strata(ratios2)
    systems2 = pd.enumerate_systems(strata2)
    tasks2 = tuple(
        pd.first_witness(system, 2, ratios2, strata2)[0]
        for system in systems2
    )
    full_signatures2 = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in systems2
    )
    relevant2 = pd.relevant_walls(systems2, tasks2, ratios2)
    assert len(systems2) == 5_823 and len(relevant2) == 21

    task_sets = defaultdict(set)
    old_systems_by_parent = defaultdict(list)
    for system, full_signature, task in zip(systems2, full_signatures2, tasks2):
        parent = tuple(full_signature[index] for index in relevant2)
        task_sets[parent].add(task)
        old_systems_by_parent[parent].append(system)
    assert len(task_sets) == 849
    assert all(len(tasks) == 1 for tasks in task_sets.values())
    old_task = {parent: next(iter(tasks)) for parent, tasks in task_sets.items()}

    new_walls = tuple(
        sorted(
            {
                coordinate
                for case in base.completion_residual_cases
                for coordinate in case.coordinates
            },
            key=lambda item: (item.pair, item.ratio),
        )
    )
    assert len(new_walls) == 7
    new_wall_index = {coordinate: index for index, coordinate in enumerate(new_walls)}

    # Freeze Phase-8C.2 decoders for the six completion parents.
    ratios3, strata3, completion_local = ro._reconstruct_local_completion_children(
        base.completion_required_parents
    )
    completion_case = {case.parent: case for case in base.completion_residual_cases}
    decoder_by_parent = {}
    selected_union_indices = {}
    for parent in sorted(base.completion_required_parents):
        case = completion_case[parent]
        selected_features = tuple(
            ro._feature_index(coordinate, ratios3)
            for coordinate in case.coordinates
        )
        records = ro._unique_raw_records(
            tuple(completion_local[parent]),
            selected_features,
            ratios3,
            strata3,
        )
        root, *_rest = ro._optimal_decoder(records)
        decoder_by_parent[parent] = root
        selected_union_indices[parent] = tuple(new_wall_index[item] for item in case.coordinates)

    reindex_task = {case.parent: case.new_task for case in base.history_reindex_cases}

    # Expand only by the seven frozen new walls. Feasible sign combinations are
    # generated from center-2 exact constraints, not from the full center-3 census.
    feasible_by_parent = defaultdict(set)
    for parent, systems in old_systems_by_parent.items():
        for system in systems:
            feasible_by_parent[parent].update(
                _feasible_new_signatures(system, strata2, new_walls)
            )
    assert set(feasible_by_parent) == set(task_sets)

    items = []
    labels = []
    parent_by_item = []
    item_index = {}
    for parent in sorted(task_sets):
        for new_signature in sorted(feasible_by_parent[parent]):
            if parent in base.completion_required_parents:
                key = tuple(
                    new_signature[index]
                    for index in selected_union_indices[parent]
                )
                task = _decoder_task(decoder_by_parent[parent], key)
            elif parent in base.history_reindex_parents:
                task = reindex_task[parent]
            else:
                task = old_task[parent]
            signature = tuple(parent) + tuple(new_signature)
            item_index[(parent, tuple(new_signature))] = len(items)
            items.append(signature)
            labels.append(task)
            parent_by_item.append(parent)

    items = tuple(items)
    parent_by_item = tuple(parent_by_item)
    task_values = sorted(set(labels), key=repr)
    assert len(task_values) == 75
    task_id = {task: index for index, task in enumerate(task_values)}
    task_ids = tuple(task_id[task] for task in labels)

    all_walls2 = tuple(
        (i, j, ratio)
        for i, j in pd.PAIRS
        for ratio in ratios2
    )

    usage_weights = [0] * len(items)
    training = pd.integer_quadruples(8)
    assert len(training) == 55
    for values in training:
        full = pd.signs_for_quad(values, all_walls2)
        parent = tuple(full[index] for index in relevant2)
        new_signature = tuple(
            -1 if Fraction(values[coordinate.pair[1]], values[coordinate.pair[0]]) < coordinate.ratio
            else (1 if Fraction(values[coordinate.pair[1]], values[coordinate.pair[0]]) > coordinate.ratio else 0)
            for coordinate in new_walls
        )
        usage_weights[item_index[(parent, new_signature)]] += 1
    assert sum(usage_weights) == 55

    refinement_weights = [0] * len(items)
    for parent in sorted(base.completion_required_parents):
        for child, _task in completion_local[parent]:
            full3 = pd.full_signature(child, ratios3, strata3)
            new_signature = tuple(
                full3[ro._feature_index(coordinate, ratios3)]
                for coordinate in new_walls
            )
            refinement_weights[item_index[(parent, new_signature)]] += 1
    assert sum(refinement_weights) == 288

    candidates = []
    for mixture in (Fraction(0), Fraction(1, 16), Fraction(1, 4)):
        weights = tuple(
            (1 - mixture) * Fraction(current, 55)
            + mixture * Fraction(refinement, 288)
            for current, refinement in zip(usage_weights, refinement_weights)
        )
        tree, cost = pd.build_tree(items, task_ids, weights)
        histories = tuple(pd.tree_history(tree, signature) for signature in items)
        widths = pd.widths(histories)
        assert sum(widths) == cost[1]

        current_depth = sum(
            usage_weights[index] * len(histories[index])
            for index in range(len(items))
        )
        completion_depth = sum(
            refinement_weights[index] * len(histories[index])
            for index in range(len(items))
        )
        new_nodes, cross_nodes, earliest, activation = _walk_activation(
            tree,
            items,
            parent_by_item,
            len(relevant2),
            new_walls,
        )
        candidates.append(
            InterleavingCandidate(
                mixture=mixture,
                expanded_items=len(items),
                final_tasks=len(task_values),
                current_weighted_depth=current_depth,
                completion_weighted_depth=completion_depth,
                tree_nodes=cost[1],
                internal_nodes=cost[3],
                terminal_merged_dag_nodes=cost[3] + len(task_values),
                peak_frontier=max(widths),
                worst_depth=cost[2],
                widths=widths,
                new_wall_internal_nodes=new_nodes,
                cross_parent_new_wall_nodes=cross_nodes,
                earliest_new_wall_depth=earliest,
                new_wall_activation=activation,
            )
        )

    return InterleavingProbe(new_walls=new_walls, candidates=tuple(candidates))


def main() -> None:
    result = analyze_controlled_interleaving()
    print("Phase 8E controlled old/new wall interleaving probe")
    print("  frozen new walls:")
    for coordinate in result.new_walls:
        print(f"    u{coordinate.pair[1]+1}/u{coordinate.pair[0]+1} ? {coordinate.ratio}")
    for candidate in result.candidates:
        print(f"  lambda={candidate.mixture}")
        print(f"    expanded feasible items: {candidate.expanded_items}")
        print(f"    final tasks:             {candidate.final_tasks}")
        print(f"    current depth total:     {candidate.current_weighted_depth}")
        print(f"    completion depth total:  {candidate.completion_weighted_depth}")
        print(f"    tree / internals / DAG:  {candidate.tree_nodes} / {candidate.internal_nodes} / {candidate.terminal_merged_dag_nodes}")
        print(f"    peak / worst:            {candidate.peak_frontier} / {candidate.worst_depth}")
        print(f"    new-wall internal nodes: {candidate.new_wall_internal_nodes}")
        print(f"    cross-parent activations:{candidate.cross_parent_new_wall_nodes}")
        print(f"    earliest new-wall depth: {candidate.earliest_new_wall_depth}")
        print(f"    widths:                  {candidate.widths}")
        print("    activation (wall, earliest depth, occurrences):")
        for entry in candidate.new_wall_activation:
            print(f"      {entry}")


if __name__ == "__main__":
    main()
