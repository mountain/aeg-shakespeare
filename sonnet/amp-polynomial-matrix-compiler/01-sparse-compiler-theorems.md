# Sparse AMP compiler theorems

Status: exact over rational `t>0` at every fixed observer order.

## 1. Polynomial-like observer basis

On the `y=log x` chart, use

\[
q^k=e^{-ky}=x^{-k},
\qquad 1\le k\le K.
\]

The compiled coordinate has the finite AMP form

\[
H_K(y)=y+\sum_{k=1}^K h_kq^k.
\]

It is a finite slice of the exponential-logarithmic algebra: the affine `y`
term records the Power direction, and the `q` ray records the completed
Addition residual around the power-dominant chart.

## 2. Matrix-like composition

Let `C_K` be composition by

\[
g(q)=\frac{q^d}{1+tq^d}
\]

on the truncated ray.  Its entries are

\[
(C_K)_{r,k}=[q^r]g(q)^k.
\]

Using the negative-binomial expansion,

\[
g(q)^k
=q^{dk}(1+tq^d)^{-k}
=\sum_{j\ge0}
(-1)^j\binom{k+j-1}{j}t^j q^{d(k+j)}.
\]

Therefore

\[
(C_K)_{d(k+j),k}
=(-1)^j\binom{k+j-1}{j}t^j,
\]

and every other entry is zero.

**Proposition 2.1.**  `C_K` is nilpotent.  In particular,

\[
C_K^r=0
\quad\text{whenever}\quad
d^r>K.
\]

**Proof.**  One application sends a monomial of degree `k` to degrees at
least `dk`.  After `r` applications, every surviving degree is at least
`d^r k`.  No positive degree survives the observer cutoff when `d^r>K`.
QED.

This nilpotence is the finite-observer version of power-driven scale escape.

## 3. The linear eigenproblem

Write

\[
u(q)=\log(1+tq^d)
=\sum_{j\ge1}\frac{(-1)^{j+1}}{j}t^jq^{dj}.
\]

Composition gives

\[
H_K(F(y))
=dy+u(q)+\sum_{k=1}^K h_k g(q)^k.
\]

Thus the truncated conjugacy condition

\[
H_K\circ F=dH_K+O(q^{K+1})
\]

is exactly

\[
(dI-C_K)h=u_{\le K}.
\]

**Theorem 3.1.**  This equation has a unique rational solution for rational
`t`.

**Proof.**  `C_K` strictly raises degree, so `dI-C_K` is triangular with
nonzero diagonal `d`.  Equivalently, nilpotence gives the finite inverse

\[
(dI-C_K)^{-1}
=\frac1d\sum_{r\ge0}^{\mathrm{finite}}
\left(\frac{C_K}{d}\right)^r.
\]

All entries remain rational.  QED.

For `d=2`, `t=1`, and `K=10`, the compiler obtains

\[
H_{10}(y)
=y+\frac12q^2-\frac13q^6+\frac58q^8-\frac9{10}q^{10}.
\]

The finite eigenrelation replays exactly.  Its first omitted residual is

\[
2q^{12}.
\]

## 4. Long-horizon observer

The exact, untruncated coordinate is the logarithm of a Böttcher coordinate
and satisfies

\[
H(F(y))=dH(y).
\]

Consequently,

\[
d^{-N}H(F^{\circ N}(y))=H(y).
\]

When the correction `H(z)-z` vanishes along the escaping orbit,

\[
\lim_{N\to\infty}d^{-N}F^{\circ N}(y)=H(y).
\]

The finite compiler approximates this observer directly, without constructing
the degree-`d^N` iterate.

## 5. Classical boundary

This construction meets established mathematics:

- Böttcher coordinates conjugate a degree-`d` polynomial near infinity to
  `z -> z^d`;
- the Green/escape-rate function is the logarithmic long-horizon observer;
- the Koopman operator acts linearly on observables by composition;
- Carleman-style methods represent nonlinear composition in an infinite
  function basis.

The AMP-specific question is narrower: does the arithmetic chart select the
right sparse dictionary and typed completion automatically?  The present
example gives one positive calibration, not a novelty claim about these
classical structures.

Primary references used as boundaries:

1. B. O. Koopman,
   [“Hamiltonian Systems and Transformation in Hilbert Space”](https://www.pnas.org/doi/10.1073/pnas.17.5.315),
   1931.
2. C. Favre and T. Gauthier,
   [“The arithmetic of polynomial dynamical pairs”](https://arxiv.org/abs/2004.13801),
   including formal Böttcher expansions at infinity.
3. L. DeMarco, K. Lindsey,
   [“Convergence properties of the Gronwall area formula for quadratic Julia sets”](https://arxiv.org/abs/1405.1933),
   including coefficient-level numerical use of Böttcher maps.
4. M. J. Colbrook,
   [structure-preserving finite approximations of Koopman operators](https://arxiv.org/abs/2209.02244),
   a distinct data-driven setting that reinforces the need to state the
   dictionary, truncation, and convergence target.
