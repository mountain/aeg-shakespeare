"""Phase 9B: exact local center-4 semantic red team for the nine pressure cells.

The Phase-9A detector marks only nine of the 2,753 center-3 persistent cells for
reopening.  This script does not build a full center-4 wall arrangement.  For
each exact closure atom under those nine cells it advances the contact process
event by event.  Whenever the next-event order is not decided, it branches only
on that single process-generated collision wall.  As soon as the first-witness
task is decided, refinement stops.

The result is therefore an exact local semantic oracle driven by event-order
necessity rather than a Cartesian product of all center-4 wall strata.  It is
used only to red-team the Phase-9A pressure roles and to expose the wall language
needed by the next completion search.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

import controlled_interleaving as ci
import local_contact_refinement as lcr
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


Task = tuple[object, ...]
Event = tuple[int, int, str]


@dataclass(frozen=True)
class SemanticExpansion:
    tasks: frozenset[Task]
    leaf_count: int
    queried_walls: frozenset[lcr.ResidualCoordinate]


@dataclass(frozen=True)
class Center4SemanticCase:
    signature: tuple[int, ...]
    phase9a_role: str
    old_task: Task
    new_tasks: tuple[Task, ...]
    atom_count: int
    semantic_leaf_count: int
    queried_walls: tuple[lcr.ResidualCoordinate, ...]
    new_center4_walls: tuple[lcr.ResidualCoordinate, ...]
    latent_older_walls: tuple[lcr.ResidualCoordinate, ...]

    @property
    def task_count(self) -> int:
        return len(self.new_tasks)

    @property
    def same_boundary_and_mode(self) -> bool:
        return self.task_count == 1 and (
            self.old_task[1:] == self.new_tasks[0][1:]
        )


@dataclass(frozen=True)
class Center4SemanticRedTeam:
    cases: tuple[Center4SemanticCase, ...]

    @property
    def branching_cases(self) -> tuple[Center4SemanticCase, ...]:
        return tuple(case for case in self.cases if case.task_count > 1)

    @property
    def uniform_cases(self) -> tuple[Center4SemanticCase, ...]:
        return tuple(case for case in self.cases if case.task_count == 1)


def _events(max_center: int) -> tuple[Event, ...]:
    return tuple(
        (runner, center, kind)
        for runner in range(pd.K)
        for center in range(max_center + 1)
        for kind in (("exit",) if center == 0 else ("enter", "exit"))
    )


def _event_relation(closure: pcc.Closure, left: Event, right: Event) -> int | None:
    """Closure-decided sign(t_left-t_right), including domain-trivial ratios."""

    i = left[0]
    j = right[0]
    a = lcr.alpha(left)
    b = lcr.alpha(right)
    if i == j:
        return -1 if a < b else (1 if a > b else 0)

    if i < j:
        threshold = b / a
        if threshold <= 1:
            return 1
        if threshold >= pd.RMAX:
            return -1
        return pcc._relation_from_closure(closure, (i, j), threshold)

    threshold = a / b
    if threshold <= 1:
        return -1
    if threshold >= pd.RMAX:
        return 1
    relation = pcc._relation_from_closure(closure, (j, i), threshold)
    return None if relation is None else -relation


def _collision_coordinate(left: Event, right: Event) -> lcr.ResidualCoordinate:
    wall = lcr.collision_wall(left, right)
    if wall is None:
        raise AssertionError(f"unresolved comparison has no admissible wall: {left}, {right}")
    return lcr.ResidualCoordinate(pair=(wall[0], wall[1]), ratio=wall[2])


def _merge(expansions) -> SemanticExpansion:
    tasks = set()
    leaves = 0
    walls = set()
    for expansion in expansions:
        tasks.update(expansion.tasks)
        leaves += expansion.leaf_count
        walls.update(expansion.queried_walls)
    return SemanticExpansion(
        tasks=frozenset(tasks),
        leaf_count=leaves,
        queried_walls=frozenset(walls),
    )


def expand_first_witness(
    closure: pcc.Closure,
    *,
    max_center: int,
) -> SemanticExpansion:
    """Enumerate only event-order branches required to decide first witness."""

    initial_events = _events(max_center)

    @lru_cache(maxsize=None)
    def solve(
        current: pcc.Closure,
        remaining: tuple[Event, ...],
        bad_tuple: tuple[int, ...],
        event_index: int,
    ) -> SemanticExpansion:
        assert remaining
        bad = set(bad_tuple)

        candidate = remaining[0]
        for event in remaining[1:]:
            relation = _event_relation(current, event, candidate)
            if relation is None:
                wall = _collision_coordinate(event, candidate)
                branches = []
                for sign in (-1, 0, 1):
                    next_closure = pd.add_edges(
                        current,
                        ci._sign_edges(wall, sign),
                    )
                    if next_closure is None:
                        continue
                    branches.append(
                        solve(next_closure, remaining, bad_tuple, event_index)
                    )
                assert branches
                merged = _merge(branches)
                return SemanticExpansion(
                    tasks=merged.tasks,
                    leaf_count=merged.leaf_count,
                    queried_walls=merged.queried_walls | {wall},
                )
            if relation < 0:
                candidate = event

        group = []
        for event in remaining:
            relation = _event_relation(current, event, candidate)
            if relation is None:
                wall = _collision_coordinate(event, candidate)
                branches = []
                for sign in (-1, 0, 1):
                    next_closure = pd.add_edges(
                        current,
                        ci._sign_edges(wall, sign),
                    )
                    if next_closure is None:
                        continue
                    branches.append(
                        solve(next_closure, remaining, bad_tuple, event_index)
                    )
                assert branches
                merged = _merge(branches)
                return SemanticExpansion(
                    tasks=merged.tasks,
                    leaf_count=merged.leaf_count,
                    queried_walls=merged.queried_walls | {wall},
                )
            if relation == 0:
                group.append(event)

        assert group
        next_index = event_index + 1
        boundary_runners = {runner for runner, _center, _kind in group}
        bad_on = tuple(sorted(bad - boundary_runners))
        after = set(bad)
        for runner, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            else:
                after.add(runner)
        boundary = tuple(sorted(group))

        if not bad_on:
            mode = "interval" if not after else "point"
            task: Task = (next_index, boundary, mode)
            return SemanticExpansion(
                tasks=frozenset((task,)),
                leaf_count=1,
                queried_walls=frozenset(),
            )

        group_set = set(group)
        next_remaining = tuple(event for event in remaining if event not in group_set)
        return solve(
            current,
            next_remaining,
            tuple(sorted(after)),
            next_index,
        )

    return solve(
        closure,
        initial_events,
        tuple(range(pd.K)),
        0,
    )


def analyze_center4_semantic_redteam() -> Center4SemanticRedTeam:
    cells, pressure = pcc.probe_center3_to_center4_pressure()
    by_signature = {cell.signature: cell for cell in cells}
    assert len(by_signature) == 2_753

    new_ratio_set = set(pd.contact_ratios(4)) - set(pd.contact_ratios(3))
    cases = []
    for signature in sorted(pressure.affected):
        cell = by_signature[signature]
        tasks = set()
        walls = set()
        leaf_count = 0
        for atom in cell.atoms:
            expansion = expand_first_witness(atom, max_center=4)
            tasks.update(expansion.tasks)
            walls.update(expansion.queried_walls)
            leaf_count += expansion.leaf_count

        role = (
            "nonbranching-pressure"
            if signature in pressure.nonbranching_pressure
            else "completion-pressure"
        )
        new_walls = tuple(
            sorted(
                (wall for wall in walls if wall.ratio in new_ratio_set),
                key=lambda item: (item.pair, item.ratio),
            )
        )
        latent = tuple(
            sorted(
                (wall for wall in walls if wall.ratio not in new_ratio_set),
                key=lambda item: (item.pair, item.ratio),
            )
        )
        cases.append(
            Center4SemanticCase(
                signature=signature,
                phase9a_role=role,
                old_task=cell.task,
                new_tasks=tuple(sorted(tasks, key=repr)),
                atom_count=len(cell.atoms),
                semantic_leaf_count=leaf_count,
                queried_walls=tuple(
                    sorted(walls, key=lambda item: (item.pair, item.ratio))
                ),
                new_center4_walls=new_walls,
                latent_older_walls=latent,
            )
        )

    result = Center4SemanticRedTeam(cases=tuple(cases))
    assert len(result.cases) == 9
    return result


def main() -> None:
    result = analyze_center4_semantic_redteam()
    print("Phase 9B center4 local semantic red team")
    print(f"  cases:       {len(result.cases)}")
    print(f"  uniform:     {len(result.uniform_cases)}")
    print(f"  branching:   {len(result.branching_cases)}")
    for case in result.cases:
        print(f"  {case.phase9a_role}: {case.signature}")
        print(f"    old task:             {case.old_task}")
        print(f"    new task count:       {case.task_count}")
        print(f"    same boundary/mode:   {case.same_boundary_and_mode}")
        print(f"    closure atoms:        {case.atom_count}")
        print(f"    semantic leaves:      {case.semantic_leaf_count}")
        print(f"    queried walls:        {len(case.queried_walls)}")
        print(f"    new center4 walls:    {len(case.new_center4_walls)}")
        print(f"    latent older walls:   {len(case.latent_older_walls)}")
        if case.task_count <= 8:
            for task in case.new_tasks:
                print(f"      task: {task}")
        if case.new_center4_walls:
            print("    new walls:")
            for wall in case.new_center4_walls:
                print(
                    f"      u{wall.pair[1]+1}/u{wall.pair[0]+1} ? {wall.ratio}"
                )
        if case.latent_older_walls:
            print("    latent walls:")
            for wall in case.latent_older_walls:
                print(
                    f"      u{wall.pair[1]+1}/u{wall.pair[0]+1} ? {wall.ratio}"
                )


if __name__ == "__main__":
    main()
