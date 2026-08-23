"""Pendulum: elliptic group law as compositional rank lowering of the marked carrier.

Retrieval
---------
Problem: the elliptic group law of the planar simple pendulum's observable
carrier, reconstructed as objectification, free higher-rank composition, and
compositional rank lowering of flow-translation schemas.
Domains: constrained mechanics, elliptic curves, elliptic integrals/functions,
Abel-Jacobi map, one-parameter subgroups, process semantics.
Classical names / aliases: Euler's addition theorem, Abel's theorem, elliptic
group law, chord-tangent addition, lemniscatic elliptic functions, Jacobi sn,
Weierstrass normal form, period lattice.
Structural themes: objectified schema versus fixed output; homomorphic rank
lowering with an exact kernel; task-continuation stability; marked carrier.
Process Geometry roles: observable quotient carrier, process clock omega(D)=1,
objectification, free higher-rank composition, compositional rank lowering,
red teams against unmarked-point objectification.
Prerequisites: the pendulum family guide ``docs/vignettes/simple-pendulum.md``,
``test_pendulum_process_geometry.py``, ``test_pendulum_observable_quotient_fiber.py``,
and the AEG vertical calibrations ``test_aeg_translation_objectification_rank_lowering.py``
and ``test_aeg_addition_multiplication_rank_transition.py``.
Related vignettes: ``docs/52-canonical-completion-hypothesis.md`` (TR-0001),
``docs/50-aeg-translation-objectification-rank-lowering.md``,
``docs/51-aeg-addition-multiplication-rank-transition.md``.
Theory Map relation: supports V3-V4 with a second, geometric (non-arithmetic)
domain and refines the group-layer arrow of TR-0001 with executable content;
no Theory Map node or edge is added or promoted.

Question
--------
The pendulum observable quotient

    U = qy,   Y = D U = vy,   Y^2 = 2 (E - U) (1 - U^2)

carries the process direction ``D`` and the marked differential ``omega = dU/Y``
with ``omega(D) = 1``.  The carrier is a smooth genus-one cubic, so it also
carries the classical chord-tangent group law.  This essay asks a structural
question that is larger than the curve itself:

    Is the elliptic group law of the pendulum carrier an instance of the
    vertical Process Geometry mechanism -- objectification of a stable
    process schema, free higher-rank composition, and compositional rank
    lowering back to the process clock -- and can that reading be certified
    exactly?

The answer tested here is deliberately parallel to the AEG arithmetic
calibration.  There, Multiplication objectified the uniform repeated-Addition
schema ``R_k(T_a) = T_(ka)``: the objectified thing was an *action* on
lower-rank semantic objects, not one of its outputs.  Here the pendulum flow
objectifies the translation schema ``tau_t: p -> p (+) S(t)`` on the carrier
group: again an action, not a point.  Rank lowering is then the clock map
``tau_t -> t``, and Euler's addition theorem is exactly the statement that this
lowering is a homomorphism.

Primitive data
--------------
The primitive input is the reduced first-order carrier of the established
pendulum family (no angle variable, no elliptic function, no period lattice):

    D U = Y,   D Y = 3 U^2 - 2 E U - 1,   Y^2 = 2 (E - U) (1 - U^2),

together with the marked differential

    omega = dU / Y,    omega(D) = 1.

The group law, the Weierstrass form, the lemniscatic closed form, and the
period lattice are *outputs* of the reconstruction below, not inputs.

Classical lineage
-----------------
A smooth plane cubic ``y^2 = P_3(x)`` has a group law: for points ``P, Q`` on
the curve, the chord (or tangent when ``P = Q``) meets the curve in a third
point, whose reflection in the ``x``-axis is ``P (+) Q``; the identity is the
point at infinity and ``-P = (x, -y)``.  See [Silverman-2009, Ch. III].

Euler's addition theorem states that the differential of the third chord point
satisfies

    dU_1/Y_1 + dU_2/Y_2 + dU_3/y_3 = 0,

so the Abel-Jacobi map ``P -> integral^P dU/Y`` is a homomorphism from the
group law to the additive group of the period torus ``C / Lambda``; see
[Euler-1761], [Siegel-1969, Ch. I], [Whittaker-Watson-1927, Ch. XX].

For ``E = 0`` the curve ``Y^2 = 2 U (U^2 - 1)`` is lemniscatic: the flow has the
closed form

    U(t) = -sn^2(t / sqrt(2), i),   Y(t) = -sqrt(2) sn cn dn  (k = i),

see [DLMF-22] and [DLMF-23.5].  The point ``P(0) = (0, 0)`` is 2-torsion.

Shakespeare reconstruction
--------------------------
The explanatory order is reversed.  No group law is imported: the chord-tangent
composition is *derived* on the carrier, Euler's differential identity is
*certified* exactly modulo the curve relations, and only then is the process
reading attached:

1. the carrier cubic is reduced to Weierstrass form exactly;
2. the chord-tangent law is verified to preserve the carrier and to satisfy
   associativity/inverse spot checks with exact rational arithmetic;
3. Euler's addition theorem is certified exactly as a one-form identity modulo
   the curve ideal -- the rank-lowering certificate ``omega(P (+) Q)
   = omega(P) + omega(Q)``;
4. on the lemniscatic leaf the flow is realized in closed form and shown to be
   a one-parameter subgroup twisted by the 2-torsion base point;
5. the objectification semantics is attached: the schema ``tau_t`` (flow
   translation) is objectified, schemas compose by ``(+)``, and lowering is the
   clock sum with kernel the period lattice;
6. three red teams certify what the objectified primitive is *not*.

Calibration statement
---------------------
Passing this file certifies, for the declared carrier and normalizations:

1. the exact Weierstrass reduction ``U = x + E/3, Y = sqrt(2) y`` maps
   ``Y^2 = 2(E-U)(1-U^2)`` to ``y^2 = x^3 + A x + B`` with
   ``A = -(E^2+3)/3`` and ``B = -2E(E-3)(E+3)/27``; at ``E = 0`` this is
   ``y^2 = x^3 - x`` with ``g2 = 4, g3 = 0, j = 1728`` (exact symbolic);
2. the chord-tangent composition keeps the carrier and satisfies exact
   rational associativity and inverse spot checks (exact rational);
3. Euler's addition theorem holds exactly on the carrier, in both chord and
   tangent form (exact symbolic, modulo the curve ideal);
4. the lemniscatic flow ``U(t) = -sn^2(t/sqrt(2), i)`` satisfies the carrier
   ODE, and obeys the twisted subgroup law
   ``P(t1) (+) P(t2) = P(t1+t2) (+) P(0)``; the untwisted orbit
   ``S(t) = P(t) (+) P(0)`` is an exact one-parameter subgroup (sampled
   numerical, 30-digit mpmath);
5. the objectified schema ``tau_t`` composes by clock addition and lowers to
   the clock sum compositionally (executable semantics plus the exact
   certificate of item 3);
6. three red teams hold: an unmarked endpoint merges distinct Cartesian
   continuations; a fixed curve point does not identify the flow schema
   (period ambiguity and the torsion twist); coordinatewise addition leaves
   the carrier.

Proof map
---------
``test_weierstrass_reduction_is_exact`` checks item 1.
``test_chord_tangent_composition_preserves_the_carrier`` checks item 2 (curve
preservation, exact polynomial identity).
``test_euler_addition_identity_is_exact_for_chord_composition`` and
``test_euler_addition_identity_is_exact_for_tangent_doubling`` check item 3.
``test_rational_group_law_spot_checks`` checks item 2 (associativity/inverse,
exact rational arithmetic).
``test_lemniscatic_flow_is_a_twisted_one_parameter_subgroup`` checks item 4.
``test_flow_translation_schemas_compose_and_lower_compositionally`` checks
item 5.
``test_red_team_unmarked_endpoint_merges_distinct_continuations``,
``test_red_team_fixed_curve_point_does_not_identify_the_flow_schema``, and
``test_red_team_coordinatewise_addition_leaves_the_carrier`` check item 6.

Boundary
--------
This essay does *not* claim:

- canonicality or minimality of the group law among presentation choices, and
  does not promote TR-0001 (``docs/52-canonical-completion-hypothesis.md``)
  beyond its T1 status: the group layer is here made executable for one
  carrier, not proven canonical;
- a generic API or any new public/experimental abstraction: all objects are
  research-local and import nothing beyond the canonical namespaces;
- a statement about arbitrary elliptic curves: the carrier is the specific
  pendulum family cubic;
- exact (interval/formal) certificates for the flow subgroup tests: items 4-5
  use 30-digit sampled numerical certificates, not formal power series;
- that the Z2 state fiber of the full Cartesian task (``docs/vignettes/
  simple-pendulum.md`` P5) participates in the group law: the group law lives
  on the carrier curve itself; the fiber is the reconstruction boundary of the
  Cartesian task and is exercised only as a red team for unmarked
  objectification.

References
----------
[Euler-1761] L. Euler, "Observationes de comparatione arcuum curvarum
irrectificibilium", Novi Commentarii Academiae Scientiarum Petropolitanae 6
(1761), 58-84.  Source of the addition theorem for elliptic integrals.

[Siegel-1969] C. L. Siegel, *Topics in Complex Function Theory, Vol. I:
Elliptic Functions and Uniformization Theory*, Wiley-Interscience, 1969.
Chapter I contains Euler's addition theorem and Abel's theorem for elliptic
integrals.

[Silverman-2009] J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed.,
Springer, 2009.  Chapter III: the group law on a smooth cubic.

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson, *A Course of Modern
Analysis*, 4th ed., Cambridge University Press, 1927.  Chapter XX: elliptic
functions and the addition of arguments.

[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
"Jacobian Elliptic Functions." https://dlmf.nist.gov/22

[DLMF-23.5] NIST Digital Library of Mathematical Functions, Section 23.5,
"Special Lattices" (lemniscatic case g3 = 0, tau = i).
https://dlmf.nist.gov/23.5
"""

