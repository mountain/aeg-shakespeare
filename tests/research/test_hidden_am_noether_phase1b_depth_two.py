"""Snapshot and certificate checks for the depth-two S1b census."""

import importlib
from pathlib import Path
import sys


SONNET_PATH = Path(__file__).parents[2] / "sonnet" / "hidden-am-noether"
sys.path.insert(0, str(SONNET_PATH))
phase0 = importlib.import_module("phase0_contract")
phase1 = importlib.import_module("phase1_s1_census")
phase1b = importlib.import_module("phase1b_s1_depth_two")


def test_s1b_raw_grammar_count_is_frozen_before_semantic_search():
    expressions = phase0.expressions_through_depth_two()
    assert len(expressions) == 6488
    assert sum(expression.depth == 0 for expression in expressions) == 8
    assert sum(expression.depth == 1 for expression in expressions) == 72
    assert sum(expression.depth == 2 for expression in expressions) == 6408


def test_s1b_census_snapshot_and_exact_asymmetry_certificates():
    census = phase1b.run_s1b_census()

    # Snapshot values are filled from the first sealed execution.  These
    # assertions make any later grammar/quotient drift explicit.
    assert census.raw_expression_count == 6488
    assert census.semantic_expression_count == 2101
    assert census.generator_count == 40
    assert census.tested_pair_count == 84040
    assert len(census.visible_witnesses) == 8406
    assert len(census.asymmetric_expressions) == 286

    for expression in census.asymmetric_expressions:
        assert all(
            phase1.exact_process_residual(expression, coefficients) != 0
            for coefficients in phase1.projective_generator_coefficients()
        )


def test_bounded_generator_grammar_is_red_teamed_by_full_rational_nullspace():
    census = phase1b.run_s1b_census()
    expression = next(
        item for item in census.asymmetric_expressions if str(item) == "x*y**2"
    )
    nullspace = phase1.unrestricted_generator_nullspace(expression)

    # 2 M_x - M_y annihilates x*y^2 but lies outside {-1,0,1}^4.  Thus the
    # frozen bounded census cannot by itself certify genuine asymmetry.
    assert any(
        vector[0] == vector[2] == 0 and vector[1] == -2 * vector[3]
        for vector in nullspace
    )


def test_full_rational_stabilizer_filter_freezes_the_legal_s2_frontier():
    census = phase1b.run_s1b_census()
    split = phase1b.classify_unrestricted_linear_stabilizers(census)

    assert len(split.grammar_false_negatives) == 120
    assert len(split.genuine_asymmetric) == 166
    assert len(split.grammar_false_negatives) + len(split.genuine_asymmetric) == 286

    # Legal S2 inputs have full rank against every constant linear combination
    # of the declared A/M basis, not only the original 40 proposals.
    assert all(
        phase1.unrestricted_generator_nullspace(expression) == ()
        for expression in split.genuine_asymmetric
    )
    assert str(split.genuine_asymmetric[0]) == "-2*vx + x*y"
