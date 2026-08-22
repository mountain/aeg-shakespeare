"""Three relative speeds: exact A/M contact arrangement plus history geometry.

This is the first 2D relative-M calibration for Sonnet 001.  After quotienting
one global multiplicative scale, write

    r2 = u2/u1,   r3 = u3/u1,   1 < r2 < r3 <= 8.

Equality of lifted contact times can only create three A/M-native wall families:

    r2 = c,       r3 = c,       r3 = c*r2,

where c=beta/alpha is a ratio of primitive contact constants n +/- 1/4.

The test constructs the exact rational line arrangement without a geometry
library, evaluates the first-witness observer on every 0D/1D/2D stratum, removes
walls that never change task semantics, and then searches the minimum expected
depth ternary wall tree under a separate finite usage distribution.

The history-geometry comparison is deliberately two-axis: the selected wall tree
must improve both boundary width (space-like complexity) and stopping depth
(time-like complexity) over the literal event-by-event contact process.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import math

from aeg_shakespeare.history_geometry import boundary_profile
from aeg_shakespeare.process.history import ProcessWord


Point = tuple[Fraction, Fraction]
Wall = tuple[str, Fraction]
Task = tuple[object, ...]

FINAL_K = 3
DELTA = Fraction(1, 4)
MAX_RATIO = Fraction(8)
MAX_CONTACT_CENTER_FOR_WALLS = 3
TASK_ORACLE_CENTER_LIMIT = 12


def contact_constants(max_center: int) -> tuple[Fraction, ...]:
    values: set[Fraction] = set()
    for center in range(max_center + 1):
        values.add(Fraction(center) + DELTA)
        if center >= 1:
            values.add(Fraction(center) - DELTA)
    return tuple(sorted(value for value in values if value > 0))


def contact_ratios(max_center: int) -> tuple[Fraction, ...]:
    values = contact_constants(max_center)
    return tuple(
        sorted(
            {
                beta / alpha
                for alpha in values
                for beta in values
                if 1 < beta / alpha < MAX_RATIO
            }
        )
    )


def candidate_walls() -> tuple[Wall, ...]:
    walls: list[Wall] = []
    for ratio in contact_ratios(MAX_CONTACT_CENTER_FOR_WALLS):
        walls.extend((('V', ratio), ('H', ratio), ('D', ratio)))
    return tuple(walls)


def boundary_lines() -> tuple[tuple[str, Fraction | None], ...]:
    return (('X1', None), ('YR', None), ('DIAG', None))


def coefficients(line: tuple[str, Fraction | None]) -> tuple[Fraction, Fraction, Fraction]:
    kind, value = line
    if kind == 'V':
        assert value is not None
        return Fraction(1), Fraction(0), value
    if kind == 'H':
        assert value is not None
        return Fraction(0), Fraction(1), value
    if kind == 'D':
        assert value is not None
        return -value, Fraction(1), Fraction(0)
    if kind == 'X1':
        return Fraction(1), Fraction(0), Fraction(1)
    if kind == 'YR':
        return Fraction(0), Fraction(1), MAX_RATIO
    if kind == 'DIAG':
        return Fraction(-1), Fraction(1), Fraction(0)
    raise ValueError(kind)


def line_intersection(
    left: tuple[str, Fraction | None],
    right: tuple[str, Fraction | None],
) -> Point | None:
    a, b, d = coefficients(left)
    e, f, g = coefficients(right)
    determinant = a * f - b * e
    if determinant == 0:
        return None
    return (
        (d * f - b * g) / determinant,
        (a * g - d * e) / determinant,
    )


def in_domain_closure(point: Point) -> bool:
    r2, r3 = point
    return r2 >= 1 and r3 >= r2 and r3 <= MAX_RATIO


def in_domain_interior(point: Point) -> bool:
    r2, r3 = point
    return r2 > 1 and r3 > r2 and r3 < MAX_RATIO


def on_line(point: Point, line: tuple[str, Fraction | None]) -> bool:
    a, b, d = coefficients(line)
    r2, r3 = point
    return a * r2 + b * r3 == d


def wall_sign(point: Point, wall: Wall) -> int:
    r2, r3 = point
    kind, value = wall
    if kind == 'V':
        residual = r2 - value
    elif kind == 'H':
        residual = r3 - value
    elif kind == 'D':
        residual = r3 - value * r2
    else:  # pragma: no cover - walls are constructed above
        raise AssertionError(kind)
    return -1 if residual < 0 else (1 if residual > 0 else 0)


def signature(point: Point, walls: tuple[Wall, ...]) -> tuple[int, ...]:
    return tuple(wall_sign(point, wall) for wall in walls)


def arrangement_representatives(walls: tuple[Wall, ...]) -> dict[tuple[int, ...], Point]:
    """One exact rational representative for every 0D/1D/2D arrangement stratum."""

    lines: tuple[tuple[str, Fraction | None], ...] = walls + boundary_lines()
    vertices: set[Point] = set()
    for index, left in enumerate(lines):
        for right in lines[index + 1 :]:
            point = line_intersection(left, right)
            if point is not None and in_domain_closure(point):
                vertices.add(point)

    representatives: dict[tuple[int, ...], Point] = {}

    # 0D strata.
    for point in vertices:
        r2, r3 = point
        if r2 > 1 and r3 > r2 and r3 <= MAX_RATIO:
            representatives.setdefault(signature(point, walls), point)

    # Every arrangement edge is an open interval between adjacent vertices on
    # one line.  Its midpoint represents the 1D stratum.  A sufficiently small
    # exact rational normal perturbation on either side represents the adjacent
    # 2D cells.  Because the domain boundaries are themselves included as lines,
    # the same construction also reaches every bounded cell.
    for line_index, line in enumerate(lines):
        points = [point for point in vertices if on_line(point, line)]
        points.sort(key=(lambda point: point[1]) if line[0] == 'V' else (lambda point: point[0]))

        for left, right in zip(points[:-1], points[1:]):
            midpoint = ((left[0] + right[0]) / 2, (left[1] + right[1]) / 2)
            if not in_domain_closure(midpoint):
                continue
            incident = [candidate for candidate in lines if on_line(midpoint, candidate)]
            if len(incident) != 1:
                continue

            r2, r3 = midpoint
            if r2 > 1 and r3 > r2 and r3 <= MAX_RATIO:
                representatives.setdefault(signature(midpoint, walls), midpoint)

            normal_a, normal_b, _ = coefficients(line)
            safe_steps: list[Fraction] = []
            for other_index, other in enumerate(lines):
                if other_index == line_index:
                    continue
                a, b, d = coefficients(other)
                residual = a * r2 + b * r3 - d
                coupling = a * normal_a + b * normal_b
                if residual != 0 and coupling != 0:
                    safe_steps.append(abs(residual / coupling))

            epsilon = min(safe_steps) / 4 if safe_steps else Fraction(1, 100)
            for direction in (-1, 1):
                point = (
                    r2 + direction * epsilon * normal_a,
                    r3 + direction * epsilon * normal_b,
                )
                if in_domain_interior(point):
                    representatives.setdefault(signature(point, walls), point)

    return representatives


def clear_denominators(ratios: tuple[Fraction, ...]) -> tuple[int, ...]:
    denominator = 1
    for ratio in ratios:
        denominator = math.lcm(denominator, ratio.denominator)
    return tuple(int(ratio * denominator) for ratio in ratios)


def first_witness_and_history(point: Point) -> tuple[Task, ProcessWord[tuple[object, ...]], int]:
    speeds = clear_denominators((Fraction(1), point[0], point[1]))
    events: dict[Fraction, list[tuple[int, int, str]]] = defaultdict(list)

    for runner, speed in enumerate(speeds):
        for center in range(TASK_ORACLE_CENTER_LIMIT + 1):
            exit_time = (Fraction(center) + DELTA) / speed
            if exit_time > 0:
                events[exit_time].append((runner, center, 'exit'))
            if center >= 1:
                enter_time = (Fraction(center) - DELTA) / speed
                if enter_time > 0:
                    events[enter_time].append((runner, center, 'enter'))

    bad = {0, 1, 2}
    steps: list[tuple[object, ...]] = []
    largest_center = 0

    for event_index, time in enumerate(sorted(events), start=1):
        group = tuple(sorted(events[time]))
        if group:
            largest_center = max(largest_center, *(center for _runner, center, _kind in group))
        boundary_runners = {runner for runner, _center, _kind in group}
        bad_on = tuple(sorted(bad - boundary_runners))

        after = set(bad)
        for runner, _center, kind in group:
            if kind == 'exit':
                after.discard(runner)
            else:
                after.add(runner)

        step = (group, bad_on, tuple(sorted(after)))
        steps.append(step)
        if not bad_on:
            mode = 'interval' if not after else 'point'
            task: Task = (event_index, group, mode)
            return task, ProcessWord(tuple(steps)), largest_center
        bad = after

    raise AssertionError('bounded exact task oracle did not find a witness')


def task_relevant_wall_indices(
    signatures: tuple[tuple[int, ...], ...],
    tasks: dict[tuple[int, ...], Task],
) -> tuple[int, ...]:
    relevant: list[int] = []
    for wall_index in range(len(signatures[0])):
        groups: dict[tuple[int, ...], set[Task]] = defaultdict(set)
        for item in signatures:
            key = item[:wall_index] + item[wall_index + 1 :]
            groups[key].add(tasks[item])
        if any(len(group_tasks) > 1 for group_tasks in groups.values()):
            relevant.append(wall_index)
    return tuple(relevant)


def integer_triples(limit: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        triple
        for triple in combinations(range(1, limit + 1), 3)
        if Fraction(triple[2], triple[0]) <= MAX_RATIO
    )


def triple_point(triple: tuple[int, int, int]) -> Point:
    first, second, third = triple
    return Fraction(second, first), Fraction(third, first)


@dataclass(frozen=True)
class DecisionTree:
    predicate: int | None
    task: int | None = None
    children: tuple[tuple[int, 'DecisionTree'], ...] = ()


def build_optimal_tree(
    reduced_signatures: tuple[tuple[int, ...], ...],
    item_tasks: tuple[int, ...],
    weights: tuple[int, ...],
) -> tuple[DecisionTree, tuple[int, int, int]]:
    """Exact minimum expected-depth ternary tree; secondary geometry tie-breakers."""

    item_count = len(reduced_signatures)
    predicate_count = len(reduced_signatures[0])
    full_mask = (1 << item_count) - 1

    predicate_masks: list[tuple[int, int, int]] = []
    for predicate in range(predicate_count):
        masks = [0, 0, 0]
        for item, signs in enumerate(reduced_signatures):
            masks[signs[predicate] + 1] |= 1 << item
        predicate_masks.append(tuple(masks))

    task_masks: list[int] = []
    for task in sorted(set(item_tasks)):
        mask = 0
        for item, item_task in enumerate(item_tasks):
            if item_task == task:
                mask |= 1 << item
        task_masks.append(mask)

    def pure(mask: int) -> bool:
        count = 0
        for task_mask in task_masks:
            if mask & task_mask:
                count += 1
                if count > 1:
                    return False
        return True

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
    def solve(mask: int) -> tuple[tuple[int, int, int], int | None]:
        if pure(mask):
            return (0, 0, 0), None

        total_weight = mask_weight(mask)
        state_count = mask.bit_count()
        best: tuple[int, int, int] | None = None
        best_predicate: int | None = None

        for predicate, masks in enumerate(predicate_masks):
            children = [mask & branch for branch in masks]
            nonempty = [child for child in children if child]
            if len(nonempty) <= 1:
                continue

            weighted_depth = total_weight
            unweighted_depth = state_count
            internal_nodes = 1
            for child in nonempty:
                child_cost, _ = solve(child)
                weighted_depth += child_cost[0]
                unweighted_depth += child_cost[1]
                internal_nodes += child_cost[2]

            candidate = (weighted_depth, unweighted_depth, internal_nodes)
            if best is None or candidate < best:
                best = candidate
                best_predicate = predicate

        if best is None:
            raise AssertionError('task-relevant signs should separate every task')
        return best, best_predicate

    def build(mask: int) -> DecisionTree:
        _cost, predicate = solve(mask)
        if predicate is None:
            tasks = {
                item_tasks[item]
                for item in range(item_count)
                if mask & (1 << item)
            }
            assert len(tasks) == 1
            return DecisionTree(predicate=None, task=next(iter(tasks)))

        children: list[tuple[int, DecisionTree]] = []
        for branch_value, branch_mask in zip((-1, 0, 1), predicate_masks[predicate]):
            child = mask & branch_mask
            if child:
                children.append((branch_value, build(child)))
        return DecisionTree(predicate=predicate, children=tuple(children))

    cost, _ = solve(full_mask)
    return build(full_mask), cost


def classify(tree: DecisionTree, reduced_signature: tuple[int, ...]) -> int:
    node = tree
    while node.predicate is not None:
        branch = reduced_signature[node.predicate]
        child_map = dict(node.children)
        node = child_map[branch]
    assert node.task is not None
    return node.task


def decision_history(tree: DecisionTree, reduced_signature: tuple[int, ...]) -> ProcessWord[tuple[int, int]]:
    node = tree
    steps: list[tuple[int, int]] = []
    while node.predicate is not None:
        branch = reduced_signature[node.predicate]
        steps.append((node.predicate, branch))
        node = dict(node.children)[branch]
    return ProcessWord(tuple(steps))


def test_three_speed_am_arrangement_and_huffman_tree() -> None:
    walls = candidate_walls()
    assert len(contact_ratios(MAX_CONTACT_CENTER_FOR_WALLS)) == 17
    assert len(walls) == 51

    representatives = arrangement_representatives(walls)
    assert len(representatives) == 1771

    tasks: dict[tuple[int, ...], Task] = {}
    contact_histories: list[ProcessWord[tuple[object, ...]]] = []
    largest_center_seen = 0
    for item_signature, point in representatives.items():
        task, history, largest_center = first_witness_and_history(point)
        tasks[item_signature] = task
        contact_histories.append(history)
        largest_center_seen = max(largest_center_seen, largest_center)

    assert len(set(tasks.values())) == 44
    # Independent task evaluation is allowed to look beyond center 3; on every
    # exact arrangement stratum the first witness nevertheless occurs before a
    # center>3 contact is needed.
    assert largest_center_seen == 3

    signatures = tuple(representatives)
    relevant = task_relevant_wall_indices(signatures, tasks)
    relevant_walls = tuple(walls[index] for index in relevant)
    assert relevant_walls == (
        ('D', Fraction(11, 9)),
        ('D', Fraction(9, 7)),
        ('D', Fraction(7, 5)),
        ('D', Fraction(5, 3)),
        ('D', Fraction(9, 5)),
        ('D', Fraction(11, 5)),
        ('D', Fraction(7, 3)),
        ('D', Fraction(13, 5)),
        ('V', Fraction(3)), ('H', Fraction(3)), ('D', Fraction(3)),
        ('V', Fraction(5)), ('H', Fraction(5)), ('D', Fraction(5)),
        ('V', Fraction(7)), ('H', Fraction(7)), ('D', Fraction(7)),
    )

    reduced_task_sets: dict[tuple[int, ...], set[Task]] = defaultdict(set)
    for item_signature in signatures:
        reduced = tuple(item_signature[index] for index in relevant)
        reduced_task_sets[reduced].add(tasks[item_signature])
    assert all(len(task_set) == 1 for task_set in reduced_task_sets.values())
    assert len(reduced_task_sets) == 181

    reduced_signatures = tuple(reduced_task_sets)
    task_values = sorted({next(iter(value)) for value in reduced_task_sets.values()}, key=repr)
    task_ids = {task: index for index, task in enumerate(task_values)}
    item_tasks = tuple(
        task_ids[next(iter(reduced_task_sets[reduced]))]
        for reduced in reduced_signatures
    )
    reduced_index = {reduced: index for index, reduced in enumerate(reduced_signatures)}

    # Usage weights are deliberately separate from geometry discovery.
    training = integer_triples(10)
    assert len(training) == 105
    weights = [0] * len(reduced_signatures)
    for triple in training:
        full_signature = signature(triple_point(triple), walls)
        reduced = tuple(full_signature[index] for index in relevant)
        weights[reduced_index[reduced]] += 1

    tree, cost = build_optimal_tree(
        reduced_signatures,
        item_tasks,
        tuple(weights),
    )
    assert cost == (282, 837, 43)
    assert relevant_walls[tree.predicate] == ('H', Fraction(3))

    # Compare the complete arrangement geometry, not just training samples.
    wall_histories = tuple(
        decision_history(tree, reduced)
        for reduced in reduced_signatures
    )
    contact_profile = boundary_profile(tuple(contact_histories))
    wall_profile = boundary_profile(wall_histories)

    assert contact_profile.widths == (
        1, 1, 3, 9, 20, 28, 31, 34, 29, 25, 15, 10, 1, 1,
    )
    assert wall_profile.widths == (1, 3, 3, 9, 21, 27, 27, 24, 12, 3)
    assert contact_profile.peak_width == 34
    assert wall_profile.peak_width == 27
    assert sum(contact_profile.widths) == 208
    assert sum(wall_profile.widths) == 130
    assert contact_profile.max_depth == 13
    assert wall_profile.max_depth == 9

    # On the independent usage distribution the same exact geometry lowers the
    # average process depth from event-by-event contact evolution to 2.686 wall
    # tests.  The finite task distribution has ternary Huffman lower reference 2.
    training_contact_depth = 0
    training_wall_depth = 0
    observed_task_weights: dict[Task, int] = defaultdict(int)
    for triple in training:
        point = triple_point(triple)
        task, history, _largest_center = first_witness_and_history(point)
        training_contact_depth += history.depth
        observed_task_weights[task] += 1

        full_signature = signature(point, walls)
        reduced = tuple(full_signature[index] for index in relevant)
        training_wall_depth += decision_history(tree, reduced).depth

    assert training_contact_depth == 468
    assert training_wall_depth == 282
    assert math.isclose(training_contact_depth / 105, 4.457142857142857)
    assert math.isclose(training_wall_depth / 105, 2.6857142857142855)
    assert len(observed_task_weights) == 23

    # Larger integer holdout: geometry and tree are frozen; no new wall, task
    # rule or tree parameter is learned here.
    holdout = integer_triples(20)
    assert len(holdout) == 928
    id_to_task = {index: task for task, index in task_ids.items()}
    for triple in holdout:
        point = triple_point(triple)
        actual_task, _history, _largest_center = first_witness_and_history(point)
        full_signature = signature(point, walls)
        reduced = tuple(full_signature[index] for index in relevant)
        predicted_task = id_to_task[classify(tree, reduced)]
        assert predicted_task == actual_task
