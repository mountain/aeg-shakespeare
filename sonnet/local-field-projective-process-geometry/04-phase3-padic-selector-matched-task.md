# Phase 3 — matched-task comparison of two \(p\)-adic selectors

**Status:** Gate 3 exact rational comparison complete for Ruban and Browkin I;
finite symbolic oracle only; no preferred selector, infinite-boundary
completion, or Lagrange-periodicity claim.

**Owner:** [test_padic_continued_fraction_selector_comparison.py](../../tests/research/test_padic_continued_fraction_selector_comparison.py)

## 1. Why “a \(p\)-adic continued fraction” is not yet a definition

The real positive control in Phase 2 has a distinguished floor map and hence
a familiar regular continued-fraction algorithm.  The \(p\)-adic field has no
corresponding order, so it has no canonical integral part.  A \(p\)-adic
continued fraction begins only after choosing a section of

\[
\mathbb Q_p\longrightarrow \mathbb Q_p/p\mathbb Z_p.
\]

Ruban and Browkin I make different choices of that section.  Both then run the
same reciprocal recurrence.  It would therefore be circular to choose one by
name, historical priority, or analogy with the real algorithm and only later
ask what task it solves.

Phase 3 reverses that order.  It freezes one finite task and gives the two
selectors exactly the same input, evaluator, failure semantics, projective
oracle, and cost rulers.

## 2. The matched finite task

For an odd prime \(p\), an exact rational input
\(\alpha_0\in\mathbb Q\subset\mathbb Q_p\), a selector \(s\), and a declared
horizon \(N\), compute

\[
a_n=s(\alpha_n),
\qquad
\alpha_{n+1}=\frac1{\alpha_n-a_n}
\]

until one of three outcomes occurs:

1. **terminated:** \(\alpha_n-a_n=0\);
2. **cycle:** an exact rational complete quotient has already occurred;
3. **horizon:** \(N\) steps have been executed without either certificate.

The third outcome is deliberately not called nontermination.  Only an exact
repeated state is a finite nontermination certificate in this rational oracle.

Every selector must also provide four commuting witnesses:

- the local floor contact \(\alpha_n-a_n\in p\mathbb Z_p\);
- the corresponding two-chart finite lattice-ball label;
- the projective matrix reconstruction of the original input;
- separately declared digit, contact-resolution, and serialization costs.

This task is narrow enough to exhaust and strong enough to expose differences
that endpoint reconstruction alone would hide.

## 3. The two sections

Write the \(p\)-adic Laurent expansion as

\[
\alpha=\sum_{j=k}^{\infty}c_jp^j.
\]

Both selectors truncate through exponent zero:

\[
s(\alpha)=\sum_{j=k}^{0}c_jp^j.
\]

They differ only in the residue representatives used for every coefficient:

| selector | coefficient section | Archimedean digit bound |
| --- | --- | --- |
| Ruban | \(c_j\in\{0,\ldots,p-1\}\) | \(0\le s_R(\alpha)<p\) |
| Browkin I | \(c_j\in\{-(p-1)/2,\ldots,(p-1)/2\}\) | \(\lvert s_B(\alpha)\rvert<p/2\) |

The implementation extracts these coefficients directly from a rational
number using modular inverses.  It does not approximate an infinite \(p\)-adic
series and uses no floating point.

For either section,

\[
v_p(\alpha-s(\alpha))\ge1
\]

unless the remainder is exactly zero.  Moreover,

\[
s_R(\alpha)-s_B(\alpha)\in p\mathbb Z_p.
\]

Thus the two digits are different rational representatives of the same local
semantic observation.  This is precisely the Phase 0 section defect, now
placed inside a continuation process.

## 4. How the floor meets the finite Bruhat--Tits ball

Phase 1 represented a radius-\(n\) lattice sphere by the two normal forms

\[
[r:1],\qquad [1:pt].
\]

The floor of a complete quotient selects an exact vertex in those same
charts.

If \(v_p(\alpha)\ge0\), the first visible contact is the affine depth-one
class

\[
[\alpha\bmod p:1].
\]

If \(v_p(\alpha)=-r<0\), normalize the homogeneous point
\([\alpha:1]\) to \([1:1/\alpha]\).  The floor-visible contact is then the
infinity-chart vertex at depth \(r+1\),

\[
\left[1:p\left(\frac1{p\alpha}\bmod p^r\right)\right].
\]

The test verifies that \(\alpha\), its Ruban digit, and its Browkin digit all
give the same finite vertex.  This statement is stronger than equality of a
single residue and weaker than equality of histories: it says the two lifts
are indistinguishable to the declared finite projective observer.

The next reciprocal exposes why that is not enough.  If
\(a_R-a_B\in p\mathbb Z_p\), generally

