"""KdV tau combinatorics and history rewriting as independent presentations.

Question
--------
The previous Level-2 calibration inserted Hirota's classical pair factor into a
research-local history rewrite and showed that the three-soliton critical pair
joins.  Can a *different* representation of the same KdV sector force the same
pair data independently, and can the two presentations be shown to commute?

Primitive data for this calibration
-----------------------------------
This file starts from the standard Hirota bilinear KdV equation

    (D_x D_t + D_x^4) tau . tau = 0

and exponential plane-wave labels with dispersion

    omega_i = -k_i^3.

For an exponential term indexed by a subset S of solitons, write

    K_S     = sum_{i in S} k_i,
    Omega_S = -sum_{i in S} k_i^3.

Hirota's bilinear operator then acts on two such exponentials by the exact
kernel

    (K_S-K_T)(Omega_S-Omega_T) + (K_S-K_T)^4.

No pair interaction coefficient is inserted when solving the two-soliton
sector.  The coefficient A_12 is left unknown and solved from the bilinear
coefficient of the mixed exponential.  Likewise, after the three pair
coefficients have been fixed independently, the coefficient C_123 of the
three-soliton exponential is left unknown and solved from the three-body
bilinear sector.

Classical lineage
-----------------
Hirota's direct method converts KdV into a bilinear equation and gives exact
N-soliton solutions.  In the usual N-soliton tau polynomial the coefficient of
a subset is the product of pair factors

    A_ij = ((k_i-k_j)/(k_i+k_j))^2.

See [Hirota-1971] and [Ablowitz-Segur-1981] in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The point of this vignette is not to assume that factorization.  It asks whether
it is forced by the bilinear presentation and then compares the answer with the
independent history-rewrite presentation:

    Hirota bilinear semantics
        -> solve A_ij
        -> solve C_123

    history rewrite semantics
        -> three adjacent pair crossings
        -> product of pair interaction factors.

The desired commuting square is

    C_123 from tau  ==  product of factors carried by either braid history.

This compares representation-level residuals without evaluating the physical
field u(x,t).

Red team
--------
The red team keeps *all* one- and two-body tau coefficients unchanged but
multiplies the three-body coefficient by an irreducible factor gamma != 1.
Pairwise history rewriting therefore remains locally valid and confluent, yet it
can no longer reconstruct the tau presentation.  The Hirota three-body sector
also acquires a nonzero residual.

This separates two requirements:

    pairwise rewrite confluence                    necessary local/global law
    absence of irreducible higher-body tau data    cross-presentation completeness

Thus confluence alone is not promoted to a universal definition of
integrability.

Claim boundary
--------------
This test does not discover the bilinear transformation from primitive KdV PDE
syntax, prove an arbitrary-N theorem, construct the physical field from tau, or
promote a tau-function API.  It gives a second, algebraically independent
calibration of the pair residual and shows that the three-soliton coefficient
is forced to factor into exactly those pair data.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Literal, Sequence

import sympy as sp

from aeg_shakespeare.process.history import ProcessWord


@dataclass(frozen=True)
class TauTerm:
    """One exponential support term of a finite Hirota tau polynomial."""

    subset: tuple[int, ...]
    coefficient: sp.Expr


@dataclass(frozen=True)
class RewriteToken:
    """Minimal visible token for the independent history presentation."""

    name: str
    rank: int
    k: sp.Expr


@dataclass(frozen=True)
class RewriteTrace:
    normal_form: ProcessWord[RewriteToken]
    positions: tuple[int, ...]
    interaction_factors: tuple[sp.Expr, ...]

    @property
    def total_interaction_factor(self) -> sp.Expr:
        return sp.factor(sp.prod(self.interaction_factors))


RewritePreference = Literal["leftmost", "rightmost"]


def spectral_signature(
    subset: Sequence[int],
    wave_numbers: Sequence[sp.Expr],
) -> tuple[sp.Expr, sp.Expr]:
    """Return ``(K_S, Omega_S)`` for one exponential support subset."""

    K = sum((wave_numbers[index] for index in subset), sp.S.Zero)
    omega = -sum((wave_numbers[index] ** 3 for index in subset), sp.S.Zero)
    return sp.expand(K), sp.expand(omega)


def hirota_kernel(
    left: TauTerm,
    right: TauTerm,
    wave_numbers: Sequence[sp.Expr],
) -> sp.Expr:
    """Kernel of ``D_x D_t + D_x^4`` on a pair of exponential terms."""

    left_k, left_omega = spectral_signature(left.subset, wave_numbers)
    right_k, right_omega = spectral_signature(right.subset, wave_numbers)
    delta_k = sp.expand(left_k - right_k)
    delta_omega = sp.expand(left_omega - right_omega)
    return sp.expand(delta_k * delta_omega + delta_k**4)


def combined_occupancy(
    left: Sequence[int],
    right: Sequence[int],
    *,
    size: int,
) -> tuple[int, ...]:
    counts = [0] * size
    for index in tuple(left) + tuple(right):
        counts[index] += 1
    return tuple(counts)


def bilinear_sector_coefficient(
    terms: Sequence[TauTerm],
    occupancy: Sequence[int],
    wave_numbers: Sequence[sp.Expr],
) -> sp.Expr:
    """Collect one exponential-occupancy sector of the bilinear equation."""

    target = tuple(occupancy)
    total = sp.S.Zero
    for left in terms:
        for right in terms:
            if combined_occupancy(
                left.subset,
                right.subset,
                size=len(wave_numbers),
            ) != target:
                continue
            total += (
                left.coefficient
                * right.coefficient
                * hirota_kernel(left, right, wave_numbers)
            )
    return sp.factor(total)


def subset_tau_terms(
    size: int,
    coefficient,
) -> tuple[TauTerm, ...]:
    """Enumerate the Boolean support of an N-soliton-type tau polynomial."""

    terms: list[TauTerm] = []
    for degree in range(size + 1):
        for subset in combinations(range(size), degree):
            terms.append(TauTerm(subset, sp.sympify(coefficient(subset))))
    return tuple(terms)


def solve_two_body_factor(k1: sp.Expr, k2: sp.Expr) -> sp.Expr:
    """Derive A_12 from the mixed two-body Hirota sector."""

    A = sp.Symbol("A")
    terms = subset_tau_terms(
        2,
        lambda subset: A if len(subset) == 2 else sp.S.One,
    )
    residual = bilinear_sector_coefficient(terms, (1, 1), (k1, k2))
    solutions = sp.solve(sp.Eq(residual, 0), A)
    assert len(solutions) == 1
    return sp.factor(solutions[0])


def solve_three_body_factor(
    wave_numbers: Sequence[sp.Expr],
    pair_factors: dict[tuple[int, int], sp.Expr],
) -> sp.Expr:
    """Derive C_123 after the three pair sectors have already been fixed."""

    if len(wave_numbers) != 3:
        raise ValueError("three-body factor requires exactly three wave numbers")
    C = sp.Symbol("C123")

    def coefficient(subset: tuple[int, ...]) -> sp.Expr:
        if len(subset) < 2:
            return sp.S.One
        if len(subset) == 2:
            return pair_factors[subset]
        return C

    terms = subset_tau_terms(3, coefficient)
    residual = bilinear_sector_coefficient(terms, (1, 1, 1), wave_numbers)
    solutions = sp.solve(sp.Eq(sp.together(residual), 0), C)
    assert len(solutions) == 1
    return sp.factor(solutions[0])


def classical_history_pair_factor(
    fast: RewriteToken,
    slow: RewriteToken,
) -> sp.Expr:
    """Pair factor used by the independent Level-2 history presentation."""

    if fast.rank <= slow.rank:
        raise ValueError("history pair factor expects a speed inversion")
    return sp.factor(((fast.k - slow.k) / (fast.k + slow.k)) ** 2)


def normalize_visible_history(
    history: ProcessWord[RewriteToken],
    *,
    preference: RewritePreference,
) -> RewriteTrace:
    """Normalize only visible order while accumulating interaction factors."""

    current = list(history.steps)
    positions: list[int] = []
    factors: list[sp.Expr] = []
    while True:
        inversions = [
            index
            for index in range(len(current) - 1)
            if current[index].rank > current[index + 1].rank
        ]
        if not inversions:
            break
        position = inversions[0] if preference == "leftmost" else inversions[-1]
        fast, slow = current[position], current[position + 1]
        factors.append(classical_history_pair_factor(fast, slow))
        positions.append(position)
        current[position : position + 2] = [slow, fast]
    return RewriteTrace(
        normal_form=ProcessWord(tuple(current)),
        positions=tuple(positions),
        interaction_factors=tuple(factors),
    )


def test_two_soliton_pair_factor_is_forced_by_hirota_bilinearity():
    k1, k2 = sp.symbols("k1 k2", nonzero=True)
    discovered = solve_two_body_factor(k1, k2)
    expected = sp.factor(((k1 - k2) / (k1 + k2)) ** 2)
    assert sp.factor(discovered - expected) == 0


def test_three_soliton_sector_forces_pair_factorization():
    k1, k2, k3 = sp.symbols("k1 k2 k3", nonzero=True)
    wave_numbers = (k1, k2, k3)
    pair_factors = {
        (0, 1): solve_two_body_factor(k1, k2),
        (0, 2): solve_two_body_factor(k1, k3),
        (1, 2): solve_two_body_factor(k2, k3),
    }
    discovered_three_body = solve_three_body_factor(wave_numbers, pair_factors)
    expected = sp.factor(sp.prod(pair_factors.values()))
    assert sp.factor(discovered_three_body - expected) == 0


def test_full_three_soliton_tau_passes_all_bilinear_support_sectors():
    # Exact integer wave numbers make this a cheap full-support certificate,
    # complementary to the symbolic pair/triple derivations above.
    wave_numbers = (sp.Integer(1), sp.Integer(2), sp.Integer(3))

    def pair_factor(i: int, j: int) -> sp.Expr:
        ki, kj = wave_numbers[i], wave_numbers[j]
        return sp.factor(((ki - kj) / (ki + kj)) ** 2)

    terms = subset_tau_terms(
        3,
        lambda subset: sp.prod(
            pair_factor(i, j) for i, j in combinations(subset, 2)
        ),
    )
    occupancies = {
        combined_occupancy(left.subset, right.subset, size=3)
        for left in terms
        for right in terms
    }
    residuals = {
        occupancy: bilinear_sector_coefficient(terms, occupancy, wave_numbers)
        for occupancy in occupancies
    }
    assert all(residual == 0 for residual in residuals.values())


def test_tau_and_history_presentations_commute_on_three_solitons():
    k1, k2, k3 = sp.symbols("k1 k2 k3", nonzero=True)
    pair_factors = {
        (0, 1): solve_two_body_factor(k1, k2),
        (0, 2): solve_two_body_factor(k1, k3),
        (1, 2): solve_two_body_factor(k2, k3),
    }
    tau_three_body = solve_three_body_factor((k1, k2, k3), pair_factors)

    history = ProcessWord(
        (
            RewriteToken("s3", 3, k3),
            RewriteToken("s2", 2, k2),
            RewriteToken("s1", 1, k1),
        )
    )
    left = normalize_visible_history(history, preference="leftmost")
    right = normalize_visible_history(history, preference="rightmost")

    assert left.positions == (0, 1, 0)
    assert right.positions == (1, 0, 1)
    assert tuple(token.name for token in left.normal_form) == ("s1", "s2", "s3")
    assert tuple(token.name for token in right.normal_form) == ("s1", "s2", "s3")
    assert sp.factor(left.total_interaction_factor - tau_three_body) == 0
    assert sp.factor(right.total_interaction_factor - tau_three_body) == 0
    assert sp.factor(left.total_interaction_factor - right.total_interaction_factor) == 0


def test_irreducible_three_body_tau_defect_breaks_cross_presentation_red_team():
    # Keep every one- and two-body coefficient unchanged.  Add only a genuinely
    # irreducible three-body weight.  Pairwise history confluence therefore
    # survives, but the tau presentation is no longer reconstructed by pair data.
    wave_numbers = (sp.Integer(1), sp.Integer(2), sp.Integer(3))
    gamma = sp.Integer(2)

    def pair_factor(i: int, j: int) -> sp.Expr:
        ki, kj = wave_numbers[i], wave_numbers[j]
        return sp.factor(((ki - kj) / (ki + kj)) ** 2)

    pair_product = sp.factor(
        pair_factor(0, 1) * pair_factor(0, 2) * pair_factor(1, 2)
    )
    fake_three_body = sp.factor(gamma * pair_product)

    def fake_coefficient(subset: tuple[int, ...]) -> sp.Expr:
        if len(subset) < 2:
            return sp.S.One
        if len(subset) == 2:
            i, j = subset
            return pair_factor(i, j)
        return fake_three_body

    fake_terms = subset_tau_terms(3, fake_coefficient)
    triple_residual = bilinear_sector_coefficient(
        fake_terms,
        (1, 1, 1),
        wave_numbers,
    )
    assert triple_residual != 0

    history = ProcessWord(
        (
            RewriteToken("s3", 3, wave_numbers[2]),
            RewriteToken("s2", 2, wave_numbers[1]),
            RewriteToken("s1", 1, wave_numbers[0]),
        )
    )
    left = normalize_visible_history(history, preference="leftmost")
    right = normalize_visible_history(history, preference="rightmost")

    # Pairwise rewrite confluence still holds because the red team did not touch
    # pair data.
    assert left.total_interaction_factor == right.total_interaction_factor
    assert sp.factor(left.total_interaction_factor - pair_product) == 0

    # But the cross-presentation square no longer commutes: a new irreducible
    # three-body generator would be required to reconstruct the fake tau weight.
    assert sp.factor(fake_three_body / left.total_interaction_factor - 1) == gamma - 1
