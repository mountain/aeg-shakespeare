"""Sonnet 001 Phase 8A: discrete canonical decomposition of contact-depth refinement.

Question
--------
Can the same ``CanonicalDecomposition`` result shape that survived Riccati,
coupled scalar processes, and Restricted Kepler classify a *discrete persistent
history representation* before the next process layer is fully expanded?

More concretely: starting only from the frozen center<=2 four-speed
pair-difference/task representation and the newly admitted center-3 contact
events, can a local detector recover the exact later split

    841 stable parents / 2 transport-only parents / 6 completion parents

without consulting the complete center-3 census during classification?

Primitive data
--------------
The program receives:

- the already-certified center<=2 pair-difference sign geometry;
- its 849 exact task-safe parent states and first-witness contact prefixes;
- the new center-3 enter/exit contact events;
- exact pair-ratio/cycle semantics from the existing A/M contact presentation.

It does **not** receive the 72,241-state center-3 census, the identities of the
six splitting parents, the identities of the two uniform replacements, or a
preassigned ``renormalize / transport / complete`` label for any parent.

Classical lineage
-----------------
The Lonely Runner Conjecture and the current modular/computer-assisted frontier
are described in [Sungkawichai-Trakulthongchai-2026].  Huffman's classical
minimum-redundancy construction minimizes expected prefix-code length once a
finite symbol distribution is fixed [Huffman-1952].

Neither source contains the Shakespeare/AEG interpretation tested here.  In
particular, the identification of a persistent Hauffman task state with a local
canonical observer, and of sparse contact-depth refinement with observer
transport/completion, is explicitly a **Shakespeare interpretation**.

Shakespeare reconstruction
---------------------------
The existing local refinement code defines two observations using only old
state plus the next contact layer:

``A = forced_earlier``
    A new center-3 event is already forced at or before the old witness.

``B = effective_unresolved_crossing``
    A genuinely new, causally relevant contact wall can cross the old witness
    prefix and its side is not decided by the old representation.  Pure
    enter-enter swaps are removed by an exact first-witness causality argument.

Before evaluating any center-3 child semantics, classify

    stable              = not A and not B,
    transport_only      = A and not B,
    completion_required = B.

The result is then carried by the generic decomposition record as

    renormalizable <- stable,
    resonant       <- transport_only,
    completion     <- completion_required.

Only afterwards are the eight affected parents locally refined.  Their 26 old
full sign systems produce 298 center-3 children.  Those child semantics are a
red-team oracle for the pre-refinement classification: transport-only parents
must undergo one uniform witness replacement without branching, whereas every
completion parent must split into several new task semantics.

Calibration statement
---------------------
When the opt-in gate is enabled, passing this file certifies that:

1. the local pre-refinement detector partitions all 849 parents exactly as
   ``841 / 2 / 6``;
2. the partition is disjoint and exhaustive and therefore forms a valid
   set-valued ``CanonicalDecomposition`` certificate;
3. the two predicted transport-only parents each remain one semantic state but
   move to a new witness;
4. all six predicted completion parents genuinely split under local refinement;
5. only 26 of 5,823 old full systems are reopened and only 298 center-3 child
   systems require new semantic evaluation; and
6. those local updates recover all 75 center-3 witness semantics previously
   known from the frozen full census.

Proof map
---------
1. ``test_center_depth_refinement_has_discrete_canonical_decomposition`` runs
   the old-state-only classifier, wraps its three parent sets in
   ``CanonicalDecomposition``, checks exact disjoint/exhaustive partition
   certificates and the ``841/2/6`` counts, then checks the later local-child
   red team (2 uniform replacements, 6 genuine splits, 298 children, 75 final
   semantics).

Boundary
--------
This is a bounded four-speed, center-2 -> center-3 first-witness result.  It does
not prove a general discrete connection theorem, does not show that every
``forced_earlier`` event is transport in other tasks, and does not establish
that semantic splitting is universally equivalent to representation completion.
The full 72,241-state center-3 census remains an external frozen oracle behind
the earlier Phase-7 results; this Phase-8 classifier deliberately avoids using
it to choose the three roles.

The test is opt-in because rebuilding the 5,823-state center-2 exact geometry is
a research census and should not be multiplied across the routine CPython
3.10--3.14 CI matrix.

References
----------
[Sungkawichai-Trakulthongchai-2026] T. Sungkawichai, T. Trakulthongchai,
"Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026),
https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys

import pytest

from aeg_shakespeare.analysis.decomposition import CanonicalDecomposition


RUN_FULL = os.environ.get("AEG_RUN_LR_CANONICAL_DECOMPOSITION") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 center-depth canonical-decomposition census",
)


def _load_local_refinement_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "local_contact_refinement.py"

    # The research scripts intentionally use sibling imports so they remain
    # runnable as standalone files.  Add only that directory for this opt-in
    # executable essay; no solver or package state is imported from elsewhere.
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_local_contact_refinement",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_center_depth_refinement_has_discrete_canonical_decomposition():
    local = _load_local_refinement_module()
    result = local.analyze_center2_to_center3()

    source = (
        result.stable_parents
        | result.transport_only_parents
        | result.completion_required_parents
    )
    certificate = (
        result.parent_count - len(source),
        len(result.stable_parents & result.transport_only_parents),
        len(result.stable_parents & result.completion_required_parents),
        len(result.transport_only_parents & result.completion_required_parents),
    )
    decomposition = CanonicalDecomposition(
        source=source,
        renormalizable=result.stable_parents,
        resonant=result.transport_only_parents,
        completion=result.completion_required_parents,
        certificate=certificate,
        label="Lonely Runner center-depth local role partition",
    )

    # DISCOVER / ASSERT: the role partition is obtained before center-3 child
    # semantics are inspected inside the refinement analysis.
    assert decomposition.certificate == (0, 0, 0, 0)
    assert len(decomposition.renormalizable) == 841
    assert len(decomposition.resonant) == 2
    assert len(decomposition.completion) == 6

    # RED TEAM: only the locally affected children test whether the predicted
    # transport/completion roles match actual next-layer task semantics.
    assert result.verified_replacement_count == 2
    assert result.verified_split_count == 6
    assert result.affected_full_system_count == 26
    assert result.refined_child_count == 298
    assert result.recovered_semantic_count == 75
