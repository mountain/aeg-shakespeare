"""Pendulum V: projected crossings become a symplectic pairing only after lift history.

Question
--------
The period-matrix calibration supplied two closed lifted cycles, but it did not
measure their algebraic intersection.  Can the same sampled histories distinguish
base-plane crossings from genuine intersections on the Riemann surface and
recover the genus-one symplectic pairing?

Primitive data
--------------
At E=0 we use the same process quotient

    Y^2 = 2 U (U^2 - 1)

and the same two counterclockwise ellipses:

- A encloses the branch pair {-1,0};
- B encloses the branch pair {0,1}.

Their projections intersect twice in the U-plane.  No intersection number is
supplied to the library.

Classical lineage
-----------------
For transverse oriented closed curves on an oriented surface, algebraic
intersection is the signed sum of their surface intersections.  A canonical
genus-one basis (a,b) satisfies a.b=+1 and has intersection matrix

    [[0, 1], [-1, 0]].

On a two-sheeted hyperelliptic cover, coincident projected x-values need not be
the same point of the surface: the y-coordinate/sheet must also agree.  See
[Farkas-Kra-1992] and [Forster-1981] for Riemann surfaces, branched coverings,
and canonical homology bases.

Shakespeare reconstruction
---------------------------
``lifted_path_intersections`` first finds both projected ellipse crossings.  It
then interpolates the already-continued Y history on each cycle.  At the upper
crossing the two lifts occupy the same sheet; at the lower crossing they occupy
opposite sheets.  Consequently only one projected crossing is a surface
intersection, and its orientation is +1.

**Shakespeare interpretation.**  The visible geometry alone over-counts the
intersection.  The missing bit is historical: which sheet did each path arrive
on?  In this example the symplectic pairing is therefore literally a function
of lifted history, not of the projected drawing alone.

Calibration statement
---------------------
This file certifies numerically for the chosen sampled contours that:

1. the projections cross twice;
2. exactly one crossing is same-sheet and one is opposite-sheet;
3. the sampled lifted intersection number A.B is +1;
4. the full A-then-B intersection form is the canonical unimodular symplectic
   matrix;
5. combining that form with the directly measured period matrix gives a sampled
   Riemann profile that passes both topology and period-shape checks;
6. reversing B flips A.B to -1, sends tau to -i, and makes both the canonical
   pairing check and positive-Im(tau) check fail.

Proof map
---------
``test_two_projected_crossings_reduce_to_one_surface_intersection`` checks 1-3.
``test_pendulum_cycles_measure_the_canonical_symplectic_form`` checks 4-5.
``test_reversing_b_cycle_flips_pairing_and_period_orientation`` checks 6.

Boundary
--------
The intersection engine is polygonal and numerical.  It handles transverse
crossings separated from branch points; it is not yet a certified homology
algorithm and does not prove deformation invariance.  The present result is a
stronger topology calibration than a caller-declared pairing, but it remains a
sampled certificate.  Automatic canonical cycle construction for general
hyperelliptic curves is still open.

References
----------
[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992, chapters on canonical homology bases and Abelian differentials.
DOI: 10.1007/978-1-4612-2034-3.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981,
chapters on covering surfaces and homology of compact Riemann surfaces.
DOI: 10.1007/978-1-4612-5961-9.
"""

import math

import sympy as sp

from aeg_shakespeare import (
    AbelianCycleSystem,
    LiftedSquareRootPath,
    compute_period_matrix,
    hyperelliptic_profile,
    lift_square_root_path,
    lifted_path_intersections,
    sampled_intersection_form,
    sampled_intersection_number,
    sampled_riemann_profile,
)


def pendulum_e0_curve():
    U, Y = sp.symbols("U Y")
    return hyperelliptic_profile(U, Y, 2 * U * (U**2 - 1))


def branch_pair_ellipse(center: float, samples: int = 512):
    return tuple(
        center
        + 0.6 * math.cos(2 * math.pi * index / samples)
        + 0.25j * math.sin(2 * math.pi * index / samples)
        for index in range(samples + 1)
    )


def cycle_system(samples: int = 512):
    curve = pendulum_e0_curve()
    a_cycle = lift_square_root_path(curve, branch_pair_ellipse(-0.5, samples))
    b_cycle = lift_square_root_path(curve, branch_pair_ellipse(+0.5, samples))
    return AbelianCycleSystem(curve, (a_cycle,), (b_cycle,))


def reversed_lift(path: LiftedSquareRootPath) -> LiftedSquareRootPath:
    return LiftedSquareRootPath(
        curve=path.curve,
        x_values=tuple(reversed(path.x_values)),
        y_values=tuple(reversed(path.y_values)),
    )


def test_two_projected_crossings_reduce_to_one_surface_intersection():
    cycles = cycle_system()
    a_cycle = cycles.a_cycles[0]
    b_cycle = cycles.b_cycles[0]

    crossings = lifted_path_intersections(a_cycle, b_cycle)

    assert len(crossings) == 2
    assert {crossing.sheet_relation for crossing in crossings} == {"same", "opposite"}
    same_sheet = [crossing for crossing in crossings if crossing.contributes_on_surface]
    assert len(same_sheet) == 1
    assert same_sheet[0].orientation == 1
    assert sampled_intersection_number(a_cycle, b_cycle) == 1


def test_pendulum_cycles_measure_the_canonical_symplectic_form():
    cycles = cycle_system()
    intersections = sampled_intersection_form(cycles)
    periods = compute_period_matrix(cycles)
    profile = sampled_riemann_profile(periods, intersections)

    assert intersections.matrix == ((0, 1), (-1, 0))
    assert intersections.is_skew_symmetric
    assert intersections.is_unimodular
    assert intersections.is_canonical_symplectic
    assert abs(periods.tau[0][0] - 1j) < 1e-8
    assert profile.passes


def test_reversing_b_cycle_flips_pairing_and_period_orientation():
    original = cycle_system()
    reversed_cycles = AbelianCycleSystem(
        original.curve,
        original.a_cycles,
        (reversed_lift(original.b_cycles[0]),),
    )

    intersections = sampled_intersection_form(reversed_cycles)
    periods = compute_period_matrix(reversed_cycles)
    profile = sampled_riemann_profile(periods, intersections)

    assert intersections.matrix == ((0, -1), (1, 0))
    assert not intersections.is_canonical_symplectic
    assert abs(periods.tau[0][0] + 1j) < 1e-8
    assert periods.imaginary_part[0][0] < 0
    assert not periods.riemann_shape_passes()
    assert not profile.passes
