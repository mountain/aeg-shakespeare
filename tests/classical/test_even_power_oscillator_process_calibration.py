"""Even-power oscillators: a real history cover, task quotient, and clock law.

Problem
-------
For the one-degree-of-freedom Hamiltonian family

    H_m(x,p) = p^2/2 + x^m/m,       m = 2, 4, 6,

calibrate the algebraic energy carriers against the full Process Geometry
order.  The earlier genus vignette proves that their complex energy curves
have genera 0, 1, and 2.  This file asks a different question: what is the
real continuation task, which history information is forgotten, which cover
carries the clock, how are physical units restored, and where does the
decoder fail?

Retrieval header
----------------
Problem: harmonic, quartic, and sextic even-power oscillators.
Domains: Hamiltonian mechanics, real periodic orbits, algebraic curves.
Classical names / aliases: period integral, action integral, angle variable,
universal cover of a periodic orbit, turning point.
Structural themes: task quotient, deck kernel, analytic clock, branch bit,
unit frame, singular stratum.
Process Geometry roles: second end-to-end family spine after the pendulum;
separation of literal-history, topological-cover, and analytic-cover claims.
Computational modes: exact symbolic identities only.
Prerequisites: elementary Hamiltonian mechanics, the beta integral, and the
classical fact that a regular compact connected one-dimensional energy level
is a circle.
Related vignettes: ``test_even_power_oscillator_genus_hierarchy.py``,
``test_harmonic_oscillator_additive_module.py``, and
``test_harmonic_oscillator_coefficient_extension.py``.
Mathematical Core relation: refines the oscillator family without changing
the Core; it supplies a complete real harmonic continuation task.
Engineering Architecture relation: supplies exact evaluator, independent
harmonic baseline, units, decoder, failure stratum, and claim boundary; it
makes no runtime-economy claim.
Theory Map relation: unchanged.

Primitive process and declared tasks
------------------------------------
The dimensionless primitive process is

    D x = p,       D p = -x^(m-1).

On a regular positive-energy real leaf, the full-state continuation task asks
for every future ``(x,p)``.  For the harmonic member, the phase history
``tau in R`` maps to the carrier

    (X,Y) = (cos(tau), -sin(tau)).

The full-state task forgets only integer winding: ``tau`` and
``tau + 2*pi*k`` have the same future after the same time increment.  Thus
``R -> S^1`` is the topological universal cover of the regular real orbit,
with deck kernel ``2*pi*Z``.  The same ``tau`` is also an analytic clock for
this genus-zero carrier.  This equality is local to the declared harmonic
task; it is not an identification of either cover with the raw full history
unfolding of the continuous command space, which this vignette does not
construct.

For a finite exact history certificate, the harmonic flow is also sampled by
the declared quarter-period alphabet ``{R,L}``.  ``ProcessWord`` preserves the
literal words before interpretation, while the full-state continuation task
quotients their net quarter-turn modulo four.  This executes a raw history
unfolding for the declared discrete subtask; it does not claim that the entire
continuous command/path space has been intrinsically unfolded.

The position-only observable ``U=X`` is not continuation sufficient: phases
``tau`` and ``-tau`` have the same position and opposite velocity.  Away from
turning points a sign bit decodes

    Y = sigma * sqrt(1-U^2),        sigma in {-1,+1}.

The chart fails at ``U=+/-1`` where the square-root derivative is singular.

Clock, action, and units
------------------------
For positive energy ``E`` and even ``m``, let ``a=(mE)^(1/m)``.  Direct beta
substitution in the real quadratures gives

    T_m(E) = 2 sqrt(2) m^(1/m-1) E^(1/m-1/2) B(1/m,1/2),

    Omega_m(E) = 4 sqrt(2) m^(1/m-1) E^(1/m+1/2) B(1/m,3/2).

The beta recurrence proves ``d Omega_m / dE = T_m``.  It also shows that the
real period is energy-independent for ``m=2`` but diverges at the collapsed
zero-energy stratum for ``m=4,6``.  These real clock laws do not construct the
complex analytic uniformizations of the genus-one and genus-two carriers.

For the dimensional harmonic oscillator

    dx/dt = p/M,       dp/dt = -M omega^2 x,

the unit frame is

    tau=omega*t,  x=A*X,  p=M*omega*A*Y,

with energy unit ``M*omega^2*A^2``.  The inverse unit map gives physical
period ``2*pi/omega`` and action ``2*pi*E/omega``.

Executable claim and proof map
------------------------------
``test_even_power_action_derivative_is_the_real_period`` certifies the exact
beta recurrence and harmonic baseline.  ``test_harmonic_unit_frame_*``
certifies dynamics, energy, and the inverse physical unit map.
``test_harmonic_real_history_cover_*`` certifies the deck generator and the
full-state continuation equivalence.  ``test_position_only_*`` certifies
information loss, the branch decoder, and its turning-point boundary.
``test_quarter_period_words_*`` certifies the finite literal-history unfolding
and its exact continuation quotient.
``test_zero_energy_*`` certifies the declared singular stratum.

Boundary
--------
The topology ``regular compact connected one-manifold = S^1`` and the beta
integral are classical prerequisites, not discoveries of the test runner.
No intrinsic unfolding of the full continuous history space, automatic task
discovery, complex genus-one or genus-two uniformization, global position-only
decoder, certified numerical quadrature, or efficiency advantage is claimed.
The raw-history certificate is restricted to the declared quarter-period
alphabet.  In particular, the complex genus ladder and the real orbit cover
measure different structures.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.

[DLMF-5] NIST Digital Library of Mathematical Functions, Chapter 5,
``Gamma Function`` (beta-function identities), https://dlmf.nist.gov/5 .

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.
"""

