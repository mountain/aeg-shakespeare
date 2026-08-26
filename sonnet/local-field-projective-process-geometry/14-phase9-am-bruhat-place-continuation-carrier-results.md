# Phase 9 — A/M–Bruhat place carrier and task-projection audit

**Status:** Gates 9A--9E complete for the frozen finite workload.  The exact
comparison supports a finite task-independent **marked rational projective
history carrier** with compatible real and p-adic local shadows.  It rejects
the stronger claims that the bare A/M hyperbolic space is itself the common
carrier, that the real and p-adic shadows are one metric space, or that the
construction creates a new process dimension.

**Executable owner:**
[test_am_bruhat_place_continued_fraction_carrier.py](../../tests/research/test_am_bruhat_place_continued_fraction_carrier.py)

**Frozen task:**
[13-phase9-am-bruhat-place-carrier-task-contract.md](13-phase9-am-bruhat-place-carrier-task-contract.md)

## 1. Verdict

The proposed reciprocal/projective bridge works after one decisive
correction.

It is not

```text
one A/M hyperbolic space
    containing real continued fractions and p-adic continued fractions.
```

It is

```text
literal marked rational A/M + reciprocal history
    -> oriented rational projective frame in PGL2(Q)
    -> real place shadow and p-adic place shadows
    -> stopping, ruler, policy, and decoder task quotients.
```

The exact results are:

1. The existing A/M process-frame metric is hyperbolic, but it is related to
   the affine-action chart by **A/M group inversion**.  This inversion is not
   the projective reciprocal.  A positive metric weight \(c\) changes the
   curvature scale to \(-1/c\), so no canonical scalar ruler is selected.
2. The affine/Borel grammar plus one Weyl operation constructs every frozen
   rational projective frame through the exact Bruhat factorization.
3. Regular continued-fraction digits replay as
   \(M(a)=T_aR=T_aD_{-1}W\).  The sign dilation is essential: \(W=-1/z\)
   preserves the upper half-plane, while \(R=1/z\) exchanges the upper and
   lower half-planes.
4. One rational frame has compatible but different local evaluations.  The
   real evaluation remembers the determinant orientation component; the
   p-adic lattice evaluation quotients integral units at the root while its
   projective-contact interface can still see their action on branches.
5. The Phase 7/8 witnesses all lift to one finite rational-history envelope
   without precision, horizon, ruler, decoder, or task-family tags in its
   source objects.  Depth-six/depth-eight stopping and full/scalar decoding
   form exact commuting projection triangles.
6. Part of the Phase 8 boundary and twisting is therefore projection-induced.
   Precision terminals, place-grammar invalidity, and local many-to-one
   merging disappear as intrinsic defects upstairs.  The same-task Bellman
   policy residual does not disappear: it is traced to rational continuation
   data forgotten by the local observer.

The phrase earned by Phase 9 is:

> **finite task-independent continuation carrier with compatible local
> shadows.**

This is a bounded comparison theorem, not a categorical initial/terminal
object, an adelic completion, or Arithmetic Geometric Universality.

## 2. Gate 9A — the two A/M hyperbolic charts

Use the affine process group

\[
(a,v)(b,w)=(a+e^v b,v+w),
\qquad
\iota(a,v)=(-e^{-v}a,-v).
\]

The executable verifies both left and right inverse identities exactly.  It
then compares

\[
\Phi_L(a,v)=a+i e^v
\]

with

\[
\Phi_R(a,v)=-a e^{-v}+i e^{-v}.
\]

Substitution gives

\[
\boxed{\Phi_R=\Phi_L\circ\iota}.
\]

The two pullbacks of the Poincare metric are

\[
g_L=e^{-2v}da^2+dv^2,
\]

and

\[
g_R=(da-a\,dv)^2+dv^2.
\]

The exact Jacobian calculation certifies

\[
\boxed{g_R=\iota^*g_L}.
\]

Thus the process-frame and affine-action realizations are inversion-dual
descriptions of one hyperbolic class.  They are not literally the same chart,
and the comparison does not erase the orientation of process history.

### 2.1 Metric-weight boundary

For

\[
g_c=(da-a\,dv)^2+c\,dv^2,
\qquad c>0,
\]

set

\[
x=-a e^{-v},
\qquad y=e^{-v}.
\]

Then

\[
g_c=\frac{dx^2+c\,dy^2}{y^2}.
\]

After \(X=x/\sqrt c\),

