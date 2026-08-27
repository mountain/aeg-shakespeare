import unittest
from fractions import Fraction

import sympy as sp

from scale_compiler import Scale, Var, exp, infer_distinguished_scaling
from scale_compiler.balance import UnderdeterminedBalanceError


class BalanceTests(unittest.TestCase):
    def test_airy_chart_is_inferred_without_expected_scales(self):
        N = Var("N")
        t = Var("t")
        z = Var("z")
        airy_integrand = exp(-N * (t ** 3 / 3 - z * t))

        result = infer_distinguished_scaling(
            airy_integrand,
            unknown_scales=("t", "z"),
            fixed_scales={"N": Scale(1)},
        )

        self.assertEqual(result.status, "ok")
        self.assertEqual(result.scales["t"], Scale(Fraction(-1, 3)))
        self.assertEqual(result.scales["z"], Scale(Fraction(-2, 3)))
        self.assertEqual(result.term_orders, (Scale(0), Scale(0)))
        self.assertEqual(result.input_term_count, 2)
        self.assertEqual(result.solve_rank, 2)
        t_hat, z_hat = sp.symbols("t_hat z_hat")
        self.assertEqual(
            sp.simplify(result.normalized_phase - (-t_hat ** 3 / 3 + t_hat * z_hat)),
            0,
        )
        self.assertTrue(result.certified)

    def test_underdetermined_problem_requests_more_task_information(self):
        N = Var("N")
        x = Var("x")
        y = Var("y")
        expression = exp(N * x * y)
        with self.assertRaises(UnderdeterminedBalanceError):
            infer_distinguished_scaling(
                expression,
                unknown_scales=("x", "y"),
                fixed_scales={"N": Scale(1)},
            )


if __name__ == "__main__":
    unittest.main()
