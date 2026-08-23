"""Riccati canonicalization: many lifts -> induced horizontal path -> lower jet complexity.

Question
--------
A physical trajectory can be represented in many moving affine frames.  Can a
strictly local canonicalization choose one frame without looking into the future,
derive its motion by differentiating the normalization conditions, and make the
observed dynamics objectively simpler than fixed or arbitrary lifts?

Primitive data
--------------
Start from the time-dependent Riccati process

    dx/dt = a(t) + b(t) x + c(t) x^2

and the affine observer family

    x = q + s y,   s != 0.

At one instant the observer has arbitrary local rates ``q_dot`` and ``s_dot``.
The observed coefficients are therefore

    A0 = (a + b q + c q^2 - q_dot) / s,
    A1 = b + 2 c q - s_dot/s,
    A2 = c s.

No observer-rate law is supplied initially.

The canonicalization uses only the instantaneous Riccati coefficients and two
affine-frame parameters ``r,d``.  It requires ``r`` and ``r+d`` to be the two
ordered nondegenerate roots:

    Phi_0 = a + b r + c r^2 = 0,
    Phi_1 = a + b(r+d) + c(r+d)^2 = 0.

Classical lineage
-----------------
Normalization by a moving frame is classical in the theory of group actions;
Fels and Olver give an explicit moving-frame/coframe normalization algorithm and
differential-invariant framework [Fels-Olver-1998].  The Riccati equation is a
standard Lie-system example associated with ``SL(2,R)``
[Carinena-Marmo-Nasarre-1998].

The particular programme tested here -- local canonicalization first, then
observer motion obtained by differentiating the normalization, then comparison
of representation-jet complexity -- is a Shakespeare reconstruction.  Neither
reference is cited as asserting this experiment or its complexity criterion.

Shakespeare reconstruction
---------------------------
For arbitrary ``q_dot,s_dot``, the lifted equation reconstructs exactly the same
base Riccati vector field.  Hence one physical process admits many representation
paths.

On the root-normalized leaf, the *instantaneous physical* Riccati polynomial in
``y=(x-r)/d`` is

    kappa y(y-1),    kappa = c d.

Thus the three unconstrained physical coefficients ``(a,b,c)`` reduce to one
shape modulus before connection terms are added.  The moving observer itself is
not chosen by an optimizer or future trajectory.  ``ConstraintCanonicalization``
differentiates ``Phi=0`` along the declared local coefficient rates and uniquely
solves for ``r_dot,d_dot``.

The dynamic calibration is deliberately nonautonomous in the fixed frame:

    dx/dt = (x-t)(x-t-1)
          = t(t+1) - (2t+1)x + x^2.

The local root canonicalization should induce

    r_dot = 1,   d_dot = 0,

so the canonical lift ``y=x-t`` obeys

    dy/dt = y^2 - y - 1.

This is autonomous.  As a bounded objective comparison, define first-order
coefficient-jet complexity as the number of observed polynomial coefficients
whose exact time derivative is nonzero.  The fixed frame and a generic translated
frame each have complexity two in this calibration; the induced canonical lift
has complexity zero.

Calibration statement
---------------------
Passing this file certifies that:

1. arbitrary affine observer rates give distinct lifted coefficient triples but
   reconstruct the same physical Riccati process exactly;
2. root normalization reduces the instantaneous physical normal form to the
   one-modulus family ``kappa y(y-1)``;
3. arbitrary observer rates generally fail to preserve the root constraints;
4. differentiating the local root constraints uniquely induces the observer
   rates, with no future trajectory or propagator input;
5. for ``dx/dt=(x-t)(x-t-1)``, the induced rates are exactly ``r_dot=1`` and
   ``d_dot=0`` on the canonical leaf;
6. the corresponding horizontal lift is exactly ``dy/dt=y^2-y-1``; and
7. the exact first-order coefficient-jet complexity is ``2`` in the fixed frame,
   ``2`` for a noncanonical moving frame, and ``0`` on the canonical lift.

Proof map
---------
1. ``test_many_affine_lifts_project_to_the_same_base_process`` proves the exact
   reconstruction identity for arbitrary affine observer rates and exhibits
   rate-dependent lifted coefficients.
2. ``test_root_normalization_collapses_the_instantaneous_shape_to_one_modulus``
   imposes only the two root constraints and checks the resulting one-parameter
   physical normal form.
3. ``test_local_canonicalization_derives_the_horizontal_ode_and_removes_time_dependence``
   checks failure of a frozen noncanonical observer, derives the unique local
   observer rates, verifies the explicit horizontal path, and compares exact
   coefficient-jet complexity across fixed, arbitrary, and canonical frames.

Boundary
--------
This is a local nondegenerate two-root calibration, not a global Riccati normal
form across discriminant-zero strata.  The complexity reduction is an exact
result for the declared nonautonomous coefficient path, not a theorem that every
canonicalization makes every ODE autonomous or globally minimizes a universal
cost.

The affine observer family is deliberately restricted.  The surviving quadratic
direction and the classical ``sl(2)`` completion are covered by the earlier
Restricted Riccati essay.  This file isolates the logically prior question:
whether local canonicalization itself can select a distinguished lift and reduce
representation variation before completion is considered.

References
----------
[Fels-Olver-1998] Mark Fels, Peter J. Olver, "Moving Coframes: I. A Practical
Algorithm," *Acta Applicandae Mathematicae* 51(2) (1998), 161--213;
DOI 10.1023/A:1005878210297.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre,
"The nonlinear superposition principle and the Wei-Norman method,"
arXiv:physics/9802041 (1998), especially the Riccati / ``SL(2,R)`` discussion,
https://arxiv.org/abs/physics/9802041 .
"""

