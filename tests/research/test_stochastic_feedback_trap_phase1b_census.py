"""Executed depth-three semantic census and nonlinear survivor certificate."""

import importlib.util
from collections import Counter
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/stochastic-feedback-trap-first-passage/phase1_presentation_census.py"
)
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase1b_run", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_depth_three_exact_census_and_degree_histograms_are_frozen():
    u = sp.Symbol("u", real=True)
    census = module.depth_three_presentation_census()
    semantic_histogram = Counter(
        -1 if expression == 0 else sp.Poly(expression, u).degree()
        for expression in census.semantic_presentations
    )
    monotone_histogram = Counter(
        sp.Poly(certificate.presentation, u).degree()
        for certificate in census.monotone_certificates
    )

    assert census.exact_depth_counts == (4, 20, 580, 364_820)
    assert census.literal_count == 365_424
    assert len(census.semantic_presentations) == 1_519
    assert semantic_histogram == {
        -1: 1,
        0: 22,
        1: 163,
        2: 487,
        3: 503,
        4: 248,
        5: 69,
        6: 20,
        7: 5,
        8: 1,
    }
    assert len(census.monotone_certificates) == 242
    assert monotone_histogram == {1: 87, 2: 55, 3: 97, 4: 3}


def test_nonlinear_survivor_set_is_large_and_every_certificate_is_exact():
    u = sp.Symbol("u", real=True)
    census = module.depth_three_presentation_census()
    nonlinear = tuple(
        certificate
        for certificate in census.monotone_certificates
        if sp.Poly(certificate.presentation, u).degree() > 1
    )

    assert len(nonlinear) == 155
    assert all(certificate.certified for certificate in nonlinear)
    assert all(certificate.derivative_root_count == 0 for certificate in nonlinear)


def test_held_out_control_enters_post_hoc_but_is_not_a_unique_grammar_witness():
    u = sp.Symbol("u", real=True)
    census = module.depth_three_presentation_census()
    nonlinear_presentations = {
        certificate.presentation
        for certificate in census.monotone_certificates
        if sp.Poly(certificate.presentation, u).degree() > 1
    }

    assert u + u**3 in nonlinear_presentations
    assert len(nonlinear_presentations - {u + u**3}) == 154
