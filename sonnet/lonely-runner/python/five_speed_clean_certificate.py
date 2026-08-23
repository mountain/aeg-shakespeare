"""Phase 13B: apply the generic clean-separator criterion to five-speed Sonnet.

This adapter deliberately does not reuse the Phase-12 clean-tree constructor.
It translates exact terminal closure regions into the generic partial-sign task
system of Phase 13A and asks the independent exact recursive solver for a clean
tree / obstruction certificate.

The frozen baseline is RMAX = 25/4, the widest Phase-12 domain.  A second probe
crosses the next primitive outer-runner contact-order threshold after 25/4:

    R* = (8-delta)/(1+delta) = (47/6)/(7/6) = 47/7.

At R=47/7, the fastest runner's center-8 enter can tie the slowest runner's
center-1 exit.  We probe just above it at 48/7.  The probe outcome is research
data: it may return either a clean tree or a verified recursive obstruction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import clean_separator_theory as theory
import five_speed_clean_separator_sweep as sweep
import five_speed_dimension_transfer as transfer


BASELINE_RMAX = Fraction(25, 4)
CRITICAL_RMAX = Fraction(47, 7)
PROBE_RMAX = Fraction(48, 7)


@dataclass(frozen=True)
class CertificateResult:
    rmax: Fraction
    symbolic_states: int
    terminal_regions: int
    generated_coordinates: int
    canonical_tasks: int
    minimum_coordinates: int
    pairwise_separable: bool
    clean: bool
    clean_states_visited: int
    clean_tree_nodes: int | None
    clean_max_depth: int | None
    root_coordinate: transfer.Coordinate | None
    obstruction_atomic: bool | None
    max_event_index: int
    max_contact_center: int


def next_outer_contact_threshold() -> Fraction:
    """First raw outer-pair contact ratio strictly above the Phase-12 endpoint."""

    delta = Fraction(1, 6)
    coefficients = set()
    # Current Phase-12 witnesses reach through center 7.  Include the next layer
    # so the first boundary that can change that fact is visible.
    for center in range(9):
        coefficients.add(Fraction(center) + delta)
        if center >= 1:
            coefficients.add(Fraction(center) - delta)

    candidates = sorted(
        beta / alpha
        for alpha in coefficients
        for beta in coefficients
        if beta / alpha > BASELINE_RMAX
    )
    return candidates[0]


def _partial_regions(terminals, coordinates):
    return tuple(
        theory.PartialRegion(
            name=index,
            task=sweep._canonical_task(region.task),
            signs=tuple(
                transfer._relation(
                    region.closure,
                    (first, second),
                    ratio,
                )
                for first, second, ratio in coordinates
            ),
        )
        for index, region in enumerate(terminals)
    )


def analyze_certificate(rmax: Fraction) -> CertificateResult:
    old_rmax = transfer.RMAX
    transfer.RMAX = Fraction(rmax)
    try:
        terminals, generated, states, max_center = transfer._compile_terminal_regions()
        coordinates, task_count = sweep._minimum_canonical_coordinates(
            terminals,
            generated,
        )
        regions = _partial_regions(terminals, coordinates)
        pairwise = theory.pairwise_task_separable(regions)
        analysis = theory.analyze_clean_separability(regions)

        root_coordinate = None
        if analysis.tree is not None and analysis.tree.coordinate is not None:
            root_coordinate = coordinates[analysis.tree.coordinate]
            assert theory.verify_tree(regions, analysis.tree)
        if analysis.obstruction is not None:
            assert theory.verify_obstruction(regions, analysis.obstruction)

        return CertificateResult(
            rmax=Fraction(rmax),
            symbolic_states=states,
            terminal_regions=len(terminals),
            generated_coordinates=len(generated),
            canonical_tasks=task_count,
            minimum_coordinates=len(coordinates),
            pairwise_separable=pairwise,
            clean=analysis.clean,
            clean_states_visited=analysis.states_visited,
            clean_tree_nodes=analysis.tree_nodes,
            clean_max_depth=analysis.max_depth,
            root_coordinate=root_coordinate,
            obstruction_atomic=(
                analysis.obstruction.atomic
                if analysis.obstruction is not None
                else None
            ),
            max_event_index=max(region.task[0] for region in terminals),
            max_contact_center=max_center,
        )
    finally:
        transfer.RMAX = old_rmax


def analyze_baseline_and_probe():
    assert next_outer_contact_threshold() == CRITICAL_RMAX
    return (
        analyze_certificate(BASELINE_RMAX),
        analyze_certificate(PROBE_RMAX),
    )


def main() -> None:
    print("Sonnet 001 Phase 13B clean-separability certificate")
    print(f"  next primitive outer threshold: {next_outer_contact_threshold()}")
    for result in analyze_baseline_and_probe():
        print(
            f"  R<{result.rmax}: "
            f"states={result.symbolic_states} "
            f"regions={result.terminal_regions} "
            f"generated={result.generated_coordinates} "
            f"tasks/walls={result.canonical_tasks}/{result.minimum_coordinates} "
            f"pairwise={result.pairwise_separable} "
            f"clean={result.clean} "
            f"clean-states={result.clean_states_visited} "
            f"tree/depth={result.clean_tree_nodes}/{result.clean_max_depth} "
            f"root={result.root_coordinate} "
            f"obstruction-atomic={result.obstruction_atomic} "
            f"event/center={result.max_event_index}/{result.max_contact_center}"
        )


if __name__ == "__main__":
    main()