from __future__ import annotations

import sympy as sp

from process_geometry.experimental import minimize_finite_task_process
from process_geometry.process.history import ProcessWord, interpret_history


def _beta_exact(left: sp.Rational, right: sp.Rational) -> sp.Expr:
    """Gamma-ratio form of the beta function, kept exact by SymPy."""

    return sp.gamma(left) * sp.gamma(right) / sp.gamma(left + right)


def _period(power: int, energy: sp.Expr) -> sp.Expr:
    exponent = sp.Rational(1, power)
    return (
        2
        * sp.sqrt(2)
        * sp.Integer(power) ** (exponent - 1)
        * energy ** (exponent - sp.Rational(1, 2))
        * _beta_exact(exponent, sp.Rational(1, 2))
    )


def _action(power: int, energy: sp.Expr) -> sp.Expr:
    exponent = sp.Rational(1, power)
    return (
        4
        * sp.sqrt(2)
        * sp.Integer(power) ** (exponent - 1)
        * energy ** (exponent + sp.Rational(1, 2))
        * _beta_exact(exponent, sp.Rational(3, 2))
    )


def test_even_power_action_derivative_is_the_real_period():
    energy = sp.symbols("E", positive=True)

    for power in (2, 4, 6):
        exponent = sp.Rational(1, power)
        beta_recurrence = _beta_exact(
            exponent, sp.Rational(3, 2)
        ) - _beta_exact(exponent, sp.Rational(1, 2)) / (2 * exponent + 1)

        assert sp.simplify(sp.expand_func(beta_recurrence)) == 0
        assert sp.simplify(
            sp.expand_func(
                sp.diff(_action(power, energy), energy) / _period(power, energy)
            )
        ) == 1

    assert sp.simplify(sp.expand_func(_period(2, energy)) - 2 * sp.pi) == 0
    assert sp.simplify(sp.expand_func(_action(2, energy)) - 2 * sp.pi * energy) == 0


def test_harmonic_unit_frame_round_trips_dynamics_energy_period_and_action():
    phase = sp.symbols("tau", real=True)
    mass, omega, amplitude = sp.symbols("M omega A", positive=True)
    X = sp.cos(phase)
    Y = -sp.sin(phase)
    x = amplitude * X
    p = mass * omega * amplitude * Y

    dx_dt = omega * sp.diff(x, phase)
    dp_dt = omega * sp.diff(p, phase)
    energy = p**2 / (2 * mass) + mass * omega**2 * x**2 / 2
    energy_unit = mass * omega**2 * amplitude**2

    assert sp.simplify(dx_dt - p / mass) == 0
    assert sp.simplify(dp_dt + mass * omega**2 * x) == 0
    assert sp.trigsimp(energy / energy_unit - sp.Rational(1, 2)) == 0
    assert sp.simplify(x / amplitude - X) == 0
    assert sp.simplify(p / (mass * omega * amplitude) - Y) == 0

    dimensionless_energy = sp.Rational(1, 2)
    physical_energy = energy_unit / 2
    action_unit = mass * omega * amplitude**2
    assert sp.simplify(
        _period(2, dimensionless_energy) / omega - 2 * sp.pi / omega
    ) == 0
    assert sp.simplify(
        action_unit * _action(2, dimensionless_energy)
        - 2 * sp.pi * physical_energy / omega
    ) == 0


