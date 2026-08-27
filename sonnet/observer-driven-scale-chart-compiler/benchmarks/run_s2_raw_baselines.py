#!/usr/bin/env python3
"""Independent S2 raw-input baselines for the Bessel turning-point gate.

This file is an evaluator, never a discoverer.  It deliberately keeps raw
special-function probes separate from representation-supplied and
chart-supplied probes.  No result from a hinted row earns discovery credit.

The frozen success predicate lives in ``bessel-gate-contract.json`` at commit
db9898888402d7be8bbd7458c7e6b7d86d011497.  This script does not import the
compiler and does not modify its implementation.
"""

from __future__ import annotations

import importlib.util
import json
import os
import platform
import shutil
import time
from dataclasses import asdict, dataclass
from typing import Callable

import sympy as sp


@dataclass(frozen=True)
class Probe:
    id: str
    input_class: str
    manual_semantic_hints: int
    status: str
    result: str
    seconds: float
    coupled_chart_reported: bool
    discovery_credit: bool
    note: str


def run_probe(
    probe_id: str,
    input_class: str,
    manual_semantic_hints: int,
    fn: Callable[[], sp.Basic],
    *,
    note: str,
) -> Probe:
    start = time.perf_counter()
    try:
        result = fn()
        status = "ok"
        rendered = repr(result)
    except Exception as exc:  # failures are benchmark data
        status = f"error:{type(exc).__name__}"
        rendered = str(exc)
    elapsed = time.perf_counter() - start

    # The baseline has no task-observer/chart result type.  A printed Taylor
    # series, Bessel recurrence, or supplied substitution is not a discovered
    # coupled chart.  Keep this evaluator judgment explicit rather than using
    # a fragile substring heuristic.
    coupled_chart_reported = False
    discovery_credit = input_class == "raw" and coupled_chart_reported
    return Probe(
        id=probe_id,
        input_class=input_class,
        manual_semantic_hints=manual_semantic_hints,
        status=status,
        result=rendered,
        seconds=elapsed,
        coupled_chart_reported=coupled_chart_reported,
        discovery_credit=discovery_credit,
        note=note,
    )


def sympy_probes() -> list[Probe]:
    N = sp.symbols("N", integer=True, positive=True)
    z = sp.symbols("z", real=True)
    theta, u, xi = sp.symbols("theta u xi", real=True)
    eps = sp.symbols("eps", positive=True)
    raw = sp.besselj(N, N * z)

    return [
        run_probe(
            "raw_series_large_order",
            "raw",
            0,
            lambda: sp.series(raw, N, sp.oo, 2),
            note="Same raw input as the frozen S2 gate; asks for a direct large-order series.",
        ),
        run_probe(
            "raw_limit_large_order",
            "raw",
            0,
            lambda: sp.limit(raw, N, sp.oo),
            note="A fixed-z limit cannot encode the requested uniform z-local task, but tests raw support.",
        ),
        run_probe(
            "raw_aseries_large_order",
            "raw",
            0,
            lambda: raw.aseries(N, n=2),
            note="Direct asymptotic-series method on the unmodified special function.",
        ),
        run_probe(
            "raw_rewrite_integral",
            "raw",
            0,
            lambda: raw.rewrite(sp.Integral),
            note="Tests whether stock rewriting exposes a domain-valid integral representation automatically.",
        ),
        run_probe(
            "raw_rewrite_hyper",
            "raw",
            0,
            lambda: raw.rewrite(sp.hyper),
            note="Tests a generic representation rewrite without supplying a chart.",
        ),
        run_probe(
            "raw_local_z_series",
            "raw",
            0,
            lambda: sp.series(raw, z, 1, 3),
            note="Expands at z=1 but leaves large-order Bessel coefficients and reports no N-coupled scale.",
        ),
        run_probe(
            "chart_supplied_direct_special_function",
            "chart-supplied verification",
            2,
            lambda: sp.series(
                sp.besselj(eps**-3, eps**-3 * (1 + eps**2 * xi)),
                eps,
                0,
                2,
            ),
            note="The two expected scale substitutions are supplied; this can only earn verification credit.",
        ),
        run_probe(
            "representation_supplied_phase_germ",
            "representation-supplied verification",
            2,
            lambda: sp.series(N * (z * sp.sin(theta) - theta), theta, 0, 7),
            note="The integral representation and phase extraction are supplied externally; SymPy only builds the germ.",
        ),
        run_probe(
            "representation_and_chart_supplied_phase",
            "representation-and-chart-supplied verification",
            4,
            lambda: sp.series(
                eps**-3
                * ((1 + eps**2 * xi) * sp.sin(eps * u) - eps * u),
                eps,
                0,
                4,
            ),
            note="Representation, phase, and both scale exponents are supplied; exact residual verification only.",
        ),
    ]


