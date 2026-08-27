"""Phase 1J-B: exact shadows for a continuum collision-flux response budget.

Deng--Hani--Ma control bulk correlation functions through cumulants and
molecule integrals.  Their theorem does not by itself supply the collision
boundary flux, nor the pairing of its response with the unbounded logarithmic
Boltzmann affinity.  This executable essay freezes the missing target in a
finite rational measure model.

The atoms below are cells of a collision-event test partition.  They are not
letters assigned to individual collisions and carry no proposed word
composition.  A response is one signed measure on the whole declared event
space.  Exact ``Fraction`` arithmetic checks measure reconstruction, horizon
additivity, clipping and tail budgets, and the condition under which target
dissipation survives a flux response and separately typed adapter errors.

This is not a trace theorem, a molecule estimate, a Boltzmann--Grad limit, or
a microscopic H theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping


Q = Fraction


@dataclass(frozen=True, order=True)
class EventCell:
    """One atom of a finite collision-event test partition."""

    time_layer: int
    channel: str
    cell: int


@dataclass(frozen=True)
class SignedFluxMeasure:
    """A finite signed current measure, stored canonically by event cell."""

    weights: tuple[tuple[EventCell, Q], ...]

    def __post_init__(self) -> None:
        cells = tuple(cell for cell, _ in self.weights)
        assert cells == tuple(sorted(cells))
        assert len(cells) == len(set(cells))
        assert all(weight != 0 for _, weight in self.weights)

    @classmethod
    def from_mapping(cls, weights: Mapping[EventCell, Q]) -> "SignedFluxMeasure":
        return cls(
            tuple(
                sorted(
                    (cell, Q(weight))
                    for cell, weight in weights.items()
                    if weight != 0
                )
            )
        )

    def as_dict(self) -> dict[EventCell, Q]:
        return dict(self.weights)

    def add(self, other: "SignedFluxMeasure") -> "SignedFluxMeasure":
        combined = self.as_dict()
        for cell, weight in other.weights:
            combined[cell] = combined.get(cell, Q(0)) + weight
        return SignedFluxMeasure.from_mapping(combined)

    def subtract(self, other: "SignedFluxMeasure") -> "SignedFluxMeasure":
        return self.add(
            SignedFluxMeasure.from_mapping(
                {cell: -weight for cell, weight in other.weights}
            )
        )

    def restrict_layers(self, start: int, end: int) -> "SignedFluxMeasure":
        assert start <= end
        return SignedFluxMeasure.from_mapping(
            {
                cell: weight
                for cell, weight in self.weights
                if start <= cell.time_layer < end
            }
        )

    def pair(self, covector: Mapping[EventCell, Q]) -> Q:
        return sum(
            (weight * Q(covector.get(cell, Q(0))) for cell, weight in self.weights),
            Q(0),
        )

    @property
    def total_variation(self) -> Q:
        return sum((abs(weight) for _, weight in self.weights), Q(0))


@dataclass(frozen=True)
class FluxResponseLedger:
    """The whole-event-space analogue of stopped plus vertical response."""

    stopped: SignedFluxMeasure
    actual: SignedFluxMeasure

    @property
    def response(self) -> SignedFluxMeasure:
        return self.actual.subtract(self.stopped)


@dataclass(frozen=True)
class ScalarResiduals:
    """Signed scalar effects that must not be hidden inside one norm."""

    trace_lift: Q = Q(0)
    history_marking: Q = Q(0)
    truncation: Q = Q(0)
    contact_geometry: Q = Q(0)
    kinetic_comparison: Q = Q(0)

    @property
    def signed_total(self) -> Q:
        return (
            self.trace_lift
            + self.history_marking
            + self.truncation
            + self.contact_geometry
            + self.kinetic_comparison
        )

    @property
    def absolute_budget(self) -> Q:
        return (
            abs(self.trace_lift)
            + abs(self.history_marking)
            + abs(self.truncation)
            + abs(self.contact_geometry)
            + abs(self.kinetic_comparison)
        )


def _clip(value: Q, level: Q) -> Q:
    assert level >= 0
    return max(-level, min(level, value))


def _clipped_covector(
    covector: Mapping[EventCell, Q], level: Q
) -> dict[EventCell, Q]:
    return {cell: _clip(Q(value), level) for cell, value in covector.items()}


def _tail_overshoot(
    measure: SignedFluxMeasure,
    covector: Mapping[EventCell, Q],
    level: Q,
) -> Q:
    """Integral of ``|psi - clip_K psi|`` against total variation."""

    return sum(
        (
            abs(weight)
            * abs(Q(covector.get(cell, Q(0))) - _clip(Q(covector.get(cell, 0)), level))
            for cell, weight in measure.weights
        ),
        Q(0),
    )


@dataclass(frozen=True)
class HResponseCertificate:
    """A conditional Lyapunov-transfer ledger for one declared horizon."""

    target_dissipation: Q
    response: SignedFluxMeasure
    h_covector: Mapping[EventCell, Q]
    clip_level: Q
    residuals: ScalarResiduals = ScalarResiduals()

    @property
    def response_pairing(self) -> Q:
        return self.response.pair(self.h_covector)

    @property
    def adapted_increment(self) -> Q:
        return (
            -self.target_dissipation
            + self.response_pairing
            + self.residuals.signed_total
        )

    @property
    def response_budget(self) -> Q:
        return (
            self.clip_level * self.response.total_variation
            + _tail_overshoot(self.response, self.h_covector, self.clip_level)
        )

    @property
    def total_error_budget(self) -> Q:
        return self.response_budget + self.residuals.absolute_budget

    @property
    def certifies_nonincrease(self) -> bool:
        return self.target_dissipation >= self.total_error_budget


def _fixture() -> tuple[
    tuple[EventCell, EventCell, EventCell],
    FluxResponseLedger,
    dict[EventCell, Q],
]:
    cells = (
        EventCell(0, "root-current", 0),
        EventCell(1, "root-current", 1),
        EventCell(2, "root-current", 2),
    )
    stopped = SignedFluxMeasure.from_mapping(
        {cells[0]: Q(1, 2), cells[1]: Q(-1, 4), cells[2]: Q(3, 4)}
    )
    response = SignedFluxMeasure.from_mapping(
        {cells[0]: Q(1, 8), cells[1]: Q(-1, 16), cells[2]: Q(1, 4)}
    )
    ledger = FluxResponseLedger(stopped=stopped, actual=stopped.add(response))
    h_covector = {cells[0]: Q(2), cells[1]: Q(-3), cells[2]: Q(4)}
    return cells, ledger, h_covector


def test_whole_flux_response_reconstructs_every_declared_weak_pairing():
    _, ledger, h_covector = _fixture()

    assert ledger.stopped.add(ledger.response) == ledger.actual
    assert ledger.actual.pair(h_covector) == (
        ledger.stopped.pair(h_covector) + ledger.response.pair(h_covector)
    )
    assert ledger.response.pair(h_covector) == Q(23, 16)


def test_response_measure_is_additive_under_a_horizon_cut():
    _, ledger, h_covector = _fixture()
    before = ledger.response.restrict_layers(0, 2)
    after = ledger.response.restrict_layers(2, 3)

    assert before.add(after) == ledger.response
    assert before.pair(h_covector) + after.pair(h_covector) == Q(23, 16)


def test_bounded_covector_pairing_is_controlled_by_total_variation():
    _, ledger, h_covector = _fixture()
    level = Q(2)
    clipped = _clipped_covector(h_covector, level)

    assert abs(ledger.response.pair(clipped)) <= (
        level * ledger.response.total_variation
    )
    assert ledger.response.total_variation == Q(7, 16)


def test_full_pairing_splits_into_clipped_part_and_tail_overshoot():
    _, ledger, h_covector = _fixture()
    level = Q(2)
    clipped = _clipped_covector(h_covector, level)
    remainder = {
        cell: h_covector[cell] - clipped[cell] for cell in h_covector
    }

    assert ledger.response.pair(h_covector) == (
        ledger.response.pair(clipped) + ledger.response.pair(remainder)
    )
    assert abs(ledger.response.pair(h_covector)) <= (
        level * ledger.response.total_variation
        + _tail_overshoot(ledger.response, h_covector, level)
    )
    assert _tail_overshoot(ledger.response, h_covector, level) == Q(9, 16)


def test_small_total_variation_does_not_uniformly_control_unbounded_covectors():
    pairings = []
    variations = []
    for scale in (2, 4, 8, 16):
        cell = EventCell(0, "moving-tail", scale)
        response = SignedFluxMeasure.from_mapping({cell: Q(1, scale)})
        covector = {cell: Q(scale)}
        pairings.append(response.pair(covector))
        variations.append(response.total_variation)

    assert pairings == [Q(1), Q(1), Q(1), Q(1)]
    assert variations == [Q(1, 2), Q(1, 4), Q(1, 8), Q(1, 16)]


def test_response_budget_is_sufficient_but_not_automatic_for_h_monotonicity():
    _, ledger, h_covector = _fixture()
    residuals = ScalarResiduals(
        trace_lift=Q(1, 20),
        history_marking=Q(-1, 30),
        truncation=Q(1, 40),
        contact_geometry=Q(0),
        kinetic_comparison=Q(-1, 60),
    )
    passing = HResponseCertificate(
        target_dissipation=Q(2),
        response=ledger.response,
        h_covector=h_covector,
        clip_level=Q(2),
        residuals=residuals,
    )
    failing = HResponseCertificate(
        target_dissipation=Q(1),
        response=ledger.response,
        h_covector=h_covector,
        clip_level=Q(2),
        residuals=residuals,
    )

    assert passing.response_budget == Q(23, 16)
    assert passing.residuals.absolute_budget == Q(1, 8)
    assert passing.total_error_budget == Q(25, 16)
    assert passing.certifies_nonincrease
    assert passing.adapted_increment == Q(-43, 80)
    assert not failing.certifies_nonincrease
    assert failing.adapted_increment == Q(37, 80) > 0


def test_bulk_l1_record_does_not_determine_collision_flux_response():
    cells, ledger, h_covector = _fixture()
    same_bulk_error = Q(1, 1000)
    zero_response = SignedFluxMeasure.from_mapping({})
    alternate_response = SignedFluxMeasure.from_mapping({cells[0]: Q(1)})

    records = (
        (same_bulk_error, zero_response),
        (same_bulk_error, alternate_response),
    )
    assert records[0][0] == records[1][0]
    assert records[0][1].pair(h_covector) == 0
    assert records[1][1].pair(h_covector) == 2
    assert records[0][1] != records[1][1]
    assert ledger.response != zero_response


def test_adapter_residual_axes_remain_separately_auditable():
    residuals = ScalarResiduals(
        trace_lift=Q(1, 2),
        history_marking=Q(-1, 3),
        truncation=Q(1, 5),
        contact_geometry=Q(-1, 7),
        kinetic_comparison=Q(1, 11),
    )

    assert residuals.signed_total == Q(727, 2310)
    assert residuals.absolute_budget == Q(2927, 2310)
    assert residuals.trace_lift != residuals.truncation
    assert residuals.history_marking != residuals.kinetic_comparison


def test_phase1j_b_claims_remain_separately_typed():
    grades = {
        "deng_bulk_correlation": "external_theorem_L1",
        "deng_cumulant_molecule_bound": "external_theorem_bulk_L1",
        "deng_cutting": "external_Fubini_operator_identity",
        "physical_history_after_cut": "explicitly_not_preserved",
        "collision_flux_lift": "missing_theorem",
        "bounded_h_response": "exact_finite_measure_shadow",
        "unbounded_h_response": "tail_or_integrability_required",
        "continuum_h_transfer": "conditional_budget_only",
        "molecule_objectification": "not_claimed",
        "arithmetic_rank_promotion": "not_claimed",
        "generic_api": "not_claimed",
    }

    assert grades["deng_cutting"] == "external_Fubini_operator_identity"
    assert grades["physical_history_after_cut"] == "explicitly_not_preserved"
    assert grades["collision_flux_lift"] == "missing_theorem"
    assert grades["continuum_h_transfer"] == "conditional_budget_only"
