# PCR3BP dimensional scale jets: topology, Bellman state, and Huffman boundary

**Status:** Phase 1 numerical/exact calibration; research-local; no framework
extraction proposed.

**Stable entry point:** `00-phase0-history-cost.md` states the physical problem,
equations, topology, and phase-0 cost comparison.  This note tests the stronger
claim that dimensional scales already expose homotopy strata and that a local
observer ODE transports those scales compatibly.

## 1. Primitive audit

The primitive physical process remains the rotating PCR3BP vector field on a
fixed Jacobi leaf.  This phase adds no orbit oracle, propagator, prescribed
symbolic itinerary, or imported `SL(2)` observer ODE.

For primary masses `m1=1-mu`, `m2=mu` and distances `r1,r2`, use the two local
Kepler clock scales

```text
sigma_i = r_i^(3/2) / sqrt(m_i),       u_i = log sigma_i.
```

They are forced by the local dimensional balance `T^2 ~ R^3/M`.  Their local
process rates are

```text
beta_i = Z u_i
       = (3/2) ((q-p_i) dot q_rate) / r_i^2.
```

Thus `(u1,u2,beta1,beta2)` uses only the current state and current process
generator.  It satisfies the Observation Localization Principle.

## 2. The scale domain already sees the singular strata

Because the primaries are one unit apart, the two radii obey

```text
|r1-r2| <= 1 <= r1+r2.
```

The interior has two orientation sheets, `y>0` and `y<0`.  Its boundary is the
primary axis, and its two collision corners are

```text
(r1,r2)=(0,1),       (1,0).
```

Away from the axis, the scale 1-jet reconstructs the complete configuration
and velocity:

```text
x+mu = (r1^2-r2^2+1)/2,
(2/3) beta_i r_i^2 = (q-p_i) dot q_rate.
```

On the axis the two radial covectors become dependent.  At a crossing section,
the fixed Jacobi value reconstructs the magnitude of the missing normal
velocity and the crossing orientation reconstructs its sign.  Therefore

```text
(u1,u2,beta1,beta2, sheet/crossing sign, C)
```

is a local sufficient observer state, including at the declared gates.  This
is the concrete sense in which dimensional scale analysis precedes and
respects the topology rather than merely attaching a few characteristic
numbers afterward.

## 3. Topological history is retained separately

The scale domain selects two natural outward boundary rays: the axis left of
the first collision corner and right of the second.  Crossings record the free
generators `a/A` and `b/B`.  Synthetic based loops certify

```text
loop(p1) -> a,
loop(p2) -> b,
[loop(p1),loop(p2)] -> abAB.
```

The associated `Gamma(2)` commutator is

```text
rho(abAB) = [[13,8],[8,5]],
ell_H = 2 arcosh(9) ~= 5.77454.
```

But each scalar scale ODE is exact:

```text
integral_gamma beta_i dtheta = Delta u_i = 0
```

for every closed based loop.  The commutator has nontrivial nonabelian deck
holonomy while both scalar scale holonomies vanish.

This is a useful negative result.  Dimensional scale transport respects the
homotopy stratification because it is deck-invariant, but two exact scalar
rates do not by themselves generate the `F2` history.  A nonabelian observer
connection would require an additional canonicalization constraint; inserting
`sl(2)` by hand here would violate discovery and locality discipline.

## 4. Bellman audit

At `mu=0.1`, `C=3.55`, two integrated trajectories give

```text
initial (x, angle)    first four gates    fifth gate    fifth edge clock
(-0.05, 60 deg)      aaaa                A             about 0.46
(-0.05, 80 deg)      aaaa                a             about 1.71
```

Thus the universal word prefix `aaaa` is not continuation-stable: it neither
determines the next symbol nor its physical cost.  A value function on the word
alone cannot satisfy an exact Bellman recursion for this physical process.

The local scale-jet state does distinguish the two cases and reconstructs the
Poincare-section physical state.  Consequently it is a valid Markov carrier
for the physical future.  For a task that also depends on lifted topology, the
state is `(word, scale jet, crossing sign, C)`.  This carrier can support a
future Bellman problem with additive physical clock.  The present uncontrolled
PCR3BP, however, supplies no native action set and no declared optimization
task.  What has been established is Bellman **state sufficiency**, not a
Bellman policy or optimum.

## 5. Huffman / Hauffman audit

The lifted histories certainly form a prefix tree, but a prefix tree is not yet
a Huffman source.  Ordinary Huffman coding would require edge probabilities
and symbol costs determined by a continuation-stable quotient.  Phase 1 shows
that the word prefix fails this requirement; probabilities estimated only by
word would mix physically different scale jets.

The current verdict is therefore:

```text
universal prefix tree                    yes
word-only Bellman state                  no
scale-jet Bellman carrier                yes
nontrivial Bellman optimization          not yet declared
ordinary Huffman tree                    not yet justified
```

A later phase may declare a physical control/task, sample the induced return
kernel on the scale-jet section, and search for a finite continuation-stable
task quotient.  Huffman becomes legitimate only if that quotient makes the
conditional source approximately memoryless; otherwise the correct object is
a continuous-state Bellman or Markov-renewal problem on the lifted scale jet.

## 6. Theory Map relation and claim boundary

This phase supports the chain

```text
dimensional quotient -> singular scale domain -> local scale jet
                      -> universal history lift -> task-dependent coding
```

and refines the H0/H2/H3 boundary.  It does not prove that dimensional
analysis alone determines a universal cover, that the scale connection is
nonabelian, or that `SL(2,R)` is canonically forced in PCR3BP.  The `SL(2)` deck
calibration remains a topological comparison until a local canonicalization
derives a corresponding observer connection.
