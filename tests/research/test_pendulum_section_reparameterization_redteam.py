"""End-to-end red team for lift-first pendulum clock optimization.

Pre-registered prediction: on one regular half of the E=0 libration orbit,
equal-clock first-hit sections must give the same stopping policy and Bellman
value in U and in X=U^3. Equal-coordinate sections are the negative control.
"""

from functools import lru_cache

import mpmath as mp


mp.mp.dps = 40
U_START = mp.mpf("-0.9")
U_END = mp.mpf("-0.1")


def orbit_velocity(u):
    return mp.sqrt(2 * (-u) * (1 - u * u))


def x_of_u(u):
    return u**3


def u_of_x(x):
    return -((-x) ** (mp.mpf(1) / 3))


def x_velocity(x):
    u = u_of_x(x)
    return 3 * u * u * orbit_velocity(u)


def clock_u(u):
    return mp.quad(lambda coordinate: 1 / orbit_velocity(coordinate), [U_START, u])


def clock_x(x):
    return mp.quad(
        lambda coordinate: 1 / x_velocity(coordinate),
        [x_of_u(U_START), x],
    )


def invert_monotone(function, target, lower, upper, iterations=150):
    for _ in range(iterations):
        middle = (lower + upper) / 2
        if function(middle) < target:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def equal_clock_u_sections(count):
    total = clock_u(U_END)
    return tuple(
        invert_monotone(clock_u, total * index / (count - 1), U_START, U_END)
        for index in range(count)
    )


def optimal_resettable_first_hit_task(boundary_clocks, weights=(8, 4, 2, 1)):
    """Costed alphabetic task whose queries reset and wait to one boundary."""

    @lru_cache(maxsize=None)
    def solve(lower, upper):
        if upper - lower <= 1:
            return mp.mpf(0), None
        mass = sum(weights[lower:upper])
        candidates = []
        for cut in range(lower + 1, upper):
            left_mass = sum(weights[lower:cut])
            right_mass = sum(weights[cut:upper])
            left_value, _ = solve(lower, cut)
            right_value, _ = solve(cut, upper)
            value = boundary_clocks[cut] + (
                left_mass * left_value + right_mass * right_value
            ) / mass
            candidates.append((value, cut))
        return min(candidates, key=lambda candidate: (candidate[0], candidate[1]))

    def policy(lower, upper):
        _, cut = solve(lower, upper)
        if cut is None:
            return None
        return cut, policy(lower, cut), policy(cut, upper)

    value, _ = solve(0, len(weights))
    return value, policy(0, len(weights))


def test_equal_clock_sections_preserve_the_complete_stopping_optimization():
    u_sections = equal_clock_u_sections(5)
    x_sections = tuple(x_of_u(u) for u in u_sections)
    u_clocks = tuple(clock_u(u) for u in u_sections)
    x_clocks = tuple(clock_x(x) for x in x_sections)

    assert max(abs(left - right) for left, right in zip(u_clocks, x_clocks)) < mp.mpf(
        "1e-30"
    )

    u_value, u_policy = optimal_resettable_first_hit_task(u_clocks)
    x_value, x_policy = optimal_resettable_first_hit_task(x_clocks)
    assert abs(u_value - x_value) < mp.mpf("1e-30")
    assert u_policy == x_policy
    assert u_policy == (1, None, (2, None, (3, None, None)))


def test_equal_coordinate_sections_are_a_required_negative_control():
    count = 5
    equal_u = tuple(
        U_START + (U_END - U_START) * index / (count - 1)
        for index in range(count)
    )
    x_start, x_end = x_of_u(U_START), x_of_u(U_END)
    equal_x_as_u = tuple(
        u_of_x(x_start + (x_end - x_start) * index / (count - 1))
        for index in range(count)
    )

    equal_u_clocks = tuple(clock_u(u) for u in equal_u)
    equal_x_clocks = tuple(clock_u(u) for u in equal_x_as_u)
    equal_u_gaps = tuple(
        equal_u_clocks[index + 1] - equal_u_clocks[index]
        for index in range(count - 1)
    )
    equal_x_gaps = tuple(
        equal_x_clocks[index + 1] - equal_x_clocks[index]
        for index in range(count - 1)
    )

    assert max(
        abs(left - right) for left, right in zip(equal_u_gaps, equal_x_gaps)
    ) > mp.mpf("0.1")

    u_value, _ = optimal_resettable_first_hit_task(equal_u_clocks)
    x_value, _ = optimal_resettable_first_hit_task(equal_x_clocks)
    assert abs(u_value - x_value) > mp.mpf("0.1")

