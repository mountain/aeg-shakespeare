"""Phase 12B: lazy task-directed decision DAG for the five-speed transfer.

Phase 12A shows that globally materializing all 36 canonical-witness predicates
creates 69,683 complete sign cells from only 1,117 symbolic terminal regions.
This script refuses that materialization step.

Instead, a decision node queries one canonical predicate directly on the current
set of exact closure/task atoms:

* atoms with a forced sign route without changing their closure;
* only unresolved atoms would be refined into feasible sign children;
* a leaf is emitted as soon as every surviving atom has the same canonical task.

A deterministic greedy policy first minimizes the number of closure refinements
required by the next query.  In the exact Phase-12A domain this pressure remains
zero at every selected node: the complete task classifier can be built entirely
from signs already forced by the 1,117 terminal regions.

The result is not claimed to be a globally optimal Huffman tree.  It is a
constructive red team against full static sign-cell materialization.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

import five_speed_dimension_transfer as transfer


Atom = tuple[transfer.Closure, object]


@dataclass(frozen=True)
class LazyDecisionNode:
    predicate: int | None
    task: object | None = None
    children: tuple[tuple[int, "LazyDecisionNode"], ...] = ()


@dataclass(frozen=True)
class LazyTaskDagResult:
    terminal_regions: int
    canonical_tasks: int
    coordinates: tuple[transfer.Coordinate, ...]
    unique_atoms_visited: int
    closure_refinement_pressure: int
    tree_nodes: int
    internal_nodes: int
    leaves: int
    worst_depth: int
    peak_frontier: int
    widths: tuple[int, ...]
    dag_nodes: int
    dag_internal_nodes: int
    dag_task_leaves: int
    root_coordinate: transfer.Coordinate
    usage_cases: int
    usage_decision_depth: int
    usage_event_depth: int
    usage_decision_worst: int
    usage_event_worst: int
    usage_errors: int


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


def _canonical_atoms_and_coordinates():
    terminals, generated, _states, _max_center = transfer._compile_terminal_regions()
    signatures = transfer._terminal_signatures(terminals, generated)
    canonical = transfer._minimum_for_projection(
        terminals,
        generated,
        signatures,
        transfer._canonical,
    )
    atoms = frozenset(
        (region.closure, _canonical_task(region.task))
        for region in terminals
    )
    assert len(atoms) == 1_117
    assert len({task for _closure, task in atoms}) == 33
    assert len(canonical.minimum_coordinates) == 36
    return atoms, canonical.minimum_coordinates


def _splitter(coordinates):
    @lru_cache(maxsize=None)
    def split_closure(
        closure: transfer.Closure,
        predicate: int,
    ) -> tuple[tuple[int, transfer.Closure], ...]:
        first, second, ratio = coordinates[predicate]
        forced = transfer._relation(
            closure,
            (first, second),
            ratio,
        )
        if forced is not None:
            return ((forced, closure),)

        output = []
        for sign in (-1, 0, 1):
            child = transfer._add_sign(
                closure,
                coordinates[predicate],
                sign,
            )
            if child is not None:
                output.append((sign, child))
        assert output
        return tuple(output)

    def split_atoms(atoms: frozenset[Atom], predicate: int):
        branches = {-1: set(), 0: set(), 1: set()}
        refinement_pressure = 0

        for closure, task in atoms:
            parts = split_closure(closure, predicate)
            refinement_pressure += len(parts) - 1
            for sign, child in parts:
                branches[sign].add((child, task))

        return (
            {
                sign: frozenset(values)
                for sign, values in branches.items()
                if values
            },
            refinement_pressure,
        )

    return split_atoms


def _build_lazy_tree(atoms, coordinates):
    split_atoms = _splitter(coordinates)
    unique_atoms = set(atoms)
    refinement_pressure = 0

    def score(atoms, predicate):
        branches, pressure = split_atoms(atoms, predicate)
        if len(branches) <= 1:
            return None

        task_counts = [
            len({task for _closure, task in child})
            for child in branches.values()
        ]
        atom_counts = [len(child) for child in branches.values()]

        # Preserve the lazy region geometry first.  Only after minimizing new
        # closure refinement do we balance remaining task ambiguity and size.
        return (
            pressure,
            sum(atom_counts),
            max(task_counts),
            sum(task_counts),
            max(atom_counts),
        )

    def build(atoms, remaining):
        nonlocal refinement_pressure
        tasks = {task for _closure, task in atoms}
        if len(tasks) == 1:
            return LazyDecisionNode(None, task=next(iter(tasks)))

        best = None
        for predicate in remaining:
            candidate_score = score(atoms, predicate)
            if candidate_score is None:
                continue
            candidate = (candidate_score, predicate)
            if best is None or candidate < best:
                best = candidate

        if best is None:
            raise AssertionError("canonical coordinates failed to separate tasks")

        predicate = best[1]
        branches, pressure = split_atoms(atoms, predicate)
        refinement_pressure += pressure
        for child in branches.values():
            unique_atoms.update(child)

        next_remaining = tuple(
            item
            for item in remaining
            if item != predicate
        )
        children = tuple(
            (sign, build(child, next_remaining))
            for sign, child in sorted(branches.items())
        )
        return LazyDecisionNode(predicate, children=children)

    tree = build(atoms, tuple(range(len(coordinates))))
    return tree, len(unique_atoms), refinement_pressure


def _tree_metrics(tree):
    widths = Counter()
    queue = deque([(tree, 0)])
    internal = 0
    leaves = 0

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
        width_tuple,
    )


def _dag_metrics(tree):
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
    internal = sum(1 for key in cache if key[0] == "node")
    leaves = sum(1 for key in cache if key[0] == "leaf")
    return len(cache), internal, leaves


def _usage_grid():
    # Scale-fix u1=1 and use an exact rational grid that includes both sides of
    # the nontrivial u5/u1=5 threshold while remaining inside 21/4.
    candidates = (
        Fraction(3, 2),
        Fraction(2),
        Fraction(5, 2),
        Fraction(3),
        Fraction(7, 2),
        Fraction(4),
        Fraction(9, 2),
        Fraction(5),
        Fraction(41, 8),
    )
    return tuple(
        (Fraction(1),) + tail
        for tail in combinations(candidates, 4)
    )


def _direct_canonical_task(speeds, *, event_limit: int = 256):
    phases = [Fraction(0)] * transfer.K
    bad = set(range(transfer.K))

    for event_index in range(1, event_limit + 1):
        candidates = []
        kinds = []
        for phase, speed in zip(phases, speeds):
            if phase < transfer.DELTA:
                distance, kind = transfer.DELTA - phase, "exit"
            elif phase < 1 - transfer.DELTA:
                distance, kind = 1 - transfer.DELTA - phase, "enter"
            else:
                distance, kind = 1 + transfer.DELTA - phase, "exit"
            candidates.append(distance / speed)
            kinds.append(kind)

        dt = min(candidates)
        group = tuple(
            runner
            for runner, candidate in enumerate(candidates)
            if candidate == dt
        )
        bad_on = bad - set(group)
        phases = [
            (phase + speed * dt) % 1
            for phase, speed in zip(phases, speeds)
        ]

        bad_after = set(bad)
        boundary = []
        for runner in group:
            kind = kinds[runner]
            if kind == "exit":
                bad_after.discard(runner)
            else:
                bad_after.add(runner)
            boundary.append((runner, kind))

        if not bad_on:
            return (
                tuple(sorted(boundary)),
                "interval" if not bad_after else "point",
            ), event_index
        bad = bad_after

    raise AssertionError("usage oracle did not reach a witness")


def _evaluate_tree(tree, coordinates, speeds):
    node = tree
    depth = 0
    while node.predicate is not None:
        first, second, ratio = coordinates[node.predicate]
        value = speeds[second] / speeds[first]
        sign = -1 if value < ratio else (1 if value > ratio else 0)
        node = dict(node.children)[sign]
        depth += 1
    return node.task, depth


def analyze_lazy_task_dag() -> LazyTaskDagResult:
    atoms, coordinates = _canonical_atoms_and_coordinates()
    tree, unique_atoms, pressure = _build_lazy_tree(atoms, coordinates)
    (
        tree_nodes,
        internal_nodes,
        leaves,
        worst_depth,
        peak_frontier,
        widths,
    ) = _tree_metrics(tree)
    dag_nodes, dag_internal, dag_leaves = _dag_metrics(tree)

    usage = _usage_grid()
    decision_depth = 0
    event_depth = 0
    decision_worst = 0
    event_worst = 0
    errors = 0

    for speeds in usage:
        compiled_task, compiled_depth = _evaluate_tree(
            tree,
            coordinates,
            speeds,
        )
        direct_task, direct_depth = _direct_canonical_task(speeds)
        if compiled_task != direct_task:
            errors += 1
        decision_depth += compiled_depth
        event_depth += direct_depth
        decision_worst = max(decision_worst, compiled_depth)
        event_worst = max(event_worst, direct_depth)

    assert tree.predicate is not None
    return LazyTaskDagResult(
        terminal_regions=len(atoms),
        canonical_tasks=len({task for _closure, task in atoms}),
        coordinates=coordinates,
        unique_atoms_visited=unique_atoms,
        closure_refinement_pressure=pressure,
        tree_nodes=tree_nodes,
        internal_nodes=internal_nodes,
        leaves=leaves,
        worst_depth=worst_depth,
        peak_frontier=peak_frontier,
        widths=widths,
        dag_nodes=dag_nodes,
        dag_internal_nodes=dag_internal,
        dag_task_leaves=dag_leaves,
        root_coordinate=coordinates[tree.predicate],
        usage_cases=len(usage),
        usage_decision_depth=decision_depth,
        usage_event_depth=event_depth,
        usage_decision_worst=decision_worst,
        usage_event_worst=event_worst,
        usage_errors=errors,
    )


def main() -> None:
    result = analyze_lazy_task_dag()
    print("Sonnet 001 five-speed lazy task DAG")
    print(f"  terminal regions / tasks: {result.terminal_regions} / {result.canonical_tasks}")
    print(f"  minimum coordinates:      {len(result.coordinates)}")
    print(f"  unique atoms visited:     {result.unique_atoms_visited}")
    print(f"  closure refinement:       {result.closure_refinement_pressure}")
    print(
        "  tree nodes/internal/leaves: "
        f"{result.tree_nodes} / {result.internal_nodes} / {result.leaves}"
    )
    print(f"  worst / peak:             {result.worst_depth} / {result.peak_frontier}")
    print(
        "  DAG nodes/internal/tasks:  "
        f"{result.dag_nodes} / {result.dag_internal_nodes} / {result.dag_task_leaves}"
    )
    print(f"  root:                     {result.root_coordinate}")
    print(f"  widths:                   {result.widths}")
    print(
        "  usage decision/event:     "
        f"{result.usage_decision_depth} / {result.usage_event_depth}"
    )
    print(
        "  usage worst decision/event: "
        f"{result.usage_decision_worst} / {result.usage_event_worst}"
    )
    print(f"  usage errors:             {result.usage_errors}")


if __name__ == "__main__":
    main()
