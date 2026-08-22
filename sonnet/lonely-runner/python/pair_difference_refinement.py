"""Exact four-speed A/M pair-difference refinement: contact center 2 -> 3.

This is a manual research script, not a routine CI test.  It demonstrates that
contact-center refinement can be performed on the already-objectified
pair-difference geometry rather than restarting from the independent Cartesian
product of all pair-wall strata.

Run from the repository root with:

    python sonnet/lonely-runner/python/pair_difference_refinement.py

Only Python's standard library is used.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key, lru_cache
from itertools import combinations
import time


K = 4
DELTA = Fraction(1, 5)
RMAX = Fraction(8)
PAIRS = tuple(combinations(range(K), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
DFS_PAIRS = ((0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3))


@dataclass(frozen=True)
class Bound:
    weight: Fraction
    strict: bool = False


def tighter(left: Bound, right: Bound | None) -> bool:
    if right is None:
        return True
    return left.weight < right.weight or (
        left.weight == right.weight and left.strict and not right.strict
    )


def compose(left: Bound, right: Bound) -> Bound:
    return Bound(left.weight * right.weight, left.strict or right.strict)


def add_edge(
    closure: tuple[tuple[Bound | None, ...], ...],
    source: int,
    target: int,
    weight: Fraction,
    strict: bool,
) -> tuple[tuple[Bound | None, ...], ...] | None:
    """Incrementally close one exact multiplicative difference constraint."""

    edge = Bound(Fraction(weight), strict)
    if closure[source][target] is not None and not tighter(
        edge,
        closure[source][target],
    ):
        return closure

    size = len(closure)
    updated = [list(row) for row in closure]
    for first in range(size):
        to_source = closure[first][source]
        if to_source is None:
            continue
        prefix = compose(to_source, edge)
        for last in range(size):
            from_target = closure[target][last]
            if from_target is None:
                continue
            candidate = compose(prefix, from_target)
            if tighter(candidate, updated[first][last]):
                updated[first][last] = candidate

    for vertex in range(size):
        diagonal = updated[vertex][vertex]
        assert diagonal is not None
        if diagonal.weight < 1 or (
            diagonal.weight == 1 and diagonal.strict
        ):
            return None

    return tuple(tuple(row) for row in updated)


def add_edges(closure, edges):
    state = closure
    for edge in edges:
        state = add_edge(state, *edge)
        if state is None:
            return None
    return state


def initial_closure() -> tuple[tuple[Bound | None, ...], ...]:
    rows: list[list[Bound | None]] = [[None] * K for _ in range(K)]
    for vertex in range(K):
        rows[vertex][vertex] = Bound(Fraction(1), False)
    closure = tuple(tuple(row) for row in rows)
    # Work in the open relative domain u4/u1 < 8.
    result = add_edge(closure, 0, 3, RMAX, True)
    assert result is not None
    return result


def contact_events(max_center: int):
    events = []
    for center in range(max_center + 1):
        events.append((Fraction(center) + DELTA, center, "exit"))
        if center >= 1:
            events.append((Fraction(center) - DELTA, center, "enter"))
    return tuple(sorted(events))


def contact_ratios(max_center: int) -> tuple[Fraction, ...]:
    constants = tuple(alpha for alpha, _center, _kind in contact_events(max_center))
    return tuple(
        sorted(
            {
                beta / alpha
                for alpha in constants
                for beta in constants
                if 1 < beta / alpha < RMAX
            }
        )
    )


def strata(thresholds: tuple[Fraction, ...]):
    result = []
    lower = Fraction(1)
    for threshold in thresholds:
        result.append(("I", lower, threshold))
        result.append(("E", threshold, threshold))
        lower = threshold
    result.append(("I", lower, None))
    return tuple(result)


def stratum_edges(pair, item):
    first, second = pair
    kind, lower, upper = item
    if kind == "E":
        return (
            (first, second, lower, False),
            (second, first, Fraction(1, 1) / lower, False),
        )
    result = [(second, first, Fraction(1, 1) / lower, True)]
    if upper is not None:
        result.append((first, second, upper, True))
    return tuple(result)


def enumerate_systems(pair_strata) -> tuple[tuple[int, ...], ...]:
    base = initial_closure()
    systems = []

    def visit(depth, closure, choices):
        if depth == len(DFS_PAIRS):
            systems.append(tuple(choices[pair] for pair in PAIRS))
            return
        pair = DFS_PAIRS[depth]
        for index, item in enumerate(pair_strata):
            next_closure = add_edges(closure, stratum_edges(pair, item))
            if next_closure is None:
                continue
            choices[pair] = index
            visit(depth + 1, next_closure, choices)
            del choices[pair]

    visit(0, base, {})
    return tuple(systems)


def contained(child, parent) -> bool:
    child_kind, child_low, child_high = child
    parent_kind, parent_low, parent_high = parent
    if child_kind == "E":
        if parent_kind == "E":
            return child_low == parent_low
        return child_low > parent_low and (
            parent_high is None or child_low < parent_high
        )
    if parent_kind == "E" or child_low < parent_low:
        return False
    if parent_high is None:
        return child_high is None
    if child_high is None:
        return False
    return child_high <= parent_high


def refinement_map(old_strata, new_strata):
    return tuple(
        tuple(
            child_index
            for child_index, child in enumerate(new_strata)
            if contained(child, parent)
        )
        for parent in old_strata
    )


def refine_systems(old_systems, old_strata, new_strata):
    children = refinement_map(old_strata, new_strata)
    base = initial_closure()
    refined = []

    for old_system in old_systems:
        def visit(depth, closure, choices):
            if depth == len(DFS_PAIRS):
                refined.append(tuple(choices[pair] for pair in PAIRS))
                return
            pair = DFS_PAIRS[depth]
            old_index = old_system[PAIR_INDEX[pair]]
            for new_index in children[old_index]:
                next_closure = add_edges(
                    closure,
                    stratum_edges(pair, new_strata[new_index]),
                )
                if next_closure is None:
                    continue
                choices[pair] = new_index
                visit(depth + 1, next_closure, choices)
                del choices[pair]

        visit(0, base, {})

    return tuple(refined)


def sign_of(item, threshold: Fraction) -> int:
    kind, lower, upper = item
    if kind == "E":
        return -1 if lower < threshold else (1 if lower > threshold else 0)
    if upper is not None and upper <= threshold:
        return -1
    if lower >= threshold:
        return 1
    raise AssertionError((item, threshold))


def ratio_relation(system, pair, ratio, thresholds, pair_strata):
    if ratio <= 1:
        return 1
    if ratio >= RMAX:
        return -1
    return sign_of(pair_strata[system[PAIR_INDEX[pair]]], ratio)


def first_witness(system, max_center, thresholds, pair_strata):
    events = [
        (runner, alpha, center, kind)
        for runner in range(K)
        for alpha, center, kind in contact_events(max_center)
    ]

    def compare(left, right):
        i, alpha, _center_i, _kind_i = left
        j, beta, _center_j, _kind_j = right
        if i == j:
            return -1 if alpha < beta else (1 if alpha > beta else 0)
        if i < j:
            return ratio_relation(
                system,
                (i, j),
                beta / alpha,
                thresholds,
                pair_strata,
            )
        return -ratio_relation(
            system,
            (j, i),
            alpha / beta,
            thresholds,
            pair_strata,
        )

    ordered = sorted(events, key=cmp_to_key(compare))
    bad = set(range(K))
    cursor = 0
    event_index = 0
    history = []
    while cursor < len(ordered):
        group = [ordered[cursor]]
        cursor += 1
        while cursor < len(ordered) and compare(group[0], ordered[cursor]) == 0:
            group.append(ordered[cursor])
            cursor += 1
        event_index += 1

        boundary_runners = {runner for runner, _a, _n, _k in group}
        bad_on = tuple(sorted(bad - boundary_runners))
        after = set(bad)
        for runner, _alpha, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            else:
                after.add(runner)
        boundary = tuple(
            sorted((runner, center, kind) for runner, _a, center, kind in group)
        )
        history.append((boundary, bad_on, tuple(sorted(after))))
        if not bad_on:
            mode = "interval" if not after else "point"
            return (event_index, boundary, mode), tuple(history)
        bad = after
    raise AssertionError("contact alphabet did not produce a witness")


def full_signature(system, thresholds, pair_strata):
    return tuple(
        sign_of(pair_strata[system[pair_index]], threshold)
        for pair_index, _pair in enumerate(PAIRS)
        for threshold in thresholds
    )


def relevant_walls(systems, tasks, thresholds):
    """Find task-relevant wall signs using only local stratum adjacency."""

    threshold_count = len(thresholds)
    groups = [defaultdict(set) for _ in range(len(PAIRS) * threshold_count)]
    for system, task in zip(systems, tasks):
        for pair_index, local in enumerate(system):
            adjacent_thresholds = []
            if local % 2:
                adjacent_thresholds.append((local - 1) // 2)
            else:
                interval_index = local // 2
                if interval_index < threshold_count:
                    adjacent_thresholds.append(interval_index)
                if interval_index > 0:
                    adjacent_thresholds.append(interval_index - 1)
            key = system[:pair_index] + system[pair_index + 1 :]
            for threshold_index in adjacent_thresholds:
                groups[pair_index * threshold_count + threshold_index][key].add(task)

    return tuple(
        index
        for index, group in enumerate(groups)
        if any(len(task_set) > 1 for task_set in group.values())
    )


@dataclass(frozen=True)
class Tree:
    predicate: int | None
    task: int | None = None
    children: tuple[tuple[int, "Tree"], ...] = ()


def build_tree(signatures, task_ids, weights, forced_root=None):
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
        result = 0
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            result += weights[bit.bit_length() - 1]
        return result

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
            raise AssertionError("sign quotient does not separate tasks")
        return best, best_predicate

    def build(mask, root=None):
        task = pure(mask)
        if task is not None:
            return Tree(None, task=task)
        predicate = root if root is not None else solve(mask)[1]
        children = []
        for sign, branch_mask in zip((-1, 0, 1), predicate_masks[predicate]):
            child = mask & branch_mask
            if child:
                children.append((sign, build(child)))
        return Tree(predicate, children=tuple(children))

    if forced_root is None:
        cost, _ = solve(full_mask)
        return build(full_mask), cost

    child_masks = [full_mask & branch for branch in predicate_masks[forced_root]]
    nonempty = [child for child in child_masks if child]
    costs = [solve(child)[0] for child in nonempty]
    cost = (
        mask_weight(full_mask) + sum(item[0] for item in costs),
        1 + sum(item[1] for item in costs),
        1 + max(item[2] for item in costs),
        1 + sum(item[3] for item in costs),
    )
    return build(full_mask, forced_root), cost


def tree_history(tree, signature):
    result = []
    node = tree
    while node.predicate is not None:
        sign = signature[node.predicate]
        result.append((node.predicate, sign))
        node = dict(node.children)[sign]
    return tuple(result)


def tree_task(tree, signature):
    node = tree
    while node.predicate is not None:
        node = dict(node.children)[signature[node.predicate]]
    return node.task


def widths(histories):
    max_depth = max(map(len, histories))
    result = [1]
    for depth in range(1, max_depth + 1):
        result.append(
            len({history[:depth] for history in histories if len(history) >= depth})
        )
    return tuple(result)


def integer_quadruples(limit):
    return tuple(
        values
        for values in combinations(range(1, limit + 1), 4)
        if Fraction(values[3], values[0]) < RMAX
    )


def direct_task(speeds, max_center=12):
    events = defaultdict(list)
    for runner, speed in enumerate(speeds):
        for alpha, center, kind in contact_events(max_center):
            events[alpha / speed].append((runner, center, kind))
    bad = set(range(K))
    index = 0
    for time in sorted(events):
        index += 1
        group = tuple(sorted(events[time]))
        boundary_runners = {runner for runner, _center, _kind in group}
        bad_on = bad - boundary_runners
        after = set(bad)
        for runner, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            else:
                after.add(runner)
        if not bad_on:
            return (index, group, "interval" if not after else "point")
        bad = after
    raise AssertionError("direct oracle did not find witness")


def signs_for_quad(values, walls):
    return tuple(
        -1 if Fraction(values[j], values[i]) < c else (
            1 if Fraction(values[j], values[i]) > c else 0
        )
        for i, j, c in walls
    )


def main() -> None:
    started = time.time()

    ratios2 = contact_ratios(2)
    ratios3 = contact_ratios(3)
    strata2 = strata(ratios2)
    strata3 = strata(ratios3)
    assert len(ratios2) == 7 and len(strata2) == 15
    assert len(ratios3) == 15 and len(strata3) == 31

    stage = time.time()
    systems2 = enumerate_systems(strata2)
    assert len(systems2) == 5_823
    print(f"center<=2 realizable systems: {len(systems2):,}  ({time.time()-stage:.2f}s)")

    stage = time.time()
    systems3 = refine_systems(systems2, strata2, strata3)
    assert len(systems3) == 72_241
    print(f"center<=3 refined systems:   {len(systems3):,}  ({time.time()-stage:.2f}s)")

    stage = time.time()
    tasks_and_histories = tuple(
        first_witness(system, 3, ratios3, strata3)
        for system in systems3
    )
    tasks3 = tuple(item[0] for item in tasks_and_histories)
    histories3 = tuple(item[1] for item in tasks_and_histories)
    assert len(set(tasks3)) == 75
    print(f"center<=3 task semantics:    {len(set(tasks3)):,}  ({time.time()-stage:.2f}s)")

    relevant3 = relevant_walls(systems3, tasks3, ratios3)
    all_walls3 = tuple(
        (i, j, ratio)
        for i, j in PAIRS
        for ratio in ratios3
    )
    kept_walls3 = tuple(all_walls3[index] for index in relevant3)
    assert len(all_walls3) == 90
    assert len(kept_walls3) == 26

    reduced = defaultdict(set)
    for system, task in zip(systems3, tasks3):
        signature = full_signature(system, ratios3, strata3)
        key = tuple(signature[index] for index in relevant3)
        reduced[key].add(task)
    assert all(len(task_set) == 1 for task_set in reduced.values())
    assert len(reduced) == 1_953

    reduced_signatures = tuple(reduced)
    task_values = sorted(
        {next(iter(task_set)) for task_set in reduced.values()},
        key=repr,
    )
    task_id = {task: index for index, task in enumerate(task_values)}
    item_tasks = tuple(
        task_id[next(iter(reduced[signature]))]
        for signature in reduced_signatures
    )
    reduced_index = {signature: index for index, signature in enumerate(reduced_signatures)}

    training = integer_quadruples(10)
    assert len(training) == 146
    weights = [0] * len(reduced_signatures)
    training_signatures = {}
    for values in training:
        full = signs_for_quad(values, all_walls3)
        key = tuple(full[index] for index in relevant3)
        training_signatures[values] = key
        weights[reduced_index[key]] += 1

    time_tree, time_cost = build_tree(
        reduced_signatures,
        item_tasks,
        tuple(weights),
    )
    assert time_cost == (377, 376, 10, 125)
    assert kept_walls3[time_tree.predicate] == (0, 3, Fraction(4))

    balanced_root = kept_walls3.index((0, 2, Fraction(6)))
    balanced_tree, balanced_cost = build_tree(
        reduced_signatures,
        item_tasks,
        tuple(weights),
        forced_root=balanced_root,
    )
    assert balanced_cost[0] == 505
    assert balanced_cost[1] == 376
    assert balanced_cost[2] == 11

    contact_widths = widths(histories3)
    time_widths = widths(
        tuple(tree_history(time_tree, signature) for signature in reduced_signatures)
    )
    balanced_widths = widths(
        tuple(tree_history(balanced_tree, signature) for signature in reduced_signatures)
    )
    assert max(contact_widths) == 71
    assert sum(contact_widths) == 625
    assert len(contact_widths) - 1 == 16
    assert max(time_widths) == 72
    assert sum(time_widths) == 376
    assert len(time_widths) - 1 == 10
    assert max(balanced_widths) == 63
    assert sum(balanced_widths) == 376
    assert len(balanced_widths) - 1 == 11

    id_to_task = {index: task for task, index in task_id.items()}
    contact_depth = 0
    time_depth = 0
    balanced_depth = 0
    for values in training:
        actual = direct_task(values)
        contact_depth += actual[0]
        signature = training_signatures[values]
        assert id_to_task[tree_task(time_tree, signature)] == actual
        assert id_to_task[tree_task(balanced_tree, signature)] == actual
        time_depth += len(tree_history(time_tree, signature))
        balanced_depth += len(tree_history(balanced_tree, signature))
    assert contact_depth == 779
    assert time_depth == 377
    assert balanced_depth == 505

    # Complete frozen integer transfer through speed 22 in the same r4/r1<8 domain.
    holdout = integer_quadruples(22)
    assert len(holdout) == 5_151
    for values in holdout:
        full = signs_for_quad(values, all_walls3)
        signature = tuple(full[index] for index in relevant3)
        actual = direct_task(values)
        assert id_to_task[tree_task(time_tree, signature)] == actual
        assert id_to_task[tree_task(balanced_tree, signature)] == actual

    # Explicit next calculus-horizon boundary: center 4 is first needed here.
    counterexample = (3, 9, 13, 23)
    full = signs_for_quad(counterexample, all_walls3)
    signature = tuple(full[index] for index in relevant3)
    actual = direct_task(counterexample)
    predicted = id_to_task[tree_task(time_tree, signature)]
    assert predicted != actual

    print()
    print("refinement summary")
    print(f"  naive pair product:  {len(strata2)**6:,} -> {len(strata3)**6:,}")
    print(f"  realizable systems:  {len(systems2):,} -> {len(systems3):,}")
    print(f"  task-safe strata:     849 -> {len(reduced):,}")
    print(f"  task semantics:       60 -> {len(set(tasks3)):,}")
    print(f"  relevant walls:       21 -> {len(kept_walls3):,}")
    print()
    print("center<=3 history geometry")
    print(f"  literal contact: peak={max(contact_widths)} volume={sum(contact_widths)} worst={len(contact_widths)-1} mean={contact_depth/len(training):.3f}")
    print(f"  time-first tree: peak={max(time_widths)} volume={sum(time_widths)} worst={len(time_widths)-1} mean={time_depth/len(training):.3f}")
    print(f"  balanced tree:   peak={max(balanced_widths)} volume={sum(balanced_widths)} worst={len(balanced_widths)-1} mean={balanced_depth/len(training):.3f}")
    print(f"  frozen holdout:  {len(holdout):,}/{len(holdout):,} exact through speed 22")
    print(f"  next horizon counterexample: {counterexample}")
    print()
    print(f"total runtime: {time.time()-started:.2f}s")


if __name__ == "__main__":
    main()
