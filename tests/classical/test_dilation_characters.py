"""Dilation I: the same character API survives a multiplicative parameter law.

Question
--------
Does the finite-family abstraction genuinely describe the process law rather
than secretly assuming additive parameters?

Primitive data
--------------
The family law is

    S_a S_b = S_{ab},   a,b>0.

No logarithmic coordinate, Mellin transform, Fourier transform, or spectral
measure is part of the API input.

Shakespeare reconstruction
---------------------------
The same ``ProcessFamily`` and ``ProcessCharacter`` objects used for Translation
I are reused unchanged.  The multiplicative character candidate is

    eta_tau(a) = exp(i tau log a).

The backend simplifier is told that the scale parameters are positive, so the
functional equation is certified exactly.  Only afterward do we recognize
``a^(i tau)`` as the classical Mellin character and ``u=log(a)`` as its additive
shadow.

Calibration statement
---------------------
Passing this file certifies that no second family/character API is needed for
multiplicative composition.

New reusable abstraction
-------------------------
None.

Unresolved manual choice
------------------------
The logarithmic/exponential realization is still supplied; Mellin synthesis and
measure remain outside the current API.

Boundary
--------
This is a multiplicative character calibration, not a Mellin transform engine.
"""

import sympy as sp

from process_geometry.process.finite import (
    ProcessCharacter,
    ProcessFamily,
    verify_process_character,
)


def _mellin_simplify(expr):
    return sp.simplify(sp.expand_log(sp.sympify(expr), force=True))


def test_dilation_reuses_translation_character_api():
    a, b, tau = sp.symbols("a b tau", positive=True, real=True)
    dilation = ProcessFamily(
        "S",
        lambda left, right: sp.expand(left * right),
        identity=sp.S.One,
    )

    character = ProcessCharacter(
        dilation,
        lambda scale: sp.exp(sp.I * tau * sp.log(scale)),
        label=tau,
        simplify=_mellin_simplify,
    )
    certificate = verify_process_character(character, ((a, b),))
    assert certificate.exact

    # Classical shadow: log reparameterization turns the response into an
    # ordinary additive exponential without changing the public family API.
    u = sp.Symbol("u", real=True)
    assert sp.simplify(
        character.value(sp.exp(u)) - sp.exp(sp.I * tau * u)
    ) == 0
