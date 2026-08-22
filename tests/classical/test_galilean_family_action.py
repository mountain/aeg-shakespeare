"""Galilean I: a mechanics acceptance test for finite process families and actions.

Question
--------
Does the finite-family API survive a genuinely mechanical example whose target
family has a multidimensional parameter space and whose family action is a
shear rather than a scalar rescaling?

Primitive data
--------------
Use spacetime translations

    N_(a,s): (x,t) -> (x+a, t+s)

with composition

    (a,s) + (b,r) = (a+b, s+r),

and Galilean boosts

    B_v: (x,t) -> (x+v t, t)

with additive velocity parameters.  Their finite conjugation law induces the
parameter action

    (a,s) -> (a + v s, s).

No momentum, energy, mass, Hamiltonian, Poisson bracket, projective
representation, or central extension is supplied.

Shakespeare reconstruction
---------------------------
``ProcessFamily`` represents both the two-parameter translation family and the
one-parameter boost family.  ``FamilyAction`` represents the shear on spacetime
translation parameters without any special Galilei-group class.

A translation character

    chi_(p,E)(a,s) = exp(i (p a - E s))

is then transported by the boost action.  The induced scalar response is

    exp(i (p a - (E - v p) s)),

so the response labels transform by the bare dual shear

    (p,E) -> (p, E - v p).

This is an API acceptance result only.  The missing physical mass term is kept
visible as the next mathematical pressure rather than patched into the family
action abstraction.

Calibration statement
---------------------
Passing this file certifies that the same ``ProcessFamily``, ``ProcessCharacter``
and ``FamilyAction`` abstractions handle a two-dimensional parameter family and
a nontrivial mechanics shear without modification.

New reusable abstraction
-------------------------
None.

Unresolved manual choice
------------------------
The bare spacetime action does not recover the mass-dependent Galilean
energy-momentum transformation.  A later vignette must decide whether the
missing information is best represented as a central residual/cocycle; this file
deliberately does not add such an API.

Boundary
--------
This is not the full Galilei representation theory and does not derive the free
particle dispersion relation.
"""

import sympy as sp

from aeg_shakespeare.process.finite import (
    FamilyAction,
    ProcessCharacter,
    ProcessFamily,
    transport_process_character,
    verify_family_action,
    verify_process_character,
)


def _pair_add(left, right):
    return (sp.expand(left[0] + right[0]), sp.expand(left[1] + right[1]))


def test_galilean_boost_shears_spacetime_translation_characters():
    a, b, s, r = sp.symbols("a b s r", real=True)
    v, w = sp.symbols("v w", real=True)
    p, E = sp.symbols("p E", real=True)

    translations = ProcessFamily(
        "N",
        _pair_add,
        identity=(sp.S.Zero, sp.S.Zero),
    )
    boosts = ProcessFamily(
        "B",
        lambda left, right: sp.expand(left + right),
        identity=sp.S.Zero,
    )
    boost_action = FamilyAction(
        boosts,
        translations,
        lambda velocity, parameter: (
            sp.expand(parameter[0] + velocity * parameter[1]),
            parameter[1],
        ),
        name="boost_on_spacetime_translation",
    )

    action_certificate = verify_family_action(
        boost_action,
        acting_parameters=(v,),
        acting_pairs=((v, w),),
        target_parameters=((a, s),),
        target_pairs=(((a, s), (b, r)),),
    )
    assert action_certificate.exact

    character = ProcessCharacter(
        translations,
        lambda parameter: sp.exp(
            sp.I * (p * parameter[0] - E * parameter[1])
        ),
        label=(p, E),
    )
    assert verify_process_character(
        character,
        (((a, s), (b, r)),),
    ).exact

    transported = transport_process_character(character, boost_action, v)
    expected = sp.exp(sp.I * (p * a - (E - v * p) * s))
    assert sp.simplify(transported.value((a, s)) - expected) == 0
