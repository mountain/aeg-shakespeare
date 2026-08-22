"""Oscillator III red team: finer relation splitting is not automatically a cheaper presentation.

Question
--------
Oscillator II showed that enlarging the coefficient language can split a
higher-order process relation into one-dimensional kernels.  Does that imply
that the finest available splitting should automatically be preferred?

Primitive data
--------------
We use two independent harmonic processes with distinct squared frequencies,

    D x1 = p1,   D p1 = -x1,
    D x2 = p2,   D p2 = -2 x2,

and the mixed seed ``x1+x2``.  The existing additive-span closure policy is
retained from Oscillator I.  No eigenvalues, eigenvectors, Fourier basis, or
preferred coefficient extension is supplied.

Classical lineage
-----------------
A direct sum of two uncoupled oscillators has two quadratic frequency factors.
Over a coefficient language containing ``i`` and ``sqrt(2)``, those quadratics
split further into four linear factors.  This is elementary finite-dimensional
linear algebra; see [Arnold-1989] for oscillator mechanics and [Axler-2015] for
the linear-algebraic background.

Shakespeare reconstruction
---------------------------
The process first grows its finite additive grammar and discovers the single
grammar-wide relation

    (D^2+1)(D^2+2) = 0.

Ordinary relation factorization produces two order-two components.  A separate
caller proposal then enlarges the coefficient language by adjoining ``i`` and
``sqrt(2)``; the same already-discovered relation refines into four order-one
components.  Both decompositions are exact and both span the same process
grammar.

The red-team point is that refinement improves one structural measure while
worsening another: maximum component relation order drops from 2 to 1, but the
number of components rises from 2 to 4.  A calibration-only Pareto profile maps
these two transparent quantities onto the existing ``relations`` and ``grammar``
cost axes.  Neither presentation dominates the other.  Different scalar weights
can prefer opposite presentations.

Calibration statement
---------------------
Passing this file certifies that:

1. the mixed seed discovers a four-dimensional exact additive grammar;
2. its shortest grammar-wide relation is ``D^4+3D^2+2``;
3. the base coefficient language yields two exact two-dimensional relation
   kernels for ``D^2+1`` and ``D^2+2``;
4. adjoining ``i`` and ``sqrt(2)`` yields four exact one-dimensional relation
   kernels whose primitives still span the original grammar;
5. the base decomposition uses only rational relation coefficients whereas the
   refined one genuinely uses the enlarged coefficient language;
6. under the explicit two-axis red-team profile, both presentations remain on
   the Pareto frontier and opposite scalar weightings can select opposite
   winners.

Proof map
---------
``test_finer_coefficient_splitting_is_not_automatically_cheaper`` executes the
full process -> relation -> base decomposition -> extended decomposition ->
exact spanning -> Pareto red-team chain.

New reusable abstraction
-------------------------
None.  The test deliberately reuses generated-grammar discovery, ordinary and
extended relation factorization, relation kernels, ``PresentationCost``, and
``pareto_frontier``.

Unresolved manual choice
------------------------
Shakespeare still does not price coefficient-language complexity itself.  This
red team shows that no such new axis should be introduced merely to force one
winner: even before language cost is counted, the two exact presentations trade
component count against relation order.  A later task-specific calibration must
say what kind of compression is actually valuable.

Boundary
--------
The calibration-only profile is not proposed as a universal cost model.
Component count is mapped to ``grammar`` and maximum component order to
``relations`` only to exhibit a concrete non-dominance witness.  The test does
not claim that those two statistics exhaust representation cost, and it does
not establish a general spectral theorem or a universal preference for real or
complex coefficient languages.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[Axler-2015] Sheldon Axler, *Linear Algebra Done Right*, 3rd ed., Springer,
2015.
"""

import sympy as sp

from aeg_shakespeare.discovery import factor_process_relation_over_extension
from aeg_shakespeare.presentation.grammar import discover_generated_presentation
from aeg_shakespeare.presentation.relations import (
    decompose,
    discover_relation_kernel,
    factor_process_relation,
)
from aeg_shakespeare.presentation.search import (
    PresentationCandidate,
    PresentationCost,
    pareto_frontier,
)
from aeg_shakespeare.process.local import ProcessSystem


