"""Replay the exact local Bessel-to-Airy chart certificate.

This deliberately checks only the analytic germ, scale solve, and local
residual.  It does not claim contour localization or a uniform asymptotic
error bound for the Bessel integral.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    theta, delta = sp.symbols("theta delta")
    h, u, xi = sp.symbols("h u xi")

    phase = (1 + delta) * sp.sin(theta) - theta

    critical_jet = {
        "d_theta": sp.diff(phase, theta).subs({theta: 0, delta: 0}),
        "d_theta_2": sp.diff(phase, theta, 2).subs({theta: 0, delta: 0}),
        "d_theta_3": sp.diff(phase, theta, 3).subs({theta: 0, delta: 0}),
        "d_theta_d_delta": sp.diff(phase, theta, delta).subs(
            {theta: 0, delta: 0}
        ),
    }
    assert critical_jet == {
        "d_theta": 0,
        "d_theta_2": 0,
        "d_theta_3": -1,
        "d_theta_d_delta": 1,
    }

    exponent_matrix = sp.Matrix([[3, 0], [1, 1]])
    weights = exponent_matrix.inv() * sp.Matrix([1, 1])
    assert weights == sp.Matrix([sp.Rational(1, 3), sp.Rational(2, 3)])
    assert exponent_matrix.rank() == 2
    assert exponent_matrix.det() == 3

    # h = nu^(-1/3), hence nu = h^(-3), theta = h*u,
    # delta = h^2*xi.  Expanding in h avoids fractional symbolic powers.
    normalized = sp.series(
        h ** -3 * phase.subs({theta: h * u, delta: h**2 * xi}),
        h,
        0,
        5,
    ).removeO().expand()

    leading = xi * u - u**3 / 6
    residual_2 = u**5 / 120 - xi * u**3 / 6
    residual_4 = -u**7 / 5040 + xi * u**5 / 120
    expected = leading + h**2 * residual_2 + h**4 * residual_4
    assert sp.expand(normalized - expected) == 0

    certificate_path = Path(__file__).with_name("bessel_transition_certificate.json")
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    assert certificate["scale_weights"] == {"theta": "1/3", "delta": "2/3"}
    assert certificate["rank"] == exponent_matrix.rank()
    assert certificate["determinant"] == exponent_matrix.det()
    assert certificate["surreal_runtime"] == "unnecessary"

    print(
        json.dumps(
            {
                "status": "pass",
                "critical_jet": {key: str(value) for key, value in critical_jet.items()},
                "weights": [str(value) for value in weights],
                "rank": int(exponent_matrix.rank()),
                "determinant": int(exponent_matrix.det()),
                "normalized_through_h4": str(normalized),
                "claim_boundary": certificate["claim_boundary"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
