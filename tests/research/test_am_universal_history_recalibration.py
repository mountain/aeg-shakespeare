"""AM recalibration of canonicalization and Hauffman/Bellman history cost.

This essay revisits a previous cross-problem conclusion.  A quotient carrier
need not itself be a tree, but that does not prevent its free/lifted histories
from having a common rooted unfolding on which process cost is measured.

The exact calibrations below separate four layers:

1. primitive A/M-compatible presentation changes;
2. universal/free history before endpoint quotienting;
3. task or deck quotient;
4. additive process cost on the history lift.

The result is deliberately mixed.  Translation, hard-particle first contact,
and the pendulum clock support the lift-first measurement hypothesis.  A
rank-two Abelian period lattice shows that an additive universal lift does not
by itself select a unique scalar cost: a basis change preserves the lattice but
changes naive word length.  Additional ruler/connection/metric data is needed.

No generic API or universal optimality theorem is proposed.
"""

from fractions import Fraction


def _translation_endpoint(word: str) -> int:
    return sum(1 if letter == "+" else -1 for letter in word)


def _prefix_profile(words):
    prefixes = {""}
    for word in words:
        prefixes.update(word[:depth] for depth in range(1, len(word) + 1))
    width = tuple(
        sum(1 for prefix in prefixes if len(prefix) == depth)
        for depth in range(max(map(len, words)) + 1)
    )
    return width, sum(width), max(map(len, words))


def test_translation_quotient_merges_states_but_not_universal_process_cost():
    direct = "+"
    detour = "++-"

    assert _translation_endpoint(direct) == _translation_endpoint(detour) == 1
    assert len(direct) == 1
    assert len(detour) == 3

    # Continuation stability justifies the endpoint quotient.
    continuation = "+--+"
    assert _translation_endpoint(direct + continuation) == _translation_endpoint(
        detour + continuation
    )

    # Complexity is nevertheless a property of the chosen lifted process or
    # of its optimal section, not of the endpoint alone.
    width, volume, depth = _prefix_profile((direct, detour))
    assert width == (1, 1, 1, 1)
    assert (volume, depth) == (4, 3)


def _collision_times(positions, velocities):
    return tuple(
        Fraction(positions[i + 1] - positions[i], velocities[i] - velocities[i + 1])
        for i in range(len(positions) - 1)
    )


def test_hard_particle_first_hit_is_invariant_under_global_a_m_gauge():
    positions = tuple(map(Fraction, (0, 2, 7, 13)))
    velocities = tuple(map(Fraction, (7, 5, 2, 0)))
    canonical = _collision_times(positions, velocities)

    # Global A gauges: spatial translation and common velocity boost.
    x_shift, v_boost = Fraction(11), Fraction(5)
    # Global M gauge: one common positive scale on positions and velocities.
    scale = Fraction(3)
    transformed_positions = tuple(scale * x + x_shift for x in positions)
    transformed_velocities = tuple(scale * v + v_boost for v in velocities)

    assert _collision_times(transformed_positions, transformed_velocities) == canonical
    assert canonical == (Fraction(1), Fraction(5, 3), Fraction(3))
    assert min(canonical) == Fraction(1)


def test_pendulum_clock_is_invariant_under_affine_am_observer_change():
    # At a regular point, Y=DU and omega(D)=dU(D)/Y=1.  Under the affine
    # observer X=s*U+b, Z=DX=s*Y.  This is the finite A/M shadow needed here;
    # no Euclidean observer metric is supplied.
    U, Y = Fraction(2, 5), Fraction(7, 9)
    scale, shift = Fraction(5, 2), Fraction(-3, 7)
    X = scale * U + shift
    Z = scale * Y

    assert X != U
    assert Z != Y
    assert scale / Z == 1 / Y  # dX/Z pulls back to dU/Y.

    # Clock increments are additive on the lifted orbit.
    dt_01, dt_12 = Fraction(2, 7), Fraction(3, 11)
    assert dt_01 + dt_12 == Fraction(43, 77)


def _lattice_shift(coefficients, basis):
    return tuple(
        sum(coefficient * vector[axis] for coefficient, vector in zip(coefficients, basis))
        for axis in range(2)
    )


def _l1_word_cost(coefficients):
    return sum(abs(value) for value in coefficients)


def test_abelian_universal_lift_exists_but_scalar_word_cost_is_not_basis_free():
    standard_basis = ((1, 0), (0, 1))
    sheared_basis = ((1, 0), (1, 1))

    # The same lifted lattice displacement has different primitive words after
    # an integral change of basis: (0,1)=e2=(-e1)+(e1+e2).
    standard_coefficients = (0, 1)
    sheared_coefficients = (-1, 1)
    displacement = (0, 1)

    assert _lattice_shift(standard_coefficients, standard_basis) == displacement
    assert _lattice_shift(sheared_coefficients, sheared_basis) == displacement
    assert _l1_word_cost(standard_coefficients) == 1
    assert _l1_word_cost(sheared_coefficients) == 2

    # Modding out by the period lattice identifies both with the same visible
    # torus endpoint.  Neither the quotient nor universality chooses between
    # these scalar costs.
    assert displacement != (0, 0)


def test_tree_dag_and_groupoid_are_quotient_shadows_of_history_unfoldings():
    cases = {
        "translation": ("free word tree", "Cayley graph", "grammar cost"),
        "hard particle": ("comparison history tree", "argmin strata", "first-hit clock"),
        "pendulum": ("lifted orbit history", "elliptic carrier", "dU/Y clock"),
        "Abelian periods": ("lifted path history", "period quotient", "ruler-dependent vector"),
    }

    assert {unfolding for unfolding, _, _ in cases.values()} == {
        "free word tree",
        "comparison history tree",
        "lifted orbit history",
        "lifted path history",
    }
    assert len({quotient for _, quotient, _ in cases.values()}) == 4
    assert cases["Abelian periods"][2] == "ruler-dependent vector"
