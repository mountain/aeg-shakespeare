# Effective scale-carrier compiler — Workstream B

**Issue:** [#142](https://github.com/mountain/process-geometry/issues/142)  
**Status:** research-local compiler evidence; C0--C2 only  
**Public API:** none

## Outcome

This prototype implements the smallest software-visible artifact authorized by
the issue contract:

- a backend-neutral, JSON-serializable `ScaleExpr` IR;
- exact finite construction-height and feature extraction;
- a frozen C0--C2 capability matrix;
- deterministic `CarrierDecisionCertificate` records;
- lowering, upgrade, resource, residual, and decoder ledgers;
- typed refusal for symbolic-height iteration, Abel/tetration assumptions,
  and all C3/C4 runtime requests;
- independent certificate replay;
- public controls plus one public finite-height sanity case.

The result does **not** implement a Hahn field, LE-transseries normalizer,
hyperseries, or surreal arithmetic. C1 means only explicit finite rational
monomial support. C2 means only a finite `exp`/`log` syntax DAG whose
construction height can be replayed by induction.

## Carrier decisions

| Workload | Result | Evidence |
| --- | --- | --- |
| L0 Bessel local polynomial germ | C0 | only rational finite polynomial operations occur |
| finite generalized polynomial | C1f | support and rational exponents are explicitly finite; no Hahn field |
| finite nested `exp`/`log` | C2 | exact node witnesses and finite construction height |
| symbolic-height `exp^h(x)` | unsupported | no fixed unrolling is admitted as a uniform law |
| Abel equation | unsupported | existence, branch, normalization, uniqueness, and effectiveness remain obligations |
| explicit C3/C4 request | unsupported | no construction/comparison/replay backend exists |

Every C0--C2 positive result carries the eliminability statement
`surreal-runtime-eliminable-for-frozen-syntax-decision`. This means only that
syntax membership, feature/height inference, carrier choice, and certificate
replay use no surreal runtime. It is not semantic expression evaluation,
normal-form lowering, or a theorem that the source has a general LE normal
form. C1h (a genuine Hahn-field level) remains mathematics-only and is not
represented as executable capability.

## Meaning of “minimum”

`minimum_declared_carrier` is the least executable member of the **frozen
syntax-directed capability matrix** containing every witnessed feature. It is
not minimal across all fields, simplification identities, coordinate systems,
or task-specific semantic quotients. The certificate repeats this claim scope
so consumers cannot silently strengthen it.

## Evidence firewall and public sanity case

`FROZEN_CONTRACT.json` fixes the grammar, capability order, budgets, replay
rules, and claim ceiling. `FROZEN_CORPUS.json` contains public positive and
negative controls. `PUBLIC_SANITY_IDENTITY.json` identifies the exact bytes of
`PUBLIC_SANITY_CASE.json`; this is explicitly public calibration data and
receives no held-out discovery credit. The strict held-out remains solely in
the separately frozen red-team workstream.

## Run

```bash
python -m pytest
python run_corpus.py FROZEN_CORPUS.json
python run_corpus.py PUBLIC_SANITY_CASE.json
python verify_manifest.py
```

The package has no runtime dependency outside the Python standard library.

## Governance disposition

- **Mathematical Core:** unchanged.
- **Research Programme:** U1/U2/E pressure only; no universality result.
- **Engineering Architecture:** research-local carrier decision and replay
  stage, with separate compilation/certificate/replay/residual/decoder costs.
- **Theory Map:** unchanged; no stable carrier-ladder node.
- **Public API:** no pressure.
