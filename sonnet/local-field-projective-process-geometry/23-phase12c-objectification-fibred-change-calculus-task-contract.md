# Phase 12C task contract — objectification and fibred change calculus

**Status:** initialized and frozen before execution on 2026-08-27.

**Parent:** Phase 12A showed that frame/chart forgetting can obstruct strict
semantic descent.  Phase 12B supplied the positive compositional control:
partitions retain a free commutative operation and exact weight lowering after
ordered history is forgotten.  Phase 12C asks the next question forced by
those two results:

> If objectification is earned, which part of a higher-rank calculus follows
> from it, and which additional response, fibre, coherence, and effectiveness
> data still have to be proved?

**Scope decision:** this phase remains inside
`sonnet/local-field-projective-process-geometry/`.  It is a finite V5
calibration, not a new Sonnet and not a generic calculus/API proposal.

**Future result owner:**
`24-phase12c-objectification-fibred-change-calculus-results.md`.

**Future executable owner:**
`tests/research/test_objectification_fibred_change_calculus.py`.

---

## 0. Research question and provisional answer classes

The phase separates four claims that must not be collapsed.

1. **action skeleton:** an objectified compositional process acts on the
   lower semantic carrier;
2. **response existence:** a declared observer admits changes in a declared
   codomain response language;
3. **coherent response calculus:** those changes satisfy identity, cocycle,
   task-adequacy, and reconstruction laws;
4. **effective calculus:** the response is smaller or cheaper than full
   history and has an executable evaluator, certificate, and failure contract.

The working hypothesis is deliberately asymmetric:

> Strong compositional objectification should automatically give the first
> item.  It should not automatically give the other three for every observer.

The executable must either certify this separation or kill it.

---

## 1. Closest classical lineage

The closest existing formalism is the theory of **change actions**.  A change
action is a set/object acted on by a change monoid.  A derivative is a response
that reconstructs the changed output, and a regular derivative obeys a
base-point-dependent cocycle law.  Neither the change monoid nor its derivative
is required to be additive in the vector-space sense.

Primary lineage anchor:

- M. Alvarez-Picallo and C.-H. L. Ong, *Change Actions: Models of Generalised
  Differentiation*, <https://arxiv.org/abs/1902.05465>.

This phase does not claim to invent change actions, categorical finite
difference, or a nonadditive chain rule.  Its narrower Process Geometry task is
to connect that structure to **earned objectification, semantic fibres,
task-relative descent, residual compression, and effective lowering**.

The lineage comparison is itself a red team.  If all proposed structure is
already exactly a change action with no additional task/objectification
content, no new Process Geometry noun is warranted.

---

## 2. Frozen type ledger

Use right-action notation.  Let

\[
(P,\star,e_P)
\]

be a process monoid and let

\[
\rho:X\times P\to X,
\qquad x\triangleleft p=\rho(x,p)
\]

satisfy

\[
x\triangleleft e_P=x,
\qquad
(x\triangleleft p)\triangleleft q
=x\triangleleft(p\star q).
\]

This is the **finite change/action skeleton**.  Its action category has objects
\(x\in X\) and typed arrows

\[
x\xrightarrow{p}x\triangleleft p.
\]

Composition in this category is process composition, not addition of tangent
vectors.

For a task observer

\[
f:X\to Y
\]

declare a separate response monoid \((Q,\diamond,e_Q)\) acting on \(Y\):

\[
y\blacktriangleleft r.
\]

Define the **derivative/response fibre**

\[
\mathcal D_f(x,p)
=\{r\in Q:
  f(x\triangleleft p)=f(x)\blacktriangleleft r\}.
\]

A chosen response

\[
d_f(x,p)\in\mathcal D_f(x,p)
\]

is **regular** when

\[
d_f(x,e_P)=e_Q,
\]

and

\[
d_f(x,p\star q)
=d_f(x,p)\diamond d_f(x\triangleleft p,q).
\]

This is the candidate native finite chain law.  It is a monoid/action cocycle,
not a linear or infinitesimal law.

### Proposition candidates to audit

1. **Objectification--action proposition.**  If a strong objectification has a
   higher semantic monoid \(P\) and all-composite lowering
   \(L:P\to\operatorname{End}(X)\) preserving identity and chronological
   composition, then \(x\triangleleft p=L(p)(x)\) is automatically a change
   action.  Here the chronological product of endomorphisms is
   \(F\star_{\rm chr}G=G\circ F\), as required by the right-action convention.
2. **Response-fibre criterion.**  On the frozen finite domain, a derivative
   exists exactly when every required \(\mathcal D_f(x,p)\) is nonempty; in
   general, nonemptiness is the pointwise condition and a section/choice must
   also be supplied.  It is forced exactly when the fibres are singletons.  A
   selected derivative still has a separate regularity obligation.
3. **Free-action uniqueness control.**  If the response action
   \(r\mapsto y\blacktriangleleft r\) is injective for every relevant \(y\),
   then every nonempty response fibre is a singleton.  Nonfree actions may
   require a set/fibre-valued residual rather than a scalar difference.

