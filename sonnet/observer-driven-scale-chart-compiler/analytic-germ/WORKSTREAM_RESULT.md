# Engineering workstream result

## Outcome

The next engineering gate passes in a narrow, research-local sense. A
versioned registry first lowers the exact raw shape `besselj(N, N*z)` (positive
integer `N`, real `z`) to its classical cosine-integral phase. A generic
elementary analytic-germ adapter then converts that phase

\[
N(z\sin\theta-\theta),\qquad (\theta,z)\to(0,1),
\]

to the minimal rank-completing polynomial prefix

\[
N\left((z-1)\theta-\frac{\theta^3}{6}\right).
\]

The pre-existing exact solver, unchanged, derives

\[
\theta=N^{-1/3}\hat\theta,
\qquad
z-1=N^{-2/3}\hat\delta.
\]

The adapter labels the local phase only as `degenerate-order-3`. The Bessel
name exists only in the separate representation registry; no expected-scale or
named-normal-form dispatch occurs in the discovery path.

## Evidence

- Five deterministic replay checks pass.
- The two explicitly known discarded terms both have order `N^-2/3`.
- The conservative formal total-degree-six tail has order bound `N^-1`.
- Direct generic-adapter `besselj(N, N*z)` input fails with
  `special-function-oracle-required`; the explicit registry path succeeds.
- The raw pipeline is **local-chart-certified** and explicitly
  **not uniform-integral-certified**. Full reconstruction and uniform-error
  obligations remain open in the machine-readable summary.
- Noninteger order and the wrong Bessel argument shape fail by domain/shape;
  `bessely` is unregistered and fails closed.
- `sin(N*x)` fails with `fixed-scale-inside-analytic-function`, closing an
  unsafe formal-tail loophole.
- A regular quadratic phase fails a turning-point task with `regular-saddle`.
- A constructed inconsistent Newton-face case exposes two admissible charts
  and returns `ambiguous-germ`.
- The quartic cusp replays the frozen held-out chart exactly.
- All 15 adapter tests pass.
- All 12 frozen S0/S1 tests still pass; no frozen file was edited.

## Contract and claim boundary

The generic input contract starts from an explicitly declared elementary
phase. The raw path recognizes one exact registered representation; it does not
discover integral representations. Its Taylor-tail statement is a formal
scale-order certificate, not a uniform analytic remainder bound on a contour.
Therefore this result advances the raw-to-chart pipeline but does not by itself
establish Bessel asymptotics or an economy theorem.

## Governance disposition

- Mathematical Core: unchanged.
- Engineering Architecture: refined locally by adding a symbolic adapter stage
  before the stable exact balance/certificate kernel.
- Theory Map: unchanged; this remains T1/local Sonnet evidence.
- API status: research-local; no Experimental or Public extraction.
- Rust boundary: unchanged.  The symbolic germ grammar remains Python/SymPy;
  only the exact balance and replay kernel remains a later native candidate.

## Integration note

Copy this directory under the existing Sonnet only after reviewing the
formal-tail assumption and the total-degree selection rule.  Do not alter the
S0/S1 freeze manifest.  Record this as a new post-freeze phase with a separate
manifest if public integration proceeds.
