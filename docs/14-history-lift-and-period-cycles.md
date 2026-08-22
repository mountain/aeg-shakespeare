# History lift and explicit period cycles

The first Abelian layer stopped just before the hard global step: it knew the canonical differentials and the rank of first homology, but it did not yet know how a path moves from one sheet of `y^2=P(x)` to the other.

This note records the next executable layer.

## 1. Why branch continuation is a history problem

For a square-root quotient

\[
y^2=P(x),
\]

the visible coordinate `x` does not determine a single global value of `y`. Along a path in the punctured `x`-plane, the sign of the square root must be continued from the previous point.

A closed base loop can therefore satisfy

\[
x(T)=x(0)
\]

while its lift satisfies

\[
y(T)=-y(0).
\]

This is the elementary monodromy of a branched double cover.

**Shakespeare interpretation.** The base state has returned, but the lifted process history has not. The deck transformation is a residual of history that is invisible in the base quotient.

The phrase *history residual* is project terminology. The classical fact is analytic continuation / monodromy of algebraic functions; see Forster and Farkas--Kra in `docs/REFERENCES.md`.

## 2. Bounded continuation algorithm

`lift_square_root_path` receives a sampled complex path

\[
x_0,x_1,\ldots,x_N
\]

that avoids branch points. At each sample it evaluates the two candidates

\[
\pm\sqrt{P(x_k)}
\]

and chooses the candidate closest to the previously selected value.

The returned `LiftedSquareRootPath` keeps both the base samples and the selected sheet values. For a closed base loop it reports a `sheet_multiplier`:

- `+1`: the lifted path returns to the same sheet;
- `-1`: the base loop closes but the lift ends on the other sheet.

This is a numerical continuation method, not a certified topology engine. It requires sufficiently fine sampling and a path separated from branch points.

## 3. First monodromy calibration

The research vignette

`tests/research/test_square_root_history_monodromy.py`

uses

\[
y^2=x^2-1.
\]

It verifies:

- one loop around one branch point flips the sheet;
- one loop around both branch points returns to the original sheet;
- two loops around one branch point return to the original sheet.

Thus the distinction between visible state return and lifted history return is now executable independently of elliptic-function language.

## 4. Integrating a canonical differential on the lift

Once a lifted path is known, `integrate_lifted_differential` evaluates

\[
\int_\gamma x^k\,\frac{dx}{y}
\]

using the selected sheet values along the path.

The current backend is a complex trapezoidal rule. This is adequate for convergence calibrations on smooth sampled contours but does not provide rigorous interval error bounds.

## 5. Pendulum III: an actual period

For the symmetric pendulum energy `E=0`, the quotient is

\[
Y^2=2U(U^2-1),
\qquad
\omega=\frac{dU}{Y}.
\]

The test

`tests/classical/test_pendulum_period_contour.py`

chooses an ellipse in the `U`-plane enclosing the branch points `-1` and `0` but not `+1`. The continued square-root lift closes, and integration gives a nonzero period.

The same period has the independent real-cut expression

\[
\Omega_A
=2\int_{-1}^{0}\frac{dU}{\sqrt{2U(U^2-1)}}
=\frac{1}{\sqrt2}B\!\left(\frac14,\frac12\right).
\]

The contour computation converges to this beta value.

The exact automorphism

\[
(U,Y)\mapsto(-U,iY)
\]

sends

\[
\omega\mapsto i\omega,
\]

so it supplies an independent period

\[
\Omega_B=i\Omega_A.
\]

`GenusOneLattice` then records

\[
\tau=\frac{\Omega_B}{\Omega_A}=i,
\]

matching the lemniscatic square lattice and the previously recovered `j=1728` Weierstrass shadow.

## 6. What has changed conceptually

Before this layer the chain was

\[
\text{process}
\to
\text{quotient curve}
\to
\text{genus}
\to
\text{canonical differentials}.
\]

Now it continues as

\[
\boxed{
\text{base path}
\to
\text{lifted history}
\to
\text{monodromy}
\to
\text{closed lifted cycle}
\to
\text{period measurement}.
}
\]

That is the first computational bridge from local process data to global Riemann-surface history.

## 7. Boundary and next node

Still missing are:

1. automatic construction of a homology basis;
2. adaptive branch-aware contour refinement;
3. a full `g x 2g` period matrix;
4. normalization to `tau=A^{-1}B`;
5. numerical/exact checks of the Riemann bilinear relations;
6. a Jacobian object built only after those structures are stable.

The next implementation should therefore generalize from a single lifted cycle to a *cycle system* rather than jumping directly to a `Jacobian` class.
