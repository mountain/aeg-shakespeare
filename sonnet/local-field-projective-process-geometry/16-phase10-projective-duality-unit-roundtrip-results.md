# Phase 10 — projective duality, unit one, and round-trip lowering

**Status:** Gates 10A--10E complete for the frozen exact workload.  The audit
proves rank-one projective incidence duality and exact ordered-frame
reconstruction, but rejects the stronger claims that the current end-to-end
solver chain is a dual equivalence, that a bare local geometric point can be
decoded to its arithmetic process, or that projective self-duality creates a
new objectified dimension.

**Executable owner:**
[test_projective_duality_unit_roundtrip.py](../../tests/research/test_projective_duality_unit_roundtrip.py)

**Frozen task:**
[15-phase10-projective-duality-unit-roundtrip-task-contract.md](15-phase10-projective-duality-unit-roundtrip-task-contract.md)

## 1. Verdict

The three questions that motivated Phase 10 now have distinct answers.

### Universal objects

A genuine duality preserves a universal property **after reversing its
variance**.  Initial becomes terminal, coproduct becomes product, and a free
construction may become a cofree one.  Therefore the premise

```text
universal object -> universal object
```

is valid only in the qualified form

```text
universal property -> dual universal property.
```

The current history-to-matrix, place-evaluation, stopping, and decoder maps
are information-losing projections, not one demonstrated contravariant
equivalence.  No categorical universal-object conclusion may yet be
transported through the full chain.

### Projective coherence

The rational algebraic backbone is projectively coherent.  The full
continued-fraction solver is coherent only as a **marked covariant** chain:
the cusp, affine chart, ordered frame, orientation, unit, ruler, stopping
section, and decoder must be transported.  Holding those marks fixed while
acting on the point is not projective invariance.

### Unit and round trip

The projective unit \(1\) is the third mark in the ordered frame

\[
(0,1,\infty).
\]

It fixes the scale left undetermined by \((0,\infty)\).  It is not identical
to the process generator \(T_1\) or to one hyperbolic/tree/cost unit.

For the frozen rational image, the enhanced round trip is

\[
\boxed{
[g]
\longleftrightarrow
(g(0),g(1),g(\infty)).
}
\]

The corresponding round trip fails for a bare hyperbolic point, a bare
p-adic lattice vertex, and an original literal word.  The ordered frame
recovers projective matrix semantics; it does not recover chronology.

The earned carrier refinement is therefore:

> **a rationally marked ordered projective frame with an explicit
> rational-image and decoder contract.**

This remains a horizontal reconstruction refinement, not a new process rank.

## 2. Gate 10A — what duality is actually present

### 2.1 Universal-property variance

The executable uses the exact finite category

\[
0\longrightarrow1\longrightarrow2
\]

with the contravariant involution

\[
d(x)=2-x.
\]

All nine ordered object pairs satisfy

\[
x\le y
\quad\Longleftrightarrow\quad
d(y)\le d(x).
\]

The initial and terminal objects are \(0\) and \(2\), and

\[
d(0)=2,
\qquad
d(2)=0.
\]

For every pair,

\[
d(\max(x,y))=\min(d(x),d(y)).
\]

Thus the finite control executes the exact reversal

\[
\text{coproduct/join}\longleftrightarrow\text{product/meet}.
\]

This is not offered as a model of all continued-fraction algorithms.  Its role
is to block the incorrect inference that a contravariant equivalence must send
an initial/free object to another initial/free object of the same type.

The interesting live hypothesis is consequently narrower:

> If the marked rational history carrier eventually has a genuine free
> universal property, its dual may be a cofree observer or decoder rather
> than a second free history carrier.

Phase 10 does not construct that category or adjunction.

### 2.2 Exact projective incidence duality

Let

