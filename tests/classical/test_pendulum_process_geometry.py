import sympy as sp

from aeg_shakespeare import (
    AlgebraicConstraintSet,
    ProcessSystem,
    constraint_prolongation,
    hyperelliptic_profile,
)


def pendulum_raw_process():
    """Return a dimensionless planar pendulum without angle/trigonometric variables.

    q=(qx,qy) is the constrained bob position, v=(vx,vy) its velocity, and
    lambda_ is the unresolved radial constraint force. Gravity is the constant
    vector -e_y. No theta/sin/cos representation is supplied.
    """

    qx, qy, vx, vy, lambda_ = sp.symbols("qx qy vx vy lambda")
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: lambda_ * qx,
            vy: -1 + lambda_ * qy,
        },
        name="D",
    )
    return qx, qy, vx, vy, lambda_, system


def test_constraint_prolongation_derives_tangency_before_solving_force():
    qx, qy, vx, vy, lambda_, system = pendulum_raw_process()
    rod = qx**2 + qy**2 - 1

    chain = constraint_prolongation(system.derive, rod, order=2)
    assert sp.expand(chain[1] - 2 * (qx * vx + qy * vy)) == 0
    assert lambda_ in chain[2].free_symbols


def test_constraint_force_is_forced_by_preserving_the_rod_relation():
    qx, qy, vx, vy, lambda_, system = pendulum_raw_process()
    rod = qx**2 + qy**2 - 1
    tangent = sp.expand(system.derive(rod) / 2)
    tangent_rate = sp.expand(system.derive(tangent))

    quotient = AlgebraicConstraintSet(
        (qx, qy, vx, vy, lambda_),
        (rod, tangent),
    )
    reduced_rate = quotient.reduce(tangent_rate)
    solutions = sp.solve(sp.Eq(reduced_rate, 0), lambda_)

    assert len(solutions) == 1
    assert sp.expand(solutions[0] - (qy - vx**2 - vy**2)) == 0


def test_energy_is_an_invariant_after_constraint_transport():
    qx, qy, vx, vy, lambda_, raw = pendulum_raw_process()
    lambda_solution = qy - vx**2 - vy**2
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: sp.expand(lambda_solution * qx),
            vy: sp.expand(-1 + lambda_solution * qy),
        },
        name="D",
    )

    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    quotient = AlgebraicConstraintSet((qx, qy, vx, vy), (rod, tangent))
    energy = sp.Rational(1, 2) * (vx**2 + vy**2) + qy

    assert quotient.reduce(system.derive(energy)) == 0


def test_pendulum_process_quotient_forces_a_generic_genus_one_curve():
    qx, qy, vx, vy, E = sp.symbols("qx qy vx vy E")

    # These are relations discovered/maintained before any angle variable is
    # introduced: rigid rod, tangency, and one energy leaf.
    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    energy_leaf = vx**2 + vy**2 - 2 * (E - qy)
    quotient = AlgebraicConstraintSet(
        (qx, qy, vx, vy, E),
        (rod, tangent, energy_leaf),
    )

    U, Y = sp.symbols("U Y")
    curve_polynomial = sp.expand(2 * (E - U) * (1 - U**2))

    # U=qy is the gravity observable and Y=D(U)=vy. Ideal membership proves
    # that the reduced variables satisfy Y^2=P_3(U) without sin/cos input.
    physical_relation = sp.expand(vy**2 - curve_polynomial.subs(U, qy))
    assert quotient.contains(physical_relation)

    profile = hyperelliptic_profile(U, Y, curve_polynomial)
    assert profile.degree == 3
    assert profile.generic_genus == 1
    assert profile.generically_smooth
    assert sp.factor(profile.discriminant) == 64 * (E - 1) ** 2 * (E + 1) ** 2


def test_pendulum_degenerations_are_detected_as_geometry_not_special_function_cases():
    U, Y, E = sp.symbols("U Y E")
    profile = hyperelliptic_profile(U, Y, 2 * (E - U) * (1 - U**2))

    assert sp.simplify(profile.discriminant.subs(E, 1)) == 0
    assert sp.simplify(profile.discriminant.subs(E, -1)) == 0
    assert sp.simplify(profile.discriminant.subs(E, 0)) != 0
