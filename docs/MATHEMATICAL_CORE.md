# Process Geometry — mathematical core

**Status:** living mathematical synthesis; required first reading for
substantial research, theory, and theory-bearing API work.  This document is
not a frozen specification and not a Public API contract.

**Required next reading:** [`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md),
which turns the mathematics into problem, representation, algorithm,
certificate, error/failure, and cost decisions for feasible computation.

## 0. Purpose and authority

Process Geometry needs more than a list of concepts.  Mathematical
understanding must state the objects, constructions, laws, information loss,
reconstruction obligations, and failure boundaries that make one concept lead
to another.

The repository therefore separates four duties:

```text
MATHEMATICAL_CORE.md   objects, constructions, equations, and boundaries
ENGINEERING_ARCHITECTURE.md representations, algorithms, evidence, errors, cost
THEORY_MAP.md          compact location, dependency, and maturity map
THEORY_GOVERNANCE.md   promotion, falsification, and revision rules
GOVERNANCE.md          theory-to-software and API discipline
```

The Theory Map is an index of mathematical understanding; it is not a
substitute for that understanding.  A proposed node or arrow is not ready for
the stable map merely because it has an attractive name.  It must be possible
to recover, here or in a linked theory record:

1. its input and output objects;
2. the construction joining them;
3. the preserved and forgotten information;
4. at least one equation, invariant, universal property, or obstruction;
5. its local/global and existence/uniqueness status;
6. its decoder or reconstruction boundary;
7. its executable or independently checkable evidence;
8. a negative control or kill condition.

When this synthesis and a detailed proof artifact disagree, the discrepancy
must be reported and repaired; a compact synthesis never overrides a more
precise theorem or certificate silently.

---

## 1. Present first-principles schema

The current evidence supports the following order of questions:

```text
primitive process and literal histories
    -> declared continuation task
    -> history unfolding / task-sufficient lift
    -> transported clock, resource, unit, or residual
    -> stopping section or task quotient
    -> quotient carrier and retained decoder data
    -> topology / complexity / analysis when justified
    -> possible objectification and higher-rank composition
```

This is a schema, not a claim that one universal carrier has already been
found.  In particular, the transported datum may be additive, max-like,
group-valued, phase-valued, measure-valued, or problem-local.  Current evidence
does not identify one generic `HistoryPayload` or scalar complexity object.

### 1.1 Literal history and task state

Let \(\mathcal H\) be a family of admissible histories with a partially defined
continuation operation.  A declared task \(Q\) evaluates the future behaviour
of a history through its admissible continuations.  In the exact deterministic
case, the task equivalence has the form

\[
h\sim_Q h'
\quad\Longleftrightarrow\quad
Q(hk)=Q(h'k)
\quad\text{for every continuation }k
\text{ in the declared common continuation interface}.
\]

The corresponding task state is an equivalence class in
\(\mathcal H/{\sim_Q}\), not necessarily a visible vertex supplied in advance.
For stochastic, nondeterministic, approximate, or resource-bounded tasks the
codomain and quantifiers must be declared again; the displayed exact relation
must not be reused by analogy without doing so.

This gives the first information contract:

```text
literal history -> task quotient
preserves: every declared future observation
forgets: distinctions no declared continuation can expose
decoder: exists only for information deliberately retained outside the quotient
```

### 1.2 Three different lifts

The word *lift* currently covers three structures that must remain distinct.

1. **Full history unfolding.**  Histories are kept as prefix objects before
   future equivalence.  This is available even when the visible process is
   non-Markovian.
2. **Topological universal cover.**  A space with a specified topology may
   have a universal covering space.  For a graph this is a tree of reduced
   path classes, but it is not automatically the full prefix history of an
   arbitrary history-dependent process.
3. **Analytic developing cover.**  A differential may be integrated on a
   cover to obtain a single-valued developing coordinate.  Its deck kernel
   records analytic periods.

A task-sufficient lift may lie strictly between the full history unfolding and
the visible quotient.  No theorem currently makes the topological or analytic
universal cover the canonical task-sufficient lift for every process.

### 1.3 Observer and transported payload

An observer is not, in general, a free-standing differential equation.  The
minimal mathematical datum is a task-relative evaluation or presentation map

\[
\pi_Q:\mathcal H\longrightarrow Z_Q,
\]

together with the continuation semantics needed to decide whether \(Z_Q\) is
sufficient.  When variation is part of the task, the observer also needs the
appropriate history jet, clock, frame transport, branch data, or connection.
Only after these are declared may an induced observer equation be written on
\(Z_Q\).

In many exact problems the observer map itself factors through a composable
evaluation payload:

\[
h\longmapsto c(h)\longmapsto e_o(c(h))\longmapsto
[e_o(c(h))]_Q.
\]

Here \(c(h)\) can already identify literal histories, \(e_o\) evaluates it in
an observer/base frame \(o\), and the final arrow applies the declared task
quotient. These are separate information-loss boundaries. If continuation
does not descend through one arrow, the missing datum must remain as a
residual; a correct endpoint or contact evaluation alone does not certify
future adequacy.

A transported history datum is provisionally cocycle-like.  Schematically,

\[
c(hk)=c(h)\odot \tau_h c(k),
\]

where \(\tau_h\) transports the second contribution into the frame reached by
\(h\).  Ordinary additive cost has \(\odot=+\) and trivial transport; holonomy,
moving units, peak cost, and phase require different laws.  This equation is a
common shape, not yet a single promoted mother object.

### 1.4 Unit one as a local frame

Dimensional analysis is part of the mathematical data rather than display
metadata.  For a physical dimension \(d\), regard quantities as living in a
one-dimensional scale line \(L_d\).  A choice of unit is a nonzero local frame
\(u_d\in L_d\).  Writing

\[
x=[x]_u\,u_d
\]

defines the numerical coordinate of the physical quantity.  If
\(u'_d=a\,u_d\), then

\[
[x]_{u'}=a^{-1}[x]_u.
\]

Thus “unit one” is the coordinate \(1\) of a chosen frame, not an additional
dimensionless physical constant.  If the frame moves over a parameter or
observer space, raw derivatives of coordinates are not invariant; a
connection or equivalent transport rule is required.

Units and quotients perform different operations:

```text
quotient / deck kernel     says which lifted histories are identified
fundamental domain         chooses representatives for those identifications
unit frame                 measures the representatives
cost functional            orders or compares them for a declared task
```

Consequently a period lattice does not choose a scalar history cost, and a
unit choice does not create a fundamental domain.

### 1.5 Stopping sections, fundamental domains, and task residuals

A stopping rule selects a frontier or section \(\Sigma_Q\) in lifted history.
When a group \(G\) acts on the lift and the task identifies its orbits, a
fundamental domain is a choice of representatives for the relevant quotient.
The relevant group may itself be task-dependent: a carrier-only task can
forget a deck transformation that a full reconstruction task must retain.

If a finite task sees \(N_Q\) distinct continuation signatures, any exact
finite state representation requires at least

\[
b_Q=\left\lceil\log_2 N_Q\right\rceil
\]

bits of residual state.  This is an exact distinguishability bound.  It is not
by itself Shannon entropy, runtime, physical phase volume, or machine memory
usage for a particular implementation.

### 1.6 Continuous volume, discrete shells, and finite memory are different laws

For a one-degree-of-freedom Hamiltonian family, classical action--period
coarea gives

\[
d\Omega=T\,dH.
\]

A thin action shell is therefore a full physical history-domain length
multiplied by a transverse energy thickness.  This is the current exact
continuous calibration of process volume.

The finite projective-tree calibration supplies a different exact shell law.
For the standard-root ball \(B_d\) in the \((p+1)\)-regular Bruhat--Tits tree,
with sphere

\[
S_d=\mathbb P^1(\mathbb Z/p^d\mathbb Z),
\]

one has

\[
|S_d|=(p+1)p^{d-1},
\qquad
|B_d|-|B_{d-1}|=|S_d|.
\]

This is a discrete boundary-increment or coarea-like identity: one additional
longitudinal refinement layer exposes a transverse finite frontier. It has no
physical period or energy thickness, and it does not by itself supply a source
probability or coding objective.

The finite residual bound \(b_Q=\lceil\log_2N_Q\rceil\) is a separate exact
statement.  Current evidence does **not** identify energy with computational
space, tree depth with transverse memory, action with entropy, or
\(T\times S\) as one universal scalar complexity. A future unification would
have to specify the measure, stopping section, units, task evaluation, and
limiting operation that connect these laws.

---

## 2. The simple pendulum as the first end-to-end model

The pendulum now realizes enough of the preceding schema to locate elliptic
curves, elliptic functions, units, fundamental domains, and the Bolza boundary
without making any of them primitive.

### 2.1 Primitive constrained process

Use dimensionless time \(\tau=t/t_0\), position \(q=(q_x,q_y)\), and
\(v=Dq=dq/d\tau\).  The primitive Cartesian data are

\[
\langle q,q\rangle=1,
\qquad
\langle q,v\rangle=0,
\qquad
E=\frac{\langle v,v\rangle}{2}+q_y.
\]

No angle, trigonometric solution, elliptic curve, named special function, or
Addition/Multiplication chart is required at this stage.

Choose the scalar observable and its first history jet

\[
U=q_y,
\qquad
Y=DU=v_y.
\]

Eliminating the hidden Cartesian coordinates forces the marked carrier

\[
C_E:\qquad Y^2=2(E-U)(1-U^2),
\]

with induced observer dynamics

\[
DU=Y,
\qquad
DY=3U^2-2EU-1,
\]

and clock form

\[
\omega=\frac{dU}{Y},
\qquad
\omega(D)=1.
\]

Here the “observer equation” is the dynamics induced after declaring
\(\pi(q,v)=(U,Y)\).  It is inseparable from the quotient map, its task, and the
Cartesian information that the quotient forgets.

### 2.2 Unit frame and physical dimensions

The natural pendulum scale frame is

\[
E_0=mg\ell,
\qquad
t_0=\sqrt{\frac{\ell}{g}},
\qquad
A_0=E_0t_0=m\ell\sqrt{g\ell}.
\]

Thus

\[
dt=t_0\omega.
\]

The dimensionless marked carrier and its period shape do not change when the
physical frame is rescaled; physical period and action coordinates transform
through \(t_0\) and \(A_0\).  Along a family with moving scale frames the
invariant action--period statement is covariant,

\[
\nabla^{\mathcal A}\Omega
=T\,\nabla^E H,
\]

rather than an unqualified derivative of numerical coordinates taken in
different units.

### 2.3 Lifted clock, period kernel, and fundamental domain

On the certified nondegenerate \(E=0\) leaf, integrate the marked clock:

\[
z(P)=\int^P\omega.
\]

The analytic developing coordinate is single-valued on \(\mathbb C_z\).  The
periodic readout has kernel

\[
\Lambda=\omega_A\mathbb Z+i\omega_A\mathbb Z,
\]

so the completed visible carrier is

\[
\overline{C}_0(\mathbb C)\simeq\mathbb C_z/\Lambda.
\]

The lattice cuts the analytic fundamental domain; the unit frame measures it:

\[
\Lambda_{\mathrm{phys}}=t_0\Lambda.
\]

The Abel cover is therefore an exact downstream model of lifted clock history
on this leaf.  It has not thereby been proved to be the canonical upstream
history unfolding of the raw process.

The real fundamental domain is task-relative.  One interval of length
\(\omega_A\) closes \((U,Y)\) but flips the hidden Cartesian sheet.  The full
physical state closes only after \(2\omega_A\).  Hence

```text
carrier task       real domain length = omega_A       residual = 0 bits
Cartesian task     real domain length = 2 omega_A     residual = 1 bit
```

The local clock is the same; the quotient and reconstruction obligation are
different.

### 2.4 Elliptic curve and elliptic function

The physical meanings are now located precisely:

- the **elliptic curve** is the complex completed quotient geometry of the
  task-visible marked carrier, equivalently \(\mathbb C_z/\Lambda\) on the
  certified leaf;
- an **elliptic function** is a periodic decoder from the additive lifted
  clock to a visible coordinate.

At \(E=0\), one such decoder is

\[
U(z)=-\operatorname{sn}^2\!\left(\frac{z}{\sqrt2},i\right).
\]

Thus the special function is not the physical mechanism.  It is the inverse
readout made periodic by the kernel of histories that the carrier task
identifies.

### 2.5 Action as swept history-domain volume

Let \(\epsilon=E+1\) be the bottom-referenced libration energy and
\(m=\epsilon/2\).  The full physical action and period are

\[
\frac{\Omega}{A_0}
=16\bigl(\mathbf E(m)-(1-m)\mathbf K(m)\bigr),
\qquad
\frac{T}{t_0}=4\mathbf K(m),
\]

and satisfy

\[
\frac{d\Omega}{dH}=T.
\]

The action is therefore the integral of full physical history fundamental
domains across transverse energy.  The reduced carrier domain is half the
full-state real domain on the certified \(E=0\) leaf.  The reference action
\(A_0\) makes the result dimensionless; it is not a universal action quantum
or information cell.

### 2.6 Why the Bolza surface appears

The physical velocity sheet is

\[
Y^2=2(E-U)(1-U^2).
\]

A separate, declared observer metric with weight \(c\) introduces another
square-root sheet

\[
Z_m^2=c+U^2.
\]

Keeping only the product sign, \(W=YZ_m\), gives the quotient

\[
W^2=2(E-U)(1-U^2)(c+U^2).
\]

At the special choice \(E=0,c=1\), setting \(w=W/\sqrt2\) yields

\[
w^2=U^5-U,
\]

the standard affine Bolza model.  Its compactification is the genus-two Bolza
surface.  Its appearance therefore has a precise provenance: it is a
product-sign quotient after adjoining an independent metric sheet.

For the finite two-sheet census, a task that sees both signs, only their
product, or neither requires respectively

\[
2,\quad 1,\quad 0
\]

bits.  The Bolza quotient retains the product bit and forgets the individual
sheet signs.  It is not the pendulum state space, not another coordinate chart
on \(C_E\), and not a metric-independent canonical completion.

---

## 3. Finite projective-tree calibration

The local-field Sonnet supplies an independent exact discrete calibration of
the first-principles schema. For an odd prime \(p\), a finite \(p\)-adic
continued-fraction prefix has the information chain

\[
h_n=(a_0,\ldots,a_n)
\longmapsto
G_n=M(a_0)\cdots M(a_n)
\longmapsto
V_n=[G_n\mathbb Z_p^2],
\qquad
M(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix}.
\]

The literal word \(h_n\) is full prefix history. The matrix \(G_n\) is a
composable projective payload; different words may already have the same
matrix evaluation. The lattice class \(V_n\) evaluates that payload at the
standard \(p\)-adic lattice frame and forgets further right-integral and
homothety data. Reduction to a fixed depth retains only a finite projective
cylinder. These are successive constructions, not synonyms for one lift.

The Bruhat--Tits tree is therefore an observer/evaluation geometry in this
calibration. It is not automatically the full history unfolding, the
topological universal cover of a supplied visible process, or the binary
coding tree introduced for a later source task.

The exact continued-fraction reconstruction law is

\[
\alpha_0=G_n\cdot\alpha_{n+1}.
\]

Thus \(\alpha_{n+1}\), the next complete quotient, is retained continuation
residual/decoder data. A finite contact or lattice vertex may be correct for
the declared observation and still be inadequate for reciprocal continuation.
Ruban and Browkin supply the exact red team: they choose different sections of

\[
\mathbb Q_p\longrightarrow\mathbb Q_p/p\mathbb Z_p,
\]

their representatives have the same local contact, and reciprocal continuation
can separate them into different terminal or cyclic outcomes.

The standard lattice \(L_0=\mathbb Z_p^2\) fixes the base observer frame, while
the normalization \(v_p(p)=1\) fixes the edge ruler. Neither choice selects a
continued-fraction section, a task quotient, a fundamental domain, or a scalar
objective. Conversely, Ruban and Browkin are representative sections, not unit
frames or fundamental domains of the tree.

At fixed depth \(d\), the projective cylinders form the exact frontier

\[
S_d=\mathbb P^1(\mathbb Z/p^d\mathbb Z),
\qquad |S_d|=(p+1)p^{d-1}.
\]

A declared root-symmetric finite source gives each cylinder mass \(1/|S_d|\),
and those masses push consistently through parent reduction. Only after this
source and an explicit binary decoder are added does Huffman coding become a
well-posed downstream problem. Changing the source law while keeping the same
projective frontier changes the optimal Huffman tree, proving that geometry
does not choose the coding objective.

The finite selector audit additionally found zero backtracking and one common
input-directed ray on its bounded rational corpus. That is a finite evaluation
certificate, not a general ray theorem or Bellman optimum: the two selectors
still have different stopping depths and outcome semantics.

A subsequent finite control task now adds the structures that the route audit
lacked.  For each \(p\in\{3,5,7\}\), it declares the 182-input rational source,
depth-four stopping cylinder, horizon, a finite grammar of contact lifts, the
state \((n,\alpha,G,V,R)\), policy-independent exact/precision decoders, and
separate digit, tree-edge, digit-serialization, and decoder-payload rulers.
The grammar has at most two distinct rational actions per state.  Exact graph
exhaustion and set-valued Bellman recursion return replayable Pareto witnesses
for every frozen input.

This closes the previously open **task-local finite** selector-policy contract,
not the general selector problem.  Changed source weights reverse a conditional
expected-cost ranking, and digit-minimal versus decoder-minimal scalarizations
select different controllers on twelve \(p=3\) inputs.  Thus projective
geometry supplies the evaluation, stopping frontier, and edge ruler; it does
not choose the source or a scalar policy objective.  The matrix payload remains
necessary for decoder cost and the visited-set residual for cycle semantics.
Within one exact episode, the lattice value is derivable from \(G\) and the
current complete quotient is recoverable from \((G,\alpha_0)\); these are
problem-local redundancy certificates, not a general minimal-state theorem.

---

## 4. Translation table

| Mathematical object | Process interpretation |
| --- | --- |
| primitive \((q,v)\) history | physical process before observer quotienting |
| \(\pi(q,v)=(U,Y)\) | declared observer and first history jet |
| \((C_E,\omega)\) | task-visible quotient carrier marked by its clock |
| \(z=\int\omega\) | additive lifted clock / developing coordinate |
| \(\Lambda\) | kernel of periodic readout; cuts an analytic fundamental domain |
| \(t_0\) | local physical time frame; measures that domain |
| \(\mathbb C_z/\Lambda\) | completed elliptic quotient geometry |
| elliptic function | periodic decoder from lifted clock to visible state |
| Cartesian mark | task-visible residual erased by the carrier quotient |
| \(d\Omega=T\,dH\) | continuous action--history-domain coarea law |
| \(\lceil\log_2N_Q\rceil\) | finite exact continuation-memory lower bound |
| Bolza quotient | product-sign quotient after an additional metric sheet |
| \(G_n=M(a_0)\cdots M(a_n)\) | composable projective evaluation payload of a literal digit prefix |
| \([G_n\mathbb Z_p^2]\) | payload evaluated at the standard local-field lattice frame |
| \(\alpha_{n+1}\) | continuation residual in the exact projective decoder |
| \(\mathbb P^1(\mathbb Z/p^d\mathbb Z)\) | fixed-resolution projective-cylinder task frontier |
| \(|B_d|-|B_{d-1}|=|S_d|\) | exact discrete shell-increment calibration |
| binary prefix code | separately declared decoder/cost tree for a finite source |

This table is deliberately independent of any claim that an
Addition/Multiplication presentation is required or canonical.

---

## 5. Current claim boundary

### 5.1 Established in the declared calibrations

- exact finite continuation equivalence and minimal quotienting in the finite
  deterministic class;
- the pendulum Cartesian elimination, marked cubic, induced first-order flow,
  and clock form;
- the \(E=0\) period lattice and task-relative Cartesian sheet transport;
- dimensional transport by \(E_0,t_0,A_0\) and the moving-frame covariant
  action--period identity;
- the classical action--period coarea law in the pendulum family;
- exact finite residual bounds for the declared sheet tasks;
- the algebraic provenance of the Bolza model from two separately declared
  sheets;
- exact finite projective-lattice normal forms, parent refinement, sphere and
  ball counts, and the discrete shell-increment identity;
- exact rational Ruban/Browkin section-lift, reconstruction, cycle/termination,
  and bounded path certificates;
- exact finite root-symmetric cylinder mass transport and binary prefix-code
  decoding under the declared source task;
- exact finite selector-lift graph exhaustion, policy-independent terminal
  decoding, Pareto Bellman witnesses, and fixed-baseline comparison under the
  declared rational source, depth, horizon, and cost rulers.

### 5.2 Calibrated interpretations, not mother-object theorems

- the analytic Abel cover as a downstream model of lifted clock history;
- the period lattice as a task-kernel model and elliptic functions as periodic
  decoders;
- the common cocycle-like shape of transported clocks, resources, units,
  phases, and holonomies;
- action/coarea and finite frontier identities as pressure toward a broader
  process-volume theory;
- projective matrix evaluation and lattice orbits as a second problem-local
  model of payload between literal history and task quotient;
- the finite Bruhat--Tits ball as observer geometry rather than a generic
  history, cover, or coding object.

### 5.3 Open

- a canonical task-sufficient lift for a general non-Markovian process;
- a general theorem selecting the carrier for transported history payloads;
- intrinsic discovery of the pendulum normalization, flat ruler, cost
  cocycle, and stopping semantics from raw process data;
- a general relation between dimensional scale bundles, deck quotients, and
  stopping sections;
- a universal continuous/discrete time--space complexity law;
- a general relation among longitudinal refinement, transverse frontier
  growth, task memory, and continuous coarea;
- an infinite projective-boundary measure or entropy theorem forced by the
  finite root-symmetric source;
- a general or task-independent selector-policy state, action grammar,
  terminal decoder, and cost theorem beyond the executed finite rational
  corpus and depth-four stopping contract;
- generic-energy global pendulum reconstruction through all branch and
  degeneration boundaries;
- any theorem making the Bolza construction canonical or universal;
- Arithmetic Geometric Universality.

---

## 6. Red-team separations

Any proposed extension of this core must preserve the following distinctions
unless it proves a replacement theorem.

1. A visible graph's universal cover is not automatically the full history
   unfolding of a non-Markovian process.
2. A history tree, observer/evaluation tree, and coding tree are different; a
   Huffman tree optimizes a declared source only after probabilities,
   primitives, and a decoder are fixed.
3. Equal visible endpoints or finite contacts need not have equal futures.
4. A quotient carrier is not a decoder for information it has forgotten.
5. A section choosing quotient representatives is not a unit frame or a
   fundamental domain of an observer tree.
6. A unit frame does not select a deck kernel or fundamental domain.
7. A cover and lattice do not select a scalar word length or history cost; a
   lattice-basis shear or changed source law is an immediate red team.
8. A locally regular observer coordinate need not be a global algebraic chart;
   transporting a clock and transporting second-order dynamics have different
   jet obligations.
9. Continuous coarea, discrete shell growth, and finite continuation memory
   are not interchangeable meanings of “space”.
10. The Bolza product quotient is not the pendulum carrier.
11. An executable analytic or coding presentation does not by itself prove
    canonicality or universality.

---

## 7. Mathematical-understanding contract for future work

A substantial theory contribution should be expressible in the following
order before it proposes a new Theory Map noun:

```text
Primitive data
  What exists before the preferred representation?

Task and continuation semantics
  Which future distinctions must survive?

Construction
  What lift, quotient, transport, stopping section, completion, or decoder is applied?

Law
  Which equation, invariant, commuting diagram, universal property, or obstruction results?

Information contract
  What is preserved, forgotten, and reconstructible?

Covariance and units
  Under which presentation/frame changes is the statement invariant or covariant?

Scope and boundary
  Local/global, existence/uniqueness, degeneration, red team, and kill condition.

Evidence
  Proof, executable certificate, independent calibration, and conventional baseline.

Map effect
  Support, refine, split, connect, contradict, merge, deprecate, or unchanged.
```

If the contribution claims calculation, it must then supply the solver-plan
contract in `ENGINEERING_ARCHITECTURE.md`. Mathematical meaning and feasible
execution are coupled obligations, but neither may be silently substituted for
the other.

If these fields cannot yet be filled, the work may still be valuable T0
exploration, but it has not yet supplied a mathematical dependency for the
stable Theory Map or software ontology.

---

## 8. Relation to the current Theory Map

This document does not add a third stable axis or promote a generic history
payload API.  It clarifies the mathematical content that the emerging
task-covariant history-evaluation transversal must eventually carry:

```text
lift
  -> transported and unit-framed evaluation
  -> stopping / quotient / residual
  -> task-visible carrier
  -> analytic or complexity structure when justified
```

The pendulum supplies the first end-to-end continuous calibration of this
order. The local-field projective line supplies an independent finite discrete
calibration in which composable matrices, lattice evaluation, cylinder
quotients, continuation residuals, shell growth, and a downstream code tree
can be separated exactly.  Its finite Phase 6 task additionally carries that
chain through exact local lift actions, a shared decoder, and Pareto Bellman
selection, while source and scalar red teams block an intrinsic selector.
Together the calibrations refine the emerging transversal without selecting
its generic carrier or unifying continuous and discrete shadows.
`THEORY_MAP.md` should record that position and maturity; it should not replace
the equations and boundaries recorded here.

## References and executable evidence

- `docs/42-process-geometry-from-distinguishability.md`
- `docs/ENGINEERING_ARCHITECTURE.md`
- `docs/43-myhill-nerode-and-the-topological-threshold.md`
- `docs/53-process-volume-frontier-coarea-hypothesis.md`
- `docs/55-pendulum-lifted-clock-global-quotient.md`
- `docs/56-am-universal-history-recalibration.md`
- `docs/57-dimensional-resource-bundle-calibrations.md`
- `docs/62-task-covariant-complexity-coarea.md`
- `docs/64-first-principles-and-api-boundary-audit.md`
- `docs/65-effective-analysis-principle.md`
- `docs/vignettes/simple-pendulum.md`
- `sonnet/local-field-projective-process-geometry/README.md`
- `sonnet/local-field-projective-process-geometry/06-phase5-projective-cylinders-discrete-coarea-coding.md`
- `sonnet/local-field-projective-process-geometry/08-phase6-executable-selector-policy-bellman.md`
- `tests/research/test_pendulum_am_marked_carrier_bridge.py`
- `tests/research/test_pendulum_unit_history_fundamental_domain.py`
- `tests/research/test_local_field_projective_lattice_ball.py`
- `tests/research/test_padic_continued_fraction_selector_comparison.py`
- `tests/research/test_padic_selector_policy_bellman.py`
