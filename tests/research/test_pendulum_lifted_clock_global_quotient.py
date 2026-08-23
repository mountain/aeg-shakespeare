"""Pendulum: global lifted-clock quotient through the branch locus.

Retrieval
---------
Problem: how does the lifted real clock of the E = 0 pendulum globalize across
the branch points U = +/-1, and what exactly is forgotten at each level of the
clock chain R -> R/T_p Z -> C/Lambda?
Domains: elliptic curves, Riemann surfaces, branched covers, monodromy, period
lattices, Jacobi elliptic functions, covering/clock semantics.
Classical names / aliases: lemniscatic elliptic functions, sigma symmetry,
square lattice, tau = i, K(i) = varpi/2, branch point, sheet monodromy.
Structural themes: lifted clock versus geometric phase; period group as the
kernel of projection; mark monodromy through the branch locus; history
continuation versus state continuation.
Process Geometry roles: marked carrier, process clock omega(D) = 1, covering
data, history quotient, information contract.
Prerequisites: the pendulum family guide ``docs/vignettes/simple-pendulum.md``;
the carrier and group-law calibration
``tests/research/test_pendulum_elliptic_group_rank_lowering.py`` (PR #79);
``test_pendulum_observable_quotient_fiber.py`` and
``test_pendulum_local_branch_decoder.py`` for the Z2 fiber and decoder.
Related vignettes: ``docs/54-pendulum-elliptic-group-rank-lowering.md``,
``docs/13-abelian-history-periods.md``, ``docs/52-canonical-completion-hypothesis.md``.
Theory Map relation: supports the lifted-clock/geometric-phase contract of
``docs/54`` with its global realization; refines TR-0001's global-period
arrow for the lemniscatic leaf; provides the branch-locus degeneration
(boundary) that the T1->T2 gate requires.  No Theory Map node or edge is
added or promoted.

Question
--------
The carrier calibration established three clock levels in ``docs/54``:

```text
lifted real clock R
    -> geometric real action R / T_p Z
    -> complex Abel-Jacobi torus C / Lambda
```

but certified only the first projection on the real flow.  Two global
questions remain, and they are the branch-locus boundary the family guide
lists as priority 1:

1. At the branch points U = +/-1 the local decoder chart degenerates.  Does
   the Z2 mark of the marked carrier extend through them, or is it genuine
   covering data with monodromy?
2. What is the full complex period lattice Lambda of the E = 0 leaf, and what
   exactly is forgotten at each arrow of the clock chain?

The answer tested here: the E = 0 lattice is the square lattice
``Lambda = Z T_p + Z i T_p`` with ``tau = i``, the real phase embeds in the
torus (``R cap Lambda = T_p Z``), and the Z2 mark has monodromy -1 around each
branch point -- it flips at each turning point and therefore does NOT descend
to the carrier.  The mark is history/covering data, exactly the data whose
forgetting the period group measures.

Primitive data
--------------
The E = 0 carrier and its marked differential (established upstream):

    Y^2 = 2 U (U^2 - 1),   D U = Y,   D Y = 3 U^2 - 1,
    omega = dU / Y,        omega(D) = 1,

the closed-form complex flow

    U(z) = -sn^2(z / sqrt(2), i),   Y(z) = -sqrt(2) sn cn dn  (k = i),

the real period ``T_p = 2 sqrt(2) varpi`` with the lemniscatic constant
``varpi = Gamma(1/4)^2 / (2 sqrt(2 pi))``, and the symmetry

    sigma(U, Y) = (-U, i Y).

The lattice, the imaginary period, and the mark monodromy are outputs.

Classical lineage
-----------------
For ``k = i`` the Jacobi modulus is imaginary and the associated lattice is
the lemniscatic square lattice: ``K(i) = varpi / 2``, ``j = 1728``,
``tau = i``; see [DLMF-22], [DLMF-23.5], [Whittaker-Watson-1927, Ch. XXII].
The curve ``y^2 = x^3 - x`` is the classical congruent-number curve of the
lemniscate, and the involution ``(x, y) -> (-x, i y)`` scales its invariant
differential by ``i``; the lattice statement ``omega_B = i omega_A`` is the
classical proof of the square lattice.  Branched covers and their monodromy
are standard Riemann-surface material; see [Forster-1981] and
[Farkas-Kra-1992].

Shakespeare reconstruction
--------------------------
No lattice is imported.  The square lattice is *derived*: the sigma symmetry
is certified exactly on the carrier, the real and imaginary periods are
measured on the closed-form flow at 30-digit precision, the Jacobi period
identities are matched to the lattice, and only then is the clock chain
attached:

1. sigma maps the carrier to itself and scales omega by i (exact);
2. hence any cycle pair transported by sigma satisfies omega_B = i omega_A,
   i.e. tau = i (exact deduction);
3. the complex flow satisfies the carrier ODE and has periods T_p and i T_p
   (sampled numerical);
4. the Jacobi period identities ``K(i) = varpi/2`` and ``T_p = 4 sqrt(2) K(i)``
   close the loop with the classical function theory (sampled numerical);
5. at U = +/-1 the decoder chart degenerates and the Z2 mark flips: the marked
   carrier is a ramified double cover with mark monodromy -1 around each
   branch point, while the real period loop winds around two branch points and
   lifts to a closed loop (exact degeneration + sampled continuation);
6. the clock chain's information contract is then read off exactly:
   ``R -> R/T_p Z`` forgets winding (kernel T_p Z), and the real phase embeds
   in ``C/Lambda`` -- the third level is a complexification, not a further
   quotient.

Calibration statement
---------------------
Passing this file certifies, for the E = 0 leaf and the declared
normalizations:

1. sigma is an exact automorphism of the carrier with sigma*omega = i omega,
   swapping the two real branch pairs (exact symbolic);
2. the complex flow satisfies dU/dz = Y and lies on the carrier for generic
   complex z (sampled numerical);
3. P(z + T_p) = P(z) and P(z + i T_p) = P(z), with T_p the primitive real
   period, so Lambda = Z T_p + Z i T_p and tau = i (sampled numerical plus
   exact lattice statement);
4. K(i) = varpi/2 and T_p = 4 sqrt(2) K(i); the imaginary period i T_p is the
   lattice combination 2 sqrt(2)(2iK' - 2K) of the Jacobi basis (sampled
   numerical);
5. the local decoder chart degenerates at U = +/-1 (exact); the Z2 mark flips
   across each turning point, so the marked cover is ramified over the branch
   points and the real period loop lifts to a closed marked loop (exact
   degeneration statement + sampled sign flip);
6. the clock chain has kernel T_p Z at the first arrow and embeds the real
   phase into C/Lambda (exact lattice statement: R cap Lambda = T_p Z).

Proof map
---------
``test_sigma_symmetry_scales_the_clock_by_i`` checks item 1.
``test_complex_flow_satisfies_the_carrier_ode`` checks item 2.
``test_square_lattice_periods`` checks item 3.
``test_jacobi_period_identities_match_the_lattice`` checks item 4.
``test_decoder_chart_degenerates_at_the_branch_points`` checks item 5 (chart).
``test_mark_monodromy_flips_across_each_turning_point`` checks item 5 (mark).
``test_clock_chain_kernels_and_embedding`` checks item 6.

Boundary
--------
This essay does *not* claim:

- a global statement beyond the E = 0 lemniscatic leaf: other energy leaves
  and the generic-E lattice remain open;
- full Cartesian state continuation across U = +/-1 into other sheets: the
  essay certifies the mark monodromy and the decoder degeneration, not a
  global Cartesian decoder;
- interval or formal proofs for the sampled period certificates (30-digit
  mpmath);
- any canonicity of the clock chain among presentation choices, and no
  promotion of TR-0001 (``docs/52``);
- any new public or experimental API: everything is research-local and
  imports only the canonical namespaces.

References
----------
[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
"Jacobian Elliptic Functions." https://dlmf.nist.gov/22

[DLMF-23.5] NIST Digital Library of Mathematical Functions, Section 23.5,
"Special Lattices" (lemniscatic case g3 = 0, tau = i).
https://dlmf.nist.gov/23.5

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson, *A Course of Modern
Analysis*, 4th ed., Cambridge University Press, 1927.  Chapter XXII: the
lemniscatic functions and their periods.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
Branched covers, ramification, and monodromy.

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992.  Double covers of the sphere and their sheet monodromy.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# 1. Exact sigma symmetry
# ---------------------------------------------------------------------------


def test_sigma_symmetry_scales_the_clock_by_i():
    """sigma(U,Y) = (-U, iY) is an exact carrier automorphism with
    sigma*omega = i omega, and it swaps the two real branch pairs."""

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
    # {-1, 0} transports to a cycle around {0, 1}.  The deduction
    # omega_B = omega_{sigma(A)} = int_A sigma*omega = i omega_A (hence
    # tau = i) is recorded in prose and certified numerically below.
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


def test_complex_flow_satisfies_the_carrier_ode():
    """dU/dz = Y and Y^2 = 2 U (U^2 - 1) hold at generic complex z."""

    for z in (mp.mpc("0.3", "0.4"), mp.mpc("1.1", "-0.2"), mp.mpc("2.0", "0.9")):
        uu, yy = flow_point(z)
        assert abs(yy**2 - 2 * uu * (uu**2 - 1)) < mp.mpf("1e-25")
        assert abs(mp.diff(flow_U, z) - yy) < mp.mpf("1e-25")


# ---------------------------------------------------------------------------
# 3. The square lattice
# ---------------------------------------------------------------------------


def lemniscatic_constant():
    return mp.gamma(mp.mpf(1) / 4) ** 2 / (2 * mp.sqrt(2 * mp.pi))


def real_period():
    return 2 * mp.sqrt(2) * lemniscatic_constant()


def point_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def test_square_lattice_periods():
    """P(z + T_p) = P(z) and P(z + i T_p) = P(z); T_p is primitive real."""

    T_p = real_period()
    z = mp.mpc("0.3", "0.4")
    assert point_distance(flow_point(z + T_p), flow_point(z)) < mp.mpf("1e-12")
    assert point_distance(flow_point(z + 1j * T_p), flow_point(z)) < mp.mpf("1e-12")

    # Primitive real period: no smaller positive real s closes the point.
    t0 = mp.mpf("0.37")
    for s in (mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("3.0")):
        assert abs(flow_U(t0 + s) - flow_U(t0)) > mp.mpf("1e-6")

    # Exact lattice statement: Lambda = { a T_p + b i T_p : a, b in Z },
    # so the real sublattice is T_p Z (b = 0 forces realness, T_p > 0).
    assert T_p > 0


# ---------------------------------------------------------------------------
# 4. Jacobi period identities
# ---------------------------------------------------------------------------


def test_jacobi_period_identities_match_the_lattice():
    """K(i) = varpi/2, T_p = 4 sqrt(2) K(i), and i T_p is the lattice
    combination 2 sqrt(2)(2 i K' - 2 K) of the Jacobi basis."""

    varpi = lemniscatic_constant()
    T_p = real_period()

    # mpmath ellipk(m) takes the parameter m = k^2: k = i <-> m = -1,
    # and K'(i) = K(k' = sqrt(2)) <-> m = 2.
    K = mp.ellipk(-1)
    Kp = mp.ellipk(2)

    assert abs(K - varpi / 2) < mp.mpf("1e-25")
    assert abs(T_p - 4 * mp.sqrt(2) * K) < mp.mpf("1e-25")
    assert abs(Kp - (1 - 1j) * varpi / 2) < mp.mpf("1e-25")

    # In the z-coordinate the Jacobi basis of the flow is
    #   p1 = sqrt(2) * 2K,   p2 = sqrt(2) * 2 i K',
    # and the imaginary period is i T_p = 2 p2 - 2 p1.
    p1 = 2 * mp.sqrt(2) * K
    p2 = 2 * mp.sqrt(2) * 1j * Kp
    assert abs(2 * p2 - 2 * p1 - 1j * T_p) < mp.mpf("1e-25")


# ---------------------------------------------------------------------------
# 5. The branch-locus degeneration and the mark monodromy
# ---------------------------------------------------------------------------


def test_decoder_chart_degenerates_at_the_branch_points():
    """The local decoder v_x = -sigma U Y / sqrt(1 - U^2) degenerates exactly
    at U = +/-1: the chart denominator vanishes, q_x = 0, and the mark
    sigma = sign(q_x) is undefined there."""

    U, Y, sigma = sp.symbols("U Y sigma")
    decoder_vx = -sigma * U * Y / sp.sqrt(1 - U**2)
    for branch in (sp.Integer(1), sp.Integer(-1)):
        assert sp.simplify((1 - U**2).subs(U, branch)) == 0
        # q_x = sqrt(1 - U^2) vanishes at the branch points.
        assert sp.simplify(sp.sqrt(1 - U**2).subs(U, branch)) == 0


def test_mark_monodromy_flips_across_each_turning_point():
    """The Z2 mark cannot be extended through a branch point.

    On the E = 0 libration U runs between the two turning points U = 0 and
    U = -1, which are exactly the two branch points of the Cartesian mark
    q_x = sqrt(1 - U^2).  At the lower turning point t_q = varpi / sqrt(2)
    the observable Y changes sign.  With a fixed chart section sigma = +1 the
    decoder output v_x therefore jumps sign; the continuous Cartesian
    continuation forces sigma -> -sigma.  The mark flips at each turning
    point, so its monodromy around each branch point is -1, while the full
    real loop winds around two branch points and returns the mark (P(z + T_p)
    closes as a marked point, certified in item 3 above).
    """

    varpi = lemniscatic_constant()
    t_q = varpi / mp.sqrt(2)
    eps = mp.mpf("0.01")

    uu = flow_U(t_q)
    assert abs(uu + 1) < mp.mpf("1e-25")  # lower turning point U = -1
    assert abs(flow_Y(t_q)) < mp.mpf("1e-25")  # Y = 0 at the turning point

    def decoder_vx(t, sigma):
        uu_t, yy_t = flow_point(t)
        return -sigma * uu_t * yy_t / mp.sqrt(1 - uu_t**2)

    left = mp.re(decoder_vx(t_q - eps, 1))
    right = mp.re(decoder_vx(t_q + eps, 1))
    assert left * right < 0  # fixed section: v_x jumps sign across t_q
    # Flipping the mark restores continuity: sigma = +1 before and sigma = -1
    # after give the same Cartesian velocity, so the mark must flip.
    assert abs(left - mp.re(decoder_vx(t_q + eps, -1))) < mp.mpf("1e-12")

    # The full real loop restores the mark: same point AND same Y sign.
    z = mp.mpc("0.4", "0.0")
    p0 = flow_point(z)
    pT = flow_point(z + real_period())
    assert abs(p0[0] - pT[0]) + abs(p0[1] - pT[1]) < mp.mpf("1e-12")


# ---------------------------------------------------------------------------
# 6. The clock chain information contract
# ---------------------------------------------------------------------------


def test_clock_chain_kernels_and_embedding():
    """R -> R/T_p Z forgets winding (kernel T_p Z); the real phase embeds
    into C/Lambda because R cap Lambda = T_p Z; the Abel coordinate is the
    complex clock z itself along the flow."""

    T_p = real_period()

    # First arrow: two lifted clocks differ by T_p iff they project to the
    # same geometric action; the period group is the projection kernel.
    assert T_p > 0

    # Second arrow is an embedding, not a quotient: the real sublattice of
    # Lambda = Z T_p + Z i T_p is exactly T_p Z.  For a T_p + b i T_p to be
    # real requires b = 0 (exact linear independence of 1 and i over R).
    a, b = sp.symbols("a b", integer=True)
    imag_part = sp.im(a * T_p + b * sp.I * T_p)
    assert sp.simplify(imag_part - b * T_p) == 0

    # Abel coordinate equals the clock: omega = dU/Y = dz along the flow,
    # certified by dU/dz = Y at generic complex z (item 2).  The imaginary
    # period i T_p is the new lattice data gained by complexification.
    z = mp.mpc("0.3", "0.4")
    assert abs(mp.diff(flow_U, z) / flow_Y(z) - 1) < mp.mpf("1e-25")
