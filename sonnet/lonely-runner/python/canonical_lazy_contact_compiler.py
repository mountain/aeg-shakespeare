"""Phase 11B1: lazy symbolic compiler from canonical Lonely Runner dynamics.

The compiler receives no contact-center horizon and no precomputed ratio-wall
alphabet.  It starts from four ordered positive speeds in the relative domain
u4/u1 < 8 and symbolically executes the center-free torus contact rule.

Integer contact centers are retained only as lazy certificate provenance for the
*next* lifted boundary.  Whenever two candidate next-event times can exchange
order, their equality locus generates an exact rational pair-ratio coordinate.
The continuous parameter domain is split only as much as needed to identify the
next simultaneous/minimal event group.

After every symbolic history has reached a first witness, a second pass proposes
coordinates from partial-region separators.  Partial-region singleton separators
are only a discovery heuristic: unresolved coordinates may separate refinements
jointly, so they are not a general minimality proof.  The result is therefore
certified independently after materializing the complete generated sign grammar.
Every retained coordinate has a deletion witness: two full sign cells of
different tasks agree on every other generated coordinate.  The retained set is
also checked to determine the task on every full sign cell.  Together these are
an exact lower and upper certificate for the declared coordinate grammar.

This is a research-local compiler.  It does not establish a public API or a new
Lonely Runner theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


K = 4
DELTA = Fraction(1, 5)
RMAX = Fraction(8)
PAIRS = tuple(combinations(range(K), 2))


@dataclass(frozen=True)
class Bound:
    weight: Fraction
    strict: bool = False


Closure = tuple[tuple[Bound | None, ...], ...]
Coordinate = tuple[int, int, Fraction]
Task = tuple[int, tuple[tuple[int, int, str], ...], str]


@dataclass(frozen=True)
class NextContact:
    alpha: Fraction
    center: int
    kind: str


@dataclass(frozen=True)
class TerminalRegion:
    closure: Closure
    task: Task


@dataclass(frozen=True)
class DeletionWitness:
    coordinate_index: int
    left_signature: tuple[int, ...]
    right_signature: tuple[int, ...]
    left_task: Task
    right_task: Task


@dataclass(frozen=True)
class LazyCompilerResult:
    symbolic_states: int
    terminal_regions: int
    task_count: int
    max_event_index: int
    max_contact_center: int
    generated_coordinates: tuple[Coordinate, ...]
    minimum_task_coordinates: tuple[Coordinate, ...]
    unique_separator_witnesses: int
    full_sign_cells: int
    exact_deletion_witnesses: int
    deletion_witnesses: tuple[DeletionWitness, ...]


def _tighter(left: Bound, right: Bound | None) -> bool:
    if right is None:
        return True
    return left.weight < right.weight or (
        left.weight == right.weight and left.strict and not right.strict
    )


def _compose(left: Bound, right: Bound) -> Bound:
    return Bound(left.weight * right.weight, left.strict or right.strict)


def _add_edge(
    closure: Closure,
    source: int,
    target: int,
    weight: Fraction,
    strict: bool,
) -> Closure | None:
    """Add u_target/u_source <= weight and re-close multiplicatively."""

    edge = Bound(Fraction(weight), strict)
    if closure[source][target] is not None and not _tighter(
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
        prefix = _compose(to_source, edge)
        for last in range(size):
            from_target = closure[target][last]
            if from_target is None:
                continue
            candidate = _compose(prefix, from_target)
            if _tighter(candidate, updated[first][last]):
                updated[first][last] = candidate

    for vertex in range(size):
        diagonal = updated[vertex][vertex]
        assert diagonal is not None
        if diagonal.weight < 1 or (
            diagonal.weight == 1 and diagonal.strict
        ):
            return None

    return tuple(tuple(row) for row in updated)


def _initial_closure() -> Closure:
    rows: list[list[Bound | None]] = [[None] * K for _ in range(K)]
    for vertex in range(K):
        rows[vertex][vertex] = Bound(Fraction(1), False)
    closure: Closure = tuple(tuple(row) for row in rows)

    # Ordered speeds u1 < u2 < u3 < u4.
    for runner in range(K - 1):
        next_closure = _add_edge(
            closure,
            runner + 1,
            runner,
            Fraction(1),
            True,
        )
        assert next_closure is not None
        closure = next_closure

    # Same relative domain used by the earlier four-speed Sonnet calibrations.
    next_closure = _add_edge(closure, 0, K - 1, RMAX, True)
    assert next_closure is not None
    return next_closure


def _relation(
    closure: Closure,
    pair: tuple[int, int],
    threshold: Fraction,
) -> int | None:
    """Return sign(u_j/u_i-threshold) if forced by the exact closure."""

    first, second = pair
    threshold = Fraction(threshold)
    upper = closure[first][second]
    reciprocal_upper = closure[second][first]
    assert upper is not None and reciprocal_upper is not None

    if upper.weight < threshold or (
        upper.weight == threshold and upper.strict
    ):
        return -1

    reciprocal_threshold = Fraction(1, 1) / threshold
    if reciprocal_upper.weight < reciprocal_threshold or (
        reciprocal_upper.weight == reciprocal_threshold
        and reciprocal_upper.strict
    ):
        return 1

    if (
        upper.weight == threshold
        and not upper.strict
        and reciprocal_upper.weight == reciprocal_threshold
        and not reciprocal_upper.strict
    ):
        return 0

    return None


def _impose_time_equal(
    closure: Closure,
    first: int,
    left: NextContact,
    second: int,
    right: NextContact,
) -> Closure | None:
    # alpha_i/u_i = alpha_j/u_j  <=>  u_j/u_i = alpha_j/alpha_i.
    ratio = right.alpha / left.alpha
    result = _add_edge(closure, first, second, ratio, False)
    if result is None:
        return None
    return _add_edge(result, second, first, 1 / ratio, False)


def _impose_time_less(
    closure: Closure,
    first: int,
    left: NextContact,
    second: int,
    right: NextContact,
) -> Closure | None:
    # alpha_i/u_i < alpha_j/u_j  <=>  u_j/u_i < alpha_j/alpha_i.
    return _add_edge(
        closure,
        first,
        second,
        right.alpha / left.alpha,
        True,
    )


def _minimum_groups(
    closure: Closure,
    events: tuple[NextContact, ...],
) -> tuple[tuple[tuple[int, ...], Closure], ...]:
    """Partition one symbolic region by its exact next simultaneous group."""

    branches = []
    for mask in range(1, 1 << K):
        group = tuple(runner for runner in range(K) if mask & (1 << runner))
        next_closure: Closure | None = closure

        anchor = group[0]
        for runner in group[1:]:
            assert next_closure is not None
            next_closure = _impose_time_equal(
                next_closure,
                anchor,
                events[anchor],
                runner,
                events[runner],
            )
            if next_closure is None:
                break
        if next_closure is None:
            continue

        group_set = set(group)
        for runner in group:
            for other in range(K):
                if other in group_set:
                    continue
                next_closure = _impose_time_less(
                    next_closure,
                    runner,
                    events[runner],
                    other,
                    events[other],
                )
                if next_closure is None:
                    break
            if next_closure is None:
                break

        if next_closure is not None:
            branches.append((group, next_closure))

    return tuple(branches)


def _advance(event: NextContact) -> NextContact:
    if event.kind == "exit":
        center = event.center + 1
        return NextContact(Fraction(center) - DELTA, center, "enter")
    if event.kind == "enter":
        return NextContact(
            Fraction(event.center) + DELTA,
            event.center,
            "exit",
        )
    raise AssertionError(event.kind)


def _terminal_separator_sets(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
) -> tuple[tuple[int, ...], ...]:
    signatures = tuple(
        tuple(_relation(region.closure, (i, j), ratio) for i, j, ratio in coordinates)
        for region in terminals
    )

    conflicts = []
    for first, second in combinations(range(len(terminals)), 2):
        if terminals[first].task == terminals[second].task:
            continue
        separators = tuple(
            index
            for index, (left, right) in enumerate(
                zip(signatures[first], signatures[second])
            )
            if left is not None and right is not None and left != right
        )
        assert separators, "different terminal tasks must be geometrically separated"
        conflicts.append(separators)
    return tuple(conflicts)


def _add_sign(
    closure: Closure,
    coordinate: Coordinate,
    sign: int,
) -> Closure | None:
    """Intersect one exact ratio closure with a ternary coordinate sign."""

    first, second, ratio = coordinate
    if sign == -1:
        return _add_edge(closure, first, second, ratio, True)
    if sign == 0:
        result = _add_edge(closure, first, second, ratio, False)
        if result is None:
            return None
        return _add_edge(result, second, first, 1 / ratio, False)
    if sign == 1:
        return _add_edge(closure, second, first, 1 / ratio, True)
    raise ValueError(f"invalid ternary sign: {sign}")


def _refine_signature(
    closure: Closure,
    coordinates: tuple[Coordinate, ...],
) -> tuple[tuple[int, ...], ...]:
    """Materialize every feasible full sign cell inside one exact closure."""

    signs: list[int | None] = [None] * len(coordinates)
    output: set[tuple[int, ...]] = set()

    def visit(depth: int, current: Closure) -> None:
        if depth == len(coordinates):
            signature = tuple(int(sign) for sign in signs if sign is not None)
            assert len(signature) == len(coordinates)
            output.add(signature)
            return

        first, second, ratio = coordinates[depth]
        forced = _relation(current, (first, second), ratio)
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
    return tuple(sorted(output))


def _full_task_sign_cells(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
) -> dict[tuple[int, ...], Task]:
    """Return the task on every feasible cell of the complete sign grammar."""

    task_by_signature: dict[tuple[int, ...], Task] = {}
    for region in terminals:
        for signature in _refine_signature(region.closure, coordinates):
            previous = task_by_signature.setdefault(signature, region.task)
            assert previous == region.task, (
                "complete generated sign grammar does not determine the task"
            )
    return task_by_signature


def _deletion_witnesses(
    task_by_signature: dict[tuple[int, ...], Task],
    coordinate_indices: set[int],
) -> tuple[DeletionWitness, ...]:
    """Find coordinates forced in every sufficient subset of the full grammar.

    A returned index has two complete sign cells with different tasks whose
    signatures become identical after deleting exactly that index.  No subset
    of the declared full grammar can distinguish that pair without the indexed
    coordinate.
    """

    witnesses: list[DeletionWitness] = []
    for index in sorted(coordinate_indices):
        by_deleted_signature: dict[
            tuple[int, ...], tuple[tuple[int, ...], Task]
        ] = {}
        for signature, task in task_by_signature.items():
            deleted = signature[:index] + signature[index + 1 :]
            previous = by_deleted_signature.get(deleted)
            if previous is not None and previous[1] != task:
                witnesses.append(
                    DeletionWitness(
                        coordinate_index=index,
                        left_signature=previous[0],
                        right_signature=signature,
                        left_task=previous[1],
                        right_task=task,
                    )
                )
                break
            by_deleted_signature[deleted] = (signature, task)
    return tuple(witnesses)


def analyze_lazy_compiler() -> LazyCompilerResult:
    """Generate and minimize task predicates without a center horizon."""

    initial_events = tuple(NextContact(DELTA, 0, "exit") for _ in range(K))
    stack = [
        (
            _initial_closure(),
            initial_events,
            frozenset(range(K)),
            0,
        )
    ]
    seen = set()
    terminals: list[TerminalRegion] = []
    generated: set[Coordinate] = set()
    max_center = 0

    while stack:
        closure, events, bad, event_index = stack.pop()
        state_key = (closure, events, bad, event_index)
        if state_key in seen:
            continue
        seen.add(state_key)

        for first, second in PAIRS:
            threshold = events[second].alpha / events[first].alpha
            if _relation(closure, (first, second), threshold) is None:
                generated.add((first, second, threshold))

        for group, child_closure in _minimum_groups(closure, events):
            child_index = event_index + 1
            group_set = set(group)
            bad_on = set(bad) - group_set
            bad_after = set(bad)
            child_events = list(events)
            boundary = []

            for runner in group:
                event = events[runner]
                max_center = max(max_center, event.center)
                boundary.append((runner, event.center, event.kind))
                if event.kind == "exit":
                    bad_after.discard(runner)
                else:
                    bad_after.add(runner)
                child_events[runner] = _advance(event)

            if not bad_on:
                task: Task = (
                    child_index,
                    tuple(sorted(boundary)),
                    "interval" if not bad_after else "point",
                )
                terminals.append(TerminalRegion(child_closure, task))
            else:
                stack.append(
                    (
                        child_closure,
                        tuple(child_events),
                        frozenset(bad_after),
                        child_index,
                    )
                )

    coordinates = tuple(sorted(generated))
    terminal_tuple = tuple(terminals)
    conflicts = _terminal_separator_sets(terminal_tuple, coordinates)

    mandatory_indices = {
        separators[0]
        for separators in conflicts
        if len(separators) == 1
    }
    mandatory = tuple(
        coordinate
        for index, coordinate in enumerate(coordinates)
        if index in mandatory_indices
    )

    # This is a useful partial-region discovery check, but not by itself a
    # lower-bound proof: unresolved coordinates can separate refinements jointly.
    assert all(
        any(index in mandatory_indices for index in separators)
        for separators in conflicts
    )

    # Independent exact certificate in the complete 33-coordinate sign grammar.
    # The selected coordinates must determine every full-cell task (upper bound),
    # and every selected coordinate must have a full-cell deletion witness (lower
    # bound).  The latter is stronger than a singleton separator between partial
    # terminal regions.
    task_by_signature = _full_task_sign_cells(terminal_tuple, coordinates)
    task_by_selected_signature: dict[tuple[int, ...], Task] = {}
    selected_indices = tuple(sorted(mandatory_indices))
    for signature, task in task_by_signature.items():
        selected = tuple(signature[index] for index in selected_indices)
        previous = task_by_selected_signature.setdefault(selected, task)
        assert previous == task, "selected coordinates do not determine the task"

    deletion_witnesses = _deletion_witnesses(
        task_by_signature,
        mandatory_indices,
    )
    deletion_witness_indices = {
        witness.coordinate_index
        for witness in deletion_witnesses
    }
    assert deletion_witness_indices == mandatory_indices, (
        "every selected coordinate needs a complete-sign deletion witness"
    )

    tasks = {region.task for region in terminal_tuple}
    return LazyCompilerResult(
        symbolic_states=len(seen),
        terminal_regions=len(terminal_tuple),
        task_count=len(tasks),
        max_event_index=max(task[0] for task in tasks),
        max_contact_center=max_center,
        generated_coordinates=coordinates,
        minimum_task_coordinates=mandatory,
        unique_separator_witnesses=len(mandatory_indices),
        full_sign_cells=len(task_by_signature),
        exact_deletion_witnesses=len(deletion_witnesses),
        deletion_witnesses=deletion_witnesses,
    )


def main() -> None:
    result = analyze_lazy_compiler()
    print("Sonnet 001 canonical lazy contact compiler")
    print(f"  symbolic states:          {result.symbolic_states}")
    print(f"  terminal regions:         {result.terminal_regions}")
    print(f"  first-witness semantics:  {result.task_count}")
    print(f"  max event index:          {result.max_event_index}")
    print(f"  max contact center:       {result.max_contact_center}")
    print(f"  generated coordinates:    {len(result.generated_coordinates)}")
    print(f"  exact minimum coordinates:{len(result.minimum_task_coordinates)}")
    print(f"  full generated sign cells: {result.full_sign_cells}")
    print(f"  deletion witnesses:        {result.exact_deletion_witnesses}")
    for coordinate in result.minimum_task_coordinates:
        print("   ", coordinate)


if __name__ == "__main__":
    main()