from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp
import sympy as sp

from process_geometry.process.history import ProcessWord
from process_geometry.process.local import ProcessSystem


# ---------------------------------------------------------------------------
# Shared symbolic machinery: the observable carrier and exact ideal reduction
# ---------------------------------------------------------------------------

U1, Y1, U2, Y2, E, U, x, y = sp.symbols("U1 Y1 U2 Y2 E U x y")


def carrier_polynomial(t: sp.Expr) -> sp.Expr:
    """The pendulum carrier cubic ``P(U)`` with ``Y^2 = P(U)``."""

    return 2 * (E - t) * (1 - t**2)


def reduce_mod_curve(expr: sp.Expr) -> sp.Expr:
    """Reduce ``expr`` modulo ``Y_i^2 = P(U_i)`` for both marked points.

    The reduction replaces ``Y_i^k`` for ``k >= 2`` by ``P(U_i) * Y_i^(k-2)``
    in descending power order, expanding after each substitution.  This is an
    exact polynomial ideal reduction, not a floating-point simplification.
    """

    out = sp.expand(expr)
    for k in range(6, 1, -1):
        out = sp.expand(
            out.subs(
                {
                    Y1**k: Y1 ** (k - 2) * carrier_polynomial(U1),
                    Y2**k: Y2 ** (k - 2) * carrier_polynomial(U2),
                }
            )
        )
    return out


