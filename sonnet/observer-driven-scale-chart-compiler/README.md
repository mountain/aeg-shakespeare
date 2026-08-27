# Observer-driven scale and chart compiler

Research-local Sonnet for [issue #140](https://github.com/mountain/process-geometry/issues/140).

## Current disposition

**NARROW:** S2 now executes a bounded raw-special-function-to-local-chart
pipeline for the registered shape `besselj(N, N*z)`.  It produces an exact,
replayable local Newton/germ certificate with

```text
local_chart_certified = true
uniform_integral_certified = false
```

The result depends on a versioned classical representation registry and is not
a general asymptotic compiler, a uniform Bessel evaluator, or an economy
theorem.  Wolfram remains an unexecuted strong baseline.

## Reading order

1. [00-problem-frontier.md](./00-problem-frontier.md) — frozen question,
   grammar, evidence firewall, and claim ceiling.
2. [01-mathematical-semantics.md](./01-mathematical-semantics.md) — exact
   descent/minimal-repair results and the non-Archimedean scale window.
3. [02-s0-s1-results.md](./02-s0-s1-results.md) — frozen S0/S1 executable
   results, held-out evidence, baselines, and Rust boundary.
4. [03-analytic-germ-newton-bessel.md](./03-analytic-germ-newton-bessel.md) —
   Newton-face criterion, finite-jet condition, Bessel turning chart, and the
   boundary between local-chart and uniform-integral certificates.
5. [prototype/README.md](./prototype/README.md) — unchanged frozen S0/S1
   Python/SymPy prototype.
6. [analytic-germ/README.md](./analytic-germ/README.md) — post-freeze S2
   adapter, representation registry, typed failures, tests, and manifest.
7. [benchmarks/03-s2-independent-baseline-red-team.md](./benchmarks/03-s2-independent-baseline-red-team.md)
   — independent raw-input baselines, black-box replay, and final NARROW
   disposition.

No file in this directory is an Experimental or Public API commitment.
