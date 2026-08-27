from fractions import Fraction
from pathlib import Path
import sys
import unittest

import sympy as sp


WORKSTREAM_ROOT = Path(__file__).resolve().parents[1]
FROZEN_PROTOTYPE = WORKSTREAM_ROOT.parent / "scale_compiler"
sys.path.insert(0, str(FROZEN_PROTOTYPE))

from analytic_germ_adapter import (  # noqa: E402
    GermBudget,
    LocalCoordinate,
    adapt_registered_special_function,
    adapt_phase_to_germ,
    germ_summary,
    lower_registered_special_function,
    raw_germ_summary,
)
from scale_compiler import Scale  # noqa: E402


class AnalyticGermAdapterTests(unittest.TestCase):
    def setUp(self):
        self.N = sp.Symbol("N", positive=True)
        self.theta = sp.Symbol("theta")
        self.z = sp.Symbol("z")

    def test_raw_bessel_contour_phase_discovers_turning_chart(self):
        phase = self.N * (self.z * sp.sin(self.theta) - self.theta)
        report = adapt_phase_to_germ(
            phase,
            coordinates=(
                LocalCoordinate(self.theta, 0, "theta", "state"),
                LocalCoordinate(self.z, 1, "delta", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
            budget=GermBudget(max_total_degree=5),
            require_degenerate=True,
        )

        self.assertEqual(report.status, "ok")
        self.assertTrue(report.certified)
        certificate = report.certificate
        assert certificate is not None
        theta, delta, N = sp.symbols("theta delta N")
        expected = N * (delta * theta - theta**3 / 6)
        self.assertEqual(sp.expand(certificate.selected_phase - expected), 0)
        self.assertEqual(certificate.balance.scales["theta"], Scale(Fraction(-1, 3)))
        self.assertEqual(certificate.balance.scales["delta"], Scale(Fraction(-2, 3)))
        self.assertEqual(certificate.classification, "degenerate-order-3")
        self.assertTrue(all(order < Scale(0) for order in certificate.known_residual_orders))
        self.assertLess(certificate.formal_tail_order_bound, Scale(0))

    def test_normalized_detuning_phase_uses_same_generic_path(self):
        delta = sp.Symbol("delta")
        phase = self.N * ((1 + delta) * sp.sin(self.theta) - self.theta)
        report = adapt_phase_to_germ(
            phase,
            coordinates=(
                LocalCoordinate(self.theta, 0, "theta", "state"),
                LocalCoordinate(delta, 0, "delta", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
            budget=GermBudget(max_total_degree=5),
        )
        self.assertTrue(report.certified)
        assert report.certificate is not None
        self.assertEqual(report.certificate.balance.scales["theta"], Scale(Fraction(-1, 3)))
        self.assertEqual(report.certificate.balance.scales["delta"], Scale(Fraction(-2, 3)))

    def test_raw_special_function_is_oracle_boundary_failure(self):
        phase = sp.besselj(self.N, self.N * self.z)
        report = adapt_phase_to_germ(
            phase,
            coordinates=(LocalCoordinate(self.z, 1, "delta", "parameter"),),
            fixed_scales={"N": Scale(1)},
        )
        self.assertEqual(report.status, "failed")
        self.assertEqual(report.failures[0].code, "special-function-oracle-required")

    def test_registered_raw_bessel_pipeline_is_end_to_end_but_not_discovery(self):
        N = sp.Symbol("N", positive=True, integer=True)
        z = sp.Symbol("z", real=True)
        report = adapt_registered_special_function(
            sp.besselj(N, N * z),
            large_parameter=N,
            local_parameter=z,
            large_parameter_scale=Scale(1),
            budget=GermBudget(max_total_degree=5),
        )
        self.assertTrue(report.local_chart_certified)
        self.assertFalse(report.uniform_integral_certified)
        assert report.bridge.certificate is not None
        assert report.germ is not None and report.germ.certificate is not None
        bridge = report.bridge.certificate
        self.assertEqual(bridge.registry_version, 1)
        self.assertFalse(bridge.contains_scale_hint)
        self.assertFalse(bridge.contains_normal_form_hint)
        self.assertTrue(any(not item.discharged for item in bridge.obligations))
        self.assertEqual(report.germ.certificate.balance.scales["theta"], Scale(Fraction(-1, 3)))
        self.assertEqual(report.germ.certificate.balance.scales["delta"], Scale(Fraction(-2, 3)))
        summary = raw_germ_summary(report)
        self.assertTrue(summary["local_chart_certified"])
        self.assertFalse(summary["uniform_integral_certified"])
        self.assertTrue(any(not item["discharged"] for item in summary["bridge"]["obligations"]))

    def test_registered_bessel_domain_is_typed(self):
        N = sp.Symbol("N", positive=True)
        z = sp.Symbol("z", real=True)
        report = lower_registered_special_function(
            sp.besselj(N, N * z),
            large_parameter=N,
            local_parameter=z,
        )
        self.assertEqual(report.failures[0].code, "registry-domain-mismatch")

    def test_noninteger_bessel_does_not_use_integer_registry(self):
        nu = sp.Symbol("nu", positive=True, integer=False)
        z = sp.Symbol("z", real=True)
        report = lower_registered_special_function(
            sp.besselj(nu, nu * z),
            large_parameter=nu,
            local_parameter=z,
        )
        self.assertEqual(report.failures[0].code, "registry-domain-mismatch")

    def test_bessely_has_no_registered_representation(self):
        N = sp.Symbol("N", positive=True, integer=True)
        z = sp.Symbol("z", real=True)
        report = lower_registered_special_function(
            sp.bessely(N, N * z),
            large_parameter=N,
            local_parameter=z,
        )
        self.assertEqual(report.failures[0].code, "unsupported-special-function")

    def test_registered_bessel_shape_is_typed(self):
        N = sp.Symbol("N", positive=True, integer=True)
        z = sp.Symbol("z", real=True)
        report = lower_registered_special_function(
            sp.besselj(N, z),
            large_parameter=N,
            local_parameter=z,
        )
        self.assertEqual(report.failures[0].code, "registry-shape-mismatch")

    def test_regular_gaussian_is_correct_negative_control(self):
        p = sp.Symbol("p")
        phase = self.N * (self.theta**2 / 2 + p * self.theta)
        report = adapt_phase_to_germ(
            phase,
            coordinates=(
                LocalCoordinate(self.theta, 0, "theta", "state"),
                LocalCoordinate(p, 0, "p", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
            require_degenerate=True,
        )
        self.assertEqual(report.status, "failed")
        self.assertEqual(report.failures[0].code, "regular-saddle")

    def test_competing_balances_are_not_chosen_silently(self):
        x, p = sp.symbols("x p")
        phase = self.N * x**2 + self.N**2 * p * x + self.N * p**2
        report = adapt_phase_to_germ(
            phase,
            coordinates=(
                LocalCoordinate(x, 0, "x", "state"),
                LocalCoordinate(p, 0, "p", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
        )
        self.assertEqual(report.status, "failed")
        self.assertEqual(report.failures[0].code, "ambiguous-germ")
        self.assertGreaterEqual(report.subset_candidates, 2)

    def test_nonanalytic_input_fails_closed(self):
        phase = self.N * sp.Abs(self.theta)
        report = adapt_phase_to_germ(
            phase,
            coordinates=(LocalCoordinate(self.theta, 0, "theta", "state"),),
            fixed_scales={"N": Scale(1)},
        )
        self.assertEqual(report.failures[0].code, "non-analytic-germ")

    def test_resource_budget_is_visible(self):
        phase = self.N * (sp.sin(self.theta) + sp.cos(self.theta))
        report = adapt_phase_to_germ(
            phase,
            coordinates=(LocalCoordinate(self.theta, 0, "theta", "state"),),
            fixed_scales={"N": Scale(1)},
            budget=GermBudget(max_input_ops=1),
        )
        self.assertEqual(report.failures[0].code, "resource-budget-exceeded")

    def test_fixed_scale_inside_analytic_function_is_rejected(self):
        x = sp.Symbol("x")
        report = adapt_phase_to_germ(
            sp.sin(self.N * x),
            coordinates=(LocalCoordinate(x, 0, "x", "state"),),
            fixed_scales={"N": Scale(1)},
        )
        self.assertEqual(report.failures[0].code, "fixed-scale-inside-analytic-function")

    def test_quartic_cusp_control_replays_frozen_heldout_chart(self):
        t, p, q = sp.symbols("t p q")
        report = adapt_phase_to_germ(
            self.N * (t**4 / 4 + p * t**2 / 2 - q * t),
            coordinates=(
                LocalCoordinate(t, 0, "t", "state"),
                LocalCoordinate(p, 0, "p", "parameter"),
                LocalCoordinate(q, 0, "q", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
        )
        self.assertTrue(report.certified)
        assert report.certificate is not None
        self.assertEqual(report.certificate.balance.scales["t"], Scale(Fraction(-1, 4)))
        self.assertEqual(report.certificate.balance.scales["p"], Scale(Fraction(-1, 2)))
        self.assertEqual(report.certificate.balance.scales["q"], Scale(Fraction(-3, 4)))

    def test_summary_is_deterministic_and_json_compatible(self):
        delta = sp.Symbol("delta")
        report = adapt_phase_to_germ(
            self.N * ((1 + delta) * sp.sin(self.theta) - self.theta),
            coordinates=(
                LocalCoordinate(self.theta, 0, "theta", "state"),
                LocalCoordinate(delta, 0, "delta", "parameter"),
            ),
            fixed_scales={"N": Scale(1)},
            budget=GermBudget(max_total_degree=5),
        )
        first = germ_summary(report)
        second = germ_summary(report)
        self.assertEqual(first, second)
        self.assertTrue(first["certified"])


if __name__ == "__main__":
    unittest.main()
