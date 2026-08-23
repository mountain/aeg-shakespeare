"""Phase 12C: widen the five-speed domain and test clean-separator recursion.

Phase 12B found that the first nontrivial five-speed domain can be classified by
an adaptive predicate tree without refining any symbolic terminal closure.  This
script asks whether that zero-refinement property survives as the allowed speed
ratio u5/u1 is widened.

A *clean separator* at one node is a canonical-witness coordinate whose sign is
already forced on every exact terminal region reaching that node and which
separates at least two residual task classes.  A recursively clean decision tree
therefore never completes an unresolved wall coordinate.

The sweep uses exact domains

    21/4, 11/2, 23/4, 6, 25/4

and recomputes the horizon-free process, canonical task-minimum coordinates and
clean decision tree independently at each width.  It is an opt-in research
calibration, not routine CI.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

import five_speed_dimension_transfer as transfer


SWEEP = (
    Fraction(21, 4),
    Fraction(11, 2),
    Fraction(23, 4),
    Fraction(6),
    Fraction(25, 4),
)


@dataclass(frozen=True)
class CleanNode:
    predicate: int | None
    task: object | None = None
    children: tuple[tuple[int, "CleanNode"], ...] = ()


@dataclass(frozen=True)
class DomainResult:
    rmax: Fraction
    symbolic_states: int
    terminal_regions: int
    generated_coordinates: int
    canonical_tasks: int
    minimum_coordinates: int
    tree_nodes: int
    internal_nodes: int
    leaves: int
    worst_depth: int
    peak_frontier: int
    dag_nodes: int
    root_coordinate: transfer.Coordinate
    max_event_index: int
    max_contact_center: int


def _canonical_task(task: transfer.Task):
    _index, boundary, mode = task
    return (
        tuple(
            sorted(
                (runner, kind)
                for runner, _center, kind in boundary
            )
        ),
        mode,
    )


def _minimum_canonical_coordinates(terminals, coordinates):
    """Exact singleton-separator minimum using 107-bit-scale Python integers."""

    signatures = []
    tasks = []
    for region in terminals:
        negative = zero = positive = 0
        for index, (first, second, ratio) in enumerate(coordinates):
            relation = transfer._relation(
                region.closure,
                (first, second),
                ratio,
            )
            if relation == -1:
                negative |= 1 << index
            elif relation == 0:
                zero |= 1 << index
            elif relation == 1:
                positive |= 1 << index
        signatures.append((negative, zero, positive))
        tasks.append(_canonical_task(region.task))

    conflict_masks = set()
    for first, second in combinations(range(len(terminals)), 2):
        if tasks[first] == tasks[second]:
            continue
        fn, fz, fp = signatures[first]
        sn, sz, sp = signatures[second]
        separators = (
            (fn & (sz | sp))
            | (fz & (sn | sp))
            | (fp & (sn | sz))
        )
        assert separators
        conflict_masks.add(separators)

    mandatory_mask = 0
    for separators in conflict_masks:
        if separators & (separators - 1) == 0:
            mandatory_mask |= separators

    assert all(
        separators & mandatory_mask
        for separators in conflict_masks
    )

    minimum = tuple(
        coordinate
        for index, coordinate in enumerate(coordinates)
        if mandatory_mask & (1 << index)
    )
    return minimum, len(set(tasks))


def _build_clean_tree(atoms, coordinates):
    """Build a decision tree using only signs already forced on every node atom."""

    @lru_cache(maxsize=None)
    def forced(closure: transfer.Closure, predicate: int):
        first, second, ratio = coordinates[predicate]
        return transfer._relation(
            closure,
            (first, second),
            ratio,
        )

    def clean_branches(atoms, predicate):
        branches = {-1: set(), 0: set(), 1: set()}
        for closure, task in atoms:
            sign = forced(closure, predicate)
            if sign is None:
                return None
            branches[sign].add((closure, task))
        return {
            sign: frozenset(values)
            for sign, values in branches.items()
            if values
        }

    def build(atoms, remaining):
        tasks = {task for _closure, task in atoms}
        if len(tasks) == 1:
            return CleanNode(None, task=next(iter(tasks)))

        best = None
        for predicate in remaining:
            branches = clean_branches(atoms, predicate)
            if branches is None or len(branches) <= 1:
                continue
            task_counts = [
                len({task for _closure, task in child})
                for child in branches.values()
            ]
            atom_counts = [len(child) for child in branches.values()]
            score = (
                max(task_counts),
                sum(task_counts),
                max(atom_counts),
            )
            candidate = (score, predicate, branches)
            if best is None or (candidate[0], candidate[1]) < (best[0], best[1]):
                best = candidate

        if best is None:
            raise AssertionError(
                "clean-separator recursion failed before task purity"
            )

        _score, predicate, branches = best
        next_remaining = tuple(
            item
            for item in remaining
            if item != predicate
        )
        return CleanNode(
            predicate,
            children=tuple(
                (sign, build(child, next_remaining))
                for sign, child in sorted(branches.items())
            ),
        )

    return build(atoms, tuple(range(len(coordinates))))


def _tree_metrics(tree):
    widths = Counter()
    queue = deque([(tree, 0)])
    internal = leaves = 0

    while queue:
        node, depth = queue.popleft()
        widths[depth] += 1
        if node.predicate is None:
            leaves += 1
        else:
            internal += 1
            for _sign, child in node.children:
                queue.append((child, depth + 1))

    width_tuple = tuple(
        widths[depth]
        for depth in range(max(widths) + 1)
    )
    return (
        sum(width_tuple),
        internal,
        leaves,
        len(width_tuple) - 1,
        max(width_tuple),
    )


def _dag_nodes(tree):
    cache = {}

    def intern(node):
        if node.predicate is None:
            key = ("leaf", node.task)
        else:
            key = (
                "node",
                node.predicate,
                tuple(
                    (sign, intern(child))
                    for sign, child in node.children
                ),
            )
        cache.setdefault(key, len(cache))
        return cache[key]

    intern(tree)
    return len(cache)


def analyze_domain(rmax: Fraction) -> DomainResult:
    old_rmax = transfer.RMAX
    transfer.RMAX = Fraction(rmax)
    try:
        terminals, generated, states, max_center = transfer._compile_terminal_regions()
        coordinates, task_count = _minimum_canonical_coordinates(
            terminals,
            generated,
        )
        atoms = frozenset(
            (region.closure, _canonical_task(region.task))
            for region in terminals
        )
        tree = _build_clean_tree(atoms, coordinates)
        (
            tree_nodes,
            internal_nodes,
            leaves,
            worst_depth,
            peak_frontier,
        ) = _tree_metrics(tree)
        assert tree.predicate is not None
        return DomainResult(
            rmax=Fraction(rmax),
            symbolic_states=states,
            terminal_regions=len(terminals),
            generated_coordinates=len(generated),
            canonical_tasks=task_count,
            minimum_coordinates=len(coordinates),
            tree_nodes=tree_nodes,
            internal_nodes=internal_nodes,
            leaves=leaves,
            worst_depth=worst_depth,
            peak_frontier=peak_frontier,
            dag_nodes=_dag_nodes(tree),
            root_coordinate=coordinates[tree.predicate],
            max_event_index=max(region.task[0] for region in terminals),
            max_contact_center=max_center,
        )
    finally:
        transfer.RMAX = old_rmax


def analyze_sweep():
    return tuple(analyze_domain(rmax) for rmax in SWEEP)


def main() -> None:
    print("Sonnet 001 five-speed clean-separator sweep")
    for result in analyze_sweep():
        print(
            f"  R<{result.rmax}: "
            f"states={result.symbolic_states} "
            f"regions={result.terminal_regions} "
            f"generated={result.generated_coordinates} "
            f"tasks/walls={result.canonical_tasks}/{result.minimum_coordinates} "
            f"tree/internal/DAG={result.tree_nodes}/{result.internal_nodes}/{result.dag_nodes} "
            f"worst/peak={result.worst_depth}/{result.peak_frontier} "
            f"root={result.root_coordinate}"
        )


if __name__ == "__main__":
    main()
