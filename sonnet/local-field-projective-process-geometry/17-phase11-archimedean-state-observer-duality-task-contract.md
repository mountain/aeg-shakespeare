# Phase 11 task contract — Archimedean placement and state--observer duality

**Status:** frozen before execution on 2026-08-26.  This document fixes the
question, finite domains, acceptance gates, red teams, and nonclaims before
`18-phase11-archimedean-state-observer-duality-results.md` or its executable
test is written.

**Predecessor:** Phase 10 separated categorical variance, projective
contragredience, A/M group inversion, and place topology.  It proved an exact
rational ordered-frame round trip, but it did not construct a logical dual of
the complete A/M history--observer chain.

**Executable target:**
`tests/research/test_archimedean_state_observer_duality.py`.

---

## 1. Question

The rational A/M/inversion process grammar exists before an order, absolute
value, topology, or completion is selected.  The real and p-adic evaluations
then equip the same rational carrier with different observer structures.

This phase asks:

> Where exactly does the Archimedean axiom enter the A/M chain, and what is
> the correct contravariant chain on the observer side when logical duality is
> made explicit?

The task is not to declare the p-adic place the logical opposite of the real
place.  It is to separate and compare:

1. the rational A/M process syntax;
2. the Archimedean axiom for an ordered field;
3. order completeness and connectedness at the real completion;
4. state--predicate or finite Stone duality;
5. projective point--hyperplane duality;
6. real and p-adic place evaluation;
7. global compatibility across places.

Only after those types are separated may the phase ask whether the observer
side has a cofree universal property or creates an objectified dual rank.

---

## 2. Starting type correction

### 2.1 Rational A/M syntax is pre-topological

The native finite grammar remains

\[
T_a:z\mapsto z+a,
\qquad
D_k:z\mapsto kz,
\qquad
J_b:z\mapsto \frac b z,
\]

with rational parameters, literal chronological composition, and semantic
lowering to a rational projective matrix.  None of these definitions requires
an order or the Archimedean axiom.

### 2.2 Ordered-field Archimedean axiom

For an ordered field \(K\), freeze the statement

\[
\forall x,y>0\;\exists n\in\mathbb N:\quad nx>y.
\]

Its logical negation is

\[
\exists x,y>0\;\forall n\in\mathbb N:\quad nx\le y,
\]

which asserts an infinitesimal scale relative to \(y\).  This is a statement
about ordered fields.  It is not the strong triangle inequality and it does
not define a p-adic field.

Taking reciprocals inside a fixed Archimedean ordered field gives the
equivalent small-scale statement

\[
\forall \epsilon>0\;\exists n\in\mathbb N:\quad 0<\frac1n<\epsilon.
\]

Large/small reciprocal exchange therefore remains internal to the real
place; it is not a change of place.

### 2.3 Archimedean is not complete or connected

The usual ordered field \(\mathbb Q\) is Archimedean but incomplete and
disconnected in its order topology.  Completion to \(\mathbb R\), rather
than the Archimedean axiom alone, supplies the complete connected real line.

The phase must therefore maintain the ledger

```text
integer cofinality                Archimedean axiom
order and interval predicates    ordered-field structure
limits of all Cauchy sequences   completeness
connected real line              order completeness
regular-CF floor section         order + integer-part choice
hyperbolic metric                real completion + metric ruler
```

### 2.4 Non-Archimedean norm is a different predicate

At a p-adic place,

\[
|x+y|_p\le\max(|x|_p,|y|_p)
\]

creates clopen balls and nested/disjoint refinements.  This valued-field use
of *non-Archimedean* must not be identified with the logical negation in
Section 2.2.  In particular, \(\mathbb Q_p\) is not an ordered field with an
infinitesimal positive element in the ordered-field sense.

---

## 3. Declared logical duality

### 3.1 Finite state--predicate model

For a frozen finite set \(X\), let

\[
\operatorname{Pred}(X)=\mathcal P(X)
\]

with intersection, union, complement, \(\varnothing\), and \(X\).  A state
map \(f:X\to Y\) induces the inverse-image Boolean homomorphism

\[
f^*:\operatorname{Pred}(Y)\to\operatorname{Pred}(X),
\qquad
f^*(P)=f^{-1}(P).
\]

Freeze the contravariant composition law

\[
(g\circ f)^*=f^*\circ g^*.
\]

