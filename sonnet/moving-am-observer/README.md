# Sonnet — Moving A/M Observer Contract (S2′)

The static Hidden A/M Noether search ended with a structural no-go: a frozen
observer in the same product-affine group conjugates stabilizers and therefore
cannot reveal a missing stabilizer dimension.  That result narrows the next
question; it does not reject canonicalization.

This folder freezes the minimum executable contract for the next search:

```text
instantaneous normalization N(data, observer)=0
                         |
                         | differentiate DN=0
                         v
                 observer connection
                         |
                         v
physical process = canonical shape + observer transport
                         |
                         v
                exact reconstruction
```

## Current calibration

`moving_observer_contract.py` runs the known Riccati positive control

`x'=(x-t)(x-t-1)`, with `x=t+y`.

The normalization consists of the two instantaneous roots.  Their derivative,
not a supplied observer law, gives `r'=1,d'=0`.  The physical shape
`y²-y` and transport `-1` reconstruct the canonical lift `y'=y²-y-1` exactly;
its coefficient-jet complexity drops from two to zero.  A frozen observer fails
the differentiated normalization with residual `(1,-1)`.

The red team adds `epsilon*x³`.  Affine transport has degree at most one, so the
cubic coefficient survives in the canonical shape and observed equation.  The
certificate therefore cannot obtain simplicity by silently deleting completion
payload outside its declared observer grammar.

## What this does not establish

This calibration uses the existing exact SymPy constraint backend.  It is not
an AMJet construction, does not discover the root normalization blindly, and
does not reopen the 166 static-frontier expressions with a successful dynamic
observer.  It only makes four future proof obligations executable:

1. normalization must be stated without observer rates in the oracle input;
2. observer motion must be induced by differentiating normalization;
3. shape and transport must be separated; and
4. their lift must reconstruct the original process exactly, including
   out-of-grammar residual payload.

The next falsifiable gate is to derive the required local jet from bounded AM
histories, then search a frozen normalization grammar blindly.  If no
normalization both preserves the task payload and lowers the declared
representation cost, the moving-observer branch also closes negatively.

## First blind gate

`am_history_jet_search.py` now executes that gate on the same hidden control.
The coefficient path is supplied as three finite A/M expression histories.
Their first jets are evaluated compositionally from the Addition rule and the
Multiplication Leibniz rule; no traditional derivative is called by discovery.

The observer grammar is frozen at depth one over `{-1,0,1,t}` with `Add` and
`Mul`, semantically quotiented by exact clock polynomials.  Candidate pairs are
accepted only when both root constraints vanish as symbolic identities, their
history-derived rates equal the induced connection, the scale is positively
oriented at the anchor, and reconstruction is exact.  No expected observer,
labelled sample, or residual-driven switching law is an input.

The bounded census has 24 literal and 11 semantic observer expressions.  Its
121 semantic pairs contain exactly one oriented witness: `(q,s)=(t,1)`.  There
is no static witness.  The discovered lift is `y'=y^2-y-1`, reducing exact
clock-dependent coefficient count from two to zero.  With `epsilon*x^3`
adjoined, the same search still reconstructs exactly and retains cubic
coefficient `epsilon` plus the induced time-dependent quadratic payload
`3*epsilon*t+1`.

This is the first blind positive control, not yet a frontier discovery.  The
Riccati coefficient histories and the two-root normalization family are still
declared by the experiment designer.  The next gate must freeze several
normalization families and apply them to held-out A/M processes without naming
which family should succeed.

## Held-out family selection gate

The search now freezes three families before evaluation:

1. affine root with unit scale;
2. ordered quadratic root pair; and
3. quadratic vertex with unit leading coefficient.

One selector, whose inputs contain neither an expected family nor an expected
observer, is applied to four held-out exact A/M histories.  It uniquely selects
the affine family for `x'=x-t`, uniquely selects the representable root-pair
family for the asymmetric Riccati control, rejects a cubic carrier rather than
discarding its completion direction, and deliberately fails to choose uniquely
for `x'=(x-t)^2-1`.

