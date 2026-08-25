# Documentation map

The documentation is organized as a mathematical/programming narrative rather than as a flat API reference.

**Mathematical core:** `MATHEMATICAL_CORE.md` is the required first entry for
substantial research and theory work. It records the current objects,
constructions, equations, information contracts, red-team separations, and
open boundaries, with the simple pendulum as the first end-to-end model.

**Engineering architecture:** `ENGINEERING_ARCHITECTURE.md` is the required
second entry. It turns concrete physical and mathematical problems into
auditable solver plans: problem/task contracts, presentations, algorithm and
backend choices, evaluators, certificates, error/failure semantics, units,
decoders, budgets, dependencies, baselines, and total cost. It also records the
current repository-wide technical decisions and their limits.

**Theory:** `THEORY_MAP.md` is the living index and maturity map of the larger
Process Geometry research picture. It is explicitly not a substitute for the
mathematical content in `MATHEMATICAL_CORE.md` and the detailed proof records.

**Theory governance:** `THEORY_GOVERNANCE.md` governs how mathematical claims
enter the Mathematical Core and move inside the Theory Map. It separates
epistemic maturity (`T0`–`T4`) from structural role (`local` / `reusable` /
`foundational`), requires mathematical content before map placement, treats
theory-map arrows as auditable information contracts, controls strong
vocabulary such as `canonical` and `universal`, requires kill conditions for
substantial claims, and makes conservative extension the default.
`THEORY_RECORD_TEMPLATE.md` provides the standard node/edge record format.

**Software governance:** `GOVERNANCE.md` defines the research-to-API lifecycle:
Sonnet -> extraction candidate -> Experimental -> maturing -> Public API.
Material work states its Mathematical Core and Engineering Architecture
relation; Experimental/Public API changes additionally include a **Theory
Impact** review locating the change in `THEORY_MAP.md`. Mathematical,
architecture, theory-map, and API promotion remain separate gates.

**Effective analysis:** `65-effective-analysis-principle.md` makes symbolic and
numerical calculability a cross-cutting success condition for analysis-bearing
presentations.  It separates semantic adequacy, symbolic closure, numerical
stability, certification, and computational economy; updates canonicalization,
lift-first, unit/ruler, objectification, and V5 review without claiming a
universal calculus.

**Knowledge artifacts:** `VIGNETTES.md` indexes standalone mathematical
vignettes, while `VIGNETTE_CONTRACT.md` defines their statement, evidence,
retrieval, and governance obligations.

## Architecture and implementation narrative

The numeric filename prefixes below are archival chronology markers, not unique
document identifiers or maturity levels. Several numbers occur more than once
because independent research lines were merged without rewriting history.
Existing filenames remain stable for citation; new documents must not introduce
additional prefix collisions.

