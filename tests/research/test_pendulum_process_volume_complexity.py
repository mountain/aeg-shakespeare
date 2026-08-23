"""Pendulum process volume and frontier-time calibration.

Question
--------
Can the simple pendulum provide a dimensionful continuous calibration for the
repository's discrete history-geometry distinction between bulk history volume,
frontier width, and process depth?

This essay deliberately separates three layers:

1. classical mechanics theorems about symplectic area, action, and period;
2. exact dimensionless identities for the pendulum;
3. a Process Geometry interpretation that remains local evidence, not a generic
   complexity law.

Primitive dimensional scales
----------------------------
For mass ``M``, length ``ell`` and gravity ``g``, use the bottom-referenced
Hamiltonian

    H(theta,p) = p^2/(2 M ell^2) + M g ell (1-cos(theta)).

The pendulum itself supplies

    E0 = M g ell,
    t0 = sqrt(ell/g),
    A0 = E0 t0 = M ell sqrt(g ell).

Thus phase-space area/action has the natural dimension ``energy*time`` without
introducing a quantum cell.

Classical calibration
---------------------
For libration write

    epsilon = H/E0,       0 <= epsilon < 2,
    m = epsilon/2.

The closed orbit bounds the action area

    Omega(epsilon)
      = 16 A0 [E(m) - (1-m) K(m)],

where ``K`` and ``E`` are complete elliptic integrals in parameter convention.
The physical period is

    T(epsilon) = 4 t0 K(m).

The exact identity

    d Omega / d H = T

is the one-degree-of-freedom action-period relation.  In dimensionless form,
with ``V=Omega/A0``, it is

    dV/depsilon = T/t0.

At the libration separatrix ``epsilon -> 2-``, ``V -> 16`` while ``T`` diverges.
This gives a clean example in which a finite bulk phase volume coexists with an
unbounded shell/clock measure.

Process Geometry interpretation
--------------------------------
The repository's finite history geometry has

    V_N = sum_{n<=N} W(n),
    Delta V_N = W(N).

The pendulum exhibits the continuous structural analogue

    Omega(E) = integral^E T(E') dE',
    dOmega/dE = T(E).

This motivates, but does not prove, a broader volume/frontier/coarea relation.
No statement in this file identifies physical energy with computational
complexity, phase volume with machine memory, or log-volume with thermodynamic
entropy.

Theory-map effect
-----------------
None.  This is a local calibration supplying evidence for a separately governed
H3<->H4 theory-edge hypothesis.  It creates no generic complexity or spacetime
API.
"""

import sympy as sp


def test_pendulum_natural_scales_have_action_factorization():
    M, ell, g = sp.symbols("M ell g", positive=True)

    E0 = M * g * ell
    t0 = sp.sqrt(ell / g)
    A0 = M * ell * sp.sqrt(g * ell)

    assert sp.simplify(E0 * t0 - A0) == 0


def test_dimensionless_action_derivative_is_the_dimensionless_period():
    # SymPy differentiates elliptic_k/elliptic_e in the parameter convention m.
    epsilon = sp.symbols("epsilon", positive=True)
    m = epsilon / 2

    K = sp.elliptic_k(m)
    E = sp.elliptic_e(m)
    volume = 16 * (E - (1 - m) * K)
    dimensionless_period = 4 * K

    assert sp.simplify(sp.diff(volume, epsilon) - dimensionless_period) == 0


def test_small_amplitude_process_volume_has_harmonic_limit():
    epsilon = sp.symbols("epsilon", positive=True)
    m = epsilon / 2

    volume = 16 * (sp.elliptic_e(m) - (1 - m) * sp.elliptic_k(m))
    dimensionless_period = 4 * sp.elliptic_k(m)

    # Leading terms: V ~ 2*pi*epsilon and T/t0 ~ 2*pi.
    assert sp.simplify(sp.limit(volume / epsilon, epsilon, 0, dir="+")) == 2 * sp.pi
    assert sp.simplify(sp.limit(dimensionless_period, epsilon, 0, dir="+")) == 2 * sp.pi


def test_separatrix_has_finite_bulk_volume_and_divergent_clock():
    # Use the separatrix trajectory directly instead of relying on a CAS limit
    # of elliptic_k at its singular endpoint.
    theta = sp.symbols("theta", real=True)

    # At epsilon=2, the positive dimensionless momentum branch on
    # -pi < theta < pi is p/A0 = 2*cos(theta/2).  The enclosed phase area is
    # twice the positive-branch integral.
    separatrix_volume = sp.integrate(
        4 * sp.cos(theta / 2),
        (theta, -sp.pi, sp.pi),
    )
    assert sp.simplify(separatrix_volume - 16) == 0

    # Dimensionless travel time on the positive branch is
    # dtheta/(2*cos(theta/2)); an antiderivative is
    # log(sec(theta/2)+tan(theta/2)), which diverges at theta -> pi-.
    clock_primitive = sp.log(sp.sec(theta / 2) + sp.tan(theta / 2))
    assert sp.limit(clock_primitive, theta, sp.pi, dir="-") == sp.oo


def test_local_action_form_energy_derivative_is_the_process_clock_form():
    # On the observable cubic Y^2=2(E-U)(1-U^2), the physical action form is
    # lambda = Y/(1-U^2) dU.  Differentiating its coefficient along the curve
    # with respect to E gives 1/Y, the coefficient of omega=dU/Y.
    U, E = sp.symbols("U E")
    Y = sp.sqrt(2 * (E - U) * (1 - U**2))

    action_coefficient = Y / (1 - U**2)
    clock_coefficient = 1 / Y

    assert sp.simplify(sp.diff(action_coefficient, E) - clock_coefficient) == 0