def _reconstruct(coefficients, primitives):
    return sp.expand(
        sum(
            coefficient * primitive
            for coefficient, primitive in zip(coefficients, primitives)
        )
    )


def test_finer_coefficient_splitting_is_not_automatically_cheaper():
    x1, p1, x2, p2 = sp.symbols("x1 p1 x2 p2")
    system = ProcessSystem(
        (x1, p1, x2, p2),
        {
            x1: p1,
            p1: -x1,
            x2: p2,
            p2: -2 * x2,
        },
        name="D",
    )

    presentation = discover_generated_presentation(system, (x1 + x2,))
    assert presentation.complete
    assert presentation.grammar.dimension == 4
    assert presentation.relations is not None

    D = sp.Symbol("D")
    global_relation = presentation.relations.global_relation
    assert sp.expand(global_relation.as_expr(D) - (D**4 + 3 * D**2 + 2)) == 0

    base_factors = factor_process_relation(global_relation)
    assert {sp.expand(factor.as_expr(D)) for factor in base_factors} == {
        D**2 + 1,
        D**2 + 2,
    }
    base_kernels = tuple(
        discover_relation_kernel(system, presentation.grammar.basis, factor.coefficients)
        for factor in base_factors
    )
    assert sorted(len(kernel.primitives) for kernel in base_kernels) == [2, 2]
    assert all(
        coefficient.is_Rational is True
        for factor in base_factors
        for coefficient in factor.coefficients
    )

    extended_factors = factor_process_relation_over_extension(
        global_relation,
        [sp.I, sp.sqrt(2)],
    )
    expected_extended = {
        sp.expand(D - sp.I),
        sp.expand(D + sp.I),
        sp.expand(D - sp.I * sp.sqrt(2)),
        sp.expand(D + sp.I * sp.sqrt(2)),
    }
    assert {sp.expand(factor.as_expr(D)) for factor in extended_factors} == expected_extended

    extended_kernels = tuple(
        discover_relation_kernel(system, presentation.grammar.basis, factor.coefficients)
        for factor in extended_factors
    )
    assert all(len(kernel.primitives) == 1 for kernel in extended_kernels)
    extended_primitives = tuple(
        primitive
        for kernel in extended_kernels
        for primitive in kernel.primitives
    )
    assert len(extended_primitives) == 4

    for basis_item in presentation.grammar.basis:
        coordinates = decompose(basis_item, extended_primitives, system.assignments)
        assert sp.simplify(_reconstruct(coordinates, extended_primitives) - basis_item) == 0

    assert any(
        coefficient.is_Rational is not True
        for factor in extended_factors
        for coefficient in factor.coefficients
    )
    assert any(
        sp.sympify(coefficient).has(sp.I)
        for factor in extended_factors
        for coefficient in factor.coefficients
    )

    # Red-team profile only: fewer components versus lower maximum relation order.
    base_candidate = PresentationCandidate(
        payload="base coefficients",
        label="two quadratic components",
        cost=PresentationCost(
            grammar=float(len(base_factors)),
            relations=float(max(factor.order for factor in base_factors)),
        ),
    )
    refined_candidate = PresentationCandidate(
        payload="extended coefficients",
        label="four linear components",
        cost=PresentationCost(
            grammar=float(len(extended_factors)),
            relations=float(max(factor.order for factor in extended_factors)),
        ),
    )

    assert base_candidate.cost.grammar < refined_candidate.cost.grammar
    assert base_candidate.cost.relations > refined_candidate.cost.relations
    assert not base_candidate.cost.dominates(refined_candidate.cost)
    assert not refined_candidate.cost.dominates(base_candidate.cost)

    frontier = pareto_frontier((base_candidate, refined_candidate))
    assert {candidate.label for candidate in frontier} == {
        "two quadratic components",
        "four linear components",
    }

    # Equal weights prefer fewer components; relation-heavy weights prefer finer splitting.
    assert base_candidate.cost.scalarize() < refined_candidate.cost.scalarize()
    relation_heavy = {"grammar": 1.0, "relations": 4.0}
    assert (
        refined_candidate.cost.scalarize(relation_heavy)
        < base_candidate.cost.scalarize(relation_heavy)
    )