1. `00-process-presentation-v0.1.md` — process-presentation nucleus.
2. `01-ordered-process-rewriting.md` — literal histories and explicit relations.
3. `02-task-signatures.md` — bounded task-continuation signatures as finite distinguishability certificates.
4. `03-history-geometry-huffman.md` — depth, boundary, and prefix representations.
5. `04-costed-presentation-search.md` — multi-axis presentation search.
6. `05-primitive-construction.md` — construction-history-preserving proposals.
7. `06-addition-multiplication-function-theory.md` — A/M means Addition/Multiplication; first concrete process function theory.
8. `07-classical-calibration-program.md` — classical problems as process-first calibrations.
9. `08-function-theory-genus-hierarchy.md` — genus hierarchy across reduced algebraic processes.
10. `09-literate-programming-and-mathematical-lineage.md` — source-writing discipline.
11. `10-release-0.0.1.md` — first research-preview release contract.
12. `11-references-and-test-essays.md` — rigorous citation and executable-essay policy.
13. `12-test-essay-template.py.txt` — template for substantial classical/research tests.
14. `13-abelian-history-periods.md` — holomorphic differentials, period-history interpretation, symmetric pendulum square lattice, and the Jacobian threshold.
15. `14-history-lift-and-period-cycles.md` — branch continuation, sheet monodromy, explicit lifted cycles, and the first directly integrated pendulum period.
16. `15-period-matrix-and-riemann-shape.md` — A/B cycle systems, normalized candidate period matrices, and the distinction between Riemann shape checks and topological certificates.
17. `16-lifted-cycle-intersection.md` — sampled surface intersection pairing, the role of sheet history, and the first measured symplectic form.
18. `17-real-branch-cycle-presentation.md` — ordered real branch data as a cycle grammar, exact construction-level symplectic pairing, and the first branch-generated genus-two period calibration.
19. `18-abel-jacobi-history-quotient.md` — A-normalized Abelian history increments, closed-history lattice generators, and the normalized period-lattice quotient.
20. `19-polynomial-discovery-layer.md` — bounded observer grammars, template-free polynomial first integrals, and exact observable-quotient elimination.
21. `20-observer-quotient-selection.md` — costed first-order quotient search and Pareto selection inside a declared observer family.
22. `21-structured-observer-proposals.md` — minimal structured pairing constructions, backend lowering, and Pendulum III observer generation.
23. `22-oscillator-additive-process-module.md` — finite additive process closure, basis-accident red team, and relation-before-spectrum discipline.
24. `23-oscillator-coefficient-extension.md` — explicit coefficient-language extension, refined relation factors, and one-dimensional kernel primitives before spectral semantics.
25. `24-oscillator-refinement-red-team.md` — two-frequency red team showing that finer coefficient splitting trades component count against relation order rather than yielding a universal winner.
26. `25-finite-process-families-and-characters.md` — stable finite-family API slice from Translation/Dilation/A-M, plus Galilean shear acceptance and the retained mass-residual boundary.
27. `26-finite-family-api-freeze-checklist.md` — explicit merge/freeze gates for the first finite-family/character/action public API slice.
28. `27-galilean-central-residual.md` — Galilean II/III: scalar-pullback obstruction, Hamiltonian central mass residual, and the affine energy-momentum shift without yet promoting a cocycle API.
29. `28-magnetic-translation-central-residual.md` — independent magnetic-translation red team: flux 2-cocycle, central magnetic bracket, commuting visible flows, and comparison with Galilean mass residuals.
30. `29-process-cocycle-api.md` — minimal shared public cocycle layer forced by Galilean mass and magnetic flux residuals, with finite composition primary and infinitesimal brackets retained as derived realizations.
31. `30-semantic-public-api-refactor.md` — Phase A.1 semantic namespace refactor, root contraction, compatibility bridge, and separation from later physical file movement.
32. `31-internal-namespace-migration.md` — Phase A.2 migration of repository tests off the legacy root bridge, with an AST-based hygiene gate.
33. `32-physical-finite-process-consolidation.md` — Phase B.1 physical relocation of finite family/character/action/cocycle implementation under `process/finite`, with old module paths reduced to compatibility shims.
34. `33-core-decomposition.md` — Phase B.2 split of the old mixed `core.py` into canonical history, local-process, and presentation-budget owners, with source dependency hygiene gates.
35. `34-release-0.0.2.md` — second research-preview release contract: semantic API consolidation, discovery expansion, and CPython 3.10–3.14 support.
36. `35-killer-calibrations-and-dominance-target.md` — first KdV/Kepler killer calibrations and the stronger presentation-complexity/integrability target.
37. `36-kdv-soliton-rewrite-confluence.md` — KdV pair phase transport as a parametric history rewrite, three-soliton critical-pair joinability, and a two-body-preserving nonconfluence red team.
38. `37-kdv-tau-rewrite-cross-presentation.md` — Hirota bilinear derivation of the pair factor and three-body coefficient, exact agreement with rewrite residuals, and an irreducible three-body cross-presentation red team.
39. `38-resistor-network-presentation-morphism.md` — non-KdV calibration: DtN task quotient, Y–Delta discovered from response equality, Schur-complement semantic confluence, and weak-observer red team.
40. `39-braid-markov-presentation-morphism.md` — topology calibration: braid/Markov moves, Burau/Alexander closure semantics, cross-dimension stabilization, and weak topological observer red team.
41. `40-presentation-morphism-api.md` — minimal public `PresentationMorphism` contract promoted after the KdV, resistor-network, and braid/Markov calibrations.
42. `42-process-geometry-from-distinguishability.md` — first-principles horizontal program: exact task quotients, observer-relative locality, topology, entropy/complexity, and the continuous extension toward differential structure, independent of Arithmetic Universality.
43. `43-myhill-nerode-and-the-topological-threshold.md` — exact discrete anchor: Myhill–Nerode gives distinguishability -> minimal presentation before topology, while the topological threshold requires local refinement and process continuity and adds robustness, boundary, compactness, covering/homotopy, and topological entropy.
44. `44-objectification-semantic-compression-and-rank-lowering.md` — vertical Process Geometry program: semantic compression -> objectification -> new primitives -> free higher-rank composition, constrained by compositional rank lowering back to grounded lower-rank semantics; separates ontology growth from the horizontal distinguishability geometry.
45. `45-lineage-objectification-and-analytic-closure.md` — lineage/red-team map against operads, Baez–Dolan slice constructions, polygraphs, definitional extension, abstract interpretation, and sheaves; identifies AEG as a model organism that couples rank raising to a native analysis of variation, and proposes semantic/topological/analytic closure across ranks.
46. `46-release-0.0.3.md` — first release contract under the `process-geometry` distribution identity; keeps `aeg_shakespeare` as a temporary import namespace while retargeting GitHub/PyPI metadata and publishing.
47. `47-release-0.0.4.md` — makes `process_geometry` the canonical Python namespace, reduces `aeg_shakespeare` to an identity-preserving compatibility alias, and establishes one-way namespace ownership and release hygiene.
48. `48-foundation-naming-audit.md` — maps the current program vocabulary to the `42–45` foundation; reserves task quotient, jet, objectification, rank, and lowering for their stronger meanings and introduces compatibility-safe canonical names where current code collides with them.
49. `49-theory-implementation-structural-alignment.md` — audits H0–H4 and V0–V5 against executable code, distinguishes implemented nodes from calibrated shadows and missing semantics, and selects exact finite task quotienting as the first substantive theory-to-code alignment target.
50. `50-aeg-translation-objectification-rank-lowering.md` — first complete research-local V1→V4 calibration: signed unit histories compress by net translation semantics, become reusable Addition/translation primitives, freely compose at a new semantic rank, and lower compositionally with relation soundness plus a continuation-congruence red team.
51. `51-aeg-addition-multiplication-rank-transition.md` — second arithmetic rank transition: Multiplication objectifies a uniform repeated-Addition endomorphism on Translation objects, pure multiplicative words lower to Translation endomorphisms, mixed A/M words lower to the positive affine monoid, and `D_k T_a = T_(ka) D_k` aligns exactly with the existing finite/infinitesimal A/M calculus without yet claiming analytic closure.
52. `52-canonical-completion-hypothesis.md` — first governed T1 theory record: a candidate marked-carrier -> global-completion line with competing hypotheses, information-loss boundaries, kill conditions, and explicit prohibition on premature API promotion.
53. `53-process-volume-frontier-coarea-hypothesis.md` — governed T1 theory edge: the candidate coarea/frontier connection between H3 and H4 (discrete volume-frontier identity vs. classical action-period identity), without identifying energy with computational complexity.
54. `54-pendulum-elliptic-group-rank-lowering.md` — research note: the elliptic group law of the pendulum carrier as a second, geometric calibration of V3–V4; Euler's addition theorem certified exactly as compositional rank lowering of the flow-translation schema, with red teams and no map/API promotion.
55. `55-pendulum-lifted-clock-global-quotient.md` — research note: realizes the lifted-clock/geometric-phase chain of docs/54 globally on the lemniscatic leaf — sigma symmetry with tau = i, the Jacobi-derived primitive square lattice `omega_A = sqrt(2) varpi`, the unramified mark cover with sheet transport through q_x = 0, the exact clock-chain kernels, and the correction of the merged P10 period naming.
56. `API.md` — living semantic public/experimental API map: Process → Presentation → Discovery → Analysis, plus explicitly unstable Experimental probes.
57. `REFERENCES.md` — shared mathematical bibliography.
58. `RELEASE_CHECKLIST.md` — release gates.
59. `THEORY_GOVERNANCE.md` — conservative governance for Theory Map nodes and edges: T0–T4 promotion, controlled vocabulary, falsification, conservative extension, and theory/software asymmetry.
60. `THEORY_RECORD_TEMPLATE.md` — auditable node/edge record and promotion checklist for material Theory Map changes.
61. `65-effective-analysis-principle.md` — governing Effective Analysis
Principle and claim-relative engineering gates for symbolic/numerical
calculation, certificates, units, errors, costs, and cross-rank transport.

