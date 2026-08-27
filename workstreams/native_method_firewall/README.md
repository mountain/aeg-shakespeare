# Native-method firewall

Research-local executable method contract for issue #156.  This workstream
prevents a Process Geometry calculation from silently changing its ontology
when a familiar backend is convenient.

The firewall keeps four lanes distinct:

```text
native discovery   primitive histories, task, chart, fibres, native family
native evaluation  calculation in that declared language
certificate        exact or independent checks of a declared claim
baseline           conventional competing method and red team
```

Taylor/power series, ordinary polynomial algebra, matrix linearization,
Fourier/spectral methods, Koopman/Carleman lifting, generic CAS calls, and
black-box numerics are not prohibited.  They may appear freely in a declared
baseline, and may support certificates.  To enter a native lane they need a
`LoweringWitness` scoped to the exact task and lane.  The witness records the
source and target presentation, adequacy grade, preserved and forgotten
information, residual, decoder, certificate, and failure semantics.

## Solver plan

```text
Problem and task:
  Keep method semantics auditable while Process Geometry prototypes are run.
Primitive process / constraints:
  A caller-declared MethodContract; no universal Process carrier is assumed.
Mathematical Core relation:
  History -> task -> presentation -> retained fibre/residual -> decoder.

Chosen algorithm:
  Exact enum/type checks on an append-only in-memory trace.
Claim mode:
  Exact finite validation of the declared record, not proof of source honesty.
Failure semantics:
  Incomplete contract, unknown mechanism/lane/task, premature lowering,
  undeclared baseline, or evidence-lane mismatch all fail closed.
Cost:
  Multi-axis integer counts; scalarization is explicitly unauthorized.
Baseline:
  Caller-declared and task-scoped; never relabelled as native evidence.

Current software layer:
  Research workstream only.
Mathematical Core / Theory Map / Public API effect:
  Unchanged.
```

## Important boundary

This is a trace and contract checker, not a Python sandbox, theorem prover,
source-code classifier, solver, or universal calculus.  A dishonest caller can
mislabel an algorithm as `native-process`; correctness still requires
mathematical review, executable certificates, and independent baselines.  The
typed mechanism vocabulary closes accidental aliasing, not adversarial code
execution.

The Brownian scale/fibre Sonnet is the first intended downstream consumer.  It
will declare Gaussian, heat-kernel, Fourier, and PDE machinery as lowering or
baseline evidence rather than supplying them to native scale discovery.
