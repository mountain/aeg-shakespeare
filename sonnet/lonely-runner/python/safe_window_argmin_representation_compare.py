"""Phase 14C: exact local representation comparison for the K=4 argmin obstruction.

The exceptional safe-window parent has three competing next-enter events and
seven minimum-group tasks.  This script compares two exact descriptions without
promoting either to a public abstraction:

A. complete the three pairwise ternary comparisons;
B. retain the process-native minimum group as the task value.

For A we enumerate every feasible complete pairwise sign record inside the real
K=4 parent closure, map it to its exact closer task, and optimize a ternary
comparison tree.  B is reported only as the seven-value task quotient; no claim
is made that one seven-way observation has the same primitive cost as one
pairwise comparison.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import product

import safe_window_task_transfer as transfer


@dataclass(frozen=True)
class PairwiseTree:
    coordinate: int | None
    task: tuple[int, ...] | None = None
    children: tuple[tuple[int, "PairwiseTree"], ...] = ()


@dataclass(frozen=True)
class RepresentationComparison:
    pairwise_coordinates: tuple[tuple[int, int, object], ...]
    feasible_complete_sign_states: int
    minimum_group_tasks: int
    overrefined_states: int
    weighted_depth_uniform_states: int
    tree_nodes: int
    internal_nodes: int
    worst_depth: int
    peak_frontier: int
    widths: tuple[int, ...]
    terminal_merged_dag_nodes: int
    minimum_group_value_count: int


def _add_sign(module, closure, coordinate, sign):
    first, second, ratio = coordinate
    if sign == -1:
        return module._add_edge(closure, first, second, ratio, True)
    if sign == 0:
        result = module._add_edge(closure, first, second, ratio, False)
        if result is None:
            return None
        return module._add_edge(result, second, first, 1 / ratio, False)
    if sign == 1:
        return module._add_edge(closure, second, first, 1 / ratio, True)
    raise AssertionError(sign)


def _exceptional_parent():
    module = transfer.four
    frontiers, _old, _states = transfer._compile_frontiers(module)
    _extended, _next, _alternatives, cases = transfer._extend_safe_window(
        module,
        frontiers,
    )
    case = max(cases, key=lambda item: (item.closer_count, -item.parent_index))
    assert case.closer_count == 7
    assert len(case.minimum_support) == 3
    return module, frontiers[case.parent_index], case.minimum_support


def _complete_pairwise_states(module, frontier, coordinates):
    records = []
    for signature in product((-1, 0, 1), repeat=len(coordinates)):
        closure = frontier.closure
        for coordinate, sign in zip(coordinates, signature):
            closure = _add_sign(module, closure, coordinate, sign)
            if closure is None:
                break
        if closure is None:
            continue

        branches = module._minimum_groups(closure, frontier.next_events)
        # A complete consistent weak ordering of the three active candidates
        # determines one exact minimum group.
        closer_groups = {tuple(group) for group, _child in branches}
        if len(closer_groups) != 1:
            raise AssertionError((signature, closer_groups))
        closer = next(iter(closer_groups))
        records.append((tuple(signature), closer))

    return tuple(sorted(records))


def _build_optimal_tree(records):
    signatures = tuple(signature for signature, _task in records)
    tasks = tuple(task for _signature, task in records)
    item_count = len(records)
    full_mask = (1 << item_count) - 1

    predicate_masks = []
    for coordinate in range(len(signatures[0])):
        masks = [0, 0, 0]
        for item, signature in enumerate(signatures):
            masks[signature[coordinate] + 1] |= 1 << item
        predicate_masks.append(tuple(masks))

    task_masks = {}
    for task in set(tasks):
        mask = 0
        for item, item_task in enumerate(tasks):
            if item_task == task:
                mask |= 1 << item
        task_masks[task] = mask

    @lru_cache(maxsize=None)
    def pure(mask):
        found = None
        for task, task_mask in task_masks.items():
            if not (mask & task_mask):
                continue
            if found is not None:
                return None
            found = task
        return found

    @lru_cache(maxsize=None)
    def solve(mask):
        task = pure(mask)
        if task is not None:
            return (0, 1, 0, 0), None

        weight = mask.bit_count()
        best = None
        best_coordinate = None
        for coordinate, masks in enumerate(predicate_masks):
            children = [mask & branch for branch in masks]
            nonempty = [child for child in children if child]
            if len(nonempty) <= 1:
                continue
            costs = [solve(child)[0] for child in nonempty]
            candidate = (
                weight + sum(cost[0] for cost in costs),
                1 + sum(cost[1] for cost in costs),
                1 + max(cost[2] for cost in costs),
                1 + sum(cost[3] for cost in costs),
            )
            if best is None or candidate < best:
                best = candidate
                best_coordinate = coordinate
        if best is None:
            raise AssertionError("complete pairwise signs must classify argmin task")
        return best, best_coordinate

    def build(mask):
        task = pure(mask)
        if task is not None:
            return PairwiseTree(None, task=task)
        coordinate = solve(mask)[1]
        children = []
        for sign, branch in zip((-1, 0, 1), predicate_masks[coordinate]):
            child = mask & branch
            if child:
                children.append((sign, build(child)))
        return PairwiseTree(coordinate, children=tuple(children))

    cost, _root = solve(full_mask)
    return build(full_mask), cost


def _history(tree, signature):
    history = []
    node = tree
    while node.coordinate is not None:
        sign = signature[node.coordinate]
        history.append((node.coordinate, sign))
        node = dict(node.children)[sign]
    return tuple(history)


def _widths(histories):
    max_depth = max(map(len, histories))
    result = [1]
    for depth in range(1, max_depth + 1):
        result.append(
            len({history[:depth] for history in histories if len(history) >= depth})
        )
    return tuple(result)


def analyze_argmin_representation_compare():
    module, frontier, coordinates = _exceptional_parent()
    records = _complete_pairwise_states(module, frontier, coordinates)
    tree, cost = _build_optimal_tree(records)
    histories = tuple(_history(tree, signature) for signature, _task in records)
    widths = _widths(histories)
    tasks = {task for _signature, task in records}

    return RepresentationComparison(
        pairwise_coordinates=coordinates,
        feasible_complete_sign_states=len(records),
        minimum_group_tasks=len(tasks),
        overrefined_states=len(records) - len(tasks),
        weighted_depth_uniform_states=cost[0],
        tree_nodes=cost[1],
        internal_nodes=cost[3],
        worst_depth=cost[2],
        peak_frontier=max(widths),
        widths=widths,
        terminal_merged_dag_nodes=cost[3] + len(tasks),
        minimum_group_value_count=len(tasks),
    )


def main() -> None:
    print(analyze_argmin_representation_compare())


if __name__ == "__main__":
    main()
