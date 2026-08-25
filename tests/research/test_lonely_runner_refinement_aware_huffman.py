"""Sonnet 001 Phase 8D.2: refinement-aware Huffman placement is genuinely multi-axis.

Question
--------
Phase 8D showed that the local persistent graft and a separately frozen fresh
center-3 tree contain the same total amount of decision structure (`376` tree
nodes, `125` internals), but place it differently in history: the graft has
`peak/worst = 75/12`, while the fresh tree has `72/10`.

Can this placement gap be repaired merely by changing the **old center-2 wall
ordering**, if the old Huffman objective is augmented with an explicit
continuation/refinement distribution while all six local completion decoders are
kept frozen?

Primitive data
--------------
The program receives:

- the center-2 849-state task quotient, 68 persistent labels, and 21 old
  task-relevant wall predicates;
- the historical 55-input current-task usage weights;
- the six frozen Phase-8C.2 completion decoders;
- the number of locally realizable center-3 completion children below each of the
  six completion parents (288 completion children total).

No completion residual is changed.  No new center-3 wall is moved into the old
prefix search.  No full 72,241-state center-3 arrangement, fresh center-3 tree
shape, deeper contact layer, or `K=13` data is used to choose a candidate.

Classical lineage
-----------------
Huffman's classical construction optimizes expected prefix length for a fixed
symbol distribution [Huffman-1952].  Here two distinct distributions are made
explicit: current usage and continuation/refinement workload.  The Lonely Runner
computational setting is described in [Sungkawichai-Trakulthongchai-2026].

The two-distribution persistent-placement experiment is a **Shakespeare
interpretation** rather than a claim of either classical source.

Shakespeare reconstruction
---------------------------
For a bounded mixing parameter `lambda`, assign every center-2 persistent state
weight

    (1-lambda) * current_usage/55
      + lambda * completion_child_mass/288.

The exact old-wall decision-tree search is rerun for seven declared mixtures

    0, 1/16, 1/8, 1/4, 1/2, 3/4, 1.

Afterwards the six already-frozen completion decoders are grafted unchanged.
Each candidate is evaluated separately on:

- original 55-input weighted depth;
- completion-child final depth (old path plus frozen local decoder);
- boundary/tree volume;
- peak frontier;
- worst depth.

Thus the mixed weight is only a proposal generator.  The final comparison
remains multi-axis.

Calibration statement
---------------------
Passing this bounded probe certifies that:

1. `lambda=0` exactly reproduces the Phase-8D persistent graft:
   current depth `135`, completion-child depth `2933`, `376` updated tree nodes,
   `peak/worst = 75/12`;
2. a tiny refinement weight `lambda=1/16` changes current depth only `135 -> 136`
   while reducing completion-child depth `2933 -> 2146` and worst depth `12 -> 9`,
   but increases peak frontier `75 -> 93`;
3. `lambda=1/4` obtains `peak/worst = 87/10`, while `lambda=1/2` obtains `90/9`;
4. pure refinement weighting (`lambda=1`) further reduces completion-child depth
   only slightly (`1739 -> 1721` relative to `lambda=1/2`) but expands the old
   tree to `379` nodes and the graft to `427` nodes;
5. no sampled restricted-placement candidate reaches both `peak <= 72` and
   `worst <= 10`, the separately frozen fresh-tree target; and
6. after identical metric profiles are collapsed, every sampled profile is
   Pareto-nondominated across current depth, refinement depth, updated volume,
   peak frontier, and worst depth.

Proof map
---------
1. ``test_refinement_weighting_exposes_space_time_placement_tradeoff`` executes
   the seven exact old-wall searches, checks the frozen numeric profiles and
   target miss, collapses duplicate profiles, and verifies pairwise
   non-dominance of the remaining space-time/refinement tradeoffs.

Boundary
--------
This is a seven-point bounded weight sweep, not an optimization over every
possible scalarization.  More importantly, the search architecture is
restricted: all new center-3 completion walls remain below already-identified
center-2 completion terminals.  Failure to reach the fresh `72/10` placement
therefore does not prove that persistent incremental construction cannot reach
it; it shows that **reweighting the old prefix alone is insufficient in this
sampled family**.

The dramatic peak growth under refinement weighting is evidence that expected
current/refinement depth cannot safely stand in for frontier geometry.  It does
not by itself prescribe a universal `PresentationCost` field or scalar weight.

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


RUN_FULL = os.environ.get("AEG_RUN_LR_REFINEMENT_PLACEMENT") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 refinement-aware placement probe",
)


def _load_probe_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "refinement_aware_huffman.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_refinement_aware_huffman",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def _profile(candidate):
    return (
        candidate.current_weighted_depth,
        candidate.completion_final_depth,
        candidate.updated_tree_nodes,
        candidate.updated_peak,
        candidate.updated_worst,
    )


def _dominates(left, right):
    return all(a <= b for a, b in zip(left, right)) and any(
        a < b for a, b in zip(left, right)
    )


def test_refinement_weighting_exposes_space_time_placement_tradeoff():
    probe = _load_probe_module()
    result = probe.analyze_refinement_aware_placement()
    by_lambda = {candidate.mixture: candidate for candidate in result.candidates}

    baseline = by_lambda[probe.Fraction(0)]
    assert _profile(baseline) == (135, 2933, 376, 75, 12)

    small = by_lambda[probe.Fraction(1, 16)]
    assert _profile(small) == (136, 2146, 376, 93, 9)
    assert by_lambda[probe.Fraction(1, 8)] == small.__class__(
        **{**small.__dict__, "mixture": probe.Fraction(1, 8)}
    )

    quarter = by_lambda[probe.Fraction(1, 4)]
    assert _profile(quarter) == (143, 2027, 376, 87, 10)

    half = by_lambda[probe.Fraction(1, 2)]
    assert _profile(half) == (163, 1739, 376, 90, 9)
    assert _profile(by_lambda[probe.Fraction(3, 4)]) == _profile(half)

    pure = by_lambda[probe.Fraction(1)]
    assert _profile(pure) == (234, 1721, 427, 108, 9)
    assert pure.old_tree_nodes == 379

    # The restricted old-prefix reweighting family never reaches the fresh
    # center-3 peak/worst target simultaneously.
    assert not any(
        candidate.updated_peak <= 72 and candidate.updated_worst <= 10
        for candidate in result.candidates
    )

    unique_profiles = tuple(dict.fromkeys(_profile(item) for item in result.candidates))
    assert len(unique_profiles) == 5
    assert all(
        not _dominates(other, profile)
        for profile in unique_profiles
        for other in unique_profiles
        if other != profile
    )
