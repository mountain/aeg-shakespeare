# Phase 12B result — partition fibres and the Rogers--Ramanujan bridge

**Status:** completed on 2026-08-27 for the frozen B0--B2 workload.

**Contract:**
`21-phase12b-partition-fibres-rogers-ramanujan-task-contract.md`.

**Executable certificate:**
`tests/research/test_partition_fibres_rogers_ramanujan.py`.

This phase remains inside the existing local-field projective Sonnet.  It does
not open an independent partition or Ramanujan Sonnet and does not mix this
calibration with the statistical-mechanics line.

The central result is positive but qualified:

> Partitions supply an exact compositional fibre over total weight.  The fibre
> may forget ordered history while preserving the declared weight task and
> every multiset-union composite.  This earns a **fibred task-exact
> objectification** in the present local contract, but not reconstruction of
> the forgotten order, strict conservative semantic equivalence, or a new
> vertical arithmetic rank.

The Rogers--Ramanujan continued fraction then closes the intended loop.  Its
finite recursion is a depth-dependent projective process; its scalar value is
a projective readout of a two-component carrier; and the classical series,
product, and restricted-partition presentations agree at the coefficient
level without thereby preserving native composition.

---

## 1. Verdict

| Stage | Exact result | Stronger claim refused |
| --- | --- | --- |
| B0: narrow continued-fraction entry | the depth-dependent matrices, tail recursion, and continuant recursion agree for depths 1--12; the formal projective ratios have the frozen common prefixes | ordinary continued-fraction digit semantics, infinite convergence proof, unique history, or modular covariance |
| B1: partition-fibre calibration | abelianization and total weight are exact monoid maps; partitions have free commutative composition and all composites lower exactly | recovery of order, descent of shape observers, strict conservative equivalence, or new process rank |
| B2: cross-presentation return | both restricted partition families agree through weight 30; both Rogers--Ramanujan series equal their residue products through degree 40 | a supplied uniform bijection, preservation of native union, or equality of recursive/combinatorial histories |

All Gates B0--B7 pass with these bounded meanings.

---

## 2. B0 — a nonhomogeneous projective recursion

For the depth-dependent step

\[
M_k(q)=
\begin{pmatrix}
1&q^k\\
1&0
\end{pmatrix},
\qquad
M_k(q)\cdot z=1+\frac{q^k}{z},
\]

the exact truncation satisfies

\[
\binom{A_N(q)}{B_N(q)}
=M_1(q)\cdots M_N(q)\binom11,
\qquad
C_N(q)=\frac{A_N(q)}{B_N(q)},
\]

and the continued-fraction readout is

\[
R_N(q)=q^{1/5}\frac{B_N(q)}{A_N(q)}.
\]

The executable constructs this product in three independent ways: direct
matrix multiplication, inside-out tail recursion, and the continuant
recurrence.  Their integer-polynomial pairs agree at every frozen depth.
Because the matrix grammar explicitly depends on both \(q\) and \(k\), Phase
2's homogeneous regular-digit semantics cannot be imported unchanged.

Let \(G,H\) be the two Rogers--Ramanujan series.  On the frozen degree-40
formal domain, \(B_N/A_N\) and \(H/G\) first differ at the following observed
degrees when that degree lies inside the domain:

| depth \(N\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| first differing degree | 3 | 6 | 10 | 15 | 21 | 28 | 36 |

These are the triangular degrees

\[
d_N=\frac{(N+1)(N+2)}2.
\]

For depths 8--12 the first omitted degrees are 45, 55, 66, 78, and 91, so the
certificate records agreement only through the frozen degree 40.  A long
matching prefix is not used as a proof of infinite convergence.

### Branch and scale ledger

On the 60-cover \(r=q^{1/60}\), define

\[
\Phi(r)=
\begin{pmatrix}
r^{-1}G(r^{60})\\
r^{11}H(r^{60})
\end{pmatrix}.
\]

Then

\[
\frac{\Phi_2(r)}{\Phi_1(r)}
=r^{12}\frac{H(r^{60})}{G(r^{60})}
=q^{1/5}\frac{H(q)}{G(q)}.
\]

The exponent difference \(11-(-1)=12\) is invariant under a common scale
shift.  Therefore the scalar ratio forgets the common scale of \(\Phi\).  This
proves only a typed scale lift and projective readout; no modular or
vector-valued transformation law for \(\Phi\) is asserted.

---

## 3. B1 — partitions as exact compositional fibres

Include the empty object and write

\[
\operatorname{Comp}_0=\mathbb N_{>0}^{*},
\qquad
\operatorname{Par}=\mathbb N^{(\mathbb N_{>0})}.
\]

The first is the free noncommutative monoid under concatenation.  The second
is the free commutative monoid under multiset union \(\sqcup\).

### Theorem 3.1 — exact abelianization and weight lowering

Sorting, equivalently recording part multiplicities, gives the monoid
quotient

\[
a:\operatorname{Comp}_0\twoheadrightarrow\operatorname{Par},
\qquad
a(c\cdot d)=a(c)\sqcup a(d).
\]

Total weight gives a second surjective monoid map

\[
w:\operatorname{Par}\twoheadrightarrow(\mathbb N,+),
\qquad
w(\lambda)=|\lambda|,
\qquad
w(\lambda\sqcup\mu)=w(\lambda)+w(\mu).
\]

Consequently the fibres compose for every pair of weights:

\[
\operatorname{Par}(n)\times\operatorname{Par}(m)
\longrightarrow
\operatorname{Par}(n+m),
\qquad
(\lambda,\mu)\longmapsto\lambda\sqcup\mu.
\]

The executable checks the abelianization on every composition through weight
12, unique multiplicity normal forms on every partition through weight 12,
4,096 composition-pair products and 900 partition-pair products on the
weight-0--6 composition corpus.

### Information contract

| Arrow | Preserves | Forgets | Reconstruction boundary |
| --- | --- | --- | --- |
| \(a:\operatorname{Comp}_0\to\operatorname{Par}\) | parts with multiplicity, total weight, and concatenation after commutativization | order of the parts | no inverse without choosing an ordering section |
| \(w:\operatorname{Par}\to\mathbb N\) | total weight and every union composite | shape, length, largest part, multiplicities, and conjugacy data | the complete residual is the fibre \(\operatorname{Par}(n)\) |
| \(\operatorname{Par}(n)\mapsto p(n)\) | cardinality only | the fibre's elements, statistics, and operations | equal counts do not specify a uniform correspondence |

This is the required positive counterpart to Phase 12A.  Forgetting need not
destroy every semantic law: it may be exact for a declared task and closed
under every legal composite even though it is not invertible.

### 3.2 Earned objectification grade

The frozen four-part gate is met inside this local contract:

1. a partition is exposed by its unique finite multiplicity interface rather
   than treated as an arbitrary sorted list;
2. that interface has the free commutative universal property;
3. multiset union freely produces unseen composites;
4. total weight lowers every legal composite exactly, while the fibre records
   the deliberately forgotten shape.

The occupation-mode factorization below also supplies a calculational gain:
fibre enumeration is replaced by independent multiplicity modes.

The earned phrase is therefore **fibred task-exact objectification**.  Its
qualifiers are mathematical content:

- *fibred* — the residual shape is retained in \(\operatorname{Par}(n)\);
- *task-exact* — total weight and union are exact, not all partition
  observers;
- *objectification* — the quotient has a reusable free commutative interface
  and all-composite lowering.

It is not **strict conservative objectification**, because the ordered source
cannot be reconstructed.  It is not yet **vertical rank raising**, because
this one algebraic quotient does not establish a new task-independent
arithmetic process rank or a cross-rank theory.

This separates two maturities.  The free-monoid/abelianization/weight statement
is a local algebraic theorem.  Its use as a general model of forgetful fibred
objectification remains a research-local candidate.

### 3.3 Euler pushforward

Writing a partition by independent occupation numbers \(m_k\geq0\) gives

\[
\sum_{\lambda\in\operatorname{Par}}q^{|\lambda|}
=\prod_{k\geq1}\sum_{m_k\geq0}q^{km_k}
=\prod_{k\geq1}(1-q^k)^{-1}.
\]

The test independently obtains the coefficients by exhaustive fibre
enumeration and by multiplying the occupation modes.  Through weight 30 the
common sequence is

```text
p(0..30) =
1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176,
231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436,
3010, 3718, 4565, 5604
```

The census contains 28,629 partitions in total.  The composition counts
through weight 12 are

```text
1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048
```

and total 4,096.  These numbers are pushed-forward counting masses; they are
not substitutes for the corresponding fibres.

### 3.4 Observer no-gos

The partitions \((4)\) and \((2,1,1)\) have the same weight but different
length and largest part.  Hence neither shape observer factors through
\(w\).  Conjugation satisfies

\[
|\lambda'|=|\lambda|,
\qquad
\ell(\lambda')=\lambda_1,
\qquad
\lambda'_1=\ell(\lambda),
\]

but it is not a monoid homomorphism for multiset union.  These witnesses stop
the weight task from being silently promoted to full partition semantics.

---

## 4. B2 — cross-presentation strength

For each weight \(n\), let

- \(D_1(n)\) contain partitions with successive parts differing by at least
  two;
- \(P_1(n)\) contain partitions into parts congruent to 1 or 4 modulo 5;
- \(D_2(n)\subseteq D_1(n)\) additionally require smallest part at least two;
- \(P_2(n)\) contain partitions into parts congruent to 2 or 3 modulo 5.

The exact bounded census gives

```text
|D1(n)| = |P1(n)|, n=0..30:
1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 10, 12, 14, 17, 19,
23, 26, 31, 35, 41, 46, 54, 61, 70, 79, 91, 102, 117

|D2(n)| = |P2(n)|, n=0..30:
1, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9, 11, 12,
15, 16, 20, 22, 26, 29, 35, 38, 45, 50, 58, 64, 75
```

The two totals are respectively 893 and 568.  Independently, the two
Rogers--Ramanujan \(q\)-series and their residue-class products agree on all
41 coefficients from degree 0 through degree 40.

These exact finite checks calibrate the classical identities; they are not a
new proof of the infinite products.

### 4.1 The evidence hierarchy does not collapse

The strongest earned levels are:

1. bounded equality of the series and product coefficients;
2. typed equality of the corresponding finite fibre cardinalities through
   weight 30.

No uniform, explicit, computable, or natural family of bijections
\(D_i(n)\to P_i(n)\) is supplied.  Bare set-theoretic existence is not a
separate stronger level here: finite equal cardinalities already imply it.

No structured correspondence is supplied either.  The mandatory red team is
decisive.  Each \(P_i\) is a free commutative submonoid generated by its
allowed residue classes.  By contrast, \(D_1\) is not closed under native
multiset union because

\[
(1)\in D_1,
\qquad
(1)\sqcup(1)=(1,1)\notin D_1,
\]

and the analogous witness \((2)\sqcup(2)\) applies to \(D_2\).  Thus the
coefficient equality cannot be upgraded to a monoid isomorphism using the
native operations, regardless of fibre cardinality.

### 4.2 Return to the projective shadow

The classical bridge

\[
R(q)=q^{1/5}\frac{H(q)}{G(q)}
\]

now has four separately typed presentations in the calibration:

\[
\text{nonhomogeneous recursion}
\longleftrightarrow
(G,H)\text{ series}
\longleftrightarrow
\text{residue products}
\longleftrightarrow
\text{restricted fibre counts}.
\]

Only the declared coefficients and ratios commute in the executable square.
The recursive history, the two-component scale, an explicit partition
correspondence, and native composition are not recovered from the scalar
readout.

---

## 5. Semantic-preservation ledger

| Transformation | Exact retained semantics | Residual or lost semantics |
| --- | --- | --- |
| finite RRCF history \(\to(A_N,B_N)\) | exact depth-dependent projective recurrence | literal history injectivity is not claimed |
| \((G,H)\to H/G\) | scalar ratio | common scale and any stronger two-component transport law |
| \(\Phi\to R\) | ratio on the declared 60-cover | common scale; branch/cover cannot be forgotten globally |
| composition \(\to\) partition | multiset of parts, commutative composition, weight | order |
| partition \(\to\) integer | weight and additive lowering | shape and every nonfactoring observer |
| fibre \(\to\) generating coefficient | cardinality | elements, bijection, statistics, and composition |
| series \(\leftrightarrow\) residue product | bounded coefficients; classical infinite identity used as anchor | combinatorial transport witness |
| \(D_i(n)\leftrightarrow P_i(n)\) | bounded cardinality equality | no supplied uniform bijection and no native monoid correspondence |

The resulting direction of fibration is therefore task-dependent.  One may
forget order while retaining weight-composition exactly; forget shape while
retaining only total weight; forget a two-component scale while retaining a
ratio; or forget individual fibre objects while retaining only counting mass.
These are different information contracts, not instances of one untyped
forgetful arrow.

---

## 6. Gate disposition

| Gate | Disposition |
| --- | --- |
| B0 — type and branch audit | passed: nonhomogeneous steps and the 60-cover remain explicit |
| B1 — exact finite recursion | passed through depth 12 over integer polynomials |
| B2 — partition quotient | passed through the frozen composition/partition domains |
| B3 — free commutative composition | passed: multiplicity normal form, all-composite weight lowering, and Euler coefficients agree |
| B4 — observer boundary | passed negatively for length, largest part, and union-compatibility of conjugation |
| B5 — restricted partition calibration | passed through weight 30 with the native-union failure exposed |
| B6 — presentation-strength verdict | passed at bounded levels 1--2 only |
| B7 — objectification verdict | passed: fibred task-exact objectification earned; strict conservativity and vertical rank refused |

---

## 7. Governance disposition

### Mathematical Core

**Refined in evidence, unchanged in file.**  Phase 12B supplies the missing
positive control for the existing objectification gate: a forgetful fibre map
with a reusable free composition and exact all-composite lowering.  One
partition calibration does not yet establish a generic fibred-objectification
theorem.

### Engineering Architecture

**Unchanged.**  The executable is a research-local, exact finite certificate
using Python integers and `Fraction`, with no external dependency.  Its seven
tests execute in approximately 0.31 seconds in the local runtime.  It adds no
solver abstraction, backend, decoder protocol, or package dependency.

### Theory Map

**V1/V2/V3/V4 evidence refined; maturity unchanged.**  The algebraic chain is
a local theorem-level result.  The broader interpretation as a reusable model
of forgetful semantic objectification remains a research-local candidate,
pending an abstract theorem or independent compositional calibration.  No
stable node, arrow, or T-status is promoted.

### API

**No pressure.**  No partition, fibre, \(q\)-series, continued-fraction, or
objectification helper is proposed for Experimental or Public API.

---

## 8. Explicit nonclaims

Phase 12B does not claim:

- a new proof of the Rogers--Ramanujan identities or convergence of the
  Rogers--Ramanujan continued fraction;
- that the ordinary and \(q\)-continued fractions have the same history,
  matrix, cylinder, or convergence semantics;
- that \(R\) reconstructs \(\Phi\), or that \(\Phi\) has a proved modular or
  vector-valued covariance law here;
- a uniform combinatorial bijection between the difference and residue
  partition families;
- a correspondence preserving multiset union, statistics, chronology, or
  process structure across those families;
- that task-exact lowering is invertible semantic equivalence;
- a generic semantic-fibration theorem, a new vertical process rank, or
  Arithmetic Geometric Universality;
- rank/crank, Ramanujan congruences, circle-method, asymptotic, unit-circle,
  p-adic, physical, or statistical-mechanics results;
- an Experimental or Public API promotion.

---

## 9. Reproduction

Run:

```bash
pytest -q tests/research/test_partition_fibres_rogers_ramanujan.py
```

The seven tests use exact integer-polynomial and rational formal-series
arithmetic.  They certify depths 1--12, series degree 40, compositions through
weight 12, partitions and restricted fibres through weight 30, both exact
monoid laws, the observer no-gos, the native-composition obstruction, and the
qualified objectification verdict.
