# Dimensionful moving-observer Bellman calibration

**Status:** T0 end-to-end executable calibration; research-local.

## Physical process and units

Restore the dimensions suppressed by the polynomial control:

\[
\dot x=V\left[\left(\frac{x-Vt}{L}\right)^2-1\right],
\qquad [x]=[L],\quad [V]=L/T.
\]

The moving canonical coordinate and its nonlinear A/M re-presentation are

\[
u=\frac{x-Vt}{L},\qquad w=u+u^3.
\]

They obey

\[
\dot u=\frac VL(u^2-2),
\qquad
\dot w=(1+3u^2)\dot u.
\]

Thus the physical clock necessarily carries the scale `L/V`:

\[
dt=\frac LV\frac{-du}{2-u^2}
   =\frac{dw}{\dot w}.
\]

The finite task runs from the marked moving section `x=Vt+L` to
`x=Vt-L`, equivalently `u=1` to `u=-1`.

## Pre-registered prediction

Five equal-clock first-hit sections are constructed in `u`, transported to
`w`, and timed independently in both charts.  A four-class alphabetic Bellman
recursion uses the root-to-section physical time as its additive query cost.

The prediction is:

1. equal physical-clock sections give the same section clocks, Bellman value,
   and policy in `u` and `w`;
2. doubling `L/V` doubles the value but leaves policy unchanged; and
3. equal-`u` and equal-`w` grids select different physical events and may change
   both value and policy.

## Result

All three predictions pass.  Independent `u` and `w` clock integrals and their
optimized values agree below `1e-45`.  Doubling `L` at fixed `V` doubles the
Bellman value.  Under equal coordinate spacing, the value discrepancy exceeds
`0.05` seconds for the declared `L=3.5`, `V=1.4`, and the optimal alphabetic
tree changes from a balanced first cut at `2` to a left-first cut at `1`.

## Interpretation

The invariant resource is the additive lifted clock `dt`, not coefficient-jet
variation and not observer-coordinate distance.  Canonicalization removes
explicit presentation variation; the task quotient identifies gauge-related
lifts; Bellman optimization is meaningful only after its edge costs are pulled
back from the same physical clock cocycle.

This is the moving-observer analogue of the pendulum equal-clock versus
equal-coordinate red team.  It supports

```text
lift first -> canonical gauge class -> physical stopping sections
           -> additive clock cocycle -> Bellman optimization.
```

## Boundary

The model is one-dimensional, monotone, resettable, and finite.  The nonlinear
chart is supplied as a post-hoc covariance pressure rather than discovered by
the bounded affine morphism grammar.  No holonomy, stochastic control,
continuous Bellman equation, or universal optimality theorem is claimed.

## Physical realization

The dimensionful equation is the deterministic overdamped limit of a particle
in a translating nonlinear potential.  With drag coefficient `gamma`, set

\[
U(x,t)=-\gamma VL\left(\frac{u^3}{3}-u\right),
\qquad u=\frac{x-Vt}{L}.
\]

Then

\[
\gamma\dot x=-\partial_xU
=\gamma V(u^2-1).
\]

The cubic potential is not globally confining, so this equation should be read
either as a finite-window force law on `u in [-1,1]` with stabilizing tails, or
as a local normal form.  Both interpretations are experimentally meaningful.
Translated optical traps have long been used to drive and track colloidal
particles [Wang-Sevick-et-al-2002].  Feedback traps can implement explicitly
time-dependent virtual potentials [Jun-Gavrilov-Bechhoefer-2014], and nonlinear
feedback-generated effective potentials have been experimentally verified for
levitated nanoparticles [Kremer-et-al-2024].  Rotating optical-tweezer arrays
also provide a direct precedent for passing to a co-moving frame in which an
overdamped particle sees a stationary tilted potential
[Evstigneev-et-al-2008].

Thus no known naturally occurring device is claimed to obey the polynomial
globally and exactly.  The stronger defensible statement is that the declared
finite deterministic process can be synthesized in a feedback optical trap,
while its quadratic drift is a standard local saddle-node/fold form.  Noisy
parameter sweeps through saddle-node bifurcations are used for escape and
switching models in micro/nanomechanical systems [Miller-Shaw-2012], and
scan-rate-dependent saddle-node delay has been observed in nickel
electrodissolution [Koper-Aguda-1996].

## Physical meaning of canonicalization

The laboratory vector field depends on `x-Vt` and therefore admits the joint
space-time translation

\[
(t,x)\mapsto(t+\Delta t,x+V\Delta t),
\qquad K=\partial_t+V\partial_x.
\]

The moving observer `u=(x-Vt)/L` is the co-moving frame that makes this symmetry
explicit.  Its autonomous equation is a reduction by the travelling structure,
not merely a convenient substitution.  This explains the earlier static
observer no-go: a state-only frozen A/M action cannot expose a generator mixing
clock and state.

