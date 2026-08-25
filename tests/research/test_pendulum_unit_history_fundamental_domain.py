"""Pendulum P13: unit-framed history cover and fundamental-domain audit.

Retrieval
---------
Problem: where do universal history, unit one, time/space complexity,
dimensional analysis, fundamental domains, elliptic curves, elliptic functions,
and the Bolza red team sit in one pendulum interpretation?
Domains: constrained mechanics, covering spaces, dimensional analysis,
action--period coarea, elliptic uniformization, finite continuation memory.
Process Geometry roles: lift-first history, transported unit frame, clock and
transverse resource lines, task quotient, deck residual, process volume,
period fundamental domain, quotient carrier, periodic decoder.
Stable family entry: ``docs/vignettes/simple-pendulum.md``.

Question
--------
The previous pendulum essays established the observable cubic, its marked
clock, its period lattice, the physical ``Z2`` cover, and presentation
covariance.  Read from the quotient downward, however, elliptic curves and
special functions can still look like the protagonists.  This essay reverses
the order:

    primitive constrained process
      -> lifted history with local units
      -> accumulated clock and transverse resource
      -> task-dependent deck quotient / fundamental domain
      -> marked elliptic carrier
      -> periodic elliptic-function readout.

It asks what this order computes exactly for the simple pendulum, and where the
interpretation must stop.

Primitive data
--------------
The canonical start uses only Cartesian process data, not a supplied angle or
trigonometric solution:

    q=(q_x,q_y),  v=Dq,
    <q,q>=1,  <q,v>=0,
    E=|v|^2/2+q_y.

Choose the discovered scalar observable and its first history jet

    U=q_y,  Y=DU=v_y.

Eliminating the constrained Cartesian coordinates gives

    C_E: Y^2=2(E-U)(1-U^2),
    DU=Y,  DY=3U^2-2EU-1,
    omega=dU/Y.

The physical scales are

    E0=m g ell,
    t0=sqrt(ell/g),
    A0=E0 t0=m ell sqrt(g ell),

so ``dt=t0 omega`` and the natural process-volume cell has action dimension.
The carrier convention and the bottom-referenced energy convention are related
by ``epsilon=E+1``.

First-principles reconstruction
-------------------------------
This file keeps four distinctions explicit.

1. **Universal history versus quotient carrier.**  On the certified ``E=0``
   marked carrier the Abel developing coordinate is

       z(P)=integral omega,

   and its analytic universal cover is ``C_z``.  The visible complex carrier is
   ``C_z/Lambda`` with

       Lambda=omega_A Z + i omega_A Z.

   This downstream analytic cover is an exact model of lifted clock history;
   the essay does not claim that a canonical A/M history lift has thereby been
   discovered upstream.

2. **Unit versus fundamental domain.**  ``Lambda`` determines which lifted
   histories are identified.  ``t0`` only supplies their physical ruler:

       Lambda_phys=t0 Lambda.

   Choosing a unit does not create a period lattice, and choosing a lattice
   basis does not choose a scalar history cost.

3. **Task-dependent domains.**  On the real ``E=0`` flow, one interval of
   length ``omega_A`` closes ``(U,Y)`` but flips the Cartesian sheet.  The full
   physical state closes only after ``2 omega_A``.  Thus the carrier and
   full-state tasks have different real fundamental domains even though they
   use the same local clock.

4. **Continuous and discrete space/time statements.**  For bottom-referenced
   libration energy ``epsilon`` and ``m=epsilon/2``, the full physical action
   and period are

       Omega/A0 = 16 [E(m)-(1-m)K(m)],
       T/t0     = 4 K(m),

   with ``dOmega/dH=T``.  A thin phase-volume shell is therefore one full
   history fundamental-domain length times a transverse energy thickness.
   Separately, task-visible deck signatures give finite exact memory bounds.
   Neither statement identifies physical energy with machine space.

Translation table
-----------------
``primitive q,v history``
    physical process before an observer quotient.
``(U,Y)``
    selected observable and first history jet.
``(C_E,omega)``
    task-visible quotient carrier marked by its process clock.
``z=integral omega``
    additive lifted clock/developing coordinate.
``Lambda``
    kernel of the periodic readout; it cuts a fundamental domain.
``elliptic curve``
    the complex completed quotient geometry ``C_z/Lambda``.
``elliptic function``
    a periodic decoder from lifted clock to a visible coordinate; at ``E=0``,
    ``U(z)=-sn^2(z/sqrt(2),i)``.
``Cartesian mark``
    the one-bit residual erased by the carrier-only quotient.
``A0``
    a natural pendulum action scale, not a universal quantum/information cell.
``Bolza quotient``
    the product-sign quotient after adjoining a separate declared metric
    square root, not another presentation of ``C_E``.

Classical lineage
-----------------
The action--period derivative, Abel uniformization, period lattices, and
elliptic-function inversion are classical.  The project-specific content is
their placement in a lift--measure--stop--quotient information contract and
the task-relative continuation census.  See [Arnold-1989], [DLMF-19], and
[DLMF-22].

Calibration statement
---------------------
Passing this file certifies:

1. the Cartesian constraints force the marked observable cubic before any
   angle, named elliptic function, or A/M chart is supplied;
2. ``E0``, ``t0``, and ``A0`` transport energy, history-domain length, and
   action coherently, while dimensionless domain length is unchanged;
3. moving scale frames require the covariant action--period identity rather
   than the raw derivative along a varying family;
4. the exact elliptic-integral action formula is the integral of full physical
   history fundamental-domain lengths across energy, and the reduced carrier
   domain is half the full-state domain on the certified leaf;
5. quotienting the finite parity slice of a square lifted period cell can
   forget two, one, or zero deck bits according to the continuation task;
6. a universal cover and lattice do not choose a scalar cost: a unimodular
   basis shear changes naive word length;
7. the physical and declared metric ``Z2`` sheets give ``2/1/0`` residual bits
   when a task sees both signs, only their product, or neither; the product
   quotient specializes to the Bolza polynomial at ``E=0,c=1``.

Proof map
---------
``test_cartesian_process_forces_the_marked_carrier`` proves item 1.
``test_unit_frames_scale_domains_without_changing_dimensionless_shape`` proves
item 2.  ``test_moving_units_require_the_covariant_action_period_identity``
proves item 3.  ``test_action_coarea_sweeps_full_history_fundamental_domains``
proves item 4.  ``test_task_quotients_choose_which_period_residuals_survive``
proves item 5.  ``test_lattice_basis_does_not_choose_a_scalar_history_ruler``
proves item 6.  ``test_bolza_product_quotient_retains_one_of_two_sheet_bits``
proves item 7.

Effective-analysis audit
------------------------
Mode: exact symbolic algebra and finite exact continuation signatures.
Evaluator: SymPy plus direct finite enumeration.  No floating-point period or
trajectory claim is introduced.  Units: ``E0`` is energy, ``t0`` is time,
``A0`` is action; normalized carrier/history expressions are dimensionless.
Cost: the bit counts are exact finite state lower bounds.  No generic runtime,
entropy, or continuous-Huffman claim is made.

Boundary
--------
This essay does not claim:

- that the topological/analytic universal cover alone is a canonical flat
  history ruler;
- that the Abel cover has been discovered intrinsically from raw A/M history;
- that ``T*S`` is a universal scalar complexity; the exact continuous result
  here is the action--period coarea identity, and finite memory is separate;
- that ``A0`` is a universal action quantum or that ``log(Omega/A0)`` is an
  entropy;
- that an angle or Jacobi formula is the canonical starting presentation;
- that the Bolza quotient is the pendulum state space, an A/M chart, or a
  metric-independent completion;
- a Theory Map or Public/Experimental API promotion.

References and onward links
---------------------------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
"Elliptic Integrals", https://dlmf.nist.gov/19 .

[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
"Jacobian Elliptic Functions", https://dlmf.nist.gov/22 .

Repository links: ``docs/53-process-volume-frontier-coarea-hypothesis.md``;
``docs/56-am-universal-history-recalibration.md``;
``docs/62-task-covariant-complexity-coarea.md``;
``tests/research/test_pendulum_lifted_clock_global_quotient.py``;
``tests/research/test_pendulum_am_marked_carrier_bridge.py``.
"""