\[
g_c=c\frac{dX^2+dy^2}{y^2}.
\]

An independent symbolic Ricci calculation gives scalar curvature

\[
\operatorname{Scal}(g_c)=-\frac{2}{c},
\]

and hence Gaussian curvature

\[
\boxed{K(g_c)=-\frac1c}.
\]

The hyperbolic geometry survives every declared \(c>0\), but its scale does
not select \(c=1\).  The A/M mother proposal therefore supplies a geometric
class only after a ruler is declared.

## 3. Gate 9B — Borel/Weyl completion

For

\[
g=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad \Delta=AD-BC\ne0,
\]

the \(C=0\) case is upper triangular.  When \(C\ne0\), exact multiplication
verifies

\[
\boxed{
g=
\begin{pmatrix}\Delta/C&A/C\\0&1\end{pmatrix}
W
\begin{pmatrix}C&D\\0&1\end{pmatrix}.
}
\]

The executable exhausts all 496 nonsingular integer matrices with entries in
\([-2,2]\).  Every matrix lies in the declared Borel cell or factors through
the opposite Borel--Weyl--Borel cell.

It then exhausts 37,449 literal words through length five over

```text
T_-1, T_1, D_-1, D_2, D_3, D_5, D_7, W.
```

All products are nonsingular.  The largest absolute matrix numerator is
16,807 and every matrix denominator is one.  At each frozen odd prime, the
finite lattice-depth distribution is

| depth | words |
| ---: | ---: |
| 0 | 20,000 |
| 1 | 13,602 |
| 2 | 3,357 |
| 3 | 456 |
| 4 | 33 |
| 5 | 1 |

Thus 37,448 words lie inside the declared depth-four local budget and one word
at each prime is reported explicitly as `outside_depth_budget`; it is not
silently sampled away.

### 3.1 Why the oriented frame remains upstairs

If a frame has columns \((u,v)\), right multiplication gives

\[
(u,v)W=(v,-u),
\qquad
(u,v)R=(v,u).
\]

Consequently

\[
\det(gW)=\det g,
\qquad
\det(gR)=-\det g.
\]

The same test retains poles explicitly: \(W(0)=\infty\).  It also exhibits
distinct literal words with the same matrix, for example

```text
empty word  -> I
T_1 T_-1    -> I.
```

Matrix lowering is therefore a sound semantic functor, but the matrix alone
is not the lifted history or its process cost.

## 4. Gate 9C — regular continued fractions are a section

The Phase 2 Stern--Brocot workload contains every \(L/R\) word through depth
eight, hence 511 exact paths.  For each canonical rational endpoint, Phase 9
reconstructs its digits and verifies

\[
M(a)=
\begin{pmatrix}a&1\\1&0\end{pmatrix}
=T_aR=T_aD_{-1}W.
\]

Every finite product agrees with:

1. the literal right-reciprocal evaluation;
2. the Phase 2 chronological matrix lowering;
3. the rational endpoint;
4. the two consecutive convergent columns;
5. the unique canonical Stern--Brocot path;
6. the exact Farey cylinder.

The largest absolute matrix entry in this depth-eight exhaust is 55.  The
frame determinant satisfies

\[
\det(M(a_0)\cdots M(a_n))=(-1)^{n+1}.
\]

At \(i\in\mathbb H\), exact real evaluation gives

\[
W(i)=i,
\qquad
R(i)=-i.
\]

Thus a regular continued fraction is not intrinsically one point of
\(\mathbb H\).  It is a symbolic section of an oriented projective/geodesic
process.  The familiar equality

\[
[1;2]=[1;1,1]=\frac32
\]

still has different lifted frames and continuation behavior.  Endpoint
quotienting remains too coarse.

## 5. Gate 9D — compatible place shadows, not one space

For every Borel/Weyl word through length four, the executable evaluates the
same rational frame in two ways:

```text
literal word -> sequential local action
literal word -> rational matrix -> local evaluation.
```

The squares commute exactly for 4,681 words.  At each of
\(p=3,5,7\), the lattice-depth histogram is

| depth | words |
| ---: | ---: |
| 0 | 2,826 |
| 1 | 1,536 |
| 2 | 291 |
| 3 | 27 |
| 4 | 1 |

At the real place, if

\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

then

\[
g(i)=
\frac{ac+bd}{c^2+d^2}
+i\frac{\det g}{c^2+d^2}.
\]

The sign of the imaginary part is therefore exactly the determinant
orientation component.

