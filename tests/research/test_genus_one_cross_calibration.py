import sympy as sp

from aeg_shakespeare import hyperelliptic_profile


def test_pendulum_and_quartic_oscillator_share_genus_one_quotient_class():
    E, X, Y = sp.symbols("E X Y")

    pendulum = hyperelliptic_profile(
        X,
        Y,
        2 * (E - X) * (1 - X**2),
    )
    quartic = hyperelliptic_profile(
        X,
        Y,
        2 * E - sp.Rational(1, 2) * X**4,
    )

    # The branch polynomials and degeneration loci differ, so these are not the
    # same equation in disguise. Their smooth generic quotients nevertheless
    # land in the same genus-one class.
    assert pendulum.degree == 3
    assert quartic.degree == 4
    assert pendulum.generic_genus == quartic.generic_genus == 1
    assert sp.factor(pendulum.discriminant) != sp.factor(quartic.discriminant)


def test_genus_is_a_cross_problem_structural_observable_not_a_problem_label():
    E, X, Y = sp.symbols("E X Y")
    profiles = (
        hyperelliptic_profile(X, Y, 2 * (E - X) * (1 - X**2)),
        hyperelliptic_profile(X, Y, 2 * E - sp.Rational(1, 2) * X**4),
    )

    assert {profile.generic_genus for profile in profiles} == {1}
    assert all(profile.generically_smooth for profile in profiles)
