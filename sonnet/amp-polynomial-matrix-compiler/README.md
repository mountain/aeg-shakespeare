# AMP polynomial/matrix compiler

This research-local Sonnet answers issue
[#152](https://github.com/mountain/process-geometry/issues/152).

Read in order:

1. [`00-problem-frontier.md`](00-problem-frontier.md) freezes the observer,
   baselines, metrics, and claim ceiling.
2. [`01-sparse-compiler-theorems.md`](01-sparse-compiler-theorems.md) derives
   the polynomial-like coordinate and matrix-like transport.
3. [`02-benchmark-results.md`](02-benchmark-results.md) records exact support,
   sparse cost, numerical error, and the strong-baseline red team.
4. [`03-disposition.md`](03-disposition.md) states where algorithmic
   simplification was and was not earned.

The executable certificate is
[`amp_escape_compiler.py`](amp_escape_compiler.py); its independent tests are
[`test_amp_polynomial_matrix_compiler.py`](../../tests/research/test_amp_polynomial_matrix_compiler.py).

Current result:

```text
polynomial-like basis: EXPAND for symbolic support and observer coordinates
matrix-like transport: EXPAND for exact sparse compilation and replay
generic numerical acceleration: NARROW / task and tolerance dependent
overall issue disposition: EXPAND-NARROW
```

No Mathematical Core, architecture, dependency, or Public API change follows.
