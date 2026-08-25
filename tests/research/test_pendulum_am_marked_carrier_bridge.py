"""Pendulum A/M presentation audit: marked carrier, clock, and task memory.

Retrieval
---------
Problem: how do Addition/Multiplication presentation changes, the pendulum
elliptic carrier, its Abel clock, and the hidden Cartesian sheet fit together?
Domains: simple pendulum, elliptic curves, point transformations, moving
frames, dimensional analysis, covering spaces, continuation memory.
Classical aliases: energy reduction, first-order prolongation, transformed
second-order ODE, Abelian differential, nontrivial double cover.
Process Geometry roles: supplied A/M chart, marked carrier, task-relative
presentation class, lifted clock, transported scale line, continuation
residual, second-jet boundary.
Stable family entry: ``docs/vignettes/simple-pendulum.md``.

Question
--------
PRs 80--91 left five statements close enough to be confused but not identical:

1. an affine Addition/Multiplication chart can globally re-present the marked
   elliptic carrier;
2. a nonlinear A/M expression such as ``X=U^3`` can preserve the clock on a
   regular real task interval without being a global regular curve chart;
3. transporting the clock uses only ``h'``, while transporting the full
   reduced mechanical flow through ``X=h(U)`` also requires ``h''``; and
4. the Cartesian ``Z2`` sheet is dispensable for a carrier-only task but is
   one bit of necessary continuation state for full physical reconstruction;
   and
5. the Bolza surface appears only after adjoining a separate, declared
   observer-metric square-root sheet; it is not another coordinate
   presentation of the pendulum elliptic carrier.

This essay certifies those distinctions exactly.  It does not manufacture the
missing pendulum ``AMJet`` or a canonical moving observer.

Primitive data
--------------
On a fixed dimensionless energy leaf use

    U = q_y,  Y = D U,
    Y^2 = 2 (E-U) (1-U^2),
    D U = Y,  D Y = 3 U^2 - 2 E U - 1,
    omega = dU / Y.

A supplied scalar presentation is ``X=h(U)``, with prolonged velocity
``Z=D X=h'(U)Y``.  The physical clock is

    dt = sqrt(ell/g) omega.

The E=0 real carrier closes after one carrier period, while the Cartesian mark
flips and closes only after two.  Upstream essays establish the carrier, the
period, and the unramified cover; this file tests their task-memory consequence.

A separate earlier experiment declares an A/M metric with weight ``c``.  Its
oriented arc-length sheet has model ``Z_m^2=c+U^2``.  Combining this independent
sheet with the physical velocity sheet produces the third quadratic quotient

    W^2 = 2 (E-U) (1-U^2) (c+U^2).

Only on the symmetric choice ``E=0,c=1`` does ``w=W/sqrt(2)`` give the affine
Bolza model ``w^2=U^5-U``.

Classical lineage
-----------------
The transformed vector field is the ordinary second prolongation of a point
transformation:

    D Z = h''(U) Y^2 + h'(U) D Y.

The first term is the deterministic second-jet analogue of the correction that
appears when a nonlinear chart transports a second-order generator.  Elliptic
uniformization and Abelian differentials are classical; see [Arnold-1989] and
[DLMF-22].  The finite memory argument is the two-class distinguishability
argument used by Myhill--Nerode theory, here applied only to the certified
``Z2`` cover.

Process Geometry reconstruction
-------------------------------
The executable chain is deliberately vertical rather than an embedding of the
elliptic curve into the A/M half-plane:

    supplied A/M presentation
      -> prolonged reduced dynamics
      -> task-relative marked carrier (C_E, omega)
      -> lifted Abel clock
      -> period quotient / elliptic readout,

with a separate Cartesian sheet residual retained only when the task observes
it.  An affine ``h(U)=sU+b`` is a global invertible A/M chart for ``s!=0``.
The nonlinear ``h(U)=U^3`` is regular on the frozen negative libration interval
used by the equal-clock red team, but its derivative vanishes at the E=0 point
``(U,Y)=(0,0)``; local task covariance is therefore not a global birational
equivalence certificate.

Calibration statement
---------------------
Passing this file certifies:

1. every supplied affine A/M chart pulls its transformed cubic back to the
   source cubic and preserves ``dX/Z=dU/Y`` exactly;
2. ``X=U^3`` preserves the marked clock wherever ``U!=0``, but is singular at
   a point of the E=0 carrier and is therefore only a local task chart here;
3. exact transport of the reduced flow contains ``h''Y^2``; omitting it leaves
   a generically nonzero residual even though the clock still agrees;
4. the dimensional multiplier ``sqrt(ell/g)`` transports the same clock in
   both presentations and scales as a time unit should;
5. the carrier-only task has one continuation class and needs zero residual
   bits, while full Cartesian continuation has two classes and needs one bit;
6. the Bolza polynomial is the third quotient of the physical and declared
   metric sheets at ``E=0,c=1`` and varies when the metric weight varies.

Proof map
---------
``test_affine_am_chart_globally_represents_the_marked_carrier`` proves item 1.
``test_nonlinear_clock_chart_is_local_and_requires_a_second_jet`` proves 2--3.
``test_physical_time_is_a_transported_scale_line_not_coordinate_distance``
proves item 4.
``test_cartesian_sheet_is_exactly_one_task_visible_continuation_bit`` proves 5.
``test_bolza_is_a_declared_metric_completion_not_a_pendulum_chart`` proves 6.

Effective-analysis audit
------------------------
Mode: exact symbolic algebra plus a finite exact continuation census.
Closure/evaluator: polynomial/rational expressions evaluated by SymPy; finite
``C2`` signatures evaluated directly.  No numerical approximation is used.
Units: ``U,Y,E`` and ``omega`` are dimensionless; physical time carries
``sqrt(ell/g)``.  Cost claim: none.  The bit count is an exact state lower
bound for the two declared tasks, not a runtime or entropy estimate.

Boundary
--------
This essay does not claim:

- discovery of ``U``, ``h``, the clock, or a normalization from raw A/M
  histories;
- a canonical pendulum moving-observer equation: ``U`` is a selected scalar
  observable, not an observer-group parameter;
- an intrinsic second-order A/M jet; the classical prolongation below states
  the exact certificate that such a jet must reproduce;
- global algebraic equivalence for ``U^3`` or arbitrary monotone real charts;
- that the Bolza surface is the pendulum state space, an A/M presentation of
  its elliptic carrier, or a canonical completion independent of metric choice;
- a generic-energy period lattice or complex Cartesian double cover;
- a Public or Experimental API, a Theory Map promotion, or A/M universality.

References and onward links
---------------------------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
"Jacobian Elliptic Functions", https://dlmf.nist.gov/22 .

Repository links: ``docs/56-am-universal-history-recalibration.md``;
``docs/61-pendulum-section-reparameterization-redteam.md``;
``tests/research/test_pendulum_lifted_clock_global_quotient.py``;
``tests/research/test_am_checkpoint_differential_quotient.py``.
"""

