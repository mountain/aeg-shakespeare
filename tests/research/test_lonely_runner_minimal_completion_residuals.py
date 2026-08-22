"""Sonnet 001 Phase 8C: minimum raw wall-sign completions for the six branching states.

Question
--------
After Phase 8A/8B has identified six center-2 persistent task states that
genuinely split under the center-3 contact layer, can Shakespeare derive a
*minimal explicit process residual* for each state rather than retaining an
opaque parent identity or rebuilding the entire refined geometry?

The present question is deliberately narrow:

> among the process-generated pair/contact wall signs available at center 3,
> what is the minimum number of raw sign coordinates whose joint values determine
> the exact child task semantics inside each branching parent?

Primitive data
--------------
The search receives only the six parents already classified as completion
pressure and their **locally generated** center-3 children.  Across all eight
affected parents those children number 298; no complete 72,241-state center-3
census is enumerated by the algorithm.

For each completion parent the candidate residual grammar is every center-3
pair/contact wall sign that actually varies among that parent's possible local
children.  The search is *not* supplied with:

- the five globally known post-hoc task-relevant new walls from Phase 7h;
- a preferred runner pair;
- a target ratio;
- a fixed residual dimension;
- an opaque child-task label as a feature.

Classical lineage
-----------------
The finite optimization can be written as a set-cover problem.  Form every pair
of local children with different task semantics; a candidate wall coordinate
"covers" a conflict exactly when the two children have different signs on that
wall.  A sufficient residual signature is therefore a set of wall coordinates
covering every cross-task conflict.  Set cover is one of the classical
combinatorial problems in Karp's 1972 complexity catalogue [Karp-1972].

The underlying Lonely Runner frontier is described in
[Sungkawichai-Trakulthongchai-2026].  Huffman's minimum-redundancy coding remains
the reference point for later expected-depth optimization [Huffman-1952], but
Huffman coding does not choose the admissible geometric wall grammar used here.

The interpretation of these wall signs as **representation-completion
residuals** is Shakespeare/AEG-specific.

Shakespeare reconstruction
---------------------------
For one completion parent:

1. enumerate only its locally required center-3 children;
2. compute the exact center-3 full wall-sign signature of each child;
3. form every pair of children whose first-witness tasks differ;
4. for every varying wall coordinate, record which cross-task conflicts it
   separates;
5. solve the finite conflict-cover problem exactly by dynamic programming over
   the uncovered-conflict bitset;
6. choose a minimum-cardinality coordinate set with reproducible lexicographic
   tie breaking;
7. verify that the selected joint sign key never merges two different tasks;
8. delete each selected wall in turn and verify that a cross-task merge returns.

Step 8 gives a local executable irredundancy witness for the selected minimum
signature.  Exact minimum cardinality comes from the dynamic program itself.

Calibration statement
---------------------
When the opt-in research gate is enabled, passing this file certifies that:

1. all six Phase-8A completion parents admit exact task-sufficient residuals made
   solely from process-generated center-3 wall signs;
2. the minimum raw wall counts are exactly
   ``1, 2, 2, 2, 3, 4`` (sorted);
3. **every selected coordinate is genuinely new at center 3** -- no latent old
   wall is required by any of the six selected minimum signatures;
4. the union of selected coordinates contains seven distinct new pair/contact
   walls;
5. three five-semantic parents are represented exactly by two-wall / five-class
   signatures, and one three-semantic parent is represented exactly by a
   one-wall / three-class signature;
6. two parents remain over-refined even at minimum raw wall cardinality: one has
   7 task semantics but 11 residual sign classes, and one has 3 task semantics
   but 13 residual sign classes;
7. therefore minimum raw wall count is **not** yet the same as a minimum task
   representation -- the over-refined cases create explicit pressure for a
   subsequent residual objectification/quotient step.

Proof map
---------
1. ``test_six_completion_parents_have_minimum_new_wall_residuals`` runs the
   complete local 8A/8B/8C analysis, checks the six exact minimum-cardinality
   signatures, verifies all selected coordinates are new center-3 walls, checks
   the seven-wall union and the exact `(task classes, wall count, residual
   classes)` profile, and thereby freezes the first constructive completion
   result.

Boundary
--------
"Minimum" here means **minimum number of raw ternary pair/contact wall-sign
coordinates in the declared center-3 process grammar for that one parent**.  It
does not mean minimum description length among arbitrary composite primitives,
minimum decision-tree depth, minimum persistent-DAG size, or minimum expected
future refinement cost.

The exact conflict-cover search is local to the 298 refined children after
Phase 8A has already determined which parents require completion.  It is not a
replacement for the Observation Localization Principle at the classification
stage.

The two over-refined minimum signatures are especially important negative
controls: they show that even a cardinality-minimal set of primitive walls may
still retain task-irrelevant combinations.  A later phase must objectify or
quotient those sign patterns before claiming a canonical new primitive.

No new Lonely Runner theorem or `K=13` result is obtained.

References
----------
[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in
R. E. Miller and J. W. Thatcher (eds.), *Complexity of Computer Computations*,
The IBM Research Symposia Series, Plenum Press, 1972, pp. 85--103;
DOI 10.1007/978-1-4684-2001-2_9.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

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


RUN_FULL = os.environ.get("AEG_RUN_LR_CANONICAL_DECOMPOSITION") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 minimum completion-residual census",
)


def _load_local_refinement_module():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "local_contact_refinement.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_local_contact_refinement_completion",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_six_completion_parents_have_minimum_new_wall_residuals():
    local = _load_local_refinement_module()
    result = local.analyze_center2_to_center3()
    cases = result.completion_residual_cases

    assert len(cases) == 6
    assert sorted(case.coordinate_count for case in cases) == [1, 2, 2, 2, 3, 4]
    assert all(
        coordinate.new_at_center3
        for case in cases
        for coordinate in case.coordinates
    )

    union = {
        (coordinate.pair, coordinate.ratio)
        for case in cases
        for coordinate in case.coordinates
    }
    assert len(union) == 7
    assert union == {
        ((1, 2), Fraction(14, 11)),
        ((1, 2), Fraction(16, 11)),
        ((1, 3), Fraction(7, 3)),
        ((1, 3), Fraction(8, 3)),
        ((2, 3), Fraction(14, 11)),
        ((2, 3), Fraction(14, 9)),
        ((2, 3), Fraction(16, 9)),
    }

    profile = sorted(
        (
            case.semantic_count,
            case.coordinate_count,
            case.residual_class_count,
        )
        for case in cases
    )
    assert profile == [
        (3, 1, 3),
        (3, 4, 13),
        (5, 2, 5),
        (5, 2, 5),
        (5, 2, 5),
        (7, 3, 11),
    ]

    exact_cases = [
        case
        for case in cases
        if case.residual_class_count == case.semantic_count
    ]
    over_refined = [
        case
        for case in cases
        if case.residual_class_count > case.semantic_count
    ]
    assert len(exact_cases) == 4
    assert sorted(
        (case.semantic_count, case.coordinate_count)
        for case in exact_cases
    ) == [(3, 1), (5, 2), (5, 2), (5, 2)]
    assert sorted(
        (case.semantic_count, case.residual_class_count)
        for case in over_refined
    ) == [(3, 13), (7, 11)]
