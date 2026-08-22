"""Cross calibration: distinct primitive processes, the same generic genus.

Question
--------
Does Shakespeare have an executable cross-problem observable that can reveal a
shared quotient class without declaring the two physical systems to be the same
problem or importing the same named solution?

Primitive data
--------------
This file does not reconstruct the two systems from scratch; those derivations
live in the cited classical tests.  It receives only their already-certified
reduced algebraic relations:

Pendulum:
    Y^2 = 2(E-X)(1-X^2).

Quartic oscillator:
    Y^2 = 2E - X^4/2.

No elliptic-function formula, period lattice, j-invariant, or explicit
birational map is supplied.

Classical lineage
-----------------
Smooth projective curves represented by square-free cubic or quartic
hyperelliptic equations have genus one; genus-one curves underlie the classical
elliptic-function theory.  See [Forster-1981], [Silverman-2009],
[DLMF-19], and [DLMF-23].

Shakespeare reconstruction
---------------------------
The two reductions arise from different primitive processes and have different
branch polynomials and degeneration loci.  We therefore do not identify their
equations.  Instead we ask whether a common structural observable computed by
the same public routine places both generic quotients in genus one.

**Shakespeare interpretation.**  This is the first small executable instance of

    different primitive processes
        -> different quotient presentations
        -> same coarse quotient-geometry class.

It is evidence for pursuing process-normal-form/universality questions, not a
proof of such a theorem.

Calibration statement
---------------------
Passing this file certifies only that:

1. the pendulum reduction is cubic and generically genus one;
2. the quartic-oscillator reduction is quartic and generically genus one;
3. their discriminants differ, so this test is not comparing identical
   polynomial presentations;
4. genus can be computed by one problem-independent profiler across both tests.

Proof map
---------
``test_pendulum_and_quartic_*`` checks degree, generic genus, and distinct
branch-discriminant families.  ``test_genus_is_*`` checks that genus is used as
one common structural observable rather than a problem label.

Boundary
--------
Equal genus does not imply isomorphism, birational equivalence over a specified
base field, equality of period lattices, equality of j-invariants, dynamical
conjugacy, or a universal Shakespeare normal form.  Any such stronger statement
requires additional invariants and separate tests.

References
----------
[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
“Elliptic Integrals”, https://dlmf.nist.gov/19 .

[DLMF-23] NIST Digital Library of Mathematical Functions, Chapter 23,
“Weierstrass Elliptic and Modular Functions”, https://dlmf.nist.gov/23 .

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Silverman-2009] J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed.,
Springer, 2009. DOI: 10.1007/978-0-387-09494-6.
"""

import sympy as sp

from aeg_shakespeare import hyperelliptic_profile


def test_pendulum_and_quartic_oscillator_share_genus_one_quotient_class():
    E, X, Y = sp.symbols("E X Y")

    # GIVEN: two independently derived quotient equations.
    pendulum = hyperelliptic_profile(
        X,
        Y,
        2 * (E - X) * (1 - X**2),
    )
    quartic = hyperelliptic_profile(
        X,
        Y,
        2 * E - sp.Rational(1, 2) * X**4,
    )

    # ASSERT: different algebraic presentations, same coarse generic genus.
    assert pendulum.degree == 3
    assert quartic.degree == 4
    assert pendulum.generic_genus == quartic.generic_genus == 1
    assert sp.factor(pendulum.discriminant) != sp.factor(quartic.discriminant)


def test_genus_is_a_cross_problem_structural_observable_not_a_problem_label():
    E, X, Y = sp.symbols("E X Y")
    profiles = (
        hyperelliptic_profile(X, Y, 2 * (E - X) * (1 - X**2)),
        hyperelliptic_profile(X, Y, 2 * E - sp.Rational(1, 2) * X**4),
    )

    # ASSERT / BOUNDARY: this common observable is genus only.
    assert {profile.generic_genus for profile in profiles} == {1}
    assert all(profile.generically_smooth for profile in profiles)
