"""Phase 10B: exact semantic no-op certificate for the center-5 contact layer.

Phase 10A's frozen next-layer detector marks every one of the 3,067 center-4
persistent cells stable.  This script red-teams that zero-pressure result without
constructing a center-5 wall arrangement.

For every retained exact closure atom, compare every newly admitted center-5
enter/exit event directly with the current certified first-witness boundary.  If
every comparison is strictly later, the existing first witness is unchanged
regardless of the ordering among later events.  Any equality, earlier event, or
unresolved comparison is reported as a counterexample/risk rather than silently
resolved by a hidden oracle.
"""

from __future__ import annotations

from dataclasses import dataclass

import center5_pressure as c5
import persistent_constraint_cells as pcc
import pair_difference_refinement as pd


@dataclass(frozen=True)
class Center5NoopCertificate:
    cells: int
    tasks: int
    atoms: int
    new_events_per_atom: int
    strict_later_comparisons: int
    earlier_or_equal_comparisons: int
    unresolved_comparisons: int
    affected_cells: int
    unresolved_cells: int


def analyze_center5_semantic_noop() -> Center5NoopCertificate:
    _old, _generated, cells = c5.build_center4_persistent_cells()
    new_events = tuple(
        (runner, 5, kind)
        for runner in range(pd.K)
        for kind in ("enter", "exit")
    )
    assert len(new_events) == 8

    later = 0
    earlier_equal = 0
    unresolved = 0
    affected_cells = set()
    unresolved_cells = set()

    for cell in cells:
        # A task boundary may contain multiple simultaneous events; any one has
        # the same event time.  Use the first canonical boundary event.
        witness = cell.task[1][0]
        for atom in cell.atoms:
            for event in new_events:
                relation = pcc._event_relation(atom, event, witness)
                if relation is None:
                    unresolved += 1
                    unresolved_cells.add(cell.signature)
                elif relation <= 0:
                    earlier_equal += 1
                    affected_cells.add(cell.signature)
                else:
                    later += 1

    atoms = sum(len(cell.atoms) for cell in cells)
    total = atoms * len(new_events)
    assert later + earlier_equal + unresolved == total

    return Center5NoopCertificate(
        cells=len(cells),
        tasks=len({cell.task for cell in cells}),
        atoms=atoms,
        new_events_per_atom=len(new_events),
        strict_later_comparisons=later,
        earlier_or_equal_comparisons=earlier_equal,
        unresolved_comparisons=unresolved,
        affected_cells=len(affected_cells),
        unresolved_cells=len(unresolved_cells),
    )


def main() -> None:
    result = analyze_center5_semantic_noop()
    print("Phase 10B exact center5 semantic no-op certificate")
    print(f"  cells / tasks / atoms:             {result.cells} / {result.tasks} / {result.atoms}")
    print(f"  new events per atom:               {result.new_events_per_atom}")
    print(f"  strict-later comparisons:          {result.strict_later_comparisons}")
    print(f"  earlier-or-equal comparisons:      {result.earlier_or_equal_comparisons}")
    print(f"  unresolved comparisons:            {result.unresolved_comparisons}")
    print(f"  affected cells:                    {result.affected_cells}")
    print(f"  unresolved cells:                  {result.unresolved_cells}")
    assert result.earlier_or_equal_comparisons == 0
    assert result.unresolved_comparisons == 0


if __name__ == "__main__":
    main()
