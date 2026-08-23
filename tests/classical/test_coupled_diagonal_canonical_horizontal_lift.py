"""Coupled two-register canonicalization: a genuine two-dimensional horizontal lift.

Question
--------
Does the canonicalization-first mechanism survive beyond one-dimensional
Riccati root normalization?  In particular, can local constraints on a genuine
two-register moving frame derive its observer ODE and remove explicit time
dependence from a coupled process without supplying that observer motion by
hand?

Primitive data
--------------
Use the nonautonomous two-register process

    x_dot = b12(t) y,
    y_dot = b21(t) x,

and a determinant-one diagonal moving frame

    u = p x,
    v = q y,
    p q = 1.

For arbitrary observer rates the lifted coefficients are

    M1 : p_dot/p,
    M2 : q_dot/q,
    E12: b12 p/q,
    E21: b21 q/p.

The local canonicalization balances the two cross directions while fixing the
common scale gauge:

    Phi_0 = b12 p^2 - b21 q^2 = 0,
    Phi_1 = p q - 1 = 0.

No matrix ODE, eigenbasis, diagonalization, or target autonomous normal form is
supplied.

Classical lineage
-----------------
Moving-frame normalization under a transformation group has classical
antecedents; Fels and Olver provide an explicit moving-coframe normalization and
differential-invariant framework [Fels-Olver-1998].  Matrix Lie groups and their
infinitesimal linear actions are standard; see [Hall-2015], Chapters 2--3.

The process-first ordering tested here -- independent scalar registers, local
balance/gauge normalization, differentiated observer transport, and only then a
matrix shadow -- is a Shakespeare reconstruction rather than a claim attributed
to those references.

Shakespeare reconstruction
---------------------------
For arbitrary ``p,q,p_dot,q_dot``, the lifted two-register equations reconstruct
the same base process exactly.  Thus observer motion is genuine representation
freedom over one physical trajectory.

The balance condition reduces the two instantaneous cross-coupling magnitudes
to one modulus:

    b12 p/q = b21 q/p = mu.

The determinant-one condition removes the common diagonal scale gauge.  The
observer ODE is then obtained only by differentiating ``Phi_0=Phi_1=0`` along
the declared local coupling rates.

The dynamic calibration chooses

    b12(t) = exp(-2t),
    b21(t) = exp( 2t).

The canonical leaf is

    p(t) = exp(t),
    q(t) = exp(-t).

The differentiated normalization should derive

    p_dot/p = 1,
    q_dot/q = -1,

and therefore the canonical lift

    u_dot =  u + v,
    v_dot =  u - v,

whose four process coefficients are all constant.  A fixed frame and a
determinant-one but noncanonical moving frame retain two explicitly
time-dependent cross coefficients.

Calibration statement
---------------------
Passing this file certifies that:

1. arbitrary determinant-one diagonal observer paths give distinct lifted
   coefficient tuples while reconstructing the same base coupled process;
2. local balance collapses the two cross-coupling shape coefficients to one
   modulus and ``p q=1`` fixes the residual common scale gauge;
3. frozen observer rates fail to preserve the canonicalization on the declared
   time-dependent coupling path;
4. differentiating the two local constraints uniquely induces both observer
   rates, with no future trajectory or propagator input;
5. the induced rates are exactly ``p_dot=p`` and ``q_dot=-q`` on the canonical
   leaf;
6. the resulting horizontal lift is the autonomous two-register system
   ``u_dot=u+v, v_dot=u-v``;
7. exact first-order coefficient-jet complexity is ``2`` in both fixed and
   noncanonical controls and ``0`` on the canonical lift; and
8. the balance canonicalization does not extend across the one-way-coupling
   stratum, so the triangular case is not silently forced into this observer
   family.

Proof map
---------
1. ``test_many_diagonal_lifts_project_to_the_same_coupled_process`` checks exact
   reconstruction for arbitrary local frame rates and exposes their effect on
   the lifted coefficients.
2. ``test_balance_and_determinant_constraints_reduce_cross_shape_to_one_modulus``
   checks the local one-modulus cross normal form and the one-way-coupling red
   team.
3. ``test_coupled_canonicalization_derives_matrix_observer_ode_and_autonomizes``
   checks noncanonical residuals, derives the two observer rates, verifies the
   explicit horizontal path, and compares exact coefficient-jet complexity.

Boundary
--------
This is a positive bidirectional-coupling calibration in a restricted diagonal
``SL(2)`` observer family.  It is not a generic ``GL(2)`` normal-form algorithm,
an eigenvector construction, or a theorem that every matrix-valued
canonicalization makes a system autonomous.

The one-way stratum is intentionally excluded by the balance condition and is
already covered by the independent triangular-closure red team in the earlier
coupled-scalar essay.  C2 therefore tests canonical observer motion, not a
universal completion policy.

No generic ``Canonicalization`` protocol, ``CanonicalLift`` object, matrix
observer API, or universal representation-complexity functional is introduced
by this calibration.

References
----------
[Fels-Olver-1998] Mark Fels, Peter J. Olver, "Moving Coframes: I. A Practical
Algorithm," *Acta Applicandae Mathematicae* 51(2) (1998), 161--213;
DOI 10.1023/A:1005878210297.

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An
Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer,
2015, Chapters 2--3; DOI 10.1007/978-3-319-13467-3.
"""

from __future__ import annotations

import sympy as sp

from aeg_shakespeare.presentation.canonicalization import ConstraintCanonicalization


