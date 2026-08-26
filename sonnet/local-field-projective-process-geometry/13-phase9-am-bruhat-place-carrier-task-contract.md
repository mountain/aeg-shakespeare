# Phase 9 task contract — A/M–Bruhat duality and a place-indexed continued-fraction carrier

**Status:** frozen before Phase 9 execution.  This is a pre-result audit
contract; its hypotheses, workloads, and kill conditions must not be rewritten
to fit the observed comparison maps.

**Planned executable owner:**
`tests/research/test_am_bruhat_place_continued_fraction_carrier.py`.

**Planned result owner:**
`14-phase9-am-bruhat-place-continuation-carrier-results.md`.

## 1. Purpose

Phase 8 proved that the finite p-adic continuation residual is an exact stable
task-state extension, but not a uniform new dimension.  It also exposed a
remaining ambiguity: the audited carrier was a tagged union of finite task
states, not one task-independent object.  Some boundary, merging, and twisting
may therefore be induced by projection to different stopping and decoder
quotients.

The proposed repair begins upstream, at the shared arithmetic process rather
than at the residual.  Addition and positive Multiplication form an affine, or
Borel, process.  A reciprocal/Weyl operation adds the missing projective chart.
Over the real place this algebra acts on a hyperbolic homogeneous space and
supports the classical modular-geodesic coding of regular continued fractions.
Over a non-Archimedean place the same rational matrices act on the
Bruhat--Tits lattice tree and its projective boundary.

The Phase 9 question is:

> Can the literal rational A/M-plus-reciprocal history, its oriented projective
> frame, and its composition law serve as one task-independent carrier whose
> real and p-adic geometries are compatible place evaluations, and whose
> finite selector tasks are stopping/decoder quotients rather than unrelated
> tagged state spaces?

This is plausible, but four notions must remain separate:

1. the free/universal property of a declared history grammar;
2. a task-independent rational projective carrier;
3. a family of compatible local-place evaluations;
4. Arithmetic Geometric Universality or a new vertical process rank.

Phase 9 may establish the first three for a finite exact calibration.  It must
not infer the fourth.

## 2. Starting correction: the A/M premise is conditional

The existing AEG calibrations prove exact objectification, new free
composition, and compositional lowering for Translation and positive
Multiplication processes.  They do **not** prove that one A/M metric is
canonical or that A/M is a theorem-level mother object for all local-field
geometry.

Likewise, the existing A/M observer metric

\[
g_c=\theta_A^2+c\theta_M^2,
\qquad c>0,
\]

is declared data.  Its hyperbolic realization can be exact without selecting a
canonical value of \(c\), a canonical scalar cost, or a universal completion.
Phase 9 therefore tests an explicit candidate comparison; it does not begin by
assuming the desired universality.

## 3. Primitive A/M group and the two inversions

### 3.1 Affine process group

Use real A/M coordinates \((a,v)\) with affine action

\[
x\longmapsto e^v x+a.
\]

Composition and inverse are

\[
(a,v)(b,w)=(a+e^v b,v+w),
\]

\[
\iota(a,v)=(-e^{-v}a,-v).
\]

The existing process frame and its dual coframe are

\[
A=\partial_a,
\qquad
M=\partial_v+a\partial_a,
\qquad [A,M]=A,
\]

\[
\theta_A=da-a,dv,
\qquad
\theta_M=dv.
\]

The map \(\iota\) is **group inversion inside the affine A/M group**.  It
exchanges left- and right-invariant descriptions.  It is not the projective
reciprocal below.

### 3.2 Rational projective grammar

For a field \(K\), use

\[
T_t=\begin{pmatrix}1&t\\0&1\end{pmatrix},
\qquad
D_k=\begin{pmatrix}k&0\\0&1\end{pmatrix},
\qquad k\ne0,
\]

and distinguish

\[
W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad W(z)=-\frac1z,
\]

from

\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad R(z)=\frac1z.
\]

They satisfy

\[
R=D_{-1}W.
\]

Here \(W\) is the rank-one Weyl operation preserving the real upper
half-plane, while \(R\) is the reciprocal used in ordinary positive continued
fractions.  The sign dilation \(D_{-1}\) is task-visible at the real oriented
frame level and may be partly hidden by a p-adic compact quotient.  These two
operations must never be silently identified.