\[
\frac1{\alpha-a_R}
\ne
\frac1{\alpha-a_B}.
\]

The selector is therefore not merely a display convention.  It is a choice
of lift made before a singular continuation operation.

## 5. ProcessWord and projective reconstruction

Each digit lowers to

\[
M(a)=
\begin{pmatrix}
a&1\\
1&0
\end{pmatrix},
\qquad \det M(a)=-1.
\]

For a prefix \(a_0,\ldots,a_n\), the chronological `ProcessWord` product is

\[
G_n=M(a_0)\cdots M(a_n).
\]

If the next complete quotient exists, Phase 3 verifies at every prefix that

\[
\alpha_0=G_n\cdot\alpha_{n+1}.
\]

At termination, the ratio of the first column of \(G_n\) is the original
rational input.  The determinant is checked exactly at every prefix.  Hence
both selectors reconstruct correctly even when their digit histories,
termination behavior, and lattice orbits differ.

## 6. Prefix matrices as lattice classes

The columns of \(G_n\) span a \(\mathbb Z_p\)-lattice.  To identify its
standard-root Bruhat--Tits vertex, multiply by a scalar so that the minimum
entry valuation is zero.  If the normalized determinant has valuation \(d\),
the lattice has index \(p^d\).  A primitive row of the adjugate gives its
kernel covector modulo \(p^d\), which is reduced to the Phase 1 affine or
infinity normal form.

For these determinant-unit continued-fraction matrices, if \(m\) is the
minimum entry valuation then

\[
d=-2m.
\]

The executable oracle checks this identity for every tested prefix and checks
that the resulting class belongs to the complete finite Phase 1 sphere.

This adds an important distinction:

> equal rational endpoints need not have equal lifted lattice-prefix states.

The lattice orbit is history payload, not an endpoint function.

## 7. Exhausted finite domain

The comparison exhausts the 182 distinct nonzero reduced rationals

\[
\left\{
\frac ab:
1\le b\le12,
-12\le a\le12,
\gcd(|a|,b)=1
\right\}
\]

for \(p=3,5,7\), with a sixteen-step horizon.

| prime | Browkin terminated | Ruban terminated | Ruban exact cycles | horizon outcomes |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 182 | 48 | 134 | 0 |
| 5 | 182 | 36 | 146 | 0 |
| 7 | 182 | 38 | 144 | 0 |

Every Browkin expansion in this bounded oracle terminates in at most four
digits.  This finite result is consistent with Browkin's classical rational
finiteness theorem; it is not offered as a new proof of that theorem.  The
Ruban counts are exact only for the displayed finite domain.

## 8. Red team I — the same contact, then terminal versus cycle

For every tested odd prime,

\[
\alpha_0=-1.
\]

Browkin chooses the balanced representative

\[
a_0=-1
\]

and terminates immediately.

Ruban chooses

\[
a_0=p-1,
\qquad
\alpha_1=-\frac1p.
\]

At the next step,

\[
a_1=\frac{p^2-1}{p},
\qquad
\frac1{\alpha_1-a_1}=-\frac1p.
\]

So \(-1/p\) is an exact fixed complete quotient.  The first two Ruban digits
are enough to certify a one-state cycle; no horizon inference is involved.

Yet the initial Ruban digit \(p-1\) and Browkin digit \(-1\) occupy the same
affine depth-one projective contact, since they agree modulo \(p\).  The
observer quotient is correct for contact and incorrect for continuation.

Materializing five repeated cycle digits gives the exact tested lattice-depth
prefix

\[
0,2,4,6,8,10,
\]

along one nested affine ray.  The repository claims this finite prefix and
the exact rational state cycle separately; it does not promote the sample to
a general infinite-orbit theorem.

## 9. Red team II — totality and economy do not choose the same section

At \(p=5\), the positive integer \(3\) gives

\[
3=[3]_R=[-2;1/5]_B.
\]

Ruban terminates in one digit.  Browkin needs two.  Under all three declared
finite costs, Ruban is cheaper on this input:

- fewer selector iterations;
- less summed projective-contact resolution;
- fewer exact numerator/denominator serialization bits.

The two terminal prefix matrices also occupy different lattice vertices:
Ruban remains at the standard root, while Browkin reaches a depth-two affine
class.

But on \(-1\), Browkin terminates and Ruban cycles.  Therefore:

- a task demanding termination on the whole rational domain favors Browkin;
- a task concentrated on some positive inputs and charging local history may
  favor Ruban;
- endpoint correctness alone cannot decide between them.

There is no contradiction.  “Best selector” is not defined before the task
domain, admissible failures, and cost ruler are declared.

## 10. What entered from projective geometry

The role of projective geometry is now more precise than in Phase 0.

1. The floor section selects a rational lift of a finite projective contact.
2. Right reciprocal continuation is a Möbius operation that can distinguish
   two lifts of the same contact.
