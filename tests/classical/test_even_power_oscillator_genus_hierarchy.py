"""Even-power oscillators: one process family, a genus hierarchy of energy carriers.

Question
--------
If Process Geometry receives only the polynomial process

    D x = p,
    D p = -x^(m-1)

for even ``m``, can the complexity jump from elementary/trigonometric behavior
to elliptic and then higher hyperelliptic behavior be seen first as a change in
the geometry of the energy-leaf algebraic carrier, rather than by naming the
expected special functions in advance?

Primitive data
--------------
For ``m in {2,4,6}``, the test supplies the dimensionless polynomial process and
the polynomial energy candidate

    H = p^2/2 + x^m/m.

No trigonometric, elliptic, theta, hyperelliptic, or Abelian function is supplied
to the algebraic-curve profiler.

Classical lineage
-----------------
Conservative one-dimensional mechanics reduces on an energy leaf to a
quadrature.  Polynomial potentials lead to algebraic integrals; quadratic
potentials give genus-zero reductions, quartic potentials lead to elliptic
integrals, and higher degrees lead naturally to hyperelliptic/Abelian integrals.
For the mechanics background see [Arnold-1989].  For elliptic integrals and
elliptic functions see [DLMF-19], [DLMF-22], and [Whittaker-Watson-1927].  For
Riemann surfaces, Abelian integrals, and higher-genus geometry see
[Forster-1981], [Farkas-Kra-1992], and [Mumford-1983].

Process Geometry reconstruction
---------------------------
We first verify the caller-supplied energy candidate directly from the process.
On ``H=E`` we obtain

    p^2 = 2E - (2/m) x^m.

Only then is the energy-leaf relation viewed as ``Y^2=P_m(X)`` and profiled by
its degree/discriminant. For a square-free hyperelliptic model
``y^2=P_d(x)``, the smooth projective completion has generic genus
``floor((d-1)/2)`` in the cases used here.

**Process Geometry interpretation.** The function-language hierarchy is read
as a shadow of energy-leaf carrier geometry produced by the process. This is a
representation interpretation, not a claim that genus alone measures all
process complexity. No continuation task, semantic quotient, or decoder is
constructed in this file.

Calibration statement
---------------------
Passing this file certifies:

1. the supplied ``H`` candidate is an exact process invariant for m=2,4,6;
2. the quartic energy carrier is generically genus one and has discriminant
   ``-256 E^3`` in the chosen normalization;
3. the m=2,4,6 energy-carrier family has generic genera 0,1,2 respectively;
4. those classifications are obtained without a named special-function input.

Proof map
---------
``test_even_power_oscillator_energy_*`` checks the invariant.
``test_quartic_oscillator_*`` checks the quartic carrier and discriminant.
``test_even_power_oscillators_generate_*`` checks the genus ladder.
``test_harmonic_quartic_sextic_*`` checks that the profiler receives only the
algebraic energy relation.

Boundary
--------
The tests do not construct explicit period matrices, Jacobians, theta
functions, or analytic uniformizations. They also do not prove a universal
classification of ODEs by genus. They certify only the displayed algebraic
energy-leaf family and its generic curve genera. In particular, an algebraic
carrier is not thereby an exact task-semantic quotient: future-equivalence,
information loss, and reconstruction are not declared here.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.

[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
“Elliptic Integrals”, https://dlmf.nist.gov/19 .

[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
“Jacobian Elliptic Functions”, https://dlmf.nist.gov/22 .

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Mumford-1983] D. Mumford, *Tata Lectures on Theta I*, Birkhauser, 1983.
DOI: 10.1007/978-1-4899-2843-6.

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson,
*A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927,
Chapters XX-XXII.
"""

import sympy as sp

from process_geometry.analysis.algebraic import hyperelliptic_profile
from process_geometry.presentation.constraints import AlgebraicConstraintSet
from process_geometry.process.local import ProcessSystem


def even_power_oscillator(power: int):
    """Return the polynomial process and its energy candidate for even power."""

    if power < 2 or power % 2:
        raise ValueError("power must be an even integer >= 2")
    x, p = sp.symbols("x p")
    system = ProcessSystem(
        (x, p),
        {
            x: p,
            p: -x ** (power - 1),
        },
        name="D",
    )
    energy = sp.Rational(1, 2) * p**2 + sp.Rational(1, power) * x**power
    return x, p, system, energy


def test_even_power_oscillator_energy_candidate_is_exact_invariant_family():
    # GIVEN / ASSERT: the process itself certifies the energy invariant.
    for power in (2, 4, 6):
        x, p, system, energy = even_power_oscillator(power)
        assert sp.expand(system.derive(energy)) == 0


def test_quartic_oscillator_forces_genus_one_without_elliptic_function_input():
    x, p, system, energy = even_power_oscillator(4)
    E, X, Y = sp.symbols("E X Y")

    # DISCOVER: pass to one exact energy leaf.
    energy_leaf = sp.expand(energy - E)
    quotient = AlgebraicConstraintSet((x, p, E), (energy_leaf,))
    polynomial = sp.expand(2 * E - sp.Rational(1, 2) * X**4)
    assert quotient.contains(p**2 - polynomial.subs(X, x))

    # CLASSICAL SHADOW: the square-free quartic model is genus one.
    profile = hyperelliptic_profile(X, Y, polynomial)
    assert profile.degree == 4
    assert profile.generic_genus == 1
    assert sp.factor(profile.discriminant) == -256 * E**3


def test_even_power_oscillators_generate_a_genus_hierarchy_of_energy_carriers():
    E, X, Y = sp.symbols("E X Y")

    profiles = {}
    for power in (2, 4, 6):
        polynomial = sp.expand(2 * E - sp.Rational(2, power) * X**power)
        profiles[power] = hyperelliptic_profile(X, Y, polynomial)

    # ASSERT: one primitive process family yields a 0 -> 1 -> 2 genus ladder.
    assert profiles[2].generic_genus == 0
    assert profiles[4].generic_genus == 1
    assert profiles[6].generic_genus == 2
    assert all(profile.generically_smooth for profile in profiles.values())


def test_harmonic_quartic_sextic_function_complexity_is_not_named_in_advance():
    E, X, Y = sp.symbols("E X Y")
    expected = {2: 0, 4: 1, 6: 2}

    for power, genus in expected.items():
        # GIVEN: only the reduced algebraic relation, no special-function label.
        polynomial = 2 * E - sp.Rational(2, power) * X**power
        profile = hyperelliptic_profile(X, Y, polynomial)
        assert profile.generic_genus == genus
