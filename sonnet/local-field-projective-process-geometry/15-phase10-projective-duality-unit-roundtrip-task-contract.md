# Phase 10 task contract — projective duality, unit one, and round-trip lowering

**Status:** frozen before Phase 10 execution.  This is a pre-result audit
contract.  Its distinctions, workloads, and kill conditions must not be
rewritten to fit the observed result.

**Planned executable owner:**
`tests/research/test_projective_duality_unit_roundtrip.py`.

**Planned result owner:**
`16-phase10-projective-duality-unit-roundtrip-results.md`.

## 1. Purpose

Phase 9 constructed a finite marked rational projective-history carrier whose
real and p-adic shadows commute with exact matrix lowering and task
projection.  It did not establish three facts needed by the proposed
objectification route:

1. that the operation called *duality* is a genuine duality preserving the
   relevant universal property;
2. that the full continued-fraction and stopping chain is projectively
   coherent once its unit, cusp, orientation, and ruler are declared;
3. that a geometric result can be lowered back to the arithmetic process at
   the information level required by the task.

Without those facts, a common source only proves an encoding direction.  A
bare hyperbolic point or p-adic lattice vertex may be a quotient of the
arithmetic process rather than a carrier on which the original process can be
solved and reconstructed.

Phase 10 therefore asks:

> Which precise duality is present, what does the marked unit (1) become at
> the real and p-adic places, and at which information level does the
> arithmetic--geometry--arithmetic round trip actually close?

The phase is an obstruction and reconstruction audit.  It must not assume
that a dual space, a missing fibre, or a successful encoding is a new
objectified dimension.

## 2. Starting correction — three operations called duality

Keep the following structures separate.

### 2.1 A/M group inversion

For the affine A/M group,

\[
(a,v)(b,w)=(a+e^v b,v+w),
\qquad
\iota(a,v)=(-e^{-v}a,-v).
\]

The map \(\iota\) is an anti-automorphism exchanging the left and right A/M
charts.  Phase 9 proved

\[
\Phi_R=\Phi_L\circ\iota,
\qquad
g_R=\iota^*g_L.
\]

This is not projective point--hyperplane duality.

### 2.2 Weyl and reciprocal operations

Use

\[
W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
W(z)=-1/z,
\]

and

\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
R(z)=1/z=D_{-1}W(z).
\]

These are projective transformations.  \(W\) preserves the upper half-plane;
the ordinary holomorphic \(R\) exchanges its two orientation components.
Neither operation is by itself the categorical dual functor.

### 2.3 Projective contragredient action

Let \(V=\mathbb Q^2\).  A line \([v]\in\mathbb P(V)\) has annihilator
\(\operatorname{Ann}(v)\in\mathbb P(V^*)\).  Under
\(g\in GL_2(\mathbb Q)\), annihilators transform by

\[
\operatorname{Ann}(gv)=g^{-T}\operatorname{Ann}(v).
\]

Put

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=W.
\]

For the coordinate identification \(v\mapsto Jv\) between a line and its
annihilator covector, the exact identity is

\[
\boxed{Jg=(\det g)g^{-T}J}.
\]

Hence the transported dual action is projectively

\[
[g^{-T}]=[JgJ^{-1}].
\]

This explains why rank-one projective geometry is self-dual after an explicit
identification.  It does not identify the single group element \(W\) with the
operation of dualizing every object and arrow.

### 2.4 Categorical duality

For a genuine contravariant equivalence

\[
D:\mathcal C^{op}\simeq\mathcal C',
\]

universal properties change variance:

```text
initial <-> terminal
coproduct <-> product
free / left-adjoint construction <-> cofree / right-adjoint construction
```

Phase 10 will use a finite ordered-category control to execute this reversal.
That control illustrates the logical law; it does not claim that the current
history, stopping, or local-place maps already form such an equivalence.

## 3. Primitive data and forbidden identifications

Use only:

- exact rational \(2\times2\) nonsingular matrices up to projective scale;
- homogeneous points of \(\mathbb P^1(\mathbb Q)\);
- literal Phase 9 Borel/Weyl words and their chronological products;
- the ordered standard projective frame
  \((0,1,\infty)\);
