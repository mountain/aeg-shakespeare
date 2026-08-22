"""A/M I: scale transports translation characters and obstructs a nontrivial invariant scalar response.

Question
--------
Once Translation I and Dilation I share one finite-family/character API, what is
the smallest additional structure required to express their noncommutative
interaction?

Primitive data
--------------
The finite process families satisfy

    T_b T_c = T_{b+c},
    S_a S_c = S_{ac},

and scaling acts on translation parameters by

    b -> a b.

Equivalently this records the finite A/M relation

    S_a T_b S_a^{-1} = T_{ab}

without constructing a general affine-group object.

Shakespeare reconstruction
---------------------------
``FamilyAction`` stores the parameter transport ``b -> a b``.  Pulling the
translation character

    chi_xi(b) = exp(i xi b)

along that action produces

    chi_xi(ab) = chi_{a xi}(b).

Thus scale acts on the character label itself.  A nontrivial translation
character is not invariant under generic scale transport, so a one-dimensional
scalar response cannot preserve the full A/M interaction simply by assigning an
independent scalar to each family.

Calibration statement
---------------------
Passing this file certifies that ``FamilyAction`` plus character transport is
enough to express the first noncommutative A/M pressure, and that the existing
scalar character abstraction exposes its own obstruction rather than silently
pretending to be a full representation theory.

New reusable abstraction
-------------------------
``FamilyAction`` and bounded character transport/invariance residuals.

Unresolved manual choice
------------------------
The next response space after scalar characters is not selected here.  In
particular no wavelet, Hilbert-space representation, or spectrum API is added.

Boundary
--------
This is an obstruction/calibration result, not noncommutative harmonic analysis.
"""

import sympy as sp

from aeg_shakespeare.families import (
    FamilyAction,
    ProcessCharacter,
    ProcessFamily,
    character_invariance_residual,
    transport_process_character,
    verify_family_action,
    verify_process_character,
)


def test_scale_action_moves_translation_character_label_and_breaks_invariance():
    a, c = sp.symbols("a c", positive=True, real=True)
    b, d, xi = sp.symbols("b d xi", real=True)

    translation = ProcessFamily(
        "T",
        lambda left, right: sp.expand(left + right),
        identity=sp.S.Zero,
    )
    dilation = ProcessFamily(
        "S",
        lambda left, right: sp.expand(left * right),
        identity=sp.S.One,
    )
    action = FamilyAction(
        dilation,
        translation,
        lambda scale, shift: sp.expand(scale * shift),
        name="dilation_on_translation",
    )

    action_certificate = verify_family_action(
        action,
        acting_parameters=(a,),
        acting_pairs=((a, c),),
        target_parameters=(b,),
        target_pairs=((b, d),),
    )
    assert action_certificate.exact

    character = ProcessCharacter(
        translation,
        lambda shift: sp.exp(sp.I * xi * shift),
        label=xi,
    )
    transported = transport_process_character(character, action, a)
    assert verify_process_character(transported, ((b, d),)).exact
    assert sp.simplify(
        transported.value(b) - sp.exp(sp.I * (a * xi) * b)
    ) == 0

    obstruction = character_invariance_residual(character, action, a, b)
    assert obstruction != 0
    assert sp.simplify(obstruction.subs(xi, 0)) == 0
    assert sp.simplify(obstruction.subs({a: 1})) == 0
