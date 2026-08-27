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
5. [`02-compact-space-redteam.md`](02-compact-space-redteam.md) — exact cycle
   quotient, circle cover semantics, period-two obstruction, and the frozen
   sphere gate;
6. [`phase_compact_contract.py`](phase_compact_contract.py) and
   [`compact_space_redteam.py`](compact_space_redteam.py) — machine-auditable
   compact-space red team.

Current finite results:

```text
raw centered finite law -> active response order 2 -> scale balance a=1/2
finite histories -> endpoint fibres -> exact concatenation pushforward
biased law -> typed centering-required refusal
continuum / heat-kernel lowering -> not yet authorized
integer lattice -> exact deck-fibre pushforward to finite cycles
even non-lazy cycle -> typed period-two obstruction
lazy compact law -> exact uniform stationary fixed point
circle/sphere -> time-stationary, not line scale-stable
```

The scale result is narrower than a central-limit theorem.  The endpoint result
is narrower than path equivalence.  Recurrence and heat-kernel continuation
remain unauthorized while the compact sphere action/stabilizer gate is open.

The compact-space red team in #162 now blocks a second conflation.  A line
Gaussian is scale-renormalized; a compact cycle/circle law can instead be
time-stationary.  The finite cycle result is exact, while the continuum circle
and sphere remain semantic gates rather than heat-kernel claims.

This task is the second independent representation family requested in
[#140](https://github.com/mountain/process-geometry/issues/140).  Draft
[#141](https://github.com/mountain/process-geometry/pull/141) remains an
explicit compiler dependency; no implementation from that draft is copied
while it remains unmerged.  The completed stochastic feedback-trap Sonnet is
an independent downstream Itô/first-passage calibration and is not duplicated
here.

No Experimental or Public API pressure follows from S0/S1.
