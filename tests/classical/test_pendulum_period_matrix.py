"""Pendulum IV: two explicit lifted cycles produce a normalized period matrix.

Question
--------
Can the genus-one pendulum quotient now produce both independent periods from
explicit lifted contours, so that the normalized matrix ``tau=A^{-1}B`` is
measured rather than supplied by a symmetry argument?

Primitive data
--------------
We again use only the symmetric-energy quotient

    Y^2 = 2 U (U^2 - 1),

its canonical differential ``omega=dU/Y``, and two sampled ellipses in the
U-plane:

- the A-contour encloses the branch pair {-1,0};
- the B-contour encloses the branch pair {0,1}.

Neither period value nor tau is supplied to ``compute_period_matrix``.

Classical lineage
-----------------
For a genus-g compact Riemann surface, choosing a symplectic homology basis
(a_1,...,a_g,b_1,...,b_g) and integrating a basis of holomorphic differentials
produces A- and B-period blocks.  Normalization gives tau=A^{-1}B; for a genuine
symplectic basis the Riemann bilinear relations imply that tau is symmetric and
Im(tau) is positive definite.  See [Farkas-Kra-1992], [Forster-1981], and
[Mumford-1983].  In the lemniscatic genus-one case the normalized lattice has
tau=i; see [DLMF-23.5].

Shakespeare reconstruction
---------------------------
The process-first route now runs

    quotient curve
      -> canonical differential
      -> sampled base contours
      -> continued lifted histories
      -> measured A/B periods
      -> normalized candidate period matrix.

The cycle-system API refuses a base loop that does not close on the lifted
surface.  Period normalization therefore occurs only after history closure has
been checked.

**Shakespeare interpretation.**  The matrix is a compressed record of how the
canonical history coordinate fails to return around independent closed process
histories.  The period-matrix theorem is classical; this interpretation is the
project's language.

Calibration statement
---------------------
For the chosen E=0 normalization and explicit contours, this file certifies
numerically that:

1. both branch-pair contours close on the lifted surface;
2. direct integration gives two non-collinear periods of equal magnitude;
3. the measured normalized 1x1 period matrix satisfies tau approximately i;
4. its imaginary part is positive and the generic matrix-shape check passes.

Proof map
---------
``test_pendulum_two_cut_cycles_close_upstairs`` checks item 1.
``test_pendulum_explicit_cycles_produce_square_period_matrix`` checks items 2-4.

Boundary
--------
This file does not compute the topological intersection number of the two cycles.
Accordingly ``riemann_shape_passes`` is a necessary numerical consistency check,
not a proof that the supplied cycles are a canonical symplectic basis.  The
contours are hand chosen, quadrature is numerical, and no rigorous error bound is
claimed.  These limitations are precisely the next implementation target.

References
----------
[DLMF-23.5] NIST Digital Library of Mathematical Functions, §23.5,
“Special Lattices,” including the lemniscatic square lattice,
https://dlmf.nist.gov/23.5 .

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992, chapters on Abelian differentials and period matrices.
DOI: 10.1007/978-1-4612-2034-3.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Mumford-1983] D. Mumford, *Tata Lectures on Theta I*, Birkhauser, 1983,
period matrices and principally polarized complex tori.
DOI: 10.1007/978-1-4899-2843-6.
"""

import math

import sympy as sp

from aeg_shakespeare.analysis.abelian import (
    AbelianCycleSystem,
    compute_period_matrix,
    lift_square_root_path,
)
from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile


def pendulum_e0_curve():
    U, Y = sp.symbols("U Y")
    return hyperelliptic_profile(U, Y, 2 * U * (U**2 - 1))


def branch_pair_ellipse(center: float, samples: int = 2048):
    return tuple(
        center
        + 0.6 * math.cos(2 * math.pi * index / samples)
        + 0.25j * math.sin(2 * math.pi * index / samples)
        for index in range(samples + 1)
    )


def explicit_cycle_system(samples: int = 2048):
    curve = pendulum_e0_curve()
    a_cycle = lift_square_root_path(curve, branch_pair_ellipse(-0.5, samples))
    b_cycle = lift_square_root_path(curve, branch_pair_ellipse(+0.5, samples))
    return AbelianCycleSystem(curve, (a_cycle,), (b_cycle,))


def test_pendulum_two_cut_cycles_close_upstairs():
    cycles = explicit_cycle_system(1024)

    assert cycles.a_cycles[0].base_closed
    assert cycles.b_cycles[0].base_closed
    assert cycles.a_cycles[0].lifted_closed
    assert cycles.b_cycles[0].lifted_closed
    assert cycles.a_cycles[0].sheet_multiplier == 1
    assert cycles.b_cycles[0].sheet_multiplier == 1


def test_pendulum_explicit_cycles_produce_square_period_matrix():
    period_data = compute_period_matrix(explicit_cycle_system(2048))

    omega_a = period_data.a_periods[0][0]
    omega_b = period_data.b_periods[0][0]
    tau = period_data.tau[0][0]

    assert abs(abs(omega_a) - abs(omega_b)) < 1e-8
    assert abs(tau - 1j) < 1e-8
    assert period_data.symmetry_residual < 1e-12
    assert period_data.imaginary_part[0][0] > 0
    assert period_data.riemann_shape_passes(tolerance=1e-8)
