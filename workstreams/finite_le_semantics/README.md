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
python run_baselines.py
python verify_manifest.py
```

The held-out payload remains unrevealed until this evaluator source and
manifest are publicly committed.

No general transseries, hyperseries, surreal, hyperiteration, or public solver
API is authorized.
