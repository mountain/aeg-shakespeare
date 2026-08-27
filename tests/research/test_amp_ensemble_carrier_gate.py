"""Exact first-cut tests for AMP closure, ensemble folding, and carrier scope."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/amp-ensemble-carrier-gate/amp_ensemble_compiler.py"
)
SPEC = importlib.util.spec_from_file_location("amp_ensemble_compiler", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def vector_field_bracket(left: sp.Expr, right: sp.Expr, x: sp.Symbol) -> sp.Expr:
    """Coefficient of ``[left*d/dx, right*d/dx]``."""

    return sp.expand(left * sp.diff(right, x) - right * sp.diff(left, x))


def test_adjacent_amp_conjugations_are_exact_in_their_native_charts():
    x, y, s, t, r = sp.symbols("x y s t r", positive=True)

    # M_s A_t M_s^-1 = A_(exp(s)t) in the x chart.
    conjugated_addition = sp.exp(s) * (sp.exp(-s) * x + t)
    assert sp.simplify(conjugated_addition - (x + sp.exp(s) * t)) == 0

    # In y=log(x), M_s is translation and P_r is dilation.  Therefore
    # P_r M_s P_r^-1 = M_(exp(r)s) without a branch simplification oracle.
    conjugated_multiplication = sp.exp(r) * (sp.exp(-r) * y + s)
    assert sp.simplify(conjugated_multiplication - (y + sp.exp(r) * s)) == 0


def test_amp_generators_leave_their_three_dimensional_span():
    x = sp.symbols("x", positive=True)
    A = sp.Integer(1)
    M = x
    P = x * sp.log(x)

    assert sp.simplify(vector_field_bracket(A, M, x) - A) == 0
    assert sp.simplify(vector_field_bracket(M, P, x) - M) == 0
    assert sp.simplify(
        vector_field_bracket(A, P, x) - (1 + sp.log(x))
    ) == 0

    # A constant linear combination of A, M, and P cannot equal log(x)*d/dx:
    # the coefficient of x*log(x) first forces the P coefficient to zero,
    # after which the logarithm remains unavailable.
    c0, c1, c2 = sp.symbols("c0 c1 c2")
    candidate = c0 + c1 * x + c2 * x * sp.log(x)
    samples = [sp.E, sp.E**2, sp.E**3, sp.E**4]
    equations = [sp.Eq(candidate.subs(x, value), sp.log(value)) for value in samples]
    assert sp.solve(equations, (c0, c1, c2), dict=True) == []


def test_general_monomial_logarithmic_bracket_formula():
    x = sp.symbols("x", positive=True)
    for m, n, p, q in ((0, 0, 1, 1), (-2, 3, 4, 1), (1, 1, 0, 2)):
        left = x**m * sp.log(x) ** n
        right = x**p * sp.log(x) ** q
        expected = sp.Integer(0)
        for (x_power, log_degree), coefficient in module.monomial_vector_field_bracket(
            m, n, p, q
        ):
            expected += coefficient * x**x_power * sp.log(x) ** log_degree
        assert sp.simplify(vector_field_bracket(left, right, x) - expected) == 0


def test_full_amp_lie_closure_contains_an_infinite_independent_family():
    witnesses = [module.negative_power_closure_witness(k) for k in range(1, 13)]

    assert [power for _, power in witnesses] == list(range(-1, -13, -1))
    assert [coefficient for coefficient, _ in witnesses[:5]] == [1, -1, 2, -6, 24]

    # Distinct Laurent monomials are linearly independent.  A finite sweep of
    # exponents records the theorem's explicit witnesses, not a dimension guess.
    assert len({power for _, power in witnesses}) == len(witnesses)


def test_mp_words_compile_to_two_field_affine_normal_forms():
    history = (
        module.multiplication(Fraction(2, 3)),
        module.power(Fraction(3, 2)),
        module.multiplication(Fraction(-5, 7)),
        module.power(2),
    )
    normal = module.fold_mp(history)

    direct = Fraction(11, 5)
    for step in history:
        direct = step.apply_log(direct)

    assert normal.apply_log(Fraction(11, 5)) == direct
    assert normal.exponent == 3
    assert normal.log_scale == Fraction(4, 7)


def test_mp_conjugation_and_repeated_iteration_have_closed_forms():
    exponent = Fraction(5, 3)
    log_scale = Fraction(7, 4)

    conjugated = module.fold_mp(
        (
            module.power(1 / exponent),
            module.multiplication(log_scale),
            module.power(exponent),
        )
    )
    assert conjugated == module.multiplication(exponent * log_scale)

    primitive = module.MPNormalForm(exponent=Fraction(3, 2), log_scale=Fraction(5, 7))
    closed = primitive.iterate(40)
    replay = module.MPNormalForm()
    for _ in range(40):
        replay = replay.then(primitive)
    assert closed == replay


def test_homogeneous_ensemble_folds_without_cartesian_state_enumeration():
    stages = (
        module.EnsembleStage(2, Fraction(1)),
        module.EnsembleStage(3, Fraction(-2)),
        module.EnsembleStage(2, Fraction(4)),
    )
    certificate = module.compile_homogeneous_ensemble(3, stages)

    base_log_partition = Fraction(5)
    direct = base_log_partition
    for stage in stages:
        direct = stage.replicas * direct + stage.log_prefactor

    assert certificate.replay_log_partition(base_log_partition) == direct == 66
    assert certificate.normal_form.exponent == 12
    assert certificate.normal_form.log_scale == 6
    assert certificate.ledger.microstate_count_power == (3, 12)
    assert 3**12 == 531_441
    assert certificate.ledger.compiled_state_fields == 2


def test_power_objectifies_a_large_repeated_ensemble_for_a_coarse_observer():
    certificate = module.compile_homogeneous_ensemble(
        base_state_count=3,
        stages=(module.EnsembleStage(2),) * 20,
    )

    # The total-partition observer stores one exponent and one log prefactor.
    # Literal expansion would expose over one million base copies and a
    # Cartesian state count of 3**1_048_576.
    assert certificate.normal_form.exponent == 1_048_576
    assert certificate.ledger.expanded_leaf_count == 1_048_576
    assert certificate.ledger.microstate_count_power == (3, 1_048_576)
    assert certificate.ledger.compiled_state_fields == 2
    assert certificate.ledger.replay_arithmetic_operations == 2
    assert certificate.ledger.replica_exponent_bit_length == 21
    assert certificate.ledger.microstate_count_bit_length_lower_bound == 1_048_577


def test_addition_breaks_the_finite_mp_carrier_but_has_a_fixed_hahn_shadow():
    q, t = sp.symbols("q t")
    order = 8
    tail = module.logarithmic_addition_tail(Fraction(2, 3), order)
    polynomial = sum(sp.Rational(coefficient.numerator, coefficient.denominator) * q**degree for degree, coefficient in tail)

    exact_series = sp.series(sp.log(1 + sp.Rational(2, 3) * q), q, 0, order + 1).removeO()
    assert sp.expand(polynomial - exact_series) == 0

    # In y=log(x), a translation x->x+t is y->log(exp(y)+t).  Its second
    # derivative is nonzero, so it is not another affine M/P normal form.
    y = sp.symbols("y", real=True)
    moved = sp.log(sp.exp(y) + t)
    assert sp.simplify(sp.diff(moved, y, 2)) != 0


def test_typed_boundaries_fail_closed():
    for bad_exponent in (0, -1):
        try:
            module.power(bad_exponent)
        except ValueError:
            pass
        else:  # pragma: no cover - explicit fail-closed boundary.
            raise AssertionError("nonpositive power exponent was accepted")

    try:
        module.compile_homogeneous_ensemble(2, (module.EnsembleStage(0),))
    except ValueError:
        pass
    else:  # pragma: no cover
        raise AssertionError("zero-replica ensemble stage was accepted")
