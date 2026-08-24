# Sonnet — Stochastic Feedback-Trap First Passage

This Sonnet is the physical continuation of the closed affine deterministic
moving-observer phase in PRs #86–87.  It asks whether task-relative
canonicalization, presentation morphisms, and Bellman costs remain covariant
for a noisy feedback-trap process.

The primary model is the dimensionless co-moving SDE

\[
du=(u^2-2)\,d\theta+\sqrt{2\varepsilon}\,dB_\theta,
\qquad
\theta=Vt/L,
\qquad
\varepsilon=D/(LV).
\]

The first nonlinear presentation pressure is `w=u+u^3`.  In the stochastic
system it is not enough to transport the deterministic vector field: Ito's
second-order correction must survive.  Phase 0 freezes that calculus and the
task/oracle boundary before any optimal policy is computed.

## Planned gates

```text
P0  units + SDE/task contract + Ito covariance firewall
P1  bounded A/M presentation census + exact monotonicity certificates
P2  epsilon=0 non-affine deterministic control
P3  stochastic generator / backward-equation covariance
P4  independent first-passage solver and Monte Carlo red team
P5  resettable stochastic Bellman value/policy covariance
P6  blind task-morphism discovery or bounded negative certificate
```

Every gate may close negatively.  In particular, failure of a bounded A/M
grammar to discover the nonlinear morphism is not repaired by supplying
`w=u+u^3` as an answer label.

Phase 1 is implemented in `phase1_presentation_census.py` and
`01-phase1-presentation-census.md`.  It retains literal tree counts before exact
polynomial quotienting and requires exact strict-monotonicity certificates on
the full task interval.

Its exact result is `604 literal -> 60 semantic -> 16 strictly increasing`, and
all 16 survivors are affine.  Hence the frozen depth-two grammar contains no
admissible nonlinear presentation and does not contain the held-out `u+u^3`.
This negative certificate must remain visible when depth three is opened.

`02-phase1b-depth-three-contract.md` freezes that enlargement before execution.
The exact cumulative literal count is 365,424; a complete semantic closure over
the 60 depth-two values avoids materializing redundant syntax while preserving
every reachable polynomial.

Execution is recorded in `03-phase1b-depth-three-results.md`: 1,519 semantic
polynomials yield 242 strictly increasing presentations, including 155
nonlinear ones.  The held-out control enters, but is one of 155.  Depth three
therefore solves coverage and fails uniqueness; stopped-process task semantics,
not answer-shaped ranking, must supply the next quotient.

`04-phase2-task-quotient-contract.md` freezes that quotient before execution.
It tests all 242 monotone charts, retains generator, endpoints and labels,
initial point, and clock, and requires omission of the Itô correction to split
exactly into affine passes and nonlinear failures. A passing full transport
would establish a canonical task class, not a preferred polynomial spelling.

Execution in `05-phase2-task-quotient-results.md` gives `242/242` exact full
Itô transports and one task-equivalence class. The no-Itô-correction red team
splits exactly as predicted: 87 affine passes and 155 nonlinear failures. The
next gate must test numerical first-passage observables independently; symbolic
generator covariance alone is not a Bellman or solver certificate.

`06-phase3-first-passage-contract.md` now freezes that numerical gate before
execution: a backward BVP and independently evolved Monte Carlo paths compare
the source chart with two nonlinear charts, while a uniform target-coordinate
mesh is retained as an expected coordinate-artifact red team.

Execution in `07-phase3-first-passage-results.md` finds a common refined BVP
value near `0.572194`: the two nonlinear 401-node values differ from the source
by only `3.51e-6` and `1.14e-6`. Independent Euler-Maruyama estimates agree at
their declared sampling/time-step precision. Uniform target-coordinate meshes
produce the expected finite-resolution split, so node count is not promoted to
a coordinate-free physical cost.