from __future__ import annotations

import sympy as sp


def _minimum_exact_bits(signatures):
    """Return the binary state lower bound for finite task signatures."""

    return (len(set(signatures.values())) - 1).bit_length()


def test_cartesian_process_forces_the_marked_carrier():
    U, Y, E = sp.symbols("U Y E")

    # q_x^2=1-U^2 and q_x v_x=-UY imply the speed without choosing an angle.
    speed_squared = U**2 * Y**2 / (1 - U**2) + Y**2
    assert sp.simplify(speed_squared - Y**2 / (1 - U**2)) == 0

    # E=|v|^2/2+U then forces the observable cubic.
    energy_residual = E - U - speed_squared / 2
    carrier_from_energy = sp.factor(2 * (1 - U**2) * energy_residual)
    carrier_polynomial = 2 * (E - U) * (1 - U**2)
    assert sp.expand(carrier_from_energy - (carrier_polynomial - Y**2)) == 0

    # Differentiating Y^2=P_E(U) along DU=Y gives the closed reduced flow.
    acceleration = sp.diff(carrier_polynomial, U) / 2
    assert sp.expand(acceleration - (3 * U**2 - 2 * E * U - 1)) == 0


def test_unit_frames_scale_domains_without_changing_dimensionless_shape():
    mass, ell, gravity, scale = sp.symbols("m ell g k", positive=True)
    domain_shape = sp.symbols("P", positive=True)

    energy_unit = mass * gravity * ell
    time_unit = sp.sqrt(ell / gravity)
    action_unit = energy_unit * time_unit

    assert sp.simplify(
        action_unit - mass * ell * sp.sqrt(gravity * ell)
    ) == 0

    physical_domain = time_unit * domain_shape
    scaled_domain = physical_domain.subs(ell, scale**2 * ell)
    assert sp.simplify(scaled_domain - scale * physical_domain) == 0
    assert sp.simplify(scaled_domain / (scale * time_unit) - domain_shape) == 0

    scaled_energy_unit = energy_unit.subs(ell, scale**2 * ell)
    scaled_action_unit = action_unit.subs(ell, scale**2 * ell)
    assert sp.simplify(scaled_energy_unit - scale**2 * energy_unit) == 0
    assert sp.simplify(scaled_action_unit - scale**3 * action_unit) == 0


