"""KdV soliton scattering as parametric history rewriting.

Question
--------
Can Shakespeare express the first genuinely multi-history feature of KdV
solitons without introducing a public ``Soliton`` or ``YangBaxter`` API: a
pairwise scattering rule whose visible histories reorder, whose phase residuals
are transported, and whose three-body critical pair is globally joinable?

Classical lineage
-----------------
Hirota's N-soliton solution of KdV is built from pair interaction factors

    A_ij = ((k_i - k_j) / (k_i + k_j))**2.

For two solitons with distinct positive wave numbers, the collision is elastic:
the wave numbers survive and only the asymptotic phase/position coordinates
shift.  For N solitons, the interaction factorizes into pair data.  See
[Hirota-1971] and [Ablowitz-Segur-1981] in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
This vignette deliberately keeps the new machinery local to the research test.
A ``SolitonStep`` is only a parameterized finite history token.  Its ``phase``
is the dimensionless asymptotic coordinate q = k*x0.  For an adjacent inversion
``fast slow`` with k_fast > k_slow, define

    L(fast, slow) = -log(A_fast,slow)

and rewrite

    (fast, q_f) (slow, q_s)
        ->
    (slow, q_s - L) (fast, q_f + L).

Thus the visible order swaps, the two wave numbers are unchanged, and the local
phase balance ``q_f + q_s`` is exactly preserved.  Decoding q back to a spatial
center gives the standard pair displacement ``Delta x = +/- L/k`` in this phase
normalization.

The three-soliton history ``3 2 1`` has one elementary critical pair: normalize
leftmost-first or rightmost-first.  The two paths are the braid words

    s1 s2 s1     and     s2 s1 s2.

For the KdV pair law, each unordered pair crosses exactly once and contributes a
state-independent additive residual.  Therefore both histories end in the same
visible order *and* the same phase coordinates.

Red team
--------
A fake pair law is then constructed which is hard to reject from two-body data:
it still swaps the visible pair and still preserves ``q_f+q_s`` exactly, but it
adds a small state-dependent defect

    L -> L + epsilon * (q_f - q_s).

Every local rewrite therefore retains the same two-body balance certificate.
Nevertheless the two three-body rewrite orders disagree.  This separates a
local conservation law from global confluence and shows why a future
``ConfluenceCertificate`` would carry mathematical content rather than merely
repackage deterministic normalization.

Claim boundary
--------------
This test does not derive the Hirota tau function from the KdV PDE, discover the
pair factor, or prove a general set-theoretic Yang-Baxter theorem.  It calibrates
one restricted parametric rewrite model against the classical KdV pair factor
and demonstrates that three-body joinability supplies information not visible
in two-body phase balance alone.  The parametric matcher and confluence report
remain research-local until another independent calibration forces the same
abstraction.

References
----------
[Hirota-1971] R. Hirota, "Exact Solution of the Korteweg--de Vries Equation for
Multiple Collisions of Solitons," Physical Review Letters 27 (1971), 1192--1194.
DOI: 10.1103/PhysRevLett.27.1192.

[Ablowitz-Segur-1981] M. J. Ablowitz and H. Segur, *Solitons and the Inverse
Scattering Transform*, SIAM, 1981.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import sympy as sp

from aeg_shakespeare.process.history import ProcessWord

RewritePreference = Literal["leftmost", "rightmost"]


@dataclass(frozen=True)
class SolitonStep:
    """Research-local asymptotic soliton token.

    ``rank`` records the known speed ordering for the calibration; the public
    process layer is not asked to infer an order relation on symbolic wave
    numbers.  ``phase`` is q=k*x0 rather than the physical center itself.
    """

    name: str
    rank: int
    k: sp.Expr
    phase: sp.Expr


@dataclass(frozen=True)
class ParametricRewriteStep:
    position: int
    before: tuple[SolitonStep, SolitonStep]
    after: tuple[SolitonStep, SolitonStep]
    interaction_factor: sp.Expr
    phase_transfer: sp.Expr
    phase_balance_residual: sp.Expr


@dataclass(frozen=True)
class ParametricNormalization:
    original: ProcessWord[SolitonStep]
    normal_form: ProcessWord[SolitonStep]
    trace: tuple[ParametricRewriteStep, ...]

    @property
    def visible_order(self) -> tuple[str, ...]:
        return tuple(step.name for step in self.normal_form)


def kdv_pair_interaction_factor(fast: SolitonStep, slow: SolitonStep) -> sp.Expr:
    """Return the classical Hirota pair factor A_ij for an ordered inversion."""

    if fast.rank <= slow.rank:
        raise ValueError("pair interaction expects fast.rank > slow.rank")
    return sp.factor(((fast.k - slow.k) / (fast.k + slow.k)) ** 2)


def rewrite_kdv_inversion(
    fast: SolitonStep,
    slow: SolitonStep,
    *,
    defect: sp.Expr = sp.S.Zero,
) -> tuple[SolitonStep, SolitonStep, sp.Expr, sp.Expr, sp.Expr]:
    """Swap one speed inversion and transport its pair phase residual.

    ``defect=0`` is the KdV calibration.  A nonzero value multiplies the
    state-dependent red-team term ``q_fast-q_slow`` while preserving the local
    phase sum exactly.
    """

    interaction = kdv_pair_interaction_factor(fast, slow)
    base_transfer = -sp.log(interaction)
    transfer = sp.expand(
        base_transfer + sp.sympify(defect) * (fast.phase - slow.phase)
    )

    moved_fast = SolitonStep(
        name=fast.name,
        rank=fast.rank,
        k=fast.k,
        phase=sp.expand(fast.phase + transfer),
    )
    moved_slow = SolitonStep(
        name=slow.name,
        rank=slow.rank,
        k=slow.k,
        phase=sp.expand(slow.phase - transfer),
    )
    balance = sp.simplify(
        moved_fast.phase + moved_slow.phase - fast.phase - slow.phase
    )
    return moved_slow, moved_fast, interaction, transfer, balance


def normalize_soliton_history(
    history: ProcessWord[SolitonStep],
    *,
    preference: RewritePreference,
    defect: sp.Expr = sp.S.Zero,
) -> ParametricNormalization:
    """Sort by speed rank while retaining the complete parametric rewrite trace."""

    current = list(history.steps)
    trace: list[ParametricRewriteStep] = []

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
        moved_slow, moved_fast, interaction, transfer, balance = rewrite_kdv_inversion(
            fast,
            slow,
            defect=defect,
        )
        before = (fast, slow)
        after = (moved_slow, moved_fast)
        current[position : position + 2] = list(after)
        trace.append(
            ParametricRewriteStep(
                position=position,
                before=before,
                after=after,
                interaction_factor=interaction,
                phase_transfer=transfer,
                phase_balance_residual=balance,
            )
        )

    return ParametricNormalization(
        original=history,
        normal_form=ProcessWord(tuple(current)),
        trace=tuple(trace),
    )


def phase_table(history: ProcessWord[SolitonStep]) -> dict[str, sp.Expr]:
    return {step.name: step.phase for step in history}


def phase_join_residuals(
    left: ProcessWord[SolitonStep],
    right: ProcessWord[SolitonStep],
) -> dict[str, sp.Expr]:
    left_phases = phase_table(left)
    right_phases = phase_table(right)
    if set(left_phases) != set(right_phases):
        raise ValueError("histories do not contain the same named solitons")
    return {
        name: sp.simplify(left_phases[name] - right_phases[name])
        for name in sorted(left_phases)
    }


def test_two_soliton_scattering_is_a_parametric_history_rewrite():
    k_fast, k_slow = sp.symbols("k_fast k_slow", positive=True)
    q_fast, q_slow = sp.symbols("q_fast q_slow")
    fast = SolitonStep("fast", 2, k_fast, q_fast)
    slow = SolitonStep("slow", 1, k_slow, q_slow)

    moved_slow, moved_fast, interaction, transfer, balance = rewrite_kdv_inversion(
        fast,
        slow,
    )

    expected_interaction = sp.factor(
        ((k_fast - k_slow) / (k_fast + k_slow)) ** 2
    )
    assert sp.simplify(interaction - expected_interaction) == 0
    assert sp.simplify(transfer + sp.log(expected_interaction)) == 0
    assert moved_slow.name == "slow"
    assert moved_fast.name == "fast"
    assert moved_slow.k == k_slow
    assert moved_fast.k == k_fast
    assert sp.simplify(moved_fast.phase - q_fast - transfer) == 0
    assert sp.simplify(moved_slow.phase - q_slow + transfer) == 0
    assert balance == 0

    # q=k*x0, so the physical-center displacement in this convention is +/-L/k.
    assert sp.simplify((moved_fast.phase - q_fast) / k_fast - transfer / k_fast) == 0
    assert sp.simplify((moved_slow.phase - q_slow) / k_slow + transfer / k_slow) == 0


def test_three_soliton_critical_pair_is_globally_joinable():
    k1, k2, k3 = sp.symbols("k1 k2 k3", positive=True)
    q1, q2, q3 = sp.symbols("q1 q2 q3")
    history = ProcessWord(
        (
            SolitonStep("s3", 3, k3, q3),
            SolitonStep("s2", 2, k2, q2),
            SolitonStep("s1", 1, k1, q1),
        )
    )

    left = normalize_soliton_history(history, preference="leftmost")
    right = normalize_soliton_history(history, preference="rightmost")

    assert tuple(step.position for step in left.trace) == (0, 1, 0)
    assert tuple(step.position for step in right.trace) == (1, 0, 1)
    assert left.visible_order == right.visible_order == ("s1", "s2", "s3")
    assert all(step.phase_balance_residual == 0 for step in left.trace + right.trace)
    assert all(
        residual == 0
        for residual in phase_join_residuals(left.normal_form, right.normal_form).values()
    )

    L32 = -sp.log(((k3 - k2) / (k3 + k2)) ** 2)
    L31 = -sp.log(((k3 - k1) / (k3 + k1)) ** 2)
    L21 = -sp.log(((k2 - k1) / (k2 + k1)) ** 2)
    final = phase_table(left.normal_form)
    assert sp.simplify(final["s3"] - (q3 + L32 + L31)) == 0
    assert sp.simplify(final["s2"] - (q2 - L32 + L21)) == 0
    assert sp.simplify(final["s1"] - (q1 - L31 - L21)) == 0
    assert sp.simplify(sum(final.values()) - (q1 + q2 + q3)) == 0


def test_two_body_balance_does_not_imply_three_body_confluence_red_team():
    # Keep the visible pair swap and exact local phase-sum conservation, but let
    # the transferred amount depend weakly on the current pair state.  This is
    # deliberately *not* KdV; it is chosen to survive the two-body invariant and
    # fail only when competing three-body histories are compared.
    epsilon = sp.Rational(1, 10)
    history = ProcessWord(
        (
            SolitonStep("s3", 3, sp.Integer(3), sp.Integer(3)),
            SolitonStep("s2", 2, sp.Integer(2), sp.Integer(2)),
            SolitonStep("s1", 1, sp.Integer(1), sp.Integer(1)),
        )
    )

    left = normalize_soliton_history(
        history,
        preference="leftmost",
        defect=epsilon,
    )
    right = normalize_soliton_history(
        history,
        preference="rightmost",
        defect=epsilon,
    )

    assert left.visible_order == right.visible_order == ("s1", "s2", "s3")
    assert all(step.phase_balance_residual == 0 for step in left.trace + right.trace)

    residuals = phase_join_residuals(left.normal_form, right.normal_form)
    numerical = tuple(abs(float(sp.N(value, 30))) for value in residuals.values())
    assert max(numerical) > 1e-6
    assert abs(sum(numerical)) > 1e-6

    # Global phase sum is still conserved along each path: the obstruction is
    # genuinely in how the residual is distributed among the three histories.
    initial_sum = sum(step.phase for step in history)
    assert sp.simplify(sum(phase_table(left.normal_form).values()) - initial_sum) == 0
    assert sp.simplify(sum(phase_table(right.normal_form).values()) - initial_sum) == 0
