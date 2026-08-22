# Ordered Process Rewriting

**Status:** exact finite-word core; deliberately small.

This note documents the first Shakespeare layer that does not pass through a vector-field or matrix representation.

## 1. Literal histories first

A `ProcessWord` is an ordered tuple

\[
h=(X_{i_1},X_{i_2},\ldots,X_{i_n}).
\]

No commutativity, cancellation, semantic equality, or physical interpretation is assumed by the object itself. The literal history remains available even after a relational normal form is computed.

## 2. Oriented process relations

A `WordRewriteRule` records an explicit oriented relation

\[
u\longrightarrow v.
\]

`rewrite_once` searches a history from left to right for a contiguous occurrence of `u` and replaces it by `v`. If several rules match at the same location, caller order is the tie breaker.

This is intentionally weaker than declaring a global equality. An orientation is part of a presentation and may be useful for compression or normalization even when another presentation would orient the same semantic relation differently.

## 3. Certified normalization

`normalize_word` repeatedly applies the declared rules and returns a `RewriteResult` containing:

- the original literal history;
- the current/final normal form;
- every `RewriteStep`, including rule and position;
- whether normalization terminated;
- a reason: `normal_form`, `cycle`, or `max_steps`.

The library does not assume that a finite presentation has a terminating or confluent rewrite system. A cycle is therefore a result, not an exception to be hidden.

## 4. Why this layer is separate

The symbolic `ProcessSystem` backend represents a local generator as a derivation on an expression algebra. That is useful for process closure and relation discovery, but it is already a representation.

Ordered word rewriting sits earlier:

\[
\text{literal history}\to\text{declared process relations}\to\text{relational normal form}.
\]

Only after this layer need a caller choose a continuous, matrix, differential, or other semantic representation.

## 5. Compression interpretation

If a relation shortens a word,

\[
X_1X_2X_1X_2\longrightarrow Y,
\]

then the rewrite system performs a concrete history compression. `RewriteResult.depth_delta` reports the change in literal word depth, while the trace certifies how the compressed representation was obtained.

This is only one cost axis: a shorter history may require a more expensive dictionary or decoder. Shakespeare therefore keeps word rewriting separate from `PresentationCost` until a caller or future search layer supplies the relevant cost model.

## 6. Current boundary

The exact-word engine does not yet provide:

- parameterized/context-sensitive relations;
- critical-pair analysis or Knuth–Bendix completion;
- equality saturation;
- relation levels such as process, semantic, and task equivalence;
- automatic orientation from a presentation cost;
- task-sufficient history quotients.

Those are natural extensions of the same public layer. The immediate rule remains: preserve literal history, apply only explicit relations, and return a certificate whenever normalization changes the presentation.
