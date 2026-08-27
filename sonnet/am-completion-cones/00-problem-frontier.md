# AM completion cones and bigraded chamber transport

Status: T0 mathematical contract for issue
[#148](https://github.com/mountain/process-geometry/issues/148).

## 1. Why this question follows from the first compiler

The completed AM power--weight compiler in PR #147 established an exact
rank-one observer calculus. It did **not** yet construct the completion of the
entire native AM algebra.

Write

\[
X_{\nu,\kappa}
=a^\nu e^{\kappa v},
\qquad
\kappa=w-\nu.
\]

Then

\[
X_{\nu,\kappa}X_{\mu,\lambda}
=X_{\nu+\mu,\kappa+\lambda},
\]

\[
A X_{\nu,\kappa}
=\nu X_{\nu-1,\kappa},
\qquad
M X_{\nu,\kappa}
=(\nu+\kappa)X_{\nu,\kappa}.
\]

The intrinsic degree group is therefore

\[
G=\mathbb Z\oplus\Lambda,
\]

with coordinates `(power degree, exponential character)`.  The
`M`-weight is the derived linear functional

\[
w(\nu,\kappa)=\nu+\kappa.
\]

The first compiler's single weight coordinate is an abstract rank-one
completion coordinate.  It can be embedded along a declared homogeneous ray
of `G`, but the compiler does not yet record that embedding.  Its completion
evidence must therefore be read as **ray-local**.

This distinction is mathematical, not an implementation detail.

## 2. The completion problem

Let `K` be a commutative exact `Q`-algebra and let

\[
C\subset G_{\mathbb R}
\]

be a rational cone.  Put

\[
S=C\cap G.
\]

The candidate completed monoid algebra is

\[
K[[S]]
=\left\{
\sum_{g\in S}c_gX^g
\right\}.
\]

This notation is legitimate only if every requested product coefficient has
finitely many contributing decompositions.  A sufficient structure is:

1. `C` is finitely generated and rational;
2. `C` is pointed, so `C` contains no nonzero line;
3. an observer height
   \(h:G_{\mathbb R}\to\mathbb R\) is strictly positive on
   \(C\setminus\{0\}\).

The observer then sees only

\[
S_{\le N}^{h}
=\{g\in S:h(g)\le N\}.
\]

The first theorem target is that this set is finite.

## 3. Algebra versus chambers

The cone algebra `K[[S]]` is only the zero chamber.  A finite Laurent shift
produces a translated support sector

\[
\mathcal H_{g_0,C}
=K[[g_0+S]].
\]

These sectors are modules rather than copies of one untyped algebra:

\[
\mathcal H_{g_0,C}\,
\mathcal H_{g_1,C}
\longrightarrow
\mathcal H_{g_0+g_1,C}.
\]

The AM generators have exact degree behaviour

\[
A:
\mathcal H_{g_0,C}
\longrightarrow
\mathcal H_{g_0-e_\nu,C},
\]

\[
M:
\mathcal H_{g_0,C}
\longrightarrow
\mathcal H_{g_0,C},
\]

where \(e_\nu=(1,0)\).

Away from resonance, an `A`-primitive has the opposite transport

\[
P_A:
\mathcal H_{g_0,C}
\longrightarrow
\mathcal H_{g_0+e_\nu,C}.
\]

At \(\nu=-1\), the coefficient \((\nu+1)^{-1}\) does not exist and the
typed `log-a` extension is forced.  This is a codimension-one resonance wall
inside the chamber system, not a reason to insert `log(a)` into the base
algebra.

## 4. Frozen questions

The research must answer:

1. Is a pointed rational cone enough for a useful completed AM calculus?
2. Are `A` and its primitive correctly understood as chamber transports?
3. Do different positive observer heights define the same completion but
   different finite costs?
4. Can exact `exp` and `log1p` be defined on the positive augmentation ideal
   without enlarging the coefficient algebra beyond the frozen domain?
5. Which support obstruction, if any, genuinely forces Hahn, transseries, or
   surreal structure?

## 5. Controls

Positive controls:

- recover the PR #147 rank-one evaluator as a ray `S=N rho`;
- use a two-generator pointed cone and prove finite coefficient convolution;
- compare two positive heights on the same cone;
- replay `A`, `M`, ordinary primitive transport, and `log-a` resonance;
- compute one mixed two-ray completed coefficient exactly.

Negative controls:

- reject a nonpointed cone;
- reject a height that vanishes on a nonzero support ray;
- exhibit the failure of one pointed cone to be translation-invariant in both
  power directions;
- reject a general degree-zero exponential whose constant coefficient would
  require an undeclared exponential closure;
- keep symbolic-height iteration outside the fragment.

## 6. Claim ceiling

This work may justify finitely generated rational bigraded completion and
typed chamber transport.  It may not claim:

- a general Hahn field or transseries algebra;
- a surreal runtime;
- symbolic-height hyperiteration;
- a full multivariable AM function theory;
- a complexity or performance theorem;
- Core, Theory Map, or Public API promotion.

The required disposition is exactly one of `CONE`, `CHAMBERS`, `RAY-ONLY`, or
`HIGHER-SUPPORT`.
