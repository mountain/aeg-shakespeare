# AMP polynomial/matrix compiler

This research-local Sonnet answers issues
[#152](https://github.com/mountain/process-geometry/issues/152) and
[#154](https://github.com/mountain/process-geometry/issues/154).

Read in order:

1. [`00-problem-frontier.md`](00-problem-frontier.md) freezes the observer,
   baselines, metrics, and claim ceiling.
2. [`01-sparse-compiler-theorems.md`](01-sparse-compiler-theorems.md) derives
   the polynomial-like coordinate and matrix-like transport.
3. [`02-benchmark-results.md`](02-benchmark-results.md) records exact support,
   sparse cost, numerical error, and the strong-baseline red team.
4. [`03-disposition.md`](03-disposition.md) states where algorithmic
   simplification was and was not earned.
5. [`04-native-process-evaluator.md`](04-native-process-evaluator.md) separates
   direct AMP process evaluation from coefficient and matrix compilation.

The executable certificate is
[`amp_escape_compiler.py`](amp_escape_compiler.py); its independent tests are
[`test_amp_polynomial_matrix_compiler.py`](../../tests/research/test_amp_polynomial_matrix_compiler.py).

Current result:

```text
native inverse-state process: EXPAND as the default scalar numerical path
polynomial-like basis: EXPAND for fixed-chart coefficient/readout compilation
matrix-like transport: EXPAND for offline exact compilation and replay
compiled numerical acceleration: NARROW / task, tolerance, and reuse dependent
overall issue disposition: EXPAND-NARROW
```

No Mathematical Core, architecture, dependency, or Public API change follows.
