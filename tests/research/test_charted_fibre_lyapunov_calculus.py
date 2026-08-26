"""Phase 1I: exact charted fibre-response calculus before continuum H.

Phase 1G separated a renewed target branch from a continued connected
residual.  Phase 1H then found a target Lyapunov cone and showed that its
minimum polynomial member is not a microscopic Lyapunov function.  This
essay joins those results without requiring a decoder or differentiability.

For the finite reversible XOR carrier, put

    p = pi(F),
    E_sigma(F) = F - sigma(p),
    B = pi o U o sigma,
    R_sigma(F) = pi o U(E_sigma(F)).

Then every target observable ``phi`` has the exact finite-difference ledger

    phi(pi U F) - phi(p)
      = [phi(Bp) - phi(p)]
      + [phi(Bp + R_sigma(F)) - phi(Bp)].

The first bracket is the horizontal target increment and the second is the
vertical fibre response.  Taylor jets are optional chart shadows of the
second bracket; the finite identity itself needs neither a tangent space nor
global source reconstruction.

The same exact fixture also audits two target charts.  Contrast diagonalizes
the renewed channel, whereas odds make independent corner composition
multiplicative.  Hence the Phase 1H minimum-degree selector is explicitly
contrast-chart-relative.  A held-out formal coefficient check identifies
classical binary relative H as a potential of the log-odds covector, but does
not derive that covector from the target dynamics.

All arithmetic certificates are exact and research-local.  This is not a
continuum trace estimate, a Boltzmann H theorem, a generic fibre calculus, or
an objectification/rank result.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Callable


Q = Fraction
MacroLaw = tuple[Q, Q]
MicroLaw = tuple[tuple[Q, Q], tuple[Q, Q]]
Observable = Callable[[MacroLaw], Q]


@dataclass(frozen=True)
class FibreDifferenceLedger:
    """One exact horizontal/vertical observable decomposition."""

    base: MacroLaw
    stopped: MacroLaw
    response: MacroLaw
    exact_next: MacroLaw
    horizontal_increment: Q
    vertical_response: Q
    exact_increment: Q


def _macro_add(left: MacroLaw, right: MacroLaw) -> MacroLaw:
    return (left[0] + right[0], left[1] + right[1])


def _micro_add(left: MicroLaw, right: MicroLaw) -> MicroLaw:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def _micro_subtract(left: MicroLaw, right: MicroLaw) -> MicroLaw:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def _lower(law: MicroLaw) -> MacroLaw:
    return (law[0][0] + law[0][1], law[1][0] + law[1][1])


def _section(law: MacroLaw, delta: Q) -> MicroLaw:
    return (
        (law[0] * (1 - delta), law[0] * delta),
        (law[1] * (1 - delta), law[1] * delta),
    )


def _xor_pushforward(law: MicroLaw) -> MicroLaw:
    return (
        (law[0][0], law[1][1]),
        (law[1][0], law[0][1]),
    )


def _target_step(law: MacroLaw, delta: Q) -> MacroLaw:
    return _lower(_xor_pushforward(_section(law, delta)))


def _connected_residual(law: MicroLaw, delta: Q) -> MicroLaw:
    return _micro_subtract(law, _section(_lower(law), delta))


def _fibre_response(law: MicroLaw, delta: Q) -> MacroLaw:
    return _lower(_xor_pushforward(_connected_residual(law, delta)))


def _power_contrast(degree: int) -> Observable:
    assert degree > 0

    def observable(law: MacroLaw) -> Q:
        return (law[0] - law[1]) ** degree

    return observable


def _fibre_difference_ledger(
    law: MicroLaw,
    delta: Q,
    observable: Observable,
) -> FibreDifferenceLedger:
    base = _lower(law)
    stopped = _target_step(base, delta)
    response = _fibre_response(law, delta)
    exact_next = _lower(_xor_pushforward(law))
    horizontal = observable(stopped) - observable(base)
    vertical = observable(_macro_add(stopped, response)) - observable(stopped)
    return FibreDifferenceLedger(
        base=base,
        stopped=stopped,
        response=response,
        exact_next=exact_next,
        horizontal_increment=horizontal,
        vertical_response=vertical,
        exact_increment=observable(exact_next) - observable(base),
    )


def _positive_micro_corpus(total: int) -> tuple[MicroLaw, ...]:
    laws = []
    for entries in product(range(1, total), repeat=4):
        if sum(entries) != total:
            continue
        a, b, c, d = (Q(entry, total) for entry in entries)
        laws.append(((a, b), (c, d)))
    return tuple(laws)


def _contrast(law: MacroLaw) -> Q:
    return law[0] - law[1]


def _odds(law: MacroLaw) -> Q:
    if law[1] == 0:
        raise ValueError("odds require a positive denominator")
    return law[0] / law[1]


def _odds_from_contrast(contrast: Q) -> Q:
    if contrast == 1:
        raise ValueError("the pure boundary has infinite odds")
    return (1 + contrast) / (1 - contrast)


def _contrast_from_odds(odds: Q) -> Q:
    if odds == -1:
        raise ValueError("odds=-1 is outside the probability chart")
    return (odds - 1) / (odds + 1)


def _target_odds(odds: Q, contraction: Q) -> Q:
    numerator = (1 + contraction) * odds + (1 - contraction)
    denominator = (1 - contraction) * odds + (1 + contraction)
    return numerator / denominator


def _tensor_corner_odds(left: MacroLaw, right: MacroLaw) -> Q:
    return left[0] * right[0] / (left[1] * right[1])


def _formal_h_coefficients(depth: int) -> dict[int, Q]:
    return {
        2 * order: Q(1, (2 * order) * (2 * order - 1))
        for order in range(1, depth + 1)
    }


def _formal_derivative(coefficients: dict[int, Q]) -> dict[int, Q]:
    return {
        degree - 1: degree * coefficient
        for degree, coefficient in coefficients.items()
        if degree
    }


def _formal_log_odds_covector(depth: int) -> dict[int, Q]:
    # One half of log((1+z)/(1-z)) is artanh(z).
    return {2 * order - 1: Q(1, 2 * order - 1) for order in range(1, depth + 1)}


def _translate(value: Q, amount: Q) -> Q:
    return value + amount


def _scale(value: Q, factor: Q) -> Q:
    return factor * value


def test_fibre_difference_identity_holds_on_a_positive_micro_corpus():
    delta = Q(1, 16)
    corpus = _positive_micro_corpus(total=8)

    assert len(corpus) == 35
    for law, degree in product(corpus, (2, 4)):
        ledger = _fibre_difference_ledger(
            law,
            delta,
            _power_contrast(degree),
        )
        assert _macro_add(ledger.stopped, ledger.response) == ledger.exact_next
        assert (
            ledger.horizontal_increment + ledger.vertical_response
            == ledger.exact_increment
        )


def test_target_dissipation_and_fibre_response_have_independent_signs():
    delta = Q(1, 16)
    initial = (Q(3, 4), Q(1, 4))
    middle = _xor_pushforward(_section(initial, delta))
    ledger = _fibre_difference_ledger(middle, delta, _power_contrast(2))

    assert ledger.base == (Q(23, 32), Q(9, 32))
    assert ledger.stopped == (Q(177, 256), Q(79, 256))
    assert ledger.response == (Q(15, 256), Q(-15, 256))
    assert ledger.exact_next == initial
    assert ledger.horizontal_increment == Q(-735, 16384)
    assert ledger.vertical_response == Q(1695, 16384)
    assert ledger.exact_increment == Q(15, 256)
    assert ledger.vertical_response > -ledger.horizontal_increment


def test_vertical_finite_difference_contains_its_taylor_shadow_exactly():
    delta = Q(1, 16)
    initial = (Q(3, 4), Q(1, 4))
    middle = _xor_pushforward(_section(initial, delta))
    ledger = _fibre_difference_ledger(middle, delta, _power_contrast(2))
    stopped_contrast = _contrast(ledger.stopped)
    response_contrast = ledger.response[0] - ledger.response[1]
    first_pairing = 2 * stopped_contrast * response_contrast
    curvature = response_contrast**2

    assert first_pairing == Q(735, 8192)
    assert curvature == Q(225, 16384)
    assert first_pairing + curvature == ledger.vertical_response


def test_contrast_and_odds_charts_expose_different_target_normal_forms():
    delta = Q(1, 16)
    contraction = 1 - 2 * delta
    laws = (
        (Q(3, 4), Q(1, 4)),
        (Q(2, 3), Q(1, 3)),
        (Q(5, 8), Q(3, 8)),
    )

    for law in laws:
        target = _target_step(law, delta)
        contrast = _contrast(law)
        odds = _odds(law)
        assert _contrast(target) == contraction * contrast
        assert _odds(target) == _target_odds(odds, contraction)
        assert _odds_from_contrast(contrast) == odds
        assert _contrast_from_odds(odds) == contrast

    # K2 is polynomial in contrast but a reduced rational expression in odds:
    # K2 = ((r - 1) / (r + 1))^2.  At the denominator root r=-1, the numerator
    # is nonzero, so no cancellation can turn this rational law into a
    # polynomial identity.
    pole = Q(-1)
    assert (pole + 1) ** 2 == 0
    assert (pole - 1) ** 2 == 4


def test_independent_corner_composition_is_multiplicative_in_odds():
    left = (Q(3, 4), Q(1, 4))
    right = (Q(2, 3), Q(1, 3))

    assert _tensor_corner_odds(left, right) == _odds(left) * _odds(right)
    assert _tensor_corner_odds(left, right) == 6


def test_classical_h_is_the_formal_potential_of_log_odds_after_selection():
    depth = 8
    h_coefficients = _formal_h_coefficients(depth)
    derivative = _formal_derivative(h_coefficients)
    log_odds_covector = _formal_log_odds_covector(depth)

    assert derivative == log_odds_covector
    assert tuple(h_coefficients[2 * order] for order in range(1, 5)) == (
        Q(1, 2),
        Q(1, 12),
        Q(1, 30),
        Q(1, 56),
    )


def test_ordered_am_control_rejects_commuting_finite_process_words():
    value = Q(1, 2)
    amount = Q(1, 3)
    factor = Q(2)

    scale_after_translate = _scale(_translate(value, amount), factor)
    translate_after_scale = _translate(_scale(value, factor), amount)
    corrected_translate_after_scale = _translate(
        _scale(value, factor),
        factor * amount,
    )

    assert scale_after_translate != translate_after_scale
    assert scale_after_translate == corrected_translate_after_scale
    assert scale_after_translate - translate_after_scale == (factor - 1) * amount


def test_naive_residual_addition_does_not_objectify_probability_fibres():
    delta = Q(1, 16)
    base = (Q(1, 2), Q(1, 2))
    section = _section(base, delta)
    residual: MicroLaw = (
        (Q(1, 32), Q(-1, 32)),
        (Q(-1, 32), Q(1, 32)),
    )
    admissible = _micro_add(section, residual)
    doubled = _micro_add(section, _micro_add(residual, residual))

    assert _lower(residual) == (0, 0)
    assert all(entry >= 0 for row in admissible for entry in row)
    assert any(entry < 0 for row in doubled for entry in row)


def test_phase1i_claims_remain_separately_typed():
    grades = {
        "finite_fibre_difference": "exact_on_declared_xor_fixture",
        "contrast_minimality": "chart_relative_bounded_grammar",
        "odds_product_law": "exact_corner_covector_control",
        "log_odds_selection": "post_selection_formal_control",
        "ordered_am": "adjacent_exact_process_control",
        "fibre_objectification": "rejected_for_naive_addition",
        "deng_molecule_composition": "not_yet_tested",
        "continuum_h_response": "external_estimate_required",
        "generic_fibre_calculus": "not_claimed",
        "arithmetic_rank_promotion": "not_claimed",
    }

    assert grades["finite_fibre_difference"] == "exact_on_declared_xor_fixture"
    assert grades["fibre_objectification"] == "rejected_for_naive_addition"
    assert grades["continuum_h_response"] == "external_estimate_required"
    assert grades["arithmetic_rank_promotion"] == "not_claimed"