This is the logical/state--observer duality used in this phase.  Boolean
negation is an operation inside each predicate algebra; taking the opposite
category supplies the arrow reversal.  Neither operation changes a place.

### 3.2 Finite Stone recovery

For a finite set \(X\), points determine Boolean evaluations

\[
\operatorname{ev}_x:\mathcal P(X)\to\{0,1\},
\qquad
\operatorname{ev}_x(P)=1\iff x\in P.
\]

Exhaustively verify on a small frozen set that every Boolean-algebra
homomorphism \(\mathcal P(X)\to\{0,1\}\) is one of these point evaluations.
Also verify the negative control that arbitrary functions
\(\mathcal P(X)\to\{0,1\}\) are overwhelmingly not point evaluations or
Boolean homomorphisms.

This finite recovery is an exact model of logical duality.  It is not yet an
infinite Stone-space theorem for the real or p-adic boundary.

### 3.3 Process and observer transport

Freeze the finite projective state spaces

\[
X_p=\mathbb P^1(\mathbb F_p),
\qquad p\in\{3,5,7\},
\]

and the integral A/M/Weyl generators that remain nonsingular modulo \(p\).
For every frozen history \(w\), state \(x\), and predicate \(P\), verify

\[
w(x)\in P
\iff
x\in w^*(P).
\]

Chronological forward composition must become reverse predicate transport.
This is the observer-side opening of the A/M chain.

### 3.4 Projective incidence is related but distinct

For point vectors and covectors, forwarding a hyperplane with \(g\) uses
\(g^{-T}\); pulling a covector predicate backward uses \(g^T\).  The phase
must record which variance is used.  It must not call either linear action
Boolean complement or identify it with changing \(|\cdot|_\infty\) to
\(|\cdot|_p\).

---

## 4. Quotients, residuals, and dual observers

Freeze a finite task quotient

\[
q:X\twoheadrightarrow Y.
\]

The inverse image

\[
q^*:\mathcal P(Y)\hookrightarrow\mathcal P(X)
\]

must be tested as an injective Boolean homomorphism.  Its image must equal
the predicates constant on every fibre of \(q\), equivalently the unions of
whole fibres.

This gives the declared dual reading:

```text
forward task quotient        observer subalgebra
identified history fibre     predicates unable to distinguish the fibre
retained task information    predicates factoring through q
residual                     predicate not factoring through q
```

A missing predicate that merely separates two states inside a quotient fibre
repairs an observer loss.  It is not a new objectified process dimension.

Use the exact quotient

\[
\mathbb Z/p^2\mathbb Z\to\mathbb Z/p\mathbb Z
\]

for \(p=3,5\).  Exhaustively enumerate quotient predicates and verify that
singleton fine-state predicates are negative controls unless they are whole
fibres.

---

## 5. Archimedean and p-adic observer bases

### 5.1 Frozen Archimedean witnesses

On a finite exact rational corpus:

1. construct an integer \(n\) witnessing \(nx>y\) for every positive
   rational pair \((x,y)\);
2. construct an integer \(n\) witnessing \(1/n<\epsilon\);
3. verify a Pell/convergent sequence approaching \(\sqrt2\) while retaining
   the exact certificate \(p_n^2-2q_n^2=\pm1\);
4. keep the theorem-level red team that \(\sqrt2\notin\mathbb Q\), so this
   Cauchy sequence has no rational limit.

The finite executable supports the witnesses but cannot prove a quantified
Archimedean or completeness theorem by exhaustion.

### 5.2 Frozen p-adic witnesses

On residue rings modulo \(p^d\), exhaustively verify that congruence cylinders
are clopen in the finite ultrametric model and that two cylinders are nested
or disjoint.  Compare these predicates with rational order cuts without
identifying them.

The real floor selector and a p-adic residue representative are both marked
sections, but neither is the logical dual of the other.

### 5.3 Global cross-place control

For a frozen nonzero rational corpus, verify the normalized product formula

\[
|x|_\infty\prod_p |x|_p=1,
\]

where only primes dividing the numerator or denominator contribute.  In
particular,

\[
\log|p^n|_\infty=-\log|p^n|_p.
\]

This is a positive arithmetic compatibility across places.  It must be
labelled global reciprocity/product compatibility, not logical duality.

---

## 6. Bounded cofree/behavior audit

For the frozen finite A/M action alphabet, a state and terminal predicate
determine a bounded behavior table

