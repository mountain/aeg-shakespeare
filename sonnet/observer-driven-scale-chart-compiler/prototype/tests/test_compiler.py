from fractions import Fraction
import unittest

import sympy as sp

from scale_compiler import Observer, Scale, Series, Var, compile_expression, exp, log


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.N = Var("N")
        self.bindings = {"N": Series.monomial(1)}

    def test_addition_cancellation_is_exact(self):
        report = compile_expression(self.N - self.N + 1, self.bindings)
        self.assertEqual(report.status, "ok")
        self.assertEqual(report.result.constant_coefficient, 1)
        self.assertEqual(report.result.leading_scale, Scale(0))

    def test_multiplication_adds_orders(self):
        expression = self.N * (self.N ** -1)
        report = compile_expression(expression, self.bindings)
        self.assertEqual(report.status, "ok")
        self.assertEqual(report.result.constant_coefficient, 1)

    def test_log_propagates_small_scale(self):
        expression = log(1 + self.N ** -1)
        report = compile_expression(expression, self.bindings)
        self.assertEqual(report.status, "ok")
        self.assertEqual(report.result.leading_scale, Scale(-1))
        self.assertEqual(report.result.terms[Fraction(-1)], 1)

    def test_infinite_exponent_rescues_hidden_base_perturbation(self):
        expression = (1 + self.N ** -1) ** self.N
        observer = Observer(
            visible_at_or_above=Scale(0),
            require_remainder_below=Scale(-3),
            initial_taylor_order=2,
            max_taylor_order=16,
        )
        report = compile_expression(expression, self.bindings, observer)
        self.assertEqual(report.status, "ok")
        self.assertTrue(report.certified)
        self.assertEqual(sp.simplify(report.result.constant_coefficient - sp.E), 0)
        self.assertTrue(any(event.rescued for event in report.visibility_events))
        event = next(event for event in report.visibility_events if event.rescued)
        self.assertEqual(event.hidden_input, Scale(-1))
        self.assertEqual(event.amplifier, Scale(1))
        self.assertEqual(event.output_effect, Scale(0))
        base_obligation = next(
            obligation
            for obligation in report.obligations
            if obligation.operator == "Pow" and obligation.child == "base"
        )
        self.assertEqual(base_obligation.parent_required, Scale(0))
        self.assertEqual(base_obligation.child_required, Scale(-1))
        self.assertGreater(report.cost.retries, 0)

    def test_log_exp_round_trip_to_observer_precision(self):
        expression = exp(log(1 + self.N ** -1))
        observer = Observer(require_remainder_below=Scale(-3), max_taylor_order=16)
        report = compile_expression(expression, self.bindings, observer)
        self.assertEqual(report.status, "ok")
        self.assertEqual(report.result.terms[Fraction(0)], 1)
        self.assertEqual(report.result.terms[Fraction(-1)], 1)

    def test_rational_power_uses_the_same_bounded_germ(self):
        expression = (1 + self.N ** -1) ** sp.Rational(1, 2)
        observer = Observer(
            visible_at_or_above=Scale(-1),
            require_remainder_below=Scale(-3),
            max_taylor_order=16,
        )
        report = compile_expression(expression, self.bindings, observer)
        self.assertEqual(report.status, "ok")
        self.assertEqual(report.result.terms[Fraction(-1)], sp.Rational(1, 2))

    def test_inexact_float_scale_is_rejected(self):
        with self.assertRaises(TypeError):
            Scale(-1 / 3)

    def test_budget_exhaustion_is_not_silently_certified(self):
        expression = (1 + self.N ** -1) ** self.N
        observer = Observer(
            require_remainder_below=Scale(-10),
            initial_taylor_order=2,
            max_taylor_order=2,
        )
        report = compile_expression(expression, self.bindings, observer)
        self.assertEqual(report.status, "unsafe")
        self.assertFalse(report.certified)
        self.assertEqual(report.failures[0].code, "budget-exhausted")

    def test_large_exponential_is_typed_failure(self):
        report = compile_expression(exp(self.N), self.bindings)
        self.assertEqual(report.status, "failed")
        self.assertEqual(report.failures[0].code, "unsupported-scale")

    def test_resource_budget_is_part_of_the_task_contract(self):
        report = compile_expression(
            1 + self.N + self.N ** 2,
            self.bindings,
            Observer(max_input_nodes=2),
        )
        self.assertEqual(report.status, "failed")
        self.assertEqual(report.failures[0].code, "resource-budget-exceeded")


if __name__ == "__main__":
    unittest.main()
