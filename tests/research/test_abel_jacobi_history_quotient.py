"""Abel--Jacobi history: closed process histories become lattice translations.

Question
--------
The real-split genus-two calibration now generates its own symplectic A/B cycle
system and a Riemann-shaped normalized period matrix.  Can we use those measured
objects to make the next historical step executable: turn path-dependent
Abelian integrals into a normalized history coordinate whose closed-history
residuals are exactly period-lattice translations?

Primitive data
--------------
We reuse the real-split genus-two quotient

    C: y^2 = (x^2-1)(x^2-4)(x^2-9)

and supply only its ordered real branch locus

    -3 < -2 < -1 < 1 < 2 < 3.

The common branch-cut constructor emits the symplectic cycle presentation.  The
period layer measures A and B.  The intersection layer checks the sampled
surface pairing.  This test does *not* supply a period matrix, Abel--Jacobi
coordinates, a Jacobian lattice, divisor classes, or theta functions.

Classical lineage
-----------------
For a compact genus-g Riemann surface with holomorphic basis
``omega_1,...,omega_g``, path integration gives a vector of Abelian integrals.
Choosing a symplectic homology basis gives A/B period blocks.  After A-normalizing
the differentials, the period lattice has the standard form

    Lambda = Z^g + tau Z^g,

and the analytic Jacobian is ``C^g/Lambda``.  The Abel--Jacobi map is obtained
by fixing a base point and reducing path integrals modulo this lattice.  See
[Forster-1981], [Farkas-Kra-1992], and [Mumford-1983].  Historically this is the
higher-genus successor to elliptic inversion; see [Baker-1897].

Shakespeare reconstruction
---------------------------
The order is intentionally process-first:

    quotient branch geometry
      -> constructed symplectic histories
      -> measured differential periods
      -> Riemann consistency checks
      -> A-normalized history increments
      -> quotient by closed-history shifts.

For a lifted history gamma, Shakespeare keeps the vector

    u(gamma) = (int_gamma omega_1, int_gamma omega_2)

before quotienting it.  Normalization by the measured A block gives

    u_hat = A^{-1}u.

The generated closed histories must then satisfy

    u_hat(a_1)=e_1,  u_hat(a_2)=e_2,
    u_hat(b_j)=tau[:,j].

**Shakespeare interpretation.**  The period lattice is the residual grammar of
closed lifted histories after the base geometric state has returned.  Passing
to ``C^g/(Z^g+tau Z^g)`` is therefore a history quotient: it identifies
coordinates that differ only by those globally closed process histories.

Calibration statement
---------------------
Passing this file certifies for the generated genus-two presentation:

1. the branch-generated cycle system passes the sampled symplectic and Riemann
   matrix checks before a torus object is allowed to exist;
2. normalized A-cycle history increments are the two standard coordinate shifts;
3. normalized B-cycle history increments are the two columns of tau;
4. arbitrary declared integer combinations ``m + tau n`` are represented by the
   same lattice-shift API used to identify history coordinates modulo periods;
5. a failed Riemann profile cannot be silently promoted to a normalized Abelian
   torus.

Proof map
---------
``test_closed_generated_histories_become_normalized_lattice_generators`` checks
items 1-3. ``test_declared_closed_history_combinations_are_period_lattice_shifts``
checks item 4. ``test_torus_construction_is_gated_by_riemann_profile`` checks
item 5.

Boundary
--------
``NormalizedAbelianTorus`` is deliberately *not* named ``Jacobian``.  The test
constructs the numerical normalized period quotient associated with a passing
sampled Riemann profile.  It does not implement divisor equivalence, a
principally polarized Abelian variety as an algebraic object, theta functions,
Jacobi inversion, or a path-independent point map from the curve.  A genuine
Abel--Jacobi point coordinate additionally needs a fixed base point and a path
to that point; the library currently exposes the more primitive history
increment so that path dependence remains explicit.

References
----------
[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.

[Mumford-1983] D. Mumford, *Tata Lectures on Theta I*, Birkhaeuser, 1983.
DOI: 10.1007/978-1-4899-2843-6.

[Baker-1897] H. F. Baker, *Abel's Theorem and the Allied Theory Including the
Theory of the Theta Functions*, Cambridge University Press, 1897.
"""

import dataclasses

import sympy as sp
import pytest

from aeg_shakespeare import (
    SampledRiemannProfile,
    abel_jacobi_history_increment,
    compute_period_matrix,
    construct_real_branch_cycles,
    hyperelliptic_profile,
    normalized_abelian_torus,
    real_branch_cut_presentation,
    sampled_intersection_form,
    sampled_riemann_profile,
)


def generated_genus_two_riemann_profile(samples: int = 512):
    x, y = sp.symbols("x y")
    polynomial = sp.expand((x**2 - 1) * (x**2 - 4) * (x**2 - 9))
    curve = hyperelliptic_profile(x, y, polynomial)
    presentation = real_branch_cut_presentation(
        curve,
        (-3.0, -2.0, -1.0, 1.0, 2.0, 3.0),
    )
    constructed = construct_real_branch_cycles(presentation, samples=samples)
    cycles = constructed.cycle_system
    intersections = sampled_intersection_form(cycles, sheet_tolerance=2e-3)
    periods = compute_period_matrix(cycles)
    return constructed, periods, sampled_riemann_profile(periods, intersections)


def assert_vector_close(left, right, tolerance=2e-8):
    assert len(left) == len(right)
    assert max(abs(complex(a) - complex(b)) for a, b in zip(left, right, strict=True)) < tolerance


def test_closed_generated_histories_become_normalized_lattice_generators():
    constructed, periods, riemann = generated_genus_two_riemann_profile()
    assert riemann.passes

    torus = normalized_abelian_torus(riemann)
    assert torus.dimension == 2

    for index, cycle in enumerate(constructed.a_cycles):
        increment = abel_jacobi_history_increment(cycle, periods)
        assert_vector_close(increment.normalized, torus.a_shift(index))

    for index, cycle in enumerate(constructed.b_cycles):
        increment = abel_jacobi_history_increment(cycle, periods)
        assert_vector_close(increment.normalized, torus.b_shift(index))


def test_declared_closed_history_combinations_are_period_lattice_shifts():
    _, _, riemann = generated_genus_two_riemann_profile(samples=384)
    torus = normalized_abelian_torus(riemann)

    m = (2, -1)
    n = (1, 3)
    shift = torus.lattice_shift(m, n)
    origin = (0j, 0j)

    assert torus.matches_lattice_shift(origin, shift, m, n, tolerance=1e-12)
    assert not torus.matches_lattice_shift(origin, shift, (2, 0), n, tolerance=1e-12)


def test_torus_construction_is_gated_by_riemann_profile():
    _, periods, riemann = generated_genus_two_riemann_profile(samples=384)
    assert riemann.passes

    # Deliberately corrupt the topological evidence without changing the period
    # matrix.  A matrix that looks Riemann-like is not enough by itself.
    bad_intersections = dataclasses.replace(
        riemann.intersections,
        matrix=((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
    )
    bad = SampledRiemannProfile(periods=periods, intersections=bad_intersections)
    assert not bad.passes

    with pytest.raises(ValueError, match="passing Riemann profile"):
        normalized_abelian_torus(bad)
