# Phase 7 — binary action normal form and transfer results

**Status:** Gates 7A--7E complete for the frozen workloads.  The Phase 6
coefficient grammar has an exact Ruban-reference binary normal form, the closed
evaluator reproduces Phase 6, and all deeper/new-prime/held-out-input graphs
are exhaustible.  None of the frozen local signatures S0--S2 carries the
scalar-optimal lift relation: exact, including disjoint, policy collisions
survive every transfer red team.  This is not a preferred \(p\)-adic section
or a generic controller API.

**Owner:**
[test_padic_selector_structural_law.py](../../tests/research/test_padic_selector_structural_law.py)

**Frozen task:**
[09-phase7-binary-action-normal-form-transfer-task-contract.md](09-phase7-binary-action-normal-form-transfer-task-contract.md)

## 1. Verdict

Phase 7 separates the two compressions observed in Phase 6.

1. **The action-alphabet compression is a theorem.**  The raw Laurent
   coefficient box is one contiguous rational grid, and its contact fibre is
   exactly
   \[
   A_p(\alpha)=\{r\}\cup\bigl(\{r-p\}\text{ when }r\ge p^k\bigr),
   \]
   where \(k=\min(v_p(\alpha),0)\) and \(r\) is the Ruban truncation.  Every
   action is therefore a reference representative plus one admissible lift
   bit.
2. **The shallow stopping compression was task-dependent.**  Raising the
   precision from four to six and eight grows the maximum live step from two
   to three and four and the maximum per-input graph from seven to as many as
   twenty-three states.  The graphs remain small and exact, but Phase 6's
   depth-two live bound was not structural.
3. **A binary alphabet is not a local selector law.**  Equal contact
   signatures can require disjoint optimal lift bits.  Adding the current and
   next lattice vertices, edge increments, transition outcomes, and locally
   visible costs does not remove the obstruction.
4. **The obstruction transfers.**  It persists at depths six/eight, at the
   unseen primes eleven/thirteen, and on the 224 held-out inputs
   \(X_{18}\setminus X_{12}\).
5. **Binary action storage helps but does not erase state cost.**  On the
   Phase 6 controller tables it reduces total declared table storage by about
   8.4--9.5 percent.  The state keys still dominate.

The structural conclusion is therefore two-sided:

> The legal action grammar has a simple arithmetic normal form, but the
> optimal controller does not descend to the declared local geometric data.
> Alphabet compression and policy-state compression are different problems.

## 2. Gate 7A — proof of the action normal form

Let \(\alpha\ne0\),

\[
k=\min(v_p(\alpha),0),
\qquad
B=p-p^k,
\qquad
r=\lfloor\alpha\rfloor_{p,\mathrm{Ruban}}.
\]

### 2.1 The coefficient image is a complete grid

Write \(m=-k\ge0\).  Scaling a raw coefficient value by \(p^{-k}\) gives

\[
N=\sum_{i=0}^{m}c_i p^i,
\qquad
c_i\in\{-(p-1),\ldots,p-1\}.
\]

For \(m=0\), these values are every integer in
\([-(p-1),p-1]\).  Suppose the first \(m\) places fill

\[
[-(p^m-1),p^m-1]\cap\mathbb Z.
\]

For a fixed top coefficient \(c_m\), the next image is the integer interval

\[
c_m p^m+[-(p^m-1),p^m-1].
\]

Adjacent intervals overlap because \(p\ge3\), and their outer endpoints are
\(\pm(p^{m+1}-1)\).  Induction therefore gives every integer between those
endpoints.  Rescaling proves

\[
\boxed{
\operatorname{image}(C_p^{1-k})
=p^k\mathbb Z\cap[-(p-p^k),p-p^k].
}
\]

The executable red team materializes this equality at

```text
(p,k) = (3,-4), (5,-3), (7,-3), (11,-2), (13,-2),
```

including both endpoints and every grid point.

### 2.2 The contact fibre has one or two members

The Ruban truncation uses coefficients in \(\{0,\ldots,p-1\}\), hence

\[
0\le r\le B.
\]

It is admissible because either \(\alpha=r\) or
\(v_p(\alpha-r)\ge1\).  If \(a\) is any other admissible action, then

\[
a-r=(\alpha-r)-(\alpha-a)\in p\mathbb Z_p.
\]

Both \(a\) and \(r\) lie in \(p^k\mathbb Z\).  Consequently \(a-r\) is an
ordinary integer multiple of \(p\), so write \(a=r+jp\).  Since \(B<p\):

- \(j\ge1\) gives \(a>B\);
- \(j\le-2\) gives \(a<-B\);
- \(j=0\) gives \(r\);
- \(j=-1\) is admitted precisely when
  \[
  r-p\ge-B
  \iff r\ge p-B=p^k.
  \]

Therefore