from __future__ import annotations

import sympy as sp


def _reduced_derivative(expression, U, Y, E):
    """Differentiate along DU=Y, DY=3U^2-2EU-1."""

    acceleration = 3 * U**2 - 2 * E * U - 1
    return sp.expand(
        sp.diff(expression, U) * Y
        + sp.diff(expression, Y) * acceleration
    )


def _minimum_exact_bits(signatures):
    """Bits needed to keep all distinct finite continuation signatures."""

    class_count = len(set(signatures.values()))
    return (class_count - 1).bit_length()


def test_affine_am_chart_globally_represents_the_marked_carrier():
    U, Y, E = sp.symbols("U Y E")
    X, Z = sp.symbols("X Z")
    scale = sp.symbols("s", nonzero=True)
    shift = sp.symbols("b")

    source_relation = Y**2 - 2 * (E - U) * (1 - U**2)
    chart = scale * U + shift
    prolonged_velocity = scale * Y

    # Express the same cubic in the affine A/M chart.  Pullback equality is
    # the exact global presentation certificate; the nonzero scale supplies
    # the inverse U=(X-b)/s.
    inverse_U = (X - shift) / scale
    target_relation = sp.expand(
        Z**2
        - 2 * scale**2 * (E - inverse_U) * (1 - inverse_U**2)
    )
    pulled_back = sp.factor(
        target_relation.subs({X: chart, Z: prolonged_velocity})
    )
    assert sp.simplify(pulled_back - scale**2 * source_relation) == 0

    # The carrier equation changes coordinates; the marked clock does not.
    target_clock_coefficient = sp.simplify(
        sp.diff(chart, U) / prolonged_velocity
    )
    assert sp.simplify(target_clock_coefficient - 1 / Y) == 0


