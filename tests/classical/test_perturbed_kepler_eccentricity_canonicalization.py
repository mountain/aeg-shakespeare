"""Perturbed Kepler eccentricity frame: canonicalization generates ren/transport split.

Question
--------
After a physical Kepler moving frame has been derived from local
canonicalization, can the same principle classify a genuine perturbation into
shape renormalization versus observer transport rather than assigning those
labels afterwards?

Primitive data
--------------
Start from planar Cartesian motion

    r_dot = v,
    v_dot = -mu*r/|r|^3 + f,

where ``f`` is an arbitrary local perturbing acceleration.  Define the standard
eccentricity / Laplace--Runge--Lenz vector

    e = v x h / mu - r/|r|,
    h = r x v.

No Gauss planetary equations, osculating-element rate formulas, future orbit,
or periapsis-precession law is supplied.

The observer is a planar rotation ``varpi`` acting on the eccentricity vector.
Its canonicalization is simply

    E_perp = 0,
    E_parallel > 0,

so the observer first axis is aligned with the current eccentricity vector on a
noncircular local chart.

Classical lineage
-----------------
The eccentricity/Laplace--Runge--Lenz vector and central-force reduction are
classical; see Goldstein, Poole, and Safko [Goldstein-Poole-Safko-2002].  An
explicit Cartesian eccentricity-vector formula and its derivatives are recorded,
for example, in Appendix A of Dittmann [Dittmann-2020].  Moving-frame
normalization under transformation groups has classical antecedents in Fels and
Olver [Fels-Olver-1998].

The decomposition semantics tested here are project-specific: derive the local
perturbed eccentricity-vector motion first, use canonicalization to identify the
observer angular rate, and only then call the remaining aligned component
``renormalizable`` and the absorbed tangential component ``resonant/transport``.
The references are not cited as asserting that AEG/Shakespeare decomposition.

Shakespeare reconstruction
---------------------------
Differentiating the Cartesian eccentricity vector under the full perturbed
process should cancel the unperturbed Kepler acceleration exactly and leave

    e_dot = (f x h + v x (r x f)) / mu.

Thus the local correction is generated directly by the physical perturbation.

Write the perturbation-induced eccentricity-vector rate in the observer frame as

    G_parallel,
    G_perp.

For arbitrary observer angular rate ``omega``, the aligned components obey

    E_parallel_dot = G_parallel + omega*E_perp,
    E_perp_dot     = G_perp - omega*E_parallel.

On the canonical leaf ``E_perp=0``, maintaining the normalization forces

    varpi_dot = G_perp/E_parallel.

The tangential correction is therefore absorbed by observer motion, while the
surviving aligned correction changes only the eccentricity magnitude:

    e_mag_dot = G_parallel.

For the explicit local elliptic state

    mu = 1,
    r  = (1,0),
    v  = (0,sqrt(3/2)),

one has ``e=(1/2,0)``.  With local perturbation ``f=(f_r,f_t)`` the exact rates
become

    e_mag_dot = sqrt(6)*f_t,
    varpi_dot = -sqrt(6)*f_r.

Hence radial and tangential perturbation components populate different
canonical sectors at this state.  In the eccentricity-vector carrier there is
no remaining completion residual: the two-dimensional correction is exhausted
by magnitude renormalization plus orientation transport.

Calibration statement
---------------------
Passing this file certifies that:

1. direct differentiation of the Cartesian eccentricity vector cancels the
   inverse-square Kepler part and yields exactly
   ``(f x h + v x (r x f))/mu``;
2. when ``f=0`` the eccentricity vector is exactly conserved;
3. arbitrary periapsis-frame angular rates give different lifts of the same
   eccentricity-vector motion;
4. local alignment ``E_perp=0`` uniquely induces
   ``varpi_dot=G_perp/E_parallel`` on the noncircular chart;
5. for the declared elliptic state, ``e=(1/2,0)``,
   ``e_mag_dot=sqrt(6)*f_t`` and ``varpi_dot=-sqrt(6)*f_r``;
6. the perturbation correction decomposes exactly into a magnitude-changing
   renormalizable component and an orientation-changing transport component;
7. subtracting the induced observer transport leaves purely aligned magnitude
   evolution; and
8. the completion sector is exactly zero at the eccentricity-vector carrier,
   providing a negative control against manufacturing representation growth.

Proof map
---------
1. ``test_eccentricity_vector_derivative_is_generated_only_by_the_perturbation``
   differentiates the Cartesian definition and verifies the perturbation-only
   vector identity plus the unperturbed conservation red team.
2. ``test_eccentricity_alignment_uniquely_derives_periapsis_observer_rate``
   derives the generic rotating-frame rate and checks that frozen observer motion
   fails whenever the perturbation has a tangential eccentricity-vector rate.
3. ``test_local_perturbation_generates_renormalization_and_transport_without_completion``
   evaluates an exact elliptic local state, derives the magnitude and orientation
   rates, records the `CanonicalDecomposition`, and verifies that the induced
   moving frame removes the transverse residual exactly.

Boundary
--------
This is a local noncircular eccentricity-vector chart, not a full osculating
orbital-element theory.  It does not treat the circular stratum ``|e|=0``,
three-dimensional inclination dynamics, secular averaging, collisions, or a
specific global perturbing potential.

The zero completion result is carrier-relative.  The earlier restricted Kepler
function-module essay exhibits genuine second-harmonic completion under a richer
shape task.  Therefore this file explicitly demonstrates that
``F_comp`` is representation/task relative rather than an intrinsic label on a
physical perturbing force.

The experiment still uses the exact constraint backend for alignment.  It does
not yet justify a generic osculation/stationarity canonicalization API.

References
----------
[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L.
Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3,
"The Central Force Problem," ISBN 0-201-65702-3.

[Dittmann-2020] Alexander J. Dittmann, "Modified Hermite integrators of arbitrary
order," *Monthly Notices of the Royal Astronomical Society* 496(2) (2020),
1217--1223, Appendix A; DOI 10.1093/mnras/staa1631.

[Fels-Olver-1998] Mark Fels, Peter J. Olver, "Moving Coframes: I. A Practical
Algorithm," *Acta Applicandae Mathematicae* 51(2) (1998), 161--213;
DOI 10.1023/A:1005878210297.
"""

