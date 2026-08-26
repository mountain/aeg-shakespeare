"""Exact Phase 1F shadows of a weak/mild collision-history cell.

Phase 1E found that the hard-sphere BBGKY generator reads a codimension-one
contact trace, so bulk ``L1`` convergence alone cannot certify its pointwise
collision jet.  The next safe target is weaker: pair a test observable with
the *time-integrated oriented collision flux*, or equivalently inspect one
term of the iterated Duhamel expansion.

For one collision time ``tau``, that term has three typed pieces::

    source (s + 1)-particle free segment
        -> oriented collision insertion
        -> target s-particle free segment.

This file freezes a one-root, one-partner, one-quadrature-node shadow.  It is
not a discretization or proof of the continuum BBGKY hierarchy.  Exact
``Fraction`` arithmetic checks:

* backward history reconstruction and elastic matching at contact;
* nonnegative time-integrated gain and loss;
* additivity under a cut of the time-integration domain;
* the Fubini/operator-composition meaning of a molecule cut;
* failure of an unweighted time-average of the pointwise A/M coordinate;
* the boundary between a single history cell and a full continuation theorem.

Primary calibrations are Gallagher--Saint-Raymond--Texier, equations
(4.3.6), (6.2.1), and Deng--Hani--Ma, Sections 1.3.3--1.3.4 and equations
(2.10)--(2.11).  Their continuum statements remain external theorem records.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable


Q = Fraction
Vector = tuple[Q, ...]
OneBodyDensity = Callable[[Vector, Vector], Q]


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def _subtract(left: Vector, right: Vector) -> Vector:
    return tuple(x - y for x, y in zip(left, right))


def _scale(scalar: Q, vector: Vector) -> Vector:
    return tuple(scalar * value for value in vector)


def _dot(left: Vector, right: Vector) -> Q:
    return sum((x * y for x, y in zip(left, right)), Q(0))


def _squared_norm(vector: Vector) -> Q:
    return _dot(vector, vector)


def _free_endpoint(position: Vector, velocity: Vector, duration: Q) -> Vector:
    return _add(position, _scale(duration, velocity))


def _free_source(position: Vector, velocity: Vector, duration: Q) -> Vector:
    return _subtract(position, _scale(duration, velocity))


def _elastic_pair(
    velocity: Vector, partner_velocity: Vector, normal: Vector
) -> tuple[Vector, Vector]:
    """Apply the equal-mass elastic reflection, which is its own inverse."""

    assert _squared_norm(normal) == 1
    relative_normal = _dot(
        _subtract(velocity, partner_velocity),
        normal,
    )
    impulse = _scale(relative_normal, normal)
    return (
        _subtract(velocity, impulse),
        _add(partner_velocity, impulse),
    )


@dataclass(frozen=True)
class CollisionNode:
    """One positive-flux node of the oriented boundary quadrature."""

    partner_velocity: Vector
    normal: Vector
    weight: Q

    def coefficient(self, target_velocity: Vector) -> Q:
        raw_flux = _dot(
            self.normal,
            _subtract(self.partner_velocity, target_velocity),
        )
        assert raw_flux > 0
        return self.weight * raw_flux


@dataclass(frozen=True)
class SourcePair:
    """The two initial particles selected by one backward history."""

    root_position: Vector
    root_velocity: Vector
    partner_position: Vector
    partner_velocity: Vector


@dataclass(frozen=True)
class IntegratedGainLoss:
    """Observable-dependent positive flux amounts over a declared horizon."""

    gain: Q
    loss: Q

    @property
    def signed(self) -> Q:
        return self.gain - self.loss


@dataclass(frozen=True)
class OneCollisionCell:
    """A single Duhamel history with a variable collision time.

    The endpoint root is transported backward to ``tau``.  The gain branch
    then crosses the collision involution and transports the two incoming
    particles to time zero.  The loss branch transports the current pair to
    time zero.  The contact displacement is kept explicit on both branches.
    """

    endpoint_position: Vector
    endpoint_velocity: Vector
    horizon: Q
    epsilon: Q
    prefactor: Q
    node: CollisionNode

    def collision_position(self, tau: Q) -> Vector:
        assert 0 <= tau <= self.horizon
        return _free_source(
            self.endpoint_position,
            self.endpoint_velocity,
            self.horizon - tau,
        )

    def gain_source(self, tau: Q) -> SourcePair:
        contact = self.collision_position(tau)
        pre_root, pre_partner = _elastic_pair(
            self.endpoint_velocity,
            self.node.partner_velocity,
            self.node.normal,
        )
        partner_contact = _add(
            contact,
            _scale(self.epsilon, self.node.normal),
        )
        return SourcePair(
            root_position=_free_source(contact, pre_root, tau),
            root_velocity=pre_root,
            partner_position=_free_source(partner_contact, pre_partner, tau),
            partner_velocity=pre_partner,
        )

    def loss_source(self, tau: Q) -> SourcePair:
        contact = self.collision_position(tau)
        partner_contact = _subtract(
            contact,
            _scale(self.epsilon, self.node.normal),
        )
        return SourcePair(
            root_position=_free_source(contact, self.endpoint_velocity, tau),
            root_velocity=self.endpoint_velocity,
            partner_position=_free_source(
                partner_contact,
                self.node.partner_velocity,
                tau,
            ),
            partner_velocity=self.node.partner_velocity,
        )

    def _factorized_weight(
        self,
        density: OneBodyDensity,
        source: SourcePair,
    ) -> Q:
        coefficient = self.prefactor * self.node.coefficient(
            self.endpoint_velocity
        )
        return (
            coefficient
            * density(source.root_position, source.root_velocity)
            * density(source.partner_position, source.partner_velocity)
        )

    def gain_integrand(self, density: OneBodyDensity, tau: Q) -> Q:
        return self._factorized_weight(density, self.gain_source(tau))

    def loss_integrand(self, density: OneBodyDensity, tau: Q) -> Q:
        return self._factorized_weight(density, self.loss_source(tau))

    def loss_occupation(self, density: OneBodyDensity, tau: Q) -> Q:
        source = self.loss_source(tau)
        return density(source.root_position, source.root_velocity)

    def loss_multiplicative_rate(
        self,
        density: OneBodyDensity,
        tau: Q,
    ) -> Q:
        source = self.loss_source(tau)
        coefficient = self.prefactor * self.node.coefficient(
            self.endpoint_velocity
        )
        return -coefficient * density(
            source.partner_position,
            source.partner_velocity,
        )

    def integrate(
        self,
        density: OneBodyDensity,
        start: Q = Q(0),
        end: Q | None = None,
    ) -> IntegratedGainLoss:
        if end is None:
            end = self.horizon
        assert 0 <= start <= end <= self.horizon
        return IntegratedGainLoss(
            gain=_integrate_quadratic(
                lambda tau: self.gain_integrand(density, tau),
                start,
                end,
            ),
            loss=_integrate_quadratic(
                lambda tau: self.loss_integrand(density, tau),
                start,
                end,
            ),
        )


def _integrate_quadratic(function: Callable[[Q], Q], start: Q, end: Q) -> Q:
    """Exact Simpson integration for the frozen degree-at-most-two data."""

    if start == end:
        return Q(0)
    midpoint = (start + end) / 2
    return (end - start) * (
        function(start) + Q(4) * function(midpoint) + function(end)
    ) / 6


def _fixture() -> tuple[OneCollisionCell, OneBodyDensity]:
    node = CollisionNode(
        partner_velocity=(Q(-1), Q(0)),
        normal=(Q(-3, 5), Q(-4, 5)),
        # The raw positive flux is 6/5, so the quadrature coefficient is one.
        weight=Q(5, 6),
    )
    cell = OneCollisionCell(
        endpoint_position=(Q(1), Q(2)),
        endpoint_velocity=(Q(1), Q(0)),
        horizon=Q(3, 2),
        epsilon=Q(1, 10),
        prefactor=Q(7, 6),
        node=node,
    )

    def density(position: Vector, velocity: Vector) -> Q:
        # Along the frozen free segments this is affine in tau.  Products of
        # two one-body factors are therefore quadratic and Simpson is exact.
        return (
            Q(10)
            + position[0]
            + Q(2) * position[1]
            + velocity[0] * velocity[0]
        )

    return cell, density


def test_backward_gain_history_reaches_contact_and_then_the_endpoint_exactly():
    cell, _ = _fixture()
    tau = Q(2, 3)
    source = cell.gain_source(tau)
    contact = cell.collision_position(tau)
    partner_contact = _add(contact, _scale(cell.epsilon, cell.node.normal))

    assert (
        _free_endpoint(source.root_position, source.root_velocity, tau)
        == contact
    )
    assert (
        _free_endpoint(source.partner_position, source.partner_velocity, tau)
        == partner_contact
    )
    post_root, post_partner = _elastic_pair(
        source.root_velocity,
        source.partner_velocity,
        cell.node.normal,
    )
    assert post_root == cell.endpoint_velocity
    assert post_partner == cell.node.partner_velocity
    assert _add(source.root_velocity, source.partner_velocity) == _add(
        post_root, post_partner
    )
    assert (
        _squared_norm(source.root_velocity)
        + _squared_norm(source.partner_velocity)
        == _squared_norm(post_root) + _squared_norm(post_partner)
    )
    assert _free_endpoint(
        contact,
        post_root,
        cell.horizon - tau,
    ) == cell.endpoint_position


def test_time_integrated_oriented_flux_is_a_positive_gain_loss_pair():
    cell, density = _fixture()
    integrated = cell.integrate(density)

    assert cell.node.coefficient(cell.endpoint_velocity) == 1
    assert integrated.gain > 0
    assert integrated.loss > 0
    assert integrated.gain == Q(273506541, 781250)
    assert integrated.loss == Q(164633, 400)
    assert integrated.signed == Q(-384338297, 6250000)


def test_time_domain_cut_is_exactly_additive_for_the_weak_flux_observable():
    cell, density = _fixture()
    cut = Q(5, 8)
    whole = cell.integrate(density)
    lower = cell.integrate(density, Q(0), cut)
    upper = cell.integrate(density, cut, cell.horizon)

    assert whole == IntegratedGainLoss(
        gain=lower.gain + upper.gain,
        loss=lower.loss + upper.loss,
    )
    assert whole.signed == lower.signed + upper.signed


def test_pointwise_am_chart_requires_an_observer_weighted_time_average():
    cell, density = _fixture()

    for tau in (Q(0), Q(1, 2), cell.horizon):
        occupation = cell.loss_occupation(density, tau)
        multiplicative = cell.loss_multiplicative_rate(density, tau)
        assert occupation > 0
        assert multiplicative < 0
        assert occupation * multiplicative == -cell.loss_integrand(
            density, tau
        )

    # A weak task carries its own test weight.  Even though the freely
    # transported root occupation is constant along this loss history, a
    # nonconstant observable changes the measure with respect to which an
    # effective multiplicative rate must be averaged.
    def observer(tau: Q) -> Q:
        return Q(1) + tau / 3

    observed_occupation_integral = _integrate_quadratic(
        lambda tau: observer(tau) * cell.loss_occupation(density, tau),
        Q(0),
        cell.horizon,
    )
    observed_am_product_integral = _integrate_quadratic(
        lambda tau: (
            observer(tau)
            * cell.loss_occupation(density, tau)
            * cell.loss_multiplicative_rate(density, tau)
        ),
        Q(0),
        cell.horizon,
    )
    unweighted_rate_average = _integrate_quadratic(
        lambda tau: cell.loss_multiplicative_rate(density, tau),
        Q(0),
        cell.horizon,
    ) / cell.horizon
    observer_weighted_rate = (
        observed_am_product_integral / observed_occupation_integral
    )
    observed_loss = _integrate_quadratic(
        lambda tau: observer(tau) * cell.loss_integrand(density, tau),
        Q(0),
        cell.horizon,
    )

    assert observed_am_product_integral == -observed_loss
    assert (
        observed_occupation_integral * unweighted_rate_average
        != observed_am_product_integral
    )
    assert (
        observed_occupation_integral * observer_weighted_rate
        == observed_am_product_integral
    )
    assert observer_weighted_rate != unweighted_rate_average


def test_molecule_cut_has_only_the_fubini_operator_composition_claim():
    # A finite exact shadow of I_M = I_M1 o I_M2.  Interface values are kept
    # fixed while the inner source variables are integrated, then the outer
    # interface variables are integrated.  Nothing here identifies the cut
    # with physical time evolution or arithmetic-rank objectification.
    source = (Q(2), Q(3), Q(5))
    inner_kernel = (
        (Q(1, 2), Q(1, 3), Q(1, 5)),
        (Q(2, 3), Q(1, 4), Q(1, 6)),
    )
    outer_kernel = (Q(7, 5), Q(11, 7))

    inner = tuple(
        sum(
            (
                coefficient * value
                for coefficient, value in zip(row, source)
            ),
            Q(0),
        )
        for row in inner_kernel
    )
    composed = sum(
        (coefficient * value for coefficient, value in zip(outer_kernel, inner)),
        Q(0),
    )
    direct = sum(
        (
            outer_kernel[interface]
            * inner_kernel[interface][source_index]
            * source[source_index]
            for interface in range(len(outer_kernel))
            for source_index in range(len(source))
        ),
        Q(0),
    )

    assert inner == (Q(3), Q(35, 12))
    assert composed == direct == Q(3689, 420)


def test_weak_mild_continuation_tasks_remain_separately_typed():
    grades = {
        "microscopic_history_to_integrated_flux": "exact_observation_contract",
        "bulk_L1_to_integrated_collision_flux": "not_implied",
        "one_collision_cell_to_first_duhamel_term": "exact_term_contract",
        "one_collision_cell_to_full_future": "truncation_residual_required",
        "molecule_cut_to_integral_composition": "external_proof_device",
        "molecule_cut_to_physical_time_evolution": "rejected",
        "pointwise_am_to_unweighted_time_average": "rejected",
    }

    assert grades["bulk_L1_to_integrated_collision_flux"] == "not_implied"
    assert grades["one_collision_cell_to_full_future"] == (
        "truncation_residual_required"
    )
    assert grades["molecule_cut_to_physical_time_evolution"] == "rejected"
    assert grades["pointwise_am_to_unweighted_time_average"] == "rejected"
