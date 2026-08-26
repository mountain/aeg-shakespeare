"""Exact Phase 1G calibration of selective continuation and time reversal.

Phase 1F read the Deng--Hani--Ma partial expansion as an asymmetric policy:
stop a leading factorized branch and continue a connected cumulant branch.
This file asks whether that policy has a calculable finite meaning before it
is transferred back to hard spheres.

The microscopic carrier is ``Gamma = {0, 1}_x x {0, 1}_h``.  Its reversible
evolution is the XOR involution

    U(x, h) = (x xor h, h).

The target observer keeps only the ``x`` marginal.  A declared environment
law ``q_delta`` supplies a factorized section ``sigma_delta(p) = p x q``.
For every admissible microscopic law ``F`` the exact split is

    pi U F = B_delta(pi F) + pi U E_delta(F),

where ``B_delta = pi U sigma_delta`` is the stopped target branch and
``E_delta(F) = F - sigma_delta(pi F)`` is a signed connected residual that is
continued through ``U``.  Exact ``Fraction`` arithmetic verifies that:

* the microscopic evolution is reversible;
* the stopped and continued branches reconstruct the next observation;
* omitting the connected branch destroys exact reversal;
* the closure section and microscopic evolution do not commute;
* repeated re-sectioning produces a contractive target semigroup even though
  the closed microscopic system returns after two steps.

This is a finite semantic calibration, not a hard-sphere model, a proof of a
Boltzmann--Grad limit, or an H theorem.
"""

from fractions import Fraction


Q = Fraction
MacroLaw = tuple[Q, Q]
MicroLaw = tuple[tuple[Q, Q], tuple[Q, Q]]


def _macro_add(left: MacroLaw, right: MacroLaw) -> MacroLaw:
    return (left[0] + right[0], left[1] + right[1])


def _macro_subtract(left: MacroLaw, right: MacroLaw) -> MacroLaw:
    return (left[0] - right[0], left[1] - right[1])


def _micro_subtract(left: MicroLaw, right: MicroLaw) -> MicroLaw:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def _macro_l1(law: MacroLaw) -> Q:
    return abs(law[0]) + abs(law[1])


def _micro_l1(law: MicroLaw) -> Q:
    return sum((abs(entry) for row in law for entry in row), Q(0))


def _total(law: MicroLaw) -> Q:
    return sum((entry for row in law for entry in row), Q(0))


def _lower(law: MicroLaw) -> MacroLaw:
    """Observe only x and forget the hidden/environment bit h."""

    return (law[0][0] + law[0][1], law[1][0] + law[1][1])


def _environment_marginal(law: MicroLaw) -> MacroLaw:
    return (law[0][0] + law[1][0], law[0][1] + law[1][1])


def _section(law: MacroLaw, delta: Q) -> MicroLaw:
    """Attach a fresh factorized environment q=(1-delta, delta)."""

    return (
        (law[0] * (1 - delta), law[0] * delta),
        (law[1] * (1 - delta), law[1] * delta),
    )


def _xor_pushforward(law: MicroLaw) -> MicroLaw:
    """Push a law through U(x,h)=(x xor h,h), an exact involution."""

    return (
        (law[0][0], law[1][1]),
        (law[1][0], law[0][1]),
    )


def _target_step(law: MacroLaw, delta: Q) -> MacroLaw:
    """Stopped branch B_delta = pi o U o sigma_delta."""

    return _lower(_xor_pushforward(_section(law, delta)))


def _target_am_jet(law: MacroLaw, delta: Q) -> tuple[MacroLaw, MacroLaw]:
    """One-step A/M chart of the stopped binary target channel."""

    additive = (delta * law[1], delta * law[0])
    multiplicative = (-delta, -delta)
    return additive, multiplicative


def _target_iterate(law: MacroLaw, delta: Q, steps: int) -> MacroLaw:
    for _ in range(steps):
        law = _target_step(law, delta)
    return law


def _target_linear_inverse(law: MacroLaw, delta: Q) -> MacroLaw:
    """Algebraic inverse; it is not a Markov map on the whole simplex."""

    determinant = 1 - 2 * delta
    return (
        ((1 - delta) * law[0] - delta * law[1]) / determinant,
        (-delta * law[0] + (1 - delta) * law[1]) / determinant,
    )


def _micro_iterate(law: MicroLaw, steps: int) -> MicroLaw:
    for _ in range(steps):
        law = _xor_pushforward(law)
    return law


def _connected_residual(law: MicroLaw, delta: Q) -> MicroLaw:
    """Signed correlation relative to the declared factorized section."""

    return _micro_subtract(law, _section(_lower(law), delta))


def _fixture() -> tuple[MacroLaw, Q, MicroLaw, MicroLaw]:
    macro_initial = (Q(3, 4), Q(1, 4))
    delta = Q(1, 16)
    micro_initial = _section(macro_initial, delta)
    micro_middle = _xor_pushforward(micro_initial)
    return macro_initial, delta, micro_initial, micro_middle


def test_xor_microdynamics_is_an_exact_probability_preserving_involution():
    macro_initial, delta, micro_initial, micro_middle = _fixture()

    assert _total(micro_initial) == _total(micro_middle) == 1
    assert _environment_marginal(micro_initial) == (1 - delta, delta)
    assert _environment_marginal(micro_middle) == (1 - delta, delta)
    assert _xor_pushforward(micro_middle) == micro_initial
    assert _lower(micro_initial) == macro_initial
    assert _lower(micro_middle) == (Q(23, 32), Q(9, 32))


