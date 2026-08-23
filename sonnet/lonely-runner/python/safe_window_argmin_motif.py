"""Phase 14B: identify the safe-window completion obstruction as argmin geometry.

This module does not add a reusable abstraction.  It is a research-local exact
audit of the strongest K=4 and K=5 split parents found by Phase 14A.

For m candidate next-enter events, the exact task "which nonempty subset attains
the minimum?" has one region for every nonempty subset S.  On a pairwise event-
time comparison (i,j), that region forces

    -1  if i is minimal and j is not,
     0  if both are minimal,
    +1  if j is minimal and i is not,
    None if neither is minimal.

For m=2 all three regions decide the single comparison, so the task is clean.
For m=3 the seven regions are pairwise distinguishable, but every pairwise
coordinate is undefined on the region whose unique winner is the third event;
there is no clean root query.  Phase 14 checks whether the real Lonely Runner
safe-window split parents instantiate these exact partial-sign systems.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

import clean_separator_theory as clean
import safe_window_task_transfer as transfer


@dataclass(frozen=True)
class ArgminMotifSummary:
    runners: int
    active_closer_runners: tuple[int, ...]
    closer_tasks: tuple[tuple[int, ...], ...]
    minimum_support_pairs: tuple[tuple[int, int], ...]
    minimum_support_size: int
    partial_signatures: tuple[tuple[tuple[int, ...], tuple[int | None, ...]], ...]
    matches_exact_argmin_geometry: bool
    pairwise_separable: bool
    clean: bool


def _expected_sign(closer, first: int, second: int):
    first_min = first in closer
    second_min = second in closer
    if first_min and second_min:
        return 0
    if first_min:
        return -1
    if second_min:
        return 1
    return None


def _strongest_case(module):
    frontiers, _old_coordinates, _states = transfer._compile_frontiers(module)
    _extended, _next, alternatives, cases = transfer._extend_safe_window(
        module,
        frontiers,
    )
    case = max(cases, key=lambda item: (item.closer_count, -item.parent_index))
    frontier = frontiers[case.parent_index]

    raw_branches = module._minimum_groups(frontier.closure, frontier.next_events)
    branches = tuple((tuple(group), closure) for group, closure in raw_branches)
    relations = transfer._branch_relations(module, branches, case.candidates)

    candidate_index = {
        coordinate: index
        for index, coordinate in enumerate(case.candidates)
    }
    selected_indices = tuple(
        candidate_index[coordinate]
        for coordinate in case.minimum_support
    )

    closer_tasks = tuple(sorted(closer for closer, _closure in branches))
    active = tuple(sorted({runner for closer in closer_tasks for runner in closer}))
    selected_pairs = tuple((first, second) for first, second, _ratio in case.minimum_support)

    actual = tuple(
        (
            closer,
            tuple(relations[index][coordinate] for coordinate in selected_indices),
        )
        for index, (closer, _closure) in enumerate(branches)
    )
    actual = tuple(sorted(actual))

    expected_closers = tuple(
        sorted(
            tuple(active[index] for index in range(len(active)) if mask & (1 << index))
            for mask in range(1, 1 << len(active))
        )
    )
    expected_pairs = tuple(combinations(active, 2))
    expected = tuple(
        (
            closer,
            tuple(_expected_sign(closer, first, second) for first, second in expected_pairs),
        )
        for closer in expected_closers
    )

    # The lexicographic minimum support must be exactly the complete pair grammar
    # on the active closer candidates for the m=2/m=3 motifs studied here.
    matches = (
        closer_tasks == expected_closers
        and selected_pairs == expected_pairs
        and actual == expected
    )

    regions = tuple(
        clean.PartialRegion(name=closer, task=closer, signs=signs)
        for closer, signs in actual
    )
    analysis = clean.analyze_clean_separability(regions)

    return ArgminMotifSummary(
        runners=module.K,
        active_closer_runners=active,
        closer_tasks=closer_tasks,
        minimum_support_pairs=selected_pairs,
        minimum_support_size=len(case.minimum_support),
        partial_signatures=actual,
        matches_exact_argmin_geometry=matches,
        pairwise_separable=clean.pairwise_task_separable(regions),
        clean=analysis.clean,
    )


def analyze_safe_window_argmin_motifs():
    return _strongest_case(transfer.four), _strongest_case(transfer.five)


def main() -> None:
    for result in analyze_safe_window_argmin_motifs():
        print(result)


if __name__ == "__main__":
    main()
