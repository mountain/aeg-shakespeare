# AM weight compiler workstream

Research-local implementation for issue #146.

This workstream treats the completed AM power--weight algebra as the semantic
carrier. Finite coefficient windows, matrices, or jets may be generated only
after an observer is declared. The native AM frame is not identified with the
finite-LE `N/t` chart.

The contract, public corpus, budgets, baseline, scoring, and hidden commitment
freeze before compiler source. No general `series()` or `limit()` call is
allowed in compiler or replay.

No multivariable AM, higher arithmetic rank, transseries, hyperseries,
surreal, symbolic-height, Public API, Core, or Theory Map promotion is
authorized.

## Executable gate

The research-local package implements:

- exact native `power-weight` and `power-character` canonicalization;
- the product, `A`, `M`, PBW, and finite affine laws;
- exact coefficients in the finite group algebra `Q[exp(Q)]`;
- observer-directed `add`, `multiply`, `scale`, `shift`, `exp`, and `log1p`;
- typed `log-a` and `v-jordan` resonance witnesses;
- compact deterministic certificates and full semantic replay.

Run the frozen public gate with:

```console
python run_corpus.py
python -m pytest -q
```

The evaluator deliberately records dependency slices rather than completed
series windows. SymPy is reserved for the separately declared,
non-authoritative same-information baseline.
