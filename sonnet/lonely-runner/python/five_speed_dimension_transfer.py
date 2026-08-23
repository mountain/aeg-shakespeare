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

Partial-sign singleton conflicts are used only to propose lower-bound witness
pairs.  Every retained coordinate is then certified strongly: after deleting
that coordinate, two different-task terminal closures are synchronously refined
to the same complete sign vector on all other process-generated coordinates.
Thus the minimum claims do not assume that unresolved coordinates vary
independently.

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
HistoryFreeTask = tuple[tuple[tuple[int, int, str], ...], str]
CanonicalTask = tuple[tuple[tuple[int, str], ...], str]
ProjectedTask = Task | HistoryFreeTask | CanonicalTask | str


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
    """Replayable full-grammar necessity certificate for one coordinate.

    ``common_signs`` follows the complete generated-coordinate order with
    ``coordinate_index`` omitted.  The two terminal closures have different
    projected tasks, realize this same sign vector on every retained coordinate,
    and force the two recorded opposite signs on the omitted coordinate.

    Refined closures are deliberately not retained: terminal IDs plus the common
    sign vector replay the refinement while keeping the result compact and made
    only of ordinary serializable tuples, integers, and strings.
    """

    coordinate_index: int
    left_terminal_id: int
    right_terminal_id: int
    left_projected_task: ProjectedTask
    right_projected_task: ProjectedTask
    common_signs: tuple[int, ...]
    left_coordinate_sign: int
    right_coordinate_sign: int


@dataclass(frozen=True)
class ProjectionSummary:
    task_count: int
    minimum_coordinates: tuple[Coordinate, ...]
    conflict_pairs: int
    deletion_witnesses: tuple[DeletionWitness, ...]


