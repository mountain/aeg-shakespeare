"""Phase 13A: exact clean-separability for partial task signatures.

A canonical process region generally fixes only some of the signs of a compiled
predicate family.  Write one region as

    (task, sigma),

where sigma[j] is -1, 0, +1 when coordinate j is already decided on the whole
region and None when the region straddles / does not decide that coordinate.

A *clean* decision node may query coordinate j on a region family S only when
sigma[j] is defined for every region in S.  It must also split S into at least
two nonempty sign branches.  No region is refined by such a query.

This module gives an exact recursive decision procedure:

    Clean(S) = task-pure(S)
               OR exists clean coordinate j such that
                    Clean(S_{j,-}) and Clean(S_{j,0}) and Clean(S_{j,+}).

If Clean(S) is true, the returned tree is a zero-completion classifier.  If it is
false, the returned obstruction is a finite inductive certificate: for every
possible clean root coordinate, at least one child is itself obstructed.  An
empty candidate list is the atomic obstruction "mixed tasks but no clean
separator".

The result is deliberately grammar-relative.  Failure says that the declared
coordinate family cannot classify the task without eventually querying an
undefined coordinate (hence refining a region) or introducing a richer
predicate.  It does not rule out a different representation grammar.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Hashable, Iterable


Sign = int | None
Task = Hashable


@dataclass(frozen=True)
class PartialRegion:
    name: Hashable
    task: Task
    signs: tuple[Sign, ...]


@dataclass(frozen=True)
class CleanTree:
    coordinate: int | None
    task: Task | None = None
    children: tuple[tuple[int, "CleanTree"], ...] = ()


@dataclass(frozen=True)
class CandidateFailure:
    coordinate: int
    failing_sign: int
    obstruction: "CleanObstruction"


@dataclass(frozen=True)
class CleanObstruction:
    """Inductive certificate that one mixed-task family has no clean tree."""

    region_names: tuple[Hashable, ...]
    task_count: int
    candidate_failures: tuple[CandidateFailure, ...]

    @property
    def atomic(self) -> bool:
        return not self.candidate_failures


@dataclass(frozen=True)
class CleanAnalysis:
    clean: bool
    tree: CleanTree | None
    obstruction: CleanObstruction | None
    states_visited: int
    max_depth: int | None
    tree_nodes: int | None


def _validate(regions: tuple[PartialRegion, ...]) -> int:
    if not regions:
        raise ValueError("at least one region is required")
    width = len(regions[0].signs)
    if any(len(region.signs) != width for region in regions):
        raise ValueError("all partial signatures must have the same width")
    if any(sign not in (-1, 0, 1, None) for region in regions for sign in region.signs):
        raise ValueError("signs must be -1, 0, +1, or None")
    if len({region.name for region in regions}) != len(regions):
        raise ValueError("region names must be unique")
    return width


def pairwise_task_separable(regions: Iterable[PartialRegion]) -> bool:
    """Whether every cross-task pair has some jointly-defined opposite sign."""

    items = tuple(regions)
    _validate(items)
    for first_index, first in enumerate(items):
        for second in items[first_index + 1 :]:
            if first.task == second.task:
                continue
            if not any(
                left is not None
                and right is not None
                and left != right
                for left, right in zip(first.signs, second.signs)
            ):
                return False
    return True


def clean_coordinates(
    regions: tuple[PartialRegion, ...],
    indices: frozenset[int],
) -> tuple[int, ...]:
    """Coordinates total and nonconstant on the current region family."""

    width = len(regions[0].signs)
    result = []
    for coordinate in range(width):
        values = {regions[index].signs[coordinate] for index in indices}
        if None in values or len(values) <= 1:
            continue
        result.append(coordinate)
    return tuple(result)


def _partition(
    regions: tuple[PartialRegion, ...],
    indices: frozenset[int],
    coordinate: int,
) -> tuple[tuple[int, frozenset[int]], ...]:
    groups = {-1: set(), 0: set(), 1: set()}
    for index in indices:
        sign = regions[index].signs[coordinate]
        if sign is None:
            raise ValueError("coordinate is not clean on this family")
        groups[sign].add(index)
    return tuple(
        (sign, frozenset(group))
        for sign, group in groups.items()
        if group
    )


def _tree_metrics(tree: CleanTree) -> tuple[int, int]:
    if tree.coordinate is None:
        return 0, 1
    child_metrics = [_tree_metrics(child) for _sign, child in tree.children]
    return (
        1 + max(depth for depth, _nodes in child_metrics),
        1 + sum(nodes for _depth, nodes in child_metrics),
    )


def analyze_clean_separability(
    regions: Iterable[PartialRegion],
) -> CleanAnalysis:
    """Return either a clean tree or an exact recursive obstruction certificate.

    Search is exact, not greedy.  Candidate ordering is only a performance
    heuristic: if an early coordinate fails, every other clean coordinate is
    still tried before non-cleanseparability is certified.
    """

    items = tuple(regions)
    _validate(items)
    visited = set()

    def task_count(indices: frozenset[int]) -> int:
        return len({items[index].task for index in indices})

    def ordered_candidates(indices: frozenset[int]) -> tuple[int, ...]:
        scored = []
        for coordinate in clean_coordinates(items, indices):
            branches = _partition(items, indices, coordinate)
            child_task_counts = [task_count(child) for _sign, child in branches]
            child_sizes = [len(child) for _sign, child in branches]
            scored.append(
                (
                    max(child_task_counts),
                    sum(child_task_counts),
                    max(child_sizes),
                    coordinate,
                )
            )
        return tuple(item[-1] for item in sorted(scored))

    @lru_cache(maxsize=None)
    def solve(indices: frozenset[int]):
        visited.add(indices)
        tasks = {items[index].task for index in indices}
        if len(tasks) == 1:
            return CleanTree(None, task=next(iter(tasks))), None

        failures = []
        candidates = ordered_candidates(indices)
        for coordinate in candidates:
            child_trees = []
            first_failure = None
            for sign, child_indices in _partition(items, indices, coordinate):
                child_tree, child_obstruction = solve(child_indices)
                if child_tree is None:
                    assert child_obstruction is not None
                    first_failure = CandidateFailure(
                        coordinate=coordinate,
                        failing_sign=sign,
                        obstruction=child_obstruction,
                    )
                    break
                child_trees.append((sign, child_tree))

            if first_failure is None:
                return (
                    CleanTree(
                        coordinate=coordinate,
                        children=tuple(child_trees),
                    ),
                    None,
                )
            failures.append(first_failure)

        obstruction = CleanObstruction(
            region_names=tuple(sorted((items[index].name for index in indices), key=repr)),
            task_count=len(tasks),
            candidate_failures=tuple(failures),
        )
        return None, obstruction

    root = frozenset(range(len(items)))
    tree, obstruction = solve(root)
    if tree is not None:
        depth, nodes = _tree_metrics(tree)
        return CleanAnalysis(
            clean=True,
            tree=tree,
            obstruction=None,
            states_visited=len(visited),
            max_depth=depth,
            tree_nodes=nodes,
        )

    assert obstruction is not None
    return CleanAnalysis(
        clean=False,
        tree=None,
        obstruction=obstruction,
        states_visited=len(visited),
        max_depth=None,
        tree_nodes=None,
    )


def verify_tree(
    regions: Iterable[PartialRegion],
    tree: CleanTree,
) -> bool:
    """Independently verify a returned tree uses only clean queries and exact tasks."""

    items = tuple(regions)
    _validate(items)

    def visit(indices: frozenset[int], node: CleanTree) -> bool:
        tasks = {items[index].task for index in indices}
        if node.coordinate is None:
            return len(tasks) == 1 and node.task == next(iter(tasks))

        coordinate = node.coordinate
        if coordinate not in clean_coordinates(items, indices):
            return False
        expected = dict(_partition(items, indices, coordinate))
        actual = dict(node.children)
        if set(expected) != set(actual):
            return False
        return all(
            visit(expected[sign], actual[sign])
            for sign in expected
        )

    return visit(frozenset(range(len(items))), tree)


def verify_obstruction(
    regions: Iterable[PartialRegion],
    obstruction: CleanObstruction,
) -> bool:
    """Independently verify the inductive no-clean-tree certificate."""

    items = tuple(regions)
    _validate(items)
    by_name = {region.name: index for index, region in enumerate(items)}

    def visit(certificate: CleanObstruction) -> bool:
        try:
            indices = frozenset(by_name[name] for name in certificate.region_names)
        except KeyError:
            return False
        if not indices:
            return False
        tasks = {items[index].task for index in indices}
        if len(tasks) <= 1 or certificate.task_count != len(tasks):
            return False

        candidates = set(clean_coordinates(items, indices))
        failures = {failure.coordinate: failure for failure in certificate.candidate_failures}
        if set(failures) != candidates:
            return False

        for coordinate, failure in failures.items():
            branches = dict(_partition(items, indices, coordinate))
            if failure.failing_sign not in branches:
                return False
            child_names = tuple(
                sorted(
                    (items[index].name for index in branches[failure.failing_sign]),
                    key=repr,
                )
            )
            if child_names != failure.obstruction.region_names:
                return False
            if not visit(failure.obstruction):
                return False
        return True

    return visit(obstruction)
