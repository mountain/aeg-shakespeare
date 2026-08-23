"""Phase 11C: objectify canonical first-witness tasks after process canonicalization.

Phase 11B reconstructs the old full first-witness certificate task

    (event_index, lifted_boundary_with_center, mode)

from canonical torus dynamics and finds a globally minimum 27-wall compilation.
That task intentionally retained old solver/certificate provenance so the new
route could be compared byte-for-byte with the staged Sonnet results.

This calibration now asks a different question: what happens when the task is
itself quotiented by representation provenance *after* the process has already
been canonicalized?

The main canonical projection keeps only

    ((runner, enter/exit), ...), mode

at the first witness.  It drops both the event rank and the universal-cover
contact-center sheet.  The same 261 exact terminal regions and the same 33
process-generated candidate coordinates are used; only the observer/task changes.

All minimum-coordinate claims below have exact singleton-separator lower-bound
witnesses, as in Phase 11B1.  The optional Hauffman placement reuses the exact
decision-tree objective from Phase 11B2.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

import canonical_global_compilation as globalc
import canonical_lazy_contact_compiler as lazy


ProjectedTask = object


@dataclass(frozen=True)
class ProjectionSummary:
    task_count: int
    minimum_coordinates: tuple[lazy.Coordinate, ...]
    conflict_pairs: int


@dataclass(frozen=True)
class CanonicalTaskHauffman:
    sign_cells: int
    tasks: int
    weighted_depth: int
    tree_nodes: int
    worst_depth: int
    internal_nodes: int
    dag_nodes: int
    peak_frontier: int
    widths: tuple[int, ...]
    root_coordinate: lazy.Coordinate


@dataclass(frozen=True)
class CanonicalTaskObjectificationResult:
    generated_coordinates: int
    full_certificate: ProjectionSummary
    history_free_certificate: ProjectionSummary
    canonical_witness: ProjectionSummary
    mode_only: ProjectionSummary
    removed_history_coordinates: tuple[lazy.Coordinate, ...]
    canonical_sign_cells: int
    canonical_hauffman: CanonicalTaskHauffman | None


def full_certificate(task: lazy.Task) -> ProjectedTask:
    return task


def history_free_certificate(task: lazy.Task) -> ProjectedTask:
    """Drop only event rank; retain lifted boundary center and witness mode."""

    _event_index, boundary, mode = task
    return boundary, mode


def canonical_witness(task: lazy.Task) -> ProjectedTask:
    """Drop history rank and universal-cover sheet from the witness record."""

    _event_index, boundary, mode = task
    local_boundary = tuple(
        sorted((runner, kind) for runner, _center, kind in boundary)
    )
    return local_boundary, mode


def mode_only(task: lazy.Task) -> ProjectedTask:
    """Very coarse observer used as a lower-information red team."""

    return task[2]


def _terminal_signatures(
    terminals: tuple[lazy.TerminalRegion, ...],
    coordinates: tuple[lazy.Coordinate, ...],
) -> tuple[tuple[int | None, ...], ...]:
    return tuple(
        tuple(
            lazy._relation(region.closure, (first, second), ratio)
            for first, second, ratio in coordinates
        )
        for region in terminals
    )


def _minimum_for_projection(
    terminals: tuple[lazy.TerminalRegion, ...],
    coordinates: tuple[lazy.Coordinate, ...],
    signatures: tuple[tuple[int | None, ...], ...],
    project,
) -> ProjectionSummary:
    projected = tuple(project(region.task) for region in terminals)
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
        assert separators, "different projected tasks must be geometrically separated"
        conflicts.append(separators)

    mandatory_indices = {
        separators[0]
        for separators in conflicts
        if len(separators) == 1
    }
    assert all(
        any(index in mandatory_indices for index in separators)
        for separators in conflicts
    ), "singleton lower bound must attain the projected-task minimum"

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


def _canonical_sign_cells(
    terminals: tuple[lazy.TerminalRegion, ...],
    coordinates: tuple[lazy.Coordinate, ...],
):
    task_by_signature = {}
    for region in terminals:
        task = canonical_witness(region.task)
        for signature, _closure in globalc._refine_signature(
            region.closure,
            coordinates,
        ):
            previous = task_by_signature.get(signature)
            if previous is not None:
                assert previous == task
            task_by_signature[signature] = task
    return task_by_signature


def _hauffman(
    coordinates: tuple[lazy.Coordinate, ...],
    task_by_signature,
) -> CanonicalTaskHauffman:
    signatures = tuple(task_by_signature)
    task_values = sorted(set(task_by_signature.values()), key=repr)
    task_id = {task: index for index, task in enumerate(task_values)}
    task_ids = tuple(
        task_id[task_by_signature[signature]]
        for signature in signatures
    )
    weights = globalc._usage_weights(coordinates, signatures)
    tree, cost = globalc._build_tree(signatures, task_ids, weights)
    histories = tuple(
        globalc._history(tree, signature)
        for signature in signatures
    )
    widths = globalc._widths(histories)

    assert sum(widths) == cost[1]
    assert tree.predicate is not None
    return CanonicalTaskHauffman(
        sign_cells=len(signatures),
        tasks=len(task_values),
        weighted_depth=cost[0],
        tree_nodes=cost[1],
        worst_depth=cost[2],
        internal_nodes=cost[3],
        dag_nodes=cost[3] + len(task_values),
        peak_frontier=max(widths),
        widths=widths,
        root_coordinate=coordinates[tree.predicate],
    )


def analyze_task_objectification(
    *,
    include_hauffman: bool = False,
) -> CanonicalTaskObjectificationResult:
    compiler = lazy.analyze_lazy_compiler()
    terminals = globalc._terminal_regions()
    coordinates = compiler.generated_coordinates
    signatures = _terminal_signatures(terminals, coordinates)

    full = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        full_certificate,
    )
    history_free = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        history_free_certificate,
    )
    canonical = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        canonical_witness,
    )
    mode = _minimum_for_projection(
        terminals,
        coordinates,
        signatures,
        mode_only,
    )

    assert full.minimum_coordinates == compiler.minimum_task_coordinates
    assert history_free.minimum_coordinates == canonical.minimum_coordinates

    removed = tuple(
        coordinate
        for coordinate in full.minimum_coordinates
        if coordinate not in set(canonical.minimum_coordinates)
    )

    task_by_signature = _canonical_sign_cells(
        terminals,
        canonical.minimum_coordinates,
    )
    huffman = (
        _hauffman(canonical.minimum_coordinates, task_by_signature)
        if include_hauffman
        else None
    )

    return CanonicalTaskObjectificationResult(
        generated_coordinates=len(coordinates),
        full_certificate=full,
        history_free_certificate=history_free,
        canonical_witness=canonical,
        mode_only=mode,
        removed_history_coordinates=removed,
        canonical_sign_cells=len(task_by_signature),
        canonical_hauffman=huffman,
    )


def main() -> None:
    result = analyze_task_objectification(include_hauffman=True)
    print("Sonnet 001 canonical task objectification")
    print(f"  generated coordinates: {result.generated_coordinates}")
    print(
        "  full certificate:      "
        f"{result.full_certificate.task_count} tasks / "
        f"{len(result.full_certificate.minimum_coordinates)} walls"
    )
    print(
        "  drop event rank:       "
        f"{result.history_free_certificate.task_count} tasks / "
        f"{len(result.history_free_certificate.minimum_coordinates)} walls"
    )
    print(
        "  canonical witness:     "
        f"{result.canonical_witness.task_count} tasks / "
        f"{len(result.canonical_witness.minimum_coordinates)} walls"
    )
    print(
        "  mode only:             "
        f"{result.mode_only.task_count} tasks / "
        f"{len(result.mode_only.minimum_coordinates)} walls"
    )
    print(f"  removed history walls:  {len(result.removed_history_coordinates)}")
    for coordinate in result.removed_history_coordinates:
        print("   ", coordinate)

    huffman = result.canonical_hauffman
    assert huffman is not None
    print(
        "  canonical sign/tasks:  "
        f"{huffman.sign_cells} / {huffman.tasks}"
    )
    print(
        "  weighted/tree/worst/internal: "
        f"{huffman.weighted_depth} / {huffman.tree_nodes} / "
        f"{huffman.worst_depth} / {huffman.internal_nodes}"
    )
    print(f"  peak / DAG:             {huffman.peak_frontier} / {huffman.dag_nodes}")
    print(f"  root:                   {huffman.root_coordinate}")
    print(f"  widths:                 {huffman.widths}")


if __name__ == "__main__":
    main()
