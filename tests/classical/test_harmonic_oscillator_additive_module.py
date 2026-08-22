"""Oscillator I: finite process closure exposes an additive module before spectrum.

Question
--------
If Shakespeare is given the harmonic-oscillator process but no eigenmodes or
Fourier language, does the existing generated-grammar machinery recover a tiny
process presentation whose essential closure operation is additive/scalar
combination?

Primitive data
--------------
The program receives two scalar assignments and one local process generator

    D x = p,
    D p = -x.

The discovery run starts from the single seed ``x``.  The existing generated-
grammar backend is explicitly allowed to test membership in finite scalar
linear spans.  This additive-span policy is an assumption of the calibration;
the vignette does **not** claim to derive addition itself from the process.

No ambient basis, action matrix, eigenvector, eigenvalue, complex coordinate,
trigonometric solution, Fourier mode, or frequency template is supplied.

Classical lineage
-----------------
The harmonic oscillator is the canonical two-dimensional linear Hamiltonian
system.  In standard treatments its evolution may be described by matrices,
complex exponentials, normal modes, or trigonometric functions; see
[Arnold-1989].  The finite-dimensional linear-algebra background for basis
change and invariant linear maps is standard; see [Axler-2015].

Shakespeare reconstruction
---------------------------
The order is reversed.  Starting only from ``x``, process application produces

    x -> p -> -x.

The first image adds a new independent additive direction; the next lies back
in the span already generated.  Thus the smallest discovered additive process
grammar has dimension two and closes after one new history direction.

Only after closure does Shakespeare discover the process-return relation

    D^2 + 1 = 0.

The relation is primary.  This vignette deliberately stops before interpreting
its roots as eigenvalues or introducing complex exponential functions.

A second run starts from ``x+p`` rather than ``x``.  It discovers another
basis of the same two-dimensional additive grammar and the same process
relation.  The basis changes; the process relation does not.  This is a small
red-team check against confusing a convenient coordinate basis with the
process presentation itself.

Calibration statement
---------------------
Passing this file certifies that:

1. the seed ``x`` grows to the exact closed grammar ``span{x,p}`` without a
   caller-supplied ambient basis;
2. the process action has additive coordinates ``D x = p`` and ``D p = -x`` in
   the discovered grammar;
3. the shortest grammar-wide relation is exactly ``D^2+1``;
4. starting from ``x+p`` yields a different generated basis of the same
   two-dimensional span;
5. the alternative basis has the same discovered process relation.

Proof map
---------
``test_oscillator_grows_minimal_additive_process_module`` checks closure,
action coordinates, and the relation.  ``test_relation_survives_seed_basis_change``
checks the representation-accident red team.

New reusable abstraction
-------------------------
None.  This is intentional.  The existing ``GeneratedGrammar`` and relation
machinery already express the required finite additive closure.  A new public
module abstraction should not be added merely to rename a structure already
represented adequately.

Unresolved manual choice
------------------------
The generated-grammar backend itself treats finite scalar linear span as its
closure/equivalence policy.  This vignette shows that the policy is exceptionally
cheap for the harmonic oscillator; it does not explain why additive span should
be privileged for arbitrary processes.  Later translation and A/M examples
must probe that boundary.

Boundary
--------
This test establishes neither a spectral theorem nor Fourier analysis.  It does
not factor ``D^2+1`` over the complex numbers, introduce eigenvectors, or claim
that every useful representation is additive.  Those are deliberately later
questions.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[Axler-2015] Sheldon Axler, *Linear Algebra Done Right*, 3rd ed., Springer,
2015.
"""

import sympy as sp

from aeg_shakespeare import (
    ProcessSystem,
    coefficient_vector,
    discover_generated_presentation,
)


def _oscillator():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="D")


def test_oscillator_grows_minimal_additive_process_module():
    x, p, system = _oscillator()
    presentation = discover_generated_presentation(system, (x,))

    assert presentation.complete
    assert presentation.grammar.closed
    assert presentation.grammar.dimension == 2
    assert presentation.grammar.basis == (x, p)
    assert presentation.grammar.depths == (0, 1)
    assert presentation.grammar.growth_profile() == (1, 2)

    basis = presentation.grammar.basis
    assert tuple(coefficient_vector(system.derive(x), basis, (x, p))) == (
        sp.Integer(0),
        sp.Integer(1),
    )
    assert tuple(coefficient_vector(system.derive(p), basis, (x, p))) == (
        sp.Integer(-1),
        sp.Integer(0),
    )

    assert presentation.relations is not None
    D = sp.Symbol("D")
    assert sp.expand(
        presentation.relations.global_relation.as_expr(D) - (D**2 + 1)
    ) == 0


def test_relation_survives_seed_basis_change():
    x, p, system = _oscillator()
    canonical = discover_generated_presentation(system, (x,))
    rotated = discover_generated_presentation(system, (x + p,))

    assert canonical.complete and rotated.complete
    assert canonical.grammar.dimension == rotated.grammar.dimension == 2
    assert rotated.grammar.basis == (x + p, -x + p)

    columns = [
        coefficient_vector(item, canonical.grammar.basis, (x, p))
        for item in rotated.grammar.basis
    ]
    assert sp.Matrix.hstack(*columns).det() != 0

    D = sp.Symbol("D")
    assert canonical.relations is not None and rotated.relations is not None
    assert sp.expand(
        canonical.relations.global_relation.as_expr(D)
        - rotated.relations.global_relation.as_expr(D)
    ) == 0
    assert sp.expand(rotated.relations.global_relation.as_expr(D) - (D**2 + 1)) == 0
