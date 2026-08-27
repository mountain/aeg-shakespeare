# Problem frontier: do AMP polynomials and matrices simplify an algorithm?

Status: frozen contract for issue
[#152](https://github.com/mountain/process-geometry/issues/152).

## 1. The question

Issue #150 identified the finite AMP polynomial-like family

\[
\sum_{\gamma,n}^{\mathrm{finite}}
c_{\gamma,n}x^\gamma(\log x)^n
\]

and the sparse operator matrices induced by `A`, `M`, and `P` on the degree
lattice `(gamma,n)`.  Algebraic closure alone does not establish algorithmic
value.  This phase asks whether the representation reduces a frozen task under
same-information baselines.

## 2. Frozen power-dominant task

Take

\[
f(x)=x^d+t,
\qquad d\ge2,
\qquad t>0,
\]

on a declared positive chart near infinity.  Put

\[
y=\log x,
\qquad
q=e^{-y}.
\]

Then

\[
F(y)=dy+\log(1+tq^d),
\qquad
g(q)=e^{-F(y)}=\frac{q^d}{1+tq^d}.
\]

The main observer is the normalized long-horizon quantity

\[
G_N(y)=d^{-N}F^{\circ N}(y)
\]

and its limit when the asymptotic coordinate converges.  This is deliberately
narrower than reconstructing the full iterate or orbit.

## 3. Same-information baselines

Three paths receive separate ledgers.

1. **Expanded symbolic baseline:** form `f^[N](x)` as one ordinary expanded
   polynomial.
2. **Strong numerical baseline:** update `F(y)` directly in the logarithmic
   chart, accumulate the normalized correction, and stop when floating-point
   correction is zero.  It is forbidden to expand the polynomial.
3. **AMP compiler:** compile a finite polynomial-like escape coordinate once
   from a sparse substitution matrix, then evaluate it for the declared
   observer.

The expanded baseline measures symbolic support only.  It may not be used as
the sole numerical competitor.

## 4. Metrics

- exact expanded support count;
- observer order and nonzero polynomial-like terms;
- dense versus sparse matrix entries;
- exact compilation and residual certificate;
- strong-baseline executed steps;
- compile-once/evaluate-many online work;
- numerical error across observer orders;
- chart failure outside the asymptotic domain;
- decoder and output scope.

## 5. Acceptance and kill conditions

The representation earns algorithmic credit only if:

- the basis makes the declared transport exactly sparse;
- the matrix construction changes the solve, not only its notation;
- the result is replayable without hidden symbolic expansion;
- a strong recurrence baseline is reported;
- compilation, online work, and output precision are separated.

Narrow or stop a claim if:

- an ordinary Taylor or monomial basis is relabelled AMP without a support
  advantage;
- a dense generic eigensolver replaces an available triangular solve;
- symbolic expansion is treated as the only numerical baseline;
- the finite truncation is evaluated outside its chart without a refusal;
- one scalar long-time observer is presented as full-orbit reconstruction;
- a classical Böttcher/Koopman result is claimed as new.

## 6. Claim ceiling

This phase does not claim a new Böttcher theorem, generic Koopman solver,
complexity-class improvement, Ising solver, or Public API.

```text
Epistemic maturity: T1 exact finite compiler + bounded numerical calibration
Engineering status: Sonnet-local Python
Mathematical Core: unchanged
```
