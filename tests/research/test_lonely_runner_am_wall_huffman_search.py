"""Search a low-depth Lonely Runner presentation using A/M contact walls.

The continuous contact calculus supplies the admissible decision surfaces.  For
relative M coordinate r=u2/u1, equality of two lifted contact times has the form

    r = beta / alpha,

where alpha and beta are primitive contact constants n +/- delta.  Each wall
query naturally has three outcomes: left chamber, the wall stratum itself, and
right chamber.

This file discovers which walls actually change the first-witness task, then
builds the minimum expected-depth ordered ternary decision tree under a finite
training distribution.  A ternary Huffman code is used only as the unconstrained
information-theoretic reference; the selected tree is restricted to genuine A/M
contact walls.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import heapq
from itertools import combinations


Task = tuple[object, ...]


def witness_task_for_ratio(ratio: Fraction, *, final_k: int = 2) -> Task:
    """Exact first lonely-witness label for speeds (1, ratio)."""

    if ratio <= 1:
        raise ValueError("ratio must be greater than one")

    # Clear denominators so all contact times remain exact Fractions.
    speeds = (ratio.denominator, ratio.numerator)
    delta = Fraction(1, final_k + 1)
    events: dict[Fraction, list[tuple[int, int, str]]] = defaultdict(list)

    # This bound is far beyond what the ratio<=12 calibration needs.
    for runner, speed in enumerate(speeds):
        for center in range(40):
            exit_time = (Fraction(center) + delta) / speed
            if exit_time > 0:
                events[exit_time].append((runner, center, "exit"))
            if center >= 1:
                enter_time = (Fraction(center) - delta) / speed
                if enter_time > 0:
                    events[enter_time].append((runner, center, "enter"))

    bad = {0, 1}
    for index, time in enumerate(sorted(events), start=1):
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
            return (index, group, mode)
        bad = after

    raise AssertionError("calibration did not find a witness")


def contact_constants(*, final_k: int, max_center: int) -> tuple[Fraction, ...]:
    delta = Fraction(1, final_k + 1)
    values: set[Fraction] = set()
    for center in range(max_center + 1):
        values.add(Fraction(center) + delta)
        if center >= 1:
            values.add(Fraction(center) - delta)
    return tuple(sorted(value for value in values if value > 0))


def candidate_am_walls(
    *,
    final_k: int,
    max_center: int,
    max_ratio: Fraction,
) -> tuple[Fraction, ...]:
    """All bounded contact-collision walls r=beta/alpha in the ratio window."""

    constants = contact_constants(final_k=final_k, max_center=max_center)
    return tuple(
        sorted(
            {
                beta / alpha
                for alpha in constants
                for beta in constants
                if 1 < beta / alpha < max_ratio
            }
        )
    )


def relevant_task_walls(
    *,
    final_k: int,
    max_center: int,
    max_ratio: Fraction,
) -> tuple[Fraction, ...]:
    """Filter calculus-generated walls by exact left/on/right task semantics."""

    walls = candidate_am_walls(
        final_k=final_k,
        max_center=max_center,
        max_ratio=max_ratio,
    )
    points = (Fraction(1),) + walls + (max_ratio,)
    interval_tasks = tuple(
        witness_task_for_ratio((left + right) / 2, final_k=final_k)
        for left, right in zip(points[:-1], points[1:])
    )

    relevant: list[Fraction] = []
    for index, wall in enumerate(walls):
        left_task = interval_tasks[index]
        right_task = interval_tasks[index + 1]
        wall_task = witness_task_for_ratio(wall, final_k=final_k)
        if (
            left_task != right_task
            or wall_task != left_task
            or wall_task != right_task
        ):
            relevant.append(wall)
    return tuple(relevant)


def stratum_tasks(
    walls: tuple[Fraction, ...],
    *,
    final_k: int,
    max_ratio: Fraction,
) -> tuple[Task, ...]:
    """Alternating open-chamber and exact-wall task labels."""

    tasks: list[Task] = []
    left = Fraction(1)
    for wall in walls:
        tasks.append(witness_task_for_ratio((left + wall) / 2, final_k=final_k))
        tasks.append(witness_task_for_ratio(wall, final_k=final_k))
        left = wall
    tasks.append(witness_task_for_ratio((left + max_ratio) / 2, final_k=final_k))
    return tuple(tasks)


def stratum_index(ratio: Fraction, walls: tuple[Fraction, ...]) -> int:
    index = 0
    for wall in walls:
        if ratio < wall:
            return index
        if ratio == wall:
            return index + 1
        index += 2
    return index


def training_weights(
    *,
    speed_limit: int,
    walls: tuple[Fraction, ...],
    max_ratio: Fraction,
) -> tuple[int, ...]:
    weights = [0] * (2 * len(walls) + 1)
    for first, second in combinations(range(1, speed_limit + 1), 2):
        ratio = Fraction(second, first)
        if ratio <= max_ratio:
            weights[stratum_index(ratio, walls)] += 1
    return tuple(weights)


@dataclass(frozen=True)
class WallTree:
    wall: Fraction | None
    task: Task | None = None
    left: "WallTree | None" = None
    equal: "WallTree | None" = None
    right: "WallTree | None" = None

    @property
    def is_leaf(self) -> bool:
        return self.wall is None


def optimal_wall_tree(
    walls: tuple[Fraction, ...],
    tasks: tuple[Task, ...],
    weights: tuple[int, ...],
) -> tuple[WallTree, int]:
    """Minimum weighted depth tree using only ordered ternary wall comparisons."""

    if len(tasks) != 2 * len(walls) + 1 or len(weights) != len(tasks):
        raise ValueError("wall/stratum dimensions do not match")

    prefix = [0]
    for weight in weights:
        prefix.append(prefix[-1] + weight)

    def weight_sum(start: int, end: int) -> int:
        return prefix[end] - prefix[start]

    @lru_cache(maxsize=None)
    def solve(start: int, end: int) -> tuple[int, int | None]:
        if end - start <= 1:
            return 0, None

        total = weight_sum(start, end)
        best_cost: int | None = None
        best_wall_stratum: int | None = None

        # Odd strata are the exact wall strata.  Querying that wall adds one
        # comparison for every weighted input reaching the current subtree.
        for wall_stratum in range(start, end):
            if wall_stratum % 2 == 0:
                continue
            cost = total
            if start < wall_stratum:
                cost += solve(start, wall_stratum)[0]
            if wall_stratum + 1 < end:
                cost += solve(wall_stratum + 1, end)[0]
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_wall_stratum = wall_stratum

        if best_cost is None:
            raise AssertionError("nontrivial stratum range has no wall")
        return best_cost, best_wall_stratum

    def build(start: int, end: int) -> WallTree:
        _cost, wall_stratum = solve(start, end)
        if wall_stratum is None:
            return WallTree(wall=None, task=tasks[start])

        wall = walls[(wall_stratum - 1) // 2]
        left = build(start, wall_stratum) if start < wall_stratum else None
        equal = WallTree(wall=None, task=tasks[wall_stratum])
        right = (
            build(wall_stratum + 1, end)
            if wall_stratum + 1 < end
            else None
        )
        return WallTree(
            wall=wall,
            left=left,
            equal=equal,
            right=right,
        )

    total_cost, _root = solve(0, len(tasks))
    return build(0, len(tasks)), total_cost


def classify(tree: WallTree, ratio: Fraction) -> Task:
    if tree.is_leaf:
        assert tree.task is not None
        return tree.task
    assert tree.wall is not None
    if ratio < tree.wall:
        assert tree.left is not None
        return classify(tree.left, ratio)
    if ratio == tree.wall:
        assert tree.equal is not None
        return classify(tree.equal, ratio)
    assert tree.right is not None
    return classify(tree.right, ratio)


def qary_huffman_expected_depth(weights: tuple[int, ...], *, arity: int) -> float:
    """Unrestricted q-ary Huffman reference for nonzero-weight task strata."""

    if arity < 2:
        raise ValueError("arity must be at least two")
    heap = [weight for weight in weights if weight > 0]
    total = sum(heap)
    if not heap or total <= 0:
        raise ValueError("positive total weight required")
    if len(heap) == 1:
        return 1.0

    padding = (arity - 1 - ((len(heap) - 1) % (arity - 1))) % (arity - 1)
    heap.extend([0] * padding)
    heapq.heapify(heap)

    weighted_depth = 0
    while len(heap) > 1:
        merged = sum(heapq.heappop(heap) for _ in range(arity))
        weighted_depth += merged
        heapq.heappush(heap, merged)
    return weighted_depth / total


def test_calculus_discovers_the_task_relevant_contact_walls() -> None:
    walls = relevant_task_walls(
        final_k=2,
        max_center=8,
        max_ratio=Fraction(12),
    )
    assert walls == (
        Fraction(2),
        Fraction(4),
        Fraction(5),
        Fraction(7),
        Fraction(8),
        Fraction(10),
        Fraction(11),
    )

    tasks = stratum_tasks(walls, final_k=2, max_ratio=Fraction(12))
    # Seven walls split the relative-M line into eight open chambers plus seven
    # contact strata.  Every stratum has a distinct first-witness semantics.
    assert len(tasks) == 15
    assert len(set(tasks)) == 15


def test_huffman_style_search_selects_a_near_optimal_am_wall_tree() -> None:
    walls = relevant_task_walls(
        final_k=2,
        max_center=8,
        max_ratio=Fraction(12),
    )
    tasks = stratum_tasks(walls, final_k=2, max_ratio=Fraction(12))
    weights = training_weights(
        speed_limit=12,
        walls=walls,
        max_ratio=Fraction(12),
    )

    assert weights == (30, 6, 15, 3, 1, 2, 3, 1, 0, 1, 1, 1, 0, 1, 1)
    assert sum(weights) == 66

    tree, weighted_depth = optimal_wall_tree(walls, tasks, weights)
    assert tree.wall == Fraction(2)

    expected_wall_depth = weighted_depth / sum(weights)
    assert expected_wall_depth == 123 / 66
    assert expected_wall_depth < 2.0

    # A free ternary prefix code can ignore the geometric order constraint.  The
    # AM wall tree is close to that reference while remaining executable as
    # genuine contact-wall comparisons.
    free_ternary = qary_huffman_expected_depth(weights, arity=3)
    assert free_ternary == 108 / 66
    assert 0 < expected_wall_depth - free_ternary < 0.25


def test_frozen_wall_tree_transfers_to_unseen_ratios_inside_the_same_domain() -> None:
    walls = relevant_task_walls(
        final_k=2,
        max_center=8,
        max_ratio=Fraction(12),
    )
    tasks = stratum_tasks(walls, final_k=2, max_ratio=Fraction(12))
    weights = training_weights(
        speed_limit=12,
        walls=walls,
        max_ratio=Fraction(12),
    )
    tree, _weighted_depth = optimal_wall_tree(walls, tasks, weights)

    training_ratios = {
        Fraction(second, first)
        for first, second in combinations(range(1, 13), 2)
    }
    unseen_checked = 0
    total_checked = 0

    for first, second in combinations(range(1, 17), 2):
        ratio = Fraction(second, first)
        if ratio > 12:
            continue
        total_checked += 1
        predicted = classify(tree, ratio)
        actual = witness_task_for_ratio(ratio)
        assert predicted == actual
        if ratio not in training_ratios:
            unseen_checked += 1

    assert total_checked == 116
    assert unseen_checked == 30
    # 15/2 lies in the chamber (7,8), which was absent from the training ratio
    # set.  The calculus-generated chamber semantics, not sample interpolation,
    # is what makes this held-out classification exact.
    assert Fraction(15, 2) not in training_ratios
    assert classify(tree, Fraction(15, 2)) == witness_task_for_ratio(Fraction(15, 2))
