# Phase 2 note — exact finite task quotient via `ProcessJetSignature`

**Status:** first experiment that uses Shakespeare machinery to compress a Lonely Runner search presentation.  The result is exact on finite calibration worlds; it is not yet a new pruning theorem for `LRC(13)`.

## 1. From set cover to a finite process language

Phase 1 rewrote the initial `I(k,p,1)` predicate as fixed-cardinality set cover.  To isolate representation effects from the upstream MRV implementation, this experiment deliberately chooses a simpler canonical construction grammar:

```text
fold signs modulo p
fix the first speed to 1
append folded speeds in nondecreasing order
stop after k speeds
```

This grammar enumerates every folded multiset with first element `1` exactly once.  It is **not** the exact traversal order used by upstream `find_cover`; it is a clean alternative presentation on which task equivalence can be computed exhaustively.

A partial state contains the chosen prefix and its current bad-time cover.  The primitive continuation alphabet is the folded speed set

\[
A_p=\{1,\ldots,(p-1)/2\}.
\]

Appending a smaller speed than the last chosen one enters an invalid sink, so every literal continuation word has a well-defined semantics.

## 2. The task is terminal cover, not state reconstruction

For a fixed `(k,p)`, define the observation

\[
Q(h)=1
\]

exactly when `h` is a valid length-`k` canonical history whose bad-time sets cover the whole half-circle.  All shorter histories observe `0`.

If a prefix has depth `d`, there are only `k-d` slots left.  Therefore Shakespeare's existing

```python
process_jet_signature(
    state,
    alphabet,
    transition,
    observe,
    depth=k-d,
)
```

records the **entire remaining future language** of that prefix, not merely a heuristic bounded sample.  Two prefixes with equal signatures accept exactly the same literal continuations within this presentation.

This is a finite, task-relative analogue of a Nerode quotient:

\[
h_1\equiv_Q h_2
\iff
Q(h_1c)=Q(h_2c)
\quad\text{for every remaining continuation }c.
\]

The important point is that the quotient is defined by the requested task, not by equality of tuple syntax or equality of current cover bitsets.

## 3. Red team recovered inside Shakespeare

At `k=3,p=13`, consider

\[
(1,4),\qquad(1,6).
\]

Both prefixes have the same current bad-time cover

\[
\{1,2,3,4,6\}.
\]

But their one-step process-jet signatures differ:

- `(1,4)` accepts continuation `5`;
- `(1,6)` has no accepting canonical continuation.

Thus the exact Shakespeare task signature rejects the over-aggressive merge already identified in Phase 1.

## 4. A positive merge that raw cover state cannot see

The more important test is whether the signature can also justify merges that are **not** visible from current cover equality.

At `k=5,p=17`, the prefixes

\[
(1,1,4),\qquad(1,4,5)
\]

have different current cover sets:

\[
C(1,1,4)=\{1,2,4,8\},
\]

\[
C(1,4,5)=\{1,2,3,4,7,8\}.
\]

Nevertheless their exact depth-two task signatures are equal.  In both cases the only accepting literal continuation is

\[
(6,7).
\]

So, for the terminal-cover task in this canonical grammar,

\[
\boxed{(1,1,4)\equiv_Q(1,4,5)}
\]

even though their present geometric states are visibly different.

This is the first small example in the Sonnet line where Shakespeare certifies a **sound task-relative compression beyond equality of the obvious search state**.

It is still a finite calibration result.  The next mathematical question is whether these semantic classes admit a compact invariant description that can be evaluated more cheaply than computing the full future signature.

## 5. Exact class counts

The executable experiment exhausts all canonical partial prefixes beginning with `1`.

For `k=4,p=13`:

| depth | raw prefixes | exact task classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 6 | 5 |
| 3 | 21 | 5 |
| **total** | **28** | **11** |

This is a raw-history/class-count ratio of

\[
28/11\approx 2.55.
\]

For `k=5,p=17`:

| depth | raw prefixes | exact task classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 8 | 5 |
| 3 | 36 | 7 |
| 4 | 120 | 6 |
| **total** | **165** | **19** |

so

\[
165/19\approx 8.68.
\]

These ratios are **not runtime speedups**.  Computing the full signature by exhaustive continuation enumeration is itself expensive.  They only establish that substantial task-semantic redundancy exists in these small state spaces.

That distinction matters: Shakespeare has identified what may be quotiented; it has not yet discovered a cheap formula for performing the quotient.

## 6. What has actually been learned

The sequence of tests now separates three notions:

```text
current observation
    < current cover geometry
    < exact future task language
```

Neither of the first two determines the third in general.

But the third may identify histories that the first two keep separate.  Hence a useful LRC presentation should not simply minimize retained data.  It should retain exactly enough information to predict future coverability and no more.

This is precisely the pressure that `ProcessJetSignature` was designed to expose in a domain-independent way.

## 7. The next discovery problem

Full future signatures are certificates, not scalable representations.  Phase 3 should search for a compact invariant `S(h)` satisfying

\[
S(h_1)=S(h_2)
\Longrightarrow
h_1\equiv_Q h_2
\]

on exhaustive training worlds, then red-team that implication on held-out `(k,p)` worlds.

Candidate feature grammars should remain elementary and auditable:

1. uncovered-time orbit structure;
2. incidence counts of admissible future speeds against uncovered times;
3. one- and two-step completion-count profiles;
4. overlap ranks or sorted intersection spectra of remaining cover sets;
5. minimal slot deficit under exact small set-cover relaxations.

The direction should be **signature first, invariant second**:

```text
exact semantic classes
    -> inspect collisions
    -> propose compact structural invariant
    -> prove or falsify soundness
    -> only then benchmark pruning cost
```

This avoids designing a statistic around one successful tuple family and calling it a quotient after the fact.

## 8. Claim boundary and relation to upstream

This experiment does not claim that the canonical nondecreasing grammar is faster than upstream `find_cover`, nor that its task quotient can be inserted directly into the upstream MRV search.  The two searches have different construction histories and admissible-continuation languages.

A later cross-presentation step must explicitly construct a `PresentationMorphism` between:

```text
upstream MRV / AvailableChoice state
            and
canonical multiset / task-quotient state
```

and certify preservation of the `I(k,p,1)` solution set.

Only after that bridge exists can class compression be translated into a credible baseline runtime comparison.
