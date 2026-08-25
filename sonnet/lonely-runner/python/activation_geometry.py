"""Phase 8E.0: activation geometry of the seven frozen completion walls.

A new wall can always be evaluated from primitive speed ratios, but querying it
very early may split many old persistent contexts that do not need the
distinction.  This script measures a stricter notion relative to the frozen
center-2 persistent Huffman tree.

At an old-tree node, a new wall has a *clean activation* when:

1. at least one completion parent below the node actually uses that wall in its
   frozen Phase-8C minimum support; and
2. every other surviving old parent that does not use the wall has its wall sign
   already fixed by exact center-2 constraints.

Thus an early query can branch only contexts for which the wall is a declared
completion primitive.  A *shared clean activation* additionally has at least two
completion parents using the same wall below the node.

The sign possibilities are certified from center-2 multiplicative difference
constraints one wall at a time; no full center-3 arrangement or child task census
is needed.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import controlled_interleaving as ci
import local_contact_refinement as lcr
import pair_difference_refinement as pd
import persistent_dag_increment as pdi


@dataclass(frozen=True)
class WallActivation:
    coordinate: lcr.ResidualCoordinate
    completion_user_count: int
    root_unresolved_nonusers: int
    earliest_clean_depth: int | None
    earliest_clean_parent_count: int | None
    earliest_clean_user_count: int | None
    earliest_shared_clean_depth: int | None
    minimum_collateral_nonusers: int
    minimum_collateral_depth: int


@dataclass(frozen=True)
class ActivationGeometry:
    walls: tuple[WallActivation, ...]


def analyze_activation_geometry() -> ActivationGeometry:
    base = lcr.analyze_center2_to_center3()
    old = pdi._center2_persistent_tree(base)

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
    assert len(relevant2) == 21

    systems_by_parent = defaultdict(list)
    for system, signature in zip(systems2, full_signatures2):
        parent = tuple(signature[index] for index in relevant2)
        systems_by_parent[parent].append(system)
    parents = tuple(systems_by_parent)
    assert len(parents) == 849

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

    users = {
        wall: {
            case.parent
            for case in base.completion_residual_cases
            if wall in case.coordinates
        }
        for wall in new_walls
    }

    # Exact one-wall feasibility for every old persistent parent.
    signs_by_parent = {
        wall: {parent: set() for parent in parents}
        for wall in new_walls
    }
    for parent, systems in systems_by_parent.items():
        for system in systems:
            for wall in new_walls:
                for signature in ci._feasible_new_signatures(system, strata2, (wall,)):
                    signs_by_parent[wall][parent].add(signature[0])
    assert all(
        signs_by_parent[wall][parent]
        for wall in new_walls
        for parent in parents
    )

    records = {}
    for wall in new_walls:
        nonusers = set(parents) - users[wall]
        root_collateral = sum(
            len(signs_by_parent[wall][parent]) > 1
            for parent in nonusers
        )
        records[wall] = {
            "root_collateral": root_collateral,
            "clean": [],
            "shared": [],
            "minimum": None,
        }

    def visit(node, live_parents, depth):
        live_set = set(live_parents)
        for wall in new_walls:
            active_users = live_set & users[wall]
            if not active_users:
                continue
            possible = set().union(
                *(signs_by_parent[wall][parent] for parent in live_set)
            )
            if len(possible) <= 1:
                continue
            collateral = sum(
                parent not in users[wall]
                and len(signs_by_parent[wall][parent]) > 1
                for parent in live_set
            )
            data = records[wall]
            candidate = (collateral, depth, len(live_set), len(active_users))
            if data["minimum"] is None or candidate < data["minimum"]:
                data["minimum"] = candidate
            if collateral == 0:
                data["clean"].append((depth, len(live_set), len(active_users)))
                if len(active_users) >= 2:
                    data["shared"].append((depth, len(live_set), len(active_users)))

        if node.predicate is None:
            return
        grouped = defaultdict(list)
        for parent in live_parents:
            grouped[parent[node.predicate]].append(parent)
        for sign, child in node.children:
            visit(child, tuple(grouped[sign]), depth + 1)

    visit(old["tree"], parents, 0)

    results = []
    for wall in new_walls:
        data = records[wall]
        clean = min(data["clean"]) if data["clean"] else None
        shared = min(data["shared"]) if data["shared"] else None
        minimum = data["minimum"]
        assert minimum is not None
        results.append(
            WallActivation(
                coordinate=wall,
                completion_user_count=len(users[wall]),
                root_unresolved_nonusers=data["root_collateral"],
                earliest_clean_depth=None if clean is None else clean[0],
                earliest_clean_parent_count=None if clean is None else clean[1],
                earliest_clean_user_count=None if clean is None else clean[2],
                earliest_shared_clean_depth=None if shared is None else shared[0],
                minimum_collateral_nonusers=minimum[0],
                minimum_collateral_depth=minimum[1],
            )
        )

    return ActivationGeometry(walls=tuple(results))


def main() -> None:
    result = analyze_activation_geometry()
    print("Phase 8E.0 clean activation geometry")
    for record in result.walls:
        c = record.coordinate
        print(f"  u{c.pair[1]+1}/u{c.pair[0]+1} ? {c.ratio}")
        print(f"    completion users:          {record.completion_user_count}")
        print(f"    root unresolved nonusers:  {record.root_unresolved_nonusers}")
        print(f"    earliest clean depth:      {record.earliest_clean_depth}")
        print(f"    clean live parents/users:  {record.earliest_clean_parent_count} / {record.earliest_clean_user_count}")
        print(f"    earliest shared clean:     {record.earliest_shared_clean_depth}")
        print(f"    minimum collateral:        {record.minimum_collateral_nonusers} @ depth {record.minimum_collateral_depth}")


if __name__ == "__main__":
    main()