- the real base point \(i\) and exact upper/lower-half-plane action;
- the standard p-adic lattice root and finite projective contacts for
  \(p\in\{3,5,7\}\);
- declared metric weight \(c>0\), stopping data, and decoder semantics.

Forbidden identifications are:

1. group inversion = Weyl action = projective duality;
2. a universal property = an object with an attractive common-source role;
3. the boundary number \(1\) = the generator \(T_1\) = one metric/cost unit;
4. projective covariance = numerical invariance with the frame held fixed;
5. a bare local point = a projective frame = a literal history;
6. a canonical semantic lowering = recovery of the original word;
7. restoration of quotient fibres = a new process dimension.

## 4. Gate 10A — universal properties and exact rank-one duality

### 4.1 Variance control

Use the finite chain category

\[
0\longrightarrow1\longrightarrow2
\]

and the contravariant self-duality \(d(x)=2-x\).  Exhaustively verify:

- the initial object \(0\) maps to the terminal object \(2\);
- the terminal object maps to the initial object;
- joins/coproducts map to meets/products;
- applying \(d\) twice returns the original object and arrow.

The earned statement is only:

> A genuine duality preserves a universal **property in dual form**; it need
> not preserve the same kind of universal object.

### 4.2 Incidence and contragredient control

For every frozen nonsingular small rational matrix and nonzero small rational
vector, verify:

\[
Jgv=(\det g)g^{-T}Jv,
\]

projective incidence covariance, involutivity of \(g\mapsto g^{-T}\), and
composition of the transported dual action.

The executable must exhibit an explicit matrix, such as \(T_1\), for which
\(g^{-T}\ne W\).  Rank-one self-duality is mediated by \(J\); it is not the
claim that every transformation equals the Weyl element.

## 5. Gate 10B — projective coherence is marked covariance

Audit the chain

```text
literal T/D/W history
  -> rational projective matrix
  -> ordered rational projective frame
  -> real or p-adic local evaluation
  -> continued-fraction section / stopping task
  -> decoder / lowering.
```

For each arrow, record whether it is:

- exact and compositional;
- covariant only when a frame, cusp, orientation, unit, ruler, or stopping
  section is transported;
- many-to-one;
- outside the declared local geometry;
- invertible only on a declared image.

The full chain must not be called \(PGL_2\)-invariant.  Continued-fraction
digits privilege an affine chart, cusp, integer or residue section, direction,
and unit.  The correct positive target is a commuting diagram after those
marks are transported.

The reciprocal red team remains mandatory:

\[
W(\mathbb H)=\mathbb H,
\qquad
R(\mathbb H)=\overline{\mathbb H}^{-}.
\]

If the carrier is only the upper half-plane, the ordinary reciprocal is not
an internal geometric operation.

## 6. Gate 10C — unit one as an ordered projective frame

### 6.1 Projective normalization

The points \(0\) and \(\infty\) determine an affine chart but leave the scale
freedom

\[
D_k:z\mapsto kz.
\]

The third mark \(1\) fixes that freedom.  The executable must prove:

1. every \(D_k\) fixes \(0\) and \(\infty\) but sends \(1\) to \(k\);
2. an ordered triple of distinct rational projective points determines one
   projective matrix;
3. for every frozen matrix \(g\), reconstructing from
   \((g(0),g(1),g(\infty))\) returns \([g]\);
4. under a frame change the unit is transported to \(g(1)\); resetting it to
   the numeral \(1\) is an additional gauge normalization.

### 6.2 Real shadow

Keep three real meanings separate:

```text
boundary unit       the marked point 1 in (0,1,infinity)
process unit        T_1 : z -> z+1
metric unit         distance measured after choosing base point and c
```

At the Phase 9 base point,

\[
T_1(i)=1+i,
\qquad
d_{\mathbb H}(i,1+i)=2\operatorname{arsinh}(1/2).
\]

More generally,

\[
d_{\mathbb H}(iy,1+iy)=2\operatorname{arsinh}(1/(2y)),
\]

so the boundary difference \(1\) does not choose one intrinsic hyperbolic
length without a height/horocycle and curvature ruler.  The ordered boundary
frame determines an ideal triangle; an interior representative is a separate
convention.

### 6.3 p-adic shadow

For every frozen odd prime,

\[
T_1\in PGL_2(\mathbb Z_p).
\]

