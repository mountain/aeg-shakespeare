# Phase 8 — continuation-value fibres and the objectification threshold

**Status:** Gates 8A--8E complete for the frozen finite workload.  Exact
partition refinement constructs the coarsest transported extensions of S0--S2
for policy, scalar value, and full continuation semantics.  Nontrivial fibres
are real, but they are highly nonuniform and the S2-stable extension preserves
97.5 percent as many classes as the full tagged state carrier.  Lift-bit
transport is partial, terminating, and many-to-one.  The result is a finite
horizontal task-state extension and an exact obstruction to the proposed
fixed-dimensional, covering, group, or groupoid interpretation; it is not a
vertical process-rank promotion.

**Owner:**
[test_padic_continuation_value_fiber.py](../../tests/research/test_padic_continuation_value_fiber.py)

**Frozen task:**
[11-phase8-continuation-value-fiber-objectification-task-contract.md](11-phase8-continuation-value-fiber-objectification-task-contract.md)

## 1. Verdict

Phase 8 answers the question raised by the Phase 7 residual more sharply.

1. **The residual can be made into an exact finite transported state.**  For
   every frozen local interface and semantic task, finite partition refinement
   terminates at the coarsest stable extension.  Both lift bits descend to
   well-defined partial transitions, and every split has an exact
   distinguishing suffix.
2. **The extension is not one extra bit or one uniform dimension.**  Above S2,
   the largest observed fibre contains 70 stable classes and therefore needs
   at least seven bits under a fixed-width exact label.  Of 6,044 S2 base
   classes, 5,318 are singleton policy fibres, while exceptional fibres range
   irregularly through sizes 2--70.
3. **Composition nearly reconstructs the full task state.**  The 8,336 tagged
   live states reduce to 8,126 scalar-policy/value classes and 8,128 full
   continuation classes.  Thus the transported S2 extension retains about
   97.5 percent as many classes as the full state carrier.
4. **Policy, scalar value, and full reconstruction remain different.**  The
   digit/decoder policy and value modes all induce exactly the same S2-stable
   relation, but full continuation semantics splits two additional classes
   because the terminal decoder output is task-visible even when scalar costs
   and optimal bits agree.
5. **The transport is not a group action.**  At S2 it has thousands of
   terminal edges, 282 invalid bit edges, and 56 live target classes with
   multiple predecessor classes.  There is neither global invertibility nor a
   covering transformation law.
6. **A smaller policy automaton exists only after forgetting the geometric
   base.**  Ignoring S2 leaves 435 digit-policy or 395 decoder-policy response
   types.  These types are strongly task- and ruler-dependent and do not retain
   the full decoder.  They are horizontal task quotients, not vertical
   coordinates over local geometry.

The main conclusion is therefore:

> A nonzero continuation residual proves that the local observer is
> insufficient for the declared future task.  It does not by itself prove a
> new spatial dimension.  In this calibration, the exact compositional repair
> is an irregular directed finite-state extension, not a uniform fibre with a
> group-like transport law.

## 2. The finite stable-extension theorem

Let \(S\) be a finite state carrier, \(A\) a finite partial action alphabet,
\(I:S\to B\) a declared interface, and \(O:S\to Y\) the semantic output to be
preserved.  Every defined edge carries an exact observable label and either a
terminal response or a successor state.

Begin with

\[
\Pi_0=\ker(I,O).
\]

Given \(\Pi_n\), define \(s\equiv_{n+1}t\) when:

1. \(s\equiv_n t\); and
2. for every \(a\in A\), the two edge labels agree and either both edges have
   the same terminal response or their successors are \(\Pi_n\)-equivalent.

### 2.1 Termination

Each round only splits blocks.  A strictly descending chain of partitions of a
finite set has length at most \(|S|-1\), so some

\[
\Pi_\infty=\Pi_N=\Pi_{N+1}
\]

exists.  On the frozen acyclic graphs, no quotient needs more than four
refinement rounds.

### 2.2 Stability and coarseness

The fixed-point equation makes \(\Pi_\infty\) stable under every action by
construction.  Conversely, let \(R\) be any stable equivalence refining
\(\Pi_0\).  If \(R\) refines \(\Pi_n\), stability implies that equal
\(R\)-classes have equal edge labels and \(R\)-equivalent successors, hence
they remain together in \(\Pi_{n+1}\).  Induction gives

\[
R\preceq\Pi_n\quad\forall n,
\qquad
R\preceq\Pi_\infty.
\]

