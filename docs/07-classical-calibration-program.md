# Classical Calibration Program

**Status:** test-design note.  Classical systems are regression/research probes of shared Shakespeare machinery, not package-level problem objects.

## 1. Why classical tests matter

The goal is not to show that Shakespeare can reproduce textbook answers.  A
useful calibration should force the library to recover a structural language
that the textbook presentation normally supplies in advance.

Each classical test should therefore separate:

1. **first-principles input** — assignments, primitive processes, algebraic
   constraints, task, and allowed operations;
2. **forbidden prior language** — coordinates, named special functions,
   spectral modes, canonical transformations, or known closed forms that would
   trivialize the discovery;
3. **Shakespeare discovery** — relations, invariants, quotients, process
   modules, history geometry, primitive proposals, and presentation costs;
4. **structural assertions** — statements in Shakespeare's process language;
5. **classical shadow** — only at the end, compare with the known analytic or
   mechanical result.

This makes the tests resistant to formula matching.

## 2. Proposed test layers

The repository can gradually move toward:

```text
tests/
  unit/        # implementation contracts
  laws/        # problem-independent metamorphic laws
  classical/   # classical analysis/ODE/mechanics calibrations
  research/    # cross-problem universality and representation comparisons
```

Existing tests need not be moved immediately.  New classical systems should
start in `tests/classical/` and use only public library machinery unless a new
problem-independent abstraction is genuinely required.

## 3. Structural sequence

A useful order is not textbook ODE difficulty, but the first appearance of a
new process structure:

| Calibration | Structural target |
| --- | --- |
| free particle | unbounded trajectory with a tiny parabolic grammar |
| harmonic oscillator | short recurrent process relation |
| damped oscillator | compact/parabolic/hyperbolic grammar transition |
| Riccati | projective/Mobius process closure |
| simple pendulum | constrained process -> invariant leaf -> genus-one quotient |
| quartic/Duffing oscillator | different primitive process -> same genus-one class |
| Euler top | multiple invariants -> genus-one reduced dynamics + reconstruction |
| Kepler | algebraic cover + history-depth lift |
| Foucault/Berry-type examples | observer transport/holonomy |
| Mathieu/Van der Pol | return relations plus slow ruler/observer transport |

The sequence is meant to test whether apparently different classical methods
can be recovered as shadows of a smaller number of process-presentation
mechanisms.

## 4. Canonical pendulum test: no angle/trigonometric input

The pendulum is the first calibration where using the usual angle equation

\[
\ddot\theta+\sin\theta=0
\]

would already bake a major representation choice into the input.  The canonical
Shakespeare test therefore starts from a planar constrained position `q`,
velocity `v`, fixed gravity direction `e`, and an unresolved constraint force:

\[
\langle q,q\rangle=1,
\]

\[
\mathscr Dq=v,
\qquad
\mathscr Dv=-e+\lambda q.
\]

No `theta`, `sin`, or `cos` is supplied.

### 4.1 Constraint prolongation

Differentiating the rod relation yields tangency,

\[
\langle q,v\rangle=0,
\]

and preserving tangency determines

\[
\lambda=\langle e,q\rangle-\lVert v\rVert^2.
\]

The important library abstraction is not a `Pendulum` class, but exact
algebraic constraints/quotients plus process prolongation.

### 4.2 Invariant leaf

The process preserves

\[
H=\frac12\lVert v\rVert^2+\langle e,q\rangle.
\]

Fixing `H=E` creates a task/reduced leaf.  Let

\[
U=\langle e,q\rangle,
\qquad
Y=\mathscr DU=\langle e,v\rangle.
\]

Then the constraint ideal implies

\[
\boxed{Y^2=2(E-U)(1-U^2)}.
\]

The right-hand side is cubic in `U`.  Its discriminant is

\[
\boxed{64(E-1)^2(E+1)^2}.
\]

Hence the generic smooth projective completion has genus one, while `E=+/-1`
marks degenerations.

The central assertion is therefore not "the solution is a Jacobi elliptic
function".  It is:

> a first-principles constrained process, after invariant reduction, forces a
> genus-one algebraic process quotient without receiving trigonometric or
> elliptic-function language as input.

Only after this structural assertion should the test compare the natural
process differential `dU/Y` with the classical elliptic integral.

## 5. Why this is a stronger calibration

The traditional transcendental nonlinearity `sin(theta)` is absent from the
first-principles process.  It appears only if the configuration circle is first
parameterized by an angle.  The calibration therefore tests the hypothesis:

> some apparent nonlinear function complexity is representation complexity,
> not intrinsic process complexity.

The same machinery can then be applied to quartic oscillators and Euler top. If
different primitive processes independently reduce to genus-one quotients,
Shakespeare has evidence for a common standard process geometry rather than a
collection of memorized special-function solutions.

## 6. Function-theory comparison

The A/M function theory and genus-one/Abelian function theory should remain
separate candidates.

A/M can be efficient when Addition/Multiplication process closure produces a
small weight/module language.  A pendulum energy leaf instead naturally produces
an algebraic curve.  Shakespeare should eventually compare these languages by
closure, task sufficiency, history cost, decoder cost, and presentation cost,
not assume in advance that one theory is universal.

This is the intended role of classical tests: determine which process function
language is *forced or economical* for a problem, and identify when distinct
problems converge to the same representation geometry.

## 7. Effective-analysis calibration standard

Recovering the correct geometric shadow is necessary but no longer sufficient
for an analysis-bearing calibration.  A mature comparison should test whether
the process-adapted language preserves the operational strengths of classical
calculus.

For each candidate presentation, record separately:

| Question | Required evidence when claimed |
| --- | --- |
| Semantic adequacy | task equivalence, preserved/forgotten payload, and reconstruction boundary |
| Symbolic effectiveness | operator action, closure or forced extension, exact residual/property/round-trip certificate |
| Numerical effectiveness | domain, units, scale-aware error or convergence, branch/singularity/nonconvergence behavior, independent reference |
| Computational economy | workload and baseline; discovery/compilation, repeat evaluation, storage, dictionary, residual, and decoder/lowering cost |
| Transport/closure | observer/presentation covariance and lift/quotient/rank-lowering compatibility where claimed |

The conventional solution is therefore not only a value oracle.  It is a
baseline for symbolic closure, numerical conditioning, and cost.  A
process-first presentation that reconstructs the same formula but is less
stable or more expensive remains mathematically informative, but its claimed
computational advantage must be weakened.

The default broad calibration suite should eventually contain an exact finite
case, an independently checkable continuous/integrable case, and a
nonintegrable, stiff, branched, singular, or nonconservative red team.  No
single local test must cover the whole suite; breadth of evidence must track
breadth of claim.