## 4. Gate 9A — exact A/M hyperbolic duality

Construct two exact upper-half-plane charts.

The affine-action chart is

\[
\Phi_L(a,v)=a+i e^v.
\]

Pulling back the Poincare metric gives

\[
g_L=e^{-2v}da^2+dv^2.
\]

The process-frame chart is

\[
\Phi_R(a,v)=-a e^{-v}+i e^{-v}.
\]

It gives

\[
\Phi_R^*g_{\mathbb H}
=(da-a,dv)^2+dv^2
=\theta_A^2+\theta_M^2
=g_R.
\]

The executable must prove the exact comparison

\[
\Phi_R=\Phi_L\circ\iota,
\qquad
g_R=\iota^*g_L.
\]

Thus the existing A/M process metric and the affine-action metric are two
group-inversion-dual hyperbolic realizations.  Equality after applying
\(\iota\) is not permission to erase history orientation.

For the weighted family, determine explicitly whether

\[
g_c=(da-a,dv)^2+c,dv^2
\]

is a coordinate/overall rescaling of a hyperbolic metric and record its
curvature scale.  No value of \(c\) may be called canonical without a separate
ruler-selection argument.

## 5. Gate 9B — Borel/Weyl projective completion

Let \(B(K)\subset PGL_2(K)\) be the upper-triangular affine subgroup.  Verify
constructively that every nonsingular matrix

\[
g=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\]

lies either in \(B(K)\), when \(C=0\), or in the opposite Bruhat cell
\(B(K)WB(K)\).  For \(C\ne0\), retain and check the exact factorization

\[
g=
\begin{pmatrix}\Delta/C&A/C\\0&1\end{pmatrix}
W
\begin{pmatrix}C&D\\0&1\end{pmatrix},
\qquad
\Delta=AD-BC.
\]

This is the proposed algebraic mother step:

```text
A/M affine/Borel chart + one Weyl reciprocal
    -> complete rational projective matrix carrier.
```

The executable must additionally retain:

- chronological word order before matrix lowering;
- matrix columns as an oriented projective frame;
- determinant sign/valuation and the action of right multiplication by
  \(W\) or \(R\) on that frame;
- poles and chart changes as explicit outcomes.

The factorization theorem establishes projective generation.  It does not
select digits, a local metric, a fundamental domain, or a task cost.

## 6. Gate 9C — real continued fractions as a section, not a space

Reuse the exact Phase 2 regular continued-fraction workload.  For every digit
\(a\), retain

\[
M(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix}=T_aR
=T_aD_{-1}W.
\]

Certify that finite products agree simultaneously with:

1. literal right-reciprocal histories;
2. rational endpoints;
3. oriented consecutive-convergent/Farey frames;
4. canonical Stern--Brocot paths and cylinders;
5. the Borel/Weyl word with its orientation/sign record.

At the real place, \(W(z)=-1/z\) preserves the upper half-plane, while
\(R(z)=1/z\) exchanges upper and lower half-planes.  The executable must show
that the sign dilation accounts for this difference and that the alternating
determinant of continued-fraction frames is not lost.

The geometric statement to test is not that a continued fraction is a point of
\(\mathbb H\).  It is that a digit sequence is a declared symbolic section or
cutting code for an oriented projective/geodesic process associated with the
modular action.  Endpoint-only equality remains invalid for future-prefix
tasks.

## 7. Gate 9D — place-indexed local shadows

Keep the rational projective carrier fixed and change only the place.

For the real place, compare with

\[
X_\infty=PGL_2(\mathbb R)/PO(2),
\]

using the upper-half-plane realization and oriented Farey data.

For each frozen odd prime \(p\), compare with the finite part of

\[
X_p=PGL_2(\mathbb Q_p)/PGL_2(\mathbb Z_p),
\]

using the existing exact lattice-class ball.  Only finite vertices and
projective contacts are executable claims; the infinite building is a
classical control.

Both local spaces have projective boundary language

\[
\partial X_v\simeq\mathbb P^1(\mathbb Q_v),
\]