\[
J=W=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

For every nonsingular frozen matrix \(g\) and vector \(v\), exact arithmetic
verifies

\[
\boxed{Jgv=(\det g)g^{-T}Jv}.
\]

The audit covers:

- 496 nonsingular integer matrices with entries in \([-2,2]\);
- 24 nonzero integer vectors with coordinates in \([-2,2]\);
- 11,904 exact incidence checks.

Writing \(Jv\) as the annihilator covector of \(v\), the identity proves

\[
\langle g^{-T}Jv,gv\rangle=0.
\]

It also proves, projectively,

\[
[g^{-T}]=[JgJ^{-1}].
\]

The transported dual action is involutive and compositional on all 4,681
frozen words through length four.

### 2.3 The decisive limitation of the duality proposal

In projective dimension one, points and hyperplanes are both one-dimensional
projective data.  After choosing the annihilator identification \(J\), the
contragredient action is conjugate to the original action.

Therefore:

> Rank-one projective self-duality supplies an exact comparison of
> presentations, but it does not by itself produce an independent dual
> geometric dimension.

The single matrix \(W\) participates in the identification, but dualizing a
transformation is not the same operation as applying \(W\) to a point.  For
example,

\[
T_1^{-T}=
\begin{pmatrix}1&0\\-1&1\end{pmatrix}
\ne W.
\]

This separates:

```text
A/M group inversion       reverses affine process composition
Weyl W                    one projective group element
reciprocal R              D_-1 W, changes the real component
contragredient g^-T       transported action on the dual projective line
categorical duality       reverses arrows and universal-property variance
```

## 3. Gate 10B — where the complete chain is projectively coherent

The executable freezes the following ledger.

| Arrow | Exact composition | Marks required | Information forgotten | Reverse boundary |
| --- | --- | --- | --- | --- |
| literal history \(\to\) matrix | yes | chronological order | source word and literal cost | semantic canonicalization only |
| matrix \(\to\) ordered frame | yes | \(0,1,\infty\), orientation | none at projective-matrix level | exact on nonsingular rational frames |
| matrix \(\to\) real point | yes | base point and component | real stabilizer fibre | coset representative only |
| matrix \(\to\) p-adic vertex | yes | prime, lattice root, valuation ruler | integral stabilizer and boundary direction | lattice class only |
| local geometry \(\to\) CF section | no unmarked naturality | cusp, chart, unit, section, orientation | unchosen representatives | declared section image only |
| local result \(\to\) rational lowering | conditional | rational-image certificate, decoder, stopping trace | original word | certified rational frame image only |

The first four arrows are exact evaluations.  The last two are selections or
partial reconstructions.  They become commuting comparisons only after their
marks and domains are declared.

### 3.1 Reciprocal remains a component-changing operation

At the real base point,

\[
W(i)=i,
\qquad
R(i)=-i.
\]

Thus \(W=-1/z\) is an upper-half-plane symmetry, while the holomorphic
ordinary reciprocal \(R=1/z\) leaves that component.  An end-to-end carrier
containing \(R\) must either:

- retain both orientation components;
- use \(W\) and record the sign operation separately;
- or adopt a different anti-holomorphic convention and state that change.

The algebraic identity \(R=D_{-1}W\) does not make \(R\) an internal
isometry of one upper half-plane.

### 3.2 Continued-fraction digits are not projective invariants

Regular real continued fractions select a cusp, ordered integer frame, and
cross-section of modular geodesic flow.  A p-adic selector additionally
selects a prime, affine chart, residue representatives, and stopping rule.

Under a projective transformation \(g\), one may transport all these data and
compare the conjugated algorithms.  One may not transform only the point and
expect the original digit string to remain numerically invariant.

The correct target for the next phase is therefore a naturality square for
**marked sections**, not one coordinate-free digit function on the bare local
space.

## 4. Gate 10C — unit one fixes the projective gauge

### 4.1 Why two points are insufficient

Every nonzero dilation

\[
D_k=\begin{pmatrix}k&0\\0&1\end{pmatrix}
\]

fixes \(0\) and \(\infty\) but sends

\[
1\longmapsto k.
\]

Hence \((0,\infty)\) determines an affine chart only up to scale.  Adding the
third point \(1\) removes this freedom.  The phrase “unit one” in the
projective layer means precisely this third frame mark.

For any ordered triple \((p_0,p_1,p_\infty)\) of distinct rational projective
points, choose homogeneous representatives

\[
u=p_\infty,
\qquad
v=p_0,
\qquad
w=p_1.
\]

With \(\Delta=\det(u,v)\), put

\[
s=\frac{\det(w,v)}{\Delta},
\qquad
t=\frac{\det(u,w)}{\Delta}.
\]

Then

\[
g=[su\;tv]
\]

is the unique projective matrix satisfying

\[
g(0)=p_0,
\qquad
g(1)=p_1,
\qquad
g(\infty)=p_\infty.
\]

### 4.2 Exact finite frame census

The 4,681 frozen literal words lower to 1,585 distinct projective matrices.
Their ordered-frame census is also exactly 1,585:

\[
\boxed{
\#\{[g]\}
=
\#\{(g(0),g(1),g(\infty))\}
=1585.
}
\]

Every ordered frame reconstructs its normalized matrix exactly.  By contrast:

- 827 projective matrix classes have more than one literal-word preimage;
- the largest literal-word fibre contains 47 words.

The unit-marked frame is therefore sufficient for projective semantics but
not for history semantics.

### 4.3 Three meanings of unit in the real geometry

Keep separate:

1. the boundary mark \(1\) in \((0,1,\infty)\);
2. the process operation \(T_1:z\mapsto z+1\);
3. a metric unit after choosing a base point, horocycle, and curvature scale.

At the Phase 9 base point,

\[
T_1(i)=1+i.
\]

For height \(y>0\),

\[
\cosh d_{\mathbb H}(iy,1+iy)
=1+\frac1{2y^2},
\]

so

\[
\boxed{
d_{\mathbb H}(iy,1+iy)
=2\operatorname{arsinh}\frac1{2y}.
}
\]

At \(y=1\), this becomes

\[
d_{\mathbb H}(i,1+i)=2\operatorname{arsinh}(1/2).
\]

Thus the arithmetic difference \(1\) does not choose one hyperbolic length.
The metric family \(g_c\) introduces the additional curvature ruler
\(K=-1/c\).

### 4.4 The p-adic unit is invisible at the root but visible at the boundary

For \(p=3,5,7\), exact lattice evaluation gives

\[
[T_1\mathbb Z_p^2]=[\mathbb Z_p^2].
\]

The standard root vertex therefore cannot distinguish \(I\) from \(T_1\).
Nevertheless,

\[
T_1(0)=1,
\]

and the depth-one projective contacts \(0\) and \(1\) are distinct at every
frozen prime.

This is more than a technical exception.  It proves that the projective unit
must live in the marked boundary/frame data if the arithmetic unit operation
is to be reconstructed.  Radial tree distance alone cannot carry it.

## 5. Gate 10D — what comes back after geometric calculation

### 5.1 Exact A/M chart return

The two chart inverses close exactly:

\[
\Phi_L^{-1}(x+iy)=(x,\log y),
\]

\[
\Phi_R^{-1}(x+iy)=(-x/y,-\log y).
\]

So a result inside one declared A/M chart returns an A/M state.  It does not
return an arbitrary \(PGL_2\) transformation that may have produced the same
point.

### 5.2 Bare real points lose the compact fibre

The smallest exact counterexample is

\[
I(i)=W(i)=i,
\qquad I\ne W.
\]

This is the visible shadow of

\[
\mathbb H\simeq PSL_2(\mathbb R)/PSO(2).
\]

The finite census makes the loss quantitative.  The 1,585 projective matrix
classes produce only 1,291 exact real points:

- 268 real points have more than one projective-matrix preimage;
- the largest real-point fibre contains four projective matrices.

The real point is therefore an observer quotient, not a matrix decoder.

### 5.3 Bare p-adic vertices lose a much larger compact fibre

Even when the three vertex shadows at \(p=3,5,7\) are retained together, the
same 1,585 projective matrices produce only 284 vertex triples:

- 105 triples have more than one projective-matrix preimage;
- the largest fibre contains 206 projective matrices.

The explicit \(I/T_1\) root collision is one member of this general compact
stabilizer phenomenon.  Tree vertices remain valuable evaluation and stopping
geometry, but they are far from a rational-frame decoder.

### 5.4 Ordered frames recover matrix semantics

For all 1,585 frozen projective matrices,

\[
(g(0),g(1),g(\infty))
\longmapsto[g]
\]

round-trips exactly.  For all 496 nonsingular small matrices, the constructive
Borel/Weyl lowering

\[
[g]\longmapsto
\begin{cases}
T_{b/d}D_{a/d},&c=0,\\
T_{a/c}D_{\det(g)/c}
WT_dD_c,&c\ne0
\end{cases}
\]

returns the same projective matrix.

This gives a valid semantic decoder on the rational-frame image.

### 5.5 Matrix semantics still do not recover literal history

Phase 9's simplest relation remains decisive:

```text
empty word -> I
T_1 T_-1  -> I.
```

The Borel/Weyl decoder returns one canonical semantic representative, not the
original chronological word or its cost.  A task requesting literal
reconstruction must retain that history as residual data.

### 5.6 Solver outputs require an image-closure certificate

An arbitrary real geometric calculation need not return a rational frame.
The executable distinguishes:

\[
\sqrt2 I,
\]

which is projectively rational because it is a scalar multiple of \(I\), from

\[
\begin{pmatrix}\sqrt2&0\\0&1\end{pmatrix},
\]

which has no rational projective representative.

Therefore a valid lowering result must be one of:

```text
success_exact_on_rational_frame_image
success_certified_approximate_with_decoder
outside_rational_lowering_image
```

The present phase implements the first and exact negative witness for the
third.  It does not construct an approximate global/local solver.

## 6. Consequence for the proposed real/p-adic bridge

The proposal to use reciprocal or projective duality to compare the real A/M
hyperbolic model with a geometry capable of carrying continued fractions is
partly validated and partly narrowed.

The topological distinction is structural, not a missing change of
coordinates.  The real place has its Archimedean connected topology.  At the
p-adic place the strong triangle inequality

\[
|x-z|_p\le\max(|x-y|_p,|y-z|_p)
\]

makes balls clopen and any two balls disjoint or nested; the resulting space
is totally disconnected.  Finite projective cylinders and paths in the
Bruhat--Tits tree are the executed shadows of this nested refinement.  They
cannot be identified with open regions of the real hyperbolic plane.  The
shared \(PGL_2(\mathbb Q)\) carrier is deliberately placed before either
completion: changing place equips its local image with a different topology.

The current tests construct only finite tree balls, cylinder contacts, and
place evaluations.  They do not construct the full infinite Bruhat--Tits
boundary, prove a p-adic completion theorem, or supply an adelic product
topology.

What survives is:

```text
marked rational projective history/frame
    -> real marked section
    -> p-adic marked section
```

with exact incidence duality and compatible place evaluation.

What does not survive is:

```text
one hyperbolic space
    --duality--> a new independent space
    -> automatic p-adic objectification.
```

In rank one, projective duality is internally conjugate after choosing \(J\).
It reorganizes point/covector and history/observer roles; it does not generate
a new spatial rank.  The genuinely different geometry still comes from
changing the place, not from dualizing the real hyperbolic plane.

The next useful carrier is consequently not the bare product

\[
\mathbb H\times\prod_p\mathcal T_p,
\]

because arbitrary local points in that product need not arise from one
rational frame.  The correct finite research object has the opposite order:

\[
\boxed{
\text{one marked rational frame certificate}
\quad+\quad
\text{its place-indexed decorated shadows}.
}
\]

This order makes lowering a declared obligation rather than an accidental
hope.

## 7. Objectification verdict

Phase 10 strengthens the negative vertical verdict.

The dual action

\[
g\mapsto g^{-T}
\]

is already expressible within the existing rational projective grammar up to
conjugation and rational Borel/Weyl lowering.  The ordered frame restores
information lost by a quotient.  Neither supplies:

- a task-independent new generator;
- a higher free grammar;
- new composites outside the lower projective semantics;
- a new mixed relation requiring a higher-rank lowering theorem.

Hence the V2--V4 ledger is

```text
stable marked reconstruction       yes, on the rational frame image
new primitive                       no
new free composition                no
new all-composite lowering law      no
vertical objectification            no
```

This does not refute objectification as a general Process Geometry mechanism.
It refutes the specific inference that projective self-duality or restoration
of a missing local fibre is enough to objectify a new dimension.

## 8. What Phase 10 says about the earlier intuition

The earlier intuition was that twisting or closure appeared because the
discussion had begun below a sufficiently universal object.  Phase 10 gives a
more exact version.

Supported:

- bare hyperbolic points and tree vertices are strong quotients;
- their stabilizer fibres erase precisely the unit, orientation, and frame
  data needed by reconstruction;
- moving upstream to the marked rational frame removes these artificial
  ambiguities.

Not yet supported:

- that the marked rational frame is an initial, terminal, free, or otherwise
  categorical universal object;
- that duality carries it to an object of the same universal type;
- that every compatible local calculation returns to the rational image.

So the right correction is not “we have found the universal object.”  It is:

> We have identified the minimum extra marks needed for an exact finite
> projective-semantic round trip, and we can now state the missing universal
> property and solver-closure obligations without hiding them in a local
> quotient.

## 9. Claim and cost ledger

### Exact finite/algebraic statements

1. Finite-chain duality reverses initial/terminal and join/meet exactly.
2. The identity \(Jg=(\det g)g^{-T}J\) holds on 11,904 frozen
   matrix/vector pairs.
3. The contragredient action is involutive and compositional on 4,681 frozen
   words.
4. All 1,585 distinct rational projective matrices reconstruct from their
   ordered \((0,1,\infty)\) frames.
5. The exact real and three-prime p-adic fibre counts are those in Section 5.
6. All 496 small nonsingular matrices lower through one constructive rational
   Borel/Weyl semantic word.
7. The A/M chart inverses and hyperbolic unit-step identity hold symbolically.
8. \(T_1\) fixes every frozen p-adic root and moves the depth-one boundary
   contact from \(0\) to \(1\).

### Declared costs

The routine Phase 10 module contains six exact tests and runs in about 1.5
seconds on the reference execution.  It reuses Phase 9's rational alphabet,
SymPy, and finite local oracles.  It adds no dependency, package module, or API
symbol.

### Explicit nonclaims

No result proves:

- a categorical duality for the complete history/task/decoder chain;
- a free/cofree adjunction for histories and observers;
- a canonical projective polarity independent of the declared
  point--covector identification;
- one metric space containing the real and p-adic shadows;
- closure of arbitrary local solver outputs in the rational image;
- an adelic completion or local-global theorem;
- a preferred p-adic continued fraction;
- Arithmetic Geometric Universality;
- a new process dimension or vertical rank.

## 10. Core, architecture, map, and API effects

### Mathematical Core — refine

The unit-frame statement gains a projective calibration: \(1\) is the third
mark of \((0,1,\infty)\), not an intrinsic scalar or metric unit.  The
quotient/decoder boundary gains two exact stabilizer counterexamples and one
positive ordered-frame reconstruction theorem.  Universal properties under
duality are explicitly variance-sensitive.

### Engineering Architecture — refine

The presentation pipeline must distinguish:

```text
local point decoder
projective frame decoder
semantic canonical lowering
literal history reconstruction.
```

A solver that changes place or solves in a local geometry must report whether
its result lies in the rational lowering image.  No dependency or public
solver design changes.

### Theory Map — refine, no maturity promotion

Phase 10 strengthens the emerging task-covariant evaluation transversal and
the V2 obstruction.  It supplies a finite exact bridge from marked projective
frame to matrix semantics, while proving that local points and projective
self-duality do not generate a vertical rank.  The result remains
Sonnet-local T1/T2 evidence.

### API pressure — none

The frame, incidence, audit, and lowering helpers remain private to the
research test.  One Sonnet and one finite rational workload do not justify
`ProjectiveDuality`, `UniversalFrame`, `RoundTrip`, `PlaceShadow`, or
objectification APIs.

## 11. Next research gate

Only after this audit is it responsible to return to place-indexed continued
fraction sections.  The next task should test:

1. whether a real or p-adic marked section transports covariantly with its
   ordered frame;
2. whether section evaluation preserves the common rational-frame certificate
   or explicitly exits its image;
3. whether a finite geometric solve followed by frame decoding and canonical
   Borel/Weyl lowering commutes with direct arithmetic evaluation;
4. whether the dual observer suggested by \(g^{-T}\) has a precise cofree or
   decoder universal property;
5. whether any surviving residual adds new free composition rather than only
   restoring a quotient fibre.

The dependency order is now fixed:

\[
\text{marked duality/covariance}
\to
\text{unit-framed section}
\to
\text{solver image closure}
\to
\text{round-trip lowering}
\to
\text{objectification test}.
\]

This phase has completed the first and the finite algebraic part of the fourth.
The section and solver-closure gates remain open.
