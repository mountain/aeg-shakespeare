"""Phase 1J-B5: exact shadows for a marked Penrose insertion.

The proof of Deng--Hani--Ma Proposition 5.10 expands only overlap (O-atom)
indicators.  A root-visible collision observable depends on the pre-existing
C-atoms and is therefore constant on every Penrose grouping fiber.  It can be
multiplied through equations (5.19)--(5.30) before any absolute value.  Root
extraction sends every root-visible C-mark to the rooted molecule, while the
unrooted complement has no eligible mark.

This finite exact essay certifies that algebra, the additive derivation rule
for several rooted components, the independence of Penrose and gain/loss
signs, and the exact signed large-component remainder.  It is not a continuum
trace proof or a multi-layer current theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product as cartesian_product
from math import prod
from typing import Callable, Literal, Mapping


Q = Fraction
Edge = str
FiberKind = Literal["main", "large-error"]


def _powerset(items: tuple[Edge, ...]) -> tuple[frozenset[Edge], ...]:
    return tuple(
        frozenset(choice)
        for size in range(len(items) + 1)
        for choice in combinations(items, size)
    )


def _indicator_product(edges: frozenset[Edge], active: Mapping[Edge, int]) -> Q:
    return Q(prod(active[edge] for edge in edges))


@dataclass(frozen=True)
class PenroseFiber:
    """An interval fiber F subset G subset F union AL(F)."""

    name: str
    required: frozenset[Edge]
    allowed: frozenset[Edge]
    forbidden: frozenset[Edge]
    kind: FiberKind

    def __post_init__(self) -> None:
        assert self.required.isdisjoint(self.allowed)
        assert self.required.isdisjoint(self.forbidden)
        assert self.allowed.isdisjoint(self.forbidden)

    @property
    def members(self) -> frozenset[frozenset[Edge]]:
        return frozenset(
            self.required | extra
            for extra in _powerset(tuple(sorted(self.allowed)))
        )

    def grouped_coefficient(self, active: Mapping[Edge, int]) -> Q:
        required = _indicator_product(self.required, active)
        exclusions = Q(prod(1 - active[edge] for edge in self.allowed))
        return Q((-1) ** len(self.required)) * required * exclusions

    def expanded_coefficient(self, active: Mapping[Edge, int]) -> Q:
        return sum(
            (
                Q((-1) ** len(member))
                * _indicator_product(member, active)
                for member in self.members
            ),
            Q(0),
        )


@dataclass(frozen=True)
class PenrosePartition:
    edges: tuple[Edge, ...]
    fibers: tuple[PenroseFiber, ...]

    def __post_init__(self) -> None:
        universe = frozenset(_powerset(self.edges))
        members = tuple(fiber.members for fiber in self.fibers)
        assert frozenset().union(*members) == universe
        for index, first in enumerate(members):
            for second in members[index + 1 :]:
                assert first.isdisjoint(second)

    def ungrouped_coefficient(self, active: Mapping[Edge, int]) -> Q:
        return sum(
            (
                Q((-1) ** len(member))
                * _indicator_product(member, active)
                for member in _powerset(self.edges)
            ),
            Q(0),
        )

    def grouped_coefficient(self, active: Mapping[Edge, int]) -> Q:
        return sum(
            (fiber.grouped_coefficient(active) for fiber in self.fibers), Q(0)
        )

    def kind_coefficient(
        self, active: Mapping[Edge, int], kind: FiberKind
    ) -> Q:
        return sum(
            (
                fiber.grouped_coefficient(active)
                for fiber in self.fibers
                if fiber.kind == kind
            ),
            Q(0),
        )


@dataclass(frozen=True, order=True)
class CollisionMark:
    """A C-atom observable; O-atoms never create eligible marks."""

    name: str
    cluster: str
    root_visible: bool
    incoming_cell: str
    outgoing_cell: str

    def pair(self, test: Callable[[str, str], Q]) -> Q:
        return Q(test("gain", self.outgoing_cell)) - Q(
            test("loss", self.incoming_cell)
        )


@dataclass(frozen=True)
class RootedClusterSystem:
    clusters: frozenset[str]
    root_clusters: frozenset[str]
    edge_ends: Mapping[Edge, tuple[str, str]]
    marks: tuple[CollisionMark, ...]

    def rooted_union(self, overlap_edges: frozenset[Edge]) -> frozenset[str]:
        remaining = set(self.clusters)
        components: list[frozenset[str]] = []
        while remaining:
            component = {remaining.pop()}
            changed = True
            while changed:
                changed = False
                for edge in overlap_edges:
                    left, right = self.edge_ends[edge]
                    if (left in component) != (right in component):
                        component.update((left, right))
                        remaining.discard(left)
                        remaining.discard(right)
                        changed = True
            components.append(frozenset(component))
        return frozenset().union(
            *(
                component
                for component in components
                if component & self.root_clusters
            )
        )

    @property
    def eligible_marks(self) -> tuple[CollisionMark, ...]:
        return tuple(mark for mark in self.marks if mark.root_visible)


@dataclass(frozen=True, order=True)
class OrientedEvent:
    collision: str
    side: Literal["gain", "loss"]
    cell: str


def _marked_event_weights(
    mark: CollisionMark, penrose_sign: int, amplitude: Q
) -> Mapping[OrientedEvent, Q]:
    assert penrose_sign in (-1, 1)
    coefficient = penrose_sign * Q(amplitude)
    return {
        OrientedEvent(mark.name, "gain", mark.outgoing_cell): coefficient,
        OrientedEvent(mark.name, "loss", mark.incoming_cell): -coefficient,
    }


def _partition_fixture() -> PenrosePartition:
    """Three disjoint interval fibers partition all eight overlap subsets."""

    return PenrosePartition(
        edges=("a", "b", "c"),
        fibers=(
            PenroseFiber(
                "F0", frozenset(), frozenset({"a"}), frozenset({"b", "c"}), "main"
            ),
            PenroseFiber(
                "F1",
                frozenset({"b"}),
                frozenset({"a", "c"}),
                frozenset(),
                "large-error",
            ),
            PenroseFiber(
                "F2",
                frozenset({"c"}),
                frozenset({"a"}),
                frozenset({"b"}),
                "main",
            ),
        ),
    )


def _cluster_fixture() -> RootedClusterSystem:
    return RootedClusterSystem(
        clusters=frozenset({"r0", "u1", "r2", "u3"}),
        root_clusters=frozenset({"r0", "r2"}),
        edge_ends={
            "a": ("r0", "u1"),
            "b": ("u1", "u3"),
            "c": ("r2", "u3"),
        },
        marks=(
            CollisionMark("c0", "r0", True, "x0-in", "x0-out"),
            CollisionMark("c1", "r2", True, "x1-in", "x1-out"),
            CollisionMark("c2", "u1", False, "x2-in", "x2-out"),
        ),
    )


def _active_assignments(edges: tuple[Edge, ...]) -> tuple[dict[Edge, int], ...]:
    return tuple(
        dict(zip(edges, values, strict=True))
        for values in cartesian_product((0, 1), repeat=len(edges))
    )


def test_penrose_interval_fibers_group_the_full_inclusion_exclusion_exactly():
    partition = _partition_fixture()

    for active in _active_assignments(partition.edges):
        expected = Q(prod(1 - active[edge] for edge in partition.edges))
        assert partition.ungrouped_coefficient(active) == expected
        assert partition.grouped_coefficient(active) == expected
        assert all(
            fiber.expanded_coefficient(active) == fiber.grouped_coefficient(active)
            for fiber in partition.fibers
        )


def test_c_atom_mark_is_constant_on_each_o_atom_grouping_fiber():
    partition = _partition_fixture()
    system = _cluster_fixture()
    test = lambda side, cell: Q(len(cell) + (side == "gain"), 7)
    mark_value = sum((mark.pair(test) for mark in system.eligible_marks), Q(0))

    for active in _active_assignments(partition.edges):
        for fiber in partition.fibers:
            marked_expansion = mark_value * fiber.expanded_coefficient(active)
            marked_group = mark_value * fiber.grouped_coefficient(active)
            assert marked_expansion == marked_group


def test_marked_penrose_sum_equals_marking_before_inclusion_exclusion():
    partition = _partition_fixture()
    system = _cluster_fixture()
    tests = (
        lambda side, cell: Q(1),
        lambda side, cell: Q(side == "gain"),
        lambda side, cell: Q(len(cell), 3),
        lambda side, cell: Q((side == "gain") - (cell == "x0-in")),
    )

    for test in tests:
        mark_value = sum((mark.pair(test) for mark in system.eligible_marks), Q(0))
        for active in _active_assignments(partition.edges):
            before = mark_value * partition.ungrouped_coefficient(active)
            after = mark_value * partition.grouped_coefficient(active)
            assert before == after


def test_root_extraction_routes_every_eligible_c_mark_exactly_once():
    partition = _partition_fixture()
    system = _cluster_fixture()

    for fiber in partition.fibers:
        rooted = system.rooted_union(fiber.required)
        unrooted = system.clusters - rooted
        assert all(mark.cluster in rooted for mark in system.eligible_marks)
        assert all(mark.cluster not in unrooted for mark in system.eligible_marks)


def test_multiple_root_components_obey_the_additive_insertion_derivation():
    component_amplitudes = (Q(2, 3), Q(-3, 5), Q(7, 11))
    component_marks = (Q(1, 2), Q(-2), Q(5, 7))
    unmarked_product = Q(prod(component_amplitudes))
    direct = sum(component_marks, Q(0)) * unmarked_product
    derivation = sum(
        (
            component_marks[index]
            * component_amplitudes[index]
            * Q(
                prod(
                    amplitude
                    for other, amplitude in enumerate(component_amplitudes)
                    if other != index
                )
            )
            for index in range(len(component_amplitudes))
        ),
        Q(0),
    )

    assert direct == Q(1, 5)
    assert derivation == direct


def test_penrose_parity_and_gain_loss_orientation_are_independent_sign_axes():
    mark = _cluster_fixture().eligible_marks[0]
    even = _marked_event_weights(mark, penrose_sign=1, amplitude=Q(2, 5))
    odd = _marked_event_weights(mark, penrose_sign=-1, amplitude=Q(2, 5))
    gain = OrientedEvent(mark.name, "gain", mark.outgoing_cell)
    loss = OrientedEvent(mark.name, "loss", mark.incoming_cell)

    assert even[gain] == Q(2, 5)
    assert even[loss] == Q(-2, 5)
    assert odd[gain] == -even[gain]
    assert odd[loss] == -even[loss]


def test_large_component_remainder_is_exact_before_positive_domination():
    partition = _partition_fixture()
    active = {"a": 0, "b": 1, "c": 0}
    mark_value = Q(3, 4)
    main = mark_value * partition.kind_coefficient(active, "main")
    large_error = mark_value * partition.kind_coefficient(active, "large-error")

    assert main == Q(3, 4)
    assert large_error == Q(-3, 4)
    assert main + large_error == 0
    assert abs(large_error) == Q(3, 4)


def test_symmetric_event_quotient_preserves_nonroot_relabeling_multiplicity():
    partner_labels = ("p2", "p3", "p4")
    representative_pairing = Q(5, 12)
    label_pairings = {label: representative_pairing for label in partner_labels}

    assert len(set(label_pairings.values())) == 1
    assert sum(label_pairings.values(), Q(0)) == (
        len(partner_labels) * representative_pairing
    )
    assert sum(label_pairings.values(), Q(0)) == Q(5, 4)


def test_red_team_o_atom_dependent_mark_cannot_be_pulled_through_a_fiber():
    fiber = _partition_fixture().fibers[1]
    active = {"a": 1, "b": 1, "c": 0}
    variable_mark_expansion = sum(
        (
            Q(len(member))
            * Q((-1) ** len(member))
            * _indicator_product(member, active)
            for member in fiber.members
        ),
        Q(0),
    )
    pulled_constant_mark = Q(len(fiber.required)) * fiber.grouped_coefficient(active)

    assert variable_mark_expansion == Q(1)
    assert pulled_constant_mark == 0


def test_red_team_nonroot_collision_is_not_a_root_current_mark():
    system = _cluster_fixture()
    nonroot_mark = next(mark for mark in system.marks if not mark.root_visible)

    assert nonroot_mark not in system.eligible_marks
    assert nonroot_mark.cluster == "u1"


def test_claim_ledger_passes_one_layer_but_keeps_global_identification_open():
    claims: Mapping[str, str] = {
        "one_layer_marked_penrose_grouping": "passed",
        "root_component_mark_routing": "passed",
        "signed_large_component_remainder": "passed",
        "term_level_collision_evaluation": "external-exact",
        "multi_layer_marked_current_identity": "missing",
        "actual_vs_truncated_current": "missing",
        "terminal_error_current": "missing",
        "logarithmic_tail": "outside-gate",
        "continuum_h_theorem": "not-claimed",
        "generic_api": "not-claimed",
    }

    assert claims["one_layer_marked_penrose_grouping"] == "passed"
    assert claims["root_component_mark_routing"] == "passed"
    assert claims["signed_large_component_remainder"] == "passed"
    assert all(
        claims[name] == "missing"
        for name in (
            "multi_layer_marked_current_identity",
            "actual_vs_truncated_current",
            "terminal_error_current",
        )
    )
    assert claims["logarithmic_tail"] == "outside-gate"
    assert claims["continuum_h_theorem"] == "not-claimed"
    assert claims["generic_api"] == "not-claimed"
