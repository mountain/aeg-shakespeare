"""Galilean IV: the mass residual has a finite process-cocycle realization.

Question
--------
Magnetic translations expose their hidden central information directly as a
finite 2-cocycle, while Galilean II/III first exposed mass through an affine
response correction and the generator bracket ``{K,P}=m``.  Can the Galilean
organism use the same minimal ``ProcessCocycle`` abstraction without copying the
magnetic formula?

Primitive data
--------------
Use the one-dimensional Galilei family with parameters ``g=(x,v,t)`` and the
finite composition convention

    (x1,v1,t1) * (x2,v2,t2)
      = (x1+x2+v1*t2, v1+v2, t1+t2).

A standard representative of the mass central-extension class is

    omega(g1,g2)
      = m (v1*x2 + (1/2) t2*v1^2).

Equivalent conventions may differ by a coboundary.  This vignette fixes the
above representative and tests only the cocycle/central-residual structure.

Shakespeare reconstruction
---------------------------
``ProcessFamily`` carries the visible Galilei composition.  ``ProcessCocycle``
carries the additional additive central term.  The generic verifier checks the
2-cocycle identity symbolically.

For a pure boost ``B_u=(0,u,0)`` and a pure spatial translation
``T_a=(a,0,0)``, the visible family elements commute, but their lifted
compositions differ centrally by

    omega(B_u,T_a) - omega(T_a,B_u) = m u a.

Taking the mixed infinitesimal derivative at the identity gives exactly ``m``,
matching the central generator residual ``{K,P}=m`` found independently in
Galilean III.

Calibration statement
---------------------
Passing this file certifies that the same finite ``ProcessCocycle`` abstraction
used for magnetic translations also represents the Galilean mass extension,
while preserving the distinct physical realization and cocycle formula.

Boundary
--------
This does not construct the full Bargmann group API, quotient cocycles by
coboundaries, or introduce projective/unitary representations.  The finite
cocycle is one calibrated realization over the already-frozen ``ProcessFamily``.

References
----------
[Bargmann-1954] V. Bargmann, "On Unitary Ray Representations of Continuous
Groups", *Annals of Mathematics* 59 (1954), 1-46.
"""

import sympy as sp

from process_geometry.process.finite import (
    ProcessCocycle,
    ProcessFamily,
    central_commutator_residual,
    verify_process_cocycle,
)


def _galilei_compose(left, right):
    x_left, v_left, t_left = left
    x_right, v_right, t_right = right
    return (
        sp.expand(x_left + x_right + v_left * t_right),
        sp.expand(v_left + v_right),
        sp.expand(t_left + t_right),
    )


def test_galilean_mass_is_finite_cocycle_and_infinitesimal_central_residual():
    x1, v1, t1, x2, v2, t2, x3, v3, t3 = sp.symbols(
        "x1 v1 t1 x2 v2 t2 x3 v3 t3",
        real=True,
    )
    u, a, mass = sp.symbols("u a m", real=True)

    family = ProcessFamily(
        "Galilei1D",
        _galilei_compose,
        identity=(sp.S.Zero, sp.S.Zero, sp.S.Zero),
    )
    cocycle = ProcessCocycle(
        family,
        lambda left, right: sp.expand(
            mass
            * (
                left[1] * right[0]
                + sp.Rational(1, 2) * right[2] * left[1] ** 2
            )
        ),
        label="mass Bargmann cocycle",
    )

    g1 = (x1, v1, t1)
    g2 = (x2, v2, t2)
    g3 = (x3, v3, t3)
    certificate = verify_process_cocycle(
        cocycle,
        ((g1, g2, g3),),
        normalization_parameters=(g1,),
    )
    assert certificate.exact

    boost = (sp.S.Zero, u, sp.S.Zero)
    translation = (a, sp.S.Zero, sp.S.Zero)
    assert family.parameters_equivalent(
        family.compose_parameters(boost, translation),
        family.compose_parameters(translation, boost),
    )

    central = central_commutator_residual(cocycle, boost, translation)
    assert sp.simplify(central - mass * u * a) == 0

    infinitesimal = sp.diff(sp.diff(central, u), a).subs({u: 0, a: 0})
    assert sp.simplify(infinitesimal - mass) == 0

    lifted_bt = cocycle.compose_lifted((boost, sp.S.Zero), (translation, sp.S.Zero))
    lifted_tb = cocycle.compose_lifted((translation, sp.S.Zero), (boost, sp.S.Zero))
    assert family.parameters_equivalent(lifted_bt[0], lifted_tb[0])
    assert sp.simplify(lifted_bt[1] - lifted_tb[1] - mass * u * a) == 0