Required unnumbered synthesis:

- `MATHEMATICAL_CORE.md` — mathematical objects, typed constructions, exact
  laws, information-loss boundaries, red teams, and the pendulum
  lift--unit--domain--quotient--decoder model.
- `ENGINEERING_ARCHITECTURE.md` — problem-to-solver pipeline, algorithm
  selection matrix, current software-layer responsibilities, technical
  decisions, solver-plan contract, and architecture governance.

## Additional decision, calibration, and knowledge records

These records are first-class parts of the audit trail even though they are not
steps in the architecture narrative above:

- `27-finite-family-calibration-map.md` — family-level calibration ownership
  and the evidence behind the first finite-family API slice;
- `28-do-not-extend-this-api-yet.md` — explicit freeze record preserving the
  unresolved central-residual boundary;
- `35-canonical-observer-vertical-slice.md` — local executable
  canonicalization/connection/decomposition evidence;
- `36-classical-reexpression-audit.md` — complete second-pass audit of all
  `tests/classical` essays against the Mathematical Core, Engineering
  Architecture, and end-to-end pendulum calibration, with evidence classes,
  information boundaries, and staged recalibration order;
- `37-canonical-observer-claim-ledger.md` — claim-by-claim evidence and
  non-claim ledger for the canonical-observer programme;
