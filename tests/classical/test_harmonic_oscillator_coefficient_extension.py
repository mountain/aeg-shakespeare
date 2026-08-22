"""Oscillator II: coefficient extension refines a process relation into one-dimensional primitives.

Question
--------
Once Oscillator I has discovered the additive grammar and the relation
``D^2+1=0``, what is the smallest next step toward spectral structure without
preloading eigenvalues or a spectral theorem?

Primitive data
--------------
This vignette receives the same harmonic-oscillator process

    D x = p,
    D p = -x,

and starts from the single seed ``x``.  The base discovery first recovers the
same two-dimensional additive grammar and the same process relation ``D^2+1``.

Only after that relation exists does the caller make one additional, explicit
representation proposal: enlarge the coefficient language by adjoining ``i``.
The extension is not chosen automatically by Shakespeare.

No action matrix, eigenvalue list, eigenvector template, complex oscillator
coordinate, sine/cosine solution, Fourier transform, or spectral theorem is
supplied.

Classical lineage
-----------------
Over the real/rational coefficient language the polynomial ``D^2+1`` remains
irreducible, while over the complex numbers it factors as

    (D-i)(D+i).

For the harmonic oscillator this leads to the familiar complex normal
coordinates.  See [Arnold-1989] for the oscillator and Hamiltonian background
and [Axler-2015] for the finite-dimensional linear-algebra perspective.

Shakespeare reconstruction
---------------------------
The process relation remains primary.  In the original coefficient language,
ordinary relation factorization returns one irreducible order-two factor.  The
caller then asks a separate representation question: what happens if ``i`` is
adjoined to the coefficient language?

The extended factorization produces

    D-i,
    D+i.

Existing relation-kernel discovery is then reused without a new spectral API.
Each order-one factor has a one-dimensional primitive grammar.  Up to nonzero
scalar multiples these primitives are

    x - i p,
    x + i p.

Only at the end may the classical reader recognize these as complex spectral
modes.  The executable claim itself is merely relation factorization plus exact
kernel discovery under an explicit coefficient extension.

Calibration statement
---------------------
Passing this file certifies that:

1. the oscillator relation ``D^2+1`` is discovered before the coefficient
   extension is proposed;
2. ordinary factorization keeps it as one order-two factor;
3. adjoining ``i`` refines it into the two order-one process factors ``D-i``
   and ``D+i``;
4. the corresponding exact relation kernels are one-dimensional and generated,
   up to scale, by ``x-i p`` and ``x+i p``;
5. those two primitives span the original additive grammar over the extended
   coefficient language and exactly reconstruct ``x`` and ``p``.

Proof map
---------
``test_complex_coefficient_extension_splits_oscillator_process_relation``
executes the relation -> explicit extension -> factors -> kernels -> decoder
chain.  Generic extension factorization is checked separately in
``tests/test_coefficient_extension.py``.

New reusable abstraction
-------------------------
One narrow operation only: factor an already-discovered process relation in a
caller-declared algebraic coefficient extension.  The operation attaches no
spectral semantics to the resulting factors.

Unresolved manual choice
------------------------
The extension by ``i`` is still a caller proposal.  Shakespeare does not yet
price the complexity of enlarging a coefficient language against the benefit
of splitting a higher-dimensional process module into smaller components.  A
later representation-cost calibration should decide when such an extension is
worth adopting.

Boundary
--------
This is not a spectral theorem and not Fourier analysis.  It does not define a
spectrum for arbitrary operators, does not choose algebraic closures
automatically, and does not claim that one-dimensional relation factors are the
right representation for every task.  It is one controlled bridge from process
relation to a classical spectral shadow.

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
from aeg_shakespeare.process.local import ProcessSystem


def _proportional(left, right, variables):
    left_poly = sp.Poly(sp.expand(left), *variables)
    right_poly = sp.Poly(sp.expand(right), *variables)
    monomials = sorted(
        set(left_poly.monoms()) | set(right_poly.monoms()),
        reverse=True,
    )
    left_vector = sp.Matrix([left_poly.coeff_monomial(m) for m in monomials])
    right_vector = sp.Matrix([right_poly.coeff_monomial(m) for m in monomials])
    return left_vector != sp.zeros(len(monomials), 1) and sp.Matrix.hstack(
        left_vector, right_vector
    ).rank() == 1


def test_complex_coefficient_extension_splits_oscillator_process_relation():
    x, p = sp.symbols("x p")
    system = ProcessSystem((x, p), {x: p, p: -x}, name="D")
    presentation = discover_generated_presentation(system, (x,))

    assert presentation.complete
    assert presentation.relations is not None
    relation = presentation.relations.global_relation
    D = sp.Symbol("D")
    assert sp.expand(relation.as_expr(D) - (D**2 + 1)) == 0

    base_factors = factor_process_relation(relation)
    assert len(base_factors) == 1
    assert sp.expand(base_factors[0].as_expr(D) - (D**2 + 1)) == 0

    factors = factor_process_relation_over_extension(relation, sp.I)
    assert {sp.expand(factor.as_expr(D)) for factor in factors} == {
        D - sp.I,
        D + sp.I,
    }

    kernels = tuple(
        discover_relation_kernel(
            system,
            presentation.grammar.basis,
            factor.coefficients,
        )
        for factor in factors
    )
    assert all(kernel.order == 1 for kernel in kernels)
    assert all(len(kernel.primitives) == 1 for kernel in kernels)

    primitives = tuple(kernel.primitives[0] for kernel in kernels)
    assert any(_proportional(item, x - sp.I * p, (x, p)) for item in primitives)
    assert any(_proportional(item, x + sp.I * p, (x, p)) for item in primitives)

    for factor, kernel in zip(factors, kernels):
        primitive = kernel.primitives[0]
        scalar = sp.simplify(-factor.coefficients[0] / factor.coefficients[1])
        assert scalar in (sp.I, -sp.I)
        assert sp.simplify(system.derive(primitive) - scalar * primitive) == 0

    x_coordinates = decompose(x, primitives, (x, p))
    p_coordinates = decompose(p, primitives, (x, p))
    reconstructed_x = sp.expand(
        sum(coefficient * primitive for coefficient, primitive in zip(x_coordinates, primitives))
    )
    reconstructed_p = sp.expand(
        sum(coefficient * primitive for coefficient, primitive in zip(p_coordinates, primitives))
    )
    assert sp.simplify(reconstructed_x - x) == 0
    assert sp.simplify(reconstructed_p - p) == 0
