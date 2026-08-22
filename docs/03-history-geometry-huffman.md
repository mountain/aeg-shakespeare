# History geometry and Huffman-style depth allocation

**Status:** finite representation strategy; not part of the base process ontology.

## 1. Position in Shakespeare

Shakespeare keeps several questions separate:

1. literal history: what process steps occurred, and in what order?
2. exact relation: which histories may be rewritten by declared process relations?
3. task sufficiency: which histories remain indistinguishable under all bounded allowed continuations for a declared task?
4. history geometry: after those distinctions are fixed, how deep and how wide is the resulting prefix representation?
5. presentation search: is there a cheaper representation?

Huffman coding belongs to layer 4/5.  It is not used to define process equality and it does not decide which histories are semantically/task equivalent.

## 2. Process time as depth

A literal process history

\[
h=X_{i_1}\cdots X_{i_n}
\]

has unweighted depth

\[
d(h)=n.
\]

With caller-declared primitive costs \(c(X_i)\ge 0\), Shakespeare also supports

\[
d_c(h)=\sum_j c(X_{i_j}).
\]

This is **process/representation depth**, not automatically physical clock time.

## 3. Boundary/frontier complexity

For a finite family of histories, let \(B_n\) be the set of distinct prefixes at depth \(n\).  Shakespeare records

\[
W(n)=|B_n|
\]

and

\[
I(n)=\log_2 W(n).
\]

`BoundaryProfile` reports these finite quantities.  An optional caller-supplied quotient key can identify prefixes using an already chosen exact normal form or task-sufficient quotient.

The intended interpretation is:

- depth is the radial/time-like axis of the representation;
- frontier width is the number of distinguishable branches that remain at that depth;
- \(\log_2 W(n)\) is the ideal uniform information needed merely to name one frontier element.

Shakespeare deliberately calls this **boundary complexity**, not standard space complexity.  Equality with a machine-model memory bound requires additional assumptions.

For exploratory asymptotics the finite profile also exposes

\[
\frac{\log W(n)}{n},
\]

a truncated boundary-growth/entropy-rate observable.

## 4. Huffman as one strategy, not the theory

Suppose a task-relevant finite boundary has outcomes \(s_i\) with non-negative usage weights \(w_i\).  Once the symbol set is fixed, `huffman_prefix_code` constructs a binary prefix code minimizing expected code depth among binary prefix trees.

It reports:

- expected depth;
- worst depth;
- Kraft sum;
- source entropy;
- redundancy;
- leaf count;
- an executable encoder/decoder.

For weights

\[
(1/2,1/4,1/8,1/8),
\]

the optimal lengths are

\[
(1,2,3,3),
\]

so expected representation depth is \(1.75\), rather than depth \(2\) for a uniform two-bit code.

The physical process has not become faster.  Common task-relevant histories have become shallower **in this representation**.

## 5. What Huffman does not do

Classical Huffman coding assumes the symbols are already known.  Shakespeare's harder problem is allowed to ask whether a repeated history should itself become a new primitive, for example

\[
Y := X_1X_2X_1X_2.
\]

That is grammar/objectification search, not Huffman coding.

The intended future loop is therefore

\[
\text{histories}
\to \text{relations/task quotient}
\to \text{candidate primitives}
\to \text{boundary measure}
\to \text{prefix-depth strategy}
\to \text{presentation cost}.
\]

Huffman is one admissible strategy inside this loop.  MDL, dictionary grammars, non-binary codes, or continuous history-depth constructions may coexist with it.

## 6. Toward continuous history depth

For an infinite history tree with a cylinder measure \(\mu(C_x)\), a natural continuous analogue is

\[
s(x)=-\kappa^{-1}\log \mu(C_x).
\]

This assigns depth by information mass rather than by a fixed cost per primitive step.  It is a candidate bridge between prefix coding and a canonical process clock, but it is **not implemented in v0.0.1** and should not yet be treated as a theorem of the library.
