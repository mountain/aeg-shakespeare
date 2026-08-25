# Phase 2 — real continued fractions and Farey-path positive control

**Status:** Gate 2 exact finite positive control complete; symbolic
Stern--Brocot/Farey coding only; no numerical geodesic flow and no
\(p\)-adic selector.

**Owner:** [test_real_continued_fraction_geodesic_control.py](../../tests/research/test_real_continued_fraction_geodesic_control.py)

## 1. Why the real control comes before a \(p\)-adic algorithm

Phase 0 established that right-reciprocal arithmetic histories lower to
fractional-linear matrices. Phase 1 established the finite Bruhat--Tits
lattice ball and showed that inversion forces projective completion of the
affine residue observer.

The next temptation is to select a named \(p\)-adic continued-fraction
algorithm. That would still be premature. Before comparing non-Archimedean
digit selectors, the study needs one place where the relation

\[
\text{right-reciprocal history}
\longleftrightarrow
\text{continued fraction}
\longleftrightarrow
\text{projective path}
\]

is classical, exact, and completely visible. Ordinary real continued
fractions provide that positive control through Farey neighbours,
Stern--Brocot paths, and the cutting sequences of the modular tessellation
[Series-1985; Reutenauer-2019].

The Phase 2 question is:

> Which information is preserved, compressed, or lost when one finite
> right-reciprocal history is translated into a convergent matrix, a Farey
> frame, a Stern--Brocot path, and a real cylinder interval?

## 2. Four exact presentations

For regular digits

\[
\mathbf a=(a_0,a_1,\ldots,a_n),
\qquad
a_0\ge0,\quad a_i\ge1\ (i>0),
\]

write

\[
[\mathbf a]
=
a_0+\cfrac1{a_1+\cfrac1{\ddots+\cfrac1{a_n}}}.
\]

Phase 2 keeps four presentations distinct:

1. the literal right history, evaluated from the innermost digit \(a_n\)
   outward;
2. the chronological projective matrix product;
3. the ordered pair of consecutive convergents, or Farey frame;
4. the \(L/R\) word describing the path from the root of the
   Stern--Brocot tree.

Their exact relation is:

\[
\begin{array}{ccc}
\text{right ProcessWord}
&\longrightarrow&
M(a_0)\cdots M(a_n)
\\[2mm]
\downarrow&&\downarrow
\\[2mm]
[\mathbf a]
&\longleftarrow&
\begin{pmatrix}p_n&p_{n-1}\\q_n&q_{n-1}\end{pmatrix}
\\[2mm]
&&\downarrow
\\[-1mm]
&&\text{Farey frame and run-length }L/R\text{ path},
\end{array}
\]

where

\[
M(a)=
\begin{pmatrix}a&1\\1&0\end{pmatrix}.
\]

The test proves every arrow using integers and rational numbers only.

## 3. Literal right expansion and matrix lowering

The written continued fraction is outermost-first, but its executable
right-reciprocal process is chronological from inside out:

\[
a_n
\xmapsto{a_{n-1}+1/x}
[a_{n-1};a_n]
\longrightarrow\cdots\longrightarrow
[a_0;\ldots,a_n].
\]

The test stores those outer steps as

\[
\operatorname{ProcessWord}(a_{n-1},\ldots,a_0)
\]

with \(a_n\) as the initial state. Matrix composition in the same
chronological order gives

\[
M(a_0)\cdots M(a_{n-1}),
\]

whose affine action on \(a_n\) equals the literal endpoint.

Independently, the full product satisfies

\[
M(a_0)\cdots M(a_n)
=
\begin{pmatrix}
p_n&p_{n-1}\\
q_n&q_{n-1}
\end{pmatrix}.
\]

Thus the matrix is not only an endpoint evaluator. Its second column retains
the previous convergent and hence an oriented projective frame.

## 4. Convergents are exact Farey frames

The convergents obey

\[
p_k=a_kp_{k-1}+p_{k-2},
\qquad
q_k=a_kq_{k-1}+q_{k-2},
\]

