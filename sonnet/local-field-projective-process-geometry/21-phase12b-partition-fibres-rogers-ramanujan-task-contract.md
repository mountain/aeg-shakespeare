# Phase 12B task contract — partition fibres and the Rogers--Ramanujan bridge


**Status:** initialized and frozen before execution on 2026-08-27.

**Parent:** Phase 12A established two strict-descent obstructions and one
finite-jet repair.  Phase 12B supplies the missing positive calibration: a
forgetful map whose fibres retain strict composition, together with a classical
cross-presentation bridge on which stronger semantic claims can be red-teamed.

**Scope decision:** this phase remains inside
`sonnet/local-field-projective-process-geometry/`.  It does not open a new
Sonnet, does not extend the statistical-mechanics calibration, and does not
collect unrelated Ramanujan evaluations.

**Future result owner:**
`22-phase12b-partition-fibres-rogers-ramanujan-results.md`.

**Future executable owner:**
`tests/research/test_partition_fibres_rogers_ramanujan.py`.

The execution order is fixed:

\[
\text{B0: narrow continued-fraction entry}
\longrightarrow
\text{B1: partition-fibre calibration}
\longrightarrow
\text{B2: cross-presentation return}.
\]

---


## 0. Research question

> Can partitions provide a strict compositional positive control for semantic
> fibres, while the Rogers--Ramanujan continued fraction tests exactly which
> information survives transport among recursive, series, product, and
> combinatorial presentations?

The candidate bridge is

\[
\text{nonhomogeneous projective recursion}
\longleftrightarrow
q\text{-series}
\longleftrightarrow
\text{occupation-mode product}
\longleftrightarrow
\text{restricted partition fibres}.
\]

No arrow in this display is assumed to preserve more than its declared
certificate proves.

---


## 1. Classical anchors and claim boundary

The phase may invoke, but does not claim to re-prove, the following classical
results.

1. The Rogers--Ramanujan identities, in DLMF 17.2.49--50:

   \[
   G(q)=\sum_{k\geq0}\frac{q^{k^2}}{(q;q)_k}
   =\frac1{(q;q^5)_\infty(q^4;q^5)_\infty},
   \]

   \[
   H(q)=\sum_{k\geq0}\frac{q^{k(k+1)}}{(q;q)_k}
   =\frac1{(q^2;q^5)_\infty(q^3;q^5)_\infty}.
   \]

2. For \(|q|<1\), the Rogers--Ramanujan continued fraction and quotient
   identity

   \[
   R(q)=\cfrac{q^{1/5}}{1+\cfrac q{1+\cfrac{q^2}{1+\cdots}}}
   =q^{1/5}\frac{H(q)}{G(q)}.
   \]

3. Euler's partition generating function

   \[
   \sum_{n\geq0}p(n)q^n=\prod_{k\geq1}(1-q^k)^{-1}.
   \]

Primary anchors:

- <https://dlmf.nist.gov/17.2#vi>;
- <https://dlmf.nist.gov/27.14#ii>;
- Berndt--Rebák, *The Rogers--Ramanujan continued fraction*,
  <https://arxiv.org/abs/2512.19952>.

The executable may verify bounded coefficient ranges and exact finite
recurrences.  Such checks are regression certificates, not new proofs of the
infinite identities or convergence theorems.

---


## 2. Frozen type ledger

Every execution must keep the following objects distinct.

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(\operatorname{Comp}_0\) | free monoid \(\mathbb N_{>0}^*\) | finite ordered positive-part histories, including the empty word |
| \(\operatorname{Par}\) | free commutative monoid on \(\mathbb N_{>0}\) | finite multisets of positive parts |
| \(a\) | monoid quotient \(\operatorname{Comp}_0\to\operatorname{Par}\) | forget order / abelianize |
| \(w\) | monoid map \(\operatorname{Par}\to(\mathbb N,+)\) | total weight |
| \(\operatorname{Par}(n)\) | fibre \(w^{-1}(n)\) | partitions of the integer \(n\) |
| \(p(n)\) | integer | cardinality of \(\operatorname{Par}(n)\), not the fibre |
| \(\mathcal P(q)\) | formal series or analytic function under a declared mode | pushforward count generating function |
| \(G,H\) | two separate \(q\)-series / product functions | Rogers--Ramanujan functions |
| \(R\) | branch-dependent scalar ratio | Rogers--Ramanujan continued fraction value |
| \(\Phi\) | two-component lifted carrier | \((q^{-1/60}G,q^{11/60}H)^T\) on a declared cover |
| \(M_k(q)\) | nonhomogeneous projective step | matrix representing \(z\mapsto1+q^k/z\) |

