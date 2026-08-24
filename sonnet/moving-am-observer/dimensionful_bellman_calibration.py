"""Dimensionful Bellman calibration for moving-observer chart invariance."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import mpmath as mp


# A private context is part of the certificate contract.  Research tests in the
# same interpreter legitimately use other precisions; mutating ``mp.mp.dps``
# would make this calibration depend on collection/import order.
MATH = mp.mp.clone()
MATH.dps = 60
U_START = MATH.mpf("1")
U_END = MATH.mpf("-1")
DEFAULT_LENGTH = MATH.mpf("3.5")
DEFAULT_SPEED = MATH.mpf("1.4")


@dataclass(frozen=True)
class Dimension:
    """Length/time exponent pair used by the executable unit audit."""

    length: int = 0
    time: int = 0

    def __mul__(self, other: "Dimension") -> "Dimension":
        return Dimension(self.length + other.length, self.time + other.time)

    def __truediv__(self, other: "Dimension") -> "Dimension":
        return Dimension(self.length - other.length, self.time - other.time)

    def __pow__(self, power: int) -> "Dimension":
        return Dimension(self.length * power, self.time * power)


DIMENSIONLESS = Dimension()
LENGTH = Dimension(length=1)
TIME = Dimension(time=1)
SPEED = LENGTH / TIME


def w_of_u(u):
    """Nonlinear A/M re-presentation with everywhere-positive derivative."""

    return u + u**3


def u_of_w(w):
    lower, upper = U_END, U_START
    for _ in range(220):
        middle = (lower + upper) / 2
        if w_of_u(middle) < w:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def u_rate(u, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    """Rate of ``u=(x-Vt)/L`` for the declared physical process."""

    return speed / length * (u**2 - 2)


def w_rate(w, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    u = u_of_w(w)
    return (1 + 3 * u**2) * u_rate(u, length=length, speed=speed)


def clock_u(u, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    """Physical elapsed time, in units carried by ``L/V``."""

    return length / speed * MATH.quad(
        lambda coordinate: 1 / (2 - coordinate**2),
        [u, U_START],
    )


def clock_w(w, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    """The same clock independently integrated in the nonlinear chart."""

    return MATH.quad(
        lambda coordinate: 1 / (-w_rate(
            coordinate, length=length, speed=speed
        )),
        [w, w_of_u(U_START)],
    )


def invert_clock(target, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    lower, upper = U_END, U_START
    for _ in range(220):
        middle = (lower + upper) / 2
        if clock_u(middle, length=length, speed=speed) > target:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def equal_clock_sections(count, *, length=DEFAULT_LENGTH, speed=DEFAULT_SPEED):
    total = clock_u(U_END, length=length, speed=speed)
    return tuple(
        invert_clock(
            total * index / (count - 1),
            length=length,
            speed=speed,
        )
        for index in range(count)
    )


def equal_u_sections(count):
    return tuple(
        U_START + (U_END - U_START) * index / (count - 1)
        for index in range(count)
    )


def equal_w_sections_as_u(count):
    w_start, w_end = w_of_u(U_START), w_of_u(U_END)
    return tuple(
        u_of_w(w_start + (w_end - w_start) * index / (count - 1))
        for index in range(count)
    )


def optimal_resettable_first_hit_task(
    boundary_clocks,
    weights=(1, 1, 1, 1),
):
    """Finite alphabetic Bellman problem with additive physical-time cost."""

    @lru_cache(maxsize=None)
    def solve(lower, upper):
        if upper - lower <= 1:
            return MATH.mpf(0), None
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
        _value, cut = solve(lower, upper)
        if cut is None:
            return None
        return cut, policy(lower, cut), policy(cut, upper)

    value, _cut = solve(0, len(weights))
    return value, policy(0, len(weights))


__all__ = [
    "DEFAULT_LENGTH",
    "DEFAULT_SPEED",
    "DIMENSIONLESS",
    "Dimension",
    "LENGTH",
    "SPEED",
    "TIME",
    "clock_u",
    "clock_w",
    "equal_clock_sections",
    "equal_u_sections",
    "equal_w_sections_as_u",
    "optimal_resettable_first_hit_task",
    "u_of_w",
    "u_rate",
    "w_of_u",
    "w_rate",
]
