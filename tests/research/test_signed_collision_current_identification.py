"""Phase 1J-B4: exact shadows for signed-current identification.

Deng--Hani--Ma provide two distinct ingredients: an exact signed Penrose
expansion for endpoint transport and a collision-atom integral identity.  A
physical collision-current theorem still needs a path-resolved, marked
Penrose identity joining those ingredients.  Endpoint equality and positive
majorants are insufficient.

This executable essay records the smallest sufficient schema.  A signed
identity of path measures pushes linearly to an oriented gain/loss current;
separately typed path residuals push to separately typed current residuals.
The red teams show why endpoint marginals, absolute values, total masses and
event-forgetting cuts cannot replace that schema.

The fixture is finite exact logic, not a discretization of hard spheres.  It
does not prove the missing marked Penrose identity, a continuum trace bound,
an unbounded logarithmic pairing, an entropy chain rule or an H theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Literal, Mapping


Q = Fraction
Side = Literal["gain", "loss"]


@dataclass(frozen=True, order=True)
class Collision:
    """One root-visible collision in a path-resolved history."""

    time_cell: int
    channel: str
    incoming_cell: str
    outgoing_cell: str


@dataclass(frozen=True, order=True)
class Path:
    """A terminal state together with the collisions that produced it."""

    terminal_cell: str
    collisions: tuple[Collision, ...]


@dataclass(frozen=True, order=True)
class Event:
    """One atom in the common oriented collision-event space."""

    time_cell: int
    channel: str
    state_cell: str
    side: Side


@dataclass(frozen=True)
class SignedEventMeasure:
    """A canonical finite signed measure on the declared event space."""

    weights: tuple[tuple[Event, Q], ...]

    @classmethod
    def from_pairs(
        cls, pairs: tuple[tuple[Event, Q], ...]
    ) -> "SignedEventMeasure":
        combined: dict[Event, Q] = {}
        for event, weight in pairs:
            combined[event] = combined.get(event, Q(0)) + Q(weight)
        return cls(
            tuple(sorted((event, weight) for event, weight in combined.items() if weight))
        )

    @classmethod
    def zero(cls) -> "SignedEventMeasure":
        return cls(())

    def add(self, other: "SignedEventMeasure") -> "SignedEventMeasure":
        return SignedEventMeasure.from_pairs(self.weights + other.weights)

    def scale(self, scalar: Q) -> "SignedEventMeasure":
        return SignedEventMeasure.from_pairs(
            tuple((event, Q(scalar) * weight) for event, weight in self.weights)
        )

    def subtract(self, other: "SignedEventMeasure") -> "SignedEventMeasure":
        return self.add(other.scale(Q(-1)))

    def pair(self, test: Callable[[Event], Q]) -> Q:
        return sum((weight * Q(test(event)) for event, weight in self.weights), Q(0))

    @property
    def total_mass(self) -> Q:
        return sum((weight for _, weight in self.weights), Q(0))

    @property
    def total_variation(self) -> Q:
        return sum((abs(weight) for _, weight in self.weights), Q(0))

    def forget_orientation(self) -> Mapping[tuple[int, str], Q]:
        coarse: dict[tuple[int, str], Q] = {}
        for event, weight in self.weights:
            key = (event.time_cell, event.channel)
            coarse[key] = coarse.get(key, Q(0)) + weight
        return {key: weight for key, weight in coarse.items() if weight}


@dataclass(frozen=True)
class SignedPathMeasure:
    """A canonical finite signed measure retaining complete collision paths."""

    weights: tuple[tuple[Path, Q], ...]

    @classmethod
    def from_pairs(
        cls, pairs: tuple[tuple[Path, Q], ...]
    ) -> "SignedPathMeasure":
        combined: dict[Path, Q] = {}
        for path, weight in pairs:
            combined[path] = combined.get(path, Q(0)) + Q(weight)
        return cls(
            tuple(sorted((path, weight) for path, weight in combined.items() if weight))
        )

    @classmethod
    def zero(cls) -> "SignedPathMeasure":
        return cls(())

    def add(self, other: "SignedPathMeasure") -> "SignedPathMeasure":
        return SignedPathMeasure.from_pairs(self.weights + other.weights)

    def scale(self, scalar: Q) -> "SignedPathMeasure":
        return SignedPathMeasure.from_pairs(
            tuple((path, Q(scalar) * weight) for path, weight in self.weights)
        )

    def subtract(self, other: "SignedPathMeasure") -> "SignedPathMeasure":
        return self.add(other.scale(Q(-1)))

    @property
    def total_variation(self) -> Q:
        return sum((abs(weight) for _, weight in self.weights), Q(0))

    def endpoint_marginal(self) -> Mapping[str, Q]:
        marginal: dict[str, Q] = {}
        for path, weight in self.weights:
            marginal[path.terminal_cell] = marginal.get(path.terminal_cell, Q(0)) + weight
        return {cell: weight for cell, weight in marginal.items() if weight}

    def absolute_majorant(self) -> "SignedPathMeasure":
        return SignedPathMeasure.from_pairs(
            tuple((path, abs(weight)) for path, weight in self.weights)
        )

    def collision_current(self) -> SignedEventMeasure:
        """Push each collision to gain minus loss on one event space."""

        pairs: list[tuple[Event, Q]] = []
        for path, path_weight in self.weights:
            for collision in path.collisions:
                pairs.extend(
                    (
                        (
                            Event(
                                collision.time_cell,
                                collision.channel,
                                collision.outgoing_cell,
                                "gain",
                            ),
                            path_weight,
                        ),
                        (
                            Event(
                                collision.time_cell,
                                collision.channel,
                                collision.incoming_cell,
                                "loss",
                            ),
                            -path_weight,
                        ),
                    )
                )
        return SignedEventMeasure.from_pairs(tuple(pairs))


@dataclass(frozen=True)
class TypedPathResiduals:
    """Residual axes that must not be collapsed before current identification."""

    penrose_remainder: SignedPathMeasure
    truncation: SignedPathMeasure
    geometry: SignedPathMeasure
    err2: SignedPathMeasure
    terminal: SignedPathMeasure

    def total_path_residual(self) -> SignedPathMeasure:
        total = SignedPathMeasure.zero()
        for residual in (
            self.penrose_remainder,
            self.truncation,
            self.geometry,
            self.err2,
            self.terminal,
        ):
            total = total.add(residual)
        return total

    def current_ledger(self) -> Mapping[str, SignedEventMeasure]:
        return {
            "penrose_remainder": self.penrose_remainder.collision_current(),
            "truncation": self.truncation.collision_current(),
            "geometry": self.geometry.collision_current(),
            "err2": self.err2.collision_current(),
            "terminal": self.terminal.collision_current(),
        }


@dataclass(frozen=True)
class SourceGate:
    """Claim grades for the source-to-current identification chain."""

    signed_endpoint_penrose_expansion: bool
    collision_atom_integral_identity: bool
    marked_path_penrose_identity: bool
    residual_current_estimates: bool

    @property
    def verdict(self) -> str:
        if all(
            (
                self.signed_endpoint_penrose_expansion,
                self.collision_atom_integral_identity,
                self.marked_path_penrose_identity,
                self.residual_current_estimates,
            )
        ):
            return "identified"
        return "missing-theorem"


def _paths() -> tuple[Path, Path, Path, Path]:
    collision_a = Collision(0, "root-p2", "a-in", "a-out")
    collision_b = Collision(1, "root-p3", "b-in", "b-out")
    collision_g = Collision(2, "root-p4", "g-in", "g-out")
    return (
        Path("terminal-a", (collision_a,)),
        Path("terminal-b", (collision_b,)),
        Path("terminal-g", (collision_g,)),
        Path("terminal-a", ()),
    )


def _exact_penrose_fixture() -> tuple[
    SignedPathMeasure, SignedPathMeasure, SignedPathMeasure
]:
    path_a, path_b, ghost, _ = _paths()
    physical = SignedPathMeasure.from_pairs(((path_a, Q(1)), (path_b, Q(1, 4))))
    even_overlap_term = SignedPathMeasure.from_pairs(
        ((path_a, Q(3, 4)), (path_b, Q(1, 2)), (ghost, Q(1, 4)))
    )
    odd_overlap_term = SignedPathMeasure.from_pairs(
        ((path_a, Q(1, 4)), (path_b, Q(-1, 4)), (ghost, Q(-1, 4)))
    )
    return physical, even_overlap_term, odd_overlap_term


def test_current_pushforward_is_linear_and_retains_gain_loss_orientation():
    physical, even_term, odd_term = _exact_penrose_fixture()

    assert even_term.add(odd_term) == physical
    assert even_term.collision_current().add(odd_term.collision_current()) == (
        physical.collision_current()
    )
    assert physical.collision_current().total_mass == 0
    assert physical.collision_current().total_variation == Q(5, 2)


def test_path_level_signed_penrose_identity_implies_every_bounded_weak_pairing():
    physical, even_term, odd_term = _exact_penrose_fixture()
    penrose_current = even_term.collision_current().add(odd_term.collision_current())
    tests = (
        lambda event: Q(1),
        lambda event: Q(event.side == "gain"),
        lambda event: Q(event.channel == "root-p2"),
        lambda event: Q(2 * event.time_cell - (event.side == "loss")),
    )

    assert all(
        physical.collision_current().pair(test) == penrose_current.pair(test)
        for test in tests
    )


def test_current_residual_is_controlled_by_path_residual_variation_and_mark_count():
    path_a, path_b, _, _ = _paths()
    residual = SignedPathMeasure.from_pairs(
        ((path_a, Q(1, 5)), (path_b, Q(-1, 7)))
    )
    maximal_collision_count = max(len(path.collisions) for path, _ in residual.weights)

    assert residual.collision_current().total_variation == Q(24, 35)
    assert residual.collision_current().total_variation <= (
        2 * maximal_collision_count * residual.total_variation
    )


def test_endpoint_identity_does_not_determine_a_collision_current():
    path_a, _, _, no_collision = _paths()
    with_collision = SignedPathMeasure.from_pairs(((path_a, Q(1)),))
    without_collision = SignedPathMeasure.from_pairs(((no_collision, Q(1)),))

    assert with_collision.endpoint_marginal() == without_collision.endpoint_marginal()
    assert with_collision.collision_current() != without_collision.collision_current()
    assert without_collision.collision_current() == SignedEventMeasure.zero()


def test_equal_positive_majorants_do_not_determine_the_signed_current():
    path_a, path_b, _, _ = _paths()
    first = SignedPathMeasure.from_pairs(((path_a, Q(1)), (path_b, Q(-1))))
    second = SignedPathMeasure.from_pairs(((path_a, Q(1)), (path_b, Q(1))))

    assert first.absolute_majorant() == second.absolute_majorant()
    assert first.collision_current() != second.collision_current()


def test_equal_total_mass_and_variation_do_not_imply_weak_current_identity():
    path_a, path_b, _, _ = _paths()
    current_a = SignedPathMeasure.from_pairs(((path_a, Q(1)),)).collision_current()
    current_b = SignedPathMeasure.from_pairs(((path_b, Q(1)),)).collision_current()
    selects_a_gain = lambda event: Q(
        event.channel == "root-p2" and event.side == "gain"
    )

    assert current_a.total_mass == current_b.total_mass == 0
    assert current_a.total_variation == current_b.total_variation == 2
    assert current_a.pair(selects_a_gain) == 1
    assert current_b.pair(selects_a_gain) == 0


def test_forgetting_orientation_erases_the_gain_loss_current():
    path_a, _, _, _ = _paths()
    current = SignedPathMeasure.from_pairs(((path_a, Q(3, 5)),)).collision_current()
    gain_test = lambda event: Q(event.side == "gain")

    assert current.pair(gain_test) == Q(3, 5)
    assert current.forget_orientation() == {}


def test_event_forgetting_cut_cannot_reconstruct_the_marked_pairing():
    path_a, path_b, _, _ = _paths()
    same_endpoint_a = Path("forgotten", path_a.collisions)
    same_endpoint_b = Path("forgotten", path_b.collisions)
    first = SignedPathMeasure.from_pairs(((same_endpoint_a, Q(1)),))
    second = SignedPathMeasure.from_pairs(((same_endpoint_b, Q(1)),))
    test = lambda event: Q(event.channel == "root-p2" and event.side == "gain")

    assert first.endpoint_marginal() == second.endpoint_marginal() == {"forgotten": Q(1)}
    assert first.collision_current().pair(test) == 1
    assert second.collision_current().pair(test) == 0


def test_typed_path_residuals_push_to_separately_auditable_currents():
    path_a, path_b, ghost, _ = _paths()
    residuals = TypedPathResiduals(
        penrose_remainder=SignedPathMeasure.from_pairs(((ghost, Q(1, 11)),)),
        truncation=SignedPathMeasure.from_pairs(((path_a, Q(-1, 13)),)),
        geometry=SignedPathMeasure.from_pairs(((path_b, Q(1, 17)),)),
        err2=SignedPathMeasure.zero(),
        terminal=SignedPathMeasure.from_pairs(((ghost, Q(-1, 19)),)),
    )
    ledger = residuals.current_ledger()
    summed_current = SignedEventMeasure.zero()
    for current in ledger.values():
        summed_current = summed_current.add(current)

    assert tuple(ledger) == (
        "penrose_remainder",
        "truncation",
        "geometry",
        "err2",
        "terminal",
    )
    assert summed_current == residuals.total_path_residual().collision_current()
    assert ledger["err2"] == SignedEventMeasure.zero()


def test_actual_truncated_target_response_ledger_reconstructs_exactly():
    physical, even_term, odd_term = _exact_penrose_fixture()
    path_a, _, ghost, _ = _paths()
    truncation_residual = SignedPathMeasure.from_pairs(((ghost, Q(1, 10)),))
    actual = physical.add(truncation_residual)
    target = SignedPathMeasure.from_pairs(((path_a, Q(4, 5)),))
    formal_penrose = even_term.add(odd_term)

    direct_response = actual.collision_current().subtract(target.collision_current())
    decomposed_response = (
        formal_penrose.collision_current()
        .subtract(target.collision_current())
        .add(truncation_residual.collision_current())
    )

    assert formal_penrose == physical
    assert direct_response == decomposed_response


def test_source_audit_stops_at_the_missing_marked_penrose_theorem():
    source = SourceGate(
        signed_endpoint_penrose_expansion=True,
        collision_atom_integral_identity=True,
        marked_path_penrose_identity=False,
        residual_current_estimates=False,
    )
    sufficient_schema = SourceGate(True, True, True, True)

    assert source.verdict == "missing-theorem"
    assert sufficient_schema.verdict == "identified"


def test_claim_ledger_keeps_logarithms_entropy_h_rank_and_api_outside_b4():
    claims: Mapping[str, str] = {
        "term_level_collision_atom_identity": "external-exact",
        "signed_endpoint_penrose_expansion": "external-exact",
        "finite_path_to_current_schema": "passed",
        "marked_penrose_current_identity": "missing",
        "residual_current_estimates": "missing",
        "unbounded_logarithmic_test": "outside-gate",
        "entropy_chain_rule": "outside-gate",
        "continuum_h_theorem": "not-claimed",
        "rank_promotion": "not-claimed",
        "generic_api": "not-claimed",
    }

    assert claims["finite_path_to_current_schema"] == "passed"
    assert claims["marked_penrose_current_identity"] == "missing"
    assert claims["residual_current_estimates"] == "missing"
    assert claims["unbounded_logarithmic_test"] == "outside-gate"
    assert claims["entropy_chain_rule"] == "outside-gate"
    assert all(
        claims[name] == "not-claimed"
        for name in ("continuum_h_theorem", "rank_promotion", "generic_api")
    )
