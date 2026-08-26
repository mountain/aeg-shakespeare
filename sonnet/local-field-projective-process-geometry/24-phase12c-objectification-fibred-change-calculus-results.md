# Phase 12C result — objectification and fibred change calculus

**Status:** completed on 2026-08-27 for the frozen finite 12C-A--H workload.

**Contract:**
`23-phase12c-objectification-fibred-change-calculus-task-contract.md`.

**Executable certificate:**
`tests/research/test_objectification_fibred_change_calculus.py`.

This phase remains inside the existing local-field projective Sonnet.  It does
not open a generic calculus Sonnet, does not enter the statistical-mechanics
line, and does not promote any package abstraction.

The central answer is:

> **Strong compositional objectification automatically supplies a finite
> action/change skeleton, but it does not automatically supply a calculus for
> arbitrary observers.**  Response existence, a regular cocycle choice,
> task adequacy, fibred residuals, and effective compression are separate
> obligations.  When the codomain action is nonfree, the invariant response is
> naturally a fibre rather than a unique scalar difference.

This answer no longer starts from additive variation, tangent vectors, or
jets.  Those structures may arise after extra smooth/chart/limit data.  The
finite primitive here is monoid action and compositional response.

---

## 1. Lineage verdict

The closest existing formalism is **change actions**, not ordinary additive
calculus.  In that theory a change monoid acts on an object, a derivative
reconstructs the changed output, and a regular derivative satisfies a
base-point-dependent cocycle law.  The monoid need not be a vector space, and
the derivative need not be additive in its change argument.

Primary anchor:

- M. Alvarez-Picallo and C.-H. L. Ong, *Change Actions: Models of Generalised
  Differentiation*, <https://arxiv.org/abs/1902.05465>.

Phase 12C therefore claims no invention of a nonadditive derivative or chain
rule.  Its narrower contribution is a typed bridge:

```text
earned objectification
    -> all-composite lowering
    -> change-action skeleton
    -> observer response fibre
    -> regular selected response when available
    -> task/cost/effectivity audit
```

The bridge adds Process Geometry content only at the objectification,
semantic-fibre, descent, future-adequacy, and effective-compression gates.

---

## 2. Exact theorem ledger

Use right actions.  Let \((P,\star,e_P)\) act on \(X\) by

\[
x\triangleleft p.
\]

Let \((Q,\diamond,e_Q)\) act on an observer codomain \(Y\) by

\[
y\blacktriangleleft r,
\]

and let \(f:X\to Y\).

### Proposition 2.1 — objectification gives the action skeleton

Suppose an earned objectification has a higher semantic monoid \(P\) and an
all-composite lowering

\[
L:P\longrightarrow\operatorname{End}(X)
\]

that preserves the identity and composition.  Then

\[
x\triangleleft p=L(p)(x)
\]

is a monoid action:

\[
x\triangleleft e_P=x,
\qquad
(x\triangleleft p)\triangleleft q
=x\triangleleft(p\star q).
\]

This is immediate from the homomorphism laws, but its scope is decisive.  The
action category of typed arrows

\[
x\xrightarrow{p}x\triangleleft p
\]

is the finite response **skeleton** that follows from strong objectification.
It is not yet a calculus for every observer.

The convention is part of the theorem.  Because this phase uses right
actions, \(\operatorname{End}(X)\) carries chronological multiplication

\[
F\star_{\rm chr}G=G\circ F.
\]

Thus \(L(p\star q)=L(p)\star_{\rm chr}L(q)\).  With ordinary function
composition and no convention change, the same right-action lowering would be
an antihomomorphism.  The executable includes a noncommutative affine control
so that commutative scale multiplication cannot hide this variance issue.

### Proposition 2.2 — response-fibre criterion

Define

\[
\mathcal D_f(x,p)
=\{r\in Q:
  f(x\triangleleft p)=f(x)\blacktriangleleft r\}.
\]

Then:

1. on the frozen finite domain, a derivative exists exactly when every
   required fibre \(\mathcal D_f(x,p)\) is nonempty; on a general domain,
   nonemptiness is the pointwise condition and a section/choice must also be
   supplied;
2. the response is forced exactly when every such fibre is a singleton;
3. if the response action at each relevant base point is free, every nonempty
   response fibre is a singleton;
4. a nonfree response action may require the entire fibre or an explicitly
   chosen section as residual data.