- `38-canonicalization-mainline.md` — qualified local canonicalization
  mainline and its proof obligations;
- `39-canonicalization-mechanism-closure.md` — mechanism-closure audit and
  remaining genericity boundary;
- `41-hard-particle-next-event-redteam.md` — independent next-event argmin
  obstruction and red team;
- `VIGNETTES.md` — retrieval index for standalone mathematical knowledge
  units;
- `VIGNETTE_CONTRACT.md` — durable completeness and evidence contract for
  vignettes.

A named classical problem should normally be read in `tests/classical/` or
`tests/research/`, where the test itself is expected to be a complete, cited
mathematical vignette.

## Fast-moving research records and governing syntheses

The numbered architecture list above predates several fast-moving research
calibrations. These are indexed without renumbering that stable list:

- `53-process-volume-frontier-coarea-hypothesis.md` — process-volume/coarea candidate;
- `54-pendulum-canonical-history-cost.md` — marked pendulum clock as task-history edge measure;
- `55-cross-problem-canonical-history-correspondence.md` — heterogeneous audit with correction banner;
- `56-am-universal-history-recalibration.md` — lift-first universal-history correction;
- `57-dimensional-resource-bundle-calibrations.md` — dimensional resources and covariant Bellman;
- `58-noether-canonicalization-and-history-payloads.md` — Noether, curvature, magnetic and Berry probes;
- `59-noether-blind-discovery-prototype.md` — classical AD control baseline;
- `60-optical-am-process-symmetry-audit.md` — exact supported A/M symmetry slice;
- `61-pendulum-section-reparameterization-redteam.md` — equal-clock stopping experiment.
- `62-task-covariant-complexity-coarea.md` — moving-unit action--period identity,
  exact Bellman/frontier volume, task-visible holonomy memory, and a global
  integrability obstruction.
- `63-thermodynamic-objectification-and-partition-towers.md` — finite
  thermodynamic pushforward and its same-scale flattening theorem, unit-cell
  carry law, plethystic assembly boundary, and twisted finite-cycle red team.
- `64-first-principles-and-api-boundary-audit.md` — synthesis of the two-axis
  foundation, the emerging task-covariant evaluation transversal, current
  theory gaps, and the conservative Experimental ownership refactor.
- `65-effective-analysis-principle.md` — refinement of the mother picture to
  two axes governed by a cross-cutting effective-analysis constraint, together
  with research, vignette, promotion, and release standards.

Open Sonnet research is indexed by its own README and phase notes under
`sonnet/`.