def test_harmonic_real_history_cover_has_deck_kernel_and_task_quotient():
    phase, increment = sp.symbols("tau s", real=True)

    carrier = sp.Matrix([sp.cos(phase), -sp.sin(phase)])
    deck_shift = carrier.subs(phase, phase + 2 * sp.pi)
    future = sp.Matrix(
        [sp.cos(phase + increment), -sp.sin(phase + increment)]
    )
    shifted_future = future.subs(phase, phase + 2 * sp.pi)

    assert all(sp.trigsimp(item) == 0 for item in deck_shift - carrier)
    assert all(sp.trigsimp(item) == 0 for item in shifted_future - future)
    assert sp.trigsimp(carrier.dot(carrier) - 1) == 0
    assert sp.trigsimp(sp.diff(carrier[0], phase) - carrier[1]) == 0
    assert sp.trigsimp(sp.diff(carrier[1], phase) + carrier[0]) == 0


def test_quarter_period_words_unfold_history_before_the_exact_phase_quotient():
    def transition(phase: int, step: int) -> int:
        return (phase + step) % 4

    direct = ProcessWord((1,))
    detour = ProcessWord((1, 1, -1))

    assert direct != detour
    assert direct.depth == 1
    assert detour.depth == 3
    assert interpret_history(direct, 0, transition) == interpret_history(
        detour, 0, transition
    )

    for continuation in (
        ProcessWord(()),
        ProcessWord((1,)),
        ProcessWord((-1, -1)),
        ProcessWord((1, 1, 1)),
    ):
        assert interpret_history(
            direct.compose(continuation), 0, transition
        ) == interpret_history(detour.compose(continuation), 0, transition)

    carrier_states = ((1, 0), (0, -1), (-1, 0), (0, 1))
    quotient = minimize_finite_task_process(
        states=range(4),
        steps=(-1, 1),
        transition=transition,
        observe=lambda phase: carrier_states[phase],
    )
    assert quotient.class_count == 4
    assert quotient.class_of(interpret_history(direct, 0, transition)) == (
        quotient.class_of(interpret_history(detour, 0, transition))
    )


def test_position_only_observable_loses_velocity_and_has_a_branched_decoder():
    phase, increment = sp.symbols("tau s", real=True)
    U = sp.cos(phase)
    Y = -sp.sin(phase)

    assert sp.trigsimp(U.subs(phase, -phase) - U) == 0
    assert sp.trigsimp(Y.subs(phase, -phase) + Y) == 0
    future_difference = sp.expand_trig(
        sp.cos(phase + increment) - sp.cos(-phase + increment)
    )
    assert (
        sp.trigsimp(
            future_difference + 2 * sp.sin(phase) * sp.sin(increment)
        )
        == 0
    )

    observed = sp.Rational(3, 5)
    decoded_velocities = {
        sign * sp.sqrt(1 - observed**2)
        for sign in (sp.Integer(-1), sp.Integer(1))
    }
    assert decoded_velocities == {sp.Rational(-4, 5), sp.Rational(4, 5)}
    assert all(
        sp.simplify(value**2 + observed**2 - 1) == 0
        for value in decoded_velocities
    )

    u = sp.symbols("u", real=True)
    decoder_derivative = sp.diff(sp.sqrt(1 - u**2), u)
    assert sp.limit(decoder_derivative, u, 1, dir="-") is sp.S.NegativeInfinity
    assert sp.limit(decoder_derivative, u, -1, dir="+") is sp.S.Infinity


def test_zero_energy_is_a_declared_singular_stratum_for_anharmonic_real_clocks():
    energy = sp.symbols("E", positive=True)

    assert sp.limit(_period(2, energy), energy, 0, dir="+") == 2 * sp.pi
    assert sp.limit(_period(4, energy), energy, 0, dir="+") is sp.S.Infinity
    assert sp.limit(_period(6, energy), energy, 0, dir="+") is sp.S.Infinity
