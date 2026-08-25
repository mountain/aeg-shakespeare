# Phase 7f — objectifying the A/M contact arrangement as a pair-difference sign system

**Status:** positive structural prototype after the Phase-7e four-speed red team.  
**Scope:** exact bounded contact alphabet through center `2`, relative domain `u4/u1 < 8`; still Gate A.

Fast regression:

```text
tests/research/test_lonely_runner_four_speed_pair_difference.py
```

Full exact census / Huffman comparison is intentionally opt-in:

```text
.github/workflows/sonnet-lonely-runner-pair-difference-census.yml
```

The heavy census is not a routine five-version CI gate.

## 1. The object is a labeled difference graph, not a 3D grid

For four relative speeds, quotient global M scale and put

\[
x_i=\log u_i.
\]

Every A/M contact-collision wall has the form

\[
\boxed{x_j-x_i=\log c},
\]

with rational contact ratio

\[
c=\beta/\alpha.
\]

Equivalently, no logarithm is required in the implementation:

\[
\boxed{u_j=c\,u_i}.
\]

So a contact stratum can be presented as a graph:

```text
vertices        runners i
edge (i,j)      relative M coordinate u_j/u_i
edge labels     contact ratios c
edge state      < c, = c, > c
```

The crucial point is that the six pair edges are not independent.  Around every graph cycle their relative M displacements must be jointly realizable.

## 2. Exact multiplicative difference constraints

Ordinary difference constraints use

\[
x_v-x_u\le a.
\]

Here we store

\[
x_v-x_u\le\log c
\]

by the rational multiplier `c` itself.  Path composition multiplies the rational labels:

\[
\log c_1+\log c_2=\log(c_1c_2).
\]

Hence a directed cycle is impossible exactly when

\[
\prod c_e<1,
\]

or when

\[
\prod c_e=1
\]

and at least one inequality on the cycle is strict.

This gives an exact Floyd/negative-cycle-style consistency certificate using only rational multiplication and comparison.  There is no floating-point logarithm and no ambient polyhedral solver.

The smallest red team is already illustrative:

\[
\frac{u_2}{u_1}<\frac32,
\qquad
\frac{u_3}{u_2}<\frac32
\]

forces

\[
\frac{u_3}{u_1}<\frac94.
\]

The graph closure rejects the contradictory request `u3/u1 > 9/4` before any parameter tuple is constructed.

## 3. First census: cycle consistency removes almost all fake combinations

For `k=4`, threshold `delta=1/5`, contact centers through `2`, and relative domain

\[
1<\frac{u_j}{u_i}<8,
\]

the primitive contact constants generate seven collision ratios:

\[
\frac{11}{9},\quad
\frac32,\quad
\frac{11}{6},\quad
\frac94,\quad
\frac{11}{4},\quad
4,\quad6.
\]

They cut each of the six pair ratios into

```text
7 equality strata + 8 open intervals = 15 pair strata.
```

If the pair coordinates were treated as independent, the presentation would contain

\[
15^6=11{,}390{,}625
\]

joint sign assignments.

Exact cycle consistency leaves only

\[
\boxed{5{,}823}
\]

realizable pair-difference sign systems.

Thus before applying the Lonely Runner observer at all:

\[
\boxed{
11{,}390{,}625\longrightarrow5{,}823
}
\]

or roughly a three-order-of-magnitude removal of combinatorial states that never belonged to the A/M geometry.

This is the first payoff of objectifying the arrangement rather than enumerating an ambient 3D grid.

## 4. Task semantics can be read directly from the sign graph

No representative point in `(r2,r3,r4)` is required.

A contact event on runner `i` has lifted time

\[
\tau_i=\frac{\alpha}{u_i}.
\]

For runners `i<j`, two events satisfy

\[
\frac{\alpha}{u_i}<\frac{\beta}{u_j}
\iff
\frac{u_j}{u_i}<\frac{\beta}{\alpha}.
\]

The right side is exactly one edge-sign query already stored in the pair-difference system.

Therefore the graph determines the complete contact-event preorder for the declared bounded alphabet.  From that preorder the exact `before / on-contact / after` observer derives the first lonely witness.

Across all 5,823 realizable systems the center-2 bounded task has

\[
\boxed{60\text{ first-witness semantics}.}
\]

This is conceptually important: the sign graph is not merely an acceleration data structure for a later geometric solver.  It is already a process presentation from which the contact history can be interpreted.

## 5. Task-relative quotient

The full graph contains

\[
6\times7=42
\]

contact-wall sign coordinates.

Delete one wall coordinate at a time and ask whether any previously distinct sign systems with different first-witness tasks would be merged.  Only

\[
\boxed{21}
\]

wall coordinates are task-relevant.

Keeping those 21 signs collapses

\[
5{,}823\text{ realizable systems}
\longrightarrow
\boxed{849\text{ exact task-safe sign strata}}
\longrightarrow
60\text{ task semantics}.
\]

The representation ladder is now

