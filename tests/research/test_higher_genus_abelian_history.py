"""Higher genus: quotient complexity -> multi-component Abelian history coordinates.

Question
--------
The even-power oscillator calibration already shows that

    D x = p,
    D p = -x^(m-1),

with energy ``H=p^2/2+x^m/m`` produces hyperelliptic energy curves whose
generic genus rises from 0 to 1 to 2 for ``m=2,4,6``.  What new structure is
forced when the sextic case reaches genus two?

Primitive data
--------------
This vignette begins from the already-reduced sextic energy curve

    C_E: y^2 = 2E - x^6/3,

and the reduced process law ``D x = y``.  No theta functions, period matrix,
Jacobian coordinates, or Abelian-function inversion formula is supplied.

Classical lineage
-----------------
For a smooth hyperelliptic curve of genus ``g``, the space of holomorphic
one-forms has dimension ``g`` and in the affine model ``y^2=P(x)`` admits the
standard basis

    dx/y, x dx/y, ..., x^(g-1) dx/y.

The first homology has rank ``2g``.  Integrating a holomorphic basis over a
homology basis produces the period matrix entering the Jacobian
``C^g / Lambda``.  See [Forster-1981], [Farkas-Kra-1992], and the explicit
hyperelliptic canonical-form discussion in [McMullen-Riemann-Surfaces].
Classically, the need to invert several Abelian integrals rather than one is the
higher-genus successor to elliptic inversion; see [Baker-1897] and
[Mumford-1983].

Shakespeare reconstruction
---------------------------
The program does not insert a Jacobian because the equation has degree six.
Instead the algebraic quotient first reports genus two.  Only then does the
common Abelian layer emit two canonical differentials,

    omega_0 = dx/y,
    omega_1 = x dx/y,

and the topological period rank four.  Pulling them back along the actual
reduced process ``D x=y`` gives

    (omega_0, omega_1) -> (1, x) dt.

**Shakespeare interpretation.**  A single algebraic state curve can therefore
force a *vector* of natural lifted-history coordinates.  This is a precise
place where enlarging representation dimension becomes mathematically natural,
but the present test does not yet claim that the resulting two coordinates
linearize the physical flow.

Calibration statement
---------------------
Passing this file certifies:

1. the sextic energy quotient is generically genus two;
2. its canonical holomorphic differential space has dimension two;
3. the associated first-homology rank is four;
4. the process pullback of the canonical basis is exactly ``(1,x) dt``;
5. the quartic predecessor has dimension one/rank two, so the increase is tied
   to quotient genus rather than to a hard-coded function name.

Proof map
---------
``test_sextic_quotient_forces_two_holomorphic_history_channels`` checks 1-4.
``test_quartic_to_sextic_rank_raising_is_emitted_by_quotient_geometry`` checks
5 and makes the comparison explicit.

Boundary
--------
This file does not construct a symplectic homology basis, compute a genus-two
period matrix, prove Riemann bilinear relations, build the Jacobian, or solve a
Jacobi inversion problem.  In particular, ``abelian_dimension=2`` is not by
itself evidence that an arbitrary two-dimensional state enlargement is optimal
for a Shakespeare task.  It is the classical differential dimension forced by
the quotient geometry.

References
----------
[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.

[McMullen-Riemann-Surfaces] C. McMullen, *Riemann Surfaces*, Harvard Math 213b
course notes, discussion of hyperelliptic curves and the basis
``x^i dx/y``, https://abel.math.harvard.edu/~ctm/math213b/home/course/course.pdf .

[Baker-1897] H. F. Baker, *Abel's Theorem and the Allied Theory Including the
Theory of the Theta Functions*, Cambridge University Press, 1897.

[Mumford-1983] D. Mumford, *Tata Lectures on Theta I*, Birkhaeuser, 1983.
DOI: 10.1007/978-1-4899-2843-6.
"""

import sympy as sp

from aeg_shakespeare import abelian_integral_profile, hyperelliptic_profile


def oscillator_curve(power: int):
    x, y, E = sp.symbols("x y E")
    polynomial = sp.expand(2 * E - sp.Rational(2, power) * x**power)
    return x, y, E, hyperelliptic_profile(x, y, polynomial)


def test_sextic_quotient_forces_two_holomorphic_history_channels():
    x, y, E, curve = oscillator_curve(6)
    profile = abelian_integral_profile(curve)

    assert curve.generic_genus == 2
    assert profile.abelian_dimension == 2
    assert profile.homology_rank == 4
    assert [d.power for d in profile.differentials] == [0, 1]
    assert [d.coefficient for d in profile.differentials] == [1 / y, x / y]

    # The physical reduced process is D x=y on the energy curve.
    assert profile.pullback_coefficients(y) == (1, x)


def test_quartic_to_sextic_rank_raising_is_emitted_by_quotient_geometry():
    x4, y4, E4, quartic = oscillator_curve(4)
    x6, y6, E6, sextic = oscillator_curve(6)

    p4 = abelian_integral_profile(quartic)
    p6 = abelian_integral_profile(sextic)

    assert (p4.abelian_dimension, p4.homology_rank) == (1, 2)
    assert (p6.abelian_dimension, p6.homology_rank) == (2, 4)
    assert p4.pullback_coefficients(y4) == (1,)
    assert p6.pullback_coefficients(y6) == (1, x6)
