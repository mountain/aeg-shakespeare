"""Phase 1J-B3: exact shadows for a bounded marked molecule sum.

The Deng--Hani--Ma proof first bounds a cumulant by positive molecule
integrals, then controls molecule choices, operation-sequence sub-cases and
the resulting elementary integrals.  A bounded pre-cut collision observable
can be removed before that machinery is entered:

    |I_M(Q psi o e_n)| <= ||psi||_infinity I_M(|Q|).

Summing root-visible C-atoms therefore inserts at most the linear factor
``|C_H(M)| <= |M|``.  Since ``m <= 2**m``, this factor changes the generic
exponential constant in the molecule-size sum but not its positive power
margin.  The rational model below records that argument, the routing facts
for deletion/cutting/splitting, and the exact geometric-series closure.

This is not a discretization or proof of the paper's analytic estimates.  It
does not identify the absolutely summable formal molecule current with the
microscopic hard-sphere collision current, control an unbounded logarithmic
test, prove an entropy chain rule, or prove an H theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Literal, Mapping


Q = Fraction
AtomKind = Literal["C", "O"]


@dataclass(frozen=True, order=True)
class Atom:
    """A pre-operation atom; only root-visible C-atoms carry current marks."""

    name: str
    kind: AtomKind
    root_visible: bool


@dataclass(frozen=True)
class PreCutMolecule:
    """The typed data needed before an estimating operation sequence."""

    atoms: tuple[Atom, ...]
    positive_mass: Q
    sign: int

    def __post_init__(self) -> None:
        assert self.positive_mass >= 0
        assert self.sign in (-1, 1)
        assert len({atom.name for atom in self.atoms}) == len(self.atoms)

    @property
    def size(self) -> int:
        return len(self.atoms)

    @property
    def eligible_marks(self) -> tuple[Atom, ...]:
        return tuple(
            atom
            for atom in self.atoms
            if atom.kind == "C" and atom.root_visible
        )

    def delete_overlap(self, name: str) -> "PreCutMolecule":
        deleted = next(atom for atom in self.atoms if atom.name == name)
        assert deleted.kind == "O"
        return PreCutMolecule(
            atoms=tuple(atom for atom in self.atoms if atom.name != name),
            positive_mass=self.positive_mass,
            sign=self.sign,
        )

    def bounded_mark_budget(self, level: Q) -> Q:
        assert level >= 0
        return level * len(self.eligible_marks) * self.positive_mass


@dataclass(frozen=True)
class SupportCase:
    """One support cell produced by splitting Q into Q times indicators."""

    name: str
    fraction: Q
    test_value: Q


def _split_marked_pair(
    molecule: PreCutMolecule, cases: tuple[SupportCase, ...]
) -> Q:
    assert sum((case.fraction for case in cases), Q(0)) == Q(1)
    assert all(case.fraction >= 0 for case in cases)
    return molecule.sign * molecule.positive_mass * sum(
        (case.fraction * case.test_value for case in cases), Q(0)
    )


@dataclass(frozen=True)
class OperationSequenceEnvelope:
    """Paper-shaped scalar ledger after choices, sub-cases and local gains."""

    base_mass: Q
    molecule_choice_base: Q
    subcase_size_base: Q
    time_gain_per_atom: Q
    molecule_rho_cost: Q
    subcase_rho_cost: Q
    epsilon_gain_per_rho: Q

    @property
    def size_ratio(self) -> Q:
        return (
            self.molecule_choice_base
            * self.subcase_size_base
            * self.time_gain_per_atom
        )

    @property
    def rho_ratio(self) -> Q:
        return (
            self.molecule_rho_cost
            * self.subcase_rho_cost
            * self.epsilon_gain_per_rho
        )

    def __post_init__(self) -> None:
        assert self.base_mass >= 0
        assert 0 <= self.size_ratio < 1
        assert 0 <= self.rho_ratio < 1

    def unmarked_term(self, molecule_size: int, rho: int) -> Q:
        assert molecule_size >= 1
        assert rho >= 1
        return (
            self.base_mass
            * self.size_ratio**molecule_size
            * self.rho_ratio**rho
        )

    def marked_term(
        self, molecule_size: int, rho: int, eligible_mark_count: int
    ) -> Q:
        assert 0 <= eligible_mark_count <= molecule_size
        return eligible_mark_count * self.unmarked_term(molecule_size, rho)

    @property
    def unmarked_total(self) -> Q:
        q = self.size_ratio
        r = self.rho_ratio
        return self.base_mass * q / (1 - q) * r / (1 - r)

    @property
    def maximal_linear_mark_total(self) -> Q:
        q = self.size_ratio
        r = self.rho_ratio
        return self.base_mass * q / (1 - q) ** 2 * r / (1 - r)

    def maximal_linear_mark_size_tail(self, cutoff: int) -> Q:
        """Sum over m > cutoff and every rho >= 1."""

        assert cutoff >= 0
        q = self.size_ratio
        r = self.rho_ratio
        size_tail = q ** (cutoff + 1) * (
            Q(cutoff + 1) - Q(cutoff) * q
        ) / (1 - q) ** 2
        return self.base_mass * size_tail * r / (1 - r)


@dataclass(frozen=True, order=True)
class EventCell:
    molecule_size: int
    rho: int


@dataclass(frozen=True)
class SignedFormalCurrent:
    """A finite partial sum of the formal pre-cut marked molecule current."""

    weights: tuple[tuple[EventCell, Q], ...]

    @property
    def total_variation(self) -> Q:
        return sum((abs(weight) for _, weight in self.weights), Q(0))

    def pair(self, test: Callable[[EventCell], Q]) -> Q:
        return sum((weight * Q(test(event)) for event, weight in self.weights), Q(0))


def _molecule_fixture() -> PreCutMolecule:
    return PreCutMolecule(
        atoms=(
            Atom("root-c0", "C", True),
            Atom("root-c1", "C", True),
            Atom("nonroot-c", "C", False),
            Atom("overlap-o", "O", True),
        ),
        positive_mass=Q(5, 6),
        sign=-1,
    )


def _envelope_fixture() -> OperationSequenceEnvelope:
    return OperationSequenceEnvelope(
        base_mass=Q(1, 32),
        molecule_choice_base=Q(2),
        subcase_size_base=Q(2),
        time_gain_per_atom=Q(1, 16),
        molecule_rho_cost=Q(2),
        subcase_rho_cost=Q(2),
        epsilon_gain_per_rho=Q(1, 64),
    )


def test_deleting_only_overlap_atoms_preserves_every_collision_mark():
    molecule = _molecule_fixture()
    after = molecule.delete_overlap("overlap-o")

    assert tuple(atom.name for atom in molecule.eligible_marks) == (
        "root-c0",
        "root-c1",
    )
    assert after.eligible_marks == molecule.eligible_marks
    assert after.size == molecule.size - 1


def test_cut_routes_each_precut_mark_to_exactly_one_component():
    molecule = _molecule_fixture()
    component_names = (
        frozenset({"root-c0", "nonroot-c"}),
        frozenset({"root-c1", "overlap-o"}),
    )
    all_names = frozenset(atom.name for atom in molecule.atoms)

    assert component_names[0].isdisjoint(component_names[1])
    assert component_names[0] | component_names[1] == all_names
    for mark in molecule.eligible_marks:
        assert sum(mark.name in component for component in component_names) == 1


def test_support_splitting_partitions_the_marked_pair_without_duplication():
    molecule = _molecule_fixture()
    cases = (
        SupportCase("far", Q(1, 2), Q(2)),
        SupportCase("near", Q(1, 3), Q(-1)),
        SupportCase("degenerate", Q(1, 6), Q(3)),
    )

    assert _split_marked_pair(molecule, cases) == Q(-35, 36)
    assert abs(_split_marked_pair(molecule, cases)) <= Q(3) * molecule.positive_mass


def test_bounded_mark_is_erased_before_the_operation_sequence():
    molecule = _molecule_fixture()
    level = Q(3)
    possible_pairings = (Q(-4), Q(1, 2), Q(5))

    for raw_pairing in possible_pairings:
        clipped_pairing = max(-level, min(level, raw_pairing))
        one_mark_pair = molecule.sign * molecule.positive_mass * clipped_pairing
        assert abs(one_mark_pair) <= level * molecule.positive_mass

    assert molecule.bounded_mark_budget(level) == Q(5)


def test_linear_mark_factor_is_absorbed_into_the_exponential_size_base():
    for molecule_size in range(1, 65):
        assert molecule_size <= 2**molecule_size
        original_count_bound = Q(3**molecule_size)
        marked_count_bound = molecule_size * original_count_bound
        enlarged_generic_bound = Q(6**molecule_size)
        assert marked_count_bound <= enlarged_generic_bound


def test_paper_shaped_unmarked_and_marked_envelopes_are_summable():
    envelope = _envelope_fixture()

    assert envelope.size_ratio == Q(1, 4)
    assert envelope.rho_ratio == Q(1, 16)
    assert envelope.unmarked_total == Q(1, 1440)
    assert envelope.maximal_linear_mark_total == Q(1, 1080)


def test_linear_marking_changes_only_a_constant_not_the_power_ratios():
    envelope = _envelope_fixture()

    assert envelope.maximal_linear_mark_total / envelope.unmarked_total == Q(4, 3)
    assert envelope.size_ratio == Q(1, 4)
    assert envelope.rho_ratio == Q(1, 16)


def test_exact_tail_certifies_absolute_convergence_of_the_formal_current():
    envelope = _envelope_fixture()
    cutoff = 8
    partial = sum(
        (
            envelope.marked_term(size, rho, size)
            for size in range(1, cutoff + 1)
            for rho in range(1, 33)
        ),
        Q(0),
    )
    tail = envelope.maximal_linear_mark_size_tail(cutoff)

    assert partial < envelope.maximal_linear_mark_total
    assert tail == Q(7, 70778880)
    assert tail < Q(1, 10**6)


def test_full_bounded_ball_is_controlled_for_the_formal_partial_current():
    envelope = _envelope_fixture()
    weights = tuple(
        (
            EventCell(size, rho),
            (-1) ** (size + rho) * envelope.marked_term(size, rho, size),
        )
        for size in range(1, 7)
        for rho in range(1, 5)
    )
    current = SignedFormalCurrent(weights)
    sign_test = lambda event: Q((-1) ** (event.molecule_size + event.rho))

    assert current.pair(sign_test) == current.total_variation
    assert current.total_variation < envelope.maximal_linear_mark_total


def test_large_error_loss_is_only_conditionally_absorbed_by_size_reserve():
    """Exact shadow of the separate large-component error absorption."""

    for root_count in range(1, 9):
        for molecule_size in range(4 * root_count, 4 * root_count + 8):
            marked_error = (
                molecule_size * Q(2**root_count) * Q(1, 4**molecule_size)
            )
            retained_reserve = Q(1, 2**molecule_size)
            assert marked_error <= retained_reserve


def test_red_team_unit_size_ratio_destroys_global_summability():
    partial_totals = tuple(
        sum((Q(size) for size in range(1, cutoff + 1)), Q(0))
        for cutoff in range(1, 9)
    )

    assert partial_totals == (Q(1), Q(3), Q(6), Q(10), Q(15), Q(21), Q(28), Q(36))


def test_red_team_exponential_mark_multiplicity_can_erase_the_size_gain():
    base_size_ratio = Q(1, 2)
    partials = tuple(
        sum(
            ((2**size) * base_size_ratio**size for size in range(1, cutoff + 1)),
            Q(0),
        )
        for cutoff in range(1, 9)
    )

    assert partials == tuple(Q(cutoff) for cutoff in range(1, 9))


def test_claim_ledger_keeps_identification_logarithms_and_h_open():
    claims: Mapping[str, str] = {
        "bounded_formal_marked_family_sum": "passed",
        "full_bounded_ball_for_formal_current": "passed",
        "large_error_family": "conditional-on-source-hierarchy",
        "canonical_cumulant_current_identity": "missing",
        "hard_sphere_flux_identification": "missing",
        "unbounded_logarithmic_test": "missing",
        "entropy_chain_rule": "missing",
        "continuum_h_theorem": "not-claimed",
        "generic_api": "not-claimed",
    }

    assert claims["bounded_formal_marked_family_sum"] == "passed"
    assert claims["full_bounded_ball_for_formal_current"] == "passed"
    assert claims["large_error_family"] == "conditional-on-source-hierarchy"
    assert all(
        claims[name] == "missing"
        for name in (
            "canonical_cumulant_current_identity",
            "hard_sphere_flux_identification",
            "unbounded_logarithmic_test",
            "entropy_chain_rule",
        )
    )
    assert claims["continuum_h_theorem"] == "not-claimed"
    assert claims["generic_api"] == "not-claimed"
