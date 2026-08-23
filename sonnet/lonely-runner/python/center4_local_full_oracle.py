"""Independent local full-stratum oracle for Phase 9B/9C consistency.

For only the nine Phase-9A pressure cells, extend every retained exact closure
atom to all center-4 pair strata over the complete contact-ratio alphabet.  This
is a local full refinement, not the lazy event-order branching used by Phase 9B
and not the minimum-support search used by Phase 9C.

The resulting exact center-4 systems are deduplicated and evaluated by the older
`pair_difference_refinement.first_witness` implementation.  The script compares
those task sets with Phase 9B and separately tests whether the single wall
u4/u3 ? 19/11 determines each branching cell's task.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

import center4_semantic_redteam as semantic
import pair_difference_refinement as pd
import persistent_constraint_cells as pcc


def extend_atom_to_center4(atom, strata4):
    systems = []
    choices = {}

    def visit(depth, closure):
        if depth == len(pd.DFS_PAIRS):
            systems.append(tuple(choices[pair] for pair in pd.PAIRS))
            return
        pair = pd.DFS_PAIRS[depth]
        for index, item in enumerate(strata4):
            next_closure = pd.add_edges(closure, pd.stratum_edges(pair, item))
            if next_closure is None:
                continue
            choices[pair] = index
            visit(depth + 1, next_closure)
            del choices[pair]

    visit(0, atom)
    return tuple(systems)


def analyze_local_full_oracle():
    cells, pressure = pcc.probe_center3_to_center4_pressure()
    by_signature = {cell.signature: cell for cell in cells}
    lazy = semantic.analyze_center4_semantic_redteam()
    lazy_by_signature = {case.signature: case for case in lazy.cases}

    ratios4 = pd.contact_ratios(4)
    strata4 = pd.strata(ratios4)
    target_ratio = Fraction(19, 11)
    target_pair = (2, 3)

    results = []
    for signature in sorted(pressure.affected):
        cell = by_signature[signature]
        systems = set()
        for atom in cell.atoms:
            systems.update(extend_atom_to_center4(atom, strata4))
        tasks = {}
        by_sign = defaultdict(set)
        for system in systems:
            task = pd.first_witness(system, 4, ratios4, strata4)[0]
            tasks[system] = task
            sign = pd.ratio_relation(system, target_pair, target_ratio, ratios4, strata4)
            by_sign[sign].add(task)

        direct_tasks = frozenset(tasks.values())
        lazy_tasks = frozenset(lazy_by_signature[signature].new_tasks)
        results.append((
            signature,
            len(cell.atoms),
            len(systems),
            tuple(sorted(direct_tasks, key=repr)),
            tuple(sorted(lazy_tasks, key=repr)),
            tuple(sorted((sign, tuple(sorted(values, key=repr))) for sign, values in by_sign.items())),
        ))

    return tuple(results)


def main() -> None:
    results = analyze_local_full_oracle()
    print("Phase 9 local full-stratum oracle")
    print("  pressure cells:", len(results))
    for signature, atoms, systems, direct, lazy, sign_map in results:
        print("  cell:", signature)
        print("    atoms / center4 systems:", atoms, "/", systems)
        print("    direct task count:", len(direct))
        print("    lazy task count:  ", len(lazy))
        print("    lazy == direct:   ", direct == lazy)
        print("    19/11 sign map:   ", [(s, len(ts)) for s, ts in sign_map])
        for task in direct:
            print("      direct task:", task)
    assert all(direct == lazy for _sig, _a, _s, direct, lazy, _m in results)


if __name__ == "__main__":
    main()
