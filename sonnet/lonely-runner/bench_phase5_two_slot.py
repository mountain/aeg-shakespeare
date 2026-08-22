"""Manual Phase-5 benchmark for the exact two-slot Lonely Runner prune.

This script is intentionally outside pytest: the k=10,p=127 worker replay is large
for a package CI gate.  It loads the executable semantic mirror from
`tests/research/test_lonely_runner_two_slot_transversal.py`, runs selected current
upstream configurations, verifies accepted-leaf counts, and prints timing/node
metrics.

Run from the repository root:

    python sonnet/lonely-runner/bench_phase5_two_slot.py

Timings are diagnostic and machine-dependent.  Node counts are deterministic.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from runpy import run_path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[2]
NS = run_path(str(ROOT / "tests/research/test_lonely_runner_two_slot_transversal.py"))
CoverContext = NS["CoverContext"]
analyze_upstream_state = NS["analyze_upstream_state"]
two_slot_completion_exists = NS["two_slot_completion_exists"]


def second_candidates(context):
    first_covered = context.masks[0]
    analysis = analyze_upstream_state(
        context,
        covered=first_covered,
        eliminated=0,
        depth=1,
    )
    return tuple(
        choice
        for choice, mask in enumerate(context.masks)
        if analysis.selected_position == -1
        or mask & (1 << analysis.selected_position)
    )


def run_worker(context, worker_index: int, *, use_two_slot_prune: bool):
    counters = Counter()
    accepted = 0

    candidates = second_candidates(context)
    choice = candidates[worker_index]
    eliminated = 0
    for earlier in candidates[:worker_index]:
        eliminated |= 1 << earlier

    def run(covered: int, eliminated: int, depth: int) -> None:
        nonlocal accepted
        counters["nodes"] += 1

        if depth == context.k:
            if covered == context.full:
                accepted += 1
            return

        analysis = analyze_upstream_state(
            context,
            covered=covered,
            eliminated=eliminated,
            depth=depth,
        )
        if analysis.prune:
            counters["upstream_prune"] += 1
            return

        if use_two_slot_prune and context.k - depth == 2:
            counters["two_slot_checks"] += 1
            if not two_slot_completion_exists(
                context,
                covered=covered,
                available=analysis.available,
            ):
                counters["two_slot_prune"] += 1
                return

        selected = analysis.selected_position
        for child, mask in enumerate(context.masks):
            if eliminated & (1 << child):
                continue
            if selected == -1 or mask & (1 << selected):
                run(covered | mask, eliminated, depth + 1)
                eliminated |= 1 << child

    start = perf_counter()
    run(
        context.masks[0] | context.masks[choice],
        eliminated,
        2,
    )
    elapsed = perf_counter() - start
    return choice + 1, counters, accepted, elapsed


def print_pair(context, worker_index: int) -> None:
    second, baseline, baseline_accepted, baseline_time = run_worker(
        context,
        worker_index,
        use_two_slot_prune=False,
    )
    second2, enhanced, enhanced_accepted, enhanced_time = run_worker(
        context,
        worker_index,
        use_two_slot_prune=True,
    )

    assert second == second2
    assert baseline_accepted == enhanced_accepted

    reduction = 1 - enhanced["nodes"] / baseline["nodes"]
    print(
        f"second={second:>2}  "
        f"nodes {baseline['nodes']:>8} -> {enhanced['nodes']:>8}  "
        f"(-{100*reduction:5.1f}%)  "
        f"new_prunes={enhanced['two_slot_prune']:>6}  "
        f"accepted={baseline_accepted:>6}  "
        f"time {baseline_time:6.3f}s -> {enhanced_time:6.3f}s"
    )


def main() -> None:
    context = CoverContext.build(k=10, p=127)
    expected = {
        0: (2, 376376, 264486, 17022, 2822),
        1: (4, 505777, 322126, 28063, 8041),
        2: (6, 543301, 345043, 30261, 19176),
        3: (8, 394315, 244797, 22958, 8841),
        4: (10, 316729, 201286, 18319, 7454),
    }

    print("k=10, p=127 — first five serialized top-level workers")
    for worker_index in range(5):
        second, baseline, baseline_accepted, _ = run_worker(
            context,
            worker_index,
            use_two_slot_prune=False,
        )
        second2, enhanced, enhanced_accepted, _ = run_worker(
            context,
            worker_index,
            use_two_slot_prune=True,
        )
        assert second == second2
        assert baseline_accepted == enhanced_accepted
        assert (
            second,
            baseline["nodes"],
            enhanced["nodes"],
            enhanced["two_slot_prune"],
            baseline_accepted,
        ) == expected[worker_index]

        reduction = 1 - enhanced["nodes"] / baseline["nodes"]
        print(
            f"second={second:>2}  "
            f"nodes {baseline['nodes']:>8} -> {enhanced['nodes']:>8}  "
            f"(-{100*reduction:5.1f}%)  "
            f"new_prunes={enhanced['two_slot_prune']:>6}  "
            f"accepted={baseline_accepted:>6}"
        )

    baseline_total = sum(row[1] for row in expected.values())
    enhanced_total = sum(row[2] for row in expected.values())
    print(
        "aggregate nodes:",
        baseline_total,
        "->",
        enhanced_total,
        f"(-{100*(1-enhanced_total/baseline_total):.1f}%)",
    )


if __name__ == "__main__":
    main()