with the standard initial frame. Consecutive convergents satisfy

\[
\left|
p_kq_{k-1}-p_{k-1}q_k
\right|=1.
\]

They are therefore Farey neighbours. Phase 2 verifies this determinant at
every prefix of several nonstationary histories, rather than only at the
final rational.

This is the first point at which the projective matrix acquires a direct
geometric reading: its two columns are the endpoints of an oriented Farey
edge. The sign alternates with parity and must not be silently discarded
when orientation is task-visible.

## 5. Digits are compressed turn runs

For the canonical finite expansion of a positive rational, require the last
digit to exceed one. Its Stern--Brocot path word is the alternating run
expansion

\[
R^{a_0}L^{a_1}R^{a_2}\cdots
\epsilon^{a_n-1},
\]

where \(\epsilon\) is \(R\) or \(L\) according to parity. A zero initial run
is omitted. Examples are

\[
\frac12=[0;2]\longleftrightarrow L,
\]

\[
\frac53=[1;1,2]\longleftrightarrow RLR,
\]

\[
\frac7{10}=[0;1,2,3]\longleftrightarrow LRRLL.
\]

The executable oracle exhausts all \(L/R\) words through depth eight and
proves:

1. mediant navigation produces one positive rational;
2. Euclidean canonicalization of that rational regenerates the same word;
3. every prefix visits a distinct tree node;
4. dropping the final letter gives the unique tree parent;
5. the materialized unit-path length is

\[
|w|=\sum_{i=0}^n a_i-1.
\]

The last equality is a Process Geometry cost warning. A continued-fraction
digit is an objectified run, not a free unit move. Cost \(n+1\) counts stored
digits; cost \(\sum a_i-1\) counts materialized Farey turns. Neither can
replace the other without declaring the available primitive alphabet.

## 6. Prefixes define exact real observer cylinders

Let the last two convergents of a finite prefix be

\[
\frac{p_n}{q_n},
\qquad
\frac{p_{n-1}}{q_{n-1}}.
\]

The real cylinder of numbers beginning with that prefix has boundary

\[
\frac{p_n}{q_n}
\quad\text{and}\quad
\frac{p_n+p_{n-1}}{q_n+q_{n-1}},
\]

with their order determined by parity. The endpoints are Farey neighbours,
and the exact cylinder width is

\[
\frac{1}{
q_n(q_n+q_{n-1})
}.
\]

The test does not infer prefix semantics from this width alone. It exhausts
reduced positive rational samples of bounded denominator inside several
cylinders and verifies that Euclidean expansion reproduces the declared
prefix.

This supplies the real counterpart of Phase 1's finite observer:

- \(p\)-adic observation asks whether a point lies in a residue/lattice
  contact class;
- real continued-fraction observation asks whether a point lies in an
  ordered Farey cylinder.

Both are exact finite distinctions, but their local structures are not the
same.

## 7. Red team — endpoint equality is not continuation equivalence

A positive rational has two terminal continued-fraction presentations:

\[
[a_0;\ldots,a_n]
=
[a_0;\ldots,a_n-1,1],
\qquad a_n>1.
\]

For the smallest useful witness,

\[
[1;2]=[1;1,1]=\frac32.
\]

The test proves all of the following simultaneously:

1. the literal endpoints agree;
2. the canonicalized Stern--Brocot vertex and path agree;
3. the full convergent matrices differ because their previous-convergent
   columns differ;
4. their prefix cylinders lie on opposite sides of \(3/2\) and meet only at
   that endpoint;
5. appending the same tail digit \(2\) gives different values:

\[
[1;2,2]\ne[1;1,1,2].
\]

Therefore rational endpoint equality is not stable under the native
continuation operation of digit appending. Quotienting the two literal
histories is valid for an endpoint-only task or a canonical Stern--Brocot-node
task, but invalid for a future-prefix, oriented-cylinder, or lifted-frame
task.

This is not merely the familiar statement that rational continued fractions
are nonunique. It identifies exactly which presentations forget the
distinguishing payload and supplies a finite continuation witness.

