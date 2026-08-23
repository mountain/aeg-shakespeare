# Documentation map

The documentation is organized as a mathematical/programming narrative rather than as a flat API reference.

**Theory:** `THEORY_MAP.md` is the living map of the larger Process Geometry research picture. It synthesizes the current foundation, marks theory/code maturity, and is explicitly expected to evolve as Sonnets and calibrations sharpen or contradict it.

**Governance:** `GOVERNANCE.md` defines the research-to-API lifecycle: Sonnet -> extraction candidate -> Experimental -> maturing -> Public API. Material Experimental/Public API changes must include a **Theory Impact** review locating the change in `THEORY_MAP.md`; the Theory Map informs API review without becoming a frozen software specification.

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
51. `API.md` — living semantic public/experimental API map: Process → Presentation → Discovery → Analysis, plus explicitly unstable Experimental probes.
52. `REFERENCES.md` — shared mathematical bibliography.
53. `RELEASE_CHECKLIST.md` — release gates.

A named classical problem should normally be read in `tests/classical/` or `tests/research/`, where the test itself is expected to be a complete, cited mathematical vignette.
