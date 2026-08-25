# Research cross-calibrations

Files in this directory are executable research essays, not declarations of theorem status.

Each substantial file must separate:

- implemented exact statements;
- classical calibration facts;
- Process Geometry interpretations;
- conjectures or universality questions.

It must also function as an independent knowledge entry: state the mathematical problem in recognizable external language, define project-local notation, expose useful classical and Process Geometry retrieval terms, and identify the stable entry point when a research line spans several files. A reader arriving directly from search should not need repository chronology to discover what question is being asked.

Bibliographic information must be sufficient for the classical mathematics and historical claims to be audited independently of the code. A cross-problem resemblance such as “both reductions have generic genus one” is an implemented comparison; a claim that the two systems share a universal process normal form is a separate research hypothesis unless proved.

A research vignette may be valuable as a red team, degeneration, comparison, or pedagogical anchor even when its Theory Map relation is `unchanged`.

If it claims a new analysis language, numerical method, stability property, or
computational advantage, it must identify the claim mode and audit symbolic
closure, numerical domain/error/failure semantics, baseline, units, cost, and
lift/quotient/lowering compatibility as applicable.  `Not applicable` is
acceptable when justified; `not measured` does not support a positive claim.

See:

- `docs/VIGNETTES.md` — problem-oriented retrieval index;
- `docs/VIGNETTE_CONTRACT.md` — standalone, executable, and retrieval completeness;
- `docs/65-effective-analysis-principle.md` — symbolic/numerical and cost audit for analysis-bearing claims;
- `docs/09-literate-programming-and-mathematical-lineage.md`;
- `docs/11-references-and-test-essays.md`;
- `docs/12-test-essay-template.py.txt`;
- `docs/REFERENCES.md`.