This calculation uses the ordinary fractional-linear formula on both
determinant components, so negative determinant lands in the lower
half-plane.  The unoriented symmetric-space point in
\(PGL_2(\mathbb R)/PO(2)\) can instead be represented by positive forms, or by
using the anti-holomorphic convention on the negative component.  Phase 9
keeps the determinant sign as separate oriented-frame data; a bare
symmetric-space point is not the continued-fraction carrier.

At an odd p-adic place,

\[
D_{-1}\in PGL_2(\mathbb Z_p)
\]

fixes the standard root vertex.  It is not globally invisible: on the
depth-one affine contacts it sends

\[
[1:1]\longmapsto[-1:1],
\]

whose coordinates are \(1\) and \(p-1\), respectively.  The root quotient
forgets this action while the projective-direction interface sees it.

The geometric conclusion is therefore

\[
PGL_2(\mathbb Q)
\longrightarrow
\begin{cases}
PGL_2(\mathbb R)/PO(2),\\
PGL_2(\mathbb Q_p)/PGL_2(\mathbb Z_p),
\end{cases}
\]

with a common rational projective boundary language.  It is not an equality
between the real hyperbolic plane and the p-adic tree.

## 6. Gate 9E — the finite marked history envelope

### 6.1 Source object

The executable defines one source element by

\[
u=(x_0;(a_0,\ldots,a_{n-1});(G_0,\ldots,G_n);
   (\alpha_0,\ldots,\alpha_n);\kappa),
\]

where

\[
G_{j+1}=G_jM(a_j),
\qquad
\alpha_{j+1}=\frac1{\alpha_j-a_j},
\]

unless \(\alpha_j=a_j\), which is an intrinsic exact terminal.  It retains

- the marked rational origin \(x_0\);
- the literal rational action word;
- every oriented prefix matrix;
- every complete quotient;
- the declared additive cost cocycle
  \((\text{literal steps},\text{rational serialization bits})\).

The reconstruction law

\[
G_j(\alpha_j)=x_0
\]

is checked after every nonterminal prefix.  At an exact terminal, the first
matrix column reconstructs \(x_0\).  Thus the explicit origin mark is partly
redundant on exact frames, but it serves as a consistency and episode mark and
must not be confused with a task-family tag.

The finite source is a rooted prefix forest at the eight mandatory witness
origins.  Its rational histories are generated through common horizon four
using the three declared place grammars and then deduplicated as rational
histories; the generating prime is not stored in the source key.

| literal depth | distinct histories |
| ---: | ---: |
| 0 | 8 |
| 1 | 42 |
| 2 | 82 |
| 3 | 138 |
| 4 | 168 |
| **total** | **438** |

The largest matrix numerator is 3,804,769, the largest denominator is 2,401,
and the largest declared rational-action cost is 36 bits.  No floating-point
equality is used.

This is a finite free-prefix carrier for the declared workload.  Phase 9 does
not claim that it is an initial or terminal object in a category of all
continued-fraction algorithms.

### 6.2 Task projections

A task view supplies only

```text
place p, precision, horizon, and whether the full decoder payload is observed.
```

It scans the same rational history and applies the frozen precedence

```text
invalid place action
exact terminal
precision terminal
repeated-complete-quotient stop
horizon stop
live.
```

For \(p=3\), exactly 145 of the 438 rational histories are admitted by the p=3
binary grammar.  The remaining 293 are valid rational histories generated at
another place but become `invalid` under the p=3 place grammar.  Invalidity is
therefore relative to the local digit interface, not a failure of rational
projective composition.

The exact response counts are:

| response | depth 6 | depth 8 |
| --- | ---: | ---: |
| invalid place action | 293 | 293 |
| live | 60 | 73 |
| success exact | 36 | 39 |
| success precision | 40 | 7 |
| repeated quotient / cycle stop | 9 | 26 |

For every one of the 438 source histories:

1. prefix concatenation and the vector cost commute before stopping;
2. once a task has stopped, extending the source history does not change its
   stopped response;
3. the depth-eight response maps to the depth-six response by replaying its
   retained stopped trace, so

   \[
   q_6=\rho_{8\to6}\circ q_8;
   \]

4. the same construction makes the horizon-four to horizon-two triangle
   commute;
5. forgetting terminal payload maps full decoding to scalar response, so

   \[
   q_{8,\mathrm{scalar}}
   =\pi_{\mathrm{full}\to\mathrm{scalar}}\circ q_{8,\mathrm{full}};
   \]

