## Summary

<!-- What changes, and why? -->

## Change type

- [ ] Research / Sonnet only
- [ ] Theory Map / theory governance
- [ ] Engineering architecture
- [ ] Mechanical / compatibility-preserving
- [ ] Internal implementation
- [ ] Experimental API
- [ ] Public API
- [ ] Documentation / governance

## Mathematical Core Change

<!--
Required for substantial research, theory, mathematical documentation, or a
theory-bearing API change. Read docs/MATHEMATICAL_CORE.md before
docs/THEORY_MAP.md.

If unchanged, state:
"Mathematical Core Change: unchanged; this work adds local evidence without
changing the current objects, constructions, laws, or boundaries."

If changed, answer briefly:
1. Primitive data — what exists before the preferred representation?
2. Construction — what typed lift/quotient/transport/stop/completion/decoder changes?
3. Law — what equation, invariant, universal property, or obstruction is added or corrected?
4. Information contract — what is preserved, forgotten, and reconstructible?
5. Covariance/units — what frame or presentation changes are allowed?
6. Boundary — local/global, existence/uniqueness, degeneration, red team, and kill condition?
7. Evidence — proof, executable certificate, independent calibration, and baseline?
-->

## Engineering Architecture Change

<!--
Required for substantial research, solver, numerical, dependency, performance,
or theory-bearing API work. Read docs/MATHEMATICAL_CORE.md and then
docs/ENGINEERING_ARCHITECTURE.md in full.

If unchanged, state:
"Engineering Architecture Change: unchanged; the local solver plan follows the
current architecture and introduces no reusable technical decision."

If changed, answer briefly:
1. Solver stage — which problem-to-solver stage changes?
2. Mathematical task — which object/task does it serve?
3. Algorithm/backend — what is selected, rejected, or replaced?
4. Claim mode — exact, certified approximate, numerical, stochastic, or search-only?
5. Evidence — evaluator, certificate, error, and failure semantics?
6. State — units, lift/residual, decoder, and reconstruction boundary?
7. Feasibility — workload, baseline, budgets, measured cost, and scaling?
8. Software — dependency, CI, API, migration, and reproducibility effects?
9. Operation — support/refine/split/connect/replace/contradict/deprecate/unchanged?
-->

## Theory Map Change

<!--
Required when this PR materially changes a T1-T4 theory node or edge.
See docs/MATHEMATICAL_CORE.md, docs/ENGINEERING_ARCHITECTURE.md,
docs/THEORY_GOVERNANCE.md, docs/THEORY_RECORD_TEMPLATE.md, and
docs/65-effective-analysis-principle.md.

For local research that does not modify the stable map, this may be:
"Theory Map Change: none; this is T0/T1 exploration and does not modify the stable map."

For a material map change, answer briefly:
1. Node/edge — which theory node or arrow changes?
2. Maturity — old -> proposed T0/T1/T2/T3/T4?
3. Role — local / reusable / foundational?
4. Operation — support / refine / split / connect / contradict / merge / deprecate / unchanged?
5. Information contract — what is preserved and forgotten?
6. Controlled vocabulary — strongest term used (canonical/universal/forced/minimal/...) and its mathematical meaning?
7. Falsification — negative control, degeneration, adversarial case, or kill condition?
8. Software pressure — does this justify Experimental/Public API pressure, and why is software not ahead of theory?
9. Effective analysis — if analysis/computation/stability/efficiency is claimed, which gates apply and where are evaluator, certificates, units, error/failure semantics, baseline, and cost boundary recorded?
10. Mathematical Core effect — which objects, construction, law/obstruction,
    information contract, or boundary changes?
11. Engineering Architecture effect — if computational, which solver stage,
    algorithm/backend, evaluator, evidence, failure, dependency, or cost changes?

Mechanical PRs may write "Theory Map Change: not applicable."
-->

## Theory Impact

<!--
Required for any change that adds, renames, generalizes, promotes, or materially
changes an Experimental/Public API. See docs/MATHEMATICAL_CORE.md,
docs/ENGINEERING_ARCHITECTURE.md, docs/THEORY_MAP.md,
docs/THEORY_GOVERNANCE.md, and docs/GOVERNANCE.md.

For a purely mechanical change, this may be one sentence:
"Theory Impact: none; this preserves the existing semantic contract and does not
change its position in the Theory Map."

For a material API change, answer briefly:
1. Theory position — which node/arrow does this represent or test?
2. Maturity — T-status plus classical/concrete/calibrated/experimental/public evidence provenance?
3. Semantic claim — what meaning does the API commit to?
4. Non-claim — which nearby stronger meaning is not claimed?
5. Evidence — independent domains, certificates, red teams?
6. Map effect — support / refine / split / connect / contradict / merge / deprecate / unchanged?
7. Migration risk — what if the theory changes later?
8. Effective-analysis impact — if applicable, what are the symbolic/numerical mode, certificates, error/failure semantics, baseline, units, and cost boundary?
9. Mathematical Core effect — which object/construction/law/boundary does the
   API implement or pressure, and what remains unchanged?
10. Engineering Architecture effect — which algorithm/evaluator/evidence/
    failure/dependency/cost contract does the API commit to, if any?
-->

## Effective Analysis

<!--
Required when this PR claims a new analysis language, numerical method,
stability property, or computational advantage.  Otherwise write "not
applicable".

- Claim mode: exact-symbolic / certified-approximate / numerical / search-only / record-only
- Function/observable language and operators:
- Closure or controlled extension:
- Evaluator and certificates:
- Domain, units/ruler, tolerance/error, and failure semantics:
- Conventional or competing baseline:
- Workload and cost boundary, including compilation/storage/decoder cost:
- Lift/quotient/lowering compatibility:
-->

## Validation

<!-- Tests, certificates, executable calibrations, docs review, or why runtime tests are unnecessary. -->

## Boundaries / non-goals

<!-- Especially important when a name is close to a stronger concept in docs/THEORY_MAP.md. -->