def chord_data():
    """Return ``(D, N, W, M)`` for the chord through ``(U1,Y1),(U2,Y2)``.

    ``D = U2 - U1`` and ``N = Y2 - Y1``.  The chord is
    ``y = (N/D) x + mu``; its third intersection has
    ``U3 = W / D^2`` and ``y3 = M / D^3``.
    """

    D = U2 - U1
    N = Y2 - Y1
    W = sp.expand(E * D**2 + N**2 / 2 - (U1 + U2) * D**2)
    M = sp.expand(N * W + D**2 * (Y1 * D - N * U1))
    return D, N, W, M


# ---------------------------------------------------------------------------
# 1. Exact Weierstrass reduction
# ---------------------------------------------------------------------------


def test_weierstrass_reduction_is_exact():
    # y^2 = P(U)/2 after U = x + E/3 must be a monic depressed cubic.
    poly = sp.expand(carrier_polynomial(x + E / 3) / 2)
    assert sp.Poly(poly, x).nth(3) == 1
    assert sp.Poly(poly, x).nth(2) == 0

    A = sp.factor(sp.Poly(poly, x).nth(1))
    B = sp.factor(sp.Poly(poly, x).nth(0))
    assert A == sp.factor(-(E**2 + 3) / 3)
    assert B == sp.factor(-2 * E * (E - 3) * (E + 3) / 27)

    # Round trip as a polynomial identity in x: the Weierstrass cubic is
    # exactly P(x + E/3)/2, i.e. y^2 = x^3 + A x + B is the normalized carrier.
    round_trip = sp.expand((x**3 + A * x + B) - carrier_polynomial(x + E / 3) / 2)
    assert round_trip == 0

    # The E = 0 leaf is the lemniscatic curve y^2 = x^3 - x: g2 = 4, g3 = 0.
    A0 = sp.simplify(A.subs(E, 0))
    B0 = sp.simplify(B.subs(E, 0))
    assert A0 == -1 and B0 == 0
    g2 = -4 * A0
    g3 = -4 * B0
    j_invariant = sp.simplify(1728 * g2**3 / (g2**3 - 27 * g3**2))
    assert j_invariant == 1728


