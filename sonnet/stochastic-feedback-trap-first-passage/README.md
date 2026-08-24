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
