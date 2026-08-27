# Finite LE semantics workstream

Research-local implementation for [issue #144](https://github.com/mountain/process-geometry/issues/144).

The workstream closes one precise gap left by the carrier gate: it must
evaluate, not merely classify, a real single-exponential rational-rate
fragment under `N -> +infinity`.

The contract, public corpus, branch policy, budgets, and held-out commitment
were frozen before evaluator implementation.  The current source freeze:

- derives `q` from rational exponential rates;
- rewrites the source into `t = exp(-N/q) -> 0+`;
- returns exact finite Laurent/Taylor bands and residuals;
- computes `exp(2)`, `1/3`, and the public `q=6` control;
- emits conservative real-domain witnesses and typed failures;
- deterministically replays result, chart, branch, residual, costs, and C2
  obligation discharge;
- contains no generic `limit()` call in compiler or replay.

The same-information SymPy baseline computes the public limits using its
generic limit engine, but has no compiler certificate or replay credit.

Run:

```bash
python -m pytest -q
python run_corpus.py PUBLIC_CORPUS.json
python run_corpus.py HELD_OUT_CORPUS.json
python run_baselines.py
python verify_manifest.py
```

The evaluator source was remotely frozen before reveal. The committed held-out
then passed without grammar or scoring changes: it derived `q=3`, returned
exact `1/5`, retained `1/5 - t/6 + O(t**2)`, recorded cancellation jump 4, and
replayed successfully. `HELD_OUT_RESULT.json` records the compact result. This
is self-commit evidence, not independent-agent evidence.

`SOURCE_FREEZE_MANIFEST.sha256` preserves the pre-reveal manifest;
`MANIFEST.sha256` covers the post-reveal evidence bundle.

The workstream disposition is **EXPAND within the frozen finite LE task
family**. SymPy's same-information generic limit baseline also obtains all
values, so the gain is explicit chart/domain/residual semantics and replayable
C2 discharge, not raw computability or speed.

No general transseries, hyperseries, surreal, hyperiteration, or public solver
API is authorized.