# ---------------------------------------------------------------------------
# 2. The chord-tangent composition preserves the carrier
# ---------------------------------------------------------------------------


def test_chord_tangent_composition_preserves_the_carrier():
    D, N, W, M = chord_data()

    # Exact polynomial identity: the chord intersects the cubic in
    # U1, U2, U3 with U3 = W/D^2; equivalently
    # (N x + D mu)^2 - D^2 P(x) = -2 (x-U1)(x-U2)(D^2 x - W).
    lhs = sp.expand((N * x + (Y1 * D - N * U1)) ** 2 - carrier_polynomial(x) * D**2)
    rhs = sp.expand(-2 * (x - U1) * (x - U2) * (D**2 * x - W))
    assert reduce_mod_curve(sp.expand(lhs - rhs)) == 0


# ---------------------------------------------------------------------------
# 3. Euler's addition theorem: the rank-lowering certificate
# ---------------------------------------------------------------------------


def test_euler_addition_identity_is_exact_for_chord_composition():
    """omega(P1 (+) P2) = omega(P1) + omega(P2), chord form.

    With ``omega = dU/Y`` and the third intersection ``(U3, y3)`` on the
    chord, Euler's symmetric form is ``dU1/Y1 + dU2/Y2 + dU3/y3 = 0``.
    Since ``P1 (+) P2 = (U3, -y3)`` and ``omega`` flips sign under
    ``y -> -y``, this is exactly the homomorphism statement for ``omega``.
    The identity is verified as an exact one-form identity modulo the curve
    ideal ``Y_i^2 = P(U_i)``.
    """

    D, N, W, M = chord_data()
    Pp1 = sp.diff(carrier_polynomial(U1), U1)
    Pp2 = sp.diff(carrier_polynomial(U2), U2)

    # Coefficient of dU1 in dU3 (chain rule with dY_i = P'(U_i)/(2 Y_i) dU_i):
    #   -N P'(U1)/(2 Y1 D^2) + N^2/D^3 - 1
    # Equation (1/Y1 + c1/y3) * Y1 * y3 * D^3 = 0, denominators cleared:
    #   M - N P'(U1) D/2 + N^2 Y1 - Y1 D^3 = 0
    e1 = sp.expand(M - N * Pp1 * D / 2 + N**2 * Y1 - Y1 * D**3)
    # Equation (1/Y2 + c2/y3) * Y2 * y3 * D^3 = 0:
    #   M + N P'(U2) D/2 - N^2 Y2 - Y2 D^3 = 0
    e2 = sp.expand(M + N * Pp2 * D / 2 - N**2 * Y2 - Y2 * D**3)

    assert reduce_mod_curve(e1) == 0
    assert reduce_mod_curve(e2) == 0