Therefore \(T_1\) fixes the standard Bruhat--Tits root vertex while acting
nontrivially on the projective boundary and outgoing residue directions.  The
executable must show both facts.  A root vertex cannot be the decoder of the
unit process.

## 7. Gate 10D — exact round-trip and information fibres

Separate four reconstruction targets.

### 7.1 A/M chart state

For \(z=x+iy\in\mathbb H\), the Phase 9 chart inverses are

\[
\Phi_L^{-1}(z)=(x,\log y),
\]

and

\[
\Phi_R^{-1}(z)=(-x/y,-\log y).
\]

These are exact chart round trips.  They reconstruct an A/M representative,
not a general projective transformation or its literal history.

### 7.2 Projective group element

The bare real symmetric-space projection has a stabilizer fibre:

\[
\mathbb H\simeq PSL_2(\mathbb R)/PSO(2).
\]

The exact red team is

\[
I(i)=W(i)=i,
\qquad I\ne W.
\]

The p-adic vertex projection has the compact stabilizer fibre
\(PGL_2(\mathbb Z_p)\); in particular \(I\) and \(T_1\) share the standard
root.

By contrast, the ordered frame

\[
(g(0),g(1),g(\infty))
\]

must reconstruct \([g]\) exactly on the frozen rational image.

### 7.3 Literal history

Even the full projective matrix does not recover its source word:

```text
empty word   -> I
T_1 T_-1     -> I.
```

A Bruhat/Borel factorization may supply a declared canonical semantic word,
but this is canonicalization modulo matrix semantics, not history inversion.

### 7.4 Local solver closure

Define the round-trip contract schematically as

\[
E:\mathcal H_{\mathbb Q}\to\widetilde X,
\qquad
S:\widetilde X\to\widetilde X,
\qquad
L:\operatorname{Im}_{\mathbb Q}(E)\to
\mathcal H_{\mathbb Q}/{\sim}.
\]

The positive gate is

\[
L\circ E=\operatorname{canonicalization}
\]

on the declared rational-frame image.  A geometric solver result outside
that image must return `outside_rational_lowering_image`, an approximation
certificate, or another explicit failure.  Local real and p-adic results are
not assumed to be two shadows of one rational object unless a common rational
frame certificate is supplied.

## 8. Gate 10E — objectification decision

Classify each possible carrier:

| candidate | expected reconstruction level |
| --- | --- |
| bare hyperbolic point | A/M/coset representative only |
| bare p-adic tree vertex | lattice homothety class only |
| ordered projective frame | rational matrix up to scalar, on its image |
| marked rational matrix | projective semantics, not literal word |
| marked literal history | chronological source and declared cost |

Restoring a frame, stabilizer, direction, or decoder fibre lost by a quotient
does not by itself create a vertical dimension.  A positive objectification
verdict still requires:

1. a task-independent new primitive;
2. free legal composites not already supplied by the lower grammar;
3. a lowering interpretation on every legal new composite;
4. sound mixed relations and retained decoder semantics;
5. a semantic or total-cost advantage after compilation and lowering.

If Phase 10 only improves the horizontal carrier and its decoder, the vertical
verdict remains negative.

## 9. Frozen workloads and budgets

Use exact arithmetic and bounded sets only:

- the three-object finite-chain duality control;
- all 496 nonsingular integer matrices with entries in \([-2,2]\);
- all Phase 9 Borel/Weyl words through length four, totalling 4,681 literal
  histories;
- small nonzero rational homogeneous vectors sufficient to exhaust the
  incidence identity for the frozen matrix set;
- primes \(p\in\{3,5,7\}\) at the standard root and depth-one projective
  contacts;
- symbolic A/M chart and hyperbolic-distance identities with declared
  \(c>0\).

The routine module must remain seconds-scale.  No floating-point equality,
unbounded projective search, infinite building construction, or selector
optimization is part of this phase.

## 10. Kill conditions

The proposal must be rejected or weakened if:

1. the operation called duality does not specify its source, target,
   variance, and transported marks;
2. an initial object is claimed to remain initial under an unexplained
   contravariant equivalence;
3. \(W\), \(R\), A/M group inversion, and \(g^{-T}\) are identified;
4. the rank-one incidence identity fails on exact rational data;
5. the number \(1\) is treated as projectively intrinsic without the ordered
   frame that fixes scale;