```text
independent pair-stratum product       11,390,625
        ↓ cycle realizability
A/M pair-difference geometry                5,823
        ↓ task-relative wall quotient
exact task-safe sign geometry                 849
        ↓ observer quotient
first-witness semantics                         60
```

## 6. Huffman/history geometry now produces a real Pareto frontier

Use only after freezing the complete center-2 geometry.  The usage distribution is

```text
1 <= u1 < u2 < u3 < u4 <= 8,
u4/u1 < 8,
```

namely 55 quadruples.

The literal event-by-event contact histories over the complete 5,823-stratum geometry have boundary widths

```text
1, 1, 3, 9, 27, 49, 65, 71, 67, 64, 62, 58, 40, 17, 10
```

hence

\[
W_{\max}=71,
\qquad
\sum_dW(d)=544,
\qquad
d_{\max}=14.
\]

On the 55 usage inputs the total contact depth is

\[
280,
\]

so

\[
E[d]_{contact}=280/55\approx5.091.
\]

### Time-first exact tree

Search over ternary trees whose decisions must be one of the 21 retained A/M edge walls, minimizing lexicographically

1. usage-weighted depth;
2. total tree nodes = boundary volume;
3. worst depth;
4. internal decision nodes.

The optimum has

```text
weighted depth      135
boundary volume     328
worst depth           9
internal nodes      109
```

or

\[
\boxed{E[d]=135/55\approx2.455.}
\]

Its root is the native contact comparison

\[
\boxed{u_4/u_1\ ?\ 4.}
\]

This time-optimal point has peak frontier `72`, one state above the literal contact peak `71`, so it should **not** be described as simultaneous space/time dominance.

### Balanced Huffman Pareto point

Force the first distinction to

\[
\boxed{u_3/u_1\ ?\ 6}
\]

and re-optimize every descendant exactly.  This nearby tree has

```text
weighted depth      174
boundary volume     328
worst depth           9
peak frontier        69
```

therefore

\[
E[d]=174/55\approx3.164.
\]

Relative to literal contact evolution it improves every recorded axis:

\[
\boxed{
\begin{aligned}
W_{\max}:&\quad71\to69,\\
\sum W(d):&\quad544\to328,\\
d_{\max}:&\quad14\to9,\\
E[d]:&\quad5.091\to3.164.
\end{aligned}
}
\]

This is exactly why Shakespeare should keep a **space-time Pareto frontier** rather than silently scalarize representation quality.

The time-first tree and the balanced tree are different legitimate optima under different preferences.

## 7. Frozen transfer and an explicit calculus-horizon boundary

Freeze:

- the seven center-2 contact ratios;
- cycle consistency rules;
- the 21 retained walls;
- the 849-stratum task map;
- both decision trees.

Then test every integer quadruple through speed `13` with `u4/u1<8`:

\[
\boxed{515\text{ quadruples},\quad515/515\text{ exact}.}
\]

No new wall or tree parameter is introduced.

At speed `14` there is an explicit counterexample:

```text
(2, 6, 9, 14)
```

whose true first witness requires a center-3 contact distinction.  The frozen center-2 geometry therefore misclassifies it.

This failure is useful and qualitatively different from Phase 7e's sample-tree failure:

- Phase 7e failed **inside the same intended geometry** because sampled tuples did not cover the strata;
- Phase 7f is complete for its declared center-2 contact alphabet and fails only when the **calculus horizon itself** must be enlarged.

So the next problem is not “add more training samples.”  It is “objectify refinement in contact-center depth.”

## 8. New structural direction

The pair-difference graph suggests a recursive calculus presentation:

```text
contact center 0..m
    -> finite ratio label alphabet C_m
    -> consistent gain/sign graph on runner pairs
    -> task-relevant sign quotient
    -> Huffman decision DAG/tree
    -> observer asks whether center m+1 refines any current task class
```

The decisive scaling question becomes the growth of **task-relevant graph refinements** with contact center and runner count, rather than the size of a Cartesian arrangement.

This is a much more plausible route toward higher `k` because the primitive spatial carrier has only

\[
\binom{k}{2}
\]

runner-pair edges and all higher consistency lives in graph cycles.

## 9. API pressure

Do not promote a generic graph-arrangement API yet.  The research-local object now wants roughly:

```text
PairDifferenceConstraint(i, j, ratio, sign)
PairDifferenceSystem
exact_cycle_closure(...)
realizable(...)
contact_order(...)
task_quotient(...)
history_geometry(...)
```

The likely mathematical abstraction is a rational multiplicative/gain-graph shadow of the A/M contact calculus, not an arbitrary CSP or hyperplane arrangement.

An independent calibration should be required before this becomes public API.

## Claim boundary

No new Lonely Runner case is proved.

What Phase 7f establishes at bounded four-speed scale is the structural loop

\[
\boxed{
\text{A/M contact calculus}
\to
\text{pair-difference gain/sign graph}
\to
\text{cycle-complete geometry}
\to
\text{task quotient}
\to
\text{space-time Huffman Pareto frontier}.
}
\]

This is the first four-speed representation that directly addresses the completeness failure exposed by Phase 7e rather than hiding it under a larger sample.
