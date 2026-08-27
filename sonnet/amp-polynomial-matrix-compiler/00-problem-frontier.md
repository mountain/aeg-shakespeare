# Problem frontier: do AMP polynomials and matrices simplify an algorithm?

Status: frozen contract for issues
[#152](https://github.com/mountain/process-geometry/issues/152) and
[#154](https://github.com/mountain/process-geometry/issues/154).

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

The scalar readout is the normalized long-horizon quantity

\[
G_N(y)=d^{-N}F^{\circ N}(y)
\]

and its limit when the escape coordinate converges.  This is deliberately
narrower than reconstructing the full iterate or orbit.

Two computational tasks must not be conflated:

1. **numerical limit:** evaluate one scalar escape coordinate to a requested
   analytic-tail tolerance;
2. **coefficient readout:** recover a finite polynomial-like coordinate and an
   exact transport/residual certificate for reuse or symbolic inspection.

The first task does not require coefficients.  The second task does.

## 3. Same-information baselines

Four paths receive separate ledgers.

1. **Expanded symbolic baseline:** form `f^[N](x)` as one ordinary expanded
   polynomial.
2. **Strong numerical baseline:** update `F(y)` directly in the logarithmic
   chart, accumulate the normalized correction, and stop when floating-point
   correction is zero.  It is forbidden to expand the polynomial.
3. **Native AMP evaluator:** update the inverse state `q` directly, accumulate
   the exact process-level decomposition, and stop from an analytic tail bound.
   It may not call the series or matrix compiler.
4. **AMP compiler:** compile a finite polynomial-like escape coordinate once
   from a sparse substitution matrix, then evaluate it for the declared
   readout.  Its online phase uses the degree-ray variable `z=q^d`.

The expanded baseline measures symbolic support only.  It may not be used as
the sole numerical competitor.

## 4. Metrics

- exact expanded support count;
- observer order and nonzero polynomial-like terms;
- dense versus sparse matrix entries;
- exact compilation and residual certificate;
- native process levels, state width, primitive evaluations, and tail bound;
- strong-baseline executed steps;
- compile-once/evaluate-many Horner work;
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

Here “Koopman observable” means a function on state used by the classical
composition operator.  It is not identified with a Process Geometry observer,
which also carries task, information, chart, and certification semantics.

## 6. Claim ceiling

This phase does not claim a new Böttcher theorem, generic Koopman solver,
complexity-class improvement, Ising solver, or Public API.

```text
Epistemic maturity: T1 exact finite compiler + certified native calibration
Engineering status: Sonnet-local Python
Mathematical Core: unchanged
```
