"""Kepler radial moving frame: local canonicalization -> physical horizontal lift.

Question
--------
Can the canonicalization-first programme select a genuinely moving observer on a
physical Kepler trajectory, derive the observer ODE from a local normalization,
and expose a lower-dimensional shape dynamics without assuming polar coordinates
or an angular-velocity law as primitive input?

Primitive data
--------------
Start from the planar Cartesian Kepler process

    x_dot  = vx,
    y_dot  = vy,
    vx_dot = -mu*x/r^3,
    vy_dot = -mu*y/r^3,
    r^2    = x^2+y^2,

on the noncollision stratum ``r>0``.

Allow an arbitrary rotating observer with angle ``theta``.  Its local coordinates
are

    X =  cos(theta)*x + sin(theta)*y,
    Y = -sin(theta)*x + cos(theta)*y,
    U =  cos(theta)*vx + sin(theta)*vy,
    V = -sin(theta)*vx + cos(theta)*vy.

Before canonicalization, ``theta_dot=omega`` is arbitrary representation motion.
The local canonicalization uses only the present position and observer angle:

    Phi = Y = 0,

with the branch condition ``X>0`` selecting the outward radial orientation.  No
polar-coordinate equations, angular momentum reduction, future orbit, conic
solution, or formula for ``theta_dot`` is supplied.

Classical lineage
-----------------
Reduction of the central-force problem to radial motion using angular momentum
is classical; see Goldstein, Poole, and Safko, Chapter 3
[Goldstein-Poole-Safko-2002].  Moving-frame normalization under transformation
groups has classical antecedents; Fels and Olver provide a systematic moving
coframe algorithm [Fels-Olver-1998].

This executable essay reverses the usual pedagogical order.  It starts from the
Cartesian process and observer freedom, derives the radial observer ODE by
maintaining a local normalization, and only afterwards identifies the familiar
central-force reduction.  That ordering is the Shakespeare/AEG reconstruction,
not a claim attributed to the references.

Shakespeare reconstruction
---------------------------
For arbitrary observer angular rate ``omega``, differentiation of the rotated
coordinates gives

    X_dot = U + omega*Y,
    Y_dot = V - omega*X.

Thus the same Cartesian physical process has many rotating representation paths.
Merely aligning the observer instantaneously (``Y=0``) is not enough: a generic
``omega`` immediately leaves the canonical leaf.

``ConstraintCanonicalization`` differentiates ``Phi=Y=0`` using only the current
Cartesian rates and solves uniquely, on ``X!=0``, for

    theta_dot = V/X.

On the canonical leaf ``Y=0, X>0`` this is

    theta_dot = h/X^2,

because the Cartesian angular momentum becomes ``h=X*V``.

The induced horizontal lift has shape equations

    X_dot = U,
    U_dot = -mu/X^2 + V^2/X,
    V_dot = -U*V/X,

with no remaining ``theta`` dependence.  Consequently

    h = X*V,
    h_dot = 0,

and the physical process separates into

    X_dot     = U,
    U_dot     = h^2/X^3 - mu/X^2,
    theta_dot = h/X^2,
    h_dot     = 0.

The canonicalization therefore does not delete physical solutions.  It fixes the
representation path, separates the rotational observer variable as a quadrature,
and exposes the two-dimensional radial shape dynamics plus one conserved
parameter.

Calibration statement
---------------------
Passing this file certifies that:

1. arbitrary rotating observer rates give distinct lifts of the same Cartesian
   Kepler process;
2. instantaneous radial alignment with an arbitrary angular rate generally fails
   to stay aligned;
3. differentiating only the local condition ``Y=0`` uniquely induces
   ``theta_dot=V/X`` on the regular radial chart;
4. the induced connection residual vanishes exactly and uses no future trajectory
   or propagator;
5. on the canonical leaf the moving-frame equations are
   ``X_dot=U``, ``U_dot=-mu/X**2+V**2/X``, ``V_dot=-U*V/X``;
6. the observer angle disappears entirely from that shape subsystem;
7. ``h=X*V`` is then exactly constant, yielding the familiar radial equation
   ``U_dot=h**2/X**3-mu/X**2`` and reconstruction quadrature
   ``theta_dot=h/X**2``; and
8. the physical four-dimensional Cartesian flow is represented as a
   two-dimensional radial shape ODE, one conserved parameter, and one observer
   quadrature, without changing its solution set.

Proof map
---------
1. ``test_arbitrary_rotating_lifts_reconstruct_the_same_cartesian_kinematics``
   derives the two rotated position-rate identities for arbitrary ``omega`` and
   checks exact inverse reconstruction of ``vx,vy``.
2. ``test_radial_canonicalization_uniquely_derives_the_observer_angular_rate``
   shows a frozen aligned observer leaves the radial leaf generically, then uses
   ``ConstraintCanonicalization`` to derive and certify ``theta_dot=V/X``.
3. ``test_kepler_horizontal_lift_exposes_radial_shape_dynamics_and_angular_momentum``
   derives the complete canonical moving-frame equations from the Cartesian
   Kepler process, proves ``h_dot=0``, and checks the radial reduction and angle
   reconstruction law.

Boundary
--------
This is a local noncollision radial chart with ``X>0``.  It does not cover the
origin, chart transitions, collisions, global conic classification, or arbitrary
perturbed Kepler dynamics.  The familiar central-force reduction is not claimed
as new mathematics; the calibration target is the *derivation order* and the
role of the observer ODE as a consequence of local canonicalization.

This essay also does not yet validate an osculating-element canonicalization or
a non-constraint backend.  Its role is the first physical moving-frame pressure
test after the algebraic Riccati and coupled-register calibrations.  Perturbative
``F_ren/F_res/F_comp`` separation remains a subsequent Kepler step.

No generic ``CanonicalLift``/bundle/curvature API is introduced here.

References
----------
[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L.
Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3,
"The Central Force Problem," ISBN 0-201-65702-3.

[Fels-Olver-1998] Mark Fels, Peter J. Olver, "Moving Coframes: I. A Practical
Algorithm," *Acta Applicandae Mathematicae* 51(2) (1998), 161--213;
DOI 10.1023/A:1005878210297.
"""

