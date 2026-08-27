"""Phase 1J-B2: exact shadows for a marked-molecule flux lift.

Deng--Hani--Ma molecule integrals retain pre-cut collision atoms.  At that
level, a root-visible C-atom determines a measurable collision-event map.
Pushing the signed molecule measure through that map cannot increase total
variation, and inserting a bounded test function commutes with an exact
Fubini cut.  This executable essay records finite rational shadows of those
two elementary measure-theoretic facts.

The fixture is not a discretization or proof of the Deng--Hani--Ma estimates.
In particular, it does not sum over molecules, identify the resulting current
with a hard-sphere boundary trace, control the logarithmic Boltzmann affinity,
or prove an H theorem.  The full bounded L-infinity test ball below is the
dual of total variation; it is strictly stronger than a generic weak-flux
test class.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Literal, Mapping


Q = Fraction
AtomKind = Literal["C", "O"]
CutComponent = Literal["outer", "inner"]


@dataclass(frozen=True, order=True)
class IntegrationState:
    """One finite shadow of the variables in a prescribed molecule integral."""

    outer: int
    inner: int


@dataclass(frozen=True, order=True)
class MoleculeAtom:
    """A typed pre-cut molecule atom and its declared cut component."""

    name: str
    kind: AtomKind
    layer: int
    particle_lines: tuple[str, str]
    component: CutComponent
    channel: str


@dataclass(frozen=True, order=True)
class CollisionEvent:
    """One atom of a finite collision-event test partition."""

    layer: int
    root_line: str
    channel: str
    cell: int
    orientation: int


@dataclass(frozen=True)
class SignedEventMeasure:
    """A finite signed event measure, stored in canonical form."""

    weights: tuple[tuple[CollisionEvent, Q], ...]

    def __post_init__(self) -> None:
        events = tuple(event for event, _ in self.weights)
        assert events == tuple(sorted(events))
        assert len(events) == len(set(events))
        assert all(weight != 0 for _, weight in self.weights)

    @classmethod
    def from_mapping(
        cls, weights: Mapping[CollisionEvent, Q]
    ) -> "SignedEventMeasure":
        return cls(
            tuple(
                sorted(
                    (event, Q(weight))
                    for event, weight in weights.items()
                    if weight != 0
                )
            )
        )

    @classmethod
    def from_pairs(
        cls, pairs: tuple[tuple[CollisionEvent, Q], ...]
    ) -> "SignedEventMeasure":
        combined: dict[CollisionEvent, Q] = {}
        for event, weight in pairs:
            combined[event] = combined.get(event, Q(0)) + weight
        return cls.from_mapping(combined)

    def add(self, other: "SignedEventMeasure") -> "SignedEventMeasure":
        return SignedEventMeasure.from_pairs(self.weights + other.weights)

    def pair(self, test: Callable[[CollisionEvent], Q]) -> Q:
        return sum((weight * Q(test(event)) for event, weight in self.weights), Q(0))

    @property
    def total_variation(self) -> Q:
        return sum((abs(weight) for _, weight in self.weights), Q(0))

    def coarsen_without_cell(self) -> dict[tuple[int, str, str, int], Q]:
        """Push forward to a deliberately smaller cylinder test algebra."""

        coarse: dict[tuple[int, str, str, int], Q] = {}
        for event, weight in self.weights:
            key = (event.layer, event.root_line, event.channel, event.orientation)
            coarse[key] = coarse.get(key, Q(0)) + weight
        return {key: weight for key, weight in coarse.items() if weight != 0}


EventMap = Callable[[MoleculeAtom, IntegrationState], CollisionEvent]


@dataclass(frozen=True)
class PrescribedMoleculeIntegral:
    """A factored finite signed integral with positive kernel weights."""

    atoms: tuple[MoleculeAtom, ...]
    root_lines: frozenset[str]
    outer_weights: Mapping[int, Q]
    inner_weights: Mapping[IntegrationState, Q]
    amplitudes: Mapping[IntegrationState, Q]

    def __post_init__(self) -> None:
        states = set(self.inner_weights)
        assert states == set(self.amplitudes)
        assert all(state.outer in self.outer_weights for state in states)
        assert all(weight >= 0 for weight in self.outer_weights.values())
        assert all(weight >= 0 for weight in self.inner_weights.values())

    @property
    def states(self) -> tuple[IntegrationState, ...]:
        return tuple(sorted(self.inner_weights))

    def signed_weight(self, state: IntegrationState) -> Q:
        return (
            Q(self.outer_weights[state.outer])
            * Q(self.inner_weights[state])
            * Q(self.amplitudes[state])
        )

    @property
    def unmarked_integral(self) -> Q:
        return sum((self.signed_weight(state) for state in self.states), Q(0))

    @property
    def absolute_integral(self) -> Q:
        return sum((abs(self.signed_weight(state)) for state in self.states), Q(0))

    @property
    def eligible_atoms(self) -> tuple[MoleculeAtom, ...]:
        return tuple(
            atom
            for atom in self.atoms
            if atom.kind == "C"
            and any(line in self.root_lines for line in atom.particle_lines)
        )

    def marked_measure(
        self, atom: MoleculeAtom, event_map: EventMap
    ) -> SignedEventMeasure:
        assert atom in self.eligible_atoms
        return SignedEventMeasure.from_pairs(
            tuple(
                (event_map(atom, state), self.signed_weight(state))
                for state in self.states
            )
        )

    def direct_marked_pair(
        self,
        atom: MoleculeAtom,
        event_map: EventMap,
        test: Callable[[CollisionEvent], Q],
    ) -> Q:
        return sum(
            (
                self.signed_weight(state) * Q(test(event_map(atom, state)))
                for state in self.states
            ),
            Q(0),
        )

    def iterated_marked_pair(
        self,
        atom: MoleculeAtom,
        event_map: EventMap,
        test: Callable[[CollisionEvent], Q],
    ) -> Q:
        """Fubini cut with the mark retained in the component containing it."""

        total = Q(0)
        for outer in sorted(self.outer_weights):
            states = tuple(state for state in self.states if state.outer == outer)
            if atom.component == "outer":
                events = {event_map(atom, state) for state in states}
                assert len(events) == 1
                event = next(iter(events))
                inner_sum = sum(
                    (
                        Q(self.inner_weights[state]) * Q(self.amplitudes[state])
                        for state in states
                    ),
                    Q(0),
                )
                total += Q(self.outer_weights[outer]) * inner_sum * Q(test(event))
            else:
                inner_sum = sum(
                    (
                        Q(self.inner_weights[state])
                        * Q(self.amplitudes[state])
                        * Q(test(event_map(atom, state)))
                        for state in states
                    ),
                    Q(0),
                )
                total += Q(self.outer_weights[outer]) * inner_sum
        return total


def _event_map(atom: MoleculeAtom, state: IntegrationState) -> CollisionEvent:
    if atom.component == "outer":
        cell = state.outer
    else:
        cell = 2 * state.outer + state.inner
    return CollisionEvent(
        layer=atom.layer,
        root_line="root",
        channel=atom.channel,
        cell=cell,
        orientation=1,
    )


def _swapped_inner_event_map(
    atom: MoleculeAtom, state: IntegrationState
) -> CollisionEvent:
    assert atom.component == "inner"
    return CollisionEvent(
        layer=atom.layer,
        root_line="root",
        channel=atom.channel,
        cell=2 * state.outer + (1 - state.inner),
        orientation=1,
    )


def _fixture() -> PrescribedMoleculeIntegral:
    atoms = (
        MoleculeAtom("root-outer", "C", 0, ("root", "p2"), "outer", "C0"),
        MoleculeAtom("root-inner", "C", 1, ("root", "p3"), "inner", "C1"),
        MoleculeAtom("nonroot", "C", 1, ("p2", "p3"), "inner", "C2"),
        MoleculeAtom("overlap", "O", 2, ("root", "p4"), "inner", "O"),
    )
    states = tuple(IntegrationState(outer, inner) for outer in (0, 1) for inner in (0, 1))
    return PrescribedMoleculeIntegral(
        atoms=atoms,
        root_lines=frozenset({"root"}),
        outer_weights={0: Q(1, 2), 1: Q(1, 3)},
        inner_weights={
            states[0]: Q(1),
            states[1]: Q(1, 2),
            states[2]: Q(2, 3),
            states[3]: Q(1, 4),
        },
        amplitudes={
            states[0]: Q(2),
            states[1]: Q(-1),
            states[2]: Q(3),
            states[3]: Q(-2),
        },
    )


def test_only_root_visible_collision_atoms_are_eligible_for_a_flux_mark():
    molecule = _fixture()

    assert tuple(atom.name for atom in molecule.eligible_atoms) == (
        "root-outer",
        "root-inner",
    )


def test_marked_pushforward_pairing_equals_direct_observable_insertion():
    molecule = _fixture()
    atom = molecule.eligible_atoms[1]
    test = lambda event: Q(event.cell - 1)

    assert molecule.marked_measure(atom, _event_map).pair(test) == (
        molecule.direct_marked_pair(atom, _event_map, test)
    )
    assert molecule.direct_marked_pair(atom, _event_map, test) == Q(-2, 3)


def test_one_mark_pushforward_cannot_increase_total_variation():
    molecule = _fixture()
    inner_atom = molecule.eligible_atoms[1]
    outer_atom = molecule.eligible_atoms[0]

    assert molecule.absolute_integral == Q(25, 12)
    assert molecule.marked_measure(inner_atom, _event_map).total_variation == Q(25, 12)
    assert molecule.marked_measure(outer_atom, _event_map).total_variation == Q(5, 4)
    assert all(
        molecule.marked_measure(atom, _event_map).total_variation
        <= molecule.absolute_integral
        for atom in molecule.eligible_atoms
    )


def test_pre_cut_mark_survives_exact_fubini_for_both_cut_components():
    molecule = _fixture()
    test = lambda event: Q(2 * event.layer - event.cell + 3)

    for atom in molecule.eligible_atoms:
        assert molecule.direct_marked_pair(atom, _event_map, test) == (
            molecule.iterated_marked_pair(atom, _event_map, test)
        )

    assert molecule.iterated_marked_pair(
        molecule.eligible_atoms[0], _event_map, test
    ) == Q(13, 4)
    assert molecule.iterated_marked_pair(
        molecule.eligible_atoms[1], _event_map, test
    ) == Q(17, 3)


def test_aggregate_mark_cost_is_at_most_linear_in_eligible_atom_count():
    molecule = _fixture()
    aggregate = SignedEventMeasure.from_mapping({})
    for atom in molecule.eligible_atoms:
        aggregate = aggregate.add(molecule.marked_measure(atom, _event_map))

    assert aggregate.total_variation == Q(10, 3)
    assert aggregate.total_variation <= (
        len(molecule.eligible_atoms) * molecule.absolute_integral
    )
    assert len(molecule.eligible_atoms) * molecule.absolute_integral == Q(25, 6)


def test_unmarked_cut_integral_cannot_reconstruct_the_collision_event_pairing():
    molecule = _fixture()
    atom = molecule.eligible_atoms[1]
    selects_cell_zero = lambda event: Q(event.cell == 0)

    assert molecule.unmarked_integral == Q(5, 4)
    assert molecule.direct_marked_pair(
        atom, _event_map, selects_cell_zero
    ) == Q(1)
    assert molecule.direct_marked_pair(
        atom, _swapped_inner_event_map, selects_cell_zero
    ) == Q(-1, 4)


def test_full_bounded_test_ball_is_total_variation_and_stronger_than_coarse_tests():
    common = dict(layer=0, root_line="root", channel="C", orientation=1)
    measure = SignedEventMeasure.from_mapping(
        {
            CollisionEvent(cell=0, **common): Q(1),
            CollisionEvent(cell=1, **common): Q(-1),
        }
    )
    sign_test = lambda event: Q(1 if event.cell == 0 else -1)

    assert measure.pair(sign_test) == measure.total_variation == Q(2)
    assert measure.coarsen_without_cell() == {}


def test_fixed_polylog_mark_cost_is_conditionally_absorbed_by_a_power_margin():
    """Exact shadow of n^2 2^-n <= 2^(-n/2), with epsilon=2^-n."""

    for n in range(16, 65):
        marked_budget = Q(n * n, 2**n)
        retained_power_margin = Q(1, 2 ** (n // 2))
        assert marked_budget <= retained_power_margin


def test_red_team_reciprocal_mass_cancels_a_linear_mark_count():
    for eligible_mark_count in range(1, 33):
        unmarked_mass = Q(1, eligible_mark_count)
        aggregate_mark_budget = eligible_mark_count * unmarked_mass
        assert aggregate_mark_budget == Q(1)


def test_claim_ledger_keeps_the_global_flux_and_h_steps_open():
    claims = {
        "fixed_molecule_one_mark_tv_contraction": "passed",
        "pre_cut_mark_fubini_covariance": "passed",
        "global_marked_molecule_sum": "missing",
        "hard_sphere_flux_identification": "missing",
        "logarithmic_tail_control": "missing",
        "entropy_chain_rule": "missing",
        "continuum_h_theorem": "not-claimed",
        "generic_api": "not-claimed",
    }

    assert claims["fixed_molecule_one_mark_tv_contraction"] == "passed"
    assert claims["pre_cut_mark_fubini_covariance"] == "passed"
    assert all(
        claims[name] == "missing"
        for name in (
            "global_marked_molecule_sum",
            "hard_sphere_flux_identification",
            "logarithmic_tail_control",
            "entropy_chain_rule",
        )
    )
    assert claims["continuum_h_theorem"] == "not-claimed"
    assert claims["generic_api"] == "not-claimed"