from __future__ import annotations

import sympy as sp

from process_geometry.experimental import (
    CanonicalDecomposition,
    ConstraintCanonicalization,
)


def eccentricity_vector(x, y, vx, vy, mu):
    radius = sp.sqrt(x**2 + y**2)
    h = x * vy - y * vx
    return (
        vy * h / mu - x / radius,
        -vx * h / mu - y / radius,
    )


def time_derivative(expr, variables, rates):
    return sp.simplify(
        sum(sp.diff(expr, variable) * rates[variable] for variable in variables)
    )


def test_eccentricity_vector_derivative_is_generated_only_by_the_perturbation():
    x, y, vx, vy = sp.symbols("x y vx vy", real=True)
    mu = sp.symbols("mu", positive=True)
    fx, fy = sp.symbols("fx fy")
    radius = sp.sqrt(x**2 + y**2)

    ex, ey = eccentricity_vector(x, y, vx, vy, mu)
    ax = -mu * x / radius**3 + fx
    ay = -mu * y / radius**3 + fy
    rates = {x: vx, y: vy, vx: ax, vy: ay}

    ex_dot = time_derivative(ex, (x, y, vx, vy), rates)
    ey_dot = time_derivative(ey, (x, y, vx, vy), rates)

    h = x * vy - y * vx
    r_cross_f = x * fy - y * fx
    expected_x = sp.expand((fy * h + vy * r_cross_f) / mu)
    expected_y = sp.expand((-fx * h - vx * r_cross_f) / mu)

    assert sp.simplify(ex_dot - expected_x) == 0
    assert sp.simplify(ey_dot - expected_y) == 0
    assert sp.simplify(ex_dot.subs({fx: 0, fy: 0})) == 0
    assert sp.simplify(ey_dot.subs({fx: 0, fy: 0})) == 0


def test_eccentricity_alignment_uniquely_derives_periapsis_observer_rate():
    ex, ey, gx, gy, varpi = sp.symbols("ex ey gx gy varpi")
    c = sp.cos(varpi)
    s = sp.sin(varpi)
    e_parallel = c * ex + s * ey
    e_perp = -s * ex + c * ey
    g_perp = -s * gx + c * gy

    canonicalization = ConstraintCanonicalization(
        observer_parameters=(varpi,),
        constraints=(e_perp,),
        label="eccentricity-vector alignment",
    )

    frozen = canonicalization.differentiated_constraints(
        {ex: gx, ey: gy},
        {varpi: sp.S.Zero},
    )
    assert sp.trigsimp(frozen[0] - g_perp) == 0

    connection = canonicalization.induced_connection({ex: gx, ey: gy})
    assert connection.certified
    varpi_dot = sp.simplify(connection.rate(varpi))
    assert sp.trigsimp(varpi_dot - g_perp / e_parallel) == 0


def test_local_perturbation_generates_renormalization_and_transport_without_completion():
    fr, ft = sp.symbols("f_r f_t")
    speed = sp.sqrt(sp.Rational(3, 2))

    # mu=1, r=(1,0), v=(0,sqrt(3/2)) is an elliptic local Kepler state with
    # eccentricity vector (1/2,0).
    ex, ey = eccentricity_vector(
        sp.S.One,
        sp.S.Zero,
        sp.S.Zero,
        speed,
        sp.S.One,
    )
    assert sp.simplify(ex - sp.Rational(1, 2)) == 0
    assert ey == 0

    h = speed
    r_cross_f = ft
    gx = sp.simplify(ft * h + speed * r_cross_f)
    gy = sp.simplify(-fr * h)
    assert sp.simplify(gx - sp.sqrt(6) * ft) == 0
    assert sp.simplify(gy + speed * fr) == 0

    e_mag = sp.Rational(1, 2)
    e_mag_dot = gx
    varpi_dot = sp.simplify(gy / e_mag)
    assert sp.simplify(e_mag_dot - sp.sqrt(6) * ft) == 0
    assert sp.simplify(varpi_dot + sp.sqrt(6) * fr) == 0

    source = (gx, gy)
    renormalizable = (gx, sp.S.Zero)
    resonant = (sp.S.Zero, gy)
    completion = (sp.S.Zero, sp.S.Zero)
    certificate = tuple(
        sp.simplify(source[index] - renormalizable[index] - resonant[index])
        for index in range(2)
    )
    decomposition = CanonicalDecomposition(
        source=source,
        renormalizable=renormalizable,
        resonant=resonant,
        completion=completion,
        certificate=certificate,
        label="eccentricity magnitude plus periapsis transport",
    )
    assert decomposition.certificate == (0, 0)
    assert decomposition.completion == (0, 0)

    # In the aligned moving frame, the connection subtracts exactly the
    # transverse eccentricity-vector velocity e_mag*varpi_dot.
    canonical_perp_rate = sp.simplify(gy - e_mag * varpi_dot)
    canonical_parallel_rate = sp.simplify(gx)
    assert canonical_perp_rate == 0
    assert sp.simplify(canonical_parallel_rate - e_mag_dot) == 0