Thus \(\Pi_\infty\) is the **coarsest transition-stable refinement relative
to the declared interface and output**.  This qualification matters: it is not
necessarily the smallest quotient after the interface itself is allowed to be
forgotten.

### 2.3 Distinguishing suffixes

If two states first split at round \(n+1\), some bit has different edge
response or leads to states split by round \(n\).  Recursing produces a bit
suffix of length at most \(n+1\).  Phase 8 materializes a spanning set of these
certificates in every fibre; the exact extractor accepts any requested pair.
The longest observed suffix has length three for S2 and four for S0.

For full continuation semantics, an independent bottom-up structural hash of
the acyclic binary response trees produces exactly the same partition.  This
is independent evidence for the refinement implementation.

## 3. Interface-refinement monotonicity

Suppose interface \(J\) refines interface \(I\):

\[
J(s)=J(t)\Longrightarrow I(s)=I(t).
\]

Then \(\ker(J,O)\) refines \(\ker(I,O)\).  Applying the coarseness induction
above at every round gives

\[
\boxed{
\Pi_\infty(J,O)\preceq\Pi_\infty(I,O).
}
\]

Consequently the total number of stable classes and its exact finite-state
lower bound are monotone:

\[
N(J,O)\ge N(I,O),
\qquad
\left\lceil\log_2N(J,O)\right\rceil
\ge
\left\lceil\log_2N(I,O)\right\rceil.
\]

This is the precise form of the interface/residual tension.  It concerns total
distinguishable task state.  The *conditional* hidden fibre over one base point
can shrink because a refined interface moves information from the residual
into the base.  Total quotient information and unobserved vertical information
must not share one ledger.

The frozen counts obey the theorem:

| semantics | S0 stable classes | S1 stable classes | S2 stable classes |
| --- | ---: | ---: | ---: |
| digit policy | 2,636 | 8,056 | 8,126 |
| decoder policy | 2,636 | 8,056 | 8,126 |
| digit value | 2,636 | 8,056 | 8,126 |
| decoder value | 6,046 | 8,126 | 8,126 |
| full continuation | 8,128 | 8,128 | 8,128 |

The corresponding base-interface class counts are 866, 5,970, and 6,044.
For full continuation, even S0 refines to the same final relation as S1 and S2;
the complete response tree already forces every additional split.

## 4. Gate 8A — exact response universe

The selected workload contains 1,498 finite tasks and 8,336 tagged live
states.  Every Phase 7 census is reproduced:

| family | tasks | states | actions | exact | precision | cycles | horizon | max states/task | max live step |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| R3 | 182 | 682 | 1,316 | 370 | 434 | 12 | 0 | 7 | 2 |
| R5 | 182 | 838 | 1,646 | 448 | 522 | 20 | 0 | 7 | 2 |
| R7 | 182 | 880 | 1,738 | 450 | 564 | 26 | 0 | 7 | 2 |
| D6 | 182 | 988 | 1,928 | 662 | 384 | 76 | 0 | 12 | 3 |
| D8 | 182 | 1,168 | 2,288 | 842 | 204 | 256 | 0 | 17 | 4 |
| P4 | 182 | 886 | 1,750 | 446 | 574 | 26 | 0 | 7 | 2 |
| P6 | 182 | 1,342 | 2,662 | 810 | 548 | 144 | 0 | 14 | 3 |
| I | 224 | 1,552 | 3,048 | 812 | 868 | 40 | 0 | 13 | 3 |

Every rational action is encoded by its exact Phase 7 bit, every successful
witness replays, and the response alphabet preserves `invalid`, `live`, exact,
precision, cycle, and horizon outcomes.  Terminal costs include the frozen
decoder cost; full responses additionally retain the decoded rational or
projective cylinder.

## 5. Gate 8B/C — the S2 fibre census

The strongest local interface has 6,044 base classes.  Its stable extensions
are:

| semantics | initial kernel | stable classes | transport-forced splits | nontrivial fibres | max fibre | residual bits | rounds | suffix range |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| digit policy | 6,172 | 8,126 | 1,954 | 726 | 70 | 7 | 3 | 0--3 |
| decoder policy | 6,154 | 8,126 | 1,972 | 726 | 70 | 7 | 3 | 0--3 |
| digit value | 6,424 | 8,126 | 1,702 | 726 | 70 | 7 | 3 | 0--3 |
| decoder value | 6,970 | 8,126 | 1,156 | 726 | 70 | 7 | 3 | 0--3 |
| full continuation | 6,044 | 8,128 | 2,084 | 728 | 70 | 7 | 3 | 1--3 |