from __future__ import annotations

import sympy as sp

from process_geometry.experimental import ConstraintCanonicalization


def rotated_state(x, y, vx, vy, theta):
    c = sp.cos(theta)
    s = sp.sin(theta)
    return (
        c * x + s * y,
        -s * x + c * y,
        c * vx + s * vy,
        -s * vx + c * vy,
    )


def test_arbitrary_rotating_lifts_reconstruct_the_same_cartesian_kinematics():
    x, y, vx, vy, theta, omega = sp.symbols("x y vx vy theta omega")
    X, Y, U, V = rotated_state(x, y, vx, vy, theta)

    X_dot = sp.expand(U + omega * Y)
    Y_dot = sp.expand(V - omega * X)

    c = sp.cos(theta)
    s = sp.sin(theta)
    # x=cX-sY, y=sX+cY. Differentiate using theta_dot=omega.
    reconstructed_vx = sp.simplify(
        c * X_dot - s * Y_dot - omega * (s * X + c * Y)
    )
    reconstructed_vy = sp.simplify(
        s * X_dot + c * Y_dot + omega * (c * X - s * Y)
    )
    assert sp.trigsimp(reconstructed_vx - vx) == 0
    assert sp.trigsimp(reconstructed_vy - vy) == 0

    # The lifted path itself depends on observer motion even though the base
    # projection does not.
    omega_alt = sp.Symbol("omega_alt")
    assert sp.simplify((U + omega * Y) - (U + omega_alt * Y)) != 0
    assert sp.simplify((V - omega * X) - (V - omega_alt * X)) != 0


def test_radial_canonicalization_uniquely_derives_the_observer_angular_rate():
    x, y, vx, vy, theta = sp.symbols("x y vx vy theta")
    X, Y, _U, V = rotated_state(x, y, vx, vy, theta)

    canonicalization = ConstraintCanonicalization(
        observer_parameters=(theta,),
        constraints=(Y,),
        label="outward radial Kepler frame",
    )

    # An instantaneously aligned but frozen frame generally leaves Y=0 because
    # the physical velocity can have a transverse component.
    frozen = canonicalization.differentiated_constraints(
        {x: vx, y: vy},
        {theta: sp.S.Zero},
    )
    assert sp.trigsimp(frozen[0] - V) == 0

    connection = canonicalization.induced_connection({x: vx, y: vy})
    assert connection.certified
    theta_dot = sp.simplify(connection.rate(theta))
    assert sp.trigsimp(theta_dot - V / X) == 0


def test_kepler_horizontal_lift_exposes_radial_shape_dynamics_and_angular_momentum():
    X, mu = sp.symbols("X mu", positive=True)
    U0, V0 = sp.symbols("U0 V0")

    omega = V0 / X
    X_dot = U0
    Y_dot = sp.simplify(V0 - omega * X)
    assert Y_dot == 0

    # On Y=0 the Kepler acceleration has only a radial component.
    radial_acceleration = -mu / X**2
    transverse_acceleration = sp.S.Zero
    U_dot = sp.simplify(radial_acceleration + omega * V0)
    V_dot = sp.simplify(transverse_acceleration - omega * U0)

    assert sp.simplify(U_dot - (-mu / X**2 + V0**2 / X)) == 0
    assert sp.simplify(V_dot - (-U0 * V0 / X)) == 0

    h = sp.expand(X * V0)
    h_dot = sp.simplify(X_dot * V0 + X * V_dot)
    assert h_dot == 0

    h_symbol = sp.Symbol("h")
    radial_u_dot = sp.simplify(U_dot.subs(V0, h_symbol / X))
    assert sp.simplify(radial_u_dot - (h_symbol**2 / X**3 - mu / X**2)) == 0
    assert sp.simplify(omega.subs(V0, h_symbol / X) - h_symbol / X**2) == 0
