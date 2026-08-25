# Phase 0 — finite local-field certificates

**Status:** Gate 0 executable; exact rational/integer arithmetic only.

**Owner:** `tests/research/test_local_field_projective_process_geometry.py`

## 1. Why the first experiment is finite

The tempting route is to begin with a library for \(\mathbb Q_p\), draw a
Bruhat--Tits tree, and implement one named continued-fraction algorithm.  That
would answer the wrong first question.  It would show that established local-
field mathematics can be encoded, but it would not isolate which structure is
forced by the primitive arithmetic history and which structure arrived with
the imported package.

Phase 0 therefore stays over exact integers and rational numbers.  It uses
finite observations \(x\bmod p^n\), exact valuations, homogeneous projective
coordinates, and `Fraction`.  No analytic convergence is needed for any
passing assertion.

## 2. Certificate A — one process, two rulers

Take the literal Multiplication history containing \(n\) copies of the same
step \(D_p:x\mapsto px\).  Starting at one, its endpoint is

\[
x_n=p^n.
\]

The history and rational endpoint do not change.  Under the Archimedean ruler,
\(|x_n|_\infty=p^n\) increases.  Under the normalized \(p\)-adic ruler,

\[
|x_n|_p=p^{-n}
\]

decreases.  The test records both sequences exactly.  This is a finite witness
for place-relative geometry; the classical limiting statements follow without
being approximated numerically.

## 3. Certificate B — distinguishability builds a refinement tree

At resolution \(n\), define

\[
x\sim_{p,n}y
\iff x\equiv y\pmod {p^n}.
\]

On a complete finite window modulo \(p^N\), the test verifies:

- the level-\(n\) quotient has exactly \(p^n\) classes;
- level \(n+1\) refines level \(n\);
- a base-\(p\) digit prefix reconstructs the same level-\(n\) residue.

These facts give a rooted \(p\)-ary refinement of boundary observations.  They
do not construct the full Bruhat--Tits tree of lattice homothety classes.

## 4. Certificate C — the A/M ruler is covariant

For exact rational samples the test proves by evaluation:

\[
v_p((x+a)-(y+a))=v_p(x-y),
\]

\[
v_p(kx-ky)=v_p(k)+v_p(x-y).
\]

Thus Addition moves inside one local scale comparison, while Multiplication
transports comparison depth.  This is the discrete local-field counterpart of
the existing A/M relation in which Multiplication reorganizes Addition.  The
test does not identify valuation with the full A/M calculus: \(p\)-adic units
have zero valuation while retaining task-visible residue information.

## 5. Certificate D — left and right histories meet projectively

Using homogeneous points

\[
0=[0:1],\qquad \infty=[1:0],
\]

the test verifies that rational translations and dilations fix infinity,
whereas

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

exchanges zero and infinity.  This is the smallest exact shadow of the old AEG
left-affine/right-projective distinction.  Ordinary division by zero remains
inadmissible; homogeneous continuation is recorded separately.

## 6. Certificate E — continued-fraction lowering

For the stationary right reciprocal update

\[
F(z)=1+\frac1z,
\qquad
M=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]

the chronological history starting at \(1\) gives

\[
2,\quad\frac32,\quad\frac53,\quad\frac85.
\]

At every prefix, literal evaluation equals the action of the lowered matrix
product.  This is an exact finite continued-fraction certificate.  It does not
turn the infinite golden-ratio expression into a value without a separate
convergence argument.

## 7. Certificate F — projective maps transport local resolution

For a nonsingular Möbius map \(g\), Phase 0 verifies at several primes the
exact law

\[
v_p(gx-gy)
=v_p(\det g)+v_p(x-y)
-v_p(Cx+D)-v_p(Cy+D).
\]

The denominator terms are essential.  Removing them would falsely treat a
moving projective chart as a fixed isometry and would hide the approach to a
pole.  This identity is the most substantive initial bridge to the current
observer/ruler program.

## 8. Red team — digit sections are not observer-free canonical forms

At \(p=5\), precision three, the same residue \(4\bmod125\) has two exact
digit histories:

\[
(4,0,0)
\qquad\text{and}\qquad
(-1,1,0).
\]

Both reconstruct the same residue.  The standard section uses fewer nonzero
digits; the balanced section has smaller total digit amplitude:

\[
C_{\mathrm{nonzero}}(4,0,0)=1<2
=C_{\mathrm{nonzero}}(-1,1,0),
\]

\[
C_{\mathrm{amplitude}}(-1,1,0)=2<4
=C_{\mathrm{amplitude}}(4,0,0).
\]

No contradiction exists because the rulers differ.  The result rejects only
the stronger claim that finite residue semantics selects a unique digit
presentation without a task cost.

## 9. Claim ledger

### Exact finite statements

1. place-relative scale sequences for the fixed history \(D_p^n\);
2. nested residue quotients and digit-prefix reconstruction;
3. Addition isometry and Multiplication valuation covariance;
4. homogeneous affine/inversion action;
5. right-reciprocal history/matrix endpoint agreement;
6. Möbius denominator valuation law;
7. the two-cost digit-section defect.

### Structural interpretations under test

- place choice is an observer choice capable of inducing process geometry;
- valuation is a transported discrete ruler for the multiplicative direction;
- finite right-reciprocal histories are the correct process precursor of
  continued-fraction coding;
- the refinement tree is a boundary interface to, rather than a replacement
  for, Bruhat--Tits geometry.

### Open claims

- reconstruction of the full Bruhat--Tits tree from process/task data;
- a canonical relation between tree geodesics and a selected \(p\)-adic
  continued-fraction algorithm;
- convergence, finiteness, periodicity, and complexity comparisons between
  competing algorithms;
- effective \(p\)-adic analytic closure using precision/error transport,
  Hensel lifting, derivatives, or ODEs;
- an adelic resource vector or product-formula comparison across places;
- any generic local-field or valuation API.

## 10. Next gates

The research order after Gate 0 is:

```text
exact boundary/refinement certificates
    -> full finite lattice-class model of the Bruhat--Tits ball
    -> real continued-fraction/geodesic positive control
    -> two p-adic digit/continued-fraction selectors under matched tasks
    -> convergence, reconstruction, and cost red teams
    -> only then an effective-analysis or cross-place synthesis claim.
```

The next implementation should freeze a finite lattice/coset oracle and prove
that its boundary truncations recover the residue observations used here.  It
must not begin by extending the framework API.
