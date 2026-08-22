"""Braids: local algebra and Markov moves as presentation morphisms.

Question
--------
After KdV and resistor networks, does the same presentation-morphism pressure
survive when the preserved semantics is topological rather than analytic or
linear-response data?

Primitive data
--------------
A research-local braid presentation is a strand count and a word in signed Artin
generators.  Two exact observers are used:

1. the reduced Burau matrix, which represents the braid-group element; and
2. the Alexander polynomial of the standard closure, computed from the reduced
   Burau matrix by the classical closed-braid formula.

No braid, knot, link, Markov, or Alexander object is added to the Shakespeare
public API.

Classical lineage
-----------------
Artin braid relations give alternative words for the same braid.  Markov's
theorem says that closures represent the same oriented link precisely up to
braid isotopy together with conjugation and stabilization/destabilization.  The
Alexander polynomial of a closed braid can be recovered, up to Laurent units,
from the reduced Burau representation.  See [Birman-1974] in
``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
Three morphism levels are calibrated independently.

* The braid relation ``sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2`` preserves
  the full reduced Burau matrix: a syntactic history rewrite inside one
  presentation space.
* Conjugation preserves the closed-link Alexander semantics even though the
  Burau matrices themselves are generally different.
* Positive Markov stabilization sends a two-strand trefoil presentation into a
  three-strand presentation.  The source and target state spaces have different
  dimensions, yet the closure Alexander polynomial agrees exactly.

This is the first calibration in which a semantics-preserving morphism changes
*which presentation space the object inhabits*.

Red team
--------
Component count of a braid closure is a genuine topological observable but an
incomplete one.  The one-crossing two-braid closes to an unknot, while the
three-crossing two-braid closes to a trefoil.  Both induced permutations have a
single cycle, so both closures have one component; their Alexander polynomials
are different.  A weak topological quotient therefore cannot certify a general
presentation morphism.

Calibration statement
---------------------
Passing this file certifies that:

1. the B3 braid relation has identical exact reduced Burau matrices;
2. conjugate braid presentations can have different matrices but the same
   closure Alexander polynomial;
3. Markov stabilization can change strand number/matrix dimension while
   preserving closure semantics; and
4. equality of component count is strictly weaker than equality of the chosen
   closure invariant.

Claim boundary
--------------
This is not a knot-equivalence solver.  The Alexander polynomial is not a
complete link invariant, and the test does not implement Reidemeister diagrams,
Markov search, Jones/HOMFLY invariants, braid normal forms, or a generic topology
API.  Its role is to test whether presentation morphisms must be task-relative
and may cross representation spaces of different dimensions.
"""

from __future__ import annotations

import sympy as sp

T = sp.Symbol("t")
BraidWord = tuple[int, ...]


def unreduced_burau_generator(strands: int, generator: int) -> sp.Matrix:
    if strands < 2:
        raise ValueError("Burau calibration requires at least two strands")
    if not 1 <= generator < strands:
        raise ValueError("generator index must satisfy 1 <= i < strands")
    matrix = sp.eye(strands)
    start = generator - 1
    block = sp.Matrix(((1 - T, T), (1, 0)))
    for row in range(2):
        for column in range(2):
            matrix[start + row, start + column] = block[row, column]
    return matrix


def reduced_burau_generator(strands: int, generator: int) -> sp.Matrix:
    """Induce Burau on the quotient by the invariant all-ones vector."""

    unreduced = unreduced_burau_generator(strands, generator)
    columns: list[sp.Matrix] = []
    for basis_index in range(strands - 1):
        vector = sp.zeros(strands, 1)
        vector[basis_index] = 1
        image = unreduced * vector
        last = image[strands - 1]
        columns.append(
            sp.Matrix(
                [
                    sp.expand(image[index] - last)
                    for index in range(strands - 1)
                ]
            )
        )
    return sp.Matrix.hstack(*columns)


