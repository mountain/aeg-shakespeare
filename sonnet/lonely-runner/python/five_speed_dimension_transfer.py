"""Phase 12A: five-speed dimension transfer of the canonical lazy compiler.

This is the first runner-dimension pressure test after the four-speed canonical
baseline was frozen in Phase 11.  It deliberately uses a tight but nontrivial
continuous domain:

    K = 5 relative speeds
    delta = 1/6
    1 < u2/u1 < ... < u5/u1 < 21/4

The threshold is chosen just above the analytically trivial regime u5/u1 < 5.
If u5/u1 < 5, the slowest initial exit occurs before the fastest first enter,
so all five runners exit the bad set before any runner can re-enter; the first
witness is then forced and no ratio predicate is needed.  RMAX=21/4 is a small
exact step beyond that threshold.

The script measures the growth of:

* horizon-free symbolic process states;
* terminal exact regions;
* process-generated ratio coordinates;
* full legacy-certificate and canonical-witness task bases;
* optional full static sign-cell materialization.

The static-cell pass is intentionally optional because its blow-up is itself the
scaling red team.  This script is research-local and proves no new Lonely Runner
case.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


K = 5
DELTA = Fraction(1, 6)
RMAX = Fraction(21, 4)
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
class ProjectionSummary:
    task_count: int
    minimum_coordinates: tuple[Coordinate, ...]
    conflict_pairs: int


@dataclass(frozen=True)
class FiveSpeedTransferResult:
    symbolic_states: int
    terminal_regions: int
    max_event_index: int
    max_contact_center: int
    generated_coordinates: int
    full_certificate: ProjectionSummary
    history_free_certificate: ProjectionSummary
    canonical_witness: ProjectionSummary
    mode_only: ProjectionSummary
    canonical_sign_cells: int | None


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
    """Add u_target/u_source <= weight and close multiplicatively."""

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

    next_closure = _add_edge(closure, 0, K - 1, RMAX, True)
    assert next_closure is not None
    return next_closure


def _relation(
    closure: Closure,
    pair: tuple[int, int],
    threshold: Fraction,
) -> int | None:
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
    branches = []
    for mask in range(1, 1 << K):
        group = tuple(
            runner
            for runner in range(K)
            if mask & (1 << runner)
        )
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
        return NextContact(
            Fraction(center) - DELTA,
            center,
            "enter",
        )
    if event.kind == "enter":
        return NextContact(
            Fraction(event.center) + DELTA,
            event.center,
            "exit",
        )
    raise AssertionError(event.kind)


def _compile_terminal_regions():
    initial_events = tuple(
        NextContact(DELTA, 0, "exit")
        for _ in range(K)
    )
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
            if _relation(
                closure,
                (first, second),
                threshold,
            ) is None:
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

    return (
        tuple(terminals),
        tuple(sorted(generated)),
        len(seen),
        max_center,
    )


def _terminal_signatures(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
):
    return tuple(
        tuple(
            _relation(region.closure, (first, second), ratio)
            for first, second, ratio in coordinates
        )
        for region in terminals
    )


def _full(task: Task):
    return task


def _history_free(task: Task):
    _index, boundary, mode = task
    return boundary, mode


def _canonical(task: Task):
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


def _mode(task: Task):
    return task[2]


def _minimum_for_projection(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
    signatures,
    project,
) -> ProjectionSummary:
    projected = tuple(project(region.task) for region in terminals)
    mandatory_indices = set()
    conflicts = []

    for first, second in combinations(range(len(terminals)), 2):
        if projected[first] == projected[second]:
            continue
        separators = tuple(
            index
            for index, (left, right) in enumerate(
                zip(signatures[first], signatures[second])
            )
            if left is not None and right is not None and left != right
        )
        assert separators
        conflicts.append(separators)
        if len(separators) == 1:
            mandatory_indices.add(separators[0])

    assert all(
        any(index in mandatory_indices for index in separators)
        for separators in conflicts
    )

    minimum = tuple(
        coordinate
        for index, coordinate in enumerate(coordinates)
        if index in mandatory_indices
    )
    return ProjectionSummary(
        task_count=len(set(projected)),
        minimum_coordinates=minimum,
        conflict_pairs=len(conflicts),
    )


def _add_sign(
    closure: Closure,
    coordinate: Coordinate,
    sign: int,
) -> Closure | None:
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
    raise AssertionError(sign)


def _refine_signature(
    closure: Closure,
    coordinates: tuple[Coordinate, ...],
):
    signs: list[int | None] = [None] * len(coordinates)
    output = {}

    def visit(depth: int, current: Closure) -> None:
        if depth == len(coordinates):
            signature = tuple(int(sign) for sign in signs if sign is not None)
            assert len(signature) == len(coordinates)
            output[signature] = current
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
    return tuple(sorted(output.items()))


def _canonical_sign_cell_count(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
) -> int:
    task_by_signature = {}
    for region in terminals:
        task = _canonical(region.task)
        for signature, _closure in _refine_signature(
            region.closure,
            coordinates,
        ):
            previous = task_by_signature.get(signature)
            if previous is not None:
                assert previous == task
            task_by_signature[signature] = task
    return len(task_by_signature)


def analyze_five_speed_transfer(
    *,
    include_static_cells: bool = False,
) -> FiveSpeedTransferResult:
    terminals, coordinates, states, max_center = _compile_terminal_regions()
    signatures = _terminal_signatures(terminals, coordinates)

    full = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        _full,
    )
    history_free = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        _history_free,
    )
    canonical = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        _canonical,
    )
    mode = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        _mode,
    )

    assert history_free.minimum_coordinates == canonical.minimum_coordinates

    static_cells = (
        _canonical_sign_cell_count(
            terminals,
            canonical.minimum_coordinates,
        )
        if include_static_cells
        else None
    )

    return FiveSpeedTransferResult(
        symbolic_states=states,
        terminal_regions=len(terminals),
        max_event_index=max(region.task[0] for region in terminals),
        max_contact_center=max_center,
        generated_coordinates=len(coordinates),
        full_certificate=full,
        history_free_certificate=history_free,
        canonical_witness=canonical,
        mode_only=mode,
        canonical_sign_cells=static_cells,
    )


def main() -> None:
    result = analyze_five_speed_transfer(include_static_cells=True)
    print("Sonnet 001 five-speed canonical dimension transfer")
    print(f"  symbolic states:         {result.symbolic_states}")
    print(f"  terminal regions:        {result.terminal_regions}")
    print(f"  max event / center:      {result.max_event_index} / {result.max_contact_center}")
    print(f"  generated coordinates:   {result.generated_coordinates}")
    print(
        "  full tasks / walls:     "
        f"{result.full_certificate.task_count} / "
        f"{len(result.full_certificate.minimum_coordinates)}"
    )
    print(
        "  drop-rank tasks / walls:"
        f"{result.history_free_certificate.task_count} / "
        f"{len(result.history_free_certificate.minimum_coordinates)}"
    )
    print(
        "  canonical tasks / walls:"
        f"{result.canonical_witness.task_count} / "
        f"{len(result.canonical_witness.minimum_coordinates)}"
    )
    print(
        "  mode tasks / walls:     "
        f"{result.mode_only.task_count} / "
        f"{len(result.mode_only.minimum_coordinates)}"
    )
    print(f"  canonical sign cells:    {result.canonical_sign_cells}")


if __name__ == "__main__":
    main()
