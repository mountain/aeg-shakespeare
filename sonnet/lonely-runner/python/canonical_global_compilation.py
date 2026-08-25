"""Phase 11B2: globally compile canonical lazy predicates into a decision tree.

This script starts from the horizon-free lazy compiler of Phase 11B1.  It uses
its exact 27-coordinate global minimum, refines the canonical terminal regions
only enough to assign complete ternary sign records, and then optimizes a static
decision tree with the same lexicographic space-time objective used by the older
pair-difference/Huffman experiments.

The expensive dynamic-programming tree optimization is research-local and should
not be placed in routine multi-version CI.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

import canonical_lazy_contact_compiler as lazy


@dataclass(frozen=True)
class DecisionTree:
    predicate: int | None
    task: int | None = None
    children: tuple[tuple[int, "DecisionTree"], ...] = ()


@dataclass(frozen=True)
class GlobalCompilationResult:
    coordinates: tuple[lazy.Coordinate, ...]
    sign_cells: int
    tasks: int
    weighted_depth: int
    tree_nodes: int
    worst_depth: int
    internal_nodes: int
    dag_nodes: int
    peak_frontier: int
    widths: tuple[int, ...]
    root_coordinate: lazy.Coordinate


def _terminal_regions() -> tuple[lazy.TerminalRegion, ...]:
    """Replay Phase 11B1 and retain its exact terminal closures."""

    initial_events = tuple(
        lazy.NextContact(lazy.DELTA, 0, "exit")
        for _ in range(lazy.K)
    )
    stack = [
        (
            lazy._initial_closure(),
            initial_events,
            frozenset(range(lazy.K)),
            0,
        )
    ]
    seen = set()
    terminals = []

    while stack:
        closure, events, bad, event_index = stack.pop()
        state_key = (closure, events, bad, event_index)
        if state_key in seen:
            continue
        seen.add(state_key)

        for group, child_closure in lazy._minimum_groups(closure, events):
            child_index = event_index + 1
            group_set = set(group)
            bad_on = set(bad) - group_set
            bad_after = set(bad)
            child_events = list(events)
            boundary = []

            for runner in group:
                event = events[runner]
                boundary.append((runner, event.center, event.kind))
                if event.kind == "exit":
                    bad_after.discard(runner)
                else:
                    bad_after.add(runner)
                child_events[runner] = lazy._advance(event)

            if not bad_on:
                task: lazy.Task = (
                    child_index,
                    tuple(sorted(boundary)),
                    "interval" if not bad_after else "point",
                )
                terminals.append(lazy.TerminalRegion(child_closure, task))
            else:
                stack.append(
                    (
                        child_closure,
                        tuple(child_events),
                        frozenset(bad_after),
                        child_index,
                    )
                )

    assert len(seen) == 388
    assert len(terminals) == 261
    return tuple(terminals)


def _add_sign(
    closure: lazy.Closure,
    coordinate: lazy.Coordinate,
    sign: int,
) -> lazy.Closure | None:
    first, second, ratio = coordinate
    if sign == -1:
        return lazy._add_edge(closure, first, second, ratio, True)
    if sign == 0:
        result = lazy._add_edge(closure, first, second, ratio, False)
        if result is None:
            return None
        return lazy._add_edge(result, second, first, 1 / ratio, False)
    if sign == 1:
        return lazy._add_edge(closure, second, first, 1 / ratio, True)
    raise AssertionError(sign)


def _refine_signature(
    closure: lazy.Closure,
    coordinates: tuple[lazy.Coordinate, ...],
) -> tuple[tuple[tuple[int, ...], lazy.Closure], ...]:
    signs: list[int | None] = [None] * len(coordinates)
    output = {}

    def visit(depth: int, current: lazy.Closure) -> None:
        if depth == len(coordinates):
            signature = tuple(int(sign) for sign in signs if sign is not None)
            assert len(signature) == len(coordinates)
            output[signature] = current
            return

        first, second, ratio = coordinates[depth]
        forced = lazy._relation(current, (first, second), ratio)
        if forced is not None:
            signs[depth] = forced
            visit(depth + 1, current)
            signs[depth] = None
            return

        for sign in (-1, 0, 1):
            child = _add_sign(current, coordinates[depth], sign)
            if child is None:
                continue
            signs[depth] = sign
            visit(depth + 1, child)
        signs[depth] = None

    visit(0, closure)
    return tuple(sorted(output.items()))


def build_global_sign_cells():
    """Return the exact 27-wall sign cells and their first-witness tasks."""

    compiler = lazy.analyze_lazy_compiler()
    coordinates = compiler.minimum_task_coordinates
    task_by_signature = {}

    for region in _terminal_regions():
        for signature, _closure in _refine_signature(
            region.closure,
            coordinates,
        ):
            previous = task_by_signature.get(signature)
            if previous is not None:
                assert previous == region.task
            task_by_signature[signature] = region.task

    assert len(task_by_signature) == 2_211
    assert len(set(task_by_signature.values())) == 81
    return coordinates, task_by_signature


def _usage_weights(
    coordinates: tuple[lazy.Coordinate, ...],
    signatures: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    index = {signature: position for position, signature in enumerate(signatures)}
    weights = [0] * len(signatures)

    usage = tuple(
        values
        for values in combinations(range(1, 9), 4)
        if Fraction(values[-1], values[0]) < lazy.RMAX
    )
    assert len(usage) == 55

    for values in usage:
        signature = tuple(
            -1
            if Fraction(values[second], values[first]) < ratio
            else (
                1
                if Fraction(values[second], values[first]) > ratio
                else 0
            )
            for first, second, ratio in coordinates
        )
        weights[index[signature]] += 1

    assert sum(weights) == 55
    return tuple(weights)


def _build_tree(signatures, task_ids, weights):
    item_count = len(signatures)
    full_mask = (1 << item_count) - 1

    predicate_masks = []
    for predicate in range(len(signatures[0])):
        masks = [0, 0, 0]
        for item, signature in enumerate(signatures):
            masks[signature[predicate] + 1] |= 1 << item
        predicate_masks.append(tuple(masks))

    task_masks = {}
    for task in set(task_ids):
        mask = 0
        for item, item_task in enumerate(task_ids):
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
    def mask_weight(mask):
        total = 0
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            total += weights[bit.bit_length() - 1]
        return total

    @lru_cache(maxsize=None)
    def solve(mask):
        task = pure(mask)
        if task is not None:
            return (0, 1, 0, 0), None

        total_weight = mask_weight(mask)
        best = None
        best_predicate = None
        for predicate, masks in enumerate(predicate_masks):
            children = [mask & branch for branch in masks]
            nonempty = [child for child in children if child]
            if len(nonempty) <= 1:
                continue
            costs = [solve(child)[0] for child in nonempty]
            candidate = (
                total_weight + sum(cost[0] for cost in costs),
                1 + sum(cost[1] for cost in costs),
                1 + max(cost[2] for cost in costs),
                1 + sum(cost[3] for cost in costs),
            )
            if best is None or candidate < best:
                best = candidate
                best_predicate = predicate

        if best is None:
            raise AssertionError("global sign cells do not separate tasks")
        return best, best_predicate

    def build(mask):
        task = pure(mask)
        if task is not None:
            return DecisionTree(None, task=task)
        predicate = solve(mask)[1]
        children = []
        for sign, branch in zip((-1, 0, 1), predicate_masks[predicate]):
            child = mask & branch
            if child:
                children.append((sign, build(child)))
        return DecisionTree(predicate, children=tuple(children))

    cost, _predicate = solve(full_mask)
    return build(full_mask), cost


def _history(tree: DecisionTree, signature: tuple[int, ...]):
    result = []
    node = tree
    while node.predicate is not None:
        sign = signature[node.predicate]
        result.append((node.predicate, sign))
        node = dict(node.children)[sign]
    return tuple(result)


def _widths(histories):
    max_depth = max(map(len, histories))
    result = [1]
    for depth in range(1, max_depth + 1):
        result.append(
            len(
                {
                    history[:depth]
                    for history in histories
                    if len(history) >= depth
                }
            )
        )
    return tuple(result)


def analyze_global_compilation() -> GlobalCompilationResult:
    coordinates, task_by_signature = build_global_sign_cells()
    signatures = tuple(task_by_signature)
    task_values = sorted(set(task_by_signature.values()), key=repr)
    task_id = {task: index for index, task in enumerate(task_values)}
    task_ids = tuple(task_id[task_by_signature[signature]] for signature in signatures)
    weights = _usage_weights(coordinates, signatures)

    tree, cost = _build_tree(signatures, task_ids, weights)
    histories = tuple(_history(tree, signature) for signature in signatures)
    widths = _widths(histories)

    assert sum(widths) == cost[1]
    assert tree.predicate is not None
    return GlobalCompilationResult(
        coordinates=coordinates,
        sign_cells=len(signatures),
        tasks=len(task_values),
        weighted_depth=cost[0],
        tree_nodes=cost[1],
        worst_depth=cost[2],
        internal_nodes=cost[3],
        dag_nodes=cost[3] + len(task_values),
        peak_frontier=max(widths),
        widths=widths,
        root_coordinate=coordinates[tree.predicate],
    )


def main() -> None:
    result = analyze_global_compilation()
    print("Sonnet 001 canonical global compilation")
    print(f"  coordinates:                {len(result.coordinates)}")
    print(f"  sign cells / tasks:         {result.sign_cells} / {result.tasks}")
    print(f"  weighted/tree/worst/internal: {result.weighted_depth} / {result.tree_nodes} / {result.worst_depth} / {result.internal_nodes}")
    print(f"  peak / DAG:                 {result.peak_frontier} / {result.dag_nodes}")
    print(f"  root:                       {result.root_coordinate}")
    print(f"  widths:                     {result.widths}")


if __name__ == "__main__":
    main()