The zero-length suffix in the scalar rows means the current policy or value
output already distinguishes two states in the same S2 fibre.  Positive-length
suffixes certify additional splits forced only by future transport.

### 5.1 Nonuniformity

For the common scalar stable partition:

```text
S2 base fibres                 6,044
singleton fibres               5,318
two-class fibres                 586
fibres with more than 2 classes   140
nontrivial fibres                726  (12.0 percent)
maximum fibre                     70
fixed-width lower bound             7 bits
```

The exceptional sizes are not concentrated at one rank: observed values
include 3--15, 18, 20, 21, 24, 68, 69, and 70.  This is a stratified finite
residual profile, not a constant-rank fibre.

The stable scalar quotient has

\[
\frac{8126}{8336}\approx97.48\%
\]

as many classes as the full tagged carrier.  The full response quotient has
8,128 classes, or about 97.50 percent.  Therefore the exact compositional
extension provides almost no state-count compression once S2 must be retained.

### 5.2 Family breakdown

| family | states | S2 classes | stable classes | nontrivial fibres | max fibre | residual bits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R3 | 682 | 494 | 682 | 42 | 24 | 5 |
| R5 | 838 | 680 | 838 | 32 | 15 | 4 |
| R7 | 880 | 746 | 880 | 14 | 11 | 4 |
| D6 | 988 | 800 | 988 | 42 | 24 | 5 |
| D8 | 1,168 | 978 | 1,166 | 42 | 24 | 5 |
| P4 | 886 | 768 | 886 | 22 | 11 | 4 |
| P6 | 1,342 | 1,216 | 1,334 | 22 | 11 | 4 |
| I | 1,552 | 1,202 | 1,548 | 96 | 28 | 5 |

All five semantic modes have this same within-family stable-class ledger.
R3, R5, R7, D6, and P4 retain one stable class per full state.  The only
within-family identifications are two state pairs in D8, four in I, and eight
in P6.  The larger joint maximum of 70 is partly created when multiple task
families share one S2 base signature but retain different future semantics.

## 6. Three exact witnesses

### 6.1 Immediate residual: the Phase 7 witness survives

The Phase 7 states with \(p=3\), step one, \(k=-1\), \(r=2/3\), the same
current/next lattice geometry, and the same local cost table still split at
round zero because their decoder-optimal first-bit sets are disjoint.  Phase 8
therefore preserves the original positive witness rather than explaining it
away through implementation detail.

### 6.2 Same current policy, different transported future

At \(p=3\), precision four, the initial states for

\[
x=-12,
\qquad
x'=-\frac65

\]

have the same S2 signature and the same decoder-optimal output
\(P_{\mathrm{decoder}}=\{0\}\).  Applying the common suffix `00` keeps both
steps live but reaches different next S2 states:

```text
x  = -12:  next Ruban contact 5/3, infinity coordinate 1 -> 4
x' = -6/5: next Ruban contact 7/3, infinity coordinate 1 -> 22
```

Both reached states prefer bit one, but they are not the same transported
state.  Current optimal choice is therefore not a congruence: a residual is
needed even when the present policy agrees.

### 6.3 Changed stopping surface

For the same input \(x=3/11\), the D6 and D8 initial states have equal S2 and
the same decoder-optimal bit zero.  The common suffix `010` reaches equal
depth-six local geometry, but the next bit-zero edge is:

```text
D6: success_precision, local decoder cost 50
D8: live,              local decoder cost  0
```

Bit one is exact in both cases.  The residual therefore records the declared
stopping task, not a task-free arithmetic coordinate.

### 6.4 Scalar control versus full decoder semantics

Two step-two states have the same S2-stable scalar class:

```text
D6, input -8/11, alpha = 1/3
I,  input  17/7, alpha = 1/3
```

Bit zero is exact in both, with the same full cost vector
\((1,2,3,16)\), but the terminal decoder reconstructs \(-8/11\) in one task
and \(17/7\) in the other.  Full continuation semantics therefore separates
them.  This is the source of the two extra full-response classes: an adequate
policy quotient is not an adequate reconstruction quotient.

## 7. Gate 8D — transport and recurrence

At S2, the descended quotient transitions are:

| semantics | classes | live edges | terminal edges | invalid edges | merged live targets | excess preimages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| scalar policy/value | 8,126 | 6,744 | 9,226 | 282 | 56 | 56 |
| full continuation | 8,128 | 6,744 | 9,230 | 282 | 56 | 56 |

Well-definedness is exact: every representative in one class has the same
edge response and live successor class.  Invertibility fails just as exactly:

- terminal edges have no live inverse;
- invalid bits make the action partial;
- 56 target classes each receive more than one distinct live predecessor
  class under a fixed bit.

The natural finite structure is therefore a directed labelled transition
system, or a small category after adjoining paths and terminal objects.  It is
not a group action, covering transformation system, or groupoid because the
generating arrows are not generally invertible.

### 7.1 What remains after forgetting S2

Bottom-up response types computed without the local base give:

| semantics | behavior types | shared by >=2 families | shared by all 8 families | family-specific |
| --- | ---: | ---: | ---: | ---: |
| digit policy | 435 | 144 | 12 | 291 |
| decoder policy | 395 | 138 | 12 | 257 |
| digit value | 437 | 144 | 12 | 293 |
| decoder value | 3,687 | 331 | 0 | 3,356 |
| full continuation | 8,058 | 194 | 0 | 7,864 |

This ledger cuts in both directions.

- A compact policy-behavior quotient exists if local geometry and decoder
  reconstruction are deliberately forgotten.
- Only twelve policy response types occur in every task family.
- No decoder-value or full-continuation type occurs in all families.
- Almost every full response type is family-specific.

Thus the compact object is a task/ruler-specific controller automaton, while
the reconstruction-bearing object is almost the original state.  Neither is a
uniform vertical coordinate over S2.

## 8. Gate 8E — information and cost ledger

The exact class counts separate three costs:

```text
local S2 base                         6,044 classes
S2 + transported scalar residual      8,126 classes
S2 + full continuation residual        8,128 classes
full tagged live carrier               8,336 states
```

The base already retains about 72.5 percent as many classes as the full state.
Transport adds 2,082 scalar classes above it, a 34.4 percent increase in the
number of represented base/residual states.  Nevertheless both 6,044 and 8,128
lie between \(2^{12}\) and \(2^{13}\), so a single global fixed-width class
identifier remains thirteen bits in this finite census.  The conditional
worst-case residual above one S2 class is seven bits.  These numbers answer
different storage questions and must not be added as if every fibre had the
maximum size.

On the reference Python 3.12 run:

- exact graph and Bellman reconstruction took about 6.4 seconds;
- one uncached S2 policy quotient took about 5.3 seconds;
- subsequent cached semantic modes took about 1.8--2.0 seconds each;
- the complete five-mode, three-interface test module passed in about 51
  seconds.

These are reproducibility measurements, not asymptotic claims.  The module
stays finite and seconds-scale, but it is a research regression rather than a
candidate generic partition API.

## 9. Objectification verdict

Phase 8 establishes the following finite construction:

\[
\mathcal S_{\mathrm{full}}
\longrightarrow
Z_{S2,Q}
\longrightarrow
S2,

\]

where the first map is the coarsest stable quotient relative to S2 and the
declared semantics, and lift bits descend to partial endomorphisms with
terminal outputs.

This earns the phrase **transported finite task-state extension**.  It does not
earn vertical objectification for four independent reasons.

1. **Nonuniform fibre:** the fibre size varies from one to seventy.
2. **Task dependence:** depth, terminal decoder, and scalar ruler change the
   residual semantics; full response types do not persist across all families.
3. **Noninvertible transport:** partial, terminal, and many-to-one edges block
   group, covering, and groupoid interpretations.
4. **No new free grammar or lowering theorem:** refinement composes already
   admitted bit words inside the finite graph.  It does not create new
   primitives whose arbitrary higher-rank composites lower coherently to the
   original rational process.

The right geometric picture is consequently not

```text
S2 x one new coordinate
```

but

```text
an irregular finite directed task-state fibration over S2,
with most fibres trivial and exceptional fibres carrying future semantics.
```

The word *fibration* here describes the explicit projection of finite sets and
directed transitions.  It does not claim a locally trivial topological bundle.

### 9.1 Universal-carrier boundary

The carrier audited here is not a universal object.  It is the disjoint tagged
union of states produced by finitely many primes, stopping depths, input sets,
cost rulers, and decoders.  Phase 8 proves no universal property relating all
such task quotients, and it constructs no task-independent object from which
their projections descend naturally.

This leaves a precise ambiguity.  Some terminal and invalid edges are created
by the frozen stopping contracts, and some many-to-one arrows may be caused by
forgetting different history data in different task quotients.  A larger
continuation carrier could therefore turn part of the observed boundary or
twisting into an ordinary projection effect.  Phase 8 does not rule that out.
It does rule out promoting the *current quotient residual itself* to a new
dimension.