The following implications are forbidden without proof:

```text
same analytic value       => same history
same formal series        => explicit combinatorial bijection
same fibre cardinality    => canonical or computable bijection
same projective ratio     => same two-component carrier
strict monoid lowering    => new vertical process rank
```

---


## 3. Phase 12B0 — narrow Rogers--Ramanujan entry

### 3.1 Nonhomogeneous history

Ordinary simple continued fractions use a digit word in a fixed matrix grammar.
Here the step at depth \(k\) is

\[
M_k(q)=
\begin{pmatrix}
1&q^k\\
1&0
\end{pmatrix},
\qquad
M_k(q)\cdot z=1+\frac{q^k}{z}.
\]

For a depth-\(N\) truncation, set \(z_{N+1}=1\) and

\[
z_k=1+\frac{q^k}{z_{k+1}},
\qquad
C_N(q)=z_1.
\]

Then

\[
\binom{A_N(q)}{B_N(q)}
=M_1(q)\cdots M_N(q)\binom11,
\qquad
C_N(q)=\frac{A_N(q)}{B_N(q)},
\]

and the truncated continued-fraction reading is

\[
R_N(q)=q^{1/5}\frac{B_N(q)}{A_N(q)}.
\]

The executable must verify the matrix, tail, and continuant recurrences over
exact integer polynomials.  It must not import the Phase 2 homogeneous digit
claims unchanged.

### 3.2 Branch and cover contract

For real \(0<q<1\), the positive fifth root is unambiguous.  On a complex
domain, either declare a branch of \(\log q\) on a simply connected chart or
lift to

\[
q=e^{2\pi i\tau},\qquad \operatorname{Im}\tau>0.
\]

Then

\[
q^{1/5}=e^{2\pi i\tau/5}.
\]

For the proposed two-component carrier, the convenient cover coordinate is
\(r=q^{1/60}\):

\[
\Phi(r)=
\begin{pmatrix}
r^{-1}G(r^{60})\\
r^{11}H(r^{60})
\end{pmatrix},
\qquad
R(r)=\frac{\Phi_2(r)}{\Phi_1(r)}
=r^{12}\frac{H(r^{60})}{G(r^{60})}.
\]

This algebra proves only that \(R\) is a projective readout and forgets common
scale.  A modular or vector-valued transformation law for \(\Phi\) remains a
future theorem obligation.

---


## 4. Phase 12B1 — partition fibres as the main calibration

### 4.1 Two exact forgetful maps

Include the empty object and define

\[
\operatorname{Comp}_0=\mathbb N_{>0}^*,
\qquad
\operatorname{Par}=\mathbb N^{(\mathbb N_{>0})}.
\]

Concatenation makes \(\operatorname{Comp}_0\) free noncommutative; multiset
union \(\sqcup\) makes \(\operatorname{Par}\) free commutative.  Sorting or
recording multiplicities gives the abelianization

\[
a:\operatorname{Comp}_0\twoheadrightarrow\operatorname{Par},
\qquad
a(c\cdot d)=a(c)\sqcup a(d).
\]

Weight is a second strict monoid map:

\[
w:\operatorname{Par}\twoheadrightarrow\mathbb N,
\qquad
w(\lambda)=|\lambda|,
\qquad
w(\lambda\sqcup\mu)=w(\lambda)+w(\mu).
\]

Thus

\[
\operatorname{Par}(n)\times\operatorname{Par}(m)
\longrightarrow\operatorname{Par}(n+m)
\]

is exact for every composite.

### 4.2 Objectification candidate

This is a positive control for a **strict compositional semantic quotient**:

- order is deliberately forgotten;
- the target has a free commutative grammar;
- all target composites lower by the weight homomorphism;
- the fibres are nontrivial and exactly enumerable;
- the Euler product gives an independent occupation-mode presentation.

Whether this is promoted to strict objectification or a new vertical rank must
still answer:

1. Is `Partition` treated as a new primitive rather than a convenient list
   normalization?
2. Is its free commutative universal property part of the declared interface?
3. Does the presentation provide a calculability, proof, or compression gain?
4. Is lowering sound for every legal composite and every declared relation?

Fibre existence alone does not settle these questions.

### 4.3 Observers and no-go controls

Freeze the observers

\[
|\lambda|,
\quad \ell(\lambda),
\quad \lambda_1,
\quad (m_1(\lambda),m_2(\lambda),\ldots),
\quad \lambda'.
\]

The executable must show:

- total weight descends and composes;
- length and largest part do not factor through weight;
- conjugation preserves weight and exchanges length with largest part;
- conjugation is not a homomorphism for multiset union;
- `p(n)` is the pushed-forward counting mass, not a replacement for the fibre.

### 4.4 Euler product as pushforward

The equality

\[
\sum_{\lambda\in\operatorname{Par}}q^{|\lambda|}
=\prod_{k\geq1}\sum_{j\geq0}q^{jk}
=\prod_{k\geq1}(1-q^k)^{-1}
\]

records independent multiplicity choices in the free commutative generators.
The bounded executable must reproduce its coefficients by both fibre
enumeration and occupation-mode multiplication.

---


## 5. Phase 12B2 — cross-presentation calibration

### 5.1 Four restricted partition families

For each weight \(n\), define:

- \(D_1(n)\): partitions with adjacent parts differing by at least two;
- \(P_1(n)\): partitions into parts congruent to \(1\) or \(4\pmod5\);
- \(D_2(n)\): partitions in \(D_1(n)\) with smallest part at least two;
- \(P_2(n)\): partitions into parts congruent to \(2\) or \(3\pmod5\).

The classical identities imply

\[
|D_1(n)|=|P_1(n)|,
\qquad
|D_2(n)|=|P_2(n)|.
\]

The product-side families \(P_i=\bigsqcup_nP_i(n)\) are free commutative
submonoids on their allowed residue generators.  The difference-side families
\(D_i\) are not closed under ordinary multiset union.  This is a mandatory
composition red team: coefficient equality cannot be promoted to a monoid
isomorphism with the native operations.

### 5.2 Evidence hierarchy

The phase uses the following non-collapsing hierarchy.

1. **Scalar presentation identity:** analytic or formal generating functions
   are identified under declared convergence/formal semantics.
2. **Typed graded equality:** coefficient extraction is explicitly interpreted
   as equality of finite fibre cardinalities for every weight.
3. **Uniform fibre correspondence:** an explicit, natural, or computable family
   of bijections \(\beta_n:D_i(n)\to P_i(n)\) is supplied.
4. **Structured correspondence:** \(\beta\) additionally preserves declared
   statistics, processes, or composition after their transport laws are typed.

For finite fibres, level 2 already implies the bare set-theoretic existence of
some bijection.  Therefore “there exists a bijection” is not admitted as level
3 unless a uniform witness, construction, or naturality property is supplied.

The executable is allowed to establish bounded levels 1--2 only.  It must not
invent a bijection or infer level 4 from matching coefficients.

### 5.3 Return to the projective readout

The bounded certificate should independently construct:

- the nonhomogeneous continued-fraction convergents;
- truncated \(q\)-series for \(G,H\);
- truncated residue-class products;
- the formal ratio \(H/G\);
- the lifted ratio \(\Phi_2/\Phi_1\) on the 60-cover.

Matching finite coefficients is evidence for one cross-presentation square.
It does not prove infinite convergence, modular covariance, equality of
histories, or structured partition transport.

---


## 6. Bounded execution plan

The future executable must remain seconds-scale and deterministic.

```text
continued-fraction depth:       1..12
formal q-series degree:         40
composition exhaust:            weights 0..12
partition exhaust:              weights 0..30
restricted-identity census:     weights 0..30
arithmetic domain:              integer polynomial/formal-series coefficients
branch implementation:          formal 60-cover exponent ledger only
external dependencies:          none
```

The exact counts must be reported by the result note.  Any larger census is
optional and may not replace the structural proofs.

---


## 7. Acceptance gates

### Gate B0 — type and branch audit

Pass only if ordinary and \(q\)-continued fractions remain distinct, every
finite step is typed as \(M_k(q)\), and the fifth/sixtieth-root cover is
explicit.

