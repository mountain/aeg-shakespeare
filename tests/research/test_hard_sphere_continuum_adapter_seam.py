"""Exact Phase 1E shadows of the hard-sphere continuum adapter seam.

The continuum BBGKY collision operator reads an ``(s + 1)``-particle trace
on the contact boundary.  These tests do *not* discretize or prove that
continuum theorem.  They freeze a finite rational quadrature shadow of one
boundary channel so that four pieces of the proposed adapter can be checked
without floating-point or entropy input:

* the elastic collision involution;
* the positive gain/loss cone and its A/M chart on a positive target value;
* the exact decomposition of the finite-to-limit generator defect into
  Boltzmann--Grad scaling, contact displacement, and correlation-trace terms;
* the obstruction to controlling a boundary task by a bulk L1 budget alone.

The last item is deliberately continuum-native.  A boundary layer can have
vanishing bulk L1 mass while retaining a fixed trace, so the L1 state estimate
in a kinetic limit cannot by itself certify the collision-process jet.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable


Q = Fraction
Vector = tuple[Q, ...]
OneBodyDensity = Callable[[Vector, Vector], Q]


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def _scale(scalar: Q, vector: Vector) -> Vector:
    return tuple(scalar * value for value in vector)


def _dot(left: Vector, right: Vector) -> Q:
    return sum((x * y for x, y in zip(left, right)), Q(0))


def _squared_norm(vector: Vector) -> Q:
    return _dot(vector, vector)


@dataclass(frozen=True)
class CollisionNode:
    """One positive-flux node in a rational boundary quadrature."""

    partner_velocity: Vector
    normal: Vector
    weight: Q


@dataclass(frozen=True)
class GainLossJet:
    """The chart-independent positive cone before division by the state."""

    gain: Q
    loss: Q

    @property
    def tangent(self) -> Q:
        return self.gain - self.loss

    def am_chart(self, value: Q) -> tuple[Q, Q]:
        """Return ``(A, M)`` with ``gain - loss = A + value * M``."""

        if value <= 0:
            raise ValueError("the A/M boundary chart requires a positive value")
        return self.gain, -self.loss / value


@dataclass(frozen=True)
class BoundaryResidual:
    """Signed correlation data retained on the two oriented traces."""

    gain_trace: Q = Q(0)
    loss_trace: Q = Q(0)

    @property
    def tangent(self) -> Q:
        return self.gain_trace - self.loss_trace


def _elastic_preimage(
    velocity: Vector, partner_velocity: Vector, normal: Vector
) -> tuple[Vector, Vector]:
    """Invert one equal-mass elastic collision at a fixed unit normal."""

    assert _squared_norm(normal) == 1
    relative_normal = _dot(
        tuple(x - y for x, y in zip(velocity, partner_velocity)),
        normal,
    )
    impulse = _scale(relative_normal, normal)
    return (
        tuple(x - y for x, y in zip(velocity, impulse)),
        tuple(x + y for x, y in zip(partner_velocity, impulse)),
    )


def _positive_flux(velocity: Vector, node: CollisionNode) -> Q:
    flux = _dot(
        node.normal,
        tuple(
            partner - target
            for partner, target in zip(node.partner_velocity, velocity)
        ),
    )
    assert flux > 0
    return node.weight * flux


def _factorized_boundary_jet(
    density: OneBodyDensity,
    position: Vector,
    velocity: Vector,
    nodes: tuple[CollisionNode, ...],
    epsilon: Q,
    prefactor: Q = Q(1),
    residuals: tuple[BoundaryResidual, ...] | None = None,
) -> GainLossJet:
    """Evaluate an oriented factorized trace section plus residual.

    For a positive-flux node, the outgoing trace is pulled back through the
    collision involution before factorization.  The two contact evaluations
    occur at ``x + epsilon * omega`` and ``x - epsilon * omega``.  They agree
    only after the contact displacement is actually sent to zero.
    """

    if residuals is None:
        residuals = tuple(BoundaryResidual() for _ in nodes)
    assert len(residuals) == len(nodes)

    gain = Q(0)
    loss = Q(0)
    for node, residual in zip(nodes, residuals):
        coefficient = _positive_flux(velocity, node)
        pre_velocity, pre_partner = _elastic_preimage(
            velocity, node.partner_velocity, node.normal
        )
        gain_position = _add(position, _scale(epsilon, node.normal))
        loss_position = _add(position, _scale(-epsilon, node.normal))
        gain_trace = (
            density(position, pre_velocity)
            * density(gain_position, pre_partner)
            + residual.gain_trace
        )
        loss_trace = (
            density(position, velocity)
            * density(loss_position, node.partner_velocity)
            + residual.loss_trace
        )
        gain += coefficient * gain_trace
        loss += coefficient * loss_trace

    return GainLossJet(prefactor * gain, prefactor * loss)


def _fixture() -> tuple[
    OneBodyDensity,
    Vector,
    Vector,
    tuple[CollisionNode, ...],
]:
    position = (Q(0), Q(0))
    velocity = (Q(1), Q(0))
    node = CollisionNode(
        partner_velocity=(Q(-1), Q(0)),
        normal=(Q(-3, 5), Q(-4, 5)),
        # The raw positive flux is 6/5, so this makes the quadrature
        # coefficient exactly one and keeps every certificate readable.
        weight=Q(5, 6),
    )

    def density(x: Vector, v: Vector) -> Q:
        # Positive on every point used by the frozen fixture.  The anisotropic
        # v_0^2 term avoids making the chosen collision an equilibrium channel.
        return Q(10) + x[0] + Q(2) * x[1] + v[0] * v[0]

    return density, position, velocity, (node,)


def test_elastic_collision_map_is_an_exact_involution_and_conserves_rulers():
    _, _, velocity, nodes = _fixture()
    node = nodes[0]
    partner = node.partner_velocity
    pre_velocity, pre_partner = _elastic_preimage(
        velocity, partner, node.normal
    )
    restored_velocity, restored_partner = _elastic_preimage(
        pre_velocity, pre_partner, node.normal
    )

    assert (restored_velocity, restored_partner) == (velocity, partner)
    assert _add(pre_velocity, pre_partner) == _add(velocity, partner)
    assert (
        _squared_norm(pre_velocity) + _squared_norm(pre_partner)
        == _squared_norm(velocity) + _squared_norm(partner)
    )
    assert _positive_flux(velocity, node) == 1


def test_positive_boundary_cone_has_an_exact_am_chart_on_positive_states():
    density, position, velocity, nodes = _fixture()
    jet = _factorized_boundary_jet(
        density, position, velocity, nodes, epsilon=Q(0)
    )
    value = density(position, velocity)
    additive, multiplicative = jet.am_chart(value)

    assert value == 11
    assert jet.gain == Q(6299, 625) ** 2
    assert jet.loss == 121
    assert jet.gain >= 0
    assert jet.loss >= 0
    assert additive >= 0
    assert multiplicative == -11
    assert additive + value * multiplicative == jet.tangent


def test_gain_loss_cone_survives_where_the_am_division_chart_is_singular():
    jet = GainLossJet(gain=Q(3, 7), loss=Q(2, 5))

    assert jet.tangent == Q(1, 35)
    try:
        jet.am_chart(Q(0))
    except ValueError as error:
        assert "positive" in str(error)
    else:
        raise AssertionError("zero density must not enter the multiplicative chart")


def test_generator_defect_splits_into_scaling_contact_and_trace_residuals():
    density, position, velocity, nodes = _fixture()
    epsilon = Q(1, 10)
    alpha = Q(7, 6)
    residuals = (BoundaryResidual(Q(3, 7), Q(1, 5)),)

    limit_section = _factorized_boundary_jet(
        density, position, velocity, nodes, epsilon=Q(0)
    ).tangent
    finite_section = _factorized_boundary_jet(
        density, position, velocity, nodes, epsilon=epsilon
    ).tangent
    finite_source = _factorized_boundary_jet(
        density,
        position,
        velocity,
        nodes,
        epsilon=epsilon,
        prefactor=alpha,
        residuals=residuals,
    ).tangent

    scaling_defect = (alpha - 1) * limit_section
    contact_defect = alpha * (finite_section - limit_section)
    correlation_trace_defect = alpha * residuals[0].tangent

    assert scaling_defect != 0
    assert contact_defect != 0
    assert correlation_trace_defect != 0
    assert (
        finite_source - limit_section
        == scaling_defect + contact_defect + correlation_trace_defect
    )


def test_bulk_l1_smallness_does_not_control_the_collision_boundary_trace():
    # g_n(r) = max(1 - n r, 0) on r >= 0 has the exact triangular area
    # 1/(2n), while its boundary trace g_n(0) remains one.
    widths = (2, 4, 8, 16)
    bulk_l1 = tuple(Q(1, 2 * n) for n in widths)
    boundary_trace = tuple(Q(1) for _ in widths)

    assert bulk_l1 == (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32))
    assert all(left > right for left, right in zip(bulk_l1, bulk_l1[1:]))
    assert boundary_trace == (Q(1),) * len(widths)


def test_continuum_adapter_tasks_remain_separately_typed():
    grades = {
        "bulk_correlation_to_factorized_state_in_L1": "external_theorem",
        "boundary_trace_to_gain_loss_jet": "exact_operator_contract",
        "bulk_L1_to_boundary_trace": "rejected",
        "positive_gain_loss_to_am_jet": "chart_exact_on_positive_domain",
        "collision_history_to_long_time_mild_comparison": "external_theorem",
        "am_first_jet_to_full_collision_future": "unclaimed",
    }

    assert grades["bulk_L1_to_boundary_trace"] == "rejected"
    assert (
        grades["boundary_trace_to_gain_loss_jet"]
        == "exact_operator_contract"
    )
    assert grades["am_first_jet_to_full_collision_future"] == "unclaimed"
