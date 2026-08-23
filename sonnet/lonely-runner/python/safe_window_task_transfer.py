"""Phase 14: change the observer task without changing canonical dynamics.

Phases 11--13 study the first lonely witness.  This calibration keeps exactly the
same canonical contact process but asks a slightly richer, still natural task:

    first canonical witness
    + if it opens a safe interval, which runner(s) first re-enter the bad set?

The second component is the *safe-window closer*.  It is determined by the next
contact group after an interval witness.  A first-witness terminal region may or
may not already decide that next group.  If one old terminal region admits
several different closers, the old representation is not sufficient for the
richer task and must be refined/continued.

The experiment is deliberately research-local.  It replays the same mechanism
at K=4 and K=5 and introduces no public API.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

import canonical_lazy_contact_compiler as four
import five_speed_dimension_transfer as five


@dataclass(frozen=True)
class WitnessFrontier:
    closure: Any
    legacy_task: tuple[object, ...]
    next_events: tuple[Any, ...]
    bad_after: frozenset[int]


@dataclass(frozen=True)
class ExtendedRegion:
    closure: Any
    task: tuple[object, ...]
    parent_index: int


@dataclass(frozen=True)
class TaskTransferSummary:
    runners: int
    delta: Fraction
    rmax: Fraction
    symbolic_states: int
    first_witness_regions: int
    first_witness_tasks: int
    point_parents: int
    interval_parents: int
    split_parents: int
    split_parent_fraction: Fraction
    max_closer_alternatives: int
    closer_alternative_histogram: tuple[tuple[int, int], ...]
    extended_regions: int
    extended_tasks: int
    old_generated_coordinates: int
    new_next_event_coordinates: int
    genuinely_new_coordinates: int
    example_split_parent: tuple[object, ...] | None
    example_closers: tuple[tuple[int, ...], ...]


def _canonical_task(task):
    _event_index, boundary, mode = task
    return (
        tuple(sorted((runner, kind) for runner, _center, kind in boundary)),
        mode,
    )


def _compile_frontiers(module):
    initial_events = tuple(
        module.NextContact(module.DELTA, 0, "exit")
        for _ in range(module.K)
    )
    stack = [
        (
            module._initial_closure(),
            initial_events,
            frozenset(range(module.K)),
            0,
        )
    ]
    seen = set()
    frontiers: list[WitnessFrontier] = []
    generated = set()

    while stack:
        closure, events, bad, event_index = stack.pop()
        state_key = (closure, events, bad, event_index)
        if state_key in seen:
            continue
        seen.add(state_key)

        for first, second in module.PAIRS:
            threshold = events[second].alpha / events[first].alpha
            if module._relation(closure, (first, second), threshold) is None:
                generated.add((first, second, threshold))

        for group, child_closure in module._minimum_groups(closure, events):
            child_index = event_index + 1
            group_set = set(group)
            bad_on = set(bad) - group_set
            bad_after = set(bad)
            child_events = list(events)
            boundary = []

            for runner in group:
                event = events[runner]
                boundary.append((runner, event.center, event.kind))
                if event.kind == "exit":
                    bad_after.discard(runner)
                else:
                    bad_after.add(runner)
                child_events[runner] = module._advance(event)

            if not bad_on:
                legacy_task = (
                    child_index,
                    tuple(sorted(boundary)),
                    "interval" if not bad_after else "point",
                )
                frontiers.append(
                    WitnessFrontier(
                        closure=child_closure,
                        legacy_task=legacy_task,
                        next_events=tuple(child_events),
                        bad_after=frozenset(bad_after),
                    )
                )
            else:
                stack.append(
                    (
                        child_closure,
                        tuple(child_events),
                        frozenset(bad_after),
                        child_index,
                    )
                )

    return tuple(frontiers), tuple(sorted(generated)), len(seen)


def _extend_safe_window(module, frontiers):
    extended: list[ExtendedRegion] = []
    new_coordinates = set()
    alternatives_by_parent: dict[int, set[tuple[int, ...] | None]] = defaultdict(set)

    for parent_index, frontier in enumerate(frontiers):
        witness = _canonical_task(frontier.legacy_task)
        _boundary, mode = witness

        if mode == "point":
            task = (witness, None)
            extended.append(ExtendedRegion(frontier.closure, task, parent_index))
            alternatives_by_parent[parent_index].add(None)
            continue

        assert not frontier.bad_after

        for first, second in module.PAIRS:
            threshold = (
                frontier.next_events[second].alpha
                / frontier.next_events[first].alpha
            )
            if module._relation(
                frontier.closure,
                (first, second),
                threshold,
            ) is None:
                new_coordinates.add((first, second, threshold))

        branches = module._minimum_groups(
            frontier.closure,
            frontier.next_events,
        )
        assert branches
        for group, child_closure in branches:
            # Once the first witness opens an interval, all runners are in the
            # safe interior.  The first event that can close that interval is an
            # enter contact, possibly simultaneous on several runners.
            assert all(
                frontier.next_events[runner].kind == "enter"
                for runner in group
            )
            closer = tuple(group)
            task = (witness, closer)
            extended.append(ExtendedRegion(child_closure, task, parent_index))
            alternatives_by_parent[parent_index].add(closer)

    return (
        tuple(extended),
        tuple(sorted(new_coordinates)),
        alternatives_by_parent,
    )


def _summarize(module) -> TaskTransferSummary:
    frontiers, old_coordinates, symbolic_states = _compile_frontiers(module)
    extended, next_coordinates, alternatives = _extend_safe_window(
        module,
        frontiers,
    )

    first_tasks = {_canonical_task(frontier.legacy_task) for frontier in frontiers}
    point_parents = sum(
        _canonical_task(frontier.legacy_task)[1] == "point"
        for frontier in frontiers
    )
    interval_parents = len(frontiers) - point_parents

    split = {
        parent: values
        for parent, values in alternatives.items()
        if len(values) > 1
    }
    histogram = Counter(len(values) for values in alternatives.values())
    old_set = set(old_coordinates)
    new_set = set(next_coordinates)

    example_parent = None
    example_closers: tuple[tuple[int, ...], ...] = ()
    if split:
        # Prefer the strongest multiway example, then stable parent index.
        parent = max(split, key=lambda item: (len(split[item]), -item))
        example_parent = _canonical_task(frontiers[parent].legacy_task)
        example_closers = tuple(
            sorted(value for value in split[parent] if value is not None)
        )

    return TaskTransferSummary(
        runners=module.K,
        delta=module.DELTA,
        rmax=module.RMAX,
        symbolic_states=symbolic_states,
        first_witness_regions=len(frontiers),
        first_witness_tasks=len(first_tasks),
        point_parents=point_parents,
        interval_parents=interval_parents,
        split_parents=len(split),
        split_parent_fraction=Fraction(len(split), len(frontiers)),
        max_closer_alternatives=max(len(values) for values in alternatives.values()),
        closer_alternative_histogram=tuple(sorted(histogram.items())),
        extended_regions=len(extended),
        extended_tasks=len({region.task for region in extended}),
        old_generated_coordinates=len(old_coordinates),
        new_next_event_coordinates=len(next_coordinates),
        genuinely_new_coordinates=len(new_set - old_set),
        example_split_parent=example_parent,
        example_closers=example_closers,
    )


def analyze_safe_window_task_transfer():
    """Return independent K=4 and K=5 task-change calibrations."""

    return _summarize(four), _summarize(five)


def main() -> None:
    for result in analyze_safe_window_task_transfer():
        print(f"K={result.runners}, delta={result.delta}, rmax={result.rmax}")
        print(
            "  process states / first regions / first tasks: "
            f"{result.symbolic_states} / {result.first_witness_regions} / "
            f"{result.first_witness_tasks}"
        )
        print(
            "  point / interval / split parents: "
            f"{result.point_parents} / {result.interval_parents} / "
            f"{result.split_parents}"
        )
        print(
            "  max closer alternatives / histogram: "
            f"{result.max_closer_alternatives} / "
            f"{result.closer_alternative_histogram}"
        )
        print(
            "  extended regions / tasks: "
            f"{result.extended_regions} / {result.extended_tasks}"
        )
        print(
            "  old / next / genuinely-new coordinates: "
            f"{result.old_generated_coordinates} / "
            f"{result.new_next_event_coordinates} / "
            f"{result.genuinely_new_coordinates}"
        )
        print("  example parent:", result.example_split_parent)
        print("  example closers:", result.example_closers)


if __name__ == "__main__":
    main()
