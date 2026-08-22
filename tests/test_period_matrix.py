import math

import pytest
import sympy as sp

from aeg_shakespeare import AbelianCycleSystem, hyperelliptic_profile, lift_square_root_path


def test_cycle_system_rejects_sheet_open_base_loops():
    x, y = sp.symbols("x y")
    curve = hyperelliptic_profile(x, y, x**3 - x)
    loop = tuple(
        1 + 0.2 * complex(math.cos(2 * math.pi * k / 256), math.sin(2 * math.pi * k / 256))
        for k in range(257)
    )
    lifted = lift_square_root_path(curve, loop)

    assert lifted.sheet_multiplier == -1
    with pytest.raises(ValueError, match="closed on the lifted surface"):
        AbelianCycleSystem(curve, (lifted,), (lifted,))


def test_cycle_system_requires_g_pairs():
    x, y = sp.symbols("x y")
    curve = hyperelliptic_profile(x, y, x**5 - x + 1)

    with pytest.raises(ValueError, match="exactly g"):
        AbelianCycleSystem(curve, (), ())