and the common rational frame maps into each place.  The following square must
commute on every frozen word:

\[
\begin{array}{ccc}
\text{literal rational history}&\longrightarrow&PGL_2(\mathbb Q)\\
\downarrow&&\downarrow\\
\text{place-observed history}&\longrightarrow&
\text{local frame/lattice shadow}.
\end{array}
\]

The real hyperbolic plane and the p-adic tree must not be identified.  They are
different local homogeneous/building shadows of a shared rational action
carrier.

### 7.1 Sign/unit red team

At the real place, \(D_{-1}\) changes the orientation component relevant to
\(R\) versus \(W\).  At an odd p-adic place, \(D_{-1}\) belongs to the compact
integral stabilizer of the standard vertex: it fixes that vertex but may
permute outgoing projective directions.  Measure exactly which local
interfaces see the sign and which quotient it away.  Do not infer global
invisibility from root fixation.

## 8. Gate 9E — universal continuation-carrier test

Construct a finite envelope \(U_H\) from untruncated rational projective-frame
histories through one frozen horizon \(H\).  Task data such as precision,
stopping depth, scalar ruler, and terminal decoder must be projections from
\(U_H\), not tags used to define disjoint source states.

For each task \(T\), define a projection

\[
q_T:U_H\longrightarrow Z_T
\]

to its observed/stopped response carrier.  The executable must test:

1. **history compatibility:** concatenation before stopping commutes with
   \(q_T\);
2. **place compatibility:** rational matrix lowering followed by local
   evaluation equals direct place evaluation of the history;
3. **task refinement:** when one stopping/decoder task refines another, a
   comparison map between their quotients makes the triangle from \(U_H\)
   commute;
4. **residual provenance:** every Phase 8 split is classified as retained
   rational-frame data, place-observer data, stopping/decoder data, or a
   remaining interaction;
5. **twisting diagnosis:** terminal, invalid, and many-to-one arrows are
   recomputed upstairs and downstairs to determine which are induced by task
   projection.

Passing these tests would earn the phrase **finite task-independent
continuation carrier with compatible local shadows**.  It would not establish
an initial/terminal object in an unspecified category, an adelic completion,
or a new dimension.

## 9. Frozen workloads and budgets

Use only exact arithmetic and bounded workloads:

- the Phase 2 canonical continued-fraction/Farey words through its existing
  depth-eight exhaust;
- rational Borel/Weyl words through depth five over a frozen small alphabet of
  translations, nonzero dilations including \(-1\), and \(W\);
- primes \(p\in\{3,5,7\}\) and finite lattice depths through four;
- the mandatory Phase 7/8 immediate residual, transported-future,
  changed-stopping, and full-decoder witnesses;
- one common continuation horizon no larger than the existing Phase 8 maximum
  of 24 for the universal-envelope comparison.

Per-word matrix numerators/denominators and per-task graph sizes must be
reported.  A bounded exact test may stop with `inconclusive_within_budget`; it
must not sample silently or use floating-point equality.

The routine Phase 9 module should remain seconds-scale.  Any open prime, depth,
or word sweep belongs in an opt-in research script, not the default suite.

## 10. Kill conditions

The proposed bridge must be weakened or rejected if any of the following
occurs.

1. The claimed A/M hyperbolic charts fail the exact pullback or group-inversion
   identity.
2. The process-frame metric and affine-action metric are identified without
   the inversion/comparison map.
3. \(R=1/z\) and \(W=-1/z\) are identified after their orientation or sign
   payload becomes task-visible.
4. Borel/Weyl lowering loses chronological history or oriented-frame data
   required by continuation.
5. A real Farey/geodesic section is treated as intrinsic to the p-adic tree, or
   a p-adic selector is imported as canonical.
6. The task projections cannot be defined from one common \(U_H\) without
   smuggling task tags back into the carrier.
7. A task-refinement triangle fails to commute.
8. The same rational word gives incompatible matrix lowering before local
   evaluation.
9. A declared universal carrier lacks a stated category, comparison maps, or
   negative case.
10. Compatible local shadows are promoted to one metric space, an adelic
    theorem, Arithmetic Geometric Universality, or vertical objectification
    without the additional laws.

