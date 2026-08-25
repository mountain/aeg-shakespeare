"""Translation I: commuting finite histories force a character equation before Fourier language.

Question
--------
Can a one-parameter translation process family and its scalar multiplicative
responses be expressed without introducing Fourier transforms, spectra, or a
general representation hierarchy?

Primitive data
--------------
The finite family has the parameter law

    T_a T_b = T_{a+b}.

The test supplies the family law and a symbolic scalar-response candidate.  It
does not supply a Fourier transform, an orthogonal basis, a spectral theorem, or
a completeness measure.

Shakespeare reconstruction
---------------------------
``ProcessFamily`` stores only parameter composition. ``ProcessCharacter`` asks
whether a scalar response turns that composition into multiplication.  For the
continuous realization

    chi_xi(a) = exp(i xi a),

the exact symbolic residual

    chi_xi(a+b) - chi_xi(a) chi_xi(b)

vanishes.  Only after the process law and response law are certified do we name
this familiar realization an additive character; Fourier synthesis is outside
this vignette.

Calibration statement
---------------------
Passing this file certifies that the new finite-family API represents additive
translation histories and verifies their exponential scalar characters without
requiring a Fourier API.

New reusable abstraction
-------------------------
``ProcessFamily`` and ``ProcessCharacter`` only.

Unresolved manual choice
------------------------
The exponential realization is still supplied.  Shakespeare does not yet search
all regular solutions of the character functional equation, nor does it define
measure/completeness needed for Fourier synthesis.

Boundary
--------
This is character verification, not Fourier analysis.
"""

import sympy as sp

from process_geometry.process.finite import (
    ProcessCharacter,
    ProcessFamily,
    verify_process_character,
)


def test_translation_family_character_before_fourier():
    a, b, xi = sp.symbols("a b xi", real=True)
    translation = ProcessFamily(
        "T",
        lambda left, right: sp.expand(left + right),
        identity=sp.S.Zero,
    )

    assert sp.expand(translation.compose_parameters(a, b) - (a + b)) == 0
    assert sp.expand(translation.fold_parameters((a, b, -a)) - b) == 0

    character = ProcessCharacter(
        translation,
        lambda shift: sp.exp(sp.I * xi * shift),
        label=xi,
    )
    certificate = verify_process_character(character, ((a, b),))
    assert certificate.exact

    # Classical shadow: the infinitesimal response is multiplication by i*xi.
    t = sp.Symbol("t", real=True)
    response = character.value(t)
    assert sp.simplify(sp.diff(response, t) - sp.I * xi * response) == 0
