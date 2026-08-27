#!/usr/bin/env python3
"""Independent replay of the frozen S2 compiler controls.

The script imports the implementation as a black box, makes no edits to it,
and keeps evaluator-only expected scales in this benchmark workstream.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import sys

import sympy as sp


WORKSTREAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSTREAMS / "scale_compiler"))
sys.path.insert(0, str(WORKSTREAMS / "scale_analytic_germ"))

from analytic_germ_adapter import (  # noqa: E402
    GermBudget,
    LocalCoordinate,
    adapt_phase_to_germ,
    adapt_registered_special_function,
    germ_summary,
    lower_registered_special_function,
)
from scale_compiler import Scale  # noqa: E402


def main() -> None:
    N = sp.Symbol("N", positive=True, integer=True)
    z = sp.Symbol("z", real=True)
    raw = sp.besselj(N, N * z)

    e2e = adapt_registered_special_function(
        raw,
        large_parameter=N,
        local_parameter=z,
        large_parameter_scale=Scale(1),
        budget=GermBudget(max_total_degree=5),
    )
    assert e2e.local_chart_certified
    assert not e2e.uniform_integral_certified
    assert e2e.bridge.certificate is not None
    assert e2e.germ is not None and e2e.germ.certificate is not None
    bridge = e2e.bridge.certificate
    germ = e2e.germ.certificate
    assert not bridge.contains_scale_hint
    assert not bridge.contains_normal_form_hint
    assert germ.balance.scales == {
        "theta": Scale(Fraction(-1, 3)),
        "delta": Scale(Fraction(-2, 3)),
    }
    assert all(passed for _, passed in germ.checks)
    unresolved = [item.name for item in bridge.obligations if not item.discharged]
    assert unresolved == ["full-reconstruction", "uniform-error"]

    registry_source = (
        WORKSTREAMS
        / "scale_analytic_germ"
        / "analytic_germ_adapter"
        / "representation_bridge.py"
    ).read_text(encoding="utf-8")
    forbidden_literals = ["-1/3", "-2/3", "Airy", "airy"]
    assert not any(literal in registry_source for literal in forbidden_literals)

    s, delta = sp.symbols("s delta")
    cubic = adapt_phase_to_germ(
        N * (2 * s**3 + 5 * delta * s + 7 * s**4),
        coordinates=(
            LocalCoordinate(s, 0, "s", "state"),
            LocalCoordinate(delta, 0, "delta", "parameter"),
        ),
        fixed_scales={"N": Scale(1)},
        budget=GermBudget(max_total_degree=5),
        require_degenerate=True,
    )
    assert cubic.certified and cubic.certificate is not None
    assert cubic.certificate.balance.scales == {
        "s": Scale(Fraction(-1, 3)),
        "delta": Scale(Fraction(-2, 3)),
    }
    assert cubic.certificate.known_residual_orders == (Scale(Fraction(-1, 3)),)

    t, p, q = sp.symbols("t p q")
    quartic = adapt_phase_to_germ(
        N * (t**4 / 4 + p * t**2 / 2 - q * t),
        coordinates=(
            LocalCoordinate(t, 0, "t", "state"),
            LocalCoordinate(p, 0, "p", "parameter"),
            LocalCoordinate(q, 0, "q", "parameter"),
        ),
        fixed_scales={"N": Scale(1)},
    )
    assert quartic.certified and quartic.certificate is not None
    assert quartic.certificate.balance.scales == {
        "t": Scale(Fraction(-1, 4)),
        "p": Scale(Fraction(-1, 2)),
        "q": Scale(Fraction(-3, 4)),
    }

    unsupported = lower_registered_special_function(
        sp.bessely(N, N * z),
        large_parameter=N,
        local_parameter=z,
    )
    assert unsupported.failures[0].code == "unsupported-special-function"

    nu = sp.Symbol("nu", positive=True)
    domain_invalid = lower_registered_special_function(
        sp.besselj(nu, nu * z),
        large_parameter=nu,
        local_parameter=z,
    )
    assert domain_invalid.failures[0].code == "registry-domain-mismatch"

    payload = {
        "gate_commit": "db9898888402d7be8bbd7458c7e6b7d86d011497",
        "status": "pass",
        "raw_bessel": {
            "source": str(raw),
            "bridge_registry_id": bridge.registry_id,
            "bridge_registry_version": bridge.registry_version,
            "bridge_has_scale_hint": bridge.contains_scale_hint,
            "bridge_has_normal_form_hint": bridge.contains_normal_form_hint,
            "local_chart_certified": e2e.local_chart_certified,
            "uniform_integral_certified": e2e.uniform_integral_certified,
            "unresolved_obligations": unresolved,
            "scales": {name: str(scale) for name, scale in germ.balance.scales.items()},
            "all_replay_checks": all(passed for _, passed in germ.checks),
        },
        "generic_cubic": germ_summary(cubic),
        "quartic_cusp": germ_summary(quartic),
        "typed_failures": {
            "unsupported_bessely": unsupported.failures[0].code,
            "noninteger_besselj": domain_invalid.failures[0].code,
        },
        "oracle_scan": {
            "forbidden_literals": forbidden_literals,
            "found": [],
        },
        "claim_boundary": (
            "The raw-to-local-chart S2 gate passes through a versioned "
            "representation registry. Full reconstruction and uniform Bessel "
            "error remain unresolved; disposition is NARROW."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
