# Repository guidance for agents

Before any substantive work in this repository, read each of these files in
full and in order:

1. `docs/MATHEMATICAL_CORE.md` — objects, constructions, laws, information
   loss, and present mathematical boundaries;
2. `docs/RESEARCH_STATUS.md` — dated mainline evidence ledger: exact results,
   active research boundaries, downstream computation, and unearned claims;
3. `docs/ENGINEERING_ARCHITECTURE.md` — problem contracts, presentation and
   algorithm choice, evaluators, certificates, errors, costs, and technical
   decisions for feasible computation;
4. `docs/THEORY_MAP.md` — location, dependency, and maturity of those claims;
5. `docs/THEORY_GOVERNANCE.md` and `docs/GOVERNANCE.md` — theory and software
   promotion rules;
6. the relevant vignette, research note, executable proof essay, and code owner.

`RESEARCH_STATUS.md` is a navigation layer, not mathematical authority.  Use
it to locate the current evidence owner and explicit nonclaim, then verify the
detailed theorem, phase result, or executable certificate.  Do not confuse
absence of framework-wide theory promotion with absence of theorem-level local
results.

Do not begin from the Theory Map alone. It is a compact index and governance
aid, not the carrier of the full mathematics or an executable architecture. A
new concept must first be expressed as primitive data, task semantics, a typed
construction, a law or obstruction, an information contract, a scope/boundary
statement, and evidence. A solver must additionally declare its representation,
algorithm, evaluator, certificate, error/failure semantics, units, decoder,
baseline, and resource budget.

For work under `sonnet/`, also follow `sonnet/AGENTS.md`.

Do not infer a universal Process Geometry abstraction from one model organism,
and do not turn an implemented name into evidence for a mathematical claim.
Preserve the explicit distinctions and open boundaries in the mathematical
core unless the work supplies a proof or red-team-supported correction.