def reduced_burau_matrix(strands: int, word: BraidWord) -> sp.Matrix:
    matrix = sp.eye(strands - 1)
    for signed_generator in word:
        generator = abs(signed_generator)
        factor = reduced_burau_generator(strands, generator)
        if signed_generator < 0:
            factor = factor.inv()
        matrix = (matrix * factor).applyfunc(sp.cancel)
    return matrix


def closure_alexander(strands: int, word: BraidWord) -> sp.Expr:
    """Closed-braid Alexander expression in the current Burau convention."""

    burau = reduced_burau_matrix(strands, word)
    determinant = sp.det(sp.eye(strands - 1) - burau)
    return sp.factor(
        sp.cancel((1 - T) * determinant / (1 - T**strands))
    )


def braid_permutation(strands: int, word: BraidWord) -> tuple[int, ...]:
    permutation = list(range(strands))
    for signed_generator in word:
        generator = abs(signed_generator)
        if not 1 <= generator < strands:
            raise ValueError("generator index must satisfy 1 <= i < strands")
        left = generator - 1
        right = generator
        permutation[left], permutation[right] = (
            permutation[right],
            permutation[left],
        )
    return tuple(permutation)


def permutation_cycle_count(permutation: tuple[int, ...]) -> int:
    seen: set[int] = set()
    cycles = 0
    for start in range(len(permutation)):
        if start in seen:
            continue
        cycles += 1
        current = start
        while current not in seen:
            seen.add(current)
            current = permutation[current]
    return cycles


def closure_component_count(strands: int, word: BraidWord) -> int:
    return permutation_cycle_count(braid_permutation(strands, word))


def test_braid_relation_is_a_syntactic_presentation_morphism():
    left = (1, 2, 1)
    right = (2, 1, 2)

    left_matrix = reduced_burau_matrix(3, left)
    right_matrix = reduced_burau_matrix(3, right)

    assert left != right
    assert left_matrix == right_matrix
    assert closure_alexander(3, left) == closure_alexander(3, right)


def test_markov_conjugation_preserves_closure_semantics_not_matrix_syntax():
    # A three-strand trefoil presentation, obtained by stabilizing sigma_1^3.
    braid = (1, 1, 1, 2)
    conjugator = (2,)
    conjugate = conjugator + braid + (-2,)

    original_matrix = reduced_burau_matrix(3, braid)
    conjugate_matrix = reduced_burau_matrix(3, conjugate)

    assert original_matrix != conjugate_matrix
    assert closure_alexander(3, braid) == T**2 - T + 1
    assert closure_alexander(3, conjugate) == T**2 - T + 1


def test_markov_stabilization_crosses_presentation_spaces():
    two_strand_trefoil = (1, 1, 1)
    stabilized_three_strand = (1, 1, 1, 2)

    two_matrix = reduced_burau_matrix(2, two_strand_trefoil)
    three_matrix = reduced_burau_matrix(3, stabilized_three_strand)

    # The morphism changes the representation dimension: equality cannot mean
    # matrix equality or a rewrite inside one fixed alphabet/state space.
    assert two_matrix.shape == (1, 1)
    assert three_matrix.shape == (2, 2)

    assert closure_alexander(2, two_strand_trefoil) == T**2 - T + 1
    assert closure_alexander(3, stabilized_three_strand) == T**2 - T + 1
    assert closure_component_count(2, two_strand_trefoil) == 1
    assert closure_component_count(3, stabilized_three_strand) == 1


def test_component_count_is_too_weak_for_presentation_equivalence_red_team():
    one_crossing_unknot = (1,)
    three_crossing_trefoil = (1, 1, 1)

    assert closure_component_count(2, one_crossing_unknot) == 1
    assert closure_component_count(2, three_crossing_trefoil) == 1

    assert closure_alexander(2, one_crossing_unknot) == 1
    assert closure_alexander(2, three_crossing_trefoil) == T**2 - T + 1
    assert closure_alexander(2, one_crossing_unknot) != closure_alexander(
        2,
        three_crossing_trefoil,
    )
