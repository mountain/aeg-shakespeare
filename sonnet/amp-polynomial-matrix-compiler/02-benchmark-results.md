# Benchmark results

Status: exact support/certificate measurements plus certified native and
bounded compiled floating-point calibration.

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

The native inverse-state evaluator reaches the same binary64 value after four
process levels and reports the analytic tail bound

\[
4.03\times10^{-23}<10^{-15}.
\]

This is a truncation-tail statement, not a total floating-point error bound.

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

## 3. Native process calibration

The native evaluator uses one initial exponential, one `log1p` and one inverse
state update per retained process level, four persistent working scalars, and
no series or matrix construction.  It fails closed if binary64 inverse-state
or tail arithmetic underflows before a trustworthy bound can be reported.

| Initial `y` | Process levels | Reported analytic tail bound | Binary64 value |
|---:|---:|---:|---:|
| 0.0 | 6 | `3.54e-25` | `0.4073545227394800` |
| 0.5 | 5 | `5.53e-21` | `0.6746578808175746` |
| 1.0 | 4 | `9.27e-17` | `1.0670158740022506` |
| 1.5 | 4 | `4.03e-23` | `1.5248559772600594` |
| 2.0 | 4 | `7.48e-30` | `2.0091558398904660` |

The point `y=0`, where the finite asymptotic series becomes unstable, remains
well behaved for the exact process recurrence.  This is a domain separation,
not evidence that every AMP chart is global.

## 4. Sparse compilation and accuracy

| Order `K` | Dense entries | Sparse entries | Nonzero `h_k` | First residual | Absolute error |
|---:|---:|---:|---:|---:|---:|
| 6 | 36 | 6 | 2 | `5/4 q^8` | `3.58e-6` |
| 10 | 100 | 15 | 4 | `2 q^12` | `1.49e-8` |
| 14 | 196 | 28 | 6 | `-3 q^16` | `4.82e-11` |
| 20 | 400 | 55 | 9 | `144/11 q^22` | `3.13e-14` |
| 30 | 900 | 120 | 14 | `-2523/16 q^32` | below binary64 distinction |

All coefficients, sparse entries, and residuals are exact rationals.  Only
the final evaluation/error comparison uses floating point.

## 5. Same-accuracy and strong-baseline red team

At `y=1.5`, choosing the smallest tested compiled order that meets each target
gives the following structural online comparison.  `K/2` is the number of
degree-ray Horner slots; the native column is the number of `log1p` process
levels.

| Target | Native levels | Compiled `K` | Compiled error | Horner slots | Sparse compile entries |
|---:|---:|---:|---:|---:|---:|
| `1e-6` | 3 | 8 | `2.60e-7` | 4 | 10 |
| `1e-8` | 3 | 12 | `3.73e-10` | 6 | 21 |
| `1e-10` | 3 | 14 | `4.82e-11` | 7 | 28 |
| `1e-12` | 4 | 18 | `7.17e-13` | 9 | 45 |
| `1e-15` | 4 | 22 | `6.66e-16` | 11 | 66 |

For 100 queries at `K=20`:

```text
compile once:
  55 sparse entries
  20 triangular divisions
online compiled proxy:
  10 degree-ray Horner slots (9 nonzero coefficients) per query
native process:
  4 log1p levels per query with a 4.03e-23 analytic tail
strong recurrence:
  9 executed correction steps per query in binary64
```

The compiled Horner path may be faster after enough repeated same-chart
queries, because its online operations are simple multiply-adds.  The native
path has no coefficient build, accepts parameter variation directly, retains
constant-width state, and supplies a stopping certificate.  Therefore neither
path earns a universal runtime win: the crossover depends on tolerance,
initial chart, backend, validation policy, and reuse count.  Wall-clock timing
is deliberately not a CI assertion.

The main earned advantages are instead:

- avoiding exponential symbolic support;
- obtaining the long-horizon observer without choosing one horizon `N`;
- exact coefficient and residual certificates;
- a reusable compile-once coordinate for many states or parameter sweeps;
- exposing the support geometry and failure boundary.

## 6. Negative chart control

At `y_0=0`, the asymptotic series is outside its safe region.  The errors are

```text
K=14: about 0.056
K=20: more than 4.0
```

Increasing observer order makes the answer worse.  A finite AMP truncation is
therefore not a globally convergent numerical method.  The compiler must
carry a chart/domain certificate or use residual-driven adaptation; order
alone is not safety.  The native process path is the default for this scalar
numerical task in its certified `y>=0, t>0` domain.

## 7. Replay

The executable tests independently verify:

- every substitution-matrix coefficient against SymPy series composition;
- nilpotence at the finite observer;
- the exact eigenrelation and first omitted residual;
- expanded support counts against explicit small iterates;
- convergence against the strong logarithmic recurrence;
- native evaluation without coefficient or matrix compiler calls;
- analytic-tail, domain, process-budget, and primitive-cost reporting;
- degree-ray Horner replay with a generic-support fallback;
- sparse/dense cost separation;
- failure outside the asymptotic chart;
- typed refusal for invalid or cancellation-prone frozen tasks.
