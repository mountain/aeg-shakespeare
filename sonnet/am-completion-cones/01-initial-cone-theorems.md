# Initial theorems for AM completion cones

Status: T1 exact deductions inside the frozen rational-polyhedral scope.

## 1. Setup

Let

\[
G=\mathbb Z\oplus\Lambda
\]

be a rank-two lattice after clearing the denominator of the rational
rank-one character lattice `Lambda`.  Let

\[
X^g=X_{\nu,\kappa}=a^\nu e^{\kappa v},
\qquad
g=(\nu,\kappa).
\]

Fix a finitely generated rational cone

\[
C=\mathbb R_{\ge0}s_1+\cdots+\mathbb R_{\ge0}s_r
\]

and its affine monoid `S=C cap G`.  A height `h` is admissible when

\[
h(s_i)>0
\]

for every nonzero generator.

## 2. Finite-observer theorem

**Theorem 2.1.**  If `C` is pointed and rational polyhedral and `h` is
admissible, then for every real `N` the observer set

\[
S^h_{\le N}=\{g\in S:h(g)\le N\}
\]

is finite.

**Proof.**  Because `h` is strictly positive on the compact section of `C`
obtained by intersecting it with a unit sphere, there is a constant `c>0`
such that

\[
h(x)\ge c\lVert x\rVert
\qquad (x\in C).
\]

Thus `h(x)<=N` implies `||x||<=N/c`.  A lattice has only finitely many points
in a bounded set.  Hence the observer set is finite.  \(\square\)

**Corollary 2.2.**  For any `g in S`, the set of decompositions

\[
\{(p,q)\in S^2:p+q=g\}
\]

is finite.

Indeed, admissibility gives

\[
0\le h(p),h(q)\le h(g),
\]

so both entries lie in a finite observer set.

Therefore the coefficient

\[
[X^g](fg)
=\sum_{p+q=g} [X^p]f\,[X^q]g
\]

is a finite exact sum even when `f` and `g` have infinite support in `S`.

## 3. Completed exp and log

Let

\[
\mathfrak m
=\left\{f\in K[[S]]:[X^0]f=0\right\}.
\]

For `u in m`, define

\[
\exp(u)=\sum_{n\ge0}\frac{u^n}{n!},
\qquad
\log(1+u)=\sum_{n\ge1}\frac{(-1)^{n+1}}n u^n.
\]

**Theorem 3.1.**  Every target coefficient of these two expressions is a
finite exact sum.

**Proof.**  Let

\[
\epsilon
=\min\{h(s):s\in S\setminus\{0\}\}>0.
\]

The minimum exists because Theorem 2.1 makes every bounded observer slice
finite, while strict positivity excludes zero.

Every nonconstant monomial in `u^n` has height at least `n epsilon`.
Consequently only

\[
n\le h(g)/\epsilon
\]

can contribute to the coefficient at target `g`.  Each product coefficient is
finite by Corollary 2.2.  \(\square\)

This theorem deliberately assumes zero constant term.  If a general
degree-zero coefficient `c_0(a)` is allowed inside an exponential, then
`exp(c_0(a))` need not belong to the frozen coefficient algebra.  The rational
constant case handled by PR #147 is a declared narrow extension, not evidence
for arbitrary degree-zero exponential closure.

## 4. Observer-height cofinality

The observer height is not unique.

**Theorem 4.1.**  Let `h_1` and `h_2` both be admissible on the same finitely
generated cone.  Then their filtrations are cofinal: there exist constants
`0<c<=C` such that

\[
c\,h_1(x)\le h_2(x)\le C\,h_1(x)
\qquad (x\in C).
\]

**Proof.**  On the compact unit section of the pointed cone, the positive
continuous ratio `h_2/h_1` has a positive minimum and a finite maximum.
\(\square\)

**Corollary 4.2.**  The two heights define the same completed algebra and the
same convergent formal objects, but generally assign different finite
observer horizons and different dependency costs.

This is the precise form of a useful geometric principle:

> an interior observer chart may change computational economy without
> changing the completed carrier.

## 5. Bidirectional invariant-cone no-go

Let `e_nu=(1,0)`.

**Proposition 5.1.**  No pointed cone `C` containing zero can satisfy both

\[
C+e_\nu\subseteq C
\qquad\text{and}\qquad
C-e_\nu\subseteq C.
\]

**Proof.**  Applying the two inclusions to zero gives

\[
e_\nu\in C,
\qquad
-e_\nu\in C.
\]

Thus `C` contains the nonzero line `R e_nu`, contradicting pointedness.
\(\square\)

This no-go concerns literal closure, not continuity.  It does not imply that
differentiation or primitive transport is unavailable.

## 6. Bounded-shift continuity

For a translated chamber

\[
\mathcal H_{g_0,C}=K[[g_0+S]],
\]

the AM operators satisfy

\[
A:\mathcal H_{g_0,C}\to\mathcal H_{g_0-e_\nu,C},
\qquad
M:\mathcal H_{g_0,C}\to\mathcal H_{g_0,C}.
\]

**Proposition 6.1.**  These maps are continuous for every admissible height.

**Proof.**  `M` preserves degree.  `A` translates every degree by the fixed
vector `-e_nu`; therefore it translates every height by the fixed scalar
`-h(e_nu)`.  Given an output horizon, increasing the input horizon by that
fixed amount suffices.  \(\square\)

Away from the resonance wall `nu=-1`, the termwise primitive

\[
P_A X_{\nu,\kappa}
=\frac1{\nu+1}X_{\nu+1,\kappa}
\]

is the opposite continuous chamber transport.  On the wall, its codomain
must be enlarged by a typed `log-a` sector.

## 7. Initial disposition

The exact deductions already rule out a naive `CONE` interpretation in which
one pointed support cone is literally invariant under both power directions.
They do **not** force higher support such as surreal or Hahn structure.

The leading disposition is therefore

\[
\boxed{\texttt{CHAMBERS}}
\]

subject to the frozen two-generator and paired-observer calibrations.

The emerging object is a chambered completed algebra:

- pointed cones provide locally finite multiplication and completion;
- interior heights are observer charts on one completion;
- `A` and ordinary primitives transport between translated sectors;
- resonance walls force typed extensions;
- stronger support orders enter only if a later frozen task defeats every
  admissible rational-polyhedral chamber system.