def test_euler_addition_identity_is_exact_for_tangent_doubling():
    """omega(2 P) = 2 omega(P), tangent form, exact modulo the curve ideal."""

    Pp = sp.diff(carrier_polynomial(U1), U1)
    Ppp = sp.diff(carrier_polynomial(U1), U1, 2)
    lam = Pp / (2 * Y1)
    U3t = sp.expand(E + lam**2 / 2 - 2 * U1)
    # Tangent Euler identity (2/Y1 + dU3/y3) * Y1 * y3 = 0, denominators
    # cleared by Y1^3:
    #   8 P'(U3t - U1) Y1^2 + 2 P' P'' Y1^2 - P'^3 = 0
    et = sp.expand(8 * Pp * (U3t - U1) * Y1**2 + 2 * Pp * Ppp * Y1**2 - Pp**3)
    assert reduce_mod_curve(et) == 0


# ---------------------------------------------------------------------------
# 4. Exact rational group-law spot checks on the E = 13/10 carrier
# ---------------------------------------------------------------------------


def test_rational_group_law_spot_checks():
    """Associativity, inverse, and doubling with exact rational arithmetic.

    The points P = (4/5, 3/5), Q = 2P = (353/225, 2992/3375), and the
    2-torsion point R = (1, 0) lie on the carrier with E = 13/10; all
    computations below are exact rational.
    """

    E0 = sp.Rational(13, 10)
    P = (sp.Rational(4, 5), sp.Rational(3, 5))
    Q = (sp.Rational(353, 225), sp.Rational(2992, 3375))
    R = (sp.Integer(1), sp.Integer(0))

    def on_curve(pt):
        uu, yy = pt
        return sp.simplify(yy**2 - 2 * (E0 - uu) * (1 - uu**2)) == 0

    def add(pt1, pt2):
        u1, y1 = pt1
        u2, y2 = pt2
        if u1 == u2 and y1 == y2:
            slope = (6 * u1**2 - 4 * E0 * u1 - 2) / (2 * y1)
            u3 = sp.simplify(E0 + slope**2 / 2 - 2 * u1)
        else:
            slope = (y2 - y1) / (u2 - u1)
            u3 = sp.simplify(E0 + slope**2 / 2 - u1 - u2)
        y3 = sp.simplify(slope * u3 + (y1 - slope * u1))
        return (sp.simplify(u3), sp.simplify(-y3))

    assert on_curve(P) and on_curve(Q) and on_curve(R)

    # Curve preservation, chord and doubling, exact.
    assert on_curve(add(P, Q))
    assert on_curve(add(P, P))

    # Associativity with exact rationals.
    left = add(add(P, Q), R)
    right = add(P, add(Q, R))
    assert left[0] == right[0] and left[1] == right[1]

    # Inverse: (P (+) Q) (+) (-Q) = P.
    minus_Q = (Q[0], -Q[1])
    back = add(add(P, Q), minus_Q)
    assert back[0] == P[0] and back[1] == P[1]


# ---------------------------------------------------------------------------
# 5. Lemniscatic flow: a one-parameter subgroup twisted by 2-torsion
# ---------------------------------------------------------------------------

mp.mp.dps = 30


