# Classical calibrations

Files in this directory are executable mathematical essays.

Each substantial calibration must present a complete argument: a human-recognizable problem statement, primitive data, notation/prerequisites, classical lineage, Process Geometry reconstruction, precise calibration statement, proof map, boundary of the claim, and rigorous references. The executable assertions then certify the mathematical steps.

A calibration also serves as a durable knowledge entry. A reader arriving directly from search should be able to understand what problem is being studied without reconstructing repository chronology. Substantial vignettes should expose useful problem/classical/Process Geometry retrieval terms and identify a stable entry point when the argument spans several files.

If a calibration claims a process calculus, numerical reconstruction, stability,
or computational advantage, it must also state the claim mode, conventional
baseline, operator/closure contract, evaluator and certificates, units and
error/failure semantics, and total cost boundary.  Symbolic closure, numerical
stability, and efficiency are separate claims.

The named problem is never a package-level solver. A classical example is admitted here to test common Process Geometry abstractions, to provide a red team or degeneration, or because the problem is a useful pedagogical anchor. It does **not** need to promote a new theory node or public abstraction in order to be valuable.

For multi-file mathematical families, prefer one stable family-level guide over forcing every proof step into one oversized test. The first such complete guide is:

- `docs/vignettes/simple-pendulum.md` — physical problem, nondimensional bridge, P0–P13 executable dependency map, quotient-fiber/reconstruction boundary, evidence levels, and open obligations.

See:

- `docs/VIGNETTES.md` — problem-oriented retrieval index;
- `docs/VIGNETTE_CONTRACT.md` — standalone, executable, and retrieval completeness;
- `docs/65-effective-analysis-principle.md` — symbolic/numerical and cost audit for analysis-bearing claims;
- `docs/09-literate-programming-and-mathematical-lineage.md`;
- `docs/11-references-and-test-essays.md`;
- `docs/12-test-essay-template.py.txt`;
- `docs/REFERENCES.md`.