def test_cut_splits_middle_law_into_stopped_section_and_connected_residual():
    _, delta, _, micro_middle = _fixture()
    macro_middle = _lower(micro_middle)
    residual = _connected_residual(micro_middle, delta)
    factorized_middle = _section(macro_middle, delta)

    assert micro_middle == (
        (Q(45, 64), Q(1, 64)),
        (Q(15, 64), Q(3, 64)),
    )
    assert factorized_middle == (
        (Q(345, 512), Q(23, 512)),
        (Q(135, 512), Q(9, 512)),
    )
    assert residual == (
        (Q(15, 512), Q(-15, 512)),
        (Q(-15, 512), Q(15, 512)),
    )
    assert _micro_l1(residual) == Q(15, 128)
    assert _lower(residual) == (0, 0)
    assert _environment_marginal(residual) == (0, 0)
    assert factorized_middle[0][0] + residual[0][0] == micro_middle[0][0]
    assert factorized_middle[0][1] + residual[0][1] == micro_middle[0][1]
    assert factorized_middle[1][0] + residual[1][0] == micro_middle[1][0]
    assert factorized_middle[1][1] + residual[1][1] == micro_middle[1][1]


def test_stopped_leading_branch_plus_continued_residual_is_exact_next_state():
    macro_initial, delta, _, micro_middle = _fixture()
    macro_middle = _lower(micro_middle)
    residual = _connected_residual(micro_middle, delta)

    stopped_leading = _target_step(macro_middle, delta)
    additive, multiplicative = _target_am_jet(macro_middle, delta)
    continued_connected = _lower(_xor_pushforward(residual))
    exact_next = _lower(_xor_pushforward(micro_middle))

    assert stopped_leading == (Q(177, 256), Q(79, 256))
    assert stopped_leading == (
        macro_middle[0] + additive[0] + macro_middle[0] * multiplicative[0],
        macro_middle[1] + additive[1] + macro_middle[1] * multiplicative[1],
    )
    assert continued_connected == (Q(15, 256), Q(-15, 256))
    assert _macro_add(stopped_leading, continued_connected) == exact_next
    assert exact_next == macro_initial
    assert stopped_leading != exact_next


def test_factorizing_at_the_cut_erases_the_exact_return_path():
    macro_initial, delta, _, micro_middle = _fixture()
    macro_middle = _lower(micro_middle)
    factorized_middle = _section(macro_middle, delta)
    residual = _connected_residual(micro_middle, delta)

    exact_reverse_observation = _lower(_xor_pushforward(micro_middle))
    closed_reverse_observation = _lower(_xor_pushforward(factorized_middle))
    obstruction = _macro_subtract(
        exact_reverse_observation,
        closed_reverse_observation,
    )

    assert exact_reverse_observation == macro_initial
    assert closed_reverse_observation == _target_step(macro_middle, delta)
    assert obstruction == _lower(_xor_pushforward(residual))
    assert obstruction == (Q(15, 256), Q(-15, 256))


def test_repeated_resectioning_contracts_while_closed_microdynamics_returns():
    macro_initial, delta, micro_initial, micro_middle = _fixture()
    steps = 16
    contraction = 1 - 2 * delta

    exact_micro_macro = _lower(_micro_iterate(micro_initial, steps))
    renewed_target_macro = _target_iterate(macro_initial, delta, steps)
    long_horizon_gap = _macro_l1(
        _macro_subtract(exact_micro_macro, renewed_target_macro)
    )
    first_cut_residual = _micro_l1(
        _connected_residual(micro_middle, delta)
    )

    assert exact_micro_macro == macro_initial
    assert renewed_target_macro == (
        Q(1, 2) + Q(1, 4) * contraction**steps,
        Q(1, 2) - Q(1, 4) * contraction**steps,
    )
    assert long_horizon_gap == Q(1, 2) * (1 - contraction**steps)
    assert long_horizon_gap > 3 * first_cut_residual

    # B_delta is algebraically invertible for delta != 1/2, so contraction is
    # not by itself literal information destruction.  The arrow is Markov:
    # the inverse fails positivity on the full target simplex.
    inverse_pure_zero = _target_linear_inverse((Q(1), Q(0)), delta)
    assert _target_step(inverse_pure_zero, delta) == (1, 0)
    assert inverse_pure_zero[1] < 0


def test_selective_continuation_claims_remain_separately_typed():
    grades = {
        "micro_evolution": "exact_reversible_involution",
        "leading_branch": "stopped_target_channel",
        "connected_branch": "continued_signed_residual",
        "two_branch_observation": "exact_one_cut_identity",
        "stopped_branch_to_closed_micro_future": "rejected",
        "resectioned_target_to_micro_quotient": "rejected",
        "resectioned_target_to_autonomous_semigroup": "exact_finite_model",
        "finite_model_to_hard_sphere_limit": "external_theorem_required",
        "contractive_target_to_H_theorem": "not_yet_tested",
    }

    assert grades["two_branch_observation"] == "exact_one_cut_identity"
    assert grades["stopped_branch_to_closed_micro_future"] == "rejected"
    assert grades["resectioned_target_to_micro_quotient"] == "rejected"
    assert grades["contractive_target_to_H_theorem"] == "not_yet_tested"