def lemniscatic_sn(u):
    return mp.re(mp.ellipfun("sn", u, -1))


def lemniscatic_cn(u):
    return mp.re(mp.ellipfun("cn", u, -1))


def lemniscatic_dn(u):
    return mp.re(mp.ellipfun("dn", u, -1))


def flow_U(t):
    return -(lemniscatic_sn(t / mp.sqrt(2))) ** 2


def flow_Y(t):
    return -mp.sqrt(2) * lemniscatic_sn(t / mp.sqrt(2)) * lemniscatic_cn(
        t / mp.sqrt(2)
    ) * lemniscatic_dn(t / mp.sqrt(2))


def flow_point(t):
    return (flow_U(t), flow_Y(t))


def chord_add(pt1, pt2):
    """Chord-tangent composition on the E = 0 carrier, mpmath arithmetic."""

    u1, y1 = pt1
    u2, y2 = pt2
    if u1 == u2 and y1 == y2:
        if y1 == 0:  # pragma: no cover - 2-torsion doubling is the identity
            raise ValueError("doubling a 2-torsion point reaches the identity")
        slope = (6 * u1**2 - 2) / (2 * y1)
        u3 = slope**2 / 2 - 2 * u1
    else:
        slope = (y2 - y1) / (u2 - u1)
        u3 = slope**2 / 2 - u1 - u2
    y3 = slope * u3 + (y1 - slope * u1)
    return (u3, -y3)


def test_lemniscatic_flow_is_a_twisted_one_parameter_subgroup():
    """E = 0 closed form: on-carrier ODE and the torsion-twisted subgroup law.

    Sampled numerical certificates at 30-digit precision.
    """

    # The closed form satisfies Y^2 = 2 U (U^2 - 1) and dU/dt = Y.
    for tv in (mp.mpf("0.3"), mp.mpf("1.0"), mp.mpf("2.1")):
        uu, yy = flow_point(tv)
        assert abs(yy**2 - 2 * uu * (uu**2 - 1)) < mp.mpf("1e-25")
    mid = mp.mpf("0.5")
    assert abs(mp.diff(flow_U, mid) - flow_Y(mid)) < mp.mpf("1e-25")

    base = (mp.mpf(0), mp.mpf(0))  # P(0) = (0,0), a 2-torsion point

    # Twisted subgroup law: P(t1) (+) P(t2) = P(t1+t2) (+) P(0).
    for t1, t2 in ((mp.mpf("0.3"), mp.mpf("0.7")),
                   (mp.mpf("1.1"), mp.mpf("0.9")),
                   (mp.mpf("0.5"), mp.mpf("0.5"))):
        left = chord_add(flow_point(t1), flow_point(t2))
        right = chord_add(flow_point(t1 + t2), base)
        assert abs(left[0] - right[0]) + abs(left[1] - right[1]) < mp.mpf("1e-12")

    # Untwisted orbit S(t) = P(t) (+) P(0) is an exact one-parameter subgroup.
    def S(t):
        return chord_add(flow_point(t), base)

    for t1, t2 in ((mp.mpf("0.3"), mp.mpf("0.7")),
                   (mp.mpf("1.1"), mp.mpf("0.9"))):
        left = chord_add(S(t1), S(t2))
        right = S(t1 + t2)
        assert abs(left[0] - right[0]) + abs(left[1] - right[1]) < mp.mpf("1e-12")

    # Lemniscatic cross-check: sn reaches its peak sn(varpi/2, i)^2 = 1 and
    # its first positive zero at sn(varpi, i) = 0, so the real period of
    # U(t) = -sn^2(t/sqrt(2), i) is T_p = 2 sqrt(2) varpi.
    varpi = mp.gamma(mp.mpf(1) / 4) ** 2 / (2 * mp.sqrt(2 * mp.pi))
    assert abs(lemniscatic_sn(varpi / 2) ** 2 - 1) < mp.mpf("1e-25")
    assert abs(lemniscatic_sn(varpi)) < mp.mpf("1e-25")
    T_p = 2 * mp.sqrt(2) * varpi
    assert T_p > 0
    u0, y0 = flow_point(mp.mpf("0.4"))
    uT, yT = flow_point(mp.mpf("0.4") + T_p)
    assert abs(u0 - uT) + abs(y0 - yT) < mp.mpf("1e-12")


