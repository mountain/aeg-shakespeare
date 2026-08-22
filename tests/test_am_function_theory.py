import sympy as sp

from aeg_shakespeare import AMFunctionTheory, AMState, ProcessWord


def test_am_means_addition_and_multiplication_at_finite_and_infinitesimal_levels():
    a, v, t, s = sp.symbols("a v t s")
    theory = AMFunctionTheory(a, v)

    assert theory.A(a) == 1
    assert theory.A(v) == 0
    assert theory.M(a) == a
    assert theory.M(v) == 1

    residual = theory.finite_relation_residual(
        AMState(a, v),
        amount=t,
        log_scale=s,
    )
    assert residual == (0, 0)


def test_am_commutator_is_arithmetic_torsion_relation():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    expr = a**3 * v**2 + 2 * a * v + a

    assert sp.simplify(theory.commutator(expr) - theory.A(expr)) == 0


def test_ordered_process_words_remain_distinct_before_relation_reduction():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    expr = a**2

    addition_then_multiplication = theory.frame.apply_word(ProcessWord(("A", "M")), expr)
    multiplication_then_addition = theory.frame.apply_word(ProcessWord(("M", "A")), expr)

    assert sp.expand(addition_then_multiplication - multiplication_then_addition) != 0
    assert sp.expand(
        multiplication_then_addition
        - addition_then_multiplication
        - theory.A(expr)
    ) == 0


def test_am_power_weight_family_obeys_process_laws():
    a, v, w = sp.symbols("a v w")
    theory = AMFunctionTheory(a, v)
    phi = theory.power_weight(3, w)
    lowered = theory.power_weight(2, w - 1)

    assert sp.simplify(theory.M(phi.expression) - w * phi.expression) == 0
    assert sp.simplify(theory.A(phi.expression) - 3 * lowered.expression) == 0


def test_pbw_reordering_is_verified_without_erasing_history_semantics():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    expr = a**4 * v**2 + a**2 * v

    assert theory.pbw_residual(expr, m=2, n=3) == 0
