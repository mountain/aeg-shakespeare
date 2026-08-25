"""Cross-problem audit: canonical quotients versus history carriers.

The pendulum suggested that canonicalization can supply a task quotient and an
invariant edge measure before Huffman/Bellman stopping optimization.  This
essay red-teams that picture on three deliberately heterogeneous exact models:

* hard-particle first contact -- continuous first-hit / decision tree;
* signed translation -- discrete continuation quotient / reconvergent graph;
* Abelian closed-history residual -- covering history / deck groupoid.

The result is a split, not a universal tree theorem.  All three have a canonical
history quotient.  Only the first forces a stopping tree.  The second forces
reconvergence, and the third retains compositional invisible-history residuals.

No generic framework class is proposed by this research-local calibration.
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CorrespondenceProfile:
    problem: str
    canonical_state: str
    history_carrier: str
    residual: str
    cost_status: str
    huffman_role: str


def _collision_times(positions, velocities):
    return tuple(
        Fraction(positions[i + 1] - positions[i], velocities[i] - velocities[i + 1])
        for i in range(len(positions) - 1)
    )


def _minimum_group(times):
    minimum = min(times)
    return tuple(index for index, value in enumerate(times) if value == minimum)


def test_hard_particle_canonicalization_preserves_first_hit_task_and_clock():
    positions = tuple(map(Fraction, (0, 2, 7, 13)))
    velocities = tuple(map(Fraction, (7, 5, 2, 0)))
    times = _collision_times(positions, velocities)

    # Spatial affine changes and a Galilean boost are presentation changes.
    scale, shift, boost = Fraction(3), Fraction(11), Fraction(5)
    transformed_positions = tuple(scale * x + shift for x in positions)
    transformed_velocities = tuple(scale * v + boost for v in velocities)

    assert _collision_times(transformed_positions, transformed_velocities) == times
    assert _minimum_group(times) == (0,)
    assert min(times) == Fraction(1)


def _net_displacement(history):
    return sum(1 if step == "S" else -1 for step in history)


def test_translation_canonicalization_is_continuation_stable_but_reconvergent():
    left = "SSP"
    right = "PSS"
    continuation = "SPPS"

    assert left != right
    assert _net_displacement(left) == _net_displacement(right) == 1
    assert _net_displacement(left + continuation) == _net_displacement(
        right + continuation
    )

    # The free prefix tree has two distinct nodes, while the canonical carrier
    # merges them.  Hence a tree is an unfolding, not the quotient ontology.
    free_nodes = {left, right}
    quotient_nodes = {_net_displacement(left), _net_displacement(right)}
    assert len(free_nodes) == 2
    assert len(quotient_nodes) == 1

    # Bare word length is not a quotient-invariant cost.
    assert _net_displacement("S") == _net_displacement("SSP")
    assert len("S") != len("SSP")


def _compose_period_residual(left, right):
    """Formal genus-two period residual (m,n) in Z^2 + tau Z^2."""

    left_m, left_n = left
    right_m, right_n = right
    return (
        tuple(a + b for a, b in zip(left_m, right_m, strict=True)),
        tuple(a + b for a, b in zip(left_n, right_n, strict=True)),
    )


def test_abelian_closed_histories_require_a_compositional_residual_group():
    zero = ((0, 0), (0, 0))
    a1 = ((1, 0), (0, 0))
    b2 = ((0, 0), (0, 1))

    # All are closed at the visible base state, but lifted histories differ.
    visible_endpoint = {zero: "base", a1: "base", b2: "base"}
    assert len(set(visible_endpoint.values())) == 1
    assert len(visible_endpoint) == 3

    combined = _compose_period_residual(a1, b2)
    assert combined == ((1, 0), (0, 1))
    assert _compose_period_residual(combined, ((-1, 0), (0, -1))) == zero

    # Quotienting the lifted coordinate modulo periods may identify endpoints,
    # but the residual grammar must survive when winding/period is task data.
    endpoint_only_classes = {"base" for _ in visible_endpoint}
    residual_aware_classes = set(visible_endpoint)
    assert len(endpoint_only_classes) == 1
    assert len(residual_aware_classes) == 3


def test_cross_problem_profiles_force_tree_graph_groupoid_split():
    profiles = (
        CorrespondenceProfile(
            "hard-particle-first-contact",
            "candidate-time argmin stratum",
            "first-hit decision tree",
            "simultaneous-minimum tie set",
            "physical first-hit time is invariant",
            "native stopping optimization",
        ),
        CorrespondenceProfile(
            "signed-translation",
            "net displacement",
            "reconvergent Cayley graph / DAG",
            "discarded word representative",
            "requires declared grammar or objectification cost",
            "optional coding of a finite task distribution",
        ),
        CorrespondenceProfile(
            "Abelian-period-history",
            "normalized coordinate modulo period lattice",
            "covering space / deck groupoid",
            "integer period-lattice element",
            "differential integral is additive",
            "only after a finite stopping task is declared",
        ),
    )

    assert {profile.history_carrier for profile in profiles} == {
        "first-hit decision tree",
        "reconvergent Cayley graph / DAG",
        "covering space / deck groupoid",
    }
    assert sum("native" in profile.huffman_role for profile in profiles) == 1

