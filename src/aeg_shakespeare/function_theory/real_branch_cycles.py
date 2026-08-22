"""Constructed A/B cycles for real-split hyperelliptic process quotients.

Primitive question
------------------
The period and intersection layers can measure cycles once those cycles have
already been supplied. That still leaves a representation choice outside the
library: *where did the A/B cycles come from?*

For a real-split even-degree hyperelliptic quotient

    y^2 = c prod_j (x-e_j),       e_1 < ... < e_(2g+2),

there is a classical answer visible directly in the branch-point order. Pair
adjacent branch points into cuts

    [e_1,e_2], [e_3,e_4], ..., [e_(2g+1),e_(2g+2)].

A standard symplectic presentation may take ``a_i`` around the i-th nonreference
cut and ``b_i`` around the even branch set beginning at the right end of that
cut and ending at the left end of the final reference cut. In index notation
used here,

    a_i encloses e_(2i), ..., e_(2i+1),
    b_i encloses e_(2i+1), ..., e_(2g),

for ``i=0,...,g-1``. The resulting abstract pairing is

    a_i . a_j = b_i . b_j = 0,
    a_i . b_j = delta_ij.

This is the familiar branch-cut construction behind hyperelliptic homology and
period calculations; see Farkas--Kra and Frauendiener--Klein in
``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The important change is that the cycle basis is no longer an unexplained input.
The branch-point presentation itself emits:

1. the cut pairing;
2. exact combinatorial A/B cycle specifications;
3. the target symplectic intersection matrix forced by that construction;
4. sampled base contours realizing those specifications;
5. lifted histories obtained by the existing square-root continuation engine.

The exact combinatorial certificate and the sampled realization are deliberately
kept separate. Later code can ask whether numerical lifted intersections agree
with the pairing promised by construction.

Executable contract
-------------------
``real_branch_cut_presentation`` validates a supplied ordered list of all
``2g+2`` real branch points of an even-degree quotient. ``construct_real_branch_cycles``
turns the canonical interval specifications into nested/transverse ellipses and
lifts them to the Riemann surface. Under the implementation's fixed convention
that continuation starts at the rightmost point on the principal square-root
sheet, nested B-contours alternate their base orientation so that the lifted
cycles realize ``a_i.b_i=+1``. The function returns both the construction
metadata and an ``AbelianCycleSystem`` ready for period integration.

Boundary
--------
This module handles only the real-split, even-degree case with explicitly
supplied branch points. It does not discover cuts for arbitrary complex branch
configurations, prove numerical contour deformation invariance, or replace a
general Tretkoff--Tretkoff style homology algorithm. The ellipse geometry is a
sampled realization of a classical branch-cut presentation, not the topology
itself.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Literal

import sympy as sp

from .algebraic import HyperellipticProfile
from .period_matrix import AbelianCycleSystem
from .periods import LiftedSquareRootPath, lift_square_root_path

CycleFamily = Literal["A", "B"]


@dataclass(frozen=True)
class RealBranchCycleSpec:
    """One cycle specified by the consecutive branch points it encloses."""

    family: CycleFamily
    index: int
    left_branch_index: int
    right_branch_index: int

    @property
    def branch_count(self) -> int:
        return self.right_branch_index - self.left_branch_index + 1


@dataclass(frozen=True)
class RealBranchCutPresentation:
    """Classical branch-cut presentation for a real-split even-degree curve."""

    curve: HyperellipticProfile
    branch_points: tuple[float, ...]
    a_specs: tuple[RealBranchCycleSpec, ...]
    b_specs: tuple[RealBranchCycleSpec, ...]

    @property
    def genus(self) -> int:
        genus = self.curve.generic_genus
        assert genus is not None
        return genus

    @property
    def reference_cut(self) -> tuple[float, float]:
        return self.branch_points[-2], self.branch_points[-1]

    @property
    def construction_intersection_form(self) -> tuple[tuple[int, ...], ...]:
        """Return the exact target ``[[0,I],[-I,0]]`` in A-then-B order."""

        genus = self.genus
        size = 2 * genus
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for index in range(genus):
            matrix[index][genus + index] = 1
            matrix[genus + index][index] = -1
        return tuple(tuple(row) for row in matrix)


@dataclass(frozen=True)
class ConstructedRealBranchCycles:
    """Sampled lifted realization plus its branch-cut construction certificate."""

    presentation: RealBranchCutPresentation
    a_cycles: tuple[LiftedSquareRootPath, ...]
    b_cycles: tuple[LiftedSquareRootPath, ...]

    @property
    def cycle_system(self) -> AbelianCycleSystem:
        return AbelianCycleSystem(
            curve=self.presentation.curve,
            a_cycles=self.a_cycles,
            b_cycles=self.b_cycles,
        )

    @property
    def construction_intersection_form(self) -> tuple[tuple[int, ...], ...]:
        return self.presentation.construction_intersection_form


def real_branch_cut_presentation(
    curve: HyperellipticProfile,
    branch_points: tuple[float, ...] | list[float],
    *,
    root_tolerance: float = 1e-10,
) -> RealBranchCutPresentation:
    """Validate real branch points and emit the canonical interval cycle specs."""

    genus = curve.generic_genus
    if genus is None or genus < 1:
        raise ValueError("real branch-cycle presentation requires positive generic genus")
    if curve.degree != 2 * genus + 2:
        raise ValueError("real branch-cycle presentation currently requires even degree 2g+2")

    points = tuple(float(value) for value in branch_points)
    expected = 2 * genus + 2
    if len(points) != expected:
        raise ValueError(f"expected exactly {expected} real branch points")
    if any(not math.isfinite(value) for value in points):
        raise ValueError("branch points must be finite real numbers")
    if any(points[index] >= points[index + 1] for index in range(len(points) - 1)):
        raise ValueError("branch points must be strictly increasing")
    if root_tolerance <= 0:
        raise ValueError("root_tolerance must be positive")

    for point in points:
        value = complex(sp.N(curve.polynomial.subs(curve.x, point), 40))
        scale = max(1.0, abs(point) ** curve.degree)
        if abs(value) > root_tolerance * scale:
            raise ValueError(f"supplied branch point {point} is not a root of the curve polynomial")

    a_specs = tuple(
        RealBranchCycleSpec("A", index, 2 * index, 2 * index + 1)
        for index in range(genus)
    )
    # The final pair [e_(2g), e_(2g+1)] is the reference cut. b_i surrounds
    # the even branch set from the right endpoint of a_i to the left endpoint
    # of that reference cut. Nested B-contours then intersect only their dual A.
    b_specs = tuple(
        RealBranchCycleSpec("B", index, 2 * index + 1, 2 * genus)
        for index in range(genus)
    )
    if any(spec.branch_count % 2 for spec in a_specs + b_specs):
        raise AssertionError("constructed hyperelliptic cycles must enclose even branch sets")

    return RealBranchCutPresentation(
        curve=curve,
        branch_points=points,
        a_specs=a_specs,
        b_specs=b_specs,
    )


def _ellipse_for_spec(
    presentation: RealBranchCutPresentation,
    spec: RealBranchCycleSpec,
    *,
    samples: int,
    padding_fraction: float,
    height_fraction: float,
) -> tuple[complex, ...]:
    points = presentation.branch_points
    left_index = spec.left_branch_index
    right_index = spec.right_branch_index
    left = points[left_index]
    right = points[right_index]
    span = right - left

    left_clearance = (
        left - points[left_index - 1]
        if left_index > 0
        else points[1] - points[0]
    )
    right_clearance = (
        points[right_index + 1] - right
        if right_index + 1 < len(points)
        else points[-1] - points[-2]
    )
    padding = padding_fraction * min(left_clearance, right_clearance)
    center = 0.5 * (left + right)
    horizontal_radius = 0.5 * span + padding
    vertical_radius = height_fraction * horizontal_radius

    contour = tuple(
        center
        + horizontal_radius * math.cos(2.0 * math.pi * step / samples)
        + 1j * vertical_radius * math.sin(2.0 * math.pi * step / samples)
        for step in range(samples + 1)
    )
    # All contours start at their rightmost point.  With the principal-square-root
    # initial sheet used by lift_square_root_path, successive nested B cycles
    # acquire alternating lifted orientation.  Reverse the odd-indexed ones so
    # the realized basis matches the construction convention a_i.b_i=+1.
    if spec.family == "B" and spec.index % 2 == 1:
        contour = tuple(reversed(contour))
    return contour


def construct_real_branch_cycles(
    presentation: RealBranchCutPresentation,
    *,
    samples: int = 1024,
    padding_fraction: float = 0.18,
    height_fraction: float = 0.35,
) -> ConstructedRealBranchCycles:
    """Materialize and lift the A/B contours emitted by a real branch presentation."""

    if samples < 64:
        raise ValueError("cycle construction requires at least 64 contour samples")
    if not 0 < padding_fraction < 0.5:
        raise ValueError("padding_fraction must lie between 0 and 0.5")
    if height_fraction <= 0:
        raise ValueError("height_fraction must be positive")

    def lift(spec: RealBranchCycleSpec) -> LiftedSquareRootPath:
        base_path = _ellipse_for_spec(
            presentation,
            spec,
            samples=samples,
            padding_fraction=padding_fraction,
            height_fraction=height_fraction,
        )
        path = lift_square_root_path(presentation.curve, base_path)
        if not path.lifted_closed:
            raise ValueError(
                f"constructed {spec.family}{spec.index + 1} contour did not close on the lifted surface"
            )
        return path

    return ConstructedRealBranchCycles(
        presentation=presentation,
        a_cycles=tuple(lift(spec) for spec in presentation.a_specs),
        b_cycles=tuple(lift(spec) for spec in presentation.b_specs),
    )
