# Phase 1 note — `I(k,p,1)` as a set-cover completion process

**Status:** first baseline reconstruction; no new pruning theorem claimed.

## 1. The upstream bottleneck has a simpler combinatorial presentation

For `l=1`, the gcd clause in `(k,p,l)`-properness is vacuous. A residue tuple is improper exactly when it has no witness among

\[
t=\frac a p.
\]

Because distance to the nearest integer is invariant under `a -> -a`, it suffices to inspect

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

Then a `k`-tuple `(s_1,...,s_k)` lies in `I(k,p,1)` precisely when

\[
\boxed{C_{s_1}\cup\cdots\cup C_{s_k}=U_p.}
\]

So the initial LRC sieve is an exact **fixed-cardinality set-cover problem**.

This is not an analogy. The upstream C++ `find_cover` precomputes one bitset `cover(i)` for every folded speed residue and accepts a length-`K` history exactly when the union bitset covers every half-circle time position.

## 2. What upstream `find_cover` actually retains

The upstream DFS state contains

```text
covered          bad-time positions already covered
chosen speeds    construction history / current tuple
AvailableChoice  which speed choices remain live
```

It chooses a still-uncovered time with the fewest currently available covering speeds, then branches only on choices that cover that selected time. Near leaves it also applies an optimistic coverage bound.

One subtlety matters for our reconstruction: this MRV traversal is **not** equivalent to simply appending speeds in nondecreasing numerical order. A smaller speed skipped because it does not cover the currently selected time is not automatically eliminated; it may become usable later after the selected time is covered by another speed.

Therefore subsequent Shakespeare experiments will distinguish:

```text
upstream MRV presentation
        versus
canonical nondecreasing multiset presentation
```

and will not attribute the history semantics of one to the other.

## 3. A first exact terminal reconstruction at `k=3,p=13`

For `p=13`, sign folding leaves six speed residues

\[
1,2,3,4,5,6.
\]

As an independent canonical enumeration, allowing nondecreasing length-three tuples gives

\[
\binom{6+3-1}{3}=56
\]

folded multisets.

The executable reconstruction in

```text
tests/research/test_lonely_runner_initial_sieve.py
```

cross-checks two independent terminal predicates:

```text
exact rational-grid no-witness test
            ==
bad-time fixed-cardinality set cover
```

on all 56 tuples. It finds

```text
56 folded sorted tuples
14 improper / full-cover tuples
3 canonical classes after the global unit quotient
```

with canonical improper representatives

```text
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
```

Thus the combinatorial object under the initial sieve is now frozen independently of the upstream implementation details.

## 4. A deliberately simple canonical construction grammar

To ask a clean representation question, introduce a separate baseline grammar:

```text
fix the first folded speed to 1
append folded speeds in nondecreasing order
stop after k entries
```

This grammar enumerates folded multisets canonically, but it is not proposed as a faster replacement for upstream MRV.

Inside this grammar, a tempting compression is to identify partial histories whenever they have the same current covered-time bitset and the same depth. That already fails at `k=3,p=13`.

Consider

\[
(1,4),\qquad(1,6).
\]

They have exactly the same current cover:

\[
C_1\cup C_4=C_1\cup C_6=\{1,2,3,4,6\}.
\]

Only time position `5` remains uncovered in either state. But their admissible futures differ:

```text
(1,4)  -> 5 remains admissible -> complete cover
(1,6)  -> only 6 remains admissible -> no complete cover
```

Hence

\[
\boxed{
\text{same current cover + same depth}
\not\Rightarrow
\text{same future completion language}.
}
\]

This red team does **not** claim to reproduce upstream `AvailableChoice`. It establishes the more general point that once a presentation canonicalizes construction history, admissible future choices become part of task semantics.

## 5. The Shakespeare formulation

For any chosen construction presentation, let a partial history `h` determine:

- current cover `C(h)`;
- remaining slots;
- an admissible continuation language `A(h)`.

Let the terminal task predicate be

\[
Q(h)=1
\]

iff `h` is or can become a full bad-time cover within the presentation.

A sound task quotient must preserve continuation semantics:

\[
h_1\sim h_2
\quad\Longrightarrow\quad
Q(h_1c)=Q(h_2c)
\]

for every continuation word represented in the comparison grammar.

The upstream MRV state is one sufficient representation for its own traversal. The canonical multiset state is another. Shakespeare should compare them through explicit task semantics rather than assume their internal states coincide.

## 6. Candidate quotient directions

The next experiments should stay exact and auditable.

### 6.1 Orbit of uncovered-time geometry

Quotient uncovered subsets under residual multiplication/reflection symmetries only when those symmetries also transport the admissible continuation language.

### 6.2 Cover-incidence signatures

For each uncovered time, record the number or orbit-types of future choices that can cover it. Upstream `get_next_to_cover` already uses the first scalar shadow of this information.

### 6.3 Pairwise overlap profiles

Measure intersections such as

\[
|C_s\cap U_{\rm uncovered}|,
\qquad
|C_s\cap C_{s'}\cap U_{\rm uncovered}|,
\]

but promote such data only if future-completion equivalence is certified on exhaustive small worlds.

### 6.4 Exact finite future signatures

For a finite grammar, directly enumerate continuation behavior and cluster histories by the resulting task signature. Then search for a simpler invariant description of the classes.

The intended workflow is

```text
exact semantic quotient first
    -> inspect equivalence classes
    -> discover a compact invariant
    -> red-team it elsewhere
```

rather than guessing a pruning statistic and calling it a quotient after a few successes.

## 7. Connection to existing Shakespeare machinery

This reconstruction maps directly onto existing abstractions:

- `ProcessWord` — construction histories;
- `ProcessJetSignature` — finite future task language;
- `PresentationMorphism` — certified maps between different search presentations;
- `PresentationCost` — state count, branch count, certificate and reconstruction costs;
- Pareto filtering — compare presentations without assuming maximal compression is always optimal.

We should **not** introduce a generic SetCover API. Set cover is the current calibration domain, not Shakespeare's ontology.

## 8. Next experiment

Phase 2 therefore uses the canonical nondecreasing grammar, where the full remaining future is small enough to enumerate exactly, and applies the existing `ProcessJetSignature` machinery directly.

The goals are two-sided:

1. verify that the signature refuses unsound merges such as `(1,4)` / `(1,6)`;
2. find **positive** merges where different raw cover states nevertheless have identical complete future task languages.

Only after such task-semantic redundancy is measured should we search for a cheap invariant capable of replacing exhaustive future enumeration. A later phase must separately construct a certified bridge back to the upstream MRV / `AvailableChoice` presentation before any runtime claim is made.