\[
\boxed{
A_p(\alpha)=
\{r\}
\cup
\begin{cases}
\{r-p\},&r\ge p^k,\\
\varnothing,&r<p^k.
\end{cases}
}
\]

and \(A_p(0)=\{0\}\) by the task convention.  Equivalently,

\[
a=r-\varepsilon p,
\qquad \varepsilon\in\{0,1\}.
\]

The bit \(\varepsilon\) names a legal action; it does not say which action a
task should prefer.

### 2.3 Engineering consequence

The exhaustive evaluator examines

\[
(2p-1)^{1-k}
\]

coefficient tuples before quotienting.  The closed evaluator computes one
Ruban truncation and one threshold, returning at most two rationals.  Phase 6's
maximum raw counts 625, 729, and 2,197 disappear from graph construction
without changing the semantic action set.

This is a proved evaluator replacement for the declared grammar, not a new
public continued-fraction primitive.

## 3. Gate 7B — exact Phase 6 equivalence

The closed evaluator reproduces all 546 Phase 6 tasks:

| \(p\) | states | actions | exact edges | precision edges | cycle edges | initial frontiers | exact/precision frontiers |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 682 | 1,316 | 370 | 434 | 12 | 202 | 186 / 16 |
| 5 | 838 | 1,646 | 448 | 522 | 20 | 182 | 182 / 0 |
| 7 | 880 | 1,738 | 450 | 564 | 26 | 182 | 182 / 0 |

Every reachable Ruban and Browkin action belongs to the normal form, every
initial Bellman witness replays through the shared decoder, and the Phase 6
maximums remain seven states, fourteen action edges, and live step two.

The equivalence is semantic, not merely cardinal: the stored action sequences,
outcomes, Pareto costs, terminal matrices/cylinders, and decoder residuals are
unchanged.

## 4. Gate 7C — the local-signature obstruction

For each successful state frontier and each scalar task, record the set of
first lift bits attaining the minimum named axis.  Phase 7 then partitions
states by the three frozen signatures:

- **S0:** contact data \((p,k,r,\operatorname{sign}\alpha,[\alpha=r])\) and
  remaining horizon;
- **S1:** S0 plus current/next lattice vertices, edge increments, and immediate
  outcome classes;
- **S2:** S1 plus exact locally visible stage or terminal costs.

An exact collision is a signature class containing different optimal-bit
sets.  A **disjoint collision** is stronger: no one bit is optimal for every
state in the class.

### Phase 6 regression workload

| signature | scalar state records | signature classes | collisions | digit / decoder | disjoint collisions |
| --- | ---: | ---: | ---: | ---: | ---: |
| S0 | 4,800 | 866 | 96 | 48 / 48 | 78 |
| S1 | 4,800 | 3,840 | 86 | 44 / 42 | 66 |
| S2 | 4,800 | 3,840 | 86 | 44 / 42 | 66 |

S1 distinguishes most states that S0 merged, but 66 classes still require
incompatible choices.  Adding the local cost data in S2 does not remove a
single regression collision.

### 4.1 One replayable S2 witness

At \(p=3\), the following three step-one states have identical S2 signature:

```text
k = -1
r = 2/3
sign(alpha) = negative
remaining horizon = 15
current vertex = root

bit 0: next vertex affine(depth=2, coordinate=5), edge cost 2, live
       local cost (1,2,4,0)
bit 1: same next vertex, edge cost 2, live
       local cost (1,2,5,0)
```

Yet decoder-minimal continuation differs:

| episode input | current \(\alpha\) | prefix matrix | optimal first bit | optimal suffix and total decoder cost |
| ---: | ---: | --- | ---: | --- |
| \(-11\) | \(-1/12\) | \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\) | 0 | \((2/3,-4/3)\), decoder 13 |
| \(-7/8\) | \(-8/15\) | same matrix | 1 | \((-7/3,5/9)\), decoder 17 |
| \(-1/5\) | \(-5/6\) | same matrix | 0 | \((2/3,-2/3)\), decoder 12 |

For the middle state, bit zero has precision-success continuations with decoder
costs 37 and 36, whereas bit one reaches the displayed exact continuation at
decoder cost 17.  Thus the two actions have the same evaluated next geometry
and their local cost order favours bit zero, but the future reverses the
decoder choice.

This is the precise obstruction:

> A lossless action alphabet quotient does not imply that Bellman value
> descends through the current contact, lattice transition, or local cost
> signature.

The missing distinction is not another local edge label; it lies in the
continuation state and decoder-bearing history.

## 5. Gate 7D — harder transfer workloads

All stress graphs remain inside the frozen budgets; none reaches the
twenty-four-step horizon.

### 5.1 Greater precision on \(X_{12}\)

