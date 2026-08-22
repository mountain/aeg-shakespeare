"""Galilean II: bare character pullback cannot generate the mass-dependent affine shift.

Question
--------
Galilean I showed that the frozen finite-family API transports spacetime
translation characters by the bare dual shear.  Can that same pullback mechanism
also generate the mass-dependent Galilean energy-momentum shift, or is there a
structural obstruction?

Primitive data
--------------
Use the already-frozen spacetime translation family

    N_(a,s) N_(b,r) = N_(a+b,s+r)

and the boost action

    (a,s) -> (a+v s,s).

A scalar translation character is

    chi_(p,E)(a,s) = exp(i (p a - E s)).

No Hamiltonian, Poisson bracket, central extension, projective representation,
or cocycle is supplied.

Shakespeare reconstruction
---------------------------
``transport_process_character`` is pullback along the target-family parameter
action.  Therefore the trivial character ``chi=1`` must remain trivial under
every family action.  Equivalently, the origin of scalar character-label space
is fixed by bare pullback.

For the Galilean shear the transported response is

    exp(i (p a - (E-v p) s)),

so the bare label action is

    (p,E) -> (p,E-v p).

This is homogeneous in the original labels and fixes ``(0,0)``.  By contrast,
the familiar massive Galilean boost law contains an affine mass-dependent shift
and moves a rest state away from the origin.  Hence that information cannot be
manufactured by ordinary character pullback alone.

Calibration statement
---------------------
Passing this file certifies an API-level obstruction only:

1. the frozen family/character API reproduces the bare dual shear exactly;
2. the trivial character is invariant under every pullback transport;
3. consequently no nonzero additive label shift can arise from this mechanism
   without extra structure.

New reusable abstraction
-------------------------
None.

Unresolved manual choice
------------------------
The missing structure is not named here.  Galilean III will ask whether a
Hamiltonian realization exposes the same missing information as a central
residual before any cocycle abstraction is promoted.

Boundary
--------
This vignette does not derive the physical massive boost law.  It proves only
that the frozen scalar-character pullback mechanism cannot by itself create an
affine shift of the zero character.

References
----------
[Bargmann-1954] V. Bargmann, "On Unitary Ray Representations of Continuous
Groups", Annals of Mathematics 59(1), 1954, 1-46.
"""

import sympy as sp

from aeg_shakespeare import (
    FamilyAction,
    ProcessCharacter,
    ProcessFamily,
    transport_process_character,
)


def _pair_add(left, right):
    return (sp.expand(left[0] + right[0]), sp.expand(left[1] + right[1]))


def test_bare_character_pullback_fixes_zero_label_and_cannot_create_mass_shift():
    a, s, v = sp.symbols("a s v", real=True)
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

    character = ProcessCharacter(
        translations,
        lambda parameter: sp.exp(
            sp.I * (p * parameter[0] - E * parameter[1])
        ),
        label=(p, E),
    )
    transported = transport_process_character(character, boost_action, v)
    expected = sp.exp(sp.I * (p * a - (E - v * p) * s))
    assert sp.simplify(transported.value((a, s)) - expected) == 0

    # Pullback transport is homogeneous in the character labels: the zero label
    # remains the trivial character and cannot acquire a mass-dependent offset.
    trivial = ProcessCharacter(
        translations,
        lambda _parameter: sp.S.One,
        label=(sp.S.Zero, sp.S.Zero),
    )
    transported_trivial = transport_process_character(trivial, boost_action, v)
    assert sp.simplify(transported_trivial.value((a, s)) - 1) == 0

    bare_label = (p, sp.expand(E - v * p))
    assert tuple(sp.simplify(item.subs({p: 0, E: 0})) for item in bare_label) == (0, 0)
