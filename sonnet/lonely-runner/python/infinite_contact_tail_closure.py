"""Phase 10C: finite certificate for the infinite contact-event tail.

For the certified center-4 persistent state, center 5 is the first contact layer
not represented explicitly.  For each runner the earliest event in the entire
future tail n >= 5 is the center-5 enter event, with coefficient 5-delta.
Because all speeds are positive, every later enter/exit event for that runner has
strictly larger time.

Therefore it is enough to certify, on every retained exact closure atom, that
all four center-5 enter events occur strictly after the current first-witness
boundary.  This finite check implies that no event from any center n >= 5 can
change the first-witness task.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import center5_pressure as c5
import local_contact_refinement as lcr
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


@dataclass(frozen=True)
class InfiniteTailClosure:
    cells: int
    tasks: int
    atoms: int
    runners: int
    anchor_center: int
    anchor_kind: str
    anchor_alpha: Fraction
    strict_anchor_comparisons: int
    earlier_equal_anchor_comparisons: int
    unresolved_anchor_comparisons: int


def future_alpha_offset(center: int, kind: str) -> Fraction:
    """Exact alpha(center,kind) - alpha(5,enter) for center >= 5."""

    assert center >= 5
    assert kind in ("enter", "exit")
    if kind == "enter":
        return Fraction(center - 5)
    return Fraction(center - 5) + 2 * pd.DELTA


def analyze_infinite_contact_tail_closure() -> InfiniteTailClosure:
    _old, _generated, cells = c5.build_center4_persistent_cells()
    anchor_center = 5
    anchor_kind = "enter"
    anchor_alpha = lcr.alpha((0, anchor_center, anchor_kind))
    assert anchor_alpha == Fraction(5) - pd.DELTA

    strict = 0
    earlier_equal = 0
    unresolved = 0

    for cell in cells:
        witness = cell.task[1][0]
        for atom in cell.atoms:
            for runner in range(pd.K):
                event = (runner, anchor_center, anchor_kind)
                relation = pcc._event_relation(atom, event, witness)
                if relation is None:
                    unresolved += 1
                elif relation <= 0:
                    earlier_equal += 1
                else:
                    strict += 1

    atoms = sum(len(cell.atoms) for cell in cells)
    assert strict + earlier_equal + unresolved == atoms * pd.K

    # Symbolic tail step: for every allowed future event center>=5, its contact
    # coefficient is anchor_alpha plus a manifestly nonnegative offset.  The
    # function is used here at both event kinds on the boundary center; its
    # formula itself handles arbitrary larger integer centers.
    assert future_alpha_offset(5, "enter") == 0
    assert future_alpha_offset(5, "exit") == 2 * pd.DELTA > 0
    assert future_alpha_offset(6, "enter") == 1 > 0
    assert future_alpha_offset(6, "exit") == 1 + 2 * pd.DELTA > 0

    return InfiniteTailClosure(
        cells=len(cells),
        tasks=len({cell.task for cell in cells}),
        atoms=atoms,
        runners=pd.K,
        anchor_center=anchor_center,
        anchor_kind=anchor_kind,
        anchor_alpha=anchor_alpha,
        strict_anchor_comparisons=strict,
        earlier_equal_anchor_comparisons=earlier_equal,
        unresolved_anchor_comparisons=unresolved,
    )


def main() -> None:
    result = analyze_infinite_contact_tail_closure()
    print("Phase 10C infinite contact-tail closure")
    print(f"  cells / tasks / atoms:             {result.cells} / {result.tasks} / {result.atoms}")
    print(f"  anchor:                            center {result.anchor_center} {result.anchor_kind}, alpha={result.anchor_alpha}")
    print(f"  runners:                           {result.runners}")
    print(f"  strict anchor comparisons:         {result.strict_anchor_comparisons}")
    print(f"  earlier/equal anchor comparisons:  {result.earlier_equal_anchor_comparisons}")
    print(f"  unresolved anchor comparisons:     {result.unresolved_anchor_comparisons}")
    assert result.strict_anchor_comparisons == result.atoms * result.runners
    assert result.earlier_equal_anchor_comparisons == 0
    assert result.unresolved_anchor_comparisons == 0


if __name__ == "__main__":
    main()
