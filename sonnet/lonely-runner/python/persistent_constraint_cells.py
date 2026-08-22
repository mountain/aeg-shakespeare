"""Phase 9A: exact persistent constraint cells and frozen next-layer detector.

The center-2 -> center-3 research loop ended with a 2,753-item joint
representation over 21 old task-relevant walls and seven frozen completion
walls.  To continue to center 4 without reconstructing the full center-3 wall
arrangement, each joint item is materialized here as:

    task semantic
    + joint predicate signature
    + a finite union of exact multiplicative difference-constraint closures.

Each closure atom comes from one realizable center-2 full sign cell refined only
by the seven frozen center-3 completion walls.  This retains exactly the process
constraints already used by Phase 8E without silently adding omitted center-3
wall coordinates.

The same generic next-layer pressure detector is first calibrated on the
center-2 -> center-3 step.  On a fully resolved center-2 cell its causal-prefix
query is equivalent to the earlier explicit history computation.  Only after
that exact equality is checked should the identical detector be applied to the
partially materialized center-3 cells and the new center-4 contact layer.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import controlled_interleaving as ci
import local_contact_refinement as lcr
import pair_difference_refinement as pd
import residual_objectification as ro


Task = tuple[object, ...]
Closure = tuple[tuple[pd.Bound | None, ...], ...]


@dataclass(frozen=True)
class PersistentConstraintCell:
    signature: tuple[int, ...]
    task: Task
    atoms: tuple[Closure, ...]
    provenance_count: int


@dataclass(frozen=True)
class PressurePartition:
    stable: frozenset[tuple[int, ...]]
    nonbranching_pressure: frozenset[tuple[int, ...]]
    completion_pressure: frozenset[tuple[int, ...]]

    @property
    def affected(self) -> frozenset[tuple[int, ...]]:
        return self.nonbranching_pressure | self.completion_pressure


def _closure_for_system(system, strata) -> Closure:
    closure = pd.initial_closure()
    for pair in pd.PAIRS:
        closure = pd.add_edges(
            closure,
            pd.stratum_edges(pair, strata[system[pd.PAIR_INDEX[pair]]]),
        )
        assert closure is not None
    return closure


def _relation_from_closure(
    closure: Closure,
    pair: tuple[int, int],
    threshold: Fraction,
) -> int | None:
    """Return sign(u_j/u_i-threshold) when exact closure forces it."""

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


def _event_relation(closure: Closure, left, right) -> int | None:
    """Sign(t_left-t_right) when the closure decides the contact ordering."""

    i = left[0]
    j = right[0]
    a = lcr.alpha(left)
    b = lcr.alpha(right)
    if i == j:
        return -1 if a < b else (1 if a > b else 0)
    if i < j:
        return _relation_from_closure(closure, (i, j), b / a)
    relation = _relation_from_closure(closure, (j, i), a / b)
    return None if relation is None else -relation


def _refine_closure_by_walls(
    base: Closure,
    walls: tuple[lcr.ResidualCoordinate, ...],
):
    signs: list[int | None] = [None] * len(walls)
    output: dict[tuple[int, ...], Closure] = {}

    def visit(depth: int, closure: Closure) -> None:
        if depth == len(walls):
            signature = tuple(int(value) for value in signs if value is not None)
            assert len(signature) == len(walls)
            previous = output.get(signature)
            # For one base closure and one complete sign signature the tightened
            # closure is deterministic.
            if previous is not None:
                assert previous == closure
            output[signature] = closure
            return

        wall = walls[depth]
        forced = _relation_from_closure(closure, wall.pair, wall.ratio)
        if forced is not None:
            signs[depth] = forced
            visit(depth + 1, closure)
            signs[depth] = None
            return

        for sign in (-1, 0, 1):
            next_closure = pd.add_edges(
                closure,
                ci._sign_edges(wall, sign),
            )
            if next_closure is None:
                continue
            signs[depth] = sign
            visit(depth + 1, next_closure)
        signs[depth] = None

    visit(0, base)
    assert output
    return output


def _center2_cells():
    ratios2 = pd.contact_ratios(2)
    strata2 = pd.strata(ratios2)
    systems2 = pd.enumerate_systems(strata2)
    tasks2 = tuple(
        pd.first_witness(system, 2, ratios2, strata2)[0]
        for system in systems2
    )
    full_signatures2 = tuple(
        pd.full_signature(system, ratios2, strata2)
        for system in systems2
    )
    relevant2 = pd.relevant_walls(systems2, tasks2, ratios2)
    assert len(systems2) == 5_823 and len(relevant2) == 21

    atoms = defaultdict(list)
    task_by_parent = {}
    for system, full_signature, task in zip(systems2, full_signatures2, tasks2):
        parent = tuple(full_signature[index] for index in relevant2)
        atoms[parent].append(_closure_for_system(system, strata2))
        previous = task_by_parent.get(parent)
        if previous is not None:
            assert previous == task
        task_by_parent[parent] = task

    cells = tuple(
        PersistentConstraintCell(
            signature=parent,
            task=task_by_parent[parent],
            atoms=tuple(dict.fromkeys(atoms[parent])),
            provenance_count=len(atoms[parent]),
        )
        for parent in sorted(atoms)
    )
    assert len(cells) == 849
    assert sum(cell.provenance_count for cell in cells) == 5_823
    return ratios2, strata2, relevant2, cells


def build_center3_persistent_cells():
    """Materialize the frozen Phase-8E 2,753-item current representation."""

    base = lcr.analyze_center2_to_center3()
    ratios2, strata2, relevant2, center2_cells = _center2_cells()
    del ratios2

    new_walls = tuple(
        sorted(
            {
                coordinate
                for case in base.completion_residual_cases
                for coordinate in case.coordinates
            },
            key=lambda item: (item.pair, item.ratio),
        )
    )
    assert len(new_walls) == 7
    new_wall_index = {wall: index for index, wall in enumerate(new_walls)}

    # Freeze the six Phase-8C.2 task decoders.
    ratios3 = pd.contact_ratios(3)
    strata3 = pd.strata(ratios3)
    _r3, _s3, local = ro._reconstruct_local_completion_children(
        base.completion_required_parents
    )
    assert _r3 == ratios3 and _s3 == strata3
    completion_case = {case.parent: case for case in base.completion_residual_cases}
    decoder_by_parent = {}
    selected_indices = {}
    for parent in sorted(base.completion_required_parents):
        case = completion_case[parent]
        features = tuple(
            ro._feature_index(coordinate, ratios3)
            for coordinate in case.coordinates
        )
        records = ro._unique_raw_records(
            tuple(local[parent]),
            features,
            ratios3,
            strata3,
        )
        root, *_ = ro._optimal_decoder(records)
        decoder_by_parent[parent] = root
        selected_indices[parent] = tuple(new_wall_index[wall] for wall in case.coordinates)

    reindex_task = {case.parent: case.new_task for case in base.history_reindex_cases}

    atom_groups: dict[tuple[int, ...], list[Closure]] = defaultdict(list)
    provenance = defaultdict(int)
    task_by_signature = {}

    for cell in center2_cells:
        parent = cell.signature
        for atom in cell.atoms:
            variants = _refine_closure_by_walls(atom, new_walls)
            for new_signature, closure in variants.items():
                joint = tuple(parent) + tuple(new_signature)
                if parent in base.completion_required_parents:
                    key = tuple(new_signature[index] for index in selected_indices[parent])
                    task = ci._decoder_task(decoder_by_parent[parent], key)
                elif parent in base.history_reindex_parents:
                    task = reindex_task[parent]
                else:
                    task = cell.task
                previous = task_by_signature.get(joint)
                if previous is not None:
                    assert previous == task
                task_by_signature[joint] = task
                atom_groups[joint].append(closure)
                provenance[joint] += 1

    cells = tuple(
        PersistentConstraintCell(
            signature=signature,
            task=task_by_signature[signature],
            atoms=tuple(dict.fromkeys(atom_groups[signature])),
            provenance_count=provenance[signature],
        )
        for signature in sorted(atom_groups)
    )
    assert len(cells) == 2_753
    assert len({cell.task for cell in cells}) == 75
    return relevant2, new_walls, cells


def _named_events(max_center: int):
    return tuple(
        (runner, center, kind)
        for runner in range(pd.K)
        for center in range(max_center + 1)
        for kind in (("exit",) if center == 0 else ("enter", "exit"))
    )


def detect_next_layer_pressure(
    cells: tuple[PersistentConstraintCell, ...],
    *,
    old_center: int,
    new_center: int,
) -> PressurePartition:
    """Apply the frozen Phase-8 local pressure rules to a persistent cell set."""

    assert new_center == old_center + 1
    old_events = _named_events(old_center)
    new_events = tuple(
        (runner, new_center, kind)
        for runner in range(pd.K)
        for kind in ("enter", "exit")
    )
    genuinely_new_ratios = set(pd.contact_ratios(new_center)) - set(
        pd.contact_ratios(old_center)
    )

    forced = set()
    unresolved = set()

    for cell in cells:
        witness_event = cell.task[1][0]
        for atom in cell.atoms:
            if any(
                (relation := _event_relation(atom, new_event, witness_event))
                is not None
                and relation <= 0
                for new_event in new_events
            ):
                forced.add(cell.signature)

            # On a fully resolved old-center atom, this envelope is exactly the
            # old causal prefix.  On a partial persistent atom it is the safe
            # over-approximation of events that can still lie at/before witness.
            prefix_candidates = tuple(
                old_event
                for old_event in old_events
                if (
                    (relation := _event_relation(atom, old_event, witness_event))
                    is None
                    or relation <= 0
                )
            )
            hit = False
            for new_event in new_events:
                for old_event in prefix_candidates:
                    if new_event[2] == "enter" and old_event[2] == "enter":
                        continue
                    wall = lcr.collision_wall(new_event, old_event)
                    if wall is None or wall[2] not in genuinely_new_ratios:
                        continue
                    relation = _event_relation(atom, new_event, old_event)
                    if relation is None:
                        unresolved.add(cell.signature)
                        hit = True
                        break
                if hit:
                    break

    all_signatures = {cell.signature for cell in cells}
    completion = unresolved
    nonbranching = forced - unresolved
    stable = all_signatures - forced - unresolved
    assert stable | nonbranching | completion == all_signatures
    assert not stable & nonbranching
    assert not stable & completion
    assert not nonbranching & completion
    return PressurePartition(
        stable=frozenset(stable),
        nonbranching_pressure=frozenset(nonbranching),
        completion_pressure=frozenset(completion),
    )


def calibrate_center2_detector():
    """Require the generic cell detector to reproduce Phase 8A exactly."""

    _ratios2, _strata2, _relevant2, cells = _center2_cells()
    generic = detect_next_layer_pressure(cells, old_center=2, new_center=3)
    frozen = lcr.analyze_center2_to_center3()
    assert generic.stable == frozen.stable_parents
    assert generic.nonbranching_pressure == frozen.history_reindex_parents
    assert generic.completion_pressure == frozen.completion_required_parents
    return generic


def probe_center3_to_center4_pressure():
    """Apply the frozen detector to the Phase-8E current representation."""

    _old_walls, _new_walls, cells = build_center3_persistent_cells()
    partition = detect_next_layer_pressure(cells, old_center=3, new_center=4)
    return cells, partition


def main() -> None:
    calibrated = calibrate_center2_detector()
    print("Phase 9A detector replay center2 -> center3")
    print(f"  stable / nonbranching / completion: {len(calibrated.stable)} / {len(calibrated.nonbranching_pressure)} / {len(calibrated.completion_pressure)}")

    cells, partition = probe_center3_to_center4_pressure()
    print("Phase 9A frozen-rule probe center3 -> center4")
    print(f"  current persistent cells:          {len(cells)}")
    print(f"  unique current tasks:              {len({cell.task for cell in cells})}")
    print(f"  total exact closure atoms:         {sum(len(cell.atoms) for cell in cells)}")
    print(f"  provenance atoms before dedupe:    {sum(cell.provenance_count for cell in cells)}")
    print(f"  stable:                            {len(partition.stable)}")
    print(f"  nonbranching pressure:             {len(partition.nonbranching_pressure)}")
    print(f"  completion pressure:               {len(partition.completion_pressure)}")
    print(f"  affected total:                    {len(partition.affected)}")


if __name__ == "__main__":
    main()