These are elementary consequences of the frozen definitions if their typing
survives execution.  They are not assumed to establish a general Process
Geometry calculus.

---

## 3. Three directions of fibration

The word *fibre* must retain its direction.

| Direction | Projection | Fibre meaning | Phase control |
| --- | --- | --- | --- |
| semantic quotient | \(q:X\to B\) | hidden source objects over one observed value | partitions over weight |
| contract/frame index | \(E\to C\) | charted or framed semantics over one declared contract | Phase 12A frame/chart transport |
| response residual | \(\mathcal D_f(x,p)\to\{(x,p)\}\) | admissible changes reconstructing one observed transition | max/union response |

These fibres need not be invertible, constant-rank, or mutually identifiable.
The executable must not turn them into one untyped bundle.

---

## 4. Positive control A — Multiplication acts on Addition

Use the exact Phase 51 lowering semantics

\[
D_k:T_a\longmapsto T_{ka},
\qquad k\in\mathbb N_{>0},\ a\in\mathbb Z.
\]

The higher process monoid is positive multiplication.  The lower carrier is
the Translation parameter.  For words in retained generators \(D_2,D_3\),
all-composite lowering gives

\[
a\triangleleft(k_1\cdots k_m)
=a\prod_i k_i.
\]

The response is multiplicative rather than additive:

\[
d(a,k)=k,
\qquad
d(a,k\ell)=d(a,k)d(ak,\ell).
\]

The zero Translation object is a mandatory stabilizer red team.  Endpoints
alone cannot recover \(k\) from \(0\mapsto0\), although the typed process token
still retains it.  The action skeleton may therefore be exact while endpoint
response reconstruction is nonunique.

---

## 5. Positive control B — one partition object, several calculi

Let the partition monoid act on itself by multiset union:

\[
\lambda\triangleleft\mu=\lambda\sqcup\mu.
\]

Audit at least four observers:

\[
w(\lambda),
\qquad
\ell(\lambda),
\qquad
m(\lambda)=\max(\lambda)\ (m(\varnothing)=0),
\qquad
\operatorname{supp}(\lambda).
\]

Their response laws are different:

\[
w(\lambda\sqcup\mu)=w(\lambda)+w(\mu),
\]

\[
\ell(\lambda\sqcup\mu)=\ell(\lambda)+\ell(\mu),
\]

\[
m(\lambda\sqcup\mu)=\max(m(\lambda),m(\mu)),
\]

\[
\operatorname{supp}(\lambda\sqcup\mu)
=\operatorname{supp}(\lambda)\cup\operatorname{supp}(\mu).
\]

Thus one objectification does not select one calculus.  The task observer
selects an additive monoid, an idempotent max monoid, a union semilattice, or a
larger residual carrier.

For max response, freeze

\[
\mathcal D_{\max}(a,b)
=\{r:\max(a,r)=b\}.
\]

When \(b>a\), the response is forced to be \(b\).  When \(b=a\), every
\(0\le r\le a\) is compatible.  This is the minimal exact example in which a
noncancellative response makes the derivative a genuine fibre.

---

## 6. Descent and task adequacy

For a quotient \(q:X\twoheadrightarrow B\), an action descends strictly only
when each process sends every \(q\)-fibre into one \(q\)-fibre.  In finite
notation:

\[
q(x)=q(x')
\Longrightarrow
q(x\triangleleft p)=q(x'\triangleleft p)
\quad\forall p.
\]

This is the action analogue of continuation congruence.  If it fails, the base
action is not well defined; a frame, chart, discriminator, or response fibre
must remain.

The Phase 12A projective-addition witness remains the strict-descent negative
control.  No new computation may weaken its conclusion by forcing one value
for unframed \(\infty+1\).

For an earned response calculus, equal response records must additionally be
adequate for the declared future response task.  Endpoint reconstruction alone
does not certify future adequacy.

---

## 7. Mandatory negative controls

### 7.1 Insufficient response language

A nonconstant observed transition cannot have a derivative into a trivial
codomain action.  The executable must give a finite witness with an empty
response fibre.

### 7.2 Tautological response

Allowing the entire endomorphism monoid \(\operatorname{End}(Y)\), or the full
action arrow/history, can manufacture a response for almost any endpoint
transition.  This is an existence upper bound, not an earned calculus.  It
fails the compression/economy gate unless the task independently requires that
full carrier.

### 7.3 Rogers--Ramanujan difference families

Phase 12B proved that the residue-side families are closed under multiset
union while the difference-at-least-two families are not.  Therefore
coefficient equality does not transport the native partition change action.

### 7.4 Hyperoperation associativity

Native exponentiation is not associative:

\[
(2^3)^2=64\ne512=2^{(3^2)}.
\]

It therefore does not itself supply the monoid required by this finite change
action construction.  A typed operadic, sided, or unary-map replacement may
exist, but objectification does not automatically reproduce the same monoid
calculus at every hyperoperation rank.

### 7.5 Additive shadow

Tangent vectors, derivations, Lie brackets, and jets may be recovered only
after extra smooth/refinement, chart, and limiting data are declared.  They
must not appear as primitives in this finite phase.  The relation

\[
D_kT_a=T_{ka}D_k
\]

is the finite transport law; \([A,M]=A\) is its later infinitesimal shadow.

---

## 8. Earned-calculus gates

The result must grade each example against these non-collapsing levels.

### C0 — compositional action

An identity- and composition-preserving action exists on the declared carrier.

### C1 — response existence

Every required response fibre is nonempty in the declared codomain action.

### C2 — coherent reconstruction

A selected response reconstructs the output and obeys the identity/cocycle
law on every declared composite.

### C3 — task adequacy and fibred descent

The response preserves the declared future observations; nonunique or
nonfactoring cases remain explicit fibres/residuals.

### C4 — effective compression

The response has an explicit evaluator and exact certificate and is smaller
or cheaper than full history under a declared finite workload.  Compilation,
storage, residual, and lowering costs are not free.

Only C0 is predicted to follow automatically from the frozen strong
objectification hypothesis.  Calling C0 alone a calculus is forbidden.

---

## 9. Bounded execution plan

The future executable must remain deterministic, exact, dependency-free, and
seconds-scale.

```text
multiplicative generators:       2, 3
free multiplicative depth:       0..6
translation bases:               -6..6
partition weight bound:          0..10
partition-pair response audit:   complete bounded exhaust
max-response bound:              0..10
descent controls:                 exact finite tables
arithmetic domain:               Python integers, tuples, and finite sets
external dependencies:           none
```

The test must report exact counts in the result note.  Bounded exhaust is a
certificate for the declared workload, not a proof of the general literature.

---

## 10. Acceptance gates

### Gate 12C-A — lineage and type audit

Pass only if change actions are acknowledged as the closest existing
formalism and no additive, tangent, or vector-space primitive is imported.

### Gate 12C-B — automatic skeleton theorem

Pass only if identity and arbitrary word composition lower to an exact monoid
action in the A/M control.

### Gate 12C-C — multiple partition responses

Pass only if addition, max, and union response laws are separately typed and
certified on the complete bounded partition exhaust.

### Gate 12C-D — derivative fibre

Pass only if free/cancellative response uniqueness and nonfree max/zero-scale
nonuniqueness are distinguished exactly.

### Gate 12C-E — coherence

Pass only if selected responses obey reconstruction, identity, and cocycle
laws for every frozen composite.

### Gate 12C-F — strict descent

Pass only if the finite descent criterion is executed and the Phase 12A frame
obstruction remains a typed negative control.

### Gate 12C-G — nonautomaticity

Pass only if an insufficient response language yields an empty derivative
fibre, the tautological carrier is refused as evidence, and exponentiation and
Rogers--Ramanujan closure failures are retained.

### Gate 12C-H — calculus verdict

Pass only if C0--C4 grades are reported separately and the result states
exactly what does and does not follow automatically from objectification.

---

## 11. Kill conditions

The corresponding strengthening must be killed if any of the following
occurs.

1. Lowering fails to preserve the higher identity or one legal composite.
2. A claimed derivative fibre is empty on its declared domain.
3. A selected response fails output reconstruction.
4. A selected response fails the identity or cocycle law.
5. A response claimed unique comes from a nonfree action and has two witnesses.
6. A quotient action depends on the chosen lift of one base state.
7. A task-required continuation distinguishes two histories assigned the same
   supposedly sufficient response.
8. A claimed compression merely stores the full history, endpoint pair, or
   arbitrary endomorphism without a declared cost/semantic gain.
9. A native monoid calculus is transported to a family not closed under the
   stated composition.
10. A nonassociative higher operation is used as a change monoid without added
    typing/coherence.
11. An additive tangent, derivation, or jet is used to prove the finite
    process law that was supposed to precede linearization.
12. The proposal duplicates change-action theory while adding no
    objectification, task-fibre, descent, or effectiveness distinction.

---

## 12. Required outputs and governance

Execution must produce:

1. the reserved Phase 12C result note;
2. the reserved exact research executable;
3. a C0--C4 grade for every positive and negative control;
4. a theorem/non-theorem ledger answering the automatic-upgrade question;
5. dispositions for Mathematical Core, Engineering Architecture, Theory Map,
   and API maturity.

Expected disposition:

- **Mathematical Core:** propose at most a bounded refinement of the V5 open
  question; no generic calculus carrier from one phase;
- **Engineering Architecture:** unchanged unless an independently reusable
  evaluator is forced;
- **Theory Map:** refine the distinction between V4 action lowering and V5
  effective analytic closure without maturity promotion;
- **API:** no pressure; all helpers remain inside the research test.

This phase does not claim a smooth, infinitesimal, numerical, stochastic,
cohomological, sheaf, locale, or higher-categorical calculus.  It asks only
whether objectification forces a finite monoidal response skeleton and what
additional evidence is needed before that skeleton deserves the word
*calculus*.