def wolfram_boundary() -> dict[str, object]:
    executables = {
        name: shutil.which(name)
        for name in ("wolframscript", "WolframKernel", "math")
    }
    credential_names = sorted(
        key for key in os.environ if key.upper().startswith("WOLFRAM")
    )
    client_installed = importlib.util.find_spec("wolframclient") is not None
    executable = any(executables.values())
    authenticated_cloud_path = client_installed and bool(credential_names)
    return {
        "executables": executables,
        "wolframclient_installed": client_installed,
        "wolfram_environment_variable_names": credential_names,
        "authenticated_cloud_path_detected": authenticated_cloud_path,
        "exact_s2_input_executed": False,
        "boundary": (
            "No local Wolfram kernel executable, Python client, or configured "
            "Wolfram credential path was detected. Official documentation is "
            "capability evidence only, not an execution result. No comparative "
            "win or loss is inferred."
            if not executable and not authenticated_cloud_path
            else "An execution path appears available but was not exercised by this probe."
        ),
        "official_test_expressions_for_future_execution": [
            "Asymptotic[BesselJ[n, n z], n -> Infinity, Assumptions -> Element[n, Integers] && n > 0 && Element[z, Reals]]",
            "Asymptotic[BesselJ[n, n (1 + xi n^(-2/3))], n -> Infinity, Assumptions -> Element[n, Integers] && n > 0 && Element[xi, Reals]]",
            "AsymptoticIntegrate[Cos[n (theta - z Sin[theta])], {theta, 0, Pi}, n -> Infinity, Assumptions -> Element[n, Integers] && n > 0 && Element[z, Reals]]/Pi",
        ],
        "warning": (
            "The second expression supplies the turning scale and is a hinted "
            "verification row. Only the first raw special-function expression "
            "could receive raw discovery credit; the integral row supplies a representation."
        ),
    }


def main() -> None:
    probes = sympy_probes()
    by_id = {probe.id: probe for probe in probes}
    raw_rewrites = (
        by_id["raw_rewrite_integral"],
        by_id["raw_rewrite_hyper"],
    )
    payload = {
        "gate_commit": "db9898888402d7be8bbd7458c7e6b7d86d011497",
        "run_date": "2026-08-27",
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "sympy": sp.__version__,
        },
        "raw_input": "besselj(N, N*z)",
        "sympy_probes": [asdict(probe) for probe in probes],
        "sympy_disposition": {
            "raw_chart_discovered": any(
                probe.discovery_credit for probe in probes
            ),
            "representation_exposed_from_raw": any(
                probe.status == "ok" and probe.result != "besselj(N, N*z)"
                for probe in raw_rewrites
            ),
            "phase_germ_verified_after_representation_hint": (
                by_id["representation_supplied_phase_germ"].status == "ok"
            ),
            "normalized_phase_verified_after_representation_and_chart_hints": (
                by_id["representation_and_chart_supplied_phase"].status == "ok"
            ),
            "conclusion": (
                "SymPy 1.14.0 does not complete the frozen raw-to-chart S2 task. "
                "It can form the local phase germ and replay the normalized "
                "series after the missing representation/chart information is supplied."
            ),
        },
        "wolfram": wolfram_boundary(),
        "claim_boundary": (
            "This baseline can establish an observed SymPy gap. Because the exact "
            "Wolfram inputs were not executed, it cannot establish comparative novelty."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
