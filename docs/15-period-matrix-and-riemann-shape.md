# From lifted cycles to a candidate period matrix

The branch-continuation layer made a single closed lifted history measurable. The next step is to assemble enough independent histories to expose the matrix structure behind Abelian inversion.

## 1. Period blocks

For a genus-\(g\) curve with canonical holomorphic differentials

\[
\omega_1,\ldots,\omega_g,
\]

and supplied closed lifted cycles

\[
a_1,\ldots,a_g,b_1,\ldots,b_g,
\]

Shakespeare now measures

\[
A_{ij}=\oint_{a_j}\omega_i,
\qquad
B_{ij}=\oint_{b_j}\omega_i.
\]

If \(A\) is invertible, the normalized candidate matrix is

\[
\tau=A^{-1}B.
\]

`AbelianCycleSystem` checks that the caller has supplied exactly `g` A-cycles and `g` B-cycles, that every cycle belongs to the same curve, and that every path actually closes on the lifted square-root surface.

`compute_period_matrix` then integrates every canonical differential over every supplied cycle.

## 2. Riemann shape versus Riemann certificate

For a genuine symplectic homology basis, the classical Riemann bilinear relations imply

\[
\tau^T=\tau,
\qquad
\operatorname{Im}\tau>0.
\]

The current `AbelianPeriodMatrix` checks these numerical *matrix-shape* properties. It deliberately does **not** call them a proof of the Riemann bilinear relations, because the library does not yet compute the cycle intersection form.

This distinction is important:

\[
\boxed{
\text{period matrix with the right shape}
\neq
\text{certified symplectic homology presentation}.
}
\]

The missing certificate is topological, not merely numerical.

## 3. Pendulum IV

For

\[
Y^2=2U(U^2-1),
\]

we take two explicit ellipses in the base plane:

- one enclosing \(\{-1,0\}\),
- one enclosing \(\{0,1\}\).

Both have even branch parity and therefore close after square-root continuation. Direct integration of

\[
\omega=\frac{dU}{Y}
\]

produces

\[
\Omega_A\approx 3.708149\ldots,
\qquad
\Omega_B\approx i\,3.708149\ldots.
\]

Thus the measured normalized matrix is

\[
\tau=\frac{\Omega_B}{\Omega_A}\approx i.
\]

This agrees independently with the lemniscatic `j=1728` algebraic shadow and with the automorphism argument developed in the previous calibration.

The full cited executable essay is `tests/classical/test_pendulum_period_matrix.py`.

## 4. Interpretation

The sequence is now

\[
\boxed{
\text{process quotient}
\to
\text{canonical differential}
\to
\text{history lift}
\to
\text{closed cycles}
\to
\text{period blocks}
\to
\tau.
}
\]

**Shakespeare interpretation.** The period matrix is a finite compression of how a vector of canonical history coordinates fails to return around independent closed histories.

The classical mathematics is the theory of Abelian differentials and period matrices. The history-language interpretation is the project contribution.

## 5. Next obstruction

The next missing object is not the Jacobian itself. It is the intersection structure of the cycle system.

A trustworthy next stage should therefore implement:

1. a reusable representation of branch cuts and lifted cycles;
2. cycle intersection / symplectic-pairing data;
3. automatic or semi-automatic construction of a canonical cycle system for controlled hyperelliptic families;
4. only then a genuine Riemann-bilinear certificate;
5. only after that, the quotient \(\mathbb C^g/(\mathbb Z^g+\tau\mathbb Z^g)\) as a Jacobian representation.

This preserves the project rule that a classical object enters `src/` only after the process/history machinery has forced the abstraction that supports it.
