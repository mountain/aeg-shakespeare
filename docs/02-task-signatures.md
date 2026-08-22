# Finite Process-Jet Signatures

**Status:** exact bounded task-congruence layer.

This note makes the first task-dependent quotient in Shakespeare computational.

## 1. Why current value is insufficient

Two histories may give the same current task observation and still need to be kept distinct because a later process can expose hidden differences.

For a literal history `h`, let `state(h)` be its current state under caller-supplied semantics and let `T` be the task observation. Equality

\[
T(state(h_1))=T(state(h_2))
\]

is therefore not enough to justify quotienting `h_1` and `h_2`.

## 2. Bounded continuation signature

Choose an ordered process alphabet `Sigma` and a continuation depth `k`. Shakespeare enumerates every literal continuation

\[
w\in\Sigma^{\le k}
\]

including the empty word, with no commutativity assumed.

The finite process-jet signature is

\[
J_T^k(h)=\bigl(T(state(hw))\bigr)_{w\in\Sigma^{\le k}}.
\]

`history_process_jet_signature` computes this object directly from:

- a literal `ProcessWord`;
- an initial state;
- allowed future process steps;
- a transition function;
- a task observation function;
- finite depth `k`.

## 3. Bounded task congruence

`histories_task_equivalent` declares

\[
h_1\equiv_{T,k}h_2
\]

only when the two signatures agree entry by entry. A custom observation comparator may be supplied for approximate/numeric tasks.

This is deliberately finite. It is not claimed to equal the full infinite future congruence. Increasing `k` can split an equivalence class when a longer continuation exposes previously hidden state.

## 4. Relation to the history layer

The free continuation tree is enumerated by `enumerate_process_words`. Literal words are not normalized automatically. If a presentation has explicit history relations, callers may choose to normalize continuations first using the rewrite layer; that quotient is a presentation choice and is kept separate from task equivalence.

Thus the current layering is:

\[
\text{literal history}
\to
\text{optional process-relation normalization}
\to
\text{finite future task signature}
\to
\text{task-sufficient quotient candidate}.
\]

## 5. Why this matters for representation search

A compression step may shorten history or reduce grammar size but is invalid if it merges histories whose future task signatures differ. The signature layer therefore supplies a concrete sufficiency certificate for future costed presentation search.

Conversely, histories with different hidden states may be safely merged for a task when every allowed bounded continuation remains indistinguishable. This is the computational form of the task-quotient idea; Huffman/MDL coding should occur only after such distinguishability has been decided.

## 6. Current boundary

The implementation is exponential in continuation depth by design and is intended for local bounded search. It does not yet provide:

- quotient minimization / partition refinement across a large state set;
- automatic reuse of rewrite-normal forms to reduce continuation enumeration;
- probabilistic continuation weighting;
- continuous/local-jet analogues;
- adaptive depth selection;
- an end-to-end presentation optimizer combining sufficiency with `PresentationCost`.

Those are the next scaling layers, not changes to the basic definition.