### Gate B1 — exact finite recursion

Pass only if matrix products, tail recursion, and continuant recursion agree
over exact polynomials for every frozen depth.

### Gate B2 — partition quotient

Pass only if abelianization and weight are exact monoid maps, the fibres are
enumerated, and `p(n)` remains a cardinality.

### Gate B3 — free commutative composition

Pass only if unique multiplicity normal form, all-composite weight lowering,
and Euler occupation-mode coefficients agree.

### Gate B4 — observer boundary

Pass only if weight-preserving and shape-sensitive observers are separated and
explicit collisions block false descent.

### Gate B5 — restricted partition calibration

Pass only if both Rogers--Ramanujan coefficient families agree on the frozen
range and the failure of native union closure on the difference side is shown.

### Gate B6 — presentation-strength verdict

Pass only if scalar equality, coefficient equality, uniform bijection, and
structured transport are reported separately.

### Gate B7 — objectification verdict

Pass only if the result distinguishes strict compositional quotient,
objectification candidate, earned objectification, and vertical rank.

---


## 8. Mandatory red teams

1. Do not reuse ordinary simple-continued-fraction digit semantics unchanged.
2. Do not hide the depth dependence of \(M_k(q)\).
3. Do not hide a principal branch inside \(q^{1/5}\).
4. Do not call a scalar ratio the full two-component carrier.
5. Do not infer matrix/history equality from equality of a convergent.
6. Do not identify \(\operatorname{Par}(n)\) with its cardinality `p(n)`.
7. Do not identify a generating function with an individual fibre.
8. Do not call every forgetting map objectification.
9. Do not infer a vertical rank from a free commutative quotient alone.
10. Do not claim that length or largest part descends through total weight.
11. Do not claim that conjugation preserves multiset union.
12. Do not infer an explicit bijection from a generating-function proof.
13. Do not distinguish bare bijection existence from equal finite cardinality.
14. Do not infer structured transport from coefficient equality.
15. Do not ignore that \(D_i\) fails native union closure while \(P_i\) has it.
16. Do not treat a bounded coefficient match as an infinite identity proof.
17. Do not assert modular or vector-valued covariance of \(\Phi\) without a
    typed transformation law.
18. Do not introduce rank/crank, congruences, circle method, Casimir physics,
    p-adic analysis, or statistical mechanics into this phase.

---


## 9. Kill conditions

The corresponding stronger claim must be killed if any of the following
occurs.

1. Finite matrix and tail recursions disagree.
2. The branch/cover cannot be stated without changing the object.
3. Abelianization fails to preserve composition.
4. Weight fails to preserve multiset union.
5. Euler product coefficients disagree with fibre enumeration.
6. A proposed weight-only observer separates equal-weight partitions.
7. The two restricted coefficient families disagree in the frozen census.
8. The proposed cross-presentation map exists only after an undeclared
   normalization or truncation.
9. A claimed uniform bijection is only an appeal to equal cardinality.
10. A claimed monoid correspondence uses a family not closed under its stated
    composition.
11. The proposed two-component carrier is reconstructed from \(R\) without a
    scale choice.
12. The objectification claim lacks a new primitive interface, free
    composition, all-composite lowering, or calculability benefit.

A killed strengthening does not invalidate the bounded quotient or coefficient
calibration.

---


## 10. Required outputs and governance

Execution must produce:

1. the reserved Phase 12B result note;
2. the reserved exact research executable;
3. a B0/B1/B2 verdict with reproducible counts;
4. an explicit semantic-preservation ledger;
5. dispositions for Mathematical Core, Engineering Architecture, Theory Map,
   and API maturity.

Expected repository disposition:

- **Mathematical Core:** evidence may be refined, but no generic partition or
  modular theorem is promoted from one calibration;
- **Engineering Architecture:** unchanged unless a reusable exact-series
  primitive is independently justified;
- **Theory Map:** the objectification boundary may be sharpened without status
  promotion;
- **API:** no pressure; every helper remains research-local.

Phase 12C is deliberately absent.  Rank/crank observers, Ramanujan
congruences, Hardy--Ramanujan asymptotics, the circle method, unit-circle
singularities, and modular transport may be proposed only after Phase 12B has
classified what the present bridge actually preserves.