6. direct p-adic prefix evaluation agrees with rational matrix lowering
   followed by local lattice evaluation at all three primes.

These are the finite task-refinement and place-evaluation comparison squares
requested by the frozen contract.

### 6.3 Where many-to-one transport comes from

On the p=3-admitted part of the envelope, 137 legal one-step extensions have
137 distinct literal child histories.  Literal prefix extension has a unique
parent and is injective upstairs.

After projection to `(lift bit, target lattice vertex)`, those 137 arrows
occupy only 48 local slots.  Thirty-six slots have multiple rational-history
preimages, and ten even merge distinct source lattice vertices.

Thus many-to-one local transport is recomputed as a projection effect.  This
does not say every Phase 8 stable-class merger is caused only by the lattice
observer, but it supplies an exact upstream mechanism for the observed
twisting.

## 7. Exact provenance of the Phase 7/8 witnesses

| witness | exact upstairs diagnosis | what the local/task quotient forgot |
| --- | --- | --- |
| immediate S2 residual | the three marked rational states remain distinct and have decoder-optimal bits `{0}`, `{1}`, `{0}` under one common task | the place observer identifies distinct complete quotients with the same current local geometry and cost |
| transported future | after suffix `00`, the complete quotients are \(-4/3\) and \(-2/3\); their Ruban contact representatives are \(5/3\) and \(7/3\) | current policy and initial S2 agree, but rational continuation data precedes and refines the later local projection |
| changed stopping | one source word for \(3/11\), bits `0100`, is depth-six precision success and depth-eight live | the precision stopping section, not the rational arithmetic path |
| full decoder | the two step-two states at complete quotient \(1/3\) have different rational prefix frames; bit zero has common scalar cost \((1,2,3,16)\) but reconstructs \(-8/11\) and \(17/7\) | the local scalar interface forgets the marked rational frame/episode needed by the full decoder |

The changed-stopping edge is especially explicit:

```text
same rational fourth action 7/3
same next complete quotient -1/3
same depth-six lattice vertex

D6 -> success_precision, decoder cost 50
D8 -> live,              decoder cost 0.
```

The arithmetic transition exists once upstairs.  The terminal/live split is
created by applying two different precision projections.

The immediate S2 witness cuts the other way.  It uses the same place,
precision, horizon, and decoder ruler.  Its policy difference is not caused by
changing the stopping task.  The rational carrier explains it by retaining
complete-quotient and frame history that S2 discarded; Bellman optimization
still remains a downstream task operation.

## 8. What the universal-carrier repair does and does not repair

Phase 9 separates five phenomena that Phase 8 saw together.

### Intrinsic upstairs boundary

- exact equality \(\alpha=a\), after which reciprocal continuation is
  undefined;
- a projective pole in a declared affine chart.

These do not disappear by enlarging the carrier.

### Projection-induced boundary

- precision success;
- horizon stopping;
- choosing to terminate on a repeated complete quotient;
- decoder payload omission.

The repeated quotient is an intrinsic event, but treating it as terminal is a
task decision.  The untruncated finite source may retain later cycle steps.

### Place-interface boundary

- an action admitted by one local digit grammar can be invalid under another;
- an integral sign unit can fix the root while permuting branch contacts;
- many rational frames can share one local lattice vertex.

### Task-semantic residual

- equal current local data can still have different future Bellman values;
- scalar policy adequacy does not imply full decoder adequacy.

The rational carrier localizes these failures.  It does not make the task
semantics disappear.

## 9. Universality and vertical objectification remain orthogonal

The Phase 9 source uses only the already admitted lower grammar

```text
Translation, nonzero Dilation, and Weyl/reciprocal projective steps.
```

No new primitive is objectified.  No higher-rank free alphabet is introduced.
No lowering theorem is needed beyond the existing matrix/action semantics of
those lower generators.

Therefore the vertical V2--V4 gate fails at its first new-generativity step:

\[
\text{new task-independent generators}=\varnothing.
\]

Compatible projections from one source are a horizontal universal-history
result.  They are not a dimension increase.

This directly validates the stricter criterion established by the completed
Translation and Addition-to-Multiplication calibrations:

> Objectification requires stable semantics, new free composition, and a
> lowering interpretation on every legal new composite.  A residual or common
> carrier alone is insufficient.

## 10. Cost and effective-analysis ledger

The experiment keeps separate:

- literal history length;
- rational-action serialization bits;
- real Farey turns and cylinder data;
- p-adic lattice depth and tree travel;
- terminal decoder bits;
- task stopping and policy value.

No scalar sum is declared canonical.  The A/M metric weight \(c\) and the
finite history serialization convention are declared rulers.  Matrix
compression does not receive free credit because distinct literal histories
can lower to the same matrix.

The routine module contains seven exact tests and passes in about five seconds
on the reference run.  It reuses SymPy and Python `Fraction`; it introduces no
dependency, package module, or API symbol.

## 11. Claim ledger

### Exact finite/algebraic statements

1. The two A/M charts and metrics commute through group inversion.
2. \(g_c\) has Gaussian curvature \(-1/c\).
3. The displayed constructive Bruhat factorization holds for every
   nonsingular matrix in the frozen exhaust.
4. The 37,449 rational words lower exactly with explicit local depth budgets.
5. All 511 real continued-fraction controls agree across literal, matrix,
   convergent, Farey, and Borel/Weyl presentations.
6. The 4,681 real/p-adic place-evaluation squares commute.
7. The 438-element marked rational envelope has exact task projections and
   commuting refinement/decoder triangles.
8. Every mandatory Phase 7/8 witness has the provenance stated in Section 7.

### Corpus statistics

- the word, depth, matrix-size, envelope-size, outcome, and merging counts;
- the measured approximately five-second reference runtime.

### Process Geometry interpretation

- supports a rational projective mother **carrier** for the declared finite
  place shadows;
- confirms that bare local geometry is not continuation-complete;
- explains some terminal/invalid/merging behavior as downstream projection;
- retains task-relative Bellman and decoder semantics;
- rejects promotion from source universality to vertical dimension.

### Explicit nonclaims

No result proves:

- a canonical A/M metric weight or scalar ruler;
- one metric space containing both real and p-adic geometry;
- an infinite Bruhat--Tits tree or boundary completion;
- an adelic restricted product or adelic dynamics;
- a canonical p-adic continued-fraction selector;
- a universal object in a category of all tasks or algorithms;
- Arithmetic Geometric Universality;
- a new process rank, objectified residual primitive, or compositional rank
  lowering theorem.

## 12. Core, architecture, map, and API effects

### Mathematical Core — refine, no theorem/API promotion

The finite result sharpens the mother-object boundary.  A common rational
projective history can precede place evaluation, while metric, topology,
stopping, and decoder remain observer/task data.  The exact distinction
between horizontal source universality and vertical objectification is
strengthened.  Cross-domain evidence is still insufficient to promote a new
core theorem.

### Engineering Architecture — support and refine

The executable realizes the intended stack

```text
literal history
  -> rational frame lowering
  -> place evaluation
  -> task stopping
  -> scalar/full decoder observation.
```

It demonstrates why stopping must not mutate the upstream arithmetic process
and why a response quotient must state whether it retains enough trace for
task-refinement maps.  No dependency or API change follows.

### Theory Map — refine without maturity promotion

Phase 9 supports the horizontal history/evaluation/task-quotient axis and the
place-relative observer interpretation.  It supplies a new V2 red team:
mother-carrier compatibility is not new-object generation.  Maturity remains
Sonnet-local T1/T2 evidence.

### API pressure — none

The finite source, task views, and comparison maps remain private executable
research structures.  They have not survived an independent domain and do
not justify `LocalField`, `BruhatTitsTree`, `UniversalCarrier`, `PlaceShadow`,
or objectification APIs.

## 13. Answer to the motivating proposal

The reciprocal/projective-duality proposal is viable in the following precise
form:

> Use A/M as the affine/Borel chart, add a Weyl reciprocal to obtain the full
> rational projective action, retain literal oriented history, and regard the
> real hyperbolic/Farey geometry and p-adic lattice-tree geometry as different
> local evaluations of that rational carrier.

What is not viable is to construct one dual hyperbolic metric space and place
the p-adic continued fraction inside it as another region.  The real and
non-Archimedean observers induce incompatible local topologies.  Their exact
commonality lies one layer earlier—in the rational projective action and its
marked history—not in one shared metric completion.

That correction preserves the substance of the proposal.  It also explains
the earlier twisting: the previous discussion began after projecting to
finite local task states.  Moving upstream to the marked rational carrier
turns part of the apparent boundary into ordinary stopping/place projection,
while leaving genuine task-relative continuation semantics visible rather
than pretending it has vanished.