The vertex chart `u` and root-pair chart `y=(u+1)/2` also have a concrete
experimental meaning.  They are center/scale calibration and two-marker
calibration of the same apparatus.  Their task-preserving morphism identifies
them as one physical presentation class; it does not force the laboratory to
prefer one sensor convention.

The Bellman task can be implemented as a resettable first-passage measurement:
prepare the particle at a common section, wait to a selected moving detector
section, observe which latent class remains possible, reset, and repeat.  The
latent classes may represent particle types, drag coefficients, external-force
hypotheses, or molecular states.  Position-dependent feedback transport and
force-control protocols already exist in optical-trap experiments
[Lopez-et-al-2008, Dieterich-et-al-2016].  The calibration's practical warning
is that a nonlinear sensor encoding must not turn equal display-coordinate
spacing into Bellman edge cost.  Edge cost must be pulled back from elapsed
physical time, or from another explicitly declared additive resource cocycle.

## Symmetry and Noether boundary

The co-moving symmetry is presently an equivariance/reduction result, not a
Noether energy theorem.  The system is overdamped and externally driven; the
moving apparatus performs work and the bath dissipates it.  A Noether charge
would require an enlarged action-level model including the drive and bath, or a
separate stochastic-thermodynamic boundary construction.  The current result
must not be described as conservation of energy or momentum.

A more realistic particle follows the Langevin equation

\[
\gamma\,dx_t=-\partial_xU(x_t,t)\,dt
 +\sqrt{2\gamma k_BT}\,dW_t.
\]

The deterministic Bellman test therefore calibrates the zero-noise skeleton.
The physical continuation is a stochastic first-passage problem comparing
expected-time, distributional, or risk-sensitive Bellman values across
presentations.

## Completeness decision

The present PR has completed the chain it promised:

```text
bounded A/M history jet
 -> moving normalization and induced connection
 -> shape / transport / completion reconstruction
 -> blind family selection
 -> task-preserving presentation quotient
 -> blind bounded morphism discovery
 -> observer-bound stability check
 -> dimensionful clock cocycle
 -> end-to-end Bellman covariance and coordinate red team
```

Within that chain, the remaining gaps are declared scope boundaries rather than
missing proof obligations.  In particular, a non-affine held-out process would
test generalization, but it is no longer needed to make this PR internally
complete.  Adding it here would mix a new representation-completion question
with a closed affine calibration and would make failure attribution harder.

The research plan should therefore continue, but not by extending this PR.
After #86 and this stacked PR are green and merged, open a new Sonnet phase with
the stochastic optical-trap system as the primary physical pressure.  It is a
stronger next test than an arbitrary non-affine deterministic ODE because it
simultaneously pressures task signatures beyond marked sections, stochastic
first-passage clocks, nonlinear presentation morphisms, and Bellman covariance.
The previously proposed heterogeneous non-affine deterministic process should
be retained as a cheaper Phase-0 control inside that new phase, not as the main
research target.

## References

- [Wang-Sevick-et-al-2002] G. M. Wang et al., “Experimental Demonstration of
  Violations of the Second Law of Thermodynamics for Small Systems and Short
  Time Scales,” *Physical Review Letters* 89, 050601 (2002),
  https://doi.org/10.1103/PhysRevLett.89.050601.
- [Jun-Gavrilov-Bechhoefer-2014] Y. Jun, M. Gavrilov, and J. Bechhoefer,
  “High-Precision Test of Landauer's Principle in a Feedback Trap,” *Physical
  Review Letters* 113, 190601 (2014),
  https://doi.org/10.1103/PhysRevLett.113.190601.
- [Kremer-et-al-2024] O. Kremer et al., “Perturbative nonlinear feedback forces
  for optical levitation experiments,” *Physical Review A* 109, 023521 (2024),
  https://doi.org/10.1103/PhysRevA.109.023521.
- [Evstigneev-et-al-2008] M. Evstigneev et al., “Diffusion of colloidal
  particles in a tilted periodic potential: Theory versus experiment,”
  *Physical Review E* 77, 041107 (2008),
  https://doi.org/10.1103/PhysRevE.77.041107.
- [Miller-Shaw-2012] N. J. Miller and S. W. Shaw, “Escape statistics for
  parameter sweeps through bifurcations,” *Physical Review E* 85, 046202
  (2012), https://doi.org/10.1103/PhysRevE.85.046202.
- [Koper-Aguda-1996] M. T. M. Koper and B. D. Aguda, “Experimental
  demonstration of delay and memory effects in the bifurcations of nickel
  electrodissolution,” *Physical Review E* 54, 960 (1996),
  https://doi.org/10.1103/PhysRevE.54.960.
- [Lopez-et-al-2008] B. J. Lopez et al., “Realization of a Feedback Controlled
  Flashing Ratchet,” *Physical Review Letters* 101, 220601 (2008),
  https://doi.org/10.1103/PhysRevLett.101.220601.
- [Dieterich-et-al-2016] E. Dieterich et al., “Control of force through feedback
  in small driven systems,” *Physical Review E* 94, 012107 (2016),
  https://doi.org/10.1103/PhysRevE.94.012107.
