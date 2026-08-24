"""Exact bounded presentation census for stochastic feedback-trap P1."""

import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/stochastic-feedback-trap-first-passage/phase1_presentation_census.py"
)
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase1", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_literal_and_semantic_depth_two_census_is_exact():
    census = module.depth_two_presentation_census()

    assert census.exact_depth_counts == (4, 20, 580)
    assert census.literal_count == 604
    assert len(census.semantic_presentations) == 60


def test_every_retained_presentation_has_an_auditable_strict_certificate():
    u = sp.Symbol("u", real=True)
    census = module.depth_two_presentation_census()

    assert len(census.monotone_certificates) == 16
    for certificate in census.monotone_certificates:
        assert certificate.certified
        assert certificate.derivative_root_count == 0
        assert certificate.left_value != 0
        assert certificate.right_value != 0
        assert certificate.sample_value.is_positive is True
        assert sp.Poly(certificate.derivative, u).count_roots(-1, 1) == 0
        assert sp.Poly(certificate.presentation, u).degree() == 1


def test_named_nonlinear_control_is_not_smuggled_into_depth_two_discovery():
    u = sp.Symbol("u", real=True)
    census = module.depth_two_presentation_census()

    assert u + u**3 not in census.semantic_presentations
    assert u in census.semantic_presentations


def test_monotonicity_red_teams_endpoints_interior_roots_and_orientation():
    u = sp.Symbol("u", real=True)

    positive = module.certify_strict_increase(2 * u + 1, u)
    endpoint_zero = module.certify_strict_increase(u - u**2 / 2, u)
    interior_zero = module.certify_strict_increase(u**3, u)
    reversed_orientation = module.certify_strict_increase(-u, u)

    assert positive.certified
    assert not endpoint_zero.certified
    assert not interior_zero.certified
    assert not reversed_orientation.certified
