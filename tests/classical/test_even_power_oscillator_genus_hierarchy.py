import sympy as sp

from aeg_shakespeare import AlgebraicConstraintSet, ProcessSystem, hyperelliptic_profile


def even_power_oscillator(power: int):
    """Dimensionless Hamiltonian H=p^2/2 + x^power/power for even power."""

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


def test_even_power_oscillator_energy_is_discovered_process_invariant_family():
    for power in (2, 4, 6):
        x, p, system, energy = even_power_oscillator(power)
        assert sp.expand(system.derive(energy)) == 0


def test_quartic_oscillator_forces_genus_one_without_elliptic_function_input():
    x, p, system, energy = even_power_oscillator(4)
    E, X, Y = sp.symbols("E X Y")

    energy_leaf = sp.expand(energy - E)
    quotient = AlgebraicConstraintSet((x, p, E), (energy_leaf,))
    polynomial = sp.expand(2 * E - sp.Rational(1, 2) * X**4)

    assert quotient.contains(p**2 - polynomial.subs(X, x))

    profile = hyperelliptic_profile(X, Y, polynomial)
    assert profile.degree == 4
    assert profile.generic_genus == 1
    assert sp.factor(profile.discriminant) == -256 * E**3


def test_even_power_oscillators_generate_a_genus_hierarchy_from_process_quotients():
    E, X, Y = sp.symbols("E X Y")

    profiles = {}
    for power in (2, 4, 6):
        polynomial = sp.expand(2 * E - sp.Rational(2, power) * X**power)
        profiles[power] = hyperelliptic_profile(X, Y, polynomial)

    assert profiles[2].generic_genus == 0
    assert profiles[4].generic_genus == 1
    assert profiles[6].generic_genus == 2
    assert all(profile.generically_smooth for profile in profiles.values())


def test_harmonic_quartic_sextic_function_complexity_is_not_named_in_advance():
    E, X, Y = sp.symbols("E X Y")
    expected = {2: 0, 4: 1, 6: 2}

    for power, genus in expected.items():
        # The only input is the reduced algebraic process relation on an energy
        # leaf. No trigonometric, elliptic, or hyperelliptic function name is
        # supplied to the profile routine.
        polynomial = 2 * E - sp.Rational(2, power) * X**power
        profile = hyperelliptic_profile(X, Y, polynomial)
        assert profile.generic_genus == genus
