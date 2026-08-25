"""Sonnet 001 Phase 8C.2: quotient raw completion syntax by exact task semantics.

Question
--------
Phase 8C found, for each of six genuinely branching center-2 parents, a
minimum-cardinality set of newly generated center-3 contact-wall signs whose
joint value determines the child first-witness task.  Four minimum raw
signatures already have exactly one sign class per task class, but two are
strictly over-refined:

    11 raw sign classes -> 7 task classes,
    13 raw sign classes -> 3 task classes.

Can Shakespeare objectify the task-relative quotient of those raw signatures
and construct an exact decoder using only the selected completion walls, without
re-reading the full child pair-difference state?

Primitive data
--------------
The program receives:

- the exact Phase-8A/8B six completion parents;
- the Phase-8C minimum raw completion coordinates for each parent;
- only the locally generated center-3 children below those parents;
- exact first-witness task semantics used to define the declared task quotient.

It does not receive a hand-written compound residual, a preferred decision order,
a target decoder tree, the full 72,241-state center-3 census, deeper contact
layers, or `K=13` data.

Classical lineage
-----------------
A task quotient identifies representations that are indistinguishable for the
declared output.  Finite decision procedures then choose which predicates to
inspect to recover that output.  Huffman's classical coding result optimizes
expected prefix length when a symbol distribution is already fixed
[Huffman-1952]; Phase 8C.2 does not import Huffman coding as its quotient rule.
The surrounding Lonely Runner computational setting is documented in
[Sungkawichai-Trakulthongchai-2026].

Shakespeare reconstruction
---------------------------
For each completion parent, the Phase-8C selected contact walls first generate a
finite raw ternary sign language.  Exact child semantics induce the task-relative
equivalence relation

    raw_key_1 ~ raw_key_2  iff  task(raw_key_1) == task(raw_key_2).

The quotient therefore retains exactly the task-relevant residual classes and
forgets syntactic sign distinctions that do not change the declared first-witness
output.

To certify that this quotient is computable from the completion language rather
than merely named after the task labels, an exact adaptive decoder is searched
over only the selected raw wall coordinates.  The search minimizes, in order,
internal decision-tree nodes, worst depth, and weighted path length.  The decoder
is then replayed on every locally realized raw key.  Equal task leaves are
structurally mergeable in the resulting decision DAG.

This is a **Shakespeare interpretation**: process completion first supplies a
sufficient raw language, and task-relative objectification then removes
representation accidents inside that language.

Calibration statement
---------------------
When the opt-in research gate is enabled, passing this file certifies that:

1. all six Phase-8C minimum raw signatures admit an exact task decoder using no
   coordinates outside their selected completion walls;
2. four parents are already exact raw task quotients;
3. exactly two parents are over-refined, with class reductions `11 -> 7` and
   `13 -> 3`;
4. the objectified quotient therefore has exactly one residual class per local
   task semantic for all six parents;
5. every decoder worst depth is at most the number of selected completion walls;
   and
6. no full center-3 census or open `K=13` data enters the construction.

Proof map
---------
1. ``test_minimum_raw_completion_signatures_admit_exact_task_objectification``
   independently reconstructs the six local completion families, computes their
   raw-sign quotients and exact adaptive decoders, checks the four exact cases and
   the two strict `11->7`, `13->3` reductions, and verifies the decoder depth
   boundary.

Boundary
--------
This is a bounded task-relative objectification result.  It does not prove that
the resulting quotient is canonical for another task or a deeper contact layer,
does not claim the adaptive decoder is a universal Huffman optimum, and does not
promote a package-level `Completion` or `ResidualQuotient` API.  The decoder
search optimizes the declared finite local decision grammar only.

The heavy test is opt-in because it reconstructs the exact four-speed center-2
geometry and local center-3 completion families.  Routine CI audits this essay's
literate structure and citations without multiplying the census across the
Python matrix.

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
    reason="opt-in Sonnet 001 residual-objectification census",
)


def _load_objectification_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "residual_objectification.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_residual_objectification",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_minimum_raw_completion_signatures_admit_exact_task_objectification():
    objectification = _load_objectification_module()
    result = objectification.analyze_residual_objectification()

    assert len(result.cases) == 6
    assert len(result.over_refined_cases) == 2

    profiles = sorted(
        (case.raw_class_count, case.quotient_class_count)
        for case in result.cases
    )
    assert sum(raw == quotient for raw, quotient in profiles) == 4
    assert sorted(
        (case.raw_class_count, case.quotient_class_count)
        for case in result.over_refined_cases
    ) == [(11, 7), (13, 3)]

    for case in result.cases:
        assert case.quotient_class_count <= case.raw_class_count
        assert case.decoder_worst_depth <= case.coordinate_count
        assert case.decoder_weighted_depth <= case.coordinate_count
        assert case.decoder_internal_nodes >= 1
        assert case.decoder_unique_nodes >= case.quotient_class_count