# ---------------------------------------------------------------------------
# 6. Objectification semantics: flow translations compose and lower
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FlowTranslation:
    """Research-local objectification of the flow-translation schema.

    ``tau_t`` acts on carrier points by the untwisted subgroup:
    ``p -> p (+) S(t)`` with ``S(t) = P(t) (+) P(0)``.  This mirrors the AEG
    discipline: the objectified thing is the schema (an action), not one of
    its outputs.
    """

    clock: mp.mpf

    def apply(self, point):
        return chord_add(point, _subgroup_point(self.clock))

    def compose(self, later: "FlowTranslation") -> "FlowTranslation":
        return FlowTranslation(self.clock + later.clock)

    def lower(self) -> mp.mpf:
        """Rank lowering: the schema lowers to its process clock."""

        return self.clock


def _subgroup_point(t):
    return chord_add(flow_point(t), (mp.mpf(0), mp.mpf(0)))


def test_flow_translation_schemas_compose_and_lower_compositionally():
    """Schemas compose by clock addition and lower homomorphically.

    The exact mathematical certificate for the homomorphism is the Euler
    identity of ``test_euler_addition_identity_is_exact_for_chord_composition``;
    this test makes the process semantics executable: higher-rank words of
    schemas compose by ``(+)`` and lower to the sum of clocks, with the
    period lattice as the kernel (see the fixed-point red team).
    """

    tau_1 = FlowTranslation(mp.mpf("0.3"))
    tau_2 = FlowTranslation(mp.mpf("0.7"))
    start = _subgroup_point(mp.mpf("0.1"))

    # Higher-rank free composition through the framework's ProcessWord.
    word = ProcessWord((tau_1, tau_2))
    lowered = ProcessWord[FlowTranslation]()
    total = mp.mpf(0)
    for step in word:
        total = total + step.lower()

    # Compositional rank lowering: applying the composed schema equals
    # applying the schemas in word order, and lowering is the clock sum.
    applied = tau_2.apply(tau_1.apply(start))
    composed = tau_1.compose(tau_2).apply(start)
    assert abs(applied[0] - composed[0]) + abs(applied[1] - composed[1]) < mp.mpf(
        "1e-12"
    )
    assert total == tau_1.lower() + tau_2.lower()
    assert abs(total - mp.mpf("1.0")) < mp.mpf("1e-30")


# ---------------------------------------------------------------------------
# 7. Red teams
# ---------------------------------------------------------------------------


