# Phase 1 note — `I(k,p,1)` as a set-cover completion process

**Status:** first baseline reconstruction; no new pruning theorem claimed.

## 1. The upstream bottleneck has a simpler combinatorial presentation

For `l=1`, the gcd clause in `(k,p,l)`-properness is vacuous.  A residue tuple is improper exactly when it has no witness among the times

\[
t=\frac a p.
\]

Because distance to the nearest integer is invariant under `a -> -a`, it suffices to inspect the half-circle

\[
U_p=\{1,2,\ldots,(p-1)/2\}.
\]

For a folded speed residue

\[
s\in\{1,\ldots,(p-1)/2\},
\]

define its bad-time cover

\[
C_s=\left\{a\in U_p:
\left\|\frac{as}{p}\right\|<\frac1{k+1}
\right\}.
\]

Then a `k`-tuple `(s_1,...,s_k)` is in `I(k,p,1)` precisely when

\[
\boxed{C_{s_1}\cup\cdots\cup C_{s_k}=U_p.}
\]

So the initial LRC sieve is an exact **fixed-cardinality set-cover problem**.

This is not an analogy: it is the literal predicate implemented by the upstream `find_cover` bitsets.  The C++ precomputes one bitset `cover(i)` for each folded speed residue, marks a time position when

```text
rem * (K + 1) < P
or
(P - rem) * (K + 1) < P,
```

and accepts a length-`K` speed history exactly when the union bitset covers every half-circle time position.

## 2. Upstream DFS as a process presentation

The upstream `find_cover` search state contains three components:

```text
covered          bad-time positions already covered
chosen speeds    construction history / current tuple
available choice remaining speed residues allowed by enumeration order
```

The recursive step chooses a speed residue that covers a selected still-uncovered time, adds its cover bitset, and consumes one slot.

The implementation also uses two pruning ideas:

1. **most constrained uncovered time** — choose an uncovered position with the fewest remaining speed choices that can cover it;
2. **optimistic coverage bound** — when few slots remain, bound how many uncovered positions the best remaining choices could possibly cover.

This is recognizably a constraint-search presentation.  It is already better than enumerating all tuples, but it is not obviously minimal for the LRC task.

## 3. A first exact reconstruction at `k=3, p=13`

For `p=13`, sign folding leaves six speed residues

\[
1,2,3,4,5,6.
\]

Allowing nondecreasing length-three tuples gives

\[
\binom{6+3-1}{3}=56
\]

candidate folded tuples.

The independent exact reconstruction in

```text
tests/research/test_lonely_runner_initial_sieve.py
```

finds:

```text
56 folded sorted tuples
14 tuples whose bad-time sets cover the whole half-circle
3 canonical classes after the global unit quotient
```

with canonical improper representatives

```text
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
```

The set-cover predicate is cross-checked tuple-by-tuple against a direct rational-grid witness predicate, rather than against itself.

## 4. Why `covered` alone is not a sufficient state

A tempting Shakespeare compression would identify partial histories whenever they have the same covered-time bitset and the same number of chosen speeds.

That fails even in the tiny `k=3,p=13` calibration.

Consider the two nondecreasing partial histories

\[
(1,4),\qquad(1,6).
\]

They cover the same five time positions:

\[
C_1\cup C_4=C_1\cup C_6=\{1,2,3,4,6\}.
\]

Only time position `5` remains uncovered in either state.  Yet their future task semantics differ under the ordered completion grammar:

```text
(1,4)  -> choose 5 -> complete cover
(1,6)  -> only 6 or later is allowed -> no completion
```

Thus

\[
\boxed{
\text{same covered set + same depth}
\not\Rightarrow
\text{same future completion semantics}.
}
\]

The upstream code therefore has a real reason to retain `AvailableChoice`; it is not merely an implementation detail.

This is a second, independent future-signature pressure after the Phase-0 lift example.

## 5. The Shakespeare formulation

We can now state the first representation problem without LRC-specific prose.

Let a partial search history `h` determine:

- a current cover subset `C(h) subset U_p`;
- remaining slots `r(h)`;
- an admissible continuation language `A(h)` induced by canonical enumeration.

Define the task predicate

\[
Q(h)=1
\]

iff some admissible continuation of length at most `r(h)` completes the cover.

A sound history quotient must preserve this future language:

\[
h_1\sim h_2
\quad\Longrightarrow\quad
Q(h_1c)=Q(h_2c)
\]

for every continuation represented in the comparison grammar.

The known upstream state is one sufficient presentation.  The Shakespeare question is whether we can discover a cheaper one.

## 6. Candidate quotient directions

The next experiments should not immediately add opaque learned features.  Start from exact combinatorial candidates:

### 6.1 Orbit of uncovered-time geometry

Instead of the absolute bitset, quotient uncovered subsets under residual multiplication/reflection symmetries that remain compatible with the available-choice frontier.

### 6.2 Cover-incidence signatures

For each uncovered time, record the number or orbit-types of remaining speed choices that can cover it.  The upstream `get_next_to_cover` already uses the first scalar shadow of this information.

### 6.3 Pairwise overlap profile

Record the intersection pattern

\[
|C_s\cap U_{\rm uncovered}|,
\qquad
|C_s\cap C_{s'}\cap U_{\rm uncovered}|,
\]

for admissible future choices, but only promote such a profile if future-completion equivalence can be certified on exhaustive small instances.

### 6.4 Bounded future signature

For solved small `(k,p)`, directly compute whether each short continuation leaves a completable state.  Cluster histories by this signature, then inspect whether the clusters admit a simpler invariant description.

This reverses the usual workflow:

```text
first discover the exact quotient empirically on exhaustive small worlds
then search for a compact invariant that explains it
```

rather than guessing a pruning statistic and hoping it generalizes.

## 7. Connection to existing Shakespeare machinery

This set-cover reconstruction interacts naturally with several existing layers:

- `ProcessWord`: chosen-speed construction history;
- task signatures: bounded future completion behavior;
- `PresentationMorphism`: exact maps between labelled tuple search, sign-folded search, unit-orbit canonical search, and any newly discovered quotient;
- `PresentationCost`: state count, branch count, certificate cost, reconstruction cost;
- Pareto search: compare quotients without assuming maximum compression is universally optimal.

We should **not** yet add a generic SetCover API to Shakespeare.  Set cover is the current mathematical calibration, not the ontology.  A reusable abstraction should be promoted only if another Sonnet or existing calibration forces the same state semantics.

## 8. Next experiment

The immediate next executable target is:

1. exhaust `k=3` over several primes and `k=4` over small primes;
2. enumerate reachable partial histories under the upstream ordered grammar;
3. compute exact bounded/full completion equivalence classes;
4. compare class count against the upstream `(covered, available-choice frontier, slots)` state count;
5. search small invariant grammars for a signature that exactly predicts those classes;
6. red-team every proposed merge on the next larger `(k,p)` not used for discovery.

Only after a stable quotient appears should we port the experiment toward `k=8..12`, where the upstream runtime baseline becomes meaningful.
