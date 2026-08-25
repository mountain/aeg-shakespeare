# Planar circular restricted three-body problem: costed lifted histories

**Problem:** planar circular restricted three-body problem (PCR3BP / CR3BP).

**Domains:** celestial mechanics, Hill regions, free groups, covering spaces,
hyperbolic uniformization, symbolic dynamics, numerical integration.

**Classical names / aliases:** Jacobi integral, zero-velocity curve, Lagrange
point `L1`, twice-punctured plane, pair of pants, modular lambda cover,
principal congruence group `Gamma(2)`.

**Process Geometry roles:** process history, observer gate, universal-history
lift, task-relative cost, topological threshold, dimensionless clock,
Huffman/Bellman red team.

**Prerequisites:** rotating-frame PCR3BP equations; elementary free-group
reduction; the trace classification of elements of `PSL(2,R)`.

**Related vignettes:**
`tests/research/test_kepler_sundman_collision_branch.py` and
`tests/research/test_dimensionful_moving_observer_bellman.py`.

**Theory Map relation:** refines H0/H2/H3 separation.  It is a numerical
calibration, not evidence that A/M arithmetic alone selects a universal cover
or a fundamental domain.

## 1. Question and claim boundary

The phase-0 question is deliberately narrower than orbit design:

> Can one physical trajectory be lifted to a noncommutative topological
> history and assigned three independently auditable costs: free-word length,
> deck-translation length, and physical elapsed clock?

This phase does **not** claim a complete symbolic dynamics, a Markov partition,
or that every reduced word is dynamically realizable.  It does not use Huffman
coding yet.  Huffman becomes legitimate only after a task quotient supplies a
prefix source with stable conditional probabilities; the current lifted tree
is only a candidate Bellman carrier.  Phase 1 tests its state sufficiency.

## 2. Primitive physical process and oracle

Normalize primary separation, total mass, and rotating angular rate to one.
The primaries are

```text
p1 = (-mu, 0),       p2 = (1-mu, 0).
```

With

```text
Omega(x,y) = (x^2+y^2)/2 + (1-mu)/r1 + mu/r2,
```

the rotating-frame process is

```text
x'  = vx,
y'  = vy,
vx' = 2 vy + Omega_x,
vy' = -2 vx + Omega_y.
```

The independent task oracle is the Jacobi integral

```text
C = 2 Omega - vx^2 - vy^2.
```

The integrator never projects back to a constant-`C` surface.  Consequently
`max |Delta C|` is a real numerical error certificate rather than an enforced
identity.

## 3. Observer gates and the free-group lift

Configuration space excludes the two collision points:

```text
Q_mu = R^2 - {p1,p2},          pi_1(Q_mu) = F2 = <a,b>.
```

Choose two disjoint upward rays from the primaries.  A left-to-right crossing
of the ray at `p1` records `a`, and the reverse records `A=a^-1`; the second ray
records `b/B`.  Adjacent inverse crossings are cancelled.  This gate is an
explicit observer choice: changing the cuts changes the word presentation but
not the underlying homotopy class (up to the usual base-path convention).

For comparison with the universal cover of the thrice-punctured sphere, map

```text
a -> [[1, 2], [ 0, 1]],
b -> [[1, 0], [-2, 1]].
```

These generate `Gamma(2)/{+/-I} ~= F2`.  For a deck matrix `G`, its stable
hyperbolic translation length is

```text
ell_H(G) = 2 arcosh(|tr G|/2)   when |tr G| > 2,
           0                    otherwise.
```

In particular, arbitrarily long cusp words `a^k` and `b^k` are parabolic and
have `ell_H=0`.  Therefore word length is not hyperbolic translation length.

## 4. Frozen phase-0 experiment

Parameters are

```text
mu = 0.1,     C = 3.55,     raw crossing budget = 12.
```

The code brackets the inner collinear equilibrium and obtains

```text
x_L1 ~= 0.6090351100,       C1 ~= 3.5969532299.
```

Thus `C<C1`: the `L1` neck is open while the Jacobi surface still constrains
which transitions are possible.  Initial conditions lie on `y=0`; their speed
is solved from `C`, and only the direction angle is supplied.  Integration
stops at twelve raw gate crossings, a collision guard, an escape guard, or a
clock limit.  A distance-adapted fourth-order Runge--Kutta step with maximum
step `0.001` follows the local `r^(3/2)` Kepler scale near a primary.

Run:

```bash
python sonnet/pcr3bp-history-cost/phase0_history_cost.py
```

The deterministic census gives:

| history | `n Delta t` | reduced word | `|w|` | `ell_H` | `max |Delta C|` |
| --- | ---: | --- | ---: | ---: | ---: |
| left parabolic | 30.299 | `AAAAAAAAAAAA` | 12 | 0.000 | `1.87e-12` |
| left to right | 20.877 | `AAAAAAAAAAAB` | 12 | 7.474 | `3.31e-7` |
| mixed 1 | 23.060 | `AAABBBBBAAAA` | 12 | 9.854 | `3.00e-10` |
| mixed 2 | 21.428 | `BAAAAAAABBBB` | 12 | 9.854 | `6.43e-8` |
| mixed 3 | 19.243 | `AAAAAAABBBBB` | 12 | 9.854 | `7.46e-8` |
| right parabolic | 5.808 | `bbbbbbbbbbbb` | 12 | 0.000 | `7.38e-10` |

The endpoint table is not a ranking.  It is a falsification surface for three
tempting identifications:

1. the same raw history budget need not cost the same physical clock;
2. the same reduced word length need not have the same `ell_H`;
3. neither symbolic measure determines the Jacobi-admissible transition set.

All six histories have the same symbol budget, yet their clocks differ by a
factor greater than five and their deck lengths split into three values.  The
two pure cusp histories are the sharpest red team: their word and clock costs
are nonzero while their stable hyperbolic translation length is exactly zero.

The experiment therefore supports only a qualified version of the motivating
idea.  Topology supplies the free deck group and a family of fundamental-domain
presentations; the dimensional scale supplies the natural clock unit; the
dimensionless Jacobi value selects Hill-region connectivity and prunes legal
transitions.  The scale does not by itself select the two branch cuts or a
unique hyperbolic polygon.  Those remain observer/presentation data.

## 5. What the experiment teaches Process Geometry

The lifted object is a **costed, dynamically pruned history tree**, not merely
the Cayley tree of `F2` and not merely a geodesic graph in `H2`.  It contains at
least three non-interchangeable structures:

```text
topological edge label     a, A, b, B
deck displacement cost    ell_H
physical execution cost   n Delta t
```

This refines the H0/H2/H3 boundary: a covering-space presentation does not
automatically provide the task cost needed by H3 coding, while physical scale
does not automatically canonize the H2 presentation.  The current result is a
research-local calibration and proposes no framework extraction.

## 6. What would count as the next phase

Phase 1 is recorded in `01-scale-jet-topology-and-coding-audit.md`.  A later
probabilistic/control phase must sample a declared Poincare return section over
several Jacobi levels on both sides of `C1`, retain escape and collision as
explicit outcomes, and test whether a finite task quotient makes conditional
transitions approximately continuation-stable.

## References

- V. Szebehely, *Theory of Orbits: The Restricted Problem of Three Bodies*,
  Academic Press, 1967.
- A. F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983.
- A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002,
  Sections 1.1--1.3 for fundamental groups and covering spaces.
