"""Sonnet 001 Phase 8D: increment a persistent Hauffman representation locally.

Question
--------
After Phase 8C.2 has objectified all six completion residuals, how much new
representation is actually required to absorb the center-3 contact layer?

Can the frozen center-2 persistent Hauffman tree be reused unchanged, with new
decoder structure attached only below the six genuine completion leaves, rather
than rebuilding a center-3 decision tree from the full 72,241-state geometry?

Primitive data
--------------
The program receives:

- the exact center-2 849-state task quotient and its 68-label one-step persistent
  refinement labels;
- the frozen 55-integer-quadruple usage distribution used by the center-2
  Hauffman calibration;
- the exact Phase-8A/8B split `843 renormalizable / 0 resonant / 6 completion`;
- the six Phase-8C.2 objectified local completion decoders.

It does not receive a newly optimized center-3 tree, the full 72,241 center-3
sign systems, the previously known center-3 tree topology, deeper contact layers,
or `K=13` data.

Classical lineage
-----------------
Huffman's construction optimizes expected prefix length for a fixed finite
symbol distribution [Huffman-1952].  Here the coding object is persistent: an
already-built decision representation is reused while the admissible process
language grows.  The Lonely Runner computational setting is described in
[Sungkawichai-Trakulthongchai-2026].

The incremental persistent-DAG interpretation is a **Shakespeare
interpretation**, not a claim made by either classical source.

Shakespeare reconstruction
---------------------------
First reconstruct the exact center-2 68-label persistent Hauffman tree.  Its
frozen time-first metrics are

    weighted depth = 135 on 55 inputs,
    tree/boundary volume = 328,
    worst depth = 9,
    internal decision nodes = 109.

Then preserve every old decision node.  The 841 identity-stable states and two
history-reindex states require zero new wall queries.  Only the six completion
terminal leaves are replaced by their Phase-8C.2 adaptive decoders.

For history geometry, different decoder paths remain different prefixes.  For
persistent object geometry, terminal nodes carrying the same final first-witness
task are merged.  No cross-parent sharing of internal decoder nodes is assumed,
so the reported DAG is a conservative explicit construction.

The same construction is replayed on the frozen 55-input usage distribution;
for every input, the updated local decoder must reproduce the independent exact
first-witness oracle.

Calibration statement
---------------------
When the opt-in research gate is enabled, passing this file certifies that:

1. the center-2 persistent tree is reconstructed exactly with 68 labels and
   frozen cost `(135, 328, 9, 109)`;
2. the six objectified completion decoders add exactly 16 internal decision
   nodes while all 843 renormalizable states add none;
3. replacing six old terminal leaves by the six decoder trees yields exactly 376
   prefix-tree nodes and 125 internal decision nodes;
4. after terminal semantic merging, the explicit persistent DAG has 200 nodes,
   only 23 more than the 177-node center-2 terminal-merged DAG;
5. the updated representation has exactly 75 final first-witness semantics; and
6. replay on all 55 frozen usage inputs is exact, with every extra wall query
   charged explicitly to a genuine completion path.

Proof map
---------
1. ``test_objectified_completion_decoders_give_sparse_persistent_dag_increment``
   reconstructs the old persistent tree, attaches only the six completion
   decoders, verifies exact node arithmetic and terminal merging, and replays the
   updated representation against the independent exact first-witness oracle on
   all 55 frozen usage inputs.

Boundary
--------
This is one bounded center-depth increment.  The 200-node figure is for a
specific conservative DAG construction that merges equal terminal tasks but does
not search for additional cross-parent internal sharing.  It is therefore an
explicit upper bound/construction, not a proof of globally minimum DAG size.

Likewise, equality of some structural counts with a separately frozen fresh
center-3 tree would not by itself prove graph isomorphism or universal optimality.
The experiment does not establish center-3 -> center-4 sparsity, a public
persistent-DAG API, or a general scalar Hauffman action.

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


RUN_FULL = os.environ.get("AEG_RUN_LR_CANONICAL_DECOMPOSITION") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 persistent-DAG increment census",
)


def _load_persistent_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "persistent_dag_increment.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_persistent_dag_increment",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_objectified_completion_decoders_give_sparse_persistent_dag_increment():
    persistent = _load_persistent_module()
    result = persistent.analyze_persistent_dag_increment()

    assert result.old_persistent_labels == 68
    assert result.old_tree_nodes == 328
    assert result.old_internal_nodes == 109
    assert result.old_terminal_merged_dag_nodes == 177
    assert result.old_weighted_depth == 135

    assert result.updated_semantics == 75
    assert result.new_completion_internal_nodes == 16
    assert result.updated_tree_nodes == 376
    assert result.updated_internal_nodes == 125
    assert result.incremental_tree_nodes == 48

    assert result.updated_terminal_merged_dag_nodes == 200
    assert result.incremental_dag_nodes == 23

    assert result.training_updated_depth == 135 + result.training_extra_queries
    assert result.training_extra_queries >= 0
    assert result.updated_worst_depth >= result.old_worst_depth
