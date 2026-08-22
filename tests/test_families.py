import sympy as sp

from aeg_shakespeare.process.finite import (
    FamilyAction,
    ProcessCharacter,
    ProcessFamily,
    character_invariance_residual,
    transport_process_character,
    verify_family_action,
    verify_process_character,
)


def test_process_family_reduces_ordered_parameter_history():
    family = ProcessFamily("T", lambda a, b: a + b, identity=0)
    assert family.fold_parameters((1, 2, 3)) == 6
    assert family.fold_parameters(()) == 0
    assert family.step(4).family_name == "T"
    assert family.step(4).parameter == 4


def test_symbolic_additive_character_has_exact_multiplicativity_certificate():
    a, b, xi = sp.symbols("a b xi", real=True)
    family = ProcessFamily("T", lambda left, right: sp.expand(left + right), identity=0)
    character = ProcessCharacter(
        family,
        lambda parameter: sp.exp(sp.I * xi * parameter),
        label=xi,
    )
    verification = verify_process_character(character, ((a, b),))
    assert verification.exact
    assert verification.multiplicativity_residuals == (0,)
    assert verification.normalization_residual == 0


def test_multiplicative_character_can_supply_backend_log_simplification():
    a, b, tau = sp.symbols("a b tau", positive=True, real=True)
    family = ProcessFamily("S", lambda left, right: sp.expand(left * right), identity=1)

    def simplify_mellin(expr):
        return sp.simplify(sp.expand_log(sp.sympify(expr), force=True))

    character = ProcessCharacter(
        family,
        lambda parameter: sp.exp(sp.I * tau * sp.log(parameter)),
        label=tau,
        simplify=simplify_mellin,
    )
    verification = verify_process_character(character, ((a, b),))
    assert verification.exact


def test_family_action_verifies_parameter_laws_and_transports_characters():
    a, c = sp.symbols("a c", positive=True, real=True)
    b, d, xi = sp.symbols("b d xi", real=True)
    dilation = ProcessFamily("S", lambda left, right: sp.expand(left * right), identity=1)
    translation = ProcessFamily("T", lambda left, right: sp.expand(left + right), identity=0)
    action = FamilyAction(
        dilation,
        translation,
        lambda scale, shift: sp.expand(scale * shift),
        name="scale_translation",
    )
    verification = verify_family_action(
        action,
        acting_parameters=(a,),
        acting_pairs=((a, c),),
        target_parameters=(b,),
        target_pairs=((b, d),),
    )
    assert verification.exact

    character = ProcessCharacter(
        translation,
        lambda shift: sp.exp(sp.I * xi * shift),
        label=xi,
    )
    transported = transport_process_character(character, action, a)
    assert sp.simplify(
        transported.value(b) - sp.exp(sp.I * (a * xi) * b)
    ) == 0
    assert verify_process_character(transported, ((b, d),)).exact
    assert character_invariance_residual(character, action, a, b) != 0
