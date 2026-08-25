# Phase 1 — finite lattice-class ball and affine boundary contact

**Status:** Gate 1 exact finite oracle complete; full ball around the standard
vertex at declared radius; no infinite completion and no framework API.

**Owner:** [test_local_field_projective_lattice_ball.py](../../tests/research/test_local_field_projective_lattice_ball.py)

## 1. The question left open by Phase 0

Phase 0 built the refinement

\[
\mathbb Z/p\mathbb Z
\longleftarrow
\mathbb Z/p^2\mathbb Z
\longleftarrow\cdots
\]

from finite observer distinctions.  It deliberately called this a boundary
shadow rather than the Bruhat--Tits tree.  That caution was necessary: the
level-\(n\) residue observer has \(p^n\) states, whereas the sphere of radius
\(n\) in the \((p+1)\)-regular Bruhat--Tits tree has

\[
(p+1)p^{n-1}=p^n+p^{n-1}
\]

vertices.  The missing \(p^{n-1}\) vertices are not bookkeeping.  They form
the second projective chart, and inversion moves information between the two
charts.

Gate 1 therefore asks a narrower exact question:

> Can the Phase 0 residue tower be embedded, without changing its semantics,
> into a finite lattice-class model that has the correct projective charts,
> parent maps, valencies, and inversion action?

The answer is yes at every declared finite radius.

## 2. Classical oracle and finite normal form

Let \(R_n=\mathbb Z/p^n\mathbb Z\).  A pair

\[
(a,b)\in R_n^2
\]

is primitive when \(a\) and \(b\) are not both divisible by \(p\).
Multiplication by a unit of \(R_n\) does not change its projective class.
Thus the finite projective line is

\[
\mathbb P^1(R_n)
=
\{(a,b)\text{ primitive}\}/R_n^\times.
\]

To a class \([a:b]\), attach the normalized lattice

\[
L_{[a:b]}
=
\{(x,y)\in\mathbb Z_p^2:
ax+by\equiv0\pmod {p^n}\}.
\]

Its quotient from the standard lattice is cyclic of order \(p^n\), so its
homothety class lies at distance \(n\) from the standard vertex.  Conversely,
each vertex at that distance has one such normalized representative.  This is
the classical lattice-class oracle used by the test; it is not presented as a
Process Geometry discovery.

Every primitive class has exactly one of two normal forms:

\[
[r:1],
\qquad r\in R_n,
\]

or

\[
[1:pt],
\qquad t\in\mathbb Z/p^{n-1}\mathbb Z.
\]

The charts are disjoint and give the exact count

\[
\#\mathbb P^1(R_n)
=p^n+p^{n-1}
=(p+1)p^{n-1}.
\]

The executable oracle constructs integral bases:

\[
L_{[r:1]}
=\left\langle(1,-r),(0,p^n)\right\rangle,
\]

\[
L_{[1:pt]}
=\left\langle(p^n,0),(-pt,1)\right\rangle.
\]

Both determinants have absolute value \(p^n\).  The test also reconstructs
the exact basis coordinates of every member in complete finite residue
windows; determinant agreement alone is not used as a membership proof.

## 3. Reduction constructs the finite ball

Reducing a primitive pair modulo \(p^{n-1}\) gives the unique parent:

\[
\rho_n:
\mathbb P^1(R_n)
\longrightarrow
\mathbb P^1(R_{n-1}).
\]

At the first layer, the standard root has \(p+1\) children.  At every later
layer, each projective class has \(p\) children and one parent.  Therefore the
ball of radius \(N\) has

\[
1+(p+1)\frac{p^N-1}{p-1}
\]

vertices.  The test verifies:

1. this vertex count for \(p=2,3,5\);
2. exactly one parent for every non-root vertex;
3. \(p+1\) incident edges at the root and every interior vertex;
4. one incident edge at the truncated outer sphere;
5. connectivity by repeated parent reduction;
6. edge count equal to vertex count minus one.

These jointly certify that the generated finite graph is the complete ball
around the standard lattice vertex, not merely a drawing with the expected
number of nodes.

## 4. Phase 0 becomes an exact affine contact chart

The Phase 0 residue \(r\bmod p^n\) maps to the affine projective class

\[
\iota_n(r)=[r:1].
\]

This preserves refinement:

\[
\rho_n\circ\iota_n
=
\iota_{n-1}\circ
(r\bmod p^{n-1}).
\]

It also turns residue observation into lattice incidence.  For an observed
integer \(x\),

\[
x\equiv r\pmod {p^n}
\quad\Longleftrightarrow\quad
(1,-x)\in L_{[r:1]}.
\]

Thus the earlier observer quotient is recovered without approximation as a
contact test against a normalized lattice.  This is the first nontrivial gain
of the phase: the boundary description and the lattice description are joined
by an explicit evaluator, not only by matching cardinalities.

