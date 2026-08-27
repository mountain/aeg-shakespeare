# Sonnet — Brownian scale and endpoint fibres

Research-local calibration for
[#158](https://github.com/mountain/process-geometry/issues/158).

This Sonnet recalculates the entrance to Brownian motion from raw increment
histories.  It does not begin with the continuum process, a Gaussian density,
the heat equation, or a supplied diffusive exponent.

Read in order:

1. [`00-problem-frontier.md`](00-problem-frontier.md) — primitive histories,
   tasks, scale argument, held-outs, and claim ceiling;
2. [`phase0_contract.py`](phase0_contract.py) — frozen executable method lanes;
3. [`brownian_native.py`](brownian_native.py) — exact scale and endpoint-fibre
   calculations;
4. [`test_brownian_scale_fibre_phase0.py`](../../tests/research/test_brownian_scale_fibre_phase0.py)
   — independent certificates and source firewall.

Current S0/S1 result:

```text
raw centered finite law -> active response order 2 -> scale balance a=1/2
finite histories -> endpoint fibres -> exact concatenation pushforward
biased law -> typed centering-required refusal
continuum / heat-kernel lowering -> not yet authorized
```

The scale result is narrower than a central-limit theorem.  The endpoint result
is narrower than path equivalence.  S2 must next separate lattice point return,
continuum neighbourhood recurrence, and singleton hitting before S3 authorizes
a Brownian/heat-kernel lowering.

This task is the second independent representation family requested in
[#140](https://github.com/mountain/process-geometry/issues/140).  Draft
[#141](https://github.com/mountain/process-geometry/pull/141) remains an
explicit compiler dependency; no implementation from that draft is copied
while it remains unmerged.  The completed stochastic feedback-trap Sonnet is
an independent downstream Itô/first-passage calibration and is not duplicated
here.

No Experimental or Public API pressure follows from S0/S1.
