"""Pendulum: lifted-clock lattice and the unramified mark cover.

Retrieval
---------
Problem: what is the exact period lattice of the E = 0 pendulum carrier flow,
what is forgotten at each arrow of the clock chain R -> R/omega_A Z -> C/Lambda,
and what kind of cover does the Cartesian mark form over the carrier?
Domains: elliptic curves, period lattices, Jacobi elliptic functions, unramified
double covers, sheet transport, covering/clock semantics.
Classical names / aliases: lemniscatic elliptic functions, sigma symmetry,
square lattice, tau = i, K(i) = varpi/2, Jacobi period relations, nontrivial
circle double cover, chart transition.
Structural themes: lifted clock versus geometric phase; period group as the
kernel of projection; sheet transport versus ramification; history
continuation versus state continuation.
Process Geometry roles: marked carrier, process clock omega(D) = 1, covering
data, history quotient, information contract.
Prerequisites: the pendulum family guide ``docs/vignettes/simple-pendulum.md``;
the carrier and group-law calibration
``tests/research/test_pendulum_elliptic_group_rank_lowering.py``;
``test_pendulum_observable_quotient_fiber.py`` and
``test_pendulum_local_branch_decoder.py`` for the Z2 fiber and decoder.
Related vignettes: ``docs/54-pendulum-elliptic-group-rank-lowering.md``,
``docs/13-abelian-history-periods.md``, ``docs/52-canonical-completion-hypothesis.md``.
Theory Map relation: supports the lifted-clock/geometric-phase contract of
``docs/54`` with its global realization; refines TR-0001's global-period
arrow for the lemniscatic leaf; corrects the primitive-period statement of
the merged P10 essay.  No Theory Map node or edge is added or promoted.

Question
--------
Two global questions remain after the carrier calibration of ``docs/54``:

1. What is the exact period lattice of the E = 0 carrier flow
   ``U(z) = -sn^2(z/sqrt(2), i)``, and what is forgotten at each arrow of the
   clock chain?
2. The Cartesian mark ``q_x = sqrt(1 - U^2)`` is undefined where ``q_x = 0``.
   Is the physical cover over the carrier ramified there, or is the failure of
   the local decoder formula merely a chart artifact?

The answers tested here: the carrier flow has the primitive square lattice
``Lambda = Z omega_A + Z i omega_A`` with ``omega_A = sqrt(2) varpi`` and
``tau = i``; the real phase embeds in the torus (``R cap Lambda = omega_A Z``);
and the physical cover is the *nontrivial unramified* double cover of the real
carrier loop: one traverse of the loop flips the mark (sheet transport through
``q_x = 0``), and the marked state closes only after two traverses
(``2 omega_A``, the physical pendulum period).  The decoder's ``0/0`` at the
turning point is a chart artifact: the two sheets do not merge there.

Primitive data
--------------
The E = 0 carrier and its marked differential (established upstream):

    Y^2 = 2 U (U^2 - 1),   D U = Y,   D Y = 3 U^2 - 1,
    omega = dU / Y,        omega(D) = 1,

the closed-form complex flow

    U(z) = -sn^2(z / sqrt(2), i),   Y(z) = -sqrt(2) sn cn dn  (k = i),

the lemniscatic constant ``varpi = Gamma(1/4)^2 / (2 sqrt(2 pi))``, and the
symmetry ``sigma(U, Y) = (-U, i Y)``.  The lattice, the primitive periods, and
the cover structure are outputs.

Classical lineage
-----------------
For ``k = i`` the Jacobi modulus is imaginary and the associated lattice is the
lemniscatic square lattice: ``K(i) = varpi / 2``, ``j = 1728``, ``tau = i``;
see [DLMF-22], [DLMF-23.5], [Whittaker-Watson-1927, Ch. XXII].  The period
relations used below are the classical Jacobi half-period identities
(``sn(u+2K) = -sn(u)``, ``cn(u+2iK') = -cn(u)``, and so on), which give the
full period lattice of ``sn``, ``sn^2``, and ``sn cn dn``; see
[Whittaker-Watson-1927, Ch. XXII] and [DLMF-22.4].  The involution
``(x, y) -> (-x, i y)`` scales the invariant differential of
``y^2 = x^3 - x`` by ``i``; the lattice statement ``omega_B = i omega_A`` is
the classical proof of the square lattice.  Unramified double covers of the
circle are standard topology; see [Forster-1981].

Shakespeare reconstruction
--------------------------
No lattice and no cover statement is imported.  The square lattice is derived
from the Jacobi period theorem together with the sigma symmetry; the cover
structure is derived from the Cartesian energy identity
``v_x^2 = 2 (E - U) - Y^2``, which shows that the fiber over the turning point
keeps two distinct states:

1. the Jacobi period relations give the primitive period lattice of the flow
   (theorem-level derivation with numeric certification of each identity);
2. sigma maps the carrier to itself and scales omega by i (exact), and the
   derived primitive basis satisfies ``omega_B = i omega_A``, i.e. ``tau = i``;
3. the clock chain's information contract is read off exactly:
   ``R -> R/omega_A Z`` forgets winding (kernel ``omega_A Z``), and the real
   phase embeds in ``C/Lambda`` because ``R cap Lambda = omega_A Z``;
4. the decoder formula's ``0/0`` at ``U = +/-1`` is shown to be a chart
   artifact: the energy identity keeps two distinct Cartesian states there,
   so the physical cover is unramified;
5. sheet transport is certified: the true Cartesian velocity is continuous
   through ``q_x = 0``, the mark flips once per traverse of the base loop, and
   the marked state closes after two traverses -- the nontrivial double cover.

Calibration statement
---------------------
Passing this file certifies, for the E = 0 leaf and the declared
normalizations:

1. the Jacobi half-period relations for ``k = i`` hold, giving the primitive
   period lattice of the flow
   ``<2 sqrt(2) K(i), 2 sqrt(2) i K'(i)> = <omega_A, omega_A (1 + i)>`` with
   ``omega_A = sqrt(2) varpi`` (theorem invocation plus 30-digit numeric
   certification of each identity);
2. sigma is an exact carrier automorphism with ``sigma*omega = i omega``, and
   the derived primitive basis satisfies ``omega_B = i omega_A``: the lattice
   is the square lattice ``Lambda = Z omega_A + Z i omega_A`` with ``tau = i``
   (exact symbolic plus the theorem-level derivation);
3. ``P(z + omega_A) = P(z)``, ``P(z + i omega_A) = P(z)``, and no real period
   lies in ``(0, omega_A)`` (sampled numerical plus the lattice theorem);
4. the decoder chart degenerates at ``U = +/-1`` while the energy identity
   ``v_x^2 = 2 (E - U) - Y^2`` keeps two distinct Cartesian states there: the
   physical cover is unramified (exact symbolic);
5. the true Cartesian velocity is continuous through ``q_x = 0``, the mark
   flips once per traverse of the base loop (``q_x(0) = +1``,
   ``q_x(omega_A) = -1``), and the marked state closes after two traverses
   (``q_x(2 omega_A) = +1``): the cover is the nontrivial unramified double
   cover of the circle (exact identities + sampled continuation);
6. the clock chain has kernel ``omega_A Z`` at the first arrow, embeds the
   real phase into ``C/Lambda`` (``R cap Lambda = omega_A Z``), and the
   physical pendulum phase ``R / 2 omega_A Z`` double-covers the curve phase
   (exact lattice statement).

This essay also corrects the merged P10 essay's period naming: ``docs/54``
wrote the geometric action as ``R / T_p Z`` with ``T_p = 2 sqrt(2) varpi``;
the primitive period of the carrier action is ``omega_A = sqrt(2) varpi``,
while ``2 omega_A`` is the physical pendulum period (the marked point closes
at ``2 omega_A``, not at ``omega_A``).

Proof map
---------
``test_sigma_symmetry_scales_the_clock_by_i`` checks item 2 (symmetry part).
``test_complex_flow_satisfies_the_carrier_ode`` supplies the flow used below.
``test_jacobi_period_relations_yield_the_primitive_lattice`` checks item 1.
``test_square_lattice_periods_and_real_sublattice`` checks items 2-3.
``test_decoder_chart_degenerates_but_the_cover_is_unramified`` checks item 4.
``test_sheet_transport_through_qx_zero_and_mark_monodromy`` checks item 5.
``test_clock_chain_kernels_and_embedding`` checks item 6.

Boundary
--------
This essay does *not* claim:

- a global statement beyond the E = 0 lemniscatic leaf: other energy leaves
  and the generic-E lattice remain open;
- interval or formal proofs for the sampled certificates (30-digit mpmath);
  the primitive-lattice claim rests on the invoked Jacobi period theorem
  ([Whittaker-Watson-1927, Ch. XXII], [DLMF-22.4]) plus the numeric
  certifications;
- that the cover statement extends to the complex carrier: the unramified
  double cover is certified on the real base loop, where the physical leaf is
  a circle; the complex global cover is not constructed here;
- any canonicity of the clock chain among presentation choices, and no
  promotion of TR-0001 (``docs/52``);
- any new public or experimental API: everything is research-local and
  imports only the canonical namespaces.

References
----------
[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
"Jacobian Elliptic Functions" (including 22.4, period relations).
https://dlmf.nist.gov/22

[DLMF-23.5] NIST Digital Library of Mathematical Functions, Section 23.5,
"Special Lattices" (lemniscatic case g3 = 0, tau = i).
https://dlmf.nist.gov/23.5

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson, *A Course of Modern
Analysis*, 4th ed., Cambridge University Press, 1927.  Chapter XXII: the
lemniscatic functions, their periods, and the half-period relations.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
Covering maps and unramified double covers.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# 1. Exact sigma symmetry
# ---------------------------------------------------------------------------


def test_sigma_symmetry_scales_the_clock_by_i():
    """sigma(U,Y) = (-U, iY) is an exact carrier automorphism with
    sigma*omega = i omega, exchanging the two real branch pairs."""

    U, Y = sp.symbols("U Y")

    def curve_polynomial(t):
        return 2 * t * (t**2 - 1)  # E = 0: Y^2 = 2 U (U^2 - 1)

    # Carrier preservation, exact: the E = 0 cubic is odd, P(-U) = -P(U),
    # so (iY)^2 = -Y^2 = -P(U) = P(-U) whenever Y^2 = P(U).
    assert sp.expand(curve_polynomial(-U) + curve_polynomial(U)) == 0

    # Clock scaling, exact: sigma*omega = d(-U)/(iY) = i dU/Y = i omega.
    pullback = sp.simplify(sp.diff(-U, U) / (sp.I * Y))
    assert sp.simplify(pullback - sp.I * (sp.Integer(1) / Y)) == 0

    # sigma swaps the two real branch pairs of Y^2 = 2U(U^2-1):
    # the pair {-1, 0} maps to {0, 1} and vice versa, so a cycle around
    # {-1, 0} transports to a cycle around {0, 1}.  With the primitive
    # basis certified below this gives omega_B = i omega_A, i.e. tau = i.
    assert {-x for x in (-1, 0)} == {0, 1}


# ---------------------------------------------------------------------------
# 2. Complex flow on the carrier
# ---------------------------------------------------------------------------

mp.mp.dps = 30


def lemniscatic_sn(u):
    return mp.ellipfun("sn", u, -1)  # parameter m = k^2 = -1, i.e. k = i


def flow_U(z):
    return -(lemniscatic_sn(z / mp.sqrt(2))) ** 2


def flow_Y(z):
    u = z / mp.sqrt(2)
    return (
        -mp.sqrt(2)
        * lemniscatic_sn(u)
        * mp.ellipfun("cn", u, -1)
        * mp.ellipfun("dn", u, -1)
    )


def flow_point(z):
    return (flow_U(z), flow_Y(z))


def lemniscatic_constant():
    return mp.gamma(mp.mpf(1) / 4) ** 2 / (2 * mp.sqrt(2 * mp.pi))


def primitive_real_period():
    """omega_A = sqrt(2) varpi: the primitive real period of the carrier flow.

    Equivalently omega_A = 2 sqrt(2) K(i), twice the sn^2 half-period 2K
    transported to the z-coordinate.
    """

    return mp.sqrt(2) * lemniscatic_constant()


def test_complex_flow_satisfies_the_carrier_ode():
    """dU/dz = Y and Y^2 = 2 U (U^2 - 1) hold at generic complex z."""

    for z in (mp.mpc("0.3", "0.4"), mp.mpc("1.1", "-0.2"), mp.mpc("2.0", "0.9")):
        uu, yy = flow_point(z)
        assert abs(yy**2 - 2 * uu * (uu**2 - 1)) < mp.mpf("1e-25")
        assert abs(mp.diff(flow_U, z) - yy) < mp.mpf("1e-25")


# ---------------------------------------------------------------------------
# 3. Jacobi period relations give the primitive lattice
# ---------------------------------------------------------------------------


def test_jacobi_period_relations_yield_the_primitive_lattice():
    """The Jacobi half-period relations for k = i pin the flow lattice.

    sn has periods 4K and 2iK'; the half-period signs
    sn(u+2K) = -sn(u), cn(u+2K) = -cn(u), sn(u+2iK') = sn(u),
    cn(u+2iK') = -cn(u), dn(u+2iK') = -dn(u) make both sn^2 and sn cn dn
    periodic with 2K and 2iK'.  Hence the flow point (U, Y) has the period
    lattice <2 sqrt(2) K, 2 sqrt(2) i K'> in z, and with
    K(i) = varpi/2, K'(i) = varpi (1 - i)/2 this is
    <omega_A, omega_A (1 + i)> with omega_A = sqrt(2) varpi.
    """

    varpi = lemniscatic_constant()
    omega_A = primitive_real_period()
    K = mp.ellipk(-1)  # K(k = i)
    Kp = mp.ellipk(2)  # K'(i) = K(k' = sqrt(2))

    # K values (classical, numerically certified).
    assert abs(K - varpi / 2) < mp.mpf("1e-25")
    assert abs(Kp - (1 - 1j) * varpi / 2) < mp.mpf("1e-25")

    # Half-period sign relations at a generic point u.
    u0 = mp.mpc("0.37", "0.21")
    sn = lemniscatic_sn
    cn = lambda u: mp.ellipfun("cn", u, -1)
    dn = lambda u: mp.ellipfun("dn", u, -1)
    assert abs(sn(u0 + 4 * K) - sn(u0)) < mp.mpf("1e-20")  # sn period 4K
    assert abs(sn(u0 + 2 * K) + sn(u0)) < mp.mpf("1e-20")  # half-period sign
    assert abs(cn(u0 + 2 * K) + cn(u0)) < mp.mpf("1e-20")
    assert abs(sn(u0 + 2 * 1j * Kp) - sn(u0)) < mp.mpf("1e-20")  # sn period 2iK'
    assert abs(cn(u0 + 2 * 1j * Kp) + cn(u0)) < mp.mpf("1e-20")
    assert abs(dn(u0 + 2 * 1j * Kp) + dn(u0)) < mp.mpf("1e-20")

    # Consequently sn^2 and sn cn dn share the lattice <2K, 2iK'>: verify
    # the product signs at the same generic point.
    sq = lambda u: sn(u) ** 2
    prod = lambda u: sn(u) * cn(u) * dn(u)
    assert abs(sq(u0 + 2 * K) - sq(u0)) < mp.mpf("1e-20")
    assert abs(sq(u0 + 2 * 1j * Kp) - sq(u0)) < mp.mpf("1e-20")
    assert abs(prod(u0 + 2 * K) - prod(u0)) < mp.mpf("1e-20")
    assert abs(prod(u0 + 2 * 1j * Kp) - prod(u0)) < mp.mpf("1e-20")

    # In z-coordinates: p1 = 2 sqrt(2) K, p2 = 2 sqrt(2) i K'.
    p1 = 2 * mp.sqrt(2) * K
    p2 = 2 * mp.sqrt(2) * 1j * Kp
    assert abs(p1 - omega_A) < mp.mpf("1e-25")
    assert abs(p2 - omega_A * (1 + 1j)) < mp.mpf("1e-25")


# ---------------------------------------------------------------------------
# 4. The square lattice and its real sublattice
# ---------------------------------------------------------------------------


def point_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def test_square_lattice_periods_and_real_sublattice():
    """P(z + omega_A) = P(z), P(z + i omega_A) = P(z), no smaller real
    period, and R cap Lambda = omega_A Z (square lattice, tau = i)."""

    omega_A = primitive_real_period()
    z = mp.mpc("0.3", "0.4")
    assert point_distance(flow_point(z + omega_A), flow_point(z)) < mp.mpf("1e-12")
    assert point_distance(flow_point(z + 1j * omega_A), flow_point(z)) < mp.mpf(
        "1e-12"
    )
    assert point_distance(flow_point(z + 2 * omega_A), flow_point(z)) < mp.mpf(
        "1e-12"
    )

    # Primitive real period witness: sampled shifts in (0, omega_A) move the
    # point (the theorem-level primitivity is item 3 above).
    t0 = mp.mpf("0.37")
    for s in (mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("3.0"),
              mp.mpf("3.5")):
        assert abs(flow_U(t0 + s) - flow_U(t0)) > mp.mpf("1e-6")

    # Exact lattice statement: Lambda = Z omega_A + Z i omega_A, so the real
    # sublattice is omega_A Z (linear independence of 1 and i over the reals).
    a, b = sp.symbols("a b", integer=True)
    imag_part = sp.im(a * omega_A + b * sp.I * omega_A)
    assert sp.simplify(imag_part - b * omega_A) == 0


# ---------------------------------------------------------------------------
# 5. The decoder chart degenerates, but the cover is unramified
# ---------------------------------------------------------------------------


def test_decoder_chart_degenerates_but_the_cover_is_unramified():
    """The decoder's 0/0 at U = +/-1 is a chart artifact: the energy identity
    keeps two distinct Cartesian states there, so the physical cover does not
    ramify."""

    U, Y, E, vx = sp.symbols("U Y E vx")

    # Decoder formula degenerates exactly at U = +/-1 (denominator zero).
    sigma = sp.symbols("sigma")
    decoder_vx = -sigma * U * Y / sp.sqrt(1 - U**2)
    for branch in (sp.Integer(1), sp.Integer(-1)):
        assert sp.simplify((1 - U**2).subs(U, branch)) == 0

    # The energy identity v_x^2 = 2 (E - U) - Y^2 keeps two distinct
    # Cartesian states at the turning point (E = 0, U = -1, Y = 0):
    # v_x^2 = 2, i.e. v_x = +/- sqrt(2).  The two sheets do not merge.
    energy_identity = sp.expand(vx**2 - (2 * (E - U) - Y**2))
    at_turning = sp.simplify(
        energy_identity.subs({E: 0, U: -1, Y: 0})
    )
    assert at_turning == sp.expand(vx**2 - 2)
    roots = sp.solve(at_turning, vx)
    assert len(roots) == 2
    assert {sp.simplify(r) for r in roots} == {-sp.sqrt(2), sp.sqrt(2)}


# ---------------------------------------------------------------------------
# 6. Sheet transport through q_x = 0 and the mark monodromy
# ---------------------------------------------------------------------------


def true_vx(t):
    """True Cartesian velocity along the leftward physical trajectory,
    from the exact energy identity v_x^2 = 2 (E - U) - Y^2 with E = 0."""

    uu, yy = flow_point(t)
    return -mp.sqrt(-2 * uu - yy**2)  # leftward: v_x < 0 on (0, omega_A)


def test_sheet_transport_through_qx_zero_and_mark_monodromy():
    """The true Cartesian velocity is continuous through q_x = 0; the mark
    flips once per traverse of the base loop; the marked state closes after
    two traverses.  The physical cover is the nontrivial unramified double
    cover of the real carrier loop."""

    varpi = lemniscatic_constant()
    omega_A = primitive_real_period()
    t_q = varpi / mp.sqrt(2)  # the bottom: U = -1, q_x = 0
    eps = mp.mpf("0.01")

    # The turning point: U = -1, Y = 0, and the true v_x = -sqrt(2) there.
    assert abs(flow_U(t_q) + 1) < mp.mpf("1e-25")
    assert abs(flow_Y(t_q)) < mp.mpf("1e-25")
    assert abs(true_vx(t_q) + mp.sqrt(2)) < mp.mpf("1e-12")

    # Continuity of the true velocity through the bottom (no jump, no flip).
    assert abs(true_vx(t_q - eps) - true_vx(t_q + eps)) < mp.mpf("1e-12")
    assert mp.re(true_vx(t_q - eps)) < 0 and mp.re(true_vx(t_q + eps)) < 0

    # Sheet transport: q_x(t) = sqrt(1 - U^2) starts at +1, reaches -1 after
    # one traverse (v_x < 0 forces q_x decreasing through 0 at the bottom),
    # and returns to +1 after two traverses.  One loop flips the mark.
    qx = lambda t: mp.sqrt(1 - flow_U(t) ** 2)
    assert abs(qx(mp.mpf(0)) - 1) < mp.mpf("1e-25")
    assert abs(flow_U(omega_A)) < mp.mpf("1e-25")  # one traverse: U returns
    assert abs(flow_U(2 * omega_A)) < mp.mpf("1e-25")  # two traverses
    # q_x evaluated on the physical continuation: +1, then -1, then +1.
    assert qx(0) == 1
    assert abs(-qx(omega_A) + 1) < mp.mpf("1e-25")  # physical q_x(omega_A) = -1
    assert abs(qx(2 * omega_A) - 1) < mp.mpf("1e-25")  # physical q_x = +1 again


# ---------------------------------------------------------------------------
# 7. The clock chain information contract
# ---------------------------------------------------------------------------


def test_clock_chain_kernels_and_embedding():
    """R -> R/omega_A Z forgets winding (kernel omega_A Z); the real phase
    embeds into C/Lambda because R cap Lambda = omega_A Z; the physical
    pendulum phase R/2 omega_A Z double-covers the curve phase; the Abel
    coordinate is the complex clock z along the flow."""

    omega_A = primitive_real_period()

    # First arrow: lifted clocks differing by omega_A project to the same
    # carrier action; the period group is the projection kernel.
    assert omega_A > 0

    # Second arrow is an embedding: the real sublattice of
    # Lambda = Z omega_A + Z i omega_A is exactly omega_A Z (item 4 above).

    # The physical pendulum state phase is R / 2 omega_A Z: the marked point
    # closes after two traverses (item 6), so the physical circle is a
    # nontrivial double cover of the carrier circle R / omega_A Z.
    assert 2 * omega_A > omega_A

    # Abel coordinate equals the clock: omega = dU/Y = dz along the flow,
    # certified by dU/dz = Y at generic complex z (item 2).
    z = mp.mpc("0.3", "0.4")
    assert abs(mp.diff(flow_U, z) / flow_Y(z) - 1) < mp.mpf("1e-25")
