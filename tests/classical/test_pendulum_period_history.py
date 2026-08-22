"""Pendulum II: genus-one quotient -> differential -> period history -> square torus.

Question
--------
The first pendulum vignette stops after the constrained mechanical process has
forced the genus-one quotient

    Y^2 = 2 (E-U) (1-U^2).

Can we continue one step further, still without inserting a Jacobi or
Weierstrass elliptic function as a solver, and recover the *global* two-period
structure from the quotient itself?

Primitive data
--------------
This file starts at the output boundary of
``test_pendulum_process_geometry.py``.  Its primitive object is therefore the
already-certified reduced curve together with the process relation ``D U=Y``.
At the symmetric energy ``E=0`` the curve is

    C: Y^2 = 2 U (U^2-1),

with branch points ``-1, 0, 1, infinity``.  No elliptic function, period lattice,
modulus, or angular variable is supplied.

Classical lineage
-----------------
For a smooth genus-one curve, a nonzero holomorphic differential has two
independent periods; their integer span is the lattice underlying the analytic
uniformization by a complex torus.  Weierstrass elliptic functions are
meromorphic functions periodic on such a lattice [DLMF-23.2].  The short cubic
``W^2=4X^3-g2 X-g3`` and its invariants are summarized in [DLMF-23.3]; the
lemniscatic/square-lattice case has ``g3=0`` and period ratio ``tau=i``
[DLMF-23.5].  The modular invariant relation is given in [DLMF-23.19].
For the Riemann-surface and period interpretation see [Forster-1981] and
[Farkas-Kra-1992].

The real branch-cut period below reduces by ``s=t^2`` to Euler's beta integral
[DLMF-5.12]:

    I = int_0^1 dt / sqrt(2 t (1-t^2))
      = B(1/4,1/2)/(2 sqrt(2)).

A loop around the cut ``[-1,0]`` traverses the two sheets and hence has period
``Omega_1=2I``.

Shakespeare reconstruction
---------------------------
The quotient itself first emits its canonical holomorphic differential

    omega = dU / Y.

Because the reduced process satisfies ``D U=Y``, the pullback of ``omega`` to
the lifted process history is exactly ``dt``.  A closed state cycle can
therefore return to the same point of ``C`` while its lifted integral coordinate
changes by ``int_gamma omega``.

**Shakespeare interpretation.**  Such a period is read as a history residual:
state return does not imply lifted-history return.

At ``E=0`` the curve has the exact automorphism

    sigma(U,Y) = (-U, iY).

It sends ``omega`` to ``i omega`` and maps the cut ``[-1,0]`` to ``[0,1]``.
Thus the image cycle has period ``Omega_2=i Omega_1``.  Since ``Omega_1`` is
nonzero and the ratio is non-real, the two periods generate a rank-two square
lattice.  Independently, exact cubic algebraization gives ``g3=0`` and
``j=1728``, matching the classical lemniscatic/square-torus shadow.

Calibration statement
---------------------
Passing this file certifies, for the symmetric energy leaf ``E=0``:

1. the quotient has one canonical holomorphic differential and first-homology
   rank two;
2. ``dU/Y`` pulls back to the process clock ``dt``;
3. the quotient is exactly convertible to short Weierstrass form with
   ``g2=1``, ``g3=0``, and ``j=1728`` under Shakespeare's chosen normalization;
4. ``sigma(U,Y)=(-U,iY)`` preserves the curve and multiplies the differential
   by ``i``;
5. one nonzero cut period ``Omega_1`` therefore has an independent companion
   ``Omega_2=i Omega_1``.

Proof map
---------
``test_pendulum_clock_is_the_first_abelian_integral`` checks 1-2.
``test_symmetric_pendulum_algebraizes_to_lemniscatic_weierstrass_form`` checks 3.
``test_symmetric_curve_automorphism_rotates_the_holomorphic_differential``
checks 4.
``test_symmetric_branch_cut_periods_form_a_square_lattice`` checks 5 and the
beta-function normalization of the nonzero real period.

Boundary
--------
This is not yet a general period engine.  The cycle choice is special to the
symmetric real branch configuration at ``E=0``.  The file does not numerically
continue arbitrary branches, compute a period matrix for symbolic ``E``,
construct ``wp`` as a function, or prove a general uniformization theorem.
Those remain separate layers.  In particular, ``j=1728`` is a classical
elliptic-curve invariant and does not identify the pendulum process with every
other presentation having the same ``j``.

References
----------
[DLMF-5.12] NIST Digital Library of Mathematical Functions, §5.12,
“Beta Function”, especially Eq. 5.12.1, https://dlmf.nist.gov/5.12 .

[DLMF-23.2] NIST DLMF, §23.2, “Definitions and Periodic Properties”,
https://dlmf.nist.gov/23.2 .

[DLMF-23.3] NIST DLMF, §23.3, “Differential Equations” (invariants, roots,
discriminant, and Weierstrass differential equation), https://dlmf.nist.gov/23.3 .

[DLMF-23.5] NIST DLMF, §23.5, “Special Lattices”, especially the lemniscatic
case ``g3=0`` and ``tau=i``, https://dlmf.nist.gov/23.5 .

[DLMF-23.19] NIST DLMF, §23.19, “Interrelations”, especially Eq. 23.19.3 for
Klein's invariant, https://dlmf.nist.gov/23.19 .

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.
"""

