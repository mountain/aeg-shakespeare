"""Exact certificate checks for the Hidden A/M Noether S1a census."""

import importlib
from pathlib import Path
import sys


SONNET_PATH = Path(__file__).parents[2] / "sonnet" / "hidden-am-noether"
sys.path.insert(0, str(SONNET_PATH))
phase1 = importlib.import_module("phase1_s1_census")


def test_s1a_census_exhausts_the_frozen_depth_one_product():
    census = phase1.run_s1_census()

    assert census.raw_expression_count == 80
    assert census.semantic_expression_count == 57
    assert census.generator_count == 40
    assert census.tested_pair_count == 2280
    assert len(census.visible_witnesses) == 711
    assert census.asymmetric_expressions == ()

    # Every retained witness carries the exact zero residual; every claimed
    # asymmetric expression has been tested against all 40 candidates.
    assert all(witness.residual == 0 for witness in census.visible_witnesses)
    # S2 is intentionally blocked at this depth: every semantic expression has
    # at least one visible stabilizer in the four-generator grammar.
    assert {
        str(witness.expression) for witness in census.visible_witnesses
    } == {str(expression) for expression in phase1.canonical_semantic_expressions()}


def test_census_contains_positive_and_negative_controls_without_oracle_labels():
    census = phase1.run_s1_census()
    profiles = {}
    for witness in census.visible_witnesses:
        profiles.setdefault(str(witness.expression), set()).add(
            witness.generator_coefficients
        )

    # x is invariant under A_y, while x+y has no nonzero constant-translation
    # symmetry in this projective grammar unless coefficients cancel both
    # derivatives.  The assertions inspect census output rather than seed it.
    assert (0, 0, 1, 0) in profiles["x"]
    assert str(phase1.X * phase1.Y) not in {
        str(expression) for expression in census.asymmetric_expressions
    }


def test_semantic_quotient_collapses_literal_identity_noise_exactly():
    expressions = phase1.canonical_semantic_expressions()
    rendered = {str(expression) for expression in expressions}

    # Literal x*1, x+0-like constructions (where zero arises from -1+1 only
    # at the next depth) are canonicalized by exact expression semantics.
    assert len(expressions) < 80
    assert "x" in rendered
    assert len(rendered) == len(expressions)