3. Prefix matrices carry a lattice homothety class in the Bruhat--Tits ball.
4. Termination, cycling, and lattice displacement are properties of the
   lifted history, not only of the represented endpoint.

This is the non-Archimedean counterpart of the real terminal-split red team,
but the geometries remain different.  The real tree records ordered Farey
turns and one-sided interval approach.  The \(p\)-adic tree records lattice
classes and residue branching.  The shared object is the rational
projective history carrier and its \(2\times2\) matrices.

## 11. Effective-analysis audit

- **Mode:** exact finite symbolic arithmetic over `Fraction`.
- **Domain:** rational inputs, odd primes, two named classical sections, and a
  declared step horizon.
- **Closure:** valuation, rational modular reduction, Laurent truncation,
  reciprocal continuation, projective matrices, and finite lattice classes.
- **Evaluator:** exact state/digit histories, outcome status, contact labels,
  reconstructed endpoints, and prefix lattice vertices.
- **Certificates:** local constancy, floor contact, section bounds,
  determinant identities, prefix reconstruction, sphere membership, exact
  repeated states, and finite exhaustive counts.
- **Failure semantics:** invalid/even primes, unknown sections, nonpositive
  horizons, zero valuation requests, nonunit modular denominators, projective
  poles, zero/singular matrices, exact cycles, and horizon exhaustion are
  distinguished explicitly.
- **Cost boundary:** digit steps, summed contact depth, and rational
  serialization bits are separate rulers; runtime or asymptotic superiority
  is not claimed.
- **Numerical analysis:** not applicable; no finite-precision \(p\)-adic
  approximation is used.

## 12. Claim ledger and Theory Map effect

### Exact finite statements

1. Ruban and Browkin floors choose the same finite projective contact for a
   common complete quotient;
2. reciprocal continuation can distinguish those two rational lifts;
3. both histories reconstruct through the same projective matrix calculus;
4. every tested prefix matrix lands in the Phase 1 finite lattice-ball oracle;
5. the bounded rational domain has the exact outcome counts shown above;
6. \(-1\) is an exact Browkin terminal/Ruban fixed-cycle witness;
7. the input \(3\) at \(p=5\) reverses the local economy comparison;
8. equal endpoints can retain different terminal prefix lattice classes.

### Classical boundary

The definitions and general rational behavior belong to the classical theory
of Ruban and Browkin continued fractions.  Phase 3 does not claim a new
finiteness theorem, a \(p\)-adic Lagrange theorem, or a preferred algorithm.

### Process Geometry interpretation

The result sharpens H1: a task quotient that preserves finite projective
contact can still fail under reciprocal continuation.  It strengthens H2 by
showing exactly where the place-specific lattice geometry enters.  It gives
H3 a concrete multi-ruler selector comparison, but no entropy or global
optimality claim.  The Theory Map and all API maturity levels remain
unchanged.

The more precise Mathematical Core chain is

```text
literal selector history
    -> composable prefix matrix
    -> standard-frame lattice evaluation
    -> finite projective contact
    + retained next-complete-quotient residual
```

Ruban and Browkin are sections choosing representatives of the contact
quotient. They are not unit frames or fundamental domains of the lattice tree.
The reconstruction equation shows why the next complete quotient is decoder
data rather than dispensable bookkeeping. This **refines** the Core's
observer/payload/residual distinction without proposing a generic carrier.

The Engineering Architecture effect is also **refine**: task adequacy is
checked before multi-axis cost, all exact claims use rational arithmetic,
cycle/horizon/termination remain separate failures or outcomes, and no
selector enters optimization without a shared contract. The implementation is
research-local, seconds-scale, and adds no dependency or API pressure.

## 13. Gate handoff

The next responsible question was no longer whether \(p\)-adic continued
fractions could enter; they had entered at exact finite level.  Phase 3 handed
off a **prefix-orbit geometry** task:

1. turn the already materialized consecutive
   \(PGL_2(\mathbb Q_p)\) prefix-lattice vertices into a path-metric ledger;
2. compute exact pairwise tree distance, common ancestors, backtracking, and
   net versus traveled cost;
3. compare Ruban and Browkin on the same bounded rational corpus;
4. only then decide whether a geodesic, reduced-path, or Bellman/Huffman
   interpretation is justified;
5. postpone quadratic irrationals, finite-precision input, convergence rates,
   and periodicity classification until that finite geometry is stable.

That gate is now complete in
[Phase 4](05-phase4-padic-prefix-orbit-path-metric.md).  The bounded histories
have zero backtracking and paired selectors remain on one common finite ray,
so no route-level Bellman or Huffman claim survives.  Further optimization
requires a new frozen source distribution, action set, common terminal
contract, and decoding semantics.
