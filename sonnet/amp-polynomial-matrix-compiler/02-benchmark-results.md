# Benchmark results

Status: exact support/certificate measurements plus bounded floating-point
calibration.

## 1. Frozen instance

Use

\[
d=2,
\qquad
t=1,
\qquad
y_0=1.5,
\qquad
N=100.
\]

The strong numerical recurrence gives

\[
G_{100}(y_0)=1.5248559772600594.
\]

It detects that the interaction correction has underflowed to zero after nine
executed steps in binary64 arithmetic.  This early stop is retained as a
positive baseline result.

## 2. Symbolic support

For positive `t`, the fully expanded iterate has

\[
\#\operatorname{supp}(f^{\circ N})=d^{N-1}+1.
\]

For the frozen instance this is

\[
2^{99}+1
=633825300114114700748351602689
\]

ordinary polynomial terms.  The AMP compiler never constructs this
polynomial; its observer state remains `K` ray coefficients plus the affine
`y` term.

This is a real symbolic and storage simplification.  It does not imply the
same factor against direct numerical recurrence.

## 3. Sparse compilation and accuracy

| Order `K` | Dense entries | Sparse entries | Nonzero `h_k` | First residual | Absolute error |
|---:|---:|---:|---:|---:|---:|
| 6 | 36 | 6 | 2 | `5/4 q^8` | `3.58e-6` |
| 10 | 100 | 15 | 4 | `2 q^12` | `1.49e-8` |
| 14 | 196 | 28 | 6 | `-3 q^16` | `4.82e-11` |
| 20 | 400 | 55 | 9 | `144/11 q^22` | `3.13e-14` |
| 30 | 900 | 120 | 14 | `-2523/16 q^32` | below binary64 distinction |

All coefficients, sparse entries, and residuals are exact rationals.  Only
the final evaluation/error comparison uses floating point.

## 4. Strong-baseline red team

For 100 queries at `K=20`:

```text
compile once:
  55 sparse entries
  20 triangular divisions
online compiled proxy:
  9 nonzero series terms per query
strong recurrence:
  9 executed correction steps per query in binary64
```

The online structural counts are comparable.  Compilation overhead means the
AMP path does **not** earn a universal single-query floating-point speedup.
At `K=10`, four nonzero terms give about `1.5e-8` absolute error and can be an
economical batch approximation, but the tradeoff depends on tolerance,
initial chart, numeric backend, and number of queries.

The main earned advantages are instead:

- avoiding exponential symbolic support;
- obtaining the long-horizon observer without choosing one horizon `N`;
- exact coefficient and residual certificates;
- a reusable compile-once coordinate for many states or parameter sweeps;
- exposing the support geometry and failure boundary.

## 5. Negative chart control

At `y_0=0`, the asymptotic series is outside its safe region.  The errors are

```text
K=14: about 0.056
K=20: more than 4.0
```

Increasing observer order makes the answer worse.  A finite AMP truncation is
therefore not a globally convergent numerical method.  The compiler must
carry a chart/domain certificate or use residual-driven adaptation; order
alone is not safety.

## 6. Replay

The executable tests independently verify:

- every substitution-matrix coefficient against SymPy series composition;
- nilpotence at the finite observer;
- the exact eigenrelation and first omitted residual;
- expanded support counts against explicit small iterates;
- convergence against the strong logarithmic recurrence;
- sparse/dense cost separation;
- failure outside the asymptotic chart;
- typed refusal for invalid or cancellation-prone frozen tasks.