These are direct consequences of the definition.  They explain why a unique
subtraction/difference is additional structure rather than a prerequisite for
variation.

### Proposition 2.3 — reconstruction does not imply regularity

A chosen section

\[
d_f(x,p)\in\mathcal D_f(x,p)
\]

reconstructs each observed endpoint.  It is a regular response only if

\[
d_f(x,e_P)=e_Q
\]

and

\[
d_f(x,p\star q)
=d_f(x,p)\diamond d_f(x\triangleleft p,q).
\]

The executable gives a max-action section in which every selected value
reconstructs the endpoint but the displayed cocycle fails exactly.  Hence
response existence and coherent calculus are distinct gates.

### Proposition 2.4 — finite nonadditive fundamental theorem

For a regular response and a finite process history \(p_1,\ldots,p_n\), put

\[
x_i=x_{i-1}\triangleleft p_i.
\]

Repeated reconstruction and regularity give

\[
f(x_n)
=f(x_0)\blacktriangleleft
\bigl(
  d_f(x_0,p_1)\diamond
  d_f(x_1,p_2)\diamond\cdots\diamond
  d_f(x_{n-1},p_n)
\bigr),
\]

with the order fixed by the declared right action.  This is path-ordered
finite reconstruction.  It uses no subtraction, linear tangent space, or
limit.

For composable observers
\(X\xrightarrow{f}Y\xrightarrow{g}Z\), chosen regular
responses have the change-action chain rule

\[
d_{g\circ f}(x,p)
=d_g\bigl(f(x),d_f(x,p)\bigr)
\]

when the response types match.  The executable realizes a nonadditive instance
through

\[
\operatorname{Par}
\xrightarrow{\operatorname{supp}}
\mathcal P(\mathbb N_{>0})
\xrightarrow{\text{contains odd}}
\{\mathrm{false},\mathrm{true}\},
\]

where the response operations are union and Boolean OR.

These propositions are exact under the frozen definitions.  Calling them a
generic Process Geometry calculus would still exceed the evidence.

---

## 3. What is automatic, exactly

The automatic implication is now narrowly typed:

\[
\boxed{
\begin{aligned}
&\text{higher semantic monoid }P\\
&+\ \text{all-composite lowering }L:P\to\operatorname{End}(X)\\
&\Longrightarrow\ \text{change action }X\curvearrowleft P.
\end{aligned}}
\]

Nothing in this implication selects:

- an observer \(f:X\to Y\);
- a codomain response monoid \(Q\);
- existence or uniqueness of \(\mathcal D_f(x,p)\);
- a regular section of those fibres;
- a task-sufficient response quotient;
- a symbolic/numerical evaluator or cost advantage;
- a topology, tangent carrier, derivation, jet, or integral.

Thus objectification automatically determines **where finite variation can be
typed**, not a complete calculus on everything that can be observed.

---

## 4. A/M control — multiplicative response before Lie linearization

The Phase 51 Multiplication object acts on Addition objects by

\[
D_k:T_a\longmapsto T_{ka}.
\]

For words in \(D_2,D_3\), lowering gives the exact positive-multiplicative
action

\[
a\triangleleft(k_1\cdots k_m)
=a\prod_i k_i.
\]

The frozen depth-0--6 language contains 127 literal words but only 28 scale
responses.  Fifteen scale classes have more than one word, and the largest
contains 20 histories.  Every equality of scale response remains stable after
every continuation of depth at most three.

The response is

\[
d(a,k)=k,
\]

and its cocycle is multiplicative:

\[
d(a,k\ell)=k\ell=d(a,k)d(ak,\ell).
\]

All 13 integer bases from \(-6\) through \(6\) pass the action,
reconstruction, and cocycle checks.  The exact finite cross law

\[
D_kT_a=T_{ka}D_k
\]

is also checked on the frozen bases, translations, and dilations without
using the infinitesimal commutator.

A separate noncommutative control checks 2,925 chronological compositions on
the same 13 bases and 15 affine processes.  Translation-then-dilation lowers
to \((2,2)\), while dilation-then-translation lowers to \((1,2)\), so the test
detects reversal of the right-action/endomorphism convention.

### Zero stabilizer fibre

For nonzero base \(2\), the observed transition \(2\mapsto12\) forces the
scale response \(6\).  At the zero Translation object, however,

\[
0\mapsto0
\]