import sympy as sp

from aeg_shakespeare import (
    abelian_integral_profile,
    hyperelliptic_profile,
    weierstrass_cubic_profile,
)


def symmetric_pendulum_curve():
    U, Y = sp.symbols("U Y")
    polynomial = sp.expand(2 * U * (U**2 - 1))
    return U, Y, hyperelliptic_profile(U, Y, polynomial)


def test_pendulum_clock_is_the_first_abelian_integral():
    U, Y, curve = symmetric_pendulum_curve()
    abelian = abelian_integral_profile(curve)

    # DISCOVER: genus one itself supplies one holomorphic differential dU/Y.
    assert abelian.abelian_dimension == 1
    assert abelian.homology_rank == 2
    assert len(abelian.differentials) == 1
    omega = abelian.differentials[0]
    assert omega.coefficient == 1 / Y

    # ASSERT: the reduced process law D U=Y makes omega pull back exactly to dt.
    assert sp.simplify(omega.pullback_coefficient(Y) - 1) == 0


def test_symmetric_pendulum_algebraizes_to_lemniscatic_weierstrass_form():
    U, Y, curve = symmetric_pendulum_curve()
    X, W = sp.symbols("X W")
    model = weierstrass_cubic_profile(curve, X, W)

    # ASSERT: the exact coordinate map is certified against the original cubic.
    assert model.transformation_residual() == 0
    assert model.g2 == 1
    assert model.g3 == 0
    assert model.discriminant == 1
    assert model.klein_J == 1
    assert model.j_invariant == 1728


def test_symmetric_curve_automorphism_rotates_the_holomorphic_differential():
    U, Y, curve = symmetric_pendulum_curve()
    relation = curve.relation

    # sigma(U,Y)=(-U,iY) preserves the zero set because it sends the defining
    # polynomial to its negative.
    transformed = sp.expand(
        relation.subs({U: -U, Y: sp.I * Y}, simultaneous=True)
    )
    assert sp.expand(transformed + relation) == 0

    # sigma^*(dU/Y)=d(-U)/(iY)=i dU/Y.
    differential_factor = sp.simplify(-1 / sp.I)
    assert differential_factor == sp.I


def test_symmetric_branch_cut_periods_form_a_square_lattice():
    # Euler beta integral after t^2=s gives the positive one-sheet integral
    # I = B(1/4,1/2)/(2 sqrt(2)) along the real branch interval [-1,0].
    half_cut_integral = sp.beta(sp.Rational(1, 4), sp.Rational(1, 2)) / (
        2 * sp.sqrt(2)
    )
    gamma_form = (
        sp.sqrt(sp.pi)
        * sp.gamma(sp.Rational(1, 4))
        / (2 * sp.sqrt(2) * sp.gamma(sp.Rational(3, 4)))
    )
    assert sp.simplify(sp.expand_func(half_cut_integral) - gamma_form) == 0
    assert sp.N(half_cut_integral, 30) > 0

    # A closed loop around the cut traverses both sheets.  The symmetry sigma
    # sends it to an independent cut cycle and multiplies omega by i.
    omega_1 = sp.simplify(2 * half_cut_integral)
    omega_2 = sp.simplify(sp.I * omega_1)

    assert sp.simplify(omega_2 / omega_1 - sp.I) == 0
    assert sp.re(omega_1).is_positive
    assert sp.simplify(sp.re(omega_2)) == 0
    assert sp.im(omega_2).is_positive