\[
\beta_{x,P}(w)=1\iff w(x)\in P
\]

for words through a declared maximum depth.  Verify that the same table is
obtained by reverse predicate transport.

The table is a finite shadow of a language, trace, or terminal-coalgebra
observer.  The phase may report whether the frozen predicate family separates
the frozen states.  It must not infer an infinite cofree universal property
from bounded traces.

---

## 7. Objectification gate

The observer-side analogue of the existing objectification test is frozen as

```text
task-independent cogenerator
+ cofree observation/decomposition law
+ all observations pair back to process semantics
+ coherent bidual return
```

Report the primal and dual gates separately:

```text
primal: new primitive + free composition + all-composite lowering
dual:   new cogenerator + cofree behavior + all-observation pairing + biduality
```

Finite Stone recovery satisfies a bounded state--predicate biduality after
Boolean structure is preserved.  It does not by itself prove a cofree history
object, a place-independent observer, or a new vertical rank.

---

## 8. Acceptance gates

### Gate 11A — Archimedean placement

Pass only if the result distinguishes:

- rational process syntax;
- ordered-field Archimedean cofinality;
- completeness;
- connectedness;
- real digit-section choice;
- p-adic ultrametric refinement.

### Gate 11B — finite logical duality

Pass only if inverse image is tested as a contravariant Boolean homomorphism
and finite point recovery is exhaustive on the frozen domain.

### Gate 11C — A/M state--observer square

Pass only if forward projective action and backward predicate transport
commute on all frozen states, predicates, and histories.

### Gate 11D — quotient/residual duality

Pass only if quotient predicates are exactly the fibre-constant predicates
and a nonfactoring residual predicate is retained as a negative witness.

### Gate 11E — place separation and global compatibility

Pass only if real order predicates and p-adic cylinders remain different,
while the rational product formula is verified independently.

### Gate 11F — cofree/objectification verdict

Pass only if bounded behavior is not promoted to an infinite cofree theorem
and observer repair is not promoted to a new process dimension.

---

## 9. Mandatory red teams

1. **Archimedean but incomplete:** \(\mathbb Q\) and the \(\sqrt2\)
   convergents.
2. **Reciprocal but same place:** \(n\to\infty\) versus \(1/n\to0\) over
   the real ordered field.
3. **p-adic not ordered-field negation:** strong triangle inequality must not
   be presented as the negation of the quantified ordered-field axiom.
4. **Arbitrary double dual too large:** arbitrary functions on the predicate
   algebra must outnumber structure-preserving point evaluations.
5. **Quotient loses a discriminator:** a singleton inside one residue fibre
   must fail to factor through the coarse quotient.
6. **Selector mismatch:** real floor and p-adic residue selection must disagree
   on at least one shared rational input in their common domain.
7. **Product formula is not logical duality:** cross-place cancellation must
   be typed separately.
8. **Bounded trace is not cofree universality:** no infinite claim follows
   from the finite behavior table.

---

## 10. Explicit nonclaims

This phase must not claim:

- that the p-adic place is the logical negation or categorical dual of the
  real place;
- that the Archimedean axiom alone produces \(\mathbb R\), connectedness,
  hyperbolic geometry, or regular continued fractions;
- that arithmetic addition/multiplication automatically coincide with
  categorical coproduct/product or logical disjunction/conjunction;
- that Boolean complement, projective contragredience, group inversion, and
  change of place are one operation;
- that finite powerset duality establishes an infinite Stone theorem for the
  real line or Bruhat--Tits boundary;
- that a bounded behavior table is a terminal coalgebra or cofree observer;
- that the product formula constructs an adelic topology or solver;
- that an added discriminating predicate objectifies a new process rank;
- that a new public API is justified.

---

## 11. Governance impact required after execution

If the gates pass, the result must update:

1. `docs/MATHEMATICAL_CORE.md` with the layer separation, finite
   state--predicate theorem, quotient/predicate correspondence, and nonclaim;
2. `docs/ENGINEERING_ARCHITECTURE.md` with a typed forward-state/backward-
   observer pipeline and image/factorization checks;
3. `docs/THEORY_MAP.md` with the status, scope, red teams, and objectification
   verdict;
4. this Sonnet's `README.md` with the Phase 11 index and result summary.

No package API is allowed unless the finite audit independently reveals a
repeated, problem-independent implementation need.  Research-local helpers
remain in `tests/research/`.