is compatible with every frozen scale \(1,\ldots,10\).  Endpoint data alone
therefore has a ten-element response fibre.  The typed higher process token
retains \(k\), but the endpoint quotient does not reconstruct it.

This is the multiplicative analogue of the Phase 10 stabilizer warning.  Even
when the action calculus is exact, a bare endpoint may forget the process
response.

### Grade

The frozen scale task reaches C0--C4: action, response, cocycle, future
adequacy, and bounded semantic compression are exact.  The claim is finite and
algebraic.  It does not prove smooth V5 closure.  The existing

\[
[A,M]=A
\]

remains the later additive/Lie shadow of the finite transport law, not its
foundation.

---

## 5. Partition control — one objectification, several response geometries

Let partitions act on partitions by multiset union:

\[
\lambda\triangleleft\mu=\lambda\sqcup\mu.
\]

The executable exhausts 139 base partitions through weight ten and 19 change
partitions through weight five, for 2,641 exact observed transitions.  It also
checks all 361 change-pair compositions.

On those 19 typed changes, the weight, length, maximum, support, and odd-part
responses have respectively 6, 6, 6, 10, and 2 distinct values.  These are
task-relative compressions of the change histories, not one common quotient.

Four observers produce four separately typed response monoids:

| observer | response | response composition |
| --- | --- | --- |
| total weight \(w\) | \(w(\mu)\) | addition |
| length \(\ell\) | \(\ell(\mu)\) | addition |
| largest part \(m\) | \(m(\mu)\) | maximum |
| support | \(\operatorname{supp}(\mu)\) | set union |

Every reconstruction and cocycle law holds on the complete frozen exhaust:

\[
w(\lambda\sqcup\mu)=w(\lambda)+w(\mu),
\]

\[
m(\lambda\sqcup\mu)=\max(m(\lambda),m(\mu)),
\]

and similarly for length and support.

This yields a direct negative answer to “does the object choose its calculus?”
It does not.  The same objectified partition monoid supports different response
geometries selected by the declared observer.  Addition is only one case;
maximum, union, and Boolean OR are exact nonadditive controls.

### Max derivative as a fibre

For observed maxima define

\[
\mathcal D_{\max}(a,b)
=\{r\in\{0,\ldots,10\}:\max(a,r)=b\}.
\]

If \(b>a\), this fibre is the singleton \(\{b\}\).  If \(b=a\), it is

\[
\{0,1,\ldots,a\}.
\]

Across stationary bases \(0,\ldots,10\), the executable enumerates 66 response
witnesses.  The explicit transition \(5\mapsto5\) has the six-element fibre

\[
\{0,1,2,3,4,5\},
\]

whereas \(5\mapsto8\) forces \(\{8\}\).

The canonical process-aware section \(d_{\max}(\lambda,\mu)=m(\mu)\) is
regular.  But the endpoint transition alone does not select it.  Moreover, the
test chooses two other legal stationary responses that each reconstruct the
endpoint but violate the max cocycle.  A response fibre, a chosen derivative,
and a regular derivative are therefore three different objects.

### Grade

Weight, length, max, and support reach C0--C4 for their declared bounded tasks
when the process change \(\mu\) remains typed.  Max and support are fibred at
the endpoint level because their codomain actions are nonfree.  None recovers
partition shape from weight or the ordered composition history forgotten in
Phase 12B.

---

## 6. Three fibration directions remain different

Phase 12C confirms the ledger frozen by the contract.

| Direction | Exact positive/negative fact |
| --- | --- |
| semantic quotient fibre \(q^{-1}(b)\) | \(\operatorname{Par}(n)\) retains shapes over total weight; weight action descends exactly |
| frame/contract fibre | framed addition transports between projective frames; forgetting the frame gives incompatible values for \(\infty+1\) |
| response fibre \(\mathcal D_f(x,p)\) | max and zero-scale transitions admit several reconstructing responses |

The first asks which source objects share one task value.  The second indexes
which semantic contract is active.  The third asks which codomain change can
explain one observed transition.  No canonical identification among these
directions is earned.

### Finite descent criterion

For a quotient \(q:X\twoheadrightarrow B\), a process action descends exactly
when