A future universal-carrier claim must pass three separate gates.  It must
construct one carrier \(U\) with compatible task projections
\(q_T:U\to Z_T\); show that task refinement and action continuation give
commuting comparison maps rather than unrelated tagged unions; and then, if a
new dimension is claimed, exhibit task-independent free generators together
with a lowering map natural under their composition.  The first two gates
would explain the observed twisting.  Only the third would establish vertical
objectification.  A universal state carrier can exist without contributing a
new process dimension.

## 10. Claim ledger

### Exact finite theorem-level statements

1. Finite synchronous refinement terminates at the coarsest stable extension
   of a declared interface/output kernel.
2. Interface refinement monotonically refines the stable quotient and cannot
   decrease its total class-count or \(\lceil\log_2N\rceil\) lower bound.
3. Every frozen quotient is stable and idempotent; full response refinement
   agrees with independent bottom-up tree hashing.
4. Every stored split witness produces different exact suffix responses.
5. The frozen class, fibre, transport, recurrence, and family counts are the
   exact values displayed above.

### Corpus statistics

- the 70-class maximum S2 fibre and seven-bit conditional bound;
- the 97.48/97.50 percent stable/full class ratios;
- the family-specific stable-class and behaviour-type counts;
- the 56 merging live targets and absence of all-family full-response types;
- measured Python compilation and refinement times.

### Process Geometry interpretation

- Phase 7's residual is genuine and can be transported exactly after stable
  refinement.
- The repair is horizontal task-state completion, not evidence of a fixed new
  spatial dimension.
- A compact policy quotient and a reconstruction-bearing quotient are
  different objects.
- Preserving a richer interface increases total task distinction even when it
  moves some information out of the hidden fibre and into the base.

### Explicit nonclaims

No result proves a manifold dimension, locally trivial bundle, groupoid,
covering, process rank, task-independent residual, preferred selector,
infinite-future quotient, entropy rate, convergence/periodicity theorem, or
generic minimization/controller API.

## 11. Core, architecture, and map effects

### Mathematical Core — refine

The open continuation-value-fibre question now has an exact finite answer for
the declared p-adic task.  A coarsest stable base-preserving extension exists,
its residual bound is computable fibre by fibre, and interface-refinement
monotonicity connects class refinement to the finite
\(\lceil\log_2N\rceil\) bound.  The result also sharpens the boundary: stable
partial transport is not sufficient for vertical objectification.

### Engineering Architecture — support and refine

Finite partition refinement and bottom-up response hashing provide a certified
solver path for this task.  Policy-only, value, full decoder, base-interface,
and residual costs must be kept separate.  Rich local signatures can destroy
state compression even when a smaller policy automaton exists after forgetting
them.  No dependency or API changes.

### Theory Map — refine without promotion

The result refines H1/H3 and the task-covariant history-evaluation transversal:
future value can require an exact transported residual above local evaluation.
It also supplies a V2 boundary/red team.  A finite stable quotient under
existing actions does not become a higher-rank object without task-independent
semantics, new free composition, and compositional lowering.  Maturity remains
research-local T1/T2 evidence; no stable node or API is promoted.

## 12. Postmortem and next boundary

The original intuition was partly right: the residual is not mere noise, and
it can be object-like enough to support exact transport.  The critical failure
is uniformity.  The residual does not behave like one missing coordinate; its
cardinality, decoder meaning, and transition law depend strongly on the base
state and declared task.

The most important new theorem is therefore not “dimension increases,” but:

> Stable refinement turns a finite residual into a compositional task state,
> while interface refinement monotonically raises total distinguishability;
> neither fact implies vertical process-rank objectification.

A responsible next step should first ask whether these finite p-adic task
quotients descend compatibly from one task-independent continuation carrier.
That audit must distinguish projection-induced boundary/twisting from intrinsic
failure of the lifted action law.  It must not assume that constructing \(U\)
already raises process rank: free composition and coherent lowering remain
separate gates.

The following comparison should then leave the p-adic calibration and seek an
independent domain where a residual does become uniform, admits nontrivial free
composition, and lowers by a law not tied to one finite graph.  The pendulum
sheet bit is a natural positive comparison because it has constant two-sheet
transport on a declared nondegenerate leaf; a branch degeneration or
nonintegrable return-map residual can supply the adversarial boundary.  Only
this universal-carrier audit followed by a cross-domain comparison can decide
whether “residual objectification” deserves a reusable Theory Map node.  No API
extraction is justified by Phase 8 alone.