def test_nonlinear_clock_chart_is_local_and_requires_a_second_jet():
    U, Y, E = sp.symbols("U Y E")
    carrier_polynomial = 2 * (E - U) * (1 - U**2)
    acceleration = 3 * U**2 - 2 * E * U - 1

    chart = U**3
    chart_prime = sp.diff(chart, U)
    chart_second = sp.diff(chart_prime, U)
    prolonged_velocity = chart_prime * Y

    assert _reduced_derivative(chart, U, Y, E) == prolonged_velocity

    transported_acceleration = _reduced_derivative(
        prolonged_velocity, U, Y, E
    )
    expected_acceleration = sp.expand(
        chart_second * Y**2 + chart_prime * acceleration
    )
    assert sp.expand(transported_acceleration - expected_acceleration) == 0

    # The naive first-order transport preserves neither the second jet nor the
    # observed dynamics.  Reducing its missing term on the carrier leaves a
    # nonzero polynomial; at E=0,U=-1/2 it is manifestly nonzero.
    naive_acceleration = sp.expand(chart_prime * acceleration)
    missing_second_jet = sp.expand(
        transported_acceleration - naive_acceleration
    )
    assert missing_second_jet == 6 * U * Y**2
    reduced_residual = sp.factor(
        missing_second_jet.subs(Y**2, carrier_polynomial)
    )
    assert reduced_residual != 0
    witness = reduced_residual.subs({E: 0, U: sp.Rational(-1, 2)})
    assert sp.simplify(witness) != 0

    # Nevertheless the one-form clock is transported exactly on a regular
    # branch.  This is why the PR #85 clock/Bellman square can pass without
    # having constructed the missing global second-order A/M lift.
    assert sp.simplify(chart_prime / prolonged_velocity - 1 / Y) == 0

    # U^3 is strictly increasing on the frozen negative interval, but its
    # derivative vanishes at (U,Y,E)=(0,0,0), a point of the E=0 carrier.
    assert chart_prime.subs(U, sp.Rational(-1, 2)) > 0
    assert chart_prime.subs(U, 0) == 0
    source_relation = Y**2 - carrier_polynomial
    assert source_relation.subs({U: 0, Y: 0, E: 0}) == 0


def test_physical_time_is_a_transported_scale_line_not_coordinate_distance():
    U, Y = sp.symbols("U Y")
    length, gravity, ruler_scale = sp.symbols(
        "ell g k", positive=True
    )

    time_unit = sp.sqrt(length / gravity)
    chart = U**3
    prolonged_velocity = sp.diff(chart, U) * Y

    source_clock = time_unit / Y
    target_clock = sp.simplify(
        time_unit * sp.diff(chart, U) / prolonged_velocity
    )
    assert sp.simplify(target_clock - source_clock) == 0

    # Scaling the pendulum length by k^2 transports the time frame by k.  The
    # dimensionless shape clock is unchanged.
    scaled_time_unit = sp.sqrt(ruler_scale**2 * length / gravity)
    assert sp.simplify(scaled_time_unit - ruler_scale * time_unit) == 0


def test_cartesian_sheet_is_exactly_one_task_visible_continuation_bit():
    # One carrier loop flips the Cartesian mark; two loops close it.  Residual
    # addition is C2.  The same visible carrier endpoint therefore has two
    # possible full-state continuations.
    residuals = (0, 1)
    future_loops = (0, 1)

    full_state_signatures = {
        residual: tuple(
            (residual + future) % 2 for future in future_loops
        )
        for residual in residuals
    }
    carrier_only_signatures = {
        residual: tuple(0 for _future in future_loops)
        for residual in residuals
    }

    assert len(set(full_state_signatures.values())) == 2
    assert _minimum_exact_bits(full_state_signatures) == 1
    assert len(set(carrier_only_signatures.values())) == 1
    assert _minimum_exact_bits(carrier_only_signatures) == 0

    mark = 0
    after_one_carrier_period = (mark + 1) % 2
    after_two_carrier_periods = (after_one_carrier_period + 1) % 2
    assert after_one_carrier_period != mark
    assert after_two_carrier_periods == mark

    # At the reached E=0 turning point U=-1,Y=0 the carrier state is fixed,
    # but the energy identity retains the two velocities +/-sqrt(2).  Their
    # immediate q_x continuations differ, witnessing the two signatures.
    E0, U_turn, Y_turn = 0, -1, 0
    vx_squared = 2 * (E0 - U_turn) - Y_turn**2
    assert vx_squared == 2
    assert sp.sqrt(vx_squared) != -sp.sqrt(vx_squared)


def test_bolza_is_a_declared_metric_completion_not_a_pendulum_chart():
    U, Y, metric_mark, W, E, metric_weight = sp.symbols("U Y Z_m W E c")

    physical_sheet = 2 * (E - U) * (1 - U**2)
    metric_sheet = metric_weight + U**2
    third_quotient = sp.expand(physical_sheet * metric_sheet)

    # The Bolza route adjoins an independent square root.  It is therefore a
    # biquadratic fiber-product construction, not X=h(U) on the same carrier.
    product_relation = W**2 - third_quotient
    pulled_back = product_relation.subs(W**2, Y**2 * metric_mark**2)
    pulled_back = pulled_back.subs(
        {Y**2: physical_sheet, metric_mark**2: metric_sheet},
        simultaneous=True,
    )
    assert sp.expand(pulled_back) == 0

    symmetric_leaf = sp.expand(third_quotient.subs({E: 0, metric_weight: 1}))
    assert symmetric_leaf == 2 * (U**5 - U)

    # The literal Bolza polynomial disappears as soon as the declared metric
    # weight changes.  Hence the special surface has explained provenance but
    # no metric-independent/canonical status in the pendulum family.
    bolza_scaled = 2 * (U**5 - U)
    deviation = sp.factor(third_quotient.subs(E, 0) - bolza_scaled)
    assert deviation == 2 * U * (metric_weight - 1) * (U - 1) * (U + 1)
