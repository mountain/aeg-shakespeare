"""Phase 13C: distinguish minimum-basis failure from full-grammar failure.

After the first critical boundary 47/7 remained clean, the next native outer
contact ratio is 7.  Probe the open domain just beyond it at RMAX=36/5=7.2.

Two grammars are conceptually different:

1. the exact cardinality-minimum canonical-task coordinate basis;
2. every process-generated coordinate encountered by the symbolic compiler.

If the minimum basis is clean, the full grammar is automatically clean because
it contains the same witness tree coordinates.  Only if the minimum basis fails
do we pay for a second exact clean-separability analysis on the full grammar.

This classifies a future failure as either:

* basis-completion pressure: minimum basis obstructed, full grammar clean;
* primitive/region pressure: even the full generated grammar obstructed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import clean_separator_theory as theory
import five_speed_clean_separator_sweep as sweep
import five_speed_dimension_transfer as transfer


PREVIOUS_PROBE = Fraction(48, 7)
CRITICAL_RMAX = Fraction(7)
PROBE_RMAX = Fraction(36, 5)


@dataclass(frozen=True)
class BasisVsFullResult:
    rmax: Fraction
    symbolic_states: int
    terminal_regions: int
    generated_coordinates: int
    canonical_tasks: int
    minimum_coordinates: int
    minimum_clean: bool
    minimum_tree_nodes: int | None
    minimum_max_depth: int | None
    minimum_root_coordinate: transfer.Coordinate | None
    minimum_obstruction_atomic: bool | None
    full_clean: bool
    full_analysis_required: bool
    full_tree_nodes: int | None
    full_max_depth: int | None
    full_obstruction_atomic: bool | None
    max_event_index: int
    max_contact_center: int


def next_outer_threshold_after_previous_probe() -> Fraction:
    delta = Fraction(1, 6)
    coefficients = set()
    # The first critical probe reaches center 8; include one additional layer.
    for center in range(10):
        coefficients.add(Fraction(center) + delta)
        if center >= 1:
            coefficients.add(Fraction(center) - delta)
    candidates = sorted(
        beta / alpha
        for alpha in coefficients
        for beta in coefficients
        if beta / alpha > PREVIOUS_PROBE
    )
    return candidates[0]


def _regions(terminals, coordinates):
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


def _root_coordinate(analysis, coordinates):
    if analysis.tree is None or analysis.tree.coordinate is None:
        return None
    return coordinates[analysis.tree.coordinate]


def analyze_probe() -> BasisVsFullResult:
    assert next_outer_threshold_after_previous_probe() == CRITICAL_RMAX

    old_rmax = transfer.RMAX
    transfer.RMAX = PROBE_RMAX
    try:
        terminals, generated, states, max_center = transfer._compile_terminal_regions()
        minimum, task_count = sweep._minimum_canonical_coordinates(
            terminals,
            generated,
        )

        minimum_regions = _regions(terminals, minimum)
        assert theory.pairwise_task_separable(minimum_regions)
        minimum_analysis = theory.analyze_clean_separability(minimum_regions)
        if minimum_analysis.tree is not None:
            assert theory.verify_tree(minimum_regions, minimum_analysis.tree)
        else:
            assert minimum_analysis.obstruction is not None
            assert theory.verify_obstruction(
                minimum_regions,
                minimum_analysis.obstruction,
            )

        if minimum_analysis.clean:
            # The clean witness uses only coordinates in the minimum basis, so
            # the superset grammar is clean without a second search.
            full_clean = True
            full_required = False
            full_analysis = None
        else:
            full_regions = _regions(terminals, generated)
            assert theory.pairwise_task_separable(full_regions)
            full_analysis = theory.analyze_clean_separability(full_regions)
            if full_analysis.tree is not None:
                assert theory.verify_tree(full_regions, full_analysis.tree)
            else:
                assert full_analysis.obstruction is not None
                assert theory.verify_obstruction(
                    full_regions,
                    full_analysis.obstruction,
                )
            full_clean = full_analysis.clean
            full_required = True

        return BasisVsFullResult(
            rmax=PROBE_RMAX,
            symbolic_states=states,
            terminal_regions=len(terminals),
            generated_coordinates=len(generated),
            canonical_tasks=task_count,
            minimum_coordinates=len(minimum),
            minimum_clean=minimum_analysis.clean,
            minimum_tree_nodes=minimum_analysis.tree_nodes,
            minimum_max_depth=minimum_analysis.max_depth,
            minimum_root_coordinate=_root_coordinate(minimum_analysis, minimum),
            minimum_obstruction_atomic=(
                minimum_analysis.obstruction.atomic
                if minimum_analysis.obstruction is not None
                else None
            ),
            full_clean=full_clean,
            full_analysis_required=full_required,
            full_tree_nodes=(
                full_analysis.tree_nodes
                if full_analysis is not None
                else minimum_analysis.tree_nodes
            ),
            full_max_depth=(
                full_analysis.max_depth
                if full_analysis is not None
                else minimum_analysis.max_depth
            ),
            full_obstruction_atomic=(
                full_analysis.obstruction.atomic
                if full_analysis is not None and full_analysis.obstruction is not None
                else None
            ),
            max_event_index=max(region.task[0] for region in terminals),
            max_contact_center=max_center,
        )
    finally:
        transfer.RMAX = old_rmax


def main() -> None:
    result = analyze_probe()
    print("Sonnet 001 Phase 13C minimum-basis/full-grammar probe")
    print(f"  next threshold:          {next_outer_threshold_after_previous_probe()}")
    print(f"  probe RMAX:              {result.rmax}")
    print(f"  states / regions:        {result.symbolic_states} / {result.terminal_regions}")
    print(f"  generated:               {result.generated_coordinates}")
    print(f"  tasks / minimum walls:   {result.canonical_tasks} / {result.minimum_coordinates}")
    print(
        "  minimum clean/tree/depth: "
        f"{result.minimum_clean} / {result.minimum_tree_nodes} / {result.minimum_max_depth}"
    )
    print(f"  minimum root:            {result.minimum_root_coordinate}")
    print(f"  full clean:              {result.full_clean}")
    print(f"  full analysis required:  {result.full_analysis_required}")
    print(f"  event / center:          {result.max_event_index} / {result.max_contact_center}")


if __name__ == "__main__":
    main()