def test_moving_units_require_the_covariant_action_period_identity():
    s = sp.symbols("s", positive=True)
    epsilon = sp.Function("epsilon")(s)
    energy_unit = sp.Function("E0")(s)
    time_unit = sp.Function("t0")(s)
    shape_function = sp.Function("V")

    energy = energy_unit * epsilon
    action = energy_unit * time_unit * shape_function(epsilon)
    period = time_unit * sp.diff(shape_function(epsilon), epsilon)

    alpha_energy = sp.diff(sp.log(energy_unit), s)
    alpha_time = sp.diff(sp.log(time_unit), s)
    covariant_energy = sp.diff(energy, s) - energy * alpha_energy
    covariant_action = (
        sp.diff(action, s)
        - action * (alpha_energy + alpha_time)
    )

    assert sp.simplify(covariant_action - period * covariant_energy) == 0


def test_action_coarea_sweeps_full_history_fundamental_domains():
    epsilon = sp.symbols("epsilon", positive=True)
    parameter = epsilon / 2

    normalized_action = 16 * (
        sp.elliptic_e(parameter)
        - (1 - parameter) * sp.elliptic_k(parameter)
    )
    full_domain_length = 4 * sp.elliptic_k(parameter)

    assert sp.simplify(
        sp.diff(normalized_action, epsilon) - full_domain_length
    ) == 0

    # In the carrier convention E=0 means epsilon=1.  The observable carrier
    # closes after half the full Cartesian period on this certified leaf.
    lemniscatic_full_domain = full_domain_length.subs(epsilon, 1)
    lemniscatic_carrier_domain = 2 * sp.elliptic_k(sp.Rational(1, 2))
    assert sp.simplify(
        lemniscatic_full_domain - 2 * lemniscatic_carrier_domain
    ) == 0


