# Issue #142 held-out red-team disposition

## Result

**Disposition: NARROW.**

The carrier-decision artifact succeeds, but the full frozen task does not.
The compiler classifies finite syntax and correctly refuses symbolic height;
it does not compute the L1 semantic readout.  In addition, the committed
`k=7` control lies outside the pre-reveal red-team maximum of 6 and therefore
receives zero acceptance credit.  No hyperserial or surreal runtime necessity
was observed, but the stronger `ELIMINATE` disposition is not earned.
For the executable finite subset alone, the surreal-runtime disposition is
`ELIMINATE`; this subordinate result does not replace the overall `NARROW`.

## Evidence chronology

1. The red-team corpus, capability matrix, unrolling rules, scoring, and
   commitment were frozen before compiler tuning.
2. The pre-reveal payload commitment was published on draft PR #143.
3. The compiler was publicly frozen at commit
   `d52289952021f6bf6ee7518a7e79816ff2de3924`.
4. The exact payload and 256-bit nonce were then revealed.
5. Canonical JSON replay produced the committed digest exactly:
   `40103ae7cdfc5d32bf0917fe98b28c2f427ef6fde7b829535da7a4447376ecd3`.
6. Only the frozen compiler and the previously declared SymPy 1.14 baseline
   were executed.

## Held-out outcomes

| Case | Compiler result | Independent replay | Semantic baseline | Credit |
| --- | --- | --- | --- | --- |
| mixed finite nesting | C2, construction height 3 | pass | exact limit `exp(2)` | carrier decision passes; compiler semantic task does not |
| literal exp iterate, `k=7` | C2, construction height 7 | pass | exact finite limit `exp(exp(exp(exp(E))))` | out-of-budget extrapolation; zero acceptance credit |
| symbolic exp height | typed `unsupported` | pass | unavailable | no C2/C3/C4 positive credit |

The first two compiler certificates concern finite-DAG feature/height storage
and replay.  They do **not** claim to compute the semantic limits: all three
LE normal-form, branch/domain, and comparison obligations remain open.  The
limits were separately executed by SymPy.  This is evidence that these two
finite expressions need no larger runtime carrier, but it is not evidence that
the compiler completed their semantic tasks.

The pre-reveal contract froze `literal_fixed_iteration_maximum = 6`, while the
committed held-out payload selected `k=7`.  Because the commitment cannot be
rewritten after reveal, the row is preserved transparently as an extra
extrapolation probe.  Its successful C2 classification and SymPy limit are
reported, but neither contributes to acceptance or disposition scoring.

The symbolic-height case is the decisive negative control.  The compiler did
not replace `h` with a finite bound, returned no minimum carrier, emitted the
typed failure `symbolic-height-not-finite-unrolling`, and retained the open
`uniform-iteration-normal-form` obligation.

## Adversarial audit

All held-out certificates passed independent replay and the frozen firewall:

- no smaller passed carrier was overpromoted;
- the `k=7` result received zero symbolic-height credit;
- no embedding or existence theorem was counted as an algorithm;
- no certificate stored the source expression, held-out answer, or full trace;
- no certificate-compression claim was made;
- C3/C4 received no positive capability or necessity credit.

## Why the disposition is NARROW rather than ELIMINATE, EXPAND, or STOP

`ELIMINATE` would require all frozen executable workloads to lower within the
declared budgets and the task claims to be met at their stated scope.  The
out-of-budget `k=7` row and the compiler's missing semantic evaluator prevent
that stronger verdict.  `EXPAND` requires both a replayable C0--C2 obstruction
and an effective C3/C4 construction or workload advantage.  Neither exists.
`STOP` would require
answer leakage, hidden unrolling, embedding-only promotion, non-effective
trace certificates, or no software-visible distinction.  The tests find none:
the compiler makes the useful distinction between finite syntax and a genuine
symbolic-height request, then refuses the latter correctly.

The remaining theoretical question is narrower and still open: whether a
future effective hyperserial construction can discharge the symbolic-height
obligation, and whether that task can distinguish C3 from a surreal carrier
equipped with hyperserial structure.  That is a later gate, not evidence for a
surreal runtime in this one.

## Governance

- Mathematical Core: unchanged.
- Research Programme: eliminative evidence for economy; U1/U2/E pressure only.
- Engineering Architecture: supports a research-local least-capability
  decision and typed-refusal stage.
- Theory Map: unchanged.
- Experimental/Public API: none.