@dataclass(frozen=True)
class FiveSpeedTransferResult:
    symbolic_states: int
    terminal_regions: int
    max_event_index: int
    max_contact_center: int
    generated_coordinates: int
    coordinate_grammar: tuple[Coordinate, ...]
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
    """Find a sufficient basis, then strongly certify every lower-bound index.

    A singleton conflict in the partial terminal signatures is only a candidate
    necessity witness: unresolved coordinates may be jointly correlated.  The
    synchronous completion pass below closes that loophole by finding a common
    full sign vector on every other generated coordinate.
    """

    projected = tuple(project(region.task) for region in terminals)
    mandatory_indices: set[int] = set()
    singleton_pairs: dict[int, list[tuple[int, int]]] = {}
    conflicts: list[tuple[int, ...]] = []

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
            coordinate_index = separators[0]
            mandatory_indices.add(coordinate_index)
            singleton_pairs.setdefault(coordinate_index, []).append(
                (first, second)
            )

    # This proves sufficiency in the declared coordinate grammar.  Necessity is
    # established separately by full-sign deletion witnesses, not inferred from
    # the partial singleton signatures.
    assert all(
        not mandatory_indices.isdisjoint(separators)
        for separators in conflicts
    )
    conflict_count = len(conflicts)
    del conflicts

    minimum = tuple(
        coordinate
        for index, coordinate in enumerate(coordinates)
        if index in mandatory_indices
    )
    deletion_witnesses = _build_deletion_witnesses(
        terminals,
        coordinates,
        projected,
        project,
        mandatory_indices,
        singleton_pairs,
    )
    return ProjectionSummary(
        task_count=len(set(projected)),
        minimum_coordinates=minimum,
        conflict_pairs=conflict_count,
        deletion_witnesses=deletion_witnesses,
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


def _synchronous_full_sign_completion(
    left: Closure,
    right: Closure,
    coordinates: tuple[Coordinate, ...],
    deleted_index: int,
) -> tuple[Closure, Closure, tuple[int, ...]] | None:
    """Complete two closures to one shared sign vector off one coordinate."""

    active = tuple(
        index
        for index in range(len(coordinates))
        if index != deleted_index
    )
    failed: set[tuple[Closure, Closure, tuple[int, ...]]] = set()

    def visit(
        left_closure: Closure,
        right_closure: Closure,
        remaining: tuple[int, ...],
        assigned: tuple[tuple[int, int], ...],
    ) -> tuple[Closure, Closure, tuple[int, ...]] | None:
        key = (left_closure, right_closure, remaining)
        if key in failed:
            return None

        if not remaining:
            sign_by_index = dict(assigned)
            common_signs = tuple(sign_by_index[index] for index in active)
            return left_closure, right_closure, common_signs

        # Propagate a sign already forced on either side before introducing a
        # three-way branch.  This keeps the exact search small and deterministic.
        selected_position = None
        selected_relations = None
        for position, index in enumerate(remaining):
            first, second, ratio = coordinates[index]
            left_sign = _relation(
                left_closure,
                (first, second),
                ratio,
            )
            right_sign = _relation(
                right_closure,
                (first, second),
                ratio,
            )
            if left_sign is not None or right_sign is not None:
                selected_position = position
                selected_relations = left_sign, right_sign
                break

        if selected_position is None:
            selected_position = 0
            selected_relations = None, None

        index = remaining[selected_position]
        rest = (
            remaining[:selected_position]
            + remaining[selected_position + 1 :]
        )
        left_sign, right_sign = selected_relations
        if left_sign is not None and right_sign is not None:
            if left_sign != right_sign:
                failed.add(key)
                return None
            candidate_signs = (left_sign,)
        elif left_sign is not None:
            candidate_signs = (left_sign,)
        elif right_sign is not None:
            candidate_signs = (right_sign,)
        else:
            candidate_signs = (0, -1, 1)

        for sign in candidate_signs:
            next_left = left_closure
            next_right = right_closure
            if left_sign is None:
                next_left = _add_sign(next_left, coordinates[index], sign)
            if right_sign is None:
                next_right = _add_sign(next_right, coordinates[index], sign)
            if next_left is None or next_right is None:
                continue
            result = visit(
                next_left,
                next_right,
                rest,
                assigned + ((index, sign),),
            )
            if result is not None:
                return result

        failed.add(key)
        return None

    return visit(left, right, active, ())


def _replay_deletion_witness(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
    project,
    witness: DeletionWitness,
) -> bool:
    """Replay one compact witness without rerunning the witness search."""

    if not 0 <= witness.coordinate_index < len(coordinates):
        return False
    if not 0 <= witness.left_terminal_id < len(terminals):
        return False
    if not 0 <= witness.right_terminal_id < len(terminals):
        return False
    if len(witness.common_signs) != len(coordinates) - 1:
        return False
    if any(sign not in (-1, 0, 1) for sign in witness.common_signs):
        return False
    if witness.left_coordinate_sign not in (-1, 0, 1):
        return False
    if witness.right_coordinate_sign not in (-1, 0, 1):
        return False
    if witness.left_coordinate_sign == witness.right_coordinate_sign:
        return False

    left_region = terminals[witness.left_terminal_id]
    right_region = terminals[witness.right_terminal_id]
    left_task = project(left_region.task)
    right_task = project(right_region.task)
    if left_task != witness.left_projected_task:
        return False
    if right_task != witness.right_projected_task:
        return False
    if left_task == right_task:
        return False

    active = tuple(
        index
        for index in range(len(coordinates))
        if index != witness.coordinate_index
    )
    left_closure = left_region.closure
    right_closure = right_region.closure
    for index, sign in zip(active, witness.common_signs):
        left_closure = _add_sign(left_closure, coordinates[index], sign)
        right_closure = _add_sign(right_closure, coordinates[index], sign)
        if left_closure is None or right_closure is None:
            return False

    for index, sign in zip(active, witness.common_signs):
        first, second, ratio = coordinates[index]
        if _relation(left_closure, (first, second), ratio) != sign:
            return False
        if _relation(right_closure, (first, second), ratio) != sign:
            return False

    first, second, ratio = coordinates[witness.coordinate_index]
    return (
        _relation(left_closure, (first, second), ratio)
        == witness.left_coordinate_sign
        and _relation(right_closure, (first, second), ratio)
        == witness.right_coordinate_sign
    )


def _build_deletion_witnesses(
    terminals: tuple[TerminalRegion, ...],
    coordinates: tuple[Coordinate, ...],
    projected: tuple[ProjectedTask, ...],
    project,
    mandatory_indices: set[int],
    singleton_pairs: dict[int, list[tuple[int, int]]],
) -> tuple[DeletionWitness, ...]:
    """Produce one full-coordinate indistinguishability witness per index."""

    witnesses = []
    for coordinate_index in sorted(mandatory_indices):
        witness = None
        for left_terminal_id, right_terminal_id in singleton_pairs[
            coordinate_index
        ]:
            completion = _synchronous_full_sign_completion(
                terminals[left_terminal_id].closure,
                terminals[right_terminal_id].closure,
                coordinates,
                coordinate_index,
            )
            if completion is None:
                continue
            left_closure, right_closure, common_signs = completion
            first, second, ratio = coordinates[coordinate_index]
            left_sign = _relation(left_closure, (first, second), ratio)
            right_sign = _relation(right_closure, (first, second), ratio)
            assert left_sign is not None and right_sign is not None
            assert left_sign != right_sign
            witness = DeletionWitness(
                coordinate_index=coordinate_index,
                left_terminal_id=left_terminal_id,
                right_terminal_id=right_terminal_id,
                left_projected_task=projected[left_terminal_id],
                right_projected_task=projected[right_terminal_id],
                common_signs=common_signs,
                left_coordinate_sign=left_sign,
                right_coordinate_sign=right_sign,
            )

            # Verify every stored bit against the already refined exact closures.
            # Rebuilding those closures from scratch is deliberately reserved for
            # the compact replay path below, avoiding 185 duplicate refinements in
            # the default analysis.
            active = tuple(
                index
                for index in range(len(coordinates))
                if index != coordinate_index
            )
            for index, sign in zip(active, common_signs):
                other_first, other_second, other_ratio = coordinates[index]
                assert (
                    _relation(
                        left_closure,
                        (other_first, other_second),
                        other_ratio,
                    )
                    == sign
                )
                assert (
                    _relation(
                        right_closure,
                        (other_first, other_second),
                        other_ratio,
                    )
                    == sign
                )

            # Replay every compact certificate from terminal IDs and stored
            # signs.  The search-side refined closures above are not trusted as
            # the only validation path.
            assert _replay_deletion_witness(
                terminals,
                coordinates,
                project,
                witness,
            )
            break
        assert witness is not None, (
            "partial singleton candidate has no full-sign deletion witness: "
            f"coordinate {coordinate_index}"
        )
        witnesses.append(witness)

    return tuple(witnesses)


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
        coordinate_grammar=coordinates,
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
