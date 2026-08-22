# Real branch data as a cycle grammar

The previous global-history stages deliberately accepted cycles from the caller. That was enough to make monodromy, period integration, period matrices, and sampled intersection pairing executable, but it left one important classical object unexplained: the homology basis itself.

For a smooth real-split even-degree hyperelliptic quotient

\[
y^2=c\prod_{j=1}^{2g+2}(x-e_j),\qquad e_1<\cdots<e_{2g+2},
\]

the branch order already carries a standard cut presentation. Pair adjacent branch points into cuts

\[
[e_1,e_2],\ [e_3,e_4],\ldots,[e_{2g+1},e_{2g+2}].
\]

The last pair is used as a reference cut. Shakespeare's restricted real-split constructor emits

\[
a_i:\ \text{around }[e_{2i-1},e_{2i}],
\]

and nested

\[
b_i:\ \text{around the even branch set }e_{2i},e_{2i+1},\ldots,e_{2g+1},
\]

for \(i=1,\ldots,g\). With the canonical orientations this construction has

\[
a_i\cdot a_j=b_i\cdot b_j=0,\qquad a_i\cdot b_j=\delta_{ij},
\]

hence the A-then-B intersection matrix

\[
J=\begin{pmatrix}0&I_g\\-I_g&0\end{pmatrix}.
\]

This is classical hyperelliptic topology. Farkas--Kra give the Riemann-surface background; Frauendiener and Klein treat hyperelliptic surfaces computationally from branch-point lists or cut systems and construct a canonical homology basis algorithmically. See `[Farkas-Kra-1992]` and `[Frauendiener-Klein-2015]` in `REFERENCES.md`.

## Shakespeare's separation of certificates

The implementation deliberately keeps two objects apart.

The **construction certificate** consists of the ordered branch points, the A/B interval specifications, and the exact target symplectic form. This is the mathematical statement attached to the branch-cut grammar.

The **sampled realization** consists of ellipses in the base plane, continuous square-root lifts, numerically measured surface intersections, and numerical period integrals. These can fail independently because of inadequate sampling, bad contour geometry, or branch-continuation errors.

So the execution pattern is

```text
ordered branch locus
    -> cut pairing
    -> A/B cycle specification
    -> exact target intersection form
    -> sampled base contours
    -> lifted histories
    -> measured intersection form
    -> period matrix
```

The comparison

```text
measured intersection == construction intersection
```

is therefore not circular. It is a numerical realization checking itself against an independently emitted topological contract.

## Why the B cycles are nested

For the real branch order the B-cycle associated with `a_i` encloses the consecutive branch set beginning at the right endpoint of `a_i` and ending at the left endpoint of the final reference cut. Thus later A-cycles lie inside earlier B-contours rather than crossing them. Only the boundary sharing the dual cut produces an A/B intersection.

Under the implementation's convention that every sampled contour begins at its rightmost point and the square-root continuation starts on the principal branch, successive nested B-cycles acquire alternating lifted orientation. The sampled base direction is therefore alternated so that the realized cycles obey the chosen canonical convention

\[
a_i\cdot b_i=+1.
\]

This convention is not part of the topology itself; it is the explicit bridge between the abstract symplectic orientation and the concrete square-root sheet convention used by the numerical engine.

## First genus-two calibration

The research vignette `tests/research/test_real_branch_cycle_presentation.py` uses

\[
y^2=(x^2-1)(x^2-4)(x^2-9)
\]

with branch points

\[
-3<-2<-1<1<2<3.
\]

The emitted cycle grammar is

```text
A1: {-3,-2}
A2: {-1, 1}
B1: {-2,-1,1,2}
B2: {1,2}
reference cut: {2,3}
```

and the construction target is

\[
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
-1&0&0&0\\
0&-1&0&0
\end{pmatrix}.
\]

The purpose of the test is not merely to recover this matrix. It asks whether the same constructed histories also feed the canonical differentials

\[
\frac{dx}{y},\qquad \frac{x\,dx}{y},
\]

and produce a normalized \(2\times2\) period matrix with the Riemann symmetry and positive-imaginary-part shape.

If that succeeds, the key advance is conceptual and computational:

\[
\boxed{\text{branch geometry}\to\text{cycle grammar}\to\text{symplectic history}\to\text{period data}.}
\]

The homology presentation is no longer an opaque input between the algebraic quotient and the Abelian-function layer.

## Boundary

This module is intentionally narrower than a general Riemann-surface homology engine. It assumes all `2g+2` branch points are finite, real, distinct, supplied explicitly, and already ordered. The sampled cycles are ellipses chosen to realize the known real-cut topology. Arbitrary complex branch configurations, automatic cut pairing, deformation-certified intersections, and Tretkoff--Tretkoff-style general algebraic-curve homology remain outside the present implementation.
