import sympy as sp

from aeg_shakespeare import (
    AMFunctionTheory,
    AMState,
    ProcessFunctionModule,
    ProcessWord,
    polynomial_am_module,
)


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


def test_am_power_weight_family_obeys_process_and_product_laws():
    a, v, w, z = sp.symbols("a v w z")
    theory = AMFunctionTheory(a, v)
    phi = theory.power_weight(3, w)
    lowered = theory.power_weight(2, w - 1)

    assert sp.simplify(theory.M(phi.expression) - w * phi.expression) == 0
    assert sp.simplify(theory.A(phi.expression) - 3 * lowered.expression) == 0

    psi = theory.power_weight(2, z)
    product = theory.multiply_power_weights(phi, psi)
    assert product.nu == 5
    assert sp.simplify(product.weight - (w + z)) == 0
    assert sp.simplify(product.expression - phi.expression * psi.expression) == 0


def test_pbw_reordering_is_verified_without_erasing_history_semantics():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    expr = a**4 * v**2 + a**2 * v

    assert theory.pbw_residual(expr, m=2, n=3) == 0


def test_addition_primitive_stays_on_weight_lattice_away_from_resonance():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    element = theory.power_weight(2, 5)

    primitive = theory.A_primitive(element)
    assert not primitive.resonant
    assert primitive.exceptional_factor == 3
    assert theory.primitive_residual(primitive) == 0


def test_addition_resonance_creates_logarithmic_extension():
    a, v = sp.symbols("a v", positive=True)
    theory = AMFunctionTheory(a, v)
    element = theory.power_weight(-1, 2)

    primitive = theory.A_primitive(element)
    assert primitive.resonant
    assert sp.simplify(primitive.expression - sp.exp(3 * v) * sp.log(a)) == 0
    assert theory.primitive_residual(primitive) == 0


def test_multiplication_resonance_creates_v_extension():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    element = theory.power_weight(2, 0)

    primitive = theory.M_primitive(element)
    assert primitive.resonant
    assert sp.expand(primitive.expression - v * a**2 * sp.exp(-2 * v)) == 0
    assert theory.primitive_residual(primitive) == 0


def test_ordered_am_path_flow_keeps_history_reweighting_explicit():
    a, v, t, T, a0, v0 = sp.symbols("a v t T a0 v0", positive=True)
    theory = AMFunctionTheory(a, v)

    flow = theory.path_flow(
        alpha=1,
        beta=2,
        time=t,
        start=0,
        end=T,
        a0=a0,
        v0=v0,
    )

    expected_history = (sp.exp(2 * T) - 1) / 2
    assert sp.simplify(flow.beta_integral - 2 * T) == 0
    assert sp.simplify(flow.history_term - expected_history) == 0
    assert sp.simplify(flow.a_end - (sp.exp(2 * T) * a0 + expected_history)) == 0
    assert sp.simplify(flow.v_end - (v0 + 2 * T)) == 0


def test_polynomial_tower_is_a_small_finite_am_process_module():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    module = polynomial_am_module(a, 4)

    assert module.dimension == 5
    assert module.generators == ("A", "M")
    assert module.verify(theory.frame)


def test_process_function_module_is_generic_and_returns_failed_certificates():
    a, v = sp.symbols("a v")
    theory = AMFunctionTheory(a, v)
    bad = ProcessFunctionModule(
        basis=(1, a),
        actions={
            "A": ((0, 0), (0, 0)),  # deliberately claims A(a)=0
            "M": ((0, 0), (0, 1)),
        },
    )

    residuals = bad.verification_residuals(theory.frame)
    assert residuals["A"] == (0, 1)
    assert not bad.verify(theory.frame)