\[
q(x)=q(x')
\Longrightarrow
q(x\triangleleft p)=q(x'\triangleleft p)
\quad\forall p.
\]

The test executes 469 partition-weight transitions: 67 states through weight
eight and seven changes through weight three.  The descended table is exact.
An independent four-state counterexample has two lifts of one base value that
one process sends to different observed targets, so no descended action
exists.

The Phase 12A projective witness is also replayed exactly:

\[
(0,1)\xrightarrow{1/z}(\infty,1),
\qquad
1\xrightarrow{1/z}1,
\]

while

\[
(1,2)\xrightarrow{1/(z-1)}(\infty,1),
\qquad
3\xrightarrow{1/(z-1)}\frac12.
\]

Thus the same unframed input still has incompatible outputs.  Fibred response
does not erase the strict-descent no-go; it records where the missing frame
belongs.

---

## 7. Nonautomaticity red teams

### 7.1 Empty derivative fibre

A two-state toggle observed by the identity map is tested against a trivial
codomain response action.  The source moves from \(0\) to \(1\), while the
only codomain change leaves \(0\) fixed.  Hence

\[
\mathcal D_f(0,\mathrm{toggle})=\varnothing.
\]

Objectification of the source action cannot make an insufficient response
language differentiable.

### 7.2 Tautological endomorphism carrier

On a three-element output set, the full endomorphism carrier has

\[
3^3=27
\]

responses.  A constant endomorphism can realize every one of the nine endpoint
pairs.  This passes bare response existence but is larger than the endpoint
relation and supplies no task-relative compression theorem.  It therefore
fails C4.

This is the exact anti-vacuity boundary: if arbitrary endomorphisms or full
histories are accepted as “derivatives,” nearly every process has a calculus
by definition and the word ceases to discriminate.

### 7.3 Rogers--Ramanujan composition obstruction

The product-side residue families remain free commutative submonoids.  The
difference-at-least-two families fail native union closure because

\[
(1)\sqcup(1)=(1,1)
\]

and

\[
(2)\sqcup(2)=(2,2)
\]

leave the corresponding families.  Coefficient equality therefore does not
transport the native partition change action, much less its response calculus.

### 7.4 Hyperoperation obstruction

Binary exponentiation is nonassociative:

\[
(2^3)^2=64\ne512=2^{(3^2)}.
\]

It cannot itself serve as the change monoid of the present construction.
Unary maps, sided iteration, operadic typing, or another coherent carrier may
repair the situation, but the same-shaped monoid calculus does not follow
automatically at every arithmetic rank.

---

## 8. C0--C4 grade table

| calibration | C0 action | C1 response | C2 regular reconstruction | C3 task/fibre adequacy | C4 effective compression |
| --- | --- | --- | --- | --- | --- |
| A/M scale on Translation parameters | pass | pass | pass | pass with zero stabilizer residual retained | pass on frozen word/scale task |
| partition weight | pass | pass, unique | pass | pass for weight/union only | pass with Phase 12B occupation-mode evaluator |
| partition length | pass | pass, unique | pass | pass for length/union only | pass on frozen finite task |
| partition maximum | pass | pass, generally nonunique from endpoints | canonical section passes; arbitrary section can fail | pass only with response fibre/section typed | pass on frozen max task |
| partition support / odd predicate | pass | pass, generally nonunique from endpoints | union/OR chain passes | pass for declared predicates | pass on frozen finite task |
| trivial codomain response for toggle | pass at source | **fail: empty fibre** | fail | fail | fail |
| full endomorphism response | pass | tautologically pass | selectable | task-dependent | **fail: no compression evidence** |
| Rogers--Ramanujan difference family with union | **fail: not closed** | not applicable | not applicable | coefficient equality only | fail |
| binary exponentiation as change monoid | **fail: nonassociative** | not applicable | not applicable | not applicable | fail |
| unframed projective addition | source transforms exist | incompatible descended output | fail on forgotten base | frame fibre required | fail as strict descent |

Only the first column follows from the strong objectification/action
hypothesis.  Every later column has independent proof obligations.

---

## 9. Answer to the automatic-upgrade question

The strongest exact statement supported by this phase is:

> If objectification produces a compositional higher process monoid with
> all-composite lowering into endomorphisms of a lower semantic carrier, then
> that carrier automatically becomes a change action for the higher process.
> This supplies a finite, nonadditive variation skeleton and its action
> category.  A calculus for a particular observer exists only after a suitable
> codomain response action is declared and all response fibres are nonempty;
> it is coherent only after a regular section/cocycle is supplied; it is
> semantically meaningful only after future adequacy and missing fibres are
> typed; and it is effective only after evaluator, certificate, and total cost
> gates pass.

In compact form:

\[
\boxed{
\text{objectification}
\Longrightarrow
\text{action skeleton}
\not\Longrightarrow
\text{observer calculus}
\not\Longrightarrow
\text{effective analysis}.
}
\]

The first implication is a theorem under the frozen strong-objectification
definition.  The two failed implications are witnessed exactly.

This also corrects the earlier additive bias.  The primary finite notion of
change is not a tangent vector.  It is a typed process response in a monoid or
response fibre.  Additive differential calculus may later arise by choosing a
smooth/refinement regime, chart, unit, completion, and limit in which these
finite laws linearize.

---

## 10. Gate disposition

| Gate | Disposition |
| --- | --- |
| 12C-A — lineage and type audit | passed: change actions are acknowledged; no additive primitive is imported |
| 12C-B — automatic skeleton theorem | passed for every frozen A/M word and split |
| 12C-C — multiple partition responses | passed on 2,641 transitions and 361 response composites |
| 12C-D — derivative fibre | passed: additive uniqueness, max/zero-scale nonuniqueness, and nonregular selection are explicit |
| 12C-E — coherence | passed for the selected A/M, partition, support, and Boolean responses |
| 12C-F — strict descent | passed positively for partition weight and negatively for finite/projective controls |
| 12C-G — nonautomaticity | passed: empty fibre, tautological carrier, native-closure failure, and nonassociativity survive |
| 12C-H — calculus verdict | passed at the finite graded level only; no generic calculus is earned |

The seven exact certificates execute in approximately 0.02 seconds by direct
function invocation in the local runtime.

---

## 11. Governance disposition

### Mathematical Core

**Refined in evidence, unchanged in file.**  The Core already records a
provisional cocycle shape for transported payloads and leaves generic
objectification open.  Phase 12C supplies an exact finite bridge from
all-composite lowering to a change action, plus empty/nonunique response
obstructions.  One arithmetic/combinatorial phase does not select a universal
history payload or calculus carrier.

### Engineering Architecture

**Unchanged.**  The executable uses Python integers, tuples, finite sets, and
`Fraction`.  It is deterministic, dependency-free, exact, and seconds-scale.
It adds no backend, solver path, numerical mode, or package API.

### Theory Map

**Boundary refined; maturity unchanged.**  The result locates the automatic
action skeleton at the V4/V5 boundary:

- V4 all-composite lowering supplies the higher-process action;
- observer response existence and regularity are an additional finite H4/V5
  question;
- smooth/infinitesimal analytic closure and effective analytic closure remain
  strictly stronger.

The broader candidate is at most T1/research-local.  No stable node, arrow,
T-status, or generic rank calculus is promoted.

### API

**No pressure.**  Names such as `ChangeAction`, `ResponseFibre`,
`ProcessDerivative`, `FibredCalculus`, or `AnalyticClosure` remain absent from
Experimental and Public namespaces.  The closest mature lineage must be
understood before any local helper is generalized.

---

## 12. Explicit nonclaims

Phase 12C does not claim:

- invention or generalization of the classical change-action formalism;
- that every objectification produces a monoid rather than an operad,
  category, partial action, or another typed composition carrier;
- that every observer is differentiable for a chosen response language;
- that nonempty response fibres have a natural or regular section;
- that endpoint reconstruction implies future adequacy;
- that every regular response is computationally useful;
- a tangent, cotangent, jet, differential-form, integration, smoothness,
  topology, numerical, stochastic, or continuum theorem;
- V5 smooth or effective analytic closure;
- transport of native composition through the Rogers--Ramanujan coefficient
  identity;
- an automatic continuation of the same calculus through exponentiation or
  higher hyperoperations;
- a generic semantic-fibration theorem, new vertical process rank, Arithmetic
  Geometric Universality, or an Experimental/Public API promotion;
- rank/crank, Ramanujan congruence, circle-method, or asymptotic results.

---

## 13. Reproduction

The repository-standard command is:

```bash
pytest -q tests/research/test_objectification_fibred_change_calculus.py
```

The local runtime used for this phase did not contain the `pytest` module, so
the same seven test functions were imported and invoked directly after
`py_compile`.  All passed in approximately 0.02 seconds.  The certificate
covers 127 A/M words, 28 scale responses, 2,641 partition transitions, 361
partition-response composites, 469 strict-descent evaluations, the complete
bounded additive/max response fibres, and every declared red team.