6. \(R=1/z\) is treated as an internal upper-half-plane isometry;
7. a hyperbolic point is claimed to recover \(W\), despite \(W(i)=i\);
8. a p-adic root vertex is claimed to recover \(T_1\), despite compact-root
   fixation;
9. an ordered frame fails to reconstruct its rational projective matrix;
10. matrix reconstruction is presented as recovery of the original literal
    word;
11. a local solver result is lowered without proving membership in the common
    rational image;
12. restoring lost marks is promoted to a new dimension without free
    composition and compositional lowering.

## 11. Solver-plan record

```text
Problem and task:
  audit genuine duality, the marked unit one, projective covariance, and
  arithmetic--geometry--arithmetic round trips before any objectification claim

Primitive process / constraints:
  exact rational T/D/W histories, homogeneous P1 points, ordered frames,
  real base point i, and standard finite p-adic observer data

Parameter regime and units:
  rational matrices, c>0 for the A/M metric, p in {3,5,7}; unit frame
  (0,1,infinity) kept distinct from T_1 and metric/cost units

Mathematical Core relation:
  refines the unit-frame, quotient/decoder, covariance, and objectification
  boundaries; tests whether the Phase 9 source supports a reversible carrier

Required lift and residuals:
  ordered projective frame, determinant/orientation component, rational-image
  certificate, literal history when chronological reconstruction is requested

Candidate presentations:
  categorical finite-chain duality control, projective contragredient action,
  ordered P1 frame, A/M charts, real hyperbolic point, p-adic lattice vertex

Adequacy certificates:
  exact universal-property reversal, incidence identity, frame reconstruction,
  chart inverse, stabilizer counterexamples, semantic canonical lowering

Selection cost / Pareto axes:
  no scalar selection; marks, matrix payload, literal history, local depth,
  decoder data, and lowering failure remain separate

Chosen algorithms:
  finite exhaustive category/poset checks, Fraction matrix arithmetic,
  homogeneous projective normalization, symbolic identities, local oracles

Symbolic evaluator:
  Python Fraction and SymPy

Numerical evaluator:
  not applicable

Decoder / reconstruction:
  ordered-frame-to-projective-matrix decoder; A/M chart inverses; declared
  Borel/Weyl semantic canonicalization; no original-word decoder claim

Error and failure semantics:
  repeated frame point, projective pole, orientation-component exit,
  noninjective local quotient, outside rational lowering image

Independent baselines:
  direct matrix action, Phase 9 place evaluation, finite category duality,
  stabilizer/orbit calculations

Red team / degeneration:
  I versus W at i; I versus T_1 at the p-adic root; zero/infinity without 1;
  W versus R; matrix equality versus word equality; irrational local output

Search and runtime budgets:
  frozen exact workloads in Section 9; routine seconds-scale test

Reproducibility data:
  exact alphabets, matrix/vector bounds, point normalization, primes, and
  expected fibre counts frozen in the executable

Current software layer:
  Sonnet-local research test only

Engineering Architecture effect:
  refine the presentation-transform, decoder, and failure contracts; no
  dependency or API change

Theory Map effect:
  expected refinement of the horizontal evaluation transversal and V2 red
  team; no maturity promotion

API pressure / explicit non-pressure:
  none
```

## 12. Completion boundary

Phase 10 is complete only when it supplies:

- a variance-correct answer to the universal-object premise;
- an exact separation of A/M inversion, Weyl/reciprocal action, projective
  contragredience, and categorical duality;
- a full marked-covariance ledger for the arithmetic-to-local chain;
- an exact account of the three meanings of unit one;
- real and p-adic stabilizer counterexamples to bare-point reconstruction;
- ordered-frame reconstruction on the frozen rational image;
- a semantic-versus-literal round-trip distinction and explicit failure for
  results outside the lowering image;
- an objectification verdict using new free composition and compositional
  lowering, not residual size or restored fibre dimension.

No outcome may promote a generic duality, universal carrier, projective frame,
local-field, building, round-trip, or objectification API.  No finite result
may prove an adelic completion, a canonical p-adic continued fraction,
Arithmetic Geometric Universality, or a new process rank.
