# Native AMP process evaluator

Status: executable T1 calibration for issue
[#154](https://github.com/mountain/process-geometry/issues/154).

## 1. Why split the evaluator from the compiler?

The first compiler solved a coefficient problem: find a finite
polynomial-like escape coordinate and replay its conjugacy relation exactly.
That legitimately uses a sparse linear action on coefficients.

The numerical question is smaller: evaluate one scalar escape limit.  Forcing
that question through a coefficient basis introduces Taylor order, chart
truncation, and a matrix that the original nonlinear process does not require.
The software now keeps these tasks separate.

```text
scalar numerical limit       -> native inverse-state recurrence
fixed-chart repeated readout -> polynomial-like degree-ray Horner evaluator
exact coefficient witness    -> sparse matrix-like offline compiler/replay
```

This is a split/refinement of the Sonnet, not removal of the matrix result.

## 2. Exact process identity

For

\[
F(y)=dy+\log(1+t e^{-dy}),
\qquad q_n=e^{-F^{\circ n}(y)},
\]

the inverse state evolves exactly by

\[
q_0=e^{-y},
\qquad
q_{n+1}=\frac{q_n^d}{1+tq_n^d}.
\]

Unfolding the normalized recurrence, without expanding a series, gives

\[
d^{-N}F^{\circ N}(y)
=y+\sum_{n=0}^{N-1}d^{-n-1}\log(1+tq_n^d).
\]

The native evaluator accumulates this identity directly.  It never calls the
coefficient source, substitution matrix, or triangular compiler.

## 3. First certified domain and tail

Freeze

\[
d\ge2,\qquad t>0,\qquad y\ge0.
\]

Then `0 <= q_0 <= 1` and

\[
0\le q_{n+1}\le q_n^d\le q_n.
\]

After retaining `R` process levels, use
`log(1+u) <= u` and monotonicity of `q_n`:

\[
\begin{aligned}
0\le T_R
&=\sum_{n=R}^{\infty}d^{-n-1}\log(1+tq_n^d)\\
&\le tq_R^d\sum_{n=R}^{\infty}d^{-n-1}\\
&=\frac{d^{-R}tq_R^d}{d-1}.
\end{aligned}
\]

The implementation stops only when this a posteriori analytic tail, evaluated
on the represented inverse-state recurrence, is at most the requested
tolerance.  It rejects an invalid chart, exhausted level budget, or binary64
underflow with typed errors.  The certificate intentionally excludes roundoff
and is not advertised as an interval enclosure of the total error.

## 4. Cost regimes

The implementation retains four persistent working scalars (`q`, cached
`q^d`, accumulated value, and inverse degree weight), one initial exponential,
and per level one `log1p`, one inverse-state update, and degree powers.  Storage
is `O(1)`.

For fixed positive `y`, `q_R <= exp(-d^R y)`, so the required process depth has
the double-logarithmic scale

\[
R=O(\log\log(1/\varepsilon))
\]

for fixed `d,t`; this is a domain-specific upper-scale statement, not a generic
AMP complexity theorem.

The compiled path has different economics.  Its current exact compiler stores
a sparse triangular action and costs quadratically in observer order in the
worst case of this implementation.  Once compiled, support lies on
`q^(dj)`, so evaluation uses Horner in

\[
z=q^d=e^{-dy}
\]

with `floor(K/d)` coefficient slots and no matrix at runtime.  It can win on a
large batch with the same degree, interaction, chart, and tolerance.  It loses
its premise when parameters vary or the chart fails.  Compilation amortization
is therefore reported separately rather than hidden in an online timing.

## 5. Architectural consequence

The classical Koopman composition operator remains useful for compiling a
function-space action.  It is not treated as a claim that the nonlinear AMP
process is fundamentally a linear observer.  In Process Geometry terminology,
an observer also specifies task-visible information, chart, decoder, and
certificate; it is not synonymous with a scalar Koopman observable.

The resulting boundary is deliberately local:

```text
Mathematical Core: unchanged
Research Programme: split numerical evaluation from coefficient compilation
Engineering Architecture: Sonnet-local dual path
Theory Map: no promoted node
Experimental/Public API: none
```

Transfer to mixed-log or coupled systems remains the next evidence gate.
