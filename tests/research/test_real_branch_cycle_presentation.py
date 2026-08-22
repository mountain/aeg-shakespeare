"""Real branch cuts: branch order -> symplectic cycles -> genus-two period data.

Question
--------
The previous global-history calibrations measured intersection forms and period
matrices only after A/B cycles had been hand supplied.  Can the branch geometry
itself emit a cycle presentation whose symplectic pairing is known before any
numerical integration is performed?

Primitive data
--------------
We use the real-split genus-two process quotient

    C: y^2 = (x+3)(x+2)(x+1)(x-1)(x-2)(x-3),

with the six ordered real branch points

    -3 < -2 < -1 < 1 < 2 < 3.

The test supplies the curve and this ordered branch locus.  It does *not* supply
an A/B homology basis, a period matrix, theta functions, or a Jacobian.

Classical lineage
-----------------
A hyperelliptic surface may be represented as a two-sheeted cover cut between
paired branch points.  For prescribed cuts the homology basis can be fixed from
the branch configuration, and periods of the canonical differentials can then
be computed on those cycles.  See [Farkas-Kra-1992] and the computational
branch-point/cut construction in [Frauendiener-Klein-2015], especially the
introduction and Section 2.  The latter explicitly treats hyperelliptic surfaces
from branch-point lists and constructs a canonical homology basis algorithmically.

Shakespeare reconstruction
---------------------------
The branch order first produces three adjacent cuts

    [-3,-2], [-1,1], [2,3],

where the last pair is used as a reference cut.  The emitted cycles are

    a1: around {-3,-2},        b1: around {-2,-1,1,2},
    a2: around {-1,1},         b2: around {1,2}.

The B-contours are nested.  In this real-cut presentation each ``a_i`` meets
only its dual ``b_i`` on the lifted surface, so the construction target is

        [ 0  0  1  0 ]
    J = [ 0  0  0  1 ]
        [-1  0  0  0 ]
        [ 0 -1  0  0 ].

The library then materializes those combinatorial cycles as base ellipses,
continues the square-root sheet history, measures the actual sampled
intersection form, integrates ``dx/y`` and ``x dx/y``, and normalizes the
resulting A/B period blocks.

**Shakespeare interpretation.**  This is the first step where the global
history grammar is generated from quotient singularity/branch data rather than
being chosen manually.  The topological pairing is a construction certificate;
the sampled paths are a numerical realization that can independently fail the
certificate if the continuation or contour geometry is wrong.

Calibration statement
---------------------
Passing this file certifies for this real-split genus-two curve:

1. the branch order emits two A-specifications and two nested B-specifications;
2. all four emitted base contours close after square-root continuation;
3. the sampled lifted intersection matrix agrees with the exact construction
   target ``[[0,I],[-I,0]]``;
4. the resulting 2x2 normalized period matrix is numerically symmetric with
   positive-definite imaginary part;
5. therefore, for this calibration, branch data -> constructed symplectic
   histories -> Riemann-shaped period data is executable without a hand-entered
   cycle basis.

Proof map
---------
``test_real_branch_order_emits_exact_cycle_combinatorics`` checks item 1 and the
construction-level symplectic certificate.
``test_constructed_genus_two_cycles_realize_the_certificate`` checks items 2-3.
``test_constructed_genus_two_cycles_feed_a_riemann_shaped_period_matrix`` checks
item 4 and combines it with the sampled topological evidence.

Boundary
--------
This does not solve homology construction for arbitrary complex branch loci.
The real branch points are supplied in sorted order, the numerical contours are
elliptic realizations of a known cut presentation, and the intersection engine
remains sampled rather than homotopy-certified.  A passing test therefore does
not establish a general automatic Jacobian constructor.  It establishes the
restricted but nontrivial real-split ``branch data -> symplectic cycles`` bridge
needed before that generalization.

References
----------
[Farkas-Kra-1992] H. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.

[Frauendiener-Klein-2015] J. Frauendiener and C. Klein, “Computational approach
to hyperelliptic Riemann surfaces”, *Letters in Mathematical Physics* 105
(2015), 379-400. DOI: 10.1007/s11005-015-0743-4; arXiv:1408.2201.
"""

import sympy as sp

from aeg_shakespeare.analysis.abelian import (
    canonical_symplectic_form,
    compute_period_matrix,
    construct_real_branch_cycles,
    real_branch_cut_presentation,
    sampled_intersection_form,
    sampled_riemann_profile,
)
from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile


def real_split_genus_two():
    x, y = sp.symbols("x y")
    roots = (-3.0, -2.0, -1.0, 1.0, 2.0, 3.0)
    polynomial = sp.expand((x + 3) * (x + 2) * (x + 1) * (x - 1) * (x - 2) * (x - 3))
    curve = hyperelliptic_profile(x, y, polynomial)
    presentation = real_branch_cut_presentation(curve, roots)
    return curve, presentation


def test_real_branch_order_emits_exact_cycle_combinatorics():
    curve, presentation = real_split_genus_two()

    assert curve.generic_genus == 2
    assert [(s.left_branch_index, s.right_branch_index) for s in presentation.a_specs] == [
        (0, 1),
        (2, 3),
    ]
    assert [(s.left_branch_index, s.right_branch_index) for s in presentation.b_specs] == [
        (1, 4),
        (3, 4),
    ]
    assert presentation.reference_cut == (2.0, 3.0)
    assert presentation.construction_intersection_form == canonical_symplectic_form(2)


def test_constructed_genus_two_cycles_realize_the_certificate():
    _, presentation = real_split_genus_two()
    constructed = construct_real_branch_cycles(presentation, samples=512)
    cycles = constructed.cycle_system

    assert all(cycle.lifted_closed for cycle in cycles.a_cycles + cycles.b_cycles)

    measured = sampled_intersection_form(cycles, sheet_tolerance=2e-3)
    assert measured.matrix == constructed.construction_intersection_form
    assert measured.is_canonical_symplectic


def test_constructed_genus_two_cycles_feed_a_riemann_shaped_period_matrix():
    _, presentation = real_split_genus_two()
    constructed = construct_real_branch_cycles(presentation, samples=768)
    cycles = constructed.cycle_system

    intersections = sampled_intersection_form(cycles, sheet_tolerance=2e-3)
    periods = compute_period_matrix(cycles)
    riemann = sampled_riemann_profile(periods, intersections)

    assert periods.genus == 2
    assert periods.symmetry_residual < 2e-3
    assert periods.imaginary_part_positive_definite(tolerance=1e-6)
    assert intersections.matrix == canonical_symplectic_form(2)
    assert riemann.passes
