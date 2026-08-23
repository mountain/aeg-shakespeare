"""Sonnet 001 Phase 8E.0: clean activation geometry of new completion walls.

Question
--------
Phase 8D.2 showed that reweighting only the old center-2 prefix cannot recover
the fresh center-3 placement target.  Before allowing new completion walls to
interleave with old wall queries, when can each new wall be activated without
splitting any old persistent context that does not itself use that wall as a
completion primitive?

Primitive data
--------------
The program receives:

- the frozen center-2 68-label persistent Hauffman tree;
- the 849 exact center-2 persistent parents and their underlying realizable sign
  systems;
- the seven new center-3 wall coordinates already frozen by Phase 8C;
- the six completion-parent -> raw-wall-support incidences.

It does not receive the full 72,241-state center-3 arrangement, center-3 task
labels for stable parents, a fresh center-3 tree, deeper contact layers, or
`K=13` data.

Classical lineage
-----------------
Huffman's classical setting concerns decision depth for a fixed symbol
alphabet/distribution [Huffman-1952].  The Lonely Runner computational setting is
documented in [Sungkawichai-Trakulthongchai-2026].  The activation notion below
is a **Shakespeare interpretation** of when a newly generated process distinction
can enter an existing history representation without collateral branching.

Shakespeare reconstruction
---------------------------
For one frozen new wall and one old parent, exact multiplicative difference
constraints determine which wall signs remain feasible inside that parent.

At an old-tree node, call the new wall *cleanly activatable* when:

1. at least one surviving completion parent uses the wall; and
2. every surviving parent that does not use the wall already has a fixed sign on
   that wall.

Thus querying the wall there cannot branch an unrelated old context.  A
*shared-clean* activation additionally requires at least two surviving
completion parents that use the wall.

The exact center-2 tree is traversed to find the earliest clean and shared-clean
depths.  No next-layer task semantics are used to choose those depths.

Calibration statement
---------------------
Passing this bounded test certifies that:

1. all seven frozen new walls have a clean activation somewhere in the old tree;
2. their sorted earliest clean depths are exactly `3,3,5,7,8,9,9`;
3. neither of the two walls used by four completion parents has a shared-clean
   activation: at its earliest clean depth only one actual completion user
   remains below the node;
4. no frozen new wall has any shared-clean activation in the old tree;
5. the root contains substantial collateral ambiguity for every new wall (from
   77 to 160 unresolved non-user parents); and
6. all sign possibilities are certified from center-2 constraints only.

Proof map
---------
1. ``test_frozen_new_walls_have_clean_but_no_shared_clean_activation`` rebuilds
   the exact old persistent tree and per-parent one-wall feasible signs, checks
   the seven exact activation records, and verifies the absence of any
   shared-clean activation.

Boundary
--------
Clean activation is deliberately stricter than semantic admissibility.  A stable
old parent may be split by a new wall and later reconverge to the same task; this
test classifies that as collateral rather than forbidden mathematics.  Therefore
absence of shared-clean activation does not prove that cross-parent interleaving
is impossible.  It only proves that such sharing cannot be obtained by inserting
a new query at a zero-collateral node of the **frozen old tree**.

The implementation currently recomputes many one-wall difference-constraint
closures and is a research certificate rather than an optimized runtime path.

References
----------
[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_CONTROLLED_INTERLEAVING") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 activation-geometry census",
)


def _load_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "activation_geometry.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location("sonnet_activation_geometry", script_path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_frozen_new_walls_have_clean_but_no_shared_clean_activation():
    activation = _load_module()
    result = activation.analyze_activation_geometry()
    assert len(result.walls) == 7

    assert sorted(record.earliest_clean_depth for record in result.walls) == [
        3, 3, 5, 7, 8, 9, 9
    ]
    assert all(record.earliest_shared_clean_depth is None for record in result.walls)
    assert min(record.root_unresolved_nonusers for record in result.walls) == 77
    assert max(record.root_unresolved_nonusers for record in result.walls) == 160

    four_user = [record for record in result.walls if record.completion_user_count == 4]
    assert len(four_user) == 2
    assert all(record.earliest_clean_depth == 3 for record in four_user)
    assert all(record.earliest_clean_parent_count == 19 for record in four_user)
    assert all(record.earliest_clean_user_count == 1 for record in four_user)
