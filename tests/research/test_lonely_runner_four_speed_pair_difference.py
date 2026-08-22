"""Four relative speeds: pair-difference sign systems instead of ambient 3D cells.

This file responds to the Phase-7e red team.  The A/M contact walls have the
special form

    x_j - x_i = log(c)

or equivalently, without introducing transcendental coordinates,

    u_j = c * u_i.

A candidate stratum is therefore a labeled graph of pairwise < / = / >
relations.  Joint realizability is not arbitrary: every graph cycle must be
consistent.  We certify consistency exactly with multiplicative difference
constraints, where path composition multiplies rational contact ratios.

The fast regression checks the graph-consistency mechanism on a shallow contact
alphabet.  The full center<=2 census is deliberately opt-in because it is a
research benchmark, not a routine five-version CI gate.  Set

    AEG_RUN_LR_PAIR_DIFF_CENSUS=1

to run the complete bounded census and Hauffman/history-geometry comparison.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key, lru_cache
from itertools import combinations
import os

import pytest


FINAL_K = 4
DELTA = Fraction(1, 5)
MAX_RATIO = Fraction(8)
RUN_FULL_CENSUS = os.environ.get("AEG_RUN_LR_PAIR_DIFF_CENSUS") == "1"
PAIR_ORDER = tuple(combinations(range(FINAL_K), 2))
DFS_PAIR_ORDER = ((0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3))


@dataclass(frozen=True)
class Bound:
    """Exact logarithmic upper bound stored multiplicatively.

    ``x_v - x_u <= log(weight)`` when ``strict`` is false and ``<`` when true.
    Products of rational weights represent sums of logarithmic bounds exactly.
    """

    weight: Fraction
    strict: bool = False


def tighter(left: Bound, right: Bound | None) -> bool:
    if right is None:
        return True
    return (
        left.weight < right.weight
        or (
            left.weight == right.weight
            and left.strict
            and not right.strict
        )
    )


def difference_constraints_feasible(
    vertex_count: int,
    edges: tuple[tuple[int, int, Fraction, bool], ...],
) -> bool:
    """Exact all-pairs closure for multiplicative difference constraints.

    A cycle is impossible iff its product bound is <1, or equals 1 while at
    least one edge is strict.  This is the exact multiplicative analogue of a
    negative-cycle test in ordinary difference constraints.
    """

    dist: list[list[Bound | None]] = [
        [None] * vertex_count for _ in range(vertex_count)
    ]
    for index in range(vertex_count):
        dist[index][index] = Bound(Fraction(1), False)

    for source, target, weight, strict in edges:
        candidate = Bound(Fraction(weight), bool(strict))
        if tighter(candidate, dist[source][target]):
            dist[source][target] = candidate

    for middle in range(vertex_count):
        for source in range(vertex_count):
            left = dist[source][middle]
            if left is None:
                continue
            for target in range(vertex_count):
                right = dist[middle][target]
                if right is None:
                    continue
                candidate = Bound(
                    left.weight * right.weight,
                    left.strict or right.strict,
                )
                if tighter(candidate, dist[source][target]):
                    dist[source][target] = candidate

    for index in range(vertex_count):
        diagonal = dist[index][index]
        assert diagonal is not None
        if diagonal.weight < 1:
            return False
        if diagonal.weight == 1 and diagonal.strict:
            return False
    return True


def contact_events(max_center: int) -> tuple[tuple[Fraction, int, str], ...]:
    events: list[tuple[Fraction, int, str]] = []
    for center in range(max_center + 1):
        events.append((Fraction(center) + DELTA, center, "exit"))
        if center >= 1:
            events.append((Fraction(center) - DELTA, center, "enter"))
    return tuple(sorted(events))


def contact_ratios(max_center: int) -> tuple[Fraction, ...]:
    constants = tuple(value for value, _center, _kind in contact_events(max_center))
    return tuple(
        sorted(
            {
                beta / alpha
                for alpha in constants
                for beta in constants
                if 1 < beta / alpha < MAX_RATIO
            }
        )
    )


def pair_strata(thresholds: tuple[Fraction, ...]) -> tuple[tuple[str, Fraction, Fraction | None], ...]:
    """Ordered strata for one ratio q=u_j/u_i > 1."""

    result: list[tuple[str, Fraction, Fraction | None]] = []
    lower = Fraction(1)
    for threshold in thresholds:
        result.append(("interval", lower, threshold))
        result.append(("equal", threshold, threshold))
        lower = threshold
    result.append(("interval", lower, None))
    return tuple(result)


def stratum_edges(
    pair: tuple[int, int],
    stratum: tuple[str, Fraction, Fraction | None],
) -> tuple[tuple[int, int, Fraction, bool], ...]:
    """Translate one ratio stratum into exact graph difference constraints."""

    first, second = pair
    kind, lower, upper = stratum
    if kind == "equal":
        return (
            (first, second, lower, False),
            (second, first, Fraction(1, 1) / lower, False),
        )

    edges: list[tuple[int, int, Fraction, bool]] = [
        # q > lower  <=>  x_first - x_second < -log(lower).
        (second, first, Fraction(1, 1) / lower, True),
    ]
    if upper is not None:
        edges.append((first, second, upper, True))
    return tuple(edges)


def enumerate_consistent_systems(
    max_center: int,
) -> tuple[
    tuple[Fraction, ...],
    tuple[tuple[str, Fraction, Fraction | None], ...],
    tuple[tuple[int, ...], ...],
]:
    """Enumerate only graph-realizable pair-stratum assignments.

    The ambient ratio domain is ``u4/u1 < 8``.  The DFS ordering closes
    triangles early, so cycle consistency prunes impossible combinations before
    all six pair coordinates have been assigned.
    """

    thresholds = contact_ratios(max_center)
    strata = pair_strata(thresholds)
    canonical_pair_index = {pair: index for index, pair in enumerate(PAIR_ORDER)}
    base_edges = ((0, 3, MAX_RATIO, True),)
    systems: list[tuple[int, ...]] = []

    def visit(
        depth: int,
        edges: tuple[tuple[int, int, Fraction, bool], ...],
        chosen: dict[tuple[int, int], int],
    ) -> None:
        if depth == len(DFS_PAIR_ORDER):
            systems.append(
                tuple(chosen[pair] for pair in PAIR_ORDER)
            )
            return

        pair = DFS_PAIR_ORDER[depth]
        for stratum_index, stratum in enumerate(strata):
            next_edges = edges + stratum_edges(pair, stratum)
            if not difference_constraints_feasible(
                FINAL_K,
                base_edges + next_edges,
            ):
                continue
            chosen[pair] = stratum_index
            visit(depth + 1, next_edges, chosen)
            del chosen[pair]

    visit(0, (), {})
    # The dictionary is only used to rebuild canonical pair order; this assert
    # catches accidental changes to the six-pair grammar.
    assert len(canonical_pair_index) == 6
    return thresholds, strata, tuple(systems)


def sign_of_stratum(
    stratum: tuple[str, Fraction, Fraction | None],
    threshold: Fraction,
) -> int:
    kind, lower, upper = stratum
    if kind == "equal":
        if lower < threshold:
            return -1
        if lower > threshold:
            return 1
        return 0

    if upper is not None and upper <= threshold:
        return -1
    if lower >= threshold:
        return 1
    raise AssertionError("threshold must be a boundary of the declared strata")


def full_signature(
    system: tuple[int, ...],
    thresholds: tuple[Fraction, ...],
    strata: tuple[tuple[str, Fraction, Fraction | None], ...],
) -> tuple[int, ...]:
    return tuple(
        sign_of_stratum(strata[system[pair_index]], threshold)
        for pair_index, _pair in enumerate(PAIR_ORDER)
        for threshold in thresholds
    )


def system_ratio_relation(
    system: tuple[int, ...],
    pair: tuple[int, int],
    ratio: Fraction,
    *,
    thresholds: tuple[Fraction, ...],
    strata: tuple[tuple[str, Fraction, Fraction | None], ...],
) -> int:
    """Return sign(q-ratio) for one pair ratio q=u_j/u_i."""

    if ratio <= 1:
        return 1
    # The declared domain is strict: every pair ratio is < u4/u1 < MAX_RATIO.
    if ratio >= MAX_RATIO:
        return -1
    pair_index = PAIR_ORDER.index(pair)
    return sign_of_stratum(strata[system[pair_index]], ratio)


def first_witness_from_system(
    system: tuple[int, ...],
    *,
    max_center: int,
    thresholds: tuple[Fraction, ...],
    strata: tuple[tuple[str, Fraction, Fraction | None], ...],
) -> tuple[tuple[object, ...], tuple[tuple[object, ...], ...]]:
    """Derive first-witness semantics directly from a consistent sign graph.

    No ambient 3D representative is constructed.  The sign system itself orders
    all contact events because equality of two event times is exactly one
    pair-ratio comparison generated by the A/M contact calculus.
    """

    events = tuple(
        (runner, alpha, center, kind)
        for runner in range(FINAL_K)
        for alpha, center, kind in contact_events(max_center)
    )

    def compare(left, right) -> int:
        left_runner, left_alpha, _left_center, _left_kind = left
        right_runner, right_alpha, _right_center, _right_kind = right
        if left_runner == right_runner:
            if left_alpha < right_alpha:
                return -1
            if left_alpha > right_alpha:
                return 1
            return 0

        if left_runner < right_runner:
            # tau_left < tau_right iff q=u_right/u_left < beta/alpha.
            return system_ratio_relation(
                system,
                (left_runner, right_runner),
                right_alpha / left_alpha,
                thresholds=thresholds,
                strata=strata,
            )

        # Reverse the lower/higher-runner comparison.
        return -system_ratio_relation(
            system,
            (right_runner, left_runner),
            left_alpha / right_alpha,
            thresholds=thresholds,
            strata=strata,
        )

    ordered = sorted(events, key=cmp_to_key(compare))
    bad = set(range(FINAL_K))
    steps: list[tuple[object, ...]] = []
    cursor = 0
    event_index = 0

    while cursor < len(ordered):
        group = [ordered[cursor]]
        cursor += 1
        while cursor < len(ordered) and compare(group[0], ordered[cursor]) == 0:
            group.append(ordered[cursor])
            cursor += 1
        event_index += 1

        boundary_runners = {runner for runner, _alpha, _center, _kind in group}
        bad_on = tuple(sorted(bad - boundary_runners))
        after = set(bad)
        for runner, _alpha, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            else:
                after.add(runner)

        boundary = tuple(
            sorted((runner, center, kind) for runner, _alpha, center, kind in group)
        )
        step = (boundary, bad_on, tuple(sorted(after)))
        steps.append(step)
        if not bad_on:
            mode = "interval" if not after else "point"
            return (event_index, boundary, mode), tuple(steps)
        bad = after

    raise AssertionError("bounded contact alphabet did not produce a witness")


def task_relevant_walls(
    signatures: tuple[tuple[int, ...], ...],
    tasks: tuple[tuple[object, ...], ...],
) -> tuple[int, ...]:
    relevant: list[int] = []
    for wall_index in range(len(signatures[0])):
        groups: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
        for signature, task in zip(signatures, tasks):
            key = signature[:wall_index] + signature[wall_index + 1 :]
            groups[key].add(task)
        if any(len(task_set) > 1 for task_set in groups.values()):
            relevant.append(wall_index)
    return tuple(relevant)


@dataclass(frozen=True)
class DecisionTree:
    predicate: int | None
    task: int | None = None
    children: tuple[tuple[int, "DecisionTree"], ...] = ()


def build_optimal_tree(
    signatures: tuple[tuple[int, ...], ...],
    task_ids: tuple[int, ...],
    weights: tuple[int, ...],
    *,
    forced_root: int | None = None,
) -> tuple[DecisionTree, tuple[int, int, int, int]]:
    """Exact Hauffman-style tree search on task-safe sign strata.

    The lexicographic objective is

    1. usage-weighted decision depth (time axis),
    2. total tree nodes = boundary volume (space axis),
    3. worst decision depth,
    4. internal decision nodes.

    A forced root is useful for sampling nearby space/time Pareto points without
    scalarizing the two axes into one hidden objective.
    """

    item_count = len(signatures)
    predicate_count = len(signatures[0])
    full_mask = (1 << item_count) - 1

    predicate_masks: list[tuple[int, int, int]] = []
    for predicate in range(predicate_count):
        masks = [0, 0, 0]
        for item, signature in enumerate(signatures):
            masks[signature[predicate] + 1] |= 1 << item
        predicate_masks.append(tuple(masks))

    task_masks: dict[int, int] = {}
    for task in sorted(set(task_ids)):
        mask = 0
        for item, item_task in enumerate(task_ids):
            if item_task == task:
                mask |= 1 << item
        task_masks[task] = mask

    @lru_cache(maxsize=None)
    def pure_task(mask: int) -> int | None:
        found: int | None = None
        for task, task_mask in task_masks.items():
            if not (mask & task_mask):
                continue
            if found is not None:
                return None
            found = task
        return found

    @lru_cache(maxsize=None)
    def mask_weight(mask: int) -> int:
        total = 0
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            total += weights[bit.bit_length() - 1]
        return total

    @lru_cache(maxsize=None)
    def solve(mask: int) -> tuple[tuple[int, int, int, int], int | None]:
        task = pure_task(mask)
        if task is not None:
            # One leaf contributes one node to the boundary volume.
            return (0, 1, 0, 0), None

        total_weight = mask_weight(mask)
        best: tuple[int, int, int, int] | None = None
        best_predicate: int | None = None

        for predicate, masks in enumerate(predicate_masks):
            children = [mask & branch for branch in masks]
            nonempty = [child for child in children if child]
            if len(nonempty) <= 1:
                continue

            child_costs = [solve(child)[0] for child in nonempty]
            candidate = (
                total_weight + sum(cost[0] for cost in child_costs),
                1 + sum(cost[1] for cost in child_costs),
                1 + max(cost[2] for cost in child_costs),
                1 + sum(cost[3] for cost in child_costs),
            )
            if best is None or candidate < best:
                best = candidate
                best_predicate = predicate

        if best is None:
            raise AssertionError("retained signs do not separate task semantics")
        return best, best_predicate

    def build(mask: int, root_override: int | None = None) -> DecisionTree:
        task = pure_task(mask)
        if task is not None:
            return DecisionTree(predicate=None, task=task)

        predicate = root_override if root_override is not None else solve(mask)[1]
        assert predicate is not None
        children: list[tuple[int, DecisionTree]] = []
        for branch_value, branch_mask in zip((-1, 0, 1), predicate_masks[predicate]):
            child = mask & branch_mask
            if child:
                children.append((branch_value, build(child)))
        return DecisionTree(predicate=predicate, children=tuple(children))

    if forced_root is None:
        cost, _predicate = solve(full_mask)
        return build(full_mask), cost

    root_children = [full_mask & branch for branch in predicate_masks[forced_root]]
    nonempty = [child for child in root_children if child]
    if len(nonempty) <= 1:
        raise ValueError("forced root does not split the task geometry")
    child_costs = [solve(child)[0] for child in nonempty]
    forced_cost = (
        mask_weight(full_mask) + sum(cost[0] for cost in child_costs),
        1 + sum(cost[1] for cost in child_costs),
        1 + max(cost[2] for cost in child_costs),
        1 + sum(cost[3] for cost in child_costs),
    )
    return build(full_mask, forced_root), forced_cost


def decision_history(
    tree: DecisionTree,
    signature: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    history: list[tuple[int, int]] = []
    node = tree
    while node.predicate is not None:
        branch = signature[node.predicate]
        history.append((node.predicate, branch))
        node = dict(node.children)[branch]
    return tuple(history)


def classify(tree: DecisionTree, signature: tuple[int, ...]) -> int:
    node = tree
    while node.predicate is not None:
        node = dict(node.children)[signature[node.predicate]]
    assert node.task is not None
    return node.task


def boundary_widths(histories: tuple[tuple[object, ...], ...]) -> tuple[int, ...]:
    max_depth = max((len(history) for history in histories), default=0)
    widths = [1]
    for depth in range(1, max_depth + 1):
        widths.append(
            len(
                {
                    history[:depth]
                    for history in histories
                    if len(history) >= depth
                }
            )
        )
    return tuple(widths)


def integer_quadruples(limit: int) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        values
        for values in combinations(range(1, limit + 1), FINAL_K)
        if Fraction(values[-1], values[0]) < MAX_RATIO
    )


def signature_of_quadruple(
    values: tuple[int, int, int, int],
    walls: tuple[tuple[int, int, Fraction], ...],
) -> tuple[int, ...]:
    result: list[int] = []
    for first, second, threshold in walls:
        ratio = Fraction(values[second], values[first])
        result.append(-1 if ratio < threshold else (1 if ratio > threshold else 0))
    return tuple(result)


def direct_first_witness(
    speeds: tuple[int, int, int, int],
    *,
    max_center: int = 12,
) -> tuple[object, ...]:
    events: dict[Fraction, list[tuple[int, int, str]]] = defaultdict(list)
    for runner, speed in enumerate(speeds):
        for alpha, center, kind in contact_events(max_center):
            events[alpha / speed].append((runner, center, kind))

    bad = set(range(FINAL_K))
    event_index = 0
    for time in sorted(events):
        del time
        event_index += 1
        group = tuple(sorted(events[_time] if False else ()))

    # Re-run without the intentionally-unused loop variable trick above; this
    # keeps MyPy/linters irrelevant while making the exact event grouping clear.
    bad = set(range(FINAL_K))
    event_index = 0
    for time in sorted(events):
        event_index += 1
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
            mode = "interval" if not after else "point"
            return (event_index, group, mode)
        bad = after
    raise AssertionError("direct oracle did not find a witness")


def test_multiplicative_cycle_consistency_is_exact_and_fast() -> None:
    # q01<3/2 and q12<3/2 force q02<9/4.  Asking simultaneously for
    # q02>9/4 creates an exact strict cycle of product one and must be rejected.
    impossible = (
        (0, 1, Fraction(3, 2), True),
        (1, 2, Fraction(3, 2), True),
        (2, 0, Fraction(4, 9), True),
    )
    assert not difference_constraints_feasible(3, impossible)

    possible = impossible[:-1] + (
        (2, 0, Fraction(1, 2), True),
    )
    assert difference_constraints_feasible(3, possible)

    # Shallow census: 3 contact ratios -> 7 strata on each of six pair edges.
    # Naive independent enumeration is 7^6=117,649; cycle consistency leaves
    # only 269 realizable joint sign systems.  This stays sub-second scale in the
    # intended research environment and is safe for routine CI.
    thresholds, strata, systems = enumerate_consistent_systems(max_center=1)
    assert thresholds == (Fraction(3, 2), Fraction(4), Fraction(6))
    assert len(strata) == 7
    assert len(strata) ** len(PAIR_ORDER) == 117_649
    assert len(systems) == 269


@pytest.mark.skipif(
    not RUN_FULL_CENSUS,
    reason="full four-speed pair-difference census is a manual research benchmark",
)
def test_full_pair_difference_census_and_hauffman_frontier() -> None:
    thresholds, strata, systems = enumerate_consistent_systems(max_center=2)
    assert thresholds == (
        Fraction(11, 9),
        Fraction(3, 2),
        Fraction(11, 6),
        Fraction(9, 4),
        Fraction(11, 4),
        Fraction(4),
        Fraction(6),
    )
    assert len(strata) == 15
    assert len(strata) ** len(PAIR_ORDER) == 11_390_625
    assert len(systems) == 5_823

    signatures = tuple(full_signature(system, thresholds, strata) for system in systems)
    tasks_and_histories = tuple(
        first_witness_from_system(
            system,
            max_center=2,
            thresholds=thresholds,
            strata=strata,
        )
        for system in systems
    )
    tasks = tuple(item[0] for item in tasks_and_histories)
    contact_histories = tuple(item[1] for item in tasks_and_histories)
    assert len(set(tasks)) == 60

    walls = tuple(
        (first, second, threshold)
        for first, second in PAIR_ORDER
        for threshold in thresholds
    )
    relevant = task_relevant_walls(signatures, tasks)
    relevant_walls = tuple(walls[index] for index in relevant)
    assert len(walls) == 42
    assert len(relevant_walls) == 21
    assert relevant_walls == (
        (0, 1, Fraction(4)), (0, 1, Fraction(6)),
        (0, 2, Fraction(4)), (0, 2, Fraction(6)),
        (0, 3, Fraction(4)), (0, 3, Fraction(6)),
        (1, 2, Fraction(3, 2)), (1, 2, Fraction(11, 6)),
        (1, 2, Fraction(4)), (1, 2, Fraction(6)),
        (1, 3, Fraction(3, 2)), (1, 3, Fraction(11, 6)),
        (1, 3, Fraction(9, 4)), (1, 3, Fraction(11, 4)),
        (1, 3, Fraction(4)), (1, 3, Fraction(6)),
        (2, 3, Fraction(11, 9)), (2, 3, Fraction(3, 2)),
        (2, 3, Fraction(11, 6)), (2, 3, Fraction(4)),
        (2, 3, Fraction(6)),
    )

    reduced_task_sets: dict[tuple[int, ...], set[tuple[object, ...]]] = defaultdict(set)
    for signature, task in zip(signatures, tasks):
        reduced = tuple(signature[index] for index in relevant)
        reduced_task_sets[reduced].add(task)
    assert all(len(task_set) == 1 for task_set in reduced_task_sets.values())
    assert len(reduced_task_sets) == 849

    reduced_signatures = tuple(reduced_task_sets)
    task_values = sorted(
        {next(iter(task_set)) for task_set in reduced_task_sets.values()},
        key=repr,
    )
    task_ids = {task: index for index, task in enumerate(task_values)}
    item_tasks = tuple(
        task_ids[next(iter(reduced_task_sets[signature]))]
        for signature in reduced_signatures
    )
    reduced_index = {signature: index for index, signature in enumerate(reduced_signatures)}

    # Usage weights are introduced only after the complete bounded geometry and
    # exact task quotient are frozen.
    training = integer_quadruples(8)
    assert len(training) == 55
    weights = [0] * len(reduced_signatures)
    reduced_signature_for_quad: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    for values in training:
        full = signature_of_quadruple(values, walls)
        reduced = tuple(full[index] for index in relevant)
        reduced_signature_for_quad[values] = reduced
        weights[reduced_index[reduced]] += 1

    time_tree, time_cost = build_optimal_tree(
        reduced_signatures,
        item_tasks,
        tuple(weights),
    )
    assert time_cost == (135, 328, 9, 109)
    assert relevant_walls[time_tree.predicate] == (0, 3, Fraction(4))

    # A nearby Pareto point is forced through r3/u1=6 at the root.  It gives up
    # some expected depth to reduce the peak frontier below the literal contact
    # process, producing simultaneous space/time dominance.
    balanced_root = relevant_walls.index((0, 2, Fraction(6)))
    balanced_tree, balanced_cost = build_optimal_tree(
        reduced_signatures,
        item_tasks,
        tuple(weights),
        forced_root=balanced_root,
    )
    assert balanced_cost == (174, 328, 9, 109)

    contact_widths = boundary_widths(contact_histories)
    time_widths = boundary_widths(
        tuple(decision_history(time_tree, signature) for signature in reduced_signatures)
    )
    balanced_widths = boundary_widths(
        tuple(decision_history(balanced_tree, signature) for signature in reduced_signatures)
    )
    assert contact_widths == (
        1, 1, 3, 9, 27, 49, 65, 71, 67, 64, 62, 58, 40, 17, 10,
    )
    assert time_widths == (1, 3, 3, 9, 27, 48, 63, 69, 72, 33)
    assert balanced_widths == (1, 3, 9, 15, 30, 45, 54, 57, 69, 45)

    assert max(contact_widths) == 71
    assert sum(contact_widths) == 544
    assert max(time_widths) == 72
    assert sum(time_widths) == 328
    assert max(balanced_widths) == 69
    assert sum(balanced_widths) == 328

    # Exact usage-depth comparison on the 55 training quadruples.
    id_to_task = {index: task for task, index in task_ids.items()}
    contact_depth = 0
    time_depth = 0
    balanced_depth = 0
    for values in training:
        actual = direct_first_witness(values)
        contact_depth += actual[0]
        reduced = reduced_signature_for_quad[values]
        predicted_time = id_to_task[classify(time_tree, reduced)]
        predicted_balanced = id_to_task[classify(balanced_tree, reduced)]
        assert predicted_time == actual
        assert predicted_balanced == actual
        time_depth += len(decision_history(time_tree, reduced))
        balanced_depth += len(decision_history(balanced_tree, reduced))

    assert contact_depth == 280
    assert time_depth == 135
    assert balanced_depth == 174

    # The balanced Pareto point improves every recorded Hauffman/history axis.
    assert max(balanced_widths) < max(contact_widths)
    assert sum(balanced_widths) < sum(contact_widths)
    assert len(balanced_widths) - 1 < len(contact_widths) - 1
    assert balanced_depth < contact_depth

    # Frozen-transfer gate: no new wall or task semantics through speed 13.
    holdout = integer_quadruples(13)
    assert len(holdout) == 515
    for values in holdout:
        full = signature_of_quadruple(values, walls)
        reduced = tuple(full[index] for index in relevant)
        actual = direct_first_witness(values)
        assert id_to_task[classify(time_tree, reduced)] == actual
        assert id_to_task[classify(balanced_tree, reduced)] == actual

    # And an explicit boundary of the bounded contact alphabet: center<=2 is no
    # longer complete at speed 14.  This is a calculus-horizon failure, not a
    # sample-interpolation failure, and it tells the next phase exactly what must
    # be objectified instead of silently increasing the training set.
    counterexample = (2, 6, 9, 14)
    full = signature_of_quadruple(counterexample, walls)
    reduced = tuple(full[index] for index in relevant)
    actual = direct_first_witness(counterexample)
    predicted = id_to_task[classify(time_tree, reduced)]
    assert predicted != actual
