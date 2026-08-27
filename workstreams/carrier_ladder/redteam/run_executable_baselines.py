"""Executable-only baseline probes for issue #142.

This script deliberately does not import the carrier compiler.  It records
what the installed SymPy can execute from the frozen same-information input.
Documentation, literature claims, embeddings, and hand-supplied Abel/tetration
oracles are excluded from the result ledger.
"""

from __future__ import annotations

import json
import importlib.util
import platform
import shutil
import signal
import time
from pathlib import Path
from typing import Callable

import sympy as sp


ROOT = Path(__file__).resolve().parent
N = sp.Symbol("N", positive=True)
x = sp.Symbol("x", positive=True)


class ProbeTimeout(Exception):
    pass


def _alarm(_signum: int, _frame: object) -> None:
    raise ProbeTimeout("10 second executable-probe budget exhausted")


def probe(name: str, fn: Callable[[], object]) -> dict[str, object]:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(10)
    try:
        value = fn()
        return {
            "id": name,
            "status": "ok",
            "result": str(value),
            "seconds": round(time.perf_counter() - started, 6),
        }
    except Exception as exc:  # baseline failures are evidence, not test errors
        return {
            "id": name,
            "status": f"error:{type(exc).__name__}",
            "result": str(exc),
            "seconds": round(time.perf_counter() - started, 6),
        }
    finally:
        signal.alarm(0)


def fixed_exp_iterate(k: int) -> sp.Expr:
    value: sp.Expr = -N
    for _ in range(k):
        value = sp.exp(value)
    return value


def main() -> None:
    nested = sp.exp(sp.exp(N + sp.exp(-N)) - sp.exp(N))
    third = sp.exp(3 * N) * (
        sp.log(1 + sp.exp(-N)) - sp.exp(-N) + sp.exp(-2 * N) / 2
    )

    probes = [
        probe("nested-exp-log-cancellation", lambda: sp.limit(nested, N, sp.oo)),
        probe("third-order-log-cancellation", lambda: sp.limit(third, N, sp.oo)),
    ]
    for k in range(1, 7):
        probes.append(
            probe(
                f"fixed-exp-iterate-{k}",
                lambda k=k: sp.limit(fixed_exp_iterate(k), N, sp.oo),
            )
        )

    A = sp.Function("A")
    F = sp.Function("F")
    h = sp.Symbol("h", integer=True, nonnegative=True)
    # These calls ask only what the installed solver executes.  Algebraically
    # rearranging an equation is explicitly not credited as constructing the
    # unknown function.
    probes.extend(
        [
            probe(
                "symbolic-exp-height-rsolve",
                lambda: sp.rsolve(
                    sp.Function("E")(h + 1) - sp.exp(sp.Function("E")(h)),
                    sp.Function("E")(h),
                ),
            ),
            probe(
                "abel-exp-solve-functional",
                lambda: sp.solve(A(sp.exp(x)) - A(x) - 1, A(x)),
            ),
            probe(
                "tetration-translation-solve-functional",
                lambda: sp.solve(F(x + 1) - sp.exp(F(x)), F(x)),
            ),
        ]
    )

    for row in probes:
        row["executable_credit"] = row["status"] == "ok"
        if row["id"].endswith("solve-functional") and row["status"] == "ok":
            row["executable_credit"] = False
            row["credit_boundary"] = (
                "algebraic isolation of an unknown function value is not a "
                "constructed Abel/tetration solution or evaluator"
            )
        if row["id"].startswith("fixed-exp-iterate-"):
            row["symbolic_height_credit"] = False
            row["credit_boundary"] = "literal fixed-height unrolling only"
        if row["id"] == "symbolic-exp-height-rsolve":
            row["symbolic_height_credit"] = False

    out = {
        "schema_version": "carrier-baseline-result-v1",
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "sympy": sp.__version__,
        },
        "available_tools": {
            "sympy": True,
            "mpmath": importlib.util.find_spec("mpmath") is not None,
            "sageall": importlib.util.find_spec("sageall") is not None,
            "transseries_python_module": importlib.util.find_spec("transseries") is not None,
            "surreal_python_module": importlib.util.find_spec("surreal") is not None,
            "wolframclient": importlib.util.find_spec("wolframclient") is not None,
            **{
                f"{name}_executable": shutil.which(name) is not None
                for name in (
                    "wolframscript",
                    "WolframKernel",
                    "math",
                    "sage",
                    "maxima",
                    "gp",
                    "maple",
                )
            },
        },
        "same_information": True,
        "probes": probes,
        "baseline_claim_boundary": (
            "Only executable outputs above count. SymPy documentation and "
            "mere rearrangements/embeddings receive no construction credit."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
