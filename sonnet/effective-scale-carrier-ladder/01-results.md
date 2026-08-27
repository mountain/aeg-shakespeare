# Result: carrier capability gate

## Disposition

**NARROW.**  The study produced a useful, replayable carrier-decision and
typed-refusal layer, but it did not establish an effective hyperserial or
surreal runtime advantage.  The finite executable subset eliminates a surreal
runtime; the overall gate remains narrow because symbolic-height construction,
C3/C4 separation, and semantic LE evaluation are unresolved.

This is a research-local T1 result.  It changes neither the Mathematical Core
nor the Public API.

## The main correction: capability geometry, not a linear tower

The provisional chain `C0 < C1 < C2 < C3 < C4` is mathematically misleading.
A carrier must instead be described by at least five coordinates:

```text
ambient universe
available operations and composition domains
finite or ordinal construction height
normalization principle
effective encoding, comparison, truncation, and replay
```

In particular:

- finite Hahn support is a generalized-polynomial presentation, not a field;
  inversion can force infinite well-based support;
- an LE-transseries value has finite construction rank, but need not have
  finite support or a computed normal form;
- `No` as an ordered exponential field does not automatically provide named
  hyperserial operations or total composition;
- `No` equipped with hyperserial structure and a compatible hyperseries field
  can overlap on the same hyperiteration task;
- an embedding into a larger universe supplies no algorithmic credit.

The audited local vocabulary is therefore `C0`, `C1f`, `C1h`, `C2`,
`C3(alpha)`, `C4e`, and `C4h(alpha)`, connected by typed embeddings and
operation extensions rather than one asserted strict order.

## Mathematical result and obstruction

For a closed, well-typed finite expression DAG over certified finite-stage LE
inputs, field operations and finitely many `exp`/`log` nodes remain in some
finite LE stage.  Every fixed finite iterate follows by structural induction.
This is a membership/stage certificate; it is not a generic LE normalizer,
analytic-germ evaluator, comparison algorithm, or proof of semantic
minimality.

Replacing a fixed iterate by a symbolic height changes the grammar.  A
positive eventually increasing solution of

\[
F(x+1)=\exp(F(x))
\]

is transexponential and cannot be represented by any one bounded-height
unrolling.  This gives genuine pressure beyond the implemented C2 syntax.
The equation alone does not select a unique solution, branch, domain, or
normalization, and it does not distinguish a hyperseries carrier from `No`
carrying compatible hyperserial operations.

The full proof and primary-source boundary audit is in
[`MATHEMATICS_AND_LITERATURE_AUDIT.md`](../../workstreams/carrier_ladder/math/MATHEMATICS_AND_LITERATURE_AUDIT.md).

## Software artifact

The frozen compiler implements:

- a deterministic, JSON-serializable expression IR;
- exact feature and finite construction-height extraction;
- executable `C0`, `C1f`, and syntax-level `C2` capability declarations;
- a `CarrierDecisionCertificate` with separate lowering, upgrade, and task
  obligations;
- compilation, certificate, replay, residual, and decoder cost axes;
- independent recomputation of the minimum carrier in the frozen matrix;
- typed refusal for symbolic height, Abel tasks, C3, and C4;
- fail-closed checks that keep C2 normal form, branch/domain, and comparison
  obligations open.

Its eliminability claim is deliberately only
`surreal-runtime-eliminable-for-frozen-syntax-decision`.  It does not claim
that the compiler evaluates the source expression or constructs a transseries
normal form.

The implementation, contract, public corpus, and 16 tests are in
[`workstreams/carrier_ladder/compiler/`](../../workstreams/carrier_ladder/compiler/).

## Commit--reveal result

The red team froze its firewall and a SHA-256 commitment before the compiler
freeze.  After compiler commit
`d52289952021f6bf6ee7518a7e79816ff2de3924`, the exact payload and 256-bit
nonce were revealed.  Canonical JSON reproduced

```text
40103ae7cdfc5d32bf0917fe98b28c2f427ef6fde7b829535da7a4447376ecd3
```

The result must retain two negative facts:

1. the L1 compiler certificate classified finite syntax but did not compute
   the requested exact limit; the value `exp(2)` came from the independent
   SymPy baseline;
2. the committed fixed-height control used `k=7`, outside the pre-reveal
   maximum of 6, so it is an extrapolation probe with zero acceptance credit.

The symbolic-height case correctly refused fixed unrolling.  No answer
leakage, carrier overpromotion, embedding-as-algorithm substitution, or full
trace certificate passed the firewall.  The compiler suite has 16 tests, the
red-team suite has 11, and a default-CI bridge replays all 27.

The reveal, result, report, and manifests are in
[`workstreams/carrier_ladder/redteam/`](../../workstreams/carrier_ladder/redteam/).

## Position in Process Geometry

The result supports the task-relative presentation principle and corrects a
tempting ambient-space interpretation:

> A universal ambient universe does not by itself make the observed task
> effective.  What matters is the local presentation exposed to a bounded
> observer, the operations available in that presentation, and the finite
> shadow that can be decoded and replayed.

This is compatible with the ensemble/fibration intuition: a finite observer
receives a task-covariant chart rather than the entire ensemble.  But the
experiment does not yet geometrize surreal arithmetic, replace manifolds, or
upgrade analysis.  It isolates the missing construction that such a theory
would have to make effective.

## Next gate

Do not implement a general surreal number runtime next.  The smallest
discriminating continuation is an effective, normalized hyperiteration
fragment with:

- one declared symbolic/ordinal height operation;
- explicit domain, branch, existence, and normalization data;
- a bounded finite-shadow evaluator and independent replay;
- a C2 obstruction witness;
- comparison against a smaller hyperseries implementation and a classical
  real-analytic tetration baseline;
- a task whose observer was not chosen merely to force Conway simplicity.

Only a measured construction or task advantage at this gate would justify
renewed C4 runtime work.  Until then, surreal numbers remain a strong semantic
envelope and source of structural hypotheses, not an earned software
dependency.

## Governance

```text
Mathematical Core: unchanged
Research Programme: U1/U2/E pressure; no universality promotion
Engineering Architecture: research-local carrier decision/refusal stage
Theory Map: no stable node or arrow promoted
Experimental/Public API: none
```
