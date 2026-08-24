"""S2-prime contract calibration for a genuinely moving observer."""

import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/moving_observer_contract.py"
)
SPEC = importlib.util.spec_from_file_location("moving_observer_contract", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_moving_observer_contract_closes_the_known_riccati_control():
    certificate = module.riccati_path_certificate()

    assert certificate.certified
    assert certificate.frozen_normalization_residuals == (1, -1)
    assert certificate.observer_rates == (1, 0)
    assert sp.expand(certificate.shape) == sp.Symbol("y", real=True) ** 2 - sp.Symbol("y", real=True)
    assert sp.expand(certificate.transport) == -1
    assert sp.expand(certificate.observed) == sp.Symbol("y", real=True) ** 2 - sp.Symbol("y", real=True) - 1
    assert (certificate.fixed_complexity, certificate.canonical_complexity) == (2, 0)


def test_affine_transport_cannot_erase_an_out_of_grammar_cubic():
    epsilon = sp.Symbol("epsilon", nonzero=True)
    y = sp.Symbol("y", real=True)
    certificate = module.riccati_path_certificate(cubic_perturbation=epsilon)

    assert certificate.certified
    assert sp.expand(certificate.shape).coeff(y, 3) == epsilon
    assert sp.expand(certificate.transport).coeff(y, 3) == 0
    assert sp.expand(certificate.observed).coeff(y, 3) == epsilon