The affine image contains \(p^n\) of the
\(p^n+p^{n-1}\) sphere vertices.  It is therefore an exact chart and a proper
subset.  At depth one its root has only \(p\) visible affine directions, while
the complete projective ball has \(p+1\).

## 5. Why bilateral inversion forces projective completion

Addition and multiplication by a \(p\)-adic unit preserve the affine chart.
Right-slot division contributes the projective inversion

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
[a:b]\longmapsto[-b:a].
\]

At fixed depth, \(J\) exchanges

\[
\{[1:pt]\}
\quad\text{with}\quad
\{[r:1]:p\mid r\}.
\]

Both sets have \(p^{n-1}\) elements.  The test proves the exchange is a
bijection and that \(J^2\) is the identity on projective classes.

This gives the precise relation to the earlier left/right expansion study:
the left affine sector can remain inside one residue chart, but right
inversion makes the missing projective chart dynamically unavoidable.  The
extra branch is therefore forced by the bilateral process alphabet, not
inserted only to reproduce a classical picture.

## 6. Canonicalization red teams

### Raw-pair overcount

There are

\[
p^{2n}-p^{2n-2}
\]

primitive pairs modulo \(p^n\), but each lattice kernel is repeated by

\[
\varphi(p^n)=p^n-p^{n-1}
\]

unit multiples.  The test exhausts all primitive pairs for \(p=3,n=2\) and
proves that unit-projective canonicalization and equality of finite kernel
truth tables induce exactly the same partition.

### Affine-only undercount

The residue presentation omits exactly \(p^{n-1}\) sphere vertices.  It also
fails closure under inversion.  It remains sufficient for the restricted
integral residue task, but it is insufficient for the bilateral projective
task.

These are complementary failures:

- retaining raw pairs preserves semantics but carries avoidable gauge
  duplication;
- retaining only affine residues removes genuine task-visible projective
  states.

The responsible presentation is therefore task-relative: quotient units, but
do not quotient away the second chart when inversion is admissible.

## 7. Effective-analysis audit

- **Mode:** exact finite symbolic arithmetic.
- **Closure:** unit normalization, parent reduction, lattice membership, and
  matrices invertible modulo \(p\).
- **Evaluator:** congruence membership and exact integral basis coordinates.
- **Certificates:** kernel-partition equality, determinant/index witnesses,
  graph counts and degrees, refinement/contact commutation, and inversion
  bijection.
- **Failure semantics:** nonprimitive pairs, nonpositive projective depth,
  invalid chart coordinates, nonmember coordinate requests, and matrices
  singular modulo \(p\) are rejected explicitly.
- **Baseline:** raw primitive-pair enumeration and the Phase 0 affine-only
  residue tree.
- **Cost boundary:** the canonical sphere stores
  \(p^n+p^{n-1}\) classes instead of
  \(p^{2n}-p^{2n-2}\) raw pairs; no asymptotic or runtime superiority beyond
  this exact finite count is claimed.
- **Numerical analysis:** not applicable; no approximation, convergence, or
  floating-point path is used.

## 8. Claim ledger and Theory Map effect

### Exact statements

1. primitive unit classes and normalized finite lattice kernels coincide in
   the exhausted oracle;
2. the two-chart normal forms enumerate every radius-\(n\) sphere vertex;
3. reduction builds the complete finite standard-root ball with the correct
   regular-tree incidences;
4. Phase 0 residues embed as an exact affine contact chart;
5. projective inversion forces exchange with the missing chart.

### Interpretation

The result upgrades the earlier “boundary shadow” statement: the residue
refinement is not the whole Bruhat--Tits geometry, but it is an exact affine
observer patch inside a full finite lattice-class ball.  This **refines** the
H2 reading of the living Theory Map by identifying the additional projective
completion required by the process alphabet.  It leaves the Theory Map file
and all API maturity levels unchanged.

### Still open

- the infinite inverse-limit boundary and its topology;
- geodesic coding by real or \(p\)-adic continued fractions;
- selection among competing \(p\)-adic digit algorithms;
- convergence, periodicity, Hensel lifting, derivatives, and ODEs;
- a cross-place or adelic resource law;
- any generic lattice, local-field, tree, or valuation API.

## 9. Next gate

This gate has now been executed in
[`03-phase2-real-continued-fraction-geodesic-control.md`](03-phase2-real-continued-fraction-geodesic-control.md):
ordinary continued-fraction prefixes are compiled into exact convergent
matrices, Stern--Brocot paths, Farey frames, and ordered real cylinders.  The
result is a positive control, not an identification of the real tree with the
Bruhat--Tits tree.  The next gate is therefore a matched finite comparison of
two genuinely different \(p\)-adic selectors on one frozen task.
