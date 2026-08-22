"""Cycle systems and candidate normalized period matrices.

Primitive question
------------------
A single period is not yet the global object used by Abelian function theory.
For a genus-g curve one needs g independent holomorphic differentials and 2g
closed cycles.  Their integrals form two g-by-g blocks conventionally written
A and B.  When the cycles are a symplectic homology basis and A is invertible,
the normalized period matrix is

    tau = A^{-1} B.

Classical shadow
----------------
For a compact Riemann surface, a normalized period matrix associated with a
symplectic homology basis is symmetric and has positive-definite imaginary
part.  These are the Riemann bilinear constraints underlying the Jacobian.
See Farkas--Kra, Forster, and Mumford in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
This module deliberately starts one step earlier.  The caller supplies *closed
lifted histories* already produced by the branch-continuation layer.  We first
measure every canonical differential on every supplied cycle, then normalize
the resulting blocks.  Only afterwards do we ask whether the numerical matrix
has the symmetry/positivity shape expected of genuine Riemann period data.

Crucially, the current engine does not compute intersection numbers.  Passing
the matrix-shape checks is therefore evidence that a supplied cycle system is
consistent with a symplectic period presentation, not a proof that the cycles
form a canonical homology basis.

Boundary
--------
No automatic homology basis, intersection pairing, certified quadrature error,
or Jacobian construction is implemented here.  The positivity test uses the
Sylvester criterion on the symmetrized numerical imaginary part.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .abelian import holomorphic_differential_basis
from .algebraic import HyperellipticProfile
from .periods import LiftedSquareRootPath, integrate_lifted_differential


@dataclass(frozen=True)
class AbelianCycleSystem:
    """Caller-supplied A/B closed lifted cycles for a genus-g quotient."""

    curve: HyperellipticProfile
    a_cycles: tuple[LiftedSquareRootPath, ...]
    b_cycles: tuple[LiftedSquareRootPath, ...]

    def __post_init__(self) -> None:
        genus = self.curve.generic_genus
        if genus is None or genus < 1:
            raise ValueError("cycle system requires a generically smooth positive-genus curve")
        if len(self.a_cycles) != genus or len(self.b_cycles) != genus:
            raise ValueError("cycle system requires exactly g A-cycles and g B-cycles")
        for cycle in self.a_cycles + self.b_cycles:
            if cycle.curve != self.curve:
                raise ValueError("all cycles must belong to the declared curve")
            if not cycle.lifted_closed:
                raise ValueError("period cycles must be closed on the lifted surface")


@dataclass(frozen=True)
class AbelianPeriodMatrix:
    """Measured A/B period blocks and normalized candidate ``tau=A^{-1}B``."""

    cycles: AbelianCycleSystem
    a_periods: tuple[tuple[complex, ...], ...]
    b_periods: tuple[tuple[complex, ...], ...]
    tau: tuple[tuple[complex, ...], ...]

    @property
    def genus(self) -> int:
        return len(self.tau)

    @property
    def symmetry_residual(self) -> float:
        return max(
            abs(self.tau[i][j] - self.tau[j][i])
            for i in range(self.genus)
            for j in range(self.genus)
        )

    @property
    def imaginary_part(self) -> tuple[tuple[float, ...], ...]:
        return tuple(
            tuple(float(self.tau[i][j].imag) for j in range(self.genus))
            for i in range(self.genus)
        )

    def imaginary_part_positive_definite(self, *, tolerance: float = 1e-10) -> bool:
        """Check positive-definiteness of the symmetrized Im(tau) numerically."""

        imag = self.imaginary_part
        symmetric = [
            [0.5 * (imag[i][j] + imag[j][i]) for j in range(self.genus)]
            for i in range(self.genus)
        ]
        for size in range(1, self.genus + 1):
            determinant = complex(sp.N(sp.Matrix([row[:size] for row in symmetric[:size]]).det(), 30))
            if abs(determinant.imag) > tolerance or determinant.real <= tolerance:
                return False
        return True

    def riemann_shape_passes(self, *, tolerance: float = 1e-8) -> bool:
        """Check the numerical symmetry/positivity shape required of period data.

        This is not a homology-intersection certificate.  It tests necessary
        matrix properties assuming the caller's cycles are intended as a
        symplectic basis.
        """

        return (
            self.symmetry_residual <= tolerance
            and self.imaginary_part_positive_definite(tolerance=tolerance)
        )


def compute_period_matrix(cycles: AbelianCycleSystem) -> AbelianPeriodMatrix:
    """Integrate the canonical basis over supplied A/B cycles and normalize."""

    differentials = holomorphic_differential_basis(cycles.curve)
    a_rows = tuple(
        tuple(integrate_lifted_differential(cycle, differential) for cycle in cycles.a_cycles)
        for differential in differentials
    )
    b_rows = tuple(
        tuple(integrate_lifted_differential(cycle, differential) for cycle in cycles.b_cycles)
        for differential in differentials
    )

    a_matrix = sp.Matrix(a_rows)
    b_matrix = sp.Matrix(b_rows)
    if abs(complex(sp.N(a_matrix.det(), 30))) <= 1e-14:
        raise ValueError("A-period block is numerically singular")
    tau_matrix = a_matrix.inv() * b_matrix
    tau = tuple(
        tuple(complex(sp.N(tau_matrix[i, j], 30)) for j in range(tau_matrix.cols))
        for i in range(tau_matrix.rows)
    )
    return AbelianPeriodMatrix(
        cycles=cycles,
        a_periods=a_rows,
        b_periods=b_rows,
        tau=tau,
    )
