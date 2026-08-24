"""Execute the frozen stopped-process task quotient."""

import importlib.util
from pathlib import Path
import sys


MODULE_PATH = Path(__file__).parents[2] / "sonnet/stochastic-feedback-trap-first-passage/phase2_task_quotient.py"
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase2", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_full_ito_transport_quotients_every_monotone_chart_to_one_task_class():
    quotient = module.depth_three_task_quotient()

    assert len(quotient.certificates) == 242
    assert all(certificate.full_task_certified for certificate in quotient.certificates)
    assert quotient.equivalence_class_count == 1


def test_omitting_ito_drift_correction_falsely_splits_affine_and_nonlinear_charts():
    quotient = module.depth_three_task_quotient()
    naive_passes = tuple(c for c in quotient.certificates if c.naive_residual == 0)
    naive_failures = tuple(c for c in quotient.certificates if c.naive_residual != 0)

    assert len(naive_passes) == 87
    assert len(naive_failures) == 155
    assert all(c.degree == 1 for c in naive_passes)
    assert all(c.degree > 1 for c in naive_failures)


def test_full_task_payload_is_retained_under_every_forward_morphism():
    quotient = module.depth_three_task_quotient()

    assert all(c.sections[0] < c.sections[1] for c in quotient.certificates)
    assert {c.section_labels for c in quotient.certificates} == {("left", "right")}
    assert {c.clock for c in quotient.certificates} == {"theta=Vt/L"}
