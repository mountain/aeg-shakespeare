"""Normalized Abelian history coordinates and the period-lattice quotient.

Primitive question
------------------
Once a process quotient has emitted canonical holomorphic differentials, a
symplectic cycle system, and a Riemann-shaped period matrix, what does a lifted
history *measure* globally?

For a path ``gamma`` on a genus-``g`` curve the vector

    u(gamma) = (integral_gamma omega_1, ..., integral_gamma omega_g)

records the Abelian-integral increment carried by that history.  If ``A`` is
the A-period block, the normalized increment is

    u_hat = A^{-1} u.

Closed A- and B-cycle histories then shift the normalized coordinate by

    e_j                 and                 tau[:, j],

respectively.  Thus the residual ambiguity after quotienting closed histories
is the lattice

    Z^g + tau Z^g  subset C^g.

Classical lineage
-----------------
This is the analytic construction underlying the Abel--Jacobi map and the
Jacobian of a compact Riemann surface.  Choosing a base point and integrating a
basis of holomorphic one-forms sends points/divisors to ``C^g`` modulo the
period lattice.  With A-normalized differentials the Jacobian has the standard
presentation

    C^g / (Z^g + tau Z^g).

See Farkas--Kra, Forster, and Mumford in ``docs/REFERENCES.md``.  Historically,
Abel's theorem and Jacobi inversion are the higher-genus continuation of the
elliptic-integral inversion story; Baker is retained in the bibliography as a
classical historical source.

Shakespeare reconstruction
---------------------------
The package does not insert a ``Jacobian`` object merely because the curve has
genus ``g``.  This module is enabled only after earlier executable layers have
produced:

1. actual lifted histories;
2. their period matrix;
3. a sampled canonical symplectic intersection form; and
4. the Riemann symmetry/positive-imaginary-part checks.

``NormalizedAbelianTorus`` therefore accepts a *passing* ``SampledRiemannProfile``.
It is a numerical period-lattice presentation, not a claim that Shakespeare has
implemented divisor arithmetic or an algebraic Jacobian model.

``AbelJacobiHistoryIncrement`` likewise represents the integral accumulated by
one lifted path.  A genuine point-valued Abel--Jacobi map additionally requires
a chosen base point and a path from that base point.  Keeping the object as a
history increment makes the dependence on path history explicit rather than
silently hiding it modulo periods.

Executable contract
-------------------
``abel_jacobi_history_increment`` integrates the canonical differential basis
along a lifted path and normalizes by the measured A-period block.  For the
cycle system that generated the period matrix:

    A_j -> e_j,
    B_j -> tau[:,j].

``NormalizedAbelianTorus.lattice_shift(m,n)`` returns ``m + tau n`` for integer
vectors ``m,n``.  ``matches_lattice_shift`` checks a *declared* lattice
relation; it deliberately does not solve the hard inverse problem of deciding
an arbitrary nearest/exact period relation.

Boundary
--------
All data inherit the numerical/sampling limitations of the current continuation,
intersection, and quadrature layers.  The class is not a full Jacobian: it has
no divisor classes, theta functions, polarization machinery beyond the already
checked cycle pairing, algebraic group law, or Jacobi inversion solver.  The
name ``NormalizedAbelianTorus`` is intentional.  The classical identification
with the Jacobian is the shadow when the supplied Riemann-surface data are
mathematically valid.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import sympy as sp

from .abelian import holomorphic_differential_basis
from .intersection import SampledRiemannProfile
from .period_matrix import AbelianPeriodMatrix
from .periods import LiftedSquareRootPath, integrate_lifted_differential

ComplexVector = tuple[complex, ...]


def _complex_matrix(rows: Sequence[Sequence[complex]]) -> sp.Matrix:
    return sp.Matrix([[complex(value) for value in row] for row in rows])


def _complex_vector(values: Sequence[complex]) -> sp.Matrix:
    return sp.Matrix([complex(value) for value in values])


def _as_complex_tuple(column: sp.Matrix) -> ComplexVector:
    return tuple(complex(sp.N(column[index], 30)) for index in range(column.rows))


@dataclass(frozen=True)
class AbelJacobiHistoryIncrement:
    """Raw and A-normalized Abelian-integral increment of one lifted history."""

    periods: AbelianPeriodMatrix
    path: LiftedSquareRootPath
    raw: ComplexVector
    normalized: ComplexVector

    @property
    def dimension(self) -> int:
        return len(self.normalized)


@dataclass(frozen=True)
class NormalizedAbelianTorus:
    """Numerical normalized lattice ``C^g / (Z^g + tau Z^g)``.

    Construction is intentionally gated by a passing sampled Riemann profile so
    callers cannot turn an arbitrary complex matrix into a Shakespeare
    ``Jacobian-like`` representation without the currently available topology
    and Riemann-shape evidence.
    """

    riemann: SampledRiemannProfile

    def __post_init__(self) -> None:
        if not self.riemann.passes:
            raise ValueError("normalized Abelian torus requires a passing Riemann profile")

    @property
    def periods(self) -> AbelianPeriodMatrix:
        return self.riemann.periods

    @property
    def dimension(self) -> int:
        return self.periods.genus

    @property
    def tau(self) -> tuple[tuple[complex, ...], ...]:
        return self.periods.tau

    def a_shift(self, index: int) -> ComplexVector:
        """Return the normalized lattice shift generated by A_index."""

        if not 0 <= index < self.dimension:
            raise IndexError("A-cycle index out of range")
        return tuple(1.0 + 0j if row == index else 0j for row in range(self.dimension))

    def b_shift(self, index: int) -> ComplexVector:
        """Return the normalized lattice shift generated by B_index."""

        if not 0 <= index < self.dimension:
            raise IndexError("B-cycle index out of range")
        return tuple(self.tau[row][index] for row in range(self.dimension))

    def lattice_shift(
        self,
        a_coefficients: Sequence[int],
        b_coefficients: Sequence[int],
    ) -> ComplexVector:
        """Return ``m + tau*n`` for integer coefficient vectors ``m,n``."""

        if len(a_coefficients) != self.dimension or len(b_coefficients) != self.dimension:
            raise ValueError("lattice coefficient vectors must have length g")
        if any(not isinstance(value, int) for value in tuple(a_coefficients) + tuple(b_coefficients)):
            raise TypeError("lattice coefficients must be integers")

        return tuple(
            complex(a_coefficients[row])
            + sum(
                self.tau[row][column] * b_coefficients[column]
                for column in range(self.dimension)
            )
            for row in range(self.dimension)
        )

    def matches_lattice_shift(
        self,
        left: Sequence[complex],
        right: Sequence[complex],
        a_coefficients: Sequence[int],
        b_coefficients: Sequence[int],
        *,
        tolerance: float = 1e-8,
    ) -> bool:
        """Check ``right-left = m+tau*n`` for caller-declared integer vectors."""

        if tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if len(left) != self.dimension or len(right) != self.dimension:
            raise ValueError("torus coordinates must have length g")
        shift = self.lattice_shift(a_coefficients, b_coefficients)
        return max(
            abs((complex(right[index]) - complex(left[index])) - shift[index])
            for index in range(self.dimension)
        ) <= tolerance


def normalized_abelian_torus(riemann: SampledRiemannProfile) -> NormalizedAbelianTorus:
    """Construct the normalized period-lattice quotient from checked Riemann data."""

    return NormalizedAbelianTorus(riemann=riemann)


def abel_jacobi_history_increment(
    path: LiftedSquareRootPath,
    periods: AbelianPeriodMatrix,
) -> AbelJacobiHistoryIncrement:
    """Integrate and A-normalize the canonical differential vector on ``path``."""

    if path.curve != periods.cycles.curve:
        raise ValueError("history path and period matrix must belong to the same curve")

    differentials = holomorphic_differential_basis(path.curve)
    raw = tuple(
        integrate_lifted_differential(path, differential)
        for differential in differentials
    )

    a_matrix = _complex_matrix(periods.a_periods)
    if a_matrix.rows != len(raw) or a_matrix.cols != len(raw):
        raise ValueError("A-period block and Abelian history dimension disagree")
    normalized_column = a_matrix.inv() * _complex_vector(raw)
    normalized = _as_complex_tuple(normalized_column)

    return AbelJacobiHistoryIncrement(
        periods=periods,
        path=path,
        raw=tuple(complex(value) for value in raw),
        normalized=normalized,
    )