| \(p\) | depth | states | actions | cycles | max states/input | max actions/input | max live step | frontier records | max frontier |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 6 | 988 | 1,928 | 76 | 12 | 24 | 3 | 188 | 2 |
| 3 | 8 | 1,168 | 2,288 | 256 | 17 | 34 | 4 | 188 | 2 |
| 5 | 6 | 1,248 | 2,466 | 114 | 13 | 26 | 3 | 182 | 1 |
| 5 | 8 | 1,506 | 2,982 | 328 | 19 | 38 | 4 | 182 | 1 |
| 7 | 6 | 1,330 | 2,638 | 134 | 14 | 28 | 3 | 182 | 1 |
| 7 | 8 | 1,678 | 3,334 | 324 | 23 | 46 | 4 | 182 | 1 |

Every initial frontier at depths six and eight is exactly terminal.  Moving the
precision surface outward removes the Phase 6 precision-success records from
the Pareto frontiers, even though the full graphs contain precision terminal
edges.  At \(p=3\), six extra exact Pareto records remain, so its multiobjective
branching does not disappear.

### 5.2 New primes on \(X_{12}\)

| \(p\) | depth | states | actions | cycles | max live step | frontier records | exact / precision |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 4 | 886 | 1,750 | 26 | 2 | 182 | 182 / 0 |
| 11 | 6 | 1,342 | 2,662 | 144 | 3 | 182 | 182 / 0 |
| 13 | 4 | 1,056 | 2,112 | 24 | 2 | 184 | 178 / 6 |
| 13 | 6 | 1,716 | 3,432 | 122 | 3 | 182 | 182 / 0 |

The binary normal form transfers unchanged.  The new-prime policy statistics
do not follow one monotone pattern: \(p=13,d=4\) has a small mixed
exact/precision frontier, which disappears at depth six.

### 5.3 Held-out inputs at depth six

The exact holdout has

\[
|X_{18}\setminus X_{12}|=224.
\]

| \(p\) | states | actions | cycles | max states/input | max live step | frontier records | max frontier |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 1,552 | 3,048 | 40 | 13 | 3 | 256 | 2 |
| 5 | 1,922 | 3,810 | 60 | 14 | 3 | 224 | 1 |
| 7 | 2,066 | 4,106 | 74 | 15 | 3 | 224 | 1 |

All held-out Pareto frontiers are exactly terminal.  The \(p=3\) task again
retains a two-point multiobjective structure on part of the corpus.

### 5.4 Signature obstruction under transfer

| workload | signature | records | classes | collisions | digit / decoder | disjoint |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| depth 6/8 | S0 | 15,836 | 1,092 | 102 | 53 / 49 | 98 |
| depth 6/8 | S1 | 15,836 | 9,876 | 106 | 63 / 43 | 88 |
| depth 6/8 | S2 | 15,836 | 10,104 | 106 | 63 / 43 | 88 |
| primes 11/13 | S0 | 10,000 | 862 | 60 | 31 / 29 | 52 |
| primes 11/13 | S1 | 10,000 | 7,336 | 44 | 22 / 22 | 38 |
| primes 11/13 | S2 | 10,000 | 7,488 | 44 | 22 / 22 | 38 |
| held-out inputs | S0 | 11,080 | 1,486 | 206 | 107 / 99 | 183 |
| held-out inputs | S1 | 11,080 | 9,256 | 181 | 96 / 85 | 167 |
| held-out inputs | S2 | 11,080 | 9,392 | 181 | 96 / 85 | 167 |

The local signatures are not merely overfit on the Phase 6 corpus: their
failure transfers.  S2 can distinguish more classes than S1 on the harder
tasks, but it never reduces the collision count there.

## 6. Gate 7E — storage ledger

The original Phase 6 table stored an exact rational action in every entry.
The normal form stores no choice bit at a one-action state and one bit at a
two-action state, plus one fixed-prime normal-form metadata record per table.
State keys are unchanged and fully charged.

| \(p\) | scalar | entries | state bits | rational action bits | choice bits | metadata | original total | binary total | saving |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | digit | 364 | 11,802 | 1,462 | 316 | 3 | 13,264 | 12,121 | 1,143 |
| 3 | decoder | 372 | 12,139 | 1,472 | 324 | 3 | 13,611 | 12,466 | 1,145 |
| 5 | digit | 372 | 13,124 | 1,746 | 342 | 4 | 14,870 | 13,470 | 1,400 |
| 5 | decoder | 372 | 13,124 | 1,746 | 342 | 4 | 14,870 | 13,470 | 1,400 |
| 7 | digit | 366 | 13,250 | 1,776 | 344 | 4 | 15,026 | 13,598 | 1,428 |
| 7 | decoder | 366 | 13,250 | 1,776 | 344 | 4 | 15,026 | 13,598 | 1,428 |

The action payload shrinks strongly, but total storage shrinks modestly because
the exact task state dominates.  Phase 7 therefore supplies a useful codec,
not a compact general policy.

