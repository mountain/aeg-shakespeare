"""Pendulum III: an explicit lifted cycle produces the first computed period.

Question
--------
The preceding pendulum vignettes reached a genus-one quotient and identified its
canonical differential.  Can we now compute an actual period from an explicit
closed lifted history, rather than inferring the lattice only from genus and
algebraic invariants?

Primitive data
--------------
At the symmetric energy E=0 the reduced pendulum curve is

    Y^2 = 2 U (U^2 - 1),

and its holomorphic differential is

    omega = dU / Y.

We supply only a sampled ellipse in the U-plane enclosing the two branch points
-1 and 0.  The sheet of Y is *not* prescribed along the contour; it is produced
by ``lift_square_root_path`` through continuation.

Classical lineage
-----------------
Periods of elliptic differentials are integrals over closed cycles on the
associated Riemann surface.  Cutting and gluing the two square-root sheets turns
a loop around two branch points into a closed lifted cycle.  For the lemniscatic
case the second period is an i-multiple of the first and the normalized period
ratio is tau=i.  See [DLMF-19], [DLMF-23.5], [Forster-1981], and
[Whittaker-Watson-1927].

The real cut integral used for an independent numerical check is

    2 int_{-1}^0 dU / sqrt(2 U (U^2-1))
      = B(1/4,1/2) / sqrt(2),

obtained by U=-t followed by s=t^2; this beta reduction is derived in the essay
rather than imported as the definition of the period.

Shakespeare reconstruction
---------------------------
The visible base contour returns to its initial U.  The period engine first asks
whether the *lifted* square-root history closes.  Only after that topological
check does it integrate the differential along the lifted path.

**Shakespeare interpretation.**  The resulting nonzero integral is a numerical
measurement of history residue after the quotient state closes.  Classical
mathematics calls it a period; 'history residue' is the project language.

Calibration statement
---------------------
For the chosen E=0 normalization and contour, the test certifies numerically:

1. the ellipse around {-1,0} has sheet multiplier +1 and hence closes upstairs;
2. integrating dU/Y around that lift converges under refinement;
3. its value agrees with B(1/4,1/2)/sqrt(2);
4. the exact automorphism (U,Y)->(-U,iY) supplies the independent period
   omega_b=i*omega_a, so the packaged genus-one lattice has tau=i and positive
   oriented area.

Proof map
---------
``test_pendulum_cut_contour_closes_on_the_lift`` checks item 1.
``test_pendulum_period_converges_to_beta_value`` checks items 2-3.
``test_lemniscatic_symmetry_packages_square_lattice`` checks item 4.

Boundary
--------
This is still not an automatic homology-basis finder.  The ellipse is chosen by
the test, and the second period is obtained from a proved algebraic symmetry
rather than a second independently discovered cycle.  The trapezoidal contour
integral has empirical refinement control, not a rigorous interval bound.

References
----------
[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
“Elliptic Integrals”, https://dlmf.nist.gov/19 .

[DLMF-23.5] NIST DLMF, §23.5, “Special Lattices”, especially the lemniscatic
case, https://dlmf.nist.gov/23.5 .

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson,
*A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927,
Chapters XX-XXII.
"""

import math

import sympy as sp

from process_geometry.analysis.abelian import (
    GenusOneLattice,
    holomorphic_differential_basis,
    integrate_lifted_differential,
    lift_square_root_path,
)
from process_geometry.analysis.algebraic import hyperelliptic_profile


def pendulum_e0_curve():
    U, Y = sp.symbols("U Y")
    return hyperelliptic_profile(U, Y, 2 * U * (U**2 - 1))


def cut_ellipse(samples: int):
    # Enclose -1 and 0, but not +1, while staying away from all branch points.
    return tuple(
        -0.5
        + 0.6 * math.cos(2 * math.pi * index / samples)
        + 0.25j * math.sin(2 * math.pi * index / samples)
        for index in range(samples + 1)
    )


def contour_period(samples: int) -> complex:
    curve = pendulum_e0_curve()
    omega = holomorphic_differential_basis(curve)[0]
    lifted = lift_square_root_path(curve, cut_ellipse(samples))
    assert lifted.lifted_closed
    return integrate_lifted_differential(lifted, omega)


def test_pendulum_cut_contour_closes_on_the_lift():
    curve = pendulum_e0_curve()
    lifted = lift_square_root_path(curve, cut_ellipse(768))

    assert lifted.base_closed
    assert lifted.lifted_closed
    assert lifted.sheet_multiplier == 1


def test_pendulum_period_converges_to_beta_value():
    coarse = contour_period(1024)
    fine = contour_period(2048)
    expected = complex(sp.N(sp.beta(sp.Rational(1, 4), sp.Rational(1, 2)) / sp.sqrt(2), 30))

    # Refinement improves the contour quadrature, and the fine value agrees with
    # the independently reduced real beta integral.
    assert abs(fine - coarse) < 2e-5
    assert abs(fine - expected) < 1e-5
    assert abs(fine.imag) < 1e-8
    assert fine.real > 0


def test_lemniscatic_symmetry_packages_square_lattice():
    omega_a = contour_period(2048)

    # From (U,Y)->(-U,iY), the differential dU/Y transforms to i*dU/Y.
    omega_b = 1j * omega_a
    lattice = GenusOneLattice(omega_a=omega_a, omega_b=omega_b)

    assert abs(lattice.tau - 1j) < 1e-12
    assert lattice.oriented_area > 0
