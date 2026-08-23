"""Phase 11A: exact runner-dimension probe at the five-speed LRC threshold.

For four relative speeds the Sonnet contact-depth axis closed at delta=1/5.
Moving toward five relative speeds changes two things at once:

1. the Lonely Runner threshold changes to delta=1/6;
2. a fifth speed introduces four new pair-difference directions.

This probe separates those effects.  First construct the complete four-speed
center<=2 pair-difference geometry at the *target* delta=1/6.  Then keep every
old four-speed stratum fixed and extend it only through the four new pairs
(3,4), (2,4), (1,4), (0,4).  Exact multiplicative cycle closure prunes each
extension as soon as it becomes impossible.

No five-speed task quotient, completion wall, tree topology, or K=13 data is
supplied.  The purpose is to measure whether adding one runner is already
tractable in the process-native pair-difference representation before designing
any new quotient.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations


DELTA = Fraction(1, 6)
RMAX = Fraction(8)
MAX_CENTER = 2


@dataclass(frozen=True)
class Bound:
    weight: Fraction
    strict: bool = False


@dataclass(frozen=True)
class DimensionProbeResult:
    delta: Fraction
    threshold_count: int
    stratum_count: int
    four_speed_systems: int
    four_speed_tasks: int
    four_speed_unresolved: int
    five_speed_systems: int
    five_speed_tasks: int
    five_speed_unresolved: int
    parent_extension_min: int
    parent_extension_max: int
    parent_extension_mean_num: int
    parent_extension_mean_den: int
    parent_task_multiplicity_histogram: tuple[tuple[int, int], ...]


def tighter(left: Bound, right: Bound | None) -> bool:
    if right is None:
        return True
    return left.weight < right.weight or (
        left.weight == right.weight and left.strict and not right.strict
    )


def compose(left: Bound, right: Bound) -> Bound:
    return Bound(left.weight * right.weight, left.strict or right.strict)


def add_edge(closure, source: int, target: int, weight, strict: bool):
    edge = Bound(Fraction(weight), strict)
    if closure[source][target] is not None and not tighter(edge, closure[source][target]):
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
        if diagonal.weight < 1 or (diagonal.weight == 1 and diagonal.strict):
            return None
    return tuple(tuple(row) for row in updated)


def add_edges(closure, edges):
    state = closure
    for edge in edges:
        state = add_edge(state, *edge)
        if state is None:
            return None
    return state


def initial_closure(k: int):
    rows = [[None] * k for _ in range(k)]
    for vertex in range(k):
        rows[vertex][vertex] = Bound(Fraction(1), False)
    state = tuple(tuple(row) for row in rows)
    result = add_edge(state, 0, k - 1, RMAX, True)
    assert result is not None
    return result


def contact_events(max_center: int = MAX_CENTER):
    events = []
    for center in range(max_center + 1):
        events.append((Fraction(center) + DELTA, center, "exit"))
        if center >= 1:
            events.append((Fraction(center) - DELTA, center, "enter"))
    return tuple(sorted(events))


def contact_ratios(max_center: int = MAX_CENTER):
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


def strata(thresholds):
    output = []
    lower = Fraction(1)
    for threshold in thresholds:
        output.append(("I", lower, threshold))
        output.append(("E", threshold, threshold))
        lower = threshold
    output.append(("I", lower, None))
    return tuple(output)


def pairs(k: int):
    return tuple(combinations(range(k), 2))


def extension_order(k: int):
    """Close each newly introduced vertex against all previous vertices."""

    output = []
    for last in range(1, k):
        for first in range(last - 1, -1, -1):
            output.append((first, last))
    return tuple(output)


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


def enumerate_systems(k: int, pair_strata):
    canonical_pairs = pairs(k)
    order = extension_order(k)
    base = initial_closure(k)
    systems = []

    def visit(depth, closure, choices):
        if depth == len(order):
            systems.append(tuple(choices[pair] for pair in canonical_pairs))
            return
        pair = order[depth]
        for index, item in enumerate(pair_strata):
            next_closure = add_edges(closure, stratum_edges(pair, item))
            if next_closure is None:
                continue
            choices[pair] = index
            visit(depth + 1, next_closure, choices)
            del choices[pair]

    visit(0, base, {})
    return tuple(systems)


def sign_of(item, threshold: Fraction) -> int:
    kind, lower, upper = item
    if kind == "E":
        return -1 if lower < threshold else (1 if lower > threshold else 0)
    if upper is not None and upper <= threshold:
        return -1
    if lower >= threshold:
        return 1
    raise AssertionError((item, threshold))


def ratio_relation(system, pair, ratio, pair_strata, pair_index):
    if ratio <= 1:
        return 1
    if ratio >= RMAX:
        return -1
    return sign_of(pair_strata[system[pair_index[pair]]], ratio)


def first_witness(system, k: int, pair_strata, max_center: int = MAX_CENTER):
    canonical_pairs = pairs(k)
    pair_index = {pair: index for index, pair in enumerate(canonical_pairs)}
    events = [
        (runner, alpha, center, kind)
        for runner in range(k)
        for alpha, center, kind in contact_events(max_center)
    ]

    def compare(left, right):
        i, alpha, _center_i, _kind_i = left
        j, beta, _center_j, _kind_j = right
        if i == j:
            return -1 if alpha < beta else (1 if alpha > beta else 0)
        if i < j:
            return ratio_relation(system, (i, j), beta / alpha, pair_strata, pair_index)
        return -ratio_relation(system, (j, i), alpha / beta, pair_strata, pair_index)

    ordered = sorted(events, key=cmp_to_key(compare))
    bad = set(range(k))
    cursor = 0
    event_index = 0
    while cursor < len(ordered):
        group = [ordered[cursor]]
        cursor += 1
        while cursor < len(ordered) and compare(group[0], ordered[cursor]) == 0:
            group.append(ordered[cursor])
            cursor += 1
        event_index += 1

        boundary_runners = {runner for runner, _a, _n, _kind in group}
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
        if not bad_on:
            mode = "interval" if not after else "point"
            return (event_index, boundary, mode)
        bad = after

    return ("unresolved-through-center", max_center)


def closure_from_old_system(old_system, pair_strata):
    """Embed a complete four-speed stratum into the five-speed closure."""

    old_pairs = pairs(4)
    old_index = {pair: index for index, pair in enumerate(old_pairs)}
    closure = initial_closure(5)
    for pair in extension_order(4):
        item = pair_strata[old_system[old_index[pair]]]
        closure = add_edges(closure, stratum_edges(pair, item))
        assert closure is not None
    return closure


def extend_with_fifth_runner(old_system, pair_strata):
    """Yield exact five-speed systems extending one fixed four-speed system."""

    pairs5 = pairs(5)
    index5 = {pair: index for index, pair in enumerate(pairs5)}
    old_pairs = pairs(4)
    old_index = {pair: index for index, pair in enumerate(old_pairs)}
    choices = {pair: old_system[old_index[pair]] for pair in old_pairs}
    closure0 = closure_from_old_system(old_system, pair_strata)
    new_pairs = ((3, 4), (2, 4), (1, 4), (0, 4))

    def visit(depth, closure):
        if depth == len(new_pairs):
            yield tuple(choices[pair] for pair in pairs5)
            return
        pair = new_pairs[depth]
        for index, item in enumerate(pair_strata):
            next_closure = add_edges(closure, stratum_edges(pair, item))
            if next_closure is None:
                continue
            choices[pair] = index
            yield from visit(depth + 1, next_closure)
            del choices[pair]

    yield from visit(0, closure0)


def analyze_five_speed_dimension_probe() -> DimensionProbeResult:
    thresholds = contact_ratios()
    pair_strata = strata(thresholds)
    assert len(thresholds) == 8
    assert len(pair_strata) == 17

    systems4 = enumerate_systems(4, pair_strata)
    tasks4 = tuple(first_witness(system, 4, pair_strata) for system in systems4)

    task5_values = set()
    unresolved5 = 0
    total5 = 0
    extension_counts = []
    task_multiplicity = Counter()

    for old_system in systems4:
        count = 0
        child_tasks = set()
        for system5 in extend_with_fifth_runner(old_system, pair_strata):
            count += 1
            total5 += 1
            task = first_witness(system5, 5, pair_strata)
            child_tasks.add(task)
            task5_values.add(task)
            if task[0] == "unresolved-through-center":
                unresolved5 += 1
        assert count > 0
        extension_counts.append(count)
        task_multiplicity[len(child_tasks)] += 1

    unresolved4 = sum(task[0] == "unresolved-through-center" for task in tasks4)
    total_extensions = sum(extension_counts)
    assert total_extensions == total5

    return DimensionProbeResult(
        delta=DELTA,
        threshold_count=len(thresholds),
        stratum_count=len(pair_strata),
        four_speed_systems=len(systems4),
        four_speed_tasks=len(set(tasks4)),
        four_speed_unresolved=unresolved4,
        five_speed_systems=total5,
        five_speed_tasks=len(task5_values),
        five_speed_unresolved=unresolved5,
        parent_extension_min=min(extension_counts),
        parent_extension_max=max(extension_counts),
        parent_extension_mean_num=total_extensions,
        parent_extension_mean_den=len(extension_counts),
        parent_task_multiplicity_histogram=tuple(sorted(task_multiplicity.items())),
    )


def main() -> None:
    result = analyze_five_speed_dimension_probe()
    print("Phase 11A exact five-speed dimension probe")
    print(f"  delta:                       {result.delta}")
    print(f"  contact ratios / strata:     {result.threshold_count} / {result.stratum_count}")
    print("  four-speed target-threshold base")
    print(f"    exact systems:              {result.four_speed_systems}")
    print(f"    task semantics:             {result.four_speed_tasks}")
    print(f"    unresolved through c2:      {result.four_speed_unresolved}")
    print("  add fifth speed only")
    print(f"    exact systems:              {result.five_speed_systems}")
    print(f"    task semantics:             {result.five_speed_tasks}")
    print(f"    unresolved through c2:      {result.five_speed_unresolved}")
    print(f"    extensions per old system:  {result.parent_extension_min} .. {result.parent_extension_max}")
    print(f"    mean extensions:            {result.parent_extension_mean_num}/{result.parent_extension_mean_den}")
    print(f"    child-task multiplicities:  {result.parent_task_multiplicity_histogram}")


if __name__ == "__main__":
    main()