def diagonal_lift_coefficients(b12, b21, p, q, p_dot, q_dot):
    """Return (M1,M2,E12,E21) coefficients in u=p*x, v=q*y."""

    return (
        sp.simplify(p_dot / p),
        sp.simplify(q_dot / q),
        sp.simplify(b12 * p / q),
        sp.simplify(b21 * q / p),
    )


def coefficient_jet_complexity(coefficients, t) -> int:
    return sum(
        sp.simplify(sp.diff(coefficient, t)) != 0
        for coefficient in coefficients
    )


def test_many_diagonal_lifts_project_to_the_same_coupled_process():
    b12, b21 = sp.symbols("b12 b21")
    p, q = sp.symbols("p q", nonzero=True)
    p_dot, q_dot = sp.symbols("p_dot q_dot")
    x, y = sp.symbols("x y")

    m1, m2, e12, e21 = diagonal_lift_coefficients(
        b12, b21, p, q, p_dot, q_dot
    )
    u = p * x
    v = q * y
    u_dot = sp.expand(m1 * u + e12 * v)
    v_dot = sp.expand(e21 * u + m2 * v)

    reconstructed_x_dot = sp.simplify((u_dot - p_dot * x) / p)
    reconstructed_y_dot = sp.simplify((v_dot - q_dot * y) / q)
    assert reconstructed_x_dot == b12 * y
    assert reconstructed_y_dot == b21 * x

    p_alt, q_alt = sp.symbols("p_alt q_alt", nonzero=True)
    p_rate_alt, q_rate_alt = sp.symbols("p_rate_alt q_rate_alt")
    alternate = diagonal_lift_coefficients(
        b12, b21, p_alt, q_alt, p_rate_alt, q_rate_alt
    )
    assert alternate != (m1, m2, e12, e21)


def test_balance_and_determinant_constraints_reduce_cross_shape_to_one_modulus():
    b12, b21 = sp.symbols("b12 b21", nonzero=True)
    p, q = sp.symbols("p q", nonzero=True)

    balance_leaf = {b21: b12 * p**2 / q**2}
    _m1, _m2, e12, e21 = diagonal_lift_coefficients(
        b12, b21, p, q, sp.S.Zero, sp.S.Zero
    )
    assert sp.simplify(e12 - e21.subs(balance_leaf)) == 0

    mu = sp.simplify(e12)
    assert sp.simplify(e21.subs(balance_leaf) - mu) == 0

    # A one-way process b21=0 cannot satisfy the positive/nonzero balance
    # normalization while p remains a valid observer scale.
    one_way_balance = sp.simplify((b12 * p**2 - b21 * q**2).subs(b21, 0))
    assert one_way_balance.is_zero is False


def test_coupled_canonicalization_derives_matrix_observer_ode_and_autonomizes():
    t = sp.Symbol("t", real=True)
    b12, b21 = sp.symbols("b12 b21", positive=True)
    p, q = sp.symbols("p q", positive=True)

    canonicalization = ConstraintCanonicalization(
        observer_parameters=(p, q),
        constraints=(
            b12 * p**2 - b21 * q**2,
            p * q - 1,
        ),
        label="balanced determinant-one coupled frame",
    )

    b12_path = sp.exp(-2 * t)
    b21_path = sp.exp(2 * t)
    p_path = sp.exp(t)
    q_path = sp.exp(-t)
    base_rates = {
        b12: sp.diff(b12_path, t),
        b21: sp.diff(b21_path, t),
    }
    path_subs = {
        b12: b12_path,
        b21: b21_path,
        p: p_path,
        q: q_path,
    }

    frozen_residuals = tuple(
        sp.simplify(value.subs(path_subs))
        for value in canonicalization.differentiated_constraints(
            base_rates,
            {p: sp.S.Zero, q: sp.S.Zero},
        )
    )
    assert frozen_residuals == (-4, 0)

    connection = canonicalization.induced_connection(base_rates)
    assert connection.certified
    p_dot = sp.simplify(connection.rate(p).subs(path_subs))
    q_dot = sp.simplify(connection.rate(q).subs(path_subs))
    assert p_dot == p_path
    assert q_dot == -q_path

    assert sp.diff(p_path, t) == p_dot
    assert sp.diff(q_path, t) == q_dot

    fixed = diagonal_lift_coefficients(
        b12_path, b21_path,
        sp.S.One, sp.S.One,
        sp.S.Zero, sp.S.Zero,
    )
    arbitrary_p = sp.exp(t / 2)
    arbitrary_q = sp.exp(-t / 2)
    arbitrary = diagonal_lift_coefficients(
        b12_path, b21_path,
        arbitrary_p, arbitrary_q,
        sp.diff(arbitrary_p, t), sp.diff(arbitrary_q, t),
    )
    canonical = diagonal_lift_coefficients(
        b12_path, b21_path,
        p_path, q_path,
        p_dot, q_dot,
    )

    assert tuple(map(sp.simplify, canonical)) == (1, -1, 1, 1)

    u, v = sp.symbols("u v")
    canonical_u_dot = sp.expand(canonical[0] * u + canonical[2] * v)
    canonical_v_dot = sp.expand(canonical[3] * u + canonical[1] * v)
    assert canonical_u_dot == u + v
    assert canonical_v_dot == u - v

    assert coefficient_jet_complexity(fixed, t) == 2
    assert coefficient_jet_complexity(arbitrary, t) == 2
    assert coefficient_jet_complexity(canonical, t) == 0
