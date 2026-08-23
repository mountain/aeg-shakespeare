"""Sonnet 001 Phase 9D: materialize the center-4 persistent representation.

Question
--------
After Phase 9C discovers one common task-minimal center-4 completion predicate,
can the Phase-8E persistent representation absorb the entire center-4 semantic
update without reconstructing a full center-4 wall arrangement or changing the
current-use history objective?

Primitive data
--------------
The program receives:

- the Phase-8E 2,753 center-3 persistent constraint cells and 28 predicates;
- Phase-9A pressure roles;
- Phase-9B exact local semantics;
- Phase-9C minimum-support search, from which the shared new predicate is
  discovered rather than hard-coded as input;
- the frozen 55-integer-quadruple current-use distribution.

It does not receive a fresh center-4 tree, the global center-4 arrangement,
center-5 data, or `K=13` data.

Classical lineage
-----------------
Huffman's minimum-redundancy coding gives the classical expected-prefix baseline
[Huffman-1952].  The incremental persistent representation and its process-wall
interleaving are **Shakespeare reconstructions**.

Shakespeare reconstruction
---------------------------
Phase 9C first discovers that all seven completion cells share the one ternary
process predicate

    u4/u3 ? 19/11.

Append that predicate globally to the 28-predicate Phase-8E language.  Refine
every retained exact closure atom by its feasible sign, keep stable tasks,
apply the two certified history-reindex updates, and evaluate the seven
completion branches.  The resulting 29-predicate task cells are then given to
the same exact decision-tree optimizer under the unchanged current-use weights.

Calibration statement
---------------------
Passing this bounded persistent-update calibration certifies that:

1. reconstructing the center-3 baseline from the same persistent-cell artifact
   gives exactly `2,753 cells / 75 tasks`, `376 tree nodes / 125 internals /
   200 terminal-merged DAG nodes`, peak 72, worst depth 10, and weighted depth
   total 135;
2. Phase 9C supplies the single new predicate `u4/u3 ? 19/11`;
3. the center-4 representation has exactly 3,067 feasible persistent cells,
   81 task semantics, and 14,967 exact closure/provenance atoms;
4. its exact current-use decision geometry is `391 tree nodes / 130 internals /
   211 terminal-merged DAG nodes`;
5. current weighted depth remains exactly 135 and worst depth remains 10 while
   peak frontier changes from 72 to 75;
6. relative to center 3 the update adds only 5 internal decisions, 11 explicit
   terminal-merged DAG objects, and 6 task semantics; and
7. the new predicate appears at five internal nodes, two of them genuine
   cross-parent placements, with earliest activation depth six.

Proof map
---------
1. ``test_center4_persistent_update_adds_five_decisions_without_current_depth_cost``
   reconstructs the Phase-9D representation and checks all frozen center-3 and
   center-4 structural, history, and placement metrics.

Boundary
--------
This is one four-runner, one-layer scaling calibration.  It does not prove that
future layers always add one predicate, five decisions, or preserve weighted
depth.  The 29-predicate representation is a research artifact rather than a
public persistent-state API.

The terminal-merged DAG count merges equal task terminals but does not search
for arbitrary internal graph minimization.  No new Lonely Runner theorem is
claimed.

References
----------
[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_CENTER4_PERSISTENT_UPDATE") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 center4 persistent-update calibration",
)


def _load_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "center4_persistent_update.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_center4_persistent_update",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_center4_persistent_update_adds_five_decisions_without_current_depth_cost():
    update = _load_module()
    result = update.analyze_center4_persistent_update()

    assert result.center3_cells == 2_753
    assert result.center3_tasks == 75
    assert (
        result.center3_tree_nodes,
        result.center3_internal_nodes,
        result.center3_dag_nodes,
    ) == (376, 125, 200)
    assert (
        result.center3_peak,
        result.center3_worst,
        result.center3_weighted_depth,
    ) == (72, 10, 135)

    coordinate = result.completion_coordinate
    assert coordinate.pair == (2, 3)
    assert coordinate.ratio == Fraction(19, 11)

    assert result.center4_cells == 3_067
    assert result.center4_tasks == 81
    assert result.center4_closure_atoms == 14_967
    assert result.center4_provenance_atoms == 14_967
    assert (
        result.center4_tree_nodes,
        result.center4_internal_nodes,
        result.center4_dag_nodes,
    ) == (391, 130, 211)
    assert (
        result.center4_peak,
        result.center4_worst,
        result.center4_weighted_depth,
    ) == (75, 10, 135)
    assert result.center4_widths == (1, 3, 3, 9, 27, 48, 63, 75, 66, 45, 51)

    assert result.center4_internal_nodes - result.center3_internal_nodes == 5
    assert result.center4_dag_nodes - result.center3_dag_nodes == 11
    assert result.center4_tasks - result.center3_tasks == 6
    assert result.new_wall_internal_nodes == 5
    assert result.cross_parent_new_wall_nodes == 2
    assert result.earliest_new_wall_depth == 6