def test_task_quotients_choose_which_period_residuals_survive():
    residuals = tuple(
        (real, imaginary)
        for real in range(2)
        for imaginary in range(2)
    )
    future_deck_steps = residuals

    # All four lifted points project to the same exact point in the chosen
    # half-open unit cell; only their deck coordinates differ.
    base_cell_point = (sp.Rational(1, 3), sp.Rational(2, 5))
    lifted_points = {
        residual: (
            base_cell_point[0] + residual[0],
            base_cell_point[1] + residual[1],
        )
        for residual in residuals
    }
    projected_points = {
        residual: tuple(value - sp.floor(value) for value in point)
        for residual, point in lifted_points.items()
    }
    assert set(projected_points.values()) == {base_cell_point}

    full_deck_signatures = {
        residual: tuple(
            (
                (residual[0] + future[0]) % 2,
                (residual[1] + future[1]) % 2,
            )
            for future in future_deck_steps
        )
        for residual in residuals
    }
    physical_sheet_signatures = {
        residual: tuple(
            (residual[0] + future[0]) % 2
            for future in future_deck_steps
        )
        for residual in residuals
    }
    carrier_only_signatures = {
        residual: tuple(0 for _future in future_deck_steps)
        for residual in residuals
    }

    assert _minimum_exact_bits(full_deck_signatures) == 2
    assert _minimum_exact_bits(physical_sheet_signatures) == 1
    assert _minimum_exact_bits(carrier_only_signatures) == 0


def test_lattice_basis_does_not_choose_a_scalar_history_ruler():
    standard_basis = sp.eye(2)
    sheared_basis = sp.Matrix([[1, 1], [0, 1]])
    assert sheared_basis.det() == 1

    lattice_displacement = sp.Matrix([0, 1])
    standard_coefficients = standard_basis.inv() * lattice_displacement
    sheared_coefficients = sheared_basis.inv() * lattice_displacement

    assert tuple(standard_coefficients) == (0, 1)
    assert tuple(sheared_coefficients) == (-1, 1)
    assert sum(abs(value) for value in standard_coefficients) == 1
    assert sum(abs(value) for value in sheared_coefficients) == 2


def test_bolza_product_quotient_retains_one_of_two_sheet_bits():
    sheet_states = tuple(
        (physical, metric)
        for physical in range(2)
        for metric in range(2)
    )
    future_sheet_steps = sheet_states

    both_sheet_signatures = {
        state: tuple(
            (
                (state[0] + future[0]) % 2,
                (state[1] + future[1]) % 2,
            )
            for future in future_sheet_steps
        )
        for state in sheet_states
    }
    product_signatures = {
        state: tuple(
            (state[0] + state[1] + future[0] + future[1]) % 2
            for future in future_sheet_steps
        )
        for state in sheet_states
    }
    no_sheet_signatures = {
        state: tuple(0 for _future in future_sheet_steps)
        for state in sheet_states
    }

    assert _minimum_exact_bits(both_sheet_signatures) == 2
    assert _minimum_exact_bits(product_signatures) == 1
    assert _minimum_exact_bits(no_sheet_signatures) == 0

    U, E, metric_weight = sp.symbols("U E c")
    physical_sheet = 2 * (E - U) * (1 - U**2)
    metric_sheet = metric_weight + U**2
    product_quotient = sp.expand(physical_sheet * metric_sheet)

    bolza_leaf = product_quotient.subs({E: 0, metric_weight: 1})
    assert sp.expand(bolza_leaf - 2 * (U**5 - U)) == 0
