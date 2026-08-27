# Sonnet — Brownian scale and endpoint fibres

Research-local calibration for
[#158](https://github.com/mountain/process-geometry/issues/158), corrected by
the A/M/P method gate in
[#160](https://github.com/mountain/process-geometry/issues/160).

This Sonnet recalculates the entrance to Brownian motion from raw increment
histories.  It does not begin with the continuum process, a Gaussian density,
the heat equation, or a supplied diffusive exponent.

Read in order:

1. [`00-problem-frontier.md`](00-problem-frontier.md) — primitive histories,
   tasks, scale argument, held-outs, and claim ceiling;
2. [`phase0_contract.py`](phase0_contract.py) — frozen `PRE-AMP` discrete-control
   lanes;
3. [`brownian_native.py`](brownian_native.py) — exact discrete scale and
   endpoint-fibre controls;
4. [`01-amp-generator-chart-gate.md`](01-amp-generator-chart-gate.md) — the
   corrected A/M/P grammar, competing charts, and result boundary;
5. [`phase1_amp_contract.py`](phase1_amp_contract.py) and
   [`brownian_amp.py`](brownian_amp.py) — executable grammar audit and exact
   exponential-observer adapter;
6. the two research tests in [`tests/research`](../../tests/research/) —
   independent certificates and fail-closed method checks.

Current corrected boundary:

```text
PRE-AMP: centered finite law -> response order 2 -> scale balance a=1/2
PRE-AMP: finite histories -> endpoint fibres -> exact pushforward
AMP position chart -> typed obstruction at zero / negative states
AMP ensemble chart -> exact A shift, M scale, integer-P replicas
full A/M/P closure -> infinite-dimensional residual retained
recurrence / continuum / heat-kernel -> paused and unauthorized
```

The earlier scale and endpoint results remain valid controls, but they are not
AMP results: only a discrete additive step was active.  The corrected gate
shows that the positive position chart is not global for a symmetric process,
while the positive ensemble observer supports exact A/M and the integer
replica slice of P.  Noninteger P generally leaves the finite atom family, and
the observer still forgets paths.  S2 recurrence and S3 heat-kernel work remain
paused until one of those residuals is resolved for a frozen task.

This task is the second independent representation family requested in
[#140](https://github.com/mountain/process-geometry/issues/140).  Draft
[#141](https://github.com/mountain/process-geometry/pull/141) remains an
explicit compiler dependency; no implementation from that draft is copied
while it remains unmerged.  The completed stochastic feedback-trap Sonnet is
an independent downstream Itô/first-passage calibration and is not duplicated
here.

No Experimental or Public API pressure follows from this gate.