## 11. What would count as vertical objectification

Even a successful Phase 9 supplies a horizontal/place-indexed mother carrier.
To raise process rank, a later phase must still provide:

1. task-independent new primitives, not merely existing rational matrices;
2. a free grammar generating composites beyond the frozen histories;
3. a lowering interpretation defined on every legal new composite;
4. sound mixed relations with the lower A/M/projective grammar;
5. a demonstrated semantic or cost advantage with decoder/lowering charged.

Thus the proposed universal carrier may explain Phase 8 twisting without
turning the residual into a dimension.  Universality of source and vertical
objectification are orthogonal gates.

## 12. Solver-plan record

```text
Problem and task:
  test an A/M-Borel plus Weyl rational carrier for real/p-adic continued
  fractions and for Phase 8 task-quotient provenance

Primitive process / constraints:
  literal rational Translation, nonzero Dilation, reciprocal/Weyl histories;
  chronological composition; exact projective frames

Parameter regime and units:
  real A/M coordinates with positive metric weight c; rational matrices;
  odd primes and bounded depths/word lengths in Section 9

Mathematical Core relation:
  tests the mother-object and place-relative observer boundary; does not
  assume Arithmetic Geometric Universality or dimension increase

Required lift and residuals:
  literal word, rational matrix up to declared projective scaling, oriented
  frame, determinant sign/valuation, local shadow, and task stopping payload

Candidate presentations:
  left/right A/M hyperbolic charts; Borel/Weyl words; regular continued
  fractions; real Farey frames; p-adic lattice contacts; common U_H envelope

Adequacy certificates:
  exact metric pullbacks, group-inverse square, Bruhat factorization,
  word/matrix/frame replay, place-evaluation squares, task-refinement triangles

Selection cost / Pareto axes:
  no preferred scalarization; literal steps, stored digits, Farey turns,
  lattice depth, residual state, and decoder/lowering remain separate

Chosen algorithms:
  exact symbolic differential pullback, rational 2x2 matrix normalization,
  bounded word exhaust, existing Farey and lattice oracles, finite response
  projection and partition comparison

Symbolic evaluator:
  SymPy identities plus Python integer/Fraction arithmetic

Numerical evaluator:
  not applicable

Decoder / reconstruction:
  continued-fraction convergent/frame decoder and frozen p-adic task decoders

Error and failure semantics:
  explicit poles, invalid words/actions, terminal/stopping outcomes, budget
  exhaustion, and comparison-square failure

Independent baselines:
  Phase 2 Farey control, Phase 1 lattice ball, Phase 8 stable quotients,
  direct literal action replay, and independent matrix factorization

Red team / degeneration:
  group inverse versus projective reciprocal; R versus W; determinant
  orientation; sign unit at real/p-adic places; endpoint versus frame;
  stopping/decoder task changes; metric weight c

Search and runtime budgets:
  frozen finite sets in Section 9; default module remains seconds-scale

Reproducibility data:
  every alphabet, word bound, matrix normalization, local depth, witness,
  projection map, and exact count frozen in executable snapshots

Current software layer:
  Sonnet-local research test only

Engineering Architecture effect:
  expected refine/support or explicit obstruction; no dependency/API change

Theory Map effect:
  pending result; no mother-object, local-field, building, or rank promotion

API pressure / explicit non-pressure:
  none
```

## 13. Completion boundary

Phase 9 is complete only when it supplies:

- exact left/right A/M hyperbolic comparison and metric-weight boundary;
- constructive Borel/Weyl completion with reciprocal-sign audit;
- real continued-fraction/Farey replay through the projective grammar;
- compatible finite real and p-adic place-evaluation squares;
- one common finite continuation envelope and explicit task projections;
- task-refinement commutativity or a minimal exact obstruction;
- a provenance classification of the Phase 8 residual witnesses;
- cost, failure, universality, and vertical-objectification claim ledgers.

No outcome may identify the real hyperbolic plane with the Bruhat--Tits tree,
select a canonical p-adic continued fraction, prove an adelic completion,
promote A/M to a theorem-level mother object, or infer a new process dimension
from a shared rational matrix carrier alone.