## 7. Claim ledger

### Exact theorem-level statements

1. The frozen coefficient image is the complete grid
   \(p^k\mathbb Z\cap[-(p-p^k),p-p^k]\).
2. The frozen contact-lift grammar has the exact Ruban-reference binary normal
   form displayed in Section 2.
3. Closed and exhaustive evaluators agree on the certified comparison domain,
   and the closed evaluator reproduces every Phase 6 result.
4. Every frozen depth, prime, and input-transfer graph is exhausted within the
   declared budgets; every initial witness replays exactly.
5. The S0--S2 collision counts, disjoint witnesses, and storage ledgers are the
   exact finite values displayed above.

### Corpus statistics

- the graph sizes, live depths, terminal-edge counts, and Pareto-frontier
  counts on D, P, and I;
- the persistence of \(p=3\) multiobjective frontiers;
- the mixed \(p=13,d=4\) frontier and its disappearance at depth six;
- the exact amount of storage saved by the declared table layout.

### Process Geometry interpretation

Phase 7 adds a new separation to the local-field chain:

```text
raw coefficient syntax
    -> exact binary action alphabet
    -> chronological history / residual-bearing Bellman state
    -> evaluated local geometry and costs
    -> future value and terminal decoder
```

The first arrow is lossless for legal action semantics.  The attempted arrow
from local evaluation to optimal policy is not: S2 collision witnesses block
it.  Thus canonicalizing an operation alphabet can be exact and economical
without canonicalizing histories or optimal continuations.

Equivalently, the complete Bellman state now appears as a nontrivial
task-relative fibre over the local signature:

\[
\pi:\mathcal S_{\mathrm{full}}\longrightarrow
\mathcal S_{\mathrm{S2}}.
\]

A disjoint collision proves that at least two future-value classes occur in
one fibre, hence at least one retained bit is necessary for that finite task.
This is evidence for a **continuation-value fibre**, not yet for a new manifold
dimension or process rank.  A geometric or objectified dimension would require
the fibre classes to carry a stable transported composition law, survive task
changes, and lower back to the declared continuations and decoders.

### Explicit nonclaims

No result selects a task-free section, compresses the full controller into a
closed selector rule, proves asymptotic graph growth, or establishes general
convergence, periodicity, entropy, Lagrange, infinite-boundary, or
continuous/discrete complexity results.  The normal form applies to the
declared coefficient grammar, not every mathematically interesting
\(p\)-adic digit system.

## 8. Core, architecture, and map effects

### Mathematical Core — refine

The finite projective calibration now has an exact additional information
boundary: coefficient syntax quotients losslessly to one reference rational
plus a lift bit, while optimal continuation does not quotient through the
declared contact/geometry/local-cost signatures.  This refines the distinction
between action presentation, task state, and continuation residual; it adds no
general minimal-state theorem.

### Engineering Architecture — support and refine

The normal form replaces exponential raw tuple enumeration by a direct exact
evaluator and reduces action-table payload.  The transfer audit also supplies
a negative architecture constraint: an action codec must not be mistaken for
a local policy compiler.  Complete-quotient, matrix, visited, and decoder data
remain in the problem-local solver.  No dependency or API changes.

### Theory Map — refine without promotion

The result refines H3 and the emerging task-covariant evaluation transversal.
Finite control can admit an exact binary alphabet while still requiring
history-bearing value semantics beyond local evaluated geometry.  This is a
new obstruction against collapsing history evaluation directly to a policy,
not evidence for a new stable node or API maturity.

## 9. Postmortem and next boundary

The strongest positive result is simpler than the original policy-compression
hope: the action grammar itself has a closed arithmetic theorem.  It removes a
real computational cost and compresses the action payload without changing
task semantics.

The stronger hope fails cleanly.  S0--S2 do not explain the optimal choice,
and their failure survives every frozen holdout.  This is not a reason to add
opaque features until the table is memorized.  It says that the chosen local
observation has crossed an information-loss boundary before Bellman value is
determined.

The next responsible question is therefore narrower than "find a more clever
classifier."  One should characterize the **minimal continuation residual
needed for value descent**.  On the finite binary action process, define

\[
s\sim_Qs'
\quad\Longleftrightarrow\quad
\text{all common admitted suffixes have the same outcomes and value fronts}.
\]

A future phase can compute the resulting fibre classes, their
\(\lceil\log_2N_Q\rceil\) residual bound, and their transport under lift bits.
Only if those classes close compositionally and persist across independent
tasks should they be considered a finite bundle/groupoid or a candidate new
objectification dimension.  Until then they are a task-sufficient state lift,
not a rank promotion.  The phase must charge state, decoder, and compilation
cost and retain the S2 witness as a mandatory negative control.  No API
extraction is justified yet.