from __future__ import annotations

import sympy as sp

from aeg_shakespeare.presentation.canonicalization import ConstraintCanonicalization


def affine_observed_coefficients(a, b, c, q, s, q_dot, s_dot):
    """Coefficients of y_dot under x=q+s*y for one local observer lift."""

    return (
        sp.simplify((a + b * q + c * q**2 - q_dot) / s),
        sp.simplify(b + 2 * c * q - s_dot / s),
        sp.simplify(c * s),
    )


def coefficient_jet_complexity(coefficients, t) -> int:
    """Count coefficients with a nonzero exact first time derivative."""

    return sum(
        sp.simplify(sp.diff(coefficient, t)) != 0
        for coefficient in coefficients
    )


def test_many_affine_lifts_project_to_the_same_base_process():
    a, b, c = sp.symbols("a b c")
    q, s = sp.symbols("q s", nonzero=True)
    q_dot, s_dot = sp.symbols("q_dot s_dot")
    y = sp.Symbol("y")

    coefficients = affine_observed_coefficients(
        a, b, c, q, s, q_dot, s_dot
    )
    y_dot = sp.expand(sum(value * y**degree for degree, value in enumerate(coefficients)))

    reconstructed_x_dot = sp.expand(q_dot + s_dot * y + s * y_dot)
    physical_x_dot = sp.expand(a + b * (q + s * y) + c * (q + s * y) ** 2)
    assert sp.simplify(reconstructed_x_dot - physical_x_dot) == 0

    u, v = sp.symbols("u v")
    alternate = affine_observed_coefficients(a, b, c, q, s, u, v)
    assert sp.simplify(coefficients[0] - alternate[0] + (q_dot - u) / s) == 0
    assert sp.simplify(coefficients[1] - alternate[1] + (s_dot - v) / s) == 0
    assert coefficients[2] == alternate[2]


def test_root_normalization_collapses_the_instantaneous_shape_to_one_modulus():
    a, b, c = sp.symbols("a b c")
    r, d = sp.symbols("r d", nonzero=True)

    canonical_leaf = {
        a: c * r * (r + d),
        b: -c * (2 * r + d),
    }
    coefficients = tuple(
        sp.simplify(value.subs(canonical_leaf))
        for value in affine_observed_coefficients(
            a, b, c, r, d, sp.S.Zero, sp.S.Zero
        )
    )
    kappa = sp.expand(c * d)
    assert coefficients == (sp.S.Zero, -kappa, kappa)


def test_local_canonicalization_derives_the_horizontal_ode_and_removes_time_dependence():
    t = sp.Symbol("t", real=True)
    a, b, c = sp.symbols("a b c")
    r, d = sp.symbols("r d", nonzero=True)

    canonicalization = ConstraintCanonicalization(
        observer_parameters=(r, d),
        constraints=(
            a + b * r + c * r**2,
            a + b * (r + d) + c * (r + d) ** 2,
        ),
        label="ordered Riccati roots",
    )

    a_path = t * (t + 1)
    b_path = -(2 * t + 1)
    c_path = sp.S.One
    base_rates = {
        a: sp.diff(a_path, t),
        b: sp.diff(b_path, t),
        c: sp.diff(c_path, t),
    }
    path_subs = {a: a_path, b: b_path, c: c_path, r: t, d: sp.S.One}

    # Merely placing the observer at the instantaneous roots but freezing its
    # rate does not preserve canonicalization as the coefficients evolve.
    frozen_residuals = tuple(
        sp.simplify(value.subs(path_subs))
        for value in canonicalization.differentiated_constraints(
            base_rates,
            {r: sp.S.Zero, d: sp.S.Zero},
        )
    )
    assert frozen_residuals == (sp.S.One, -sp.S.One)

    connection = canonicalization.induced_connection(base_rates)
    assert connection.certified
    r_dot = sp.simplify(connection.rate(r).subs(path_subs))
    d_dot = sp.simplify(connection.rate(d).subs(path_subs))
    assert r_dot == 1
    assert d_dot == 0

    # Initial data r(0)=0,d(0)=1 plus the induced local ODE gives r=t,d=1.
    assert sp.diff(t, t) == r_dot
    assert sp.diff(sp.S.One, t) == d_dot

    fixed = affine_observed_coefficients(
        a_path, b_path, c_path,
        sp.S.Zero, sp.S.One,
        sp.S.Zero, sp.S.Zero,
    )
    arbitrary = affine_observed_coefficients(
        a_path, b_path, c_path,
        2 * t, sp.S.One,
        sp.S(2), sp.S.Zero,
    )
    canonical = affine_observed_coefficients(
        a_path, b_path, c_path,
        t, sp.S.One,
        r_dot, d_dot,
    )

    assert tuple(map(sp.expand, canonical)) == (-1, -1, 1)
    y = sp.Symbol("y")
    canonical_y_dot = sp.expand(
        sum(value * y**degree for degree, value in enumerate(canonical))
    )
    assert canonical_y_dot == y**2 - y - 1

    assert coefficient_jet_complexity(fixed, t) == 2
    assert coefficient_jet_complexity(arbitrary, t) == 2
    assert coefficient_jet_complexity(canonical, t) == 0