## 8. Same arithmetic carrier, different local geometries

The real and \(p\)-adic phases now admit a precise comparison:

| Layer | Real place | \(p\)-adic place |
| --- | --- | --- |
| arithmetic carrier | right reciprocal histories and \(PGL_2(\mathbb Q)\) matrices | the same |
| finite observer | ordered Farey cylinder | residue/lattice contact |
| projective combinatorics | Stern--Brocot path and Farey frame | finite Bruhat--Tits lattice ball |
| local refinement | nested intervals | reduction modulo \(p^n\) |
| completion pressure | infinite cutting sequence / real endpoint | inverse residue system / \(p\)-adic endpoint |
| canonicality defect | terminal split and oriented approach side | digit section and cost ruler |

The two trees must not be identified. The Stern--Brocot tree is a real
ordered coding of positive rational directions and a combinatorial shadow of
Farey cutting sequences. The Bruhat--Tits tree is built from homothety
classes of lattices over a discretely valued field. What is shared is the
rational projective process language, not the resulting local geometry.

This is the strongest conclusion of the positive control:

> place-dependent geometry enters after a common arithmetic history carrier;
> it is selected by observer distinctions, ordering/valuation, and allowed
> continuation semantics.

## 9. Effective-analysis audit

- **Mode:** exact finite symbolic arithmetic.
- **Closure:** regular digit evaluation, Euclidean canonicalization,
  projective matrix multiplication, convergent recurrence, mediant
  navigation, and finite cylinder construction.
- **Evaluator:** Fraction endpoints, oriented matrix frames, tree nodes, and
  interval membership.
- **Certificates:** commuting endpoint calculations, unimodular
  determinants, exhaustive words through depth eight, exact widths, bounded
  cylinder samples, and a distinguishing continuation.
- **Failure semantics:** empty/negative/zero-tail digit records, nonpositive
  Stern--Brocot endpoints, invalid path letters, zero reciprocal states, and
  projective poles are explicit errors.
- **Cost boundary:** stored digits and materialized unit turns are reported
  separately; no runtime speedup is claimed.
- **Numerical analysis:** not applicable at this gate.
- **Classical baseline:** regular continued fractions, Farey neighbours,
  Stern--Brocot navigation, and Series' modular-surface cutting-sequence
  correspondence.

## 10. Claim ledger and Theory Map effect

### Exact finite statements

1. right ProcessWord, projective matrices, and convergents commute;
2. consecutive convergents form Farey frames;
3. canonical digits and finite Stern--Brocot paths are inverse on the
   exhausted word domain;
4. prefix cylinders have exact Farey boundaries and bounded-sample prefix
   semantics;
5. terminal splitting is endpoint-equal but continuation-distinguishable;
6. digit count and materialized turn count are different cost rulers.

### Classical interpretation

The \(L/R\) word is the finite combinatorial cutting-sequence control for the
classical relation between continued fractions and modular geodesics. Phase 2
does not reprove the global geodesic-flow theorem, integrate a hyperbolic
trajectory, or claim a new coding.

### Process Geometry interpretation

The phase supports H0 and sharpens H1: terminal endpoint equality is not
continuation-stable without declaring a canonical terminal convention or
forgetting future digit extension. It supports H2 by exhibiting a second
place-dependent refinement geometry, and it adds an exact cost translation
relevant to H3 without making an entropy claim. The Theory Map file and every
API maturity level remain unchanged.

## 11. Next gate

The next step is no longer “implement a \(p\)-adic continued fraction.” It is:

1. freeze one matched finite task for reconstruction, continuation, failure,
   and cost;
2. select two genuinely different \(p\)-adic digit/continued-fraction
   algorithms as competing presentations;
3. compare them against the same task and against the lattice-ball oracle;
4. preserve explicit nontermination and precision-loss semantics;
5. reject any claim of canonicality that depends only on the algorithm's
   name or historical priority.

Only after that comparison may convergence, periodicity, effective analysis,
or cross-place synthesis be reopened.