def test_red_team_unmarked_endpoint_merges_distinct_continuations():
    """Terminal (U, Y) is not continuation-stable for the Cartesian task.

    The two states below have identical observable image (U, Y) = (4/5, 3/5)
    and energy E = 13/10, but their D-continuations differ in the sign of
    qx.  An objectification that retained only the unmarked endpoint would
    merge histories whose future Cartesian continuations diverge; the marked
    point (U, Y, sigma) keeps them apart.  This is the geometric analogue of
    the AEG |q| red team.
    """

    qx, qy, vx, vy = sp.symbols("qx qy vx vy")
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: (qy - vx**2 - vy**2) * qx,
            vy: -1 + (qy - vx**2 - vy**2) * qy,
        },
        name="D",
    )

    states = {
        "plus": {qx: sp.Rational(3, 5), qy: sp.Rational(4, 5),
                 vx: sp.Rational(-4, 5), vy: sp.Rational(3, 5)},
        "minus": {qx: sp.Rational(-3, 5), qy: sp.Rational(4, 5),
                  vx: sp.Rational(4, 5), vy: sp.Rational(3, 5)},
    }

    def on_state(state, expr):
        return sp.simplify(expr.subs(state)) == 0

    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    energy = (vx**2 + vy**2) / 2 + qy - sp.Rational(13, 10)

    for state in states.values():
        assert on_state(state, rod)
        assert on_state(state, tangent)
        assert on_state(state, energy)

    # Identical observable quotient point.
    plus, minus = states["plus"], states["minus"]
    assert plus[qy] == minus[qy] == sp.Rational(4, 5)
    assert plus[vy] == minus[vy] == sp.Rational(3, 5)

    # Opposite Z2 fiber bits ...
    assert plus[qx] == -minus[qx]

    # ... and the Cartesian D-continuations diverge in qx while the
    # observable continuation agrees.
    assert sp.simplify(system.derive(qx).subs(plus)) == -sp.simplify(
        system.derive(qx).subs(minus)
    )
    assert sp.simplify(system.derive(qy).subs(plus)) == sp.simplify(
        system.derive(qy).subs(minus)
    )


def test_red_team_fixed_curve_point_does_not_identify_the_flow_schema():
    """One carrier point is the output of many distinct flow schemas.

    (a) Period ambiguity: P(t) = P(t + T_p) as carrier points, while the
    clocks differ by the real period.  (b) Torsion twist: the raw flow points
    do not even form a subgroup -- P(t1) (+) P(t2) differs from P(t1+t2) by
    the 2-torsion base point P(0).  Both show that the objectified primitive
    must be the translation schema tau_t, not the point it produces: the
    fixed-output reading cannot identify the schema, exactly as one additive
    output T_6 could not identify the multiplicative schema in the AEG
    calibration.
    """

    varpi = mp.gamma(mp.mpf(1) / 4) ** 2 / (2 * mp.sqrt(2 * mp.pi))
    T_p = 2 * mp.sqrt(2) * varpi

    # (a) Same point, distinct clocks.
    t = mp.mpf("0.4")
    pt = flow_point(t)
    ptT = flow_point(t + T_p)
    assert abs(pt[0] - ptT[0]) + abs(pt[1] - ptT[1]) < mp.mpf("1e-12")
    assert T_p > mp.mpf("1")

    # (b) The raw flow is not a subgroup; the twist by P(0) is exact.
    t1, t2 = mp.mpf("0.3"), mp.mpf("0.7")
    raw_sum = chord_add(flow_point(t1), flow_point(t2))
    raw_flow = flow_point(t1 + t2)
    assert abs(raw_sum[0] - raw_flow[0]) + abs(raw_sum[1] - raw_flow[1]) > mp.mpf(
        "1e-3"
    )
    twisted = chord_add(raw_flow, (mp.mpf(0), mp.mpf(0)))
    assert abs(raw_sum[0] - twisted[0]) + abs(raw_sum[1] - twisted[1]) < mp.mpf(
        "1e-12"
    )


def test_red_team_coordinatewise_addition_leaves_the_carrier():
    """Coordinatewise addition is not the semantic composition law.

    For the rational carrier points P = (4/5, 3/5) and R = (1, 0) on
    E = 13/10, the coordinatewise sum (9/5, 3/5) satisfies
    2(E - U)(1 - U^2) = 56/25, not (3/5)^2 = 9/25: the sum leaves the
    carrier.  The chord-tangent law is the composition compatible with the
    marked differential omega, certified exactly by Euler's identity above.
    """

    E0 = sp.Rational(13, 10)
    u_sum = sp.Rational(4, 5) + sp.Integer(1)
    y_sum = sp.Rational(3, 5)
    lhs = y_sum**2
    rhs = 2 * (E0 - u_sum) * (1 - u_sum**2)
    assert sp.simplify(lhs - rhs) != 0
    assert lhs == sp.Rational(9, 25)
    assert rhs == sp.Rational(56, 25)
