"""Sampled intersection pairing for lifted process cycles.

Primitive question
------------------
A period matrix is only a candidate Riemann period presentation until the cycles
carrying its periods have the right intersection structure.  On a genus-g
oriented surface a canonical basis satisfies

    a_i . a_j = 0,
    b_i . b_j = 0,
    a_i . b_j = delta_ij.

How much of that structure can be measured directly from the sampled lifted
histories already used by Shakespeare's period engine?

Classical shadow
----------------
The algebraic intersection number of transverse oriented curves is the signed
sum of their intersections.  On a hyperelliptic double cover, two projected
base paths may cross at the same x-value while their lifts lie on opposite
sheets, in which case there is *no* intersection on the Riemann surface.  A
symplectic homology basis has intersection matrix

    J = [[0, I], [-I, 0]].

See Farkas--Kra and Forster in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The implementation works with the actual lifted histories rather than only the
projected curves.  It first finds transverse intersections of polygonal base
segments.  At each projected crossing it interpolates the two continued y
values and asks whether the histories occupy the same sheet.  Only same-sheet
crossings contribute their orientation sign to the sampled intersection number.

This makes a subtle point executable: *projected crossing is not surface
intersection*.  Sheet history is part of the topology.

Executable contract
-------------------
``lifted_path_intersections`` reports every resolved projected crossing together
with its orientation and sheet relation. ``sampled_intersection_number`` sums
same-sheet signs and refuses unresolved sheet comparisons.  For an
``AbelianCycleSystem``, ``sampled_intersection_form`` builds the full 2g-by-2g
matrix in A-then-B order and compares it with the canonical symplectic form.

``sampled_riemann_profile`` combines that sampled topological evidence with the
symmetry/positive-imaginary-part checks of an ``AbelianPeriodMatrix``.

Boundary
--------
This remains a sampled numerical topology engine, not a certified algebraic
intersection algorithm.  Paths must be polygonally resolved, transverse, and
away from branch points.  Tangencies, shared segments, endpoint crossings, and
near-degenerate sheet comparisons are rejected or ignored rather than assigned
an intersection number.  Exact homology classes and deformation invariance are
future layers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import sympy as sp

from .period_matrix import AbelianCycleSystem, AbelianPeriodMatrix
from .periods import LiftedSquareRootPath

SheetRelation = Literal["same", "opposite", "unresolved"]


def _cross(left: complex, right: complex) -> float:
    return float((left.conjugate() * right).imag)


@dataclass(frozen=True)
class LiftedCycleIntersection:
    """One transverse crossing of two projected segments with sheet metadata."""

    base_point: complex
    left_segment: int
    right_segment: int
    orientation: int
    sheet_relation: SheetRelation
    relative_same_sheet_error: float
    relative_opposite_sheet_error: float

    @property
    def contributes_on_surface(self) -> bool:
        return self.sheet_relation == "same"


def _proper_segment_intersection(
    p: complex,
    p_next: complex,
    q: complex,
    q_next: complex,
    *,
    geometry_tolerance: float,
) -> tuple[float, float, complex, int] | None:
    r = p_next - p
    s = q_next - q
    denominator = _cross(r, s)
    if abs(denominator) <= geometry_tolerance:
        return None

    delta = q - p
    t = _cross(delta, s) / denominator
    u = _cross(delta, r) / denominator
    margin = geometry_tolerance
    if not (margin < t < 1.0 - margin and margin < u < 1.0 - margin):
        return None

    point = p + t * r
    orientation = 1 if denominator > 0 else -1
    return t, u, point, orientation


def lifted_path_intersections(
    left: LiftedSquareRootPath,
    right: LiftedSquareRootPath,
    *,
    sheet_tolerance: float = 1e-3,
    geometry_tolerance: float = 1e-12,
    dedup_tolerance: float = 1e-8,
) -> tuple[LiftedCycleIntersection, ...]:
    """Measure transverse projected crossings and resolve their sheet relation."""

    if left.curve != right.curve:
        raise ValueError("lifted paths must belong to the same curve")
    if sheet_tolerance <= 0 or geometry_tolerance <= 0 or dedup_tolerance <= 0:
        raise ValueError("intersection tolerances must be positive")

    intersections: list[LiftedCycleIntersection] = []
    for i in range(len(left.x_values) - 1):
        p = left.x_values[i]
        p_next = left.x_values[i + 1]
        left_min_x, left_max_x = sorted((p.real, p_next.real))
        left_min_y, left_max_y = sorted((p.imag, p_next.imag))

        for j in range(len(right.x_values) - 1):
            q = right.x_values[j]
            q_next = right.x_values[j + 1]
            right_min_x, right_max_x = sorted((q.real, q_next.real))
            right_min_y, right_max_y = sorted((q.imag, q_next.imag))

            if left_max_x < right_min_x or right_max_x < left_min_x:
                continue
            if left_max_y < right_min_y or right_max_y < left_min_y:
                continue

            crossing = _proper_segment_intersection(
                p,
                p_next,
                q,
                q_next,
                geometry_tolerance=geometry_tolerance,
            )
            if crossing is None:
                continue
            t, u, point, orientation = crossing

            if any(abs(point - old.base_point) <= dedup_tolerance for old in intersections):
                continue

            left_y = left.y_values[i] + t * (left.y_values[i + 1] - left.y_values[i])
            right_y = right.y_values[j] + u * (right.y_values[j + 1] - right.y_values[j])
            scale = max(1.0, abs(left_y), abs(right_y))
            same_error = abs(left_y - right_y) / scale
            opposite_error = abs(left_y + right_y) / scale

            if same_error <= sheet_tolerance and same_error < opposite_error:
                sheet_relation: SheetRelation = "same"
            elif opposite_error <= sheet_tolerance and opposite_error < same_error:
                sheet_relation = "opposite"
            else:
                sheet_relation = "unresolved"

            intersections.append(
                LiftedCycleIntersection(
                    base_point=point,
                    left_segment=i,
                    right_segment=j,
                    orientation=orientation,
                    sheet_relation=sheet_relation,
                    relative_same_sheet_error=float(same_error),
                    relative_opposite_sheet_error=float(opposite_error),
                )
            )

    return tuple(intersections)


def sampled_intersection_number(
    left: LiftedSquareRootPath,
    right: LiftedSquareRootPath,
    *,
    sheet_tolerance: float = 1e-3,
) -> int:
    """Signed same-sheet intersection count for two sampled lifted cycles."""

    crossings = lifted_path_intersections(
        left,
        right,
        sheet_tolerance=sheet_tolerance,
    )
    unresolved = [crossing for crossing in crossings if crossing.sheet_relation == "unresolved"]
    if unresolved:
        raise ValueError("sampled intersections contain unresolved sheet comparisons")
    return sum(
        crossing.orientation
        for crossing in crossings
        if crossing.contributes_on_surface
    )


def canonical_symplectic_form(genus: int) -> tuple[tuple[int, ...], ...]:
    """Return J=[[0,I],[-I,0]] in A-then-B cycle order."""

    if genus < 1:
        raise ValueError("genus must be positive")
    size = 2 * genus
    rows = [[0 for _ in range(size)] for _ in range(size)]
    for index in range(genus):
        rows[index][genus + index] = 1
        rows[genus + index][index] = -1
    return tuple(tuple(row) for row in rows)


@dataclass(frozen=True)
class SampledIntersectionForm:
    """Numerically measured intersection form for one A/B cycle system."""

    cycles: AbelianCycleSystem
    matrix: tuple[tuple[int, ...], ...]

    @property
    def genus(self) -> int:
        return self.cycles.curve.generic_genus or 0

    @property
    def is_skew_symmetric(self) -> bool:
        return all(
            self.matrix[i][j] == -self.matrix[j][i]
            for i in range(len(self.matrix))
            for j in range(len(self.matrix))
        )

    @property
    def determinant(self) -> int:
        return int(sp.Matrix(self.matrix).det())

    @property
    def is_unimodular(self) -> bool:
        return abs(self.determinant) == 1

    @property
    def canonical_residual(self) -> int:
        expected = canonical_symplectic_form(self.genus)
        return max(
            abs(self.matrix[i][j] - expected[i][j])
            for i in range(len(self.matrix))
            for j in range(len(self.matrix))
        )

    @property
    def is_canonical_symplectic(self) -> bool:
        return (
            self.is_skew_symmetric
            and self.is_unimodular
            and self.canonical_residual == 0
        )


def sampled_intersection_form(
    cycles: AbelianCycleSystem,
    *,
    sheet_tolerance: float = 1e-3,
) -> SampledIntersectionForm:
    """Measure the 2g-by-2g sampled intersection matrix in A-then-B order."""

    ordered = cycles.a_cycles + cycles.b_cycles
    size = len(ordered)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            value = sampled_intersection_number(
                ordered[i],
                ordered[j],
                sheet_tolerance=sheet_tolerance,
            )
            matrix[i][j] = value
            matrix[j][i] = -value
    return SampledIntersectionForm(cycles, tuple(tuple(row) for row in matrix))


@dataclass(frozen=True)
class SampledRiemannProfile:
    """Combined sampled topology + period-matrix consistency profile."""

    periods: AbelianPeriodMatrix
    intersections: SampledIntersectionForm

    def __post_init__(self) -> None:
        if self.periods.cycles != self.intersections.cycles:
            raise ValueError("period and intersection data must use the same cycle system")

    @property
    def passes(self) -> bool:
        return (
            self.intersections.is_canonical_symplectic
            and self.periods.riemann_shape_passes()
        )


def sampled_riemann_profile(
    periods: AbelianPeriodMatrix,
    intersections: SampledIntersectionForm,
) -> SampledRiemannProfile:
    return SampledRiemannProfile(periods=periods, intersections=intersections)
