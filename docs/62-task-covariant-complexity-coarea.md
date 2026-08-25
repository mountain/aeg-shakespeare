# Task-covariant complexity coarea and holonomy memory

**Status:** T0 executable refinement of TE-0001; two exact finite/symbolic
results, one global obstruction, and no Theory Map or API promotion.

**Executable essay:**
`tests/research/test_task_covariant_complexity_coarea.py`.

## 1. Why a stronger step was needed

`53-process-volume-frontier-coarea-hypothesis.md` deliberately left the
measure, filtration, reference cell, and clock noncanonical.  Later work added
a universal history lift, a dimensional resource bundle, and covariant
Bellman transport.  Those additions make a sharper question possible:

> Does treating the complexity unit as a transported local frame produce new
> conclusions, rather than merely cleaner dimensional bookkeeping?

This note tests four consequences:

1. moving units change the correct action--period differential;
2. Bellman stopping cost is exactly a weighted frontier volume;
3. task-visible holonomy forces memory even when the visible endpoint closes;
4. a local clock need not admit global simultaneous/stopping sections.

The candidate structure is a **task-covariant complexity polarization** on a
lifted history carrier.  The term remains research-local.

## 2. The local unit is a frame, not a fixed number

For a task `Q`, write the proposed data as

\[
\mathfrak C_Q=
(\widetilde{\mathcal H}_Q,\mathscr Z,
L_T,L_S,\nabla,\vartheta_Q,\Xi_Q,\Sigma_Q).
\]

Here:

- \(\widetilde{\mathcal H}_Q\) retains histories not yet identified by task
  continuation semantics;
- \(\mathscr Z\) is the process direction;
- \(L_T,L_S\) are local time and transverse-resource lines;
- \(\nabla\) transports their units;
- \(\vartheta_Q\) is a clock form;
- \(\Xi_Q\) is a task-declared process-volume density;
- \(\Sigma_Q\) denotes admissible stopping sections.

A local unit is a frame

\[
\mathbf 1_C(h)=\mathbf 1_T(h)\otimes\mathbf 1_S(h),
\]

not an absolute scalar shared by every history state.  Knowing only the
product leaves the reciprocal gauge freedom

\[
\mathbf 1_T\mapsto e^\phi\mathbf 1_T,
\qquad
\mathbf 1_S\mapsto e^{-\phi}\mathbf 1_S.
\]

Therefore a process volume does not by itself choose its time/space split.
The process direction, task frontier, and unit connection are additional
semantic data, not consequences of dimensional multiplication alone.

## 3. Exact moving-scale pendulum identity

For the pendulum family,

\[
E_0=mg\ell,
\qquad
t_0=\sqrt{\ell/g},
\qquad
\mathcal A_0=E_0t_0.
\]

On each frozen dimensionless leaf let

\[
E=E_0\epsilon,
\qquad
\Omega=\mathcal A_0V(\epsilon),
\qquad
T=t_0V'(\epsilon).
\]

Introduce the scale connections

\[
\alpha_E=d\log E_0,
\qquad
\alpha_T=d\log t_0,
\qquad
\alpha_{\mathcal A}=\alpha_E+\alpha_T,
\]

and covariant differentials

\[
\nabla^EE=dE-E\alpha_E,
\qquad
\nabla^{\mathcal A}\Omega
=d\Omega-\Omega\alpha_{\mathcal A}.
\]

Direct substitution gives the exact family identity

\[
\boxed{
\nabla^{\mathcal A}\Omega=T\,\nabla^EE.
}
\]

Indeed,

\[
\nabla^{\mathcal A}\Omega
=\mathcal A_0V'(\epsilon)d\epsilon
=T E_0d\epsilon
=T\nabla^EE.
\]

This is stronger than a change-of-units statement.  Along a path where
`m`, `ell`, `g`, and `epsilon` all vary, the raw slope

\[
\frac{d\Omega}{dE}
\]

need not equal the period.  In the executable red team

\[
m=s,
\quad \ell=s^2,
\quad g=s^3,
\quad \epsilon=s,
\quad V(\epsilon)=\epsilon^2,
\]

the raw slope at `s=1` is `15/14`, while the period is `2`.  The covariant
slope is exactly `2`.  This calibration concerns the geometry of the family
of frozen leaves; it does not assert energy conservation for a physically
driven variable-length pendulum.

## 4. Exact finite frontier identity

Consider a finite rooted task tree.  Each edge `e` has nonnegative canonical
cost \(c_e\), each leaf `i` has probability \(p_i\), and

\[
T_i=\sum_{e\in\operatorname{path}(i)}c_e
\]

is its stopping cost.  Let

\[
M_e=\sum_{i\succ e}p_i
\]

be the probability mass still live across edge `e`.  Rearranging the finite
sum gives

\[
\boxed{
\sum_i p_iT_i
=\sum_ec_eM_e
=\int_0^\infty\Pr(T_Q>\tau)\,d\tau.
}
\]

The three expressions are respectively:

1. expected Bellman stopping cost;
2. edgewise probability-weighted frontier volume;
3. the area under the surviving task-frontier curve.

This is an exact theorem for the declared finite tree, not an analogy.  The
test records two calibrations:

```text
unit costs, probabilities 6/10,3/10,1/10
stopping depths 1,2,2
expected/frontier volume 7/5

non-unit costs, probabilities 1/2,1/3,1/6
stopping costs 2,2,3
expected/frontier volume 13/6
```

The first is the ordinary expected-prefix-depth setting.  The second shows
that the identity survives unequal physical/process edge lengths even though
ordinary unit-depth Huffman reasoning no longer supplies the optimizer.

This locates the two planning languages precisely:

\[
\boxed{
\text{Bellman composes longitudinal transported costs; Hauffman arranges the
task-distinguishable stopping frontier.}
}
\]

Classical Huffman is the flat, unit-edge, fixed-source special case.  A
continuous measured-tree version remains conjectural.

## 5. Holonomy--memory lower bound

For lifted histories `h,h'` ending at the same visible state, define exact
task-continuation equivalence by

\[
h\sim_Qh'
\quad\Longleftrightarrow\quad
O_Q(h\eta)=O_Q(h'\eta)
\quad\text{for every admissible continuation }\eta.
\]

Suppose a connection or deck action gives residuals `g` in a finite set `H`.
Each residual has continuation signature

\[
\operatorname{Sig}_Q(g)
=\bigl(O_Q(g\cdot\eta)\bigr)_\eta.
\]

If `N` distinct signatures occur, any exact continuation-stable state
representation requires at least `N` residual states.  Hence its finite exact
memory obeys

\[
\boxed{
S_Q\ge \lceil\log_2N\rceil\ \text{bits}.
}
\]

The proof is the same distinguishability argument underlying a
Myhill--Nerode lower bound: merging two different signatures produces a
continuation witnessing an incorrect task result.  The new pressure here is
not a new automata theorem; it is the identification of transported
connection/deck holonomy as a systematic generator of continuation residuals
in process geometry.

The executable `C4` calibration separates three tasks on the same four lifted
histories and the same visible endpoint:

```text
task observes the full transported frame    4 classes    2 bits
task observes only frame parity              2 classes    1 bit
task is holonomy invariant                    1 class     0 bits
```

This red team is essential.  Nontrivial topology or holonomy alone does not
force computational memory.  Only task-visible continuation distinctions do.

For the PCR3BP phase-1 result, the scalar Kepler-scale connection has trivial
closed holonomy while the `F2` deck history is nontrivial.  Therefore scale
transport and topological residual must remain separate payload components.
If a future task observes the deck residual, the visible state or scalar scale
jet cannot erase it.

## 6. Global time/space separation has an obstruction

A local clock covector does not automatically define global stopping slices.
The test uses the standard contact form

\[
\vartheta=dz-x\,dy.
\]

The vector fields

\[
X=\partial_x,
\qquad
Y=\partial_y+x\partial_z
\]

lie in \(\ker\vartheta\), but

\[
[X,Y]=\partial_z,
\qquad
\vartheta([X,Y])=1.
\]

Thus \(\ker\vartheta\) is not Frobenius-integrable.  There is no foliation by
global surfaces everywhere tangent to the proposed spatial distribution.

Consequently the candidate factorization

\[
\widehat\Xi_Q
=\widehat\vartheta_Q\wedge
\iota_{\widehat{\mathscr Z}}\widehat\Xi_Q
\]

is always a possible local algebraic decomposition after normalization, but
its interpretation as global time slices sweeping a spatial frontier requires
an integrability theorem.  With curvature or holonomy, the correct Bellman
object may remain bundle- or groupoid-valued rather than reduce to a global
scalar clock tree.

## 7. What changes after introducing the unit frame

The results support four conclusions that are stronger than formal elegance:

1. **Policy correctness.** Values expressed in different local units cannot
   be added before transport; naive Bellman recursion can choose the wrong
   physical policy.
2. **Exact Bellman/Hauffman bridge.** Expected stopping cost equals weighted
   frontier volume on every finite costed task tree.
3. **Task-relative space lower bounds.** Task-visible holonomy creates a
   provable minimum residual memory even when endpoint and local state agree.
4. **A hardness taxonomy.** Clock degeneration, frontier proliferation, and
   nontrivial history transport are different obstructions and demand
   different algorithmic responses.

Objectification also acquires a necessary accounting rule.  Promoting a long
history to one new primitive changes the local ruler; compilation, dictionary,
decoder, and storage costs must be charged, or every computation can be named
as one artificial step.

## 8. Claim boundary and kill conditions

Established here:

- the covariant pendulum family identity above;
- the finite costed-tree frontier identity;
- the finite task-visible holonomy memory bound;
- one exact nonintegrability obstruction.

Not established:

- an AM discovery procedure for \(\vartheta_Q\), \(\Xi_Q\), or \(\nabla\);
- a canonical time/space polarization for arbitrary tasks;
- a continuous measured-history convergence theorem;
- a generic relation between physical phase volume and machine memory;
- an intrinsic scalar complexity in the presence of resource curvature;
- a new complexity class or lower bound for an unbounded computational
  problem.

The route should be rejected or narrowed if:

1. two equally task-canonical unit transports yield incompatible policies;
2. finite refinements fail to converge to any presentation-covariant frontier
   measure;
3. holonomy residuals do not survive task-continuation minimization in any
   non-toy physical example;
4. objectification costs cannot be made representation-covariant without an
   externally arbitrary scalarization.

## 9. Next experiment

The next decisive pressure is not another static finite tree.  It should use a
continuous physical history with all of:

1. a moving local scale unit;
2. a nontrivial lifted/deck residual;
3. a declared task that sometimes observes and sometimes quotients that
   residual;
4. equal-covariant-clock stopping sections in two observer presentations;
5. simultaneous measurement of expected stopping cost, peak frontier, and
   memory--time volume.

PCR3BP is a candidate carrier, but a controlled action/task must be declared
before Bellman optimality or a Hauffman tree is meaningful.  The existing
uncontrolled flow establishes state sufficiency and the word-only failure, not
an optimization problem.

## 10. Governance

```text
Theory edge: TE-0001 refinement
Epistemic maturity: T0 executable theorem candidates
Role: cross-problem calibration and obstruction
Theory Map Change: none
Experimental/Public API pressure: none
```
