"""Sonnet 001 Phase 8A/8B red team: discrete canonical decomposition.

Question
--------
Can the same ``CanonicalDecomposition`` result shape that survived Riccati,
coupled scalar processes, and Restricted Kepler classify a *discrete persistent
history representation* before the next process layer is fully expanded?

Starting only from the frozen center<=2 four-speed pair-difference/task
representation and the newly admitted center-3 contact events, the local detector
first separates

    841 stable parents / 2 nonbranching changed-task parents / 6 branching parents

without consulting the complete center-3 census during classification.

A second red team then asks a stricter question: do the two nonbranching changes
actually move the canonical witness observer, or do they merely reindex the same
witness in a deeper contact history?

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
particular, the relation between persistent Huffman task states and
renormalization/observer transport/completion is explicitly a **Shakespeare
interpretation** and must survive executable red teams before being promoted.

Shakespeare reconstruction
---------------------------
The local refinement code defines two observations using only old state plus the
next contact layer:

``A = forced_earlier``
    A new center-3 event is already forced at or before the old witness.

``B = effective_unresolved_crossing``
    A genuinely new, causally relevant contact wall can cross the old witness
    prefix and its side is not decided by the old representation.  Pure
    enter-enter swaps are removed by an exact first-witness causality argument.

Before evaluating any center-3 child semantics, classify

    stable              = not A and not B,
    nonbranching_update = A and not B,
    completion_required = B.

This local partition is exactly ``841 / 2 / 6``.

Only afterwards are the eight affected parents refined.  Their 26 old full sign
systems produce 298 center-3 children.  Those child semantics show that every
``completion_required`` parent genuinely branches.

The two nonbranching cases then receive a second, stricter audit.  In both cases:

- the witness boundary remains exactly ``((1, 1, 'exit'),)``;
- the witness mode remains exactly ``'interval'``;
- only the event index changes, by ``+2``.

So the observer geometry itself does **not** move.  These two cases are history /
decoder reindexing inside the current representation and therefore belong to the
renormalizable sector, not the resonant/observer-transport sector.

The canonical decomposition supported by the complete red team is consequently

    renormalizable = 843 = 841 stable + 2 history-reindex states,
    resonant       = 0,
    completion     = 6.

Calibration statement
---------------------
When the opt-in gate is enabled, passing this file certifies that:

1. the pre-refinement local detector partitions all 849 parents as
   ``841 stable / 2 nonbranching update / 6 completion pressure``;
2. later exact local refinement shows all six predicted completion parents
   genuinely branch;
3. the two nonbranching states preserve the exact same witness boundary and mode
   and only shift the event index by ``+2``;
4. those two states therefore remain in the current representation and join the
   stable states in the renormalizable sector;
5. the resulting evidence-bearing ``CanonicalDecomposition`` has exact sector
   sizes ``843 / 0 / 6``;
6. only 26 of 5,823 old full systems are reopened, only 298 center-3 child
   systems require new semantic evaluation, and the local update recovers all
   75 center-3 witness semantics.

Proof map
---------
1. ``test_center_depth_refinement_has_discrete_canonical_decomposition`` runs
   the old-state-only classifier, checks the exact ``841/2/6`` local partition,
   then uses the post-classification child red team to verify six genuine splits
   and to audit the two nonbranching witness records.  It finally wraps the
   corrected ``843/0/6`` sectors in ``CanonicalDecomposition`` and checks the
   disjoint/exhaustive certificate plus the 26/298/75 locality counts.

Boundary
--------
This is a bounded four-speed, center-2 -> center-3 first-witness result.  It does
not prove a general discrete canonical-decomposition theorem and does not
establish that semantic splitting is universally equivalent to representation
completion.

Most importantly, this red team gives **no evidence for a discrete observer
connection** in the two nonbranching cases.  The earlier working label
``transport-only`` was rejected: the canonical witness boundary/mode is fixed and
only its history index is renormalized.  A future discrete connection example
must exhibit an actual same-family observer-state change rather than a decoder or
history-coordinate shift.

The full 72,241-state center-3 census remains an external frozen oracle behind
the earlier Phase-7 results; this Phase-8 classifier avoids using it to choose
the local partition.  The test is opt-in because rebuilding the 5,823-state
center-2 exact geometry is a research census and should not be multiplied across
the routine CPython 3.10--3.14 CI matrix.

References
----------
[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

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

from process_geometry.experimental import CanonicalDecomposition


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
    # runnable as standalone files. Add only that directory for this opt-in
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

    # DISCOVER / ASSERT: the three-way local partition is chosen before any
    # center-3 child semantics are inspected inside the refinement analysis.
    assert len(result.stable_parents) == 841
    assert len(result.history_reindex_parents) == 2
    assert len(result.completion_required_parents) == 6

    # PHASE 8B RED TEAM: the two nonbranching states do not move the witness
    # geometry. They only shift the same witness two event ranks later.
    assert len(result.history_reindex_cases) == 2
    assert all(case.same_boundary for case in result.history_reindex_cases)
    assert all(case.same_mode for case in result.history_reindex_cases)
    assert all(case.event_index_shift == 2 for case in result.history_reindex_cases)

    source = result.renormalizable_parents | result.completion_required_parents
    certificate = (
        result.parent_count - len(source),
        len(result.renormalizable_parents & result.completion_required_parents),
        len(result.resonant_parents),
    )
    decomposition = CanonicalDecomposition(
        source=source,
        renormalizable=result.renormalizable_parents,
        resonant=result.resonant_parents,
        completion=result.completion_required_parents,
        certificate=certificate,
        label="Lonely Runner center-depth canonical role partition",
    )

    assert decomposition.certificate == (0, 0, 0)
    assert len(decomposition.renormalizable) == 843
    assert len(decomposition.resonant) == 0
    assert len(decomposition.completion) == 6

    # RED TEAM / LOCALITY: the affected children verify six genuine splits while
    # the two nonbranching changes are exact history reindexings.
    assert result.verified_reindex_count == 2
    assert result.verified_split_count == 6
    assert result.affected_full_system_count == 26
    assert result.refined_child_count == 298
    assert result.recovered_semantic_count == 75