The last result is the important red team.  The root-pair charts `(q,s)=(t-1,2)`
and vertex chart `(q,s)=(t,1)` both reconstruct exactly and both reduce the
clock-dependent coefficient count to zero.  Therefore “make the presentation
flat” is not by itself a canonicalization principle.  Complexity supplies a
minimum slice, not necessarily a point.  A task quotient, gauge convention, or
additional invariant must resolve the residual choice; the selector is required
to report ambiguity rather than hide it behind iteration order.

This gate also enforces the decomposition discipline: a family is admissible
only at its declared carrier degree.  A cubic direction cannot be treated as a
quadratic residual and silently removed.  Extension to a cubic observer family
would be a separately frozen completion step.

## Task quotient of the minimum slice

The centered-quadratic ambiguity is not two physically distinct optima.  Exact
reconstruction forces the chart morphism from the root-pair coordinate `y` to
the vertex coordinate `z`:

```text
z = 2*y - 1,       dz/dt = 2*dy/dt.
```

The executable certificate transports the complete observed vector field with
zero residual and leaves the clock unchanged.  It also maps the same physical
stopping sections `x=t-1,t+1` from coordinates `(0,1)` to `(-1,1)`.  Thus the
two minimum presentations form one task-preserving equivalence class.

This sharpens the conclusion.  Canonicalization need not select a unique chart;
it should select a unique class modulo task-preserving gauge.  A coordinate-only
penalty such as the sum of squared section coordinates gives `1` in the root
chart and `2` in the vertex chart, demonstrating exactly how a curved measuring
unit can manufacture a false preference.  Such a penalty is inadmissible unless
the task itself marks that coordinate gauge.

The next unresolved issue is no longer tie-breaking this example.  It is to
define task-preserving presentation morphisms independently of a known affine
chart formula, then test whether the quotient of a discovered minimum slice is
stable under a larger observer grammar.

## Blind morphism discovery and bound stability

That next gate is now executable.  The morphism search receives only the two
certified lifts and the marked physical stopping sections.  It enumerates the
same bounded A/M grammar for `z=alpha*y+beta`; no expected `alpha`, `beta`, or
chart-division formula is supplied.  A survivor must simultaneously map the
task sections, commute with physical reconstruction, and conjugate the complete
observed dynamics.

The depth-one census again has 24 literal and 11 semantic expressions.  Its
morphism-pair search returns exactly one certificate, `(alpha,beta)=(2,-1)`.
Corrupting the target dynamics while leaving task sections and reconstruction
charts unchanged produces no survivor, so endpoint agreement alone cannot
forge a morphism certificate.

Finally, the observer grammar is enlarged from depth one to depth two before
normalization selection: 156 generated expressions quotient to 60 exact
semantic clock polynomials, hence 3,600 observer pairs per family.  The centered
quadratic still has exactly the same two minimum presentations, and they still
form one task-equivalence class.
This is bounded stability evidence, not an unbounded theorem: deeper grammars,
non-affine morphisms, and task signatures not consisting of marked sections
remain open.

## Dimensionful Bellman closure

`01-dimensionful-bellman-calibration.md` restores length `L`, speed `V`, and the
physical time scale `L/V` for the centered moving process.  It compares the
canonical coordinate `u=(x-Vt)/L` with the nonlinear A/M chart `w=u+u^3`.

Equal physical-clock sections give independently integrated clocks, Bellman
values, and policies agreeing below `1e-45`; doubling `L/V` doubles value and
preserves policy.  Equal coordinate grids select different physical sections,
change value by more than `0.05` seconds in the declared calibration, and change
the optimal tree.  This closes the dimensional clock/Bellman arrow without
identifying coefficient variation with computational time cost.

The dimensionful note also records the physical realization as a feedback-
synthesized translating nonlinear potential, its saddle-node normal-form
interpretation, the overdamped/Noether boundary, and the stochastic Langevin
continuation.  Its completeness audit closes this PR's affine deterministic
phase and moves the next physical pressure to a separate stochastic
first-passage Sonnet rather than growing the current stack further.
