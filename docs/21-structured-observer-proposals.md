# Structured observable proposals: one pairing before any vector theory

**Status:** Experimental; first structured-construction calibration, currently
forced end-to-end only by the pendulum and deliberately narrower than a typed
mathematical theory protocol.

## 1. Why this layer exists

The first two pendulum discovery stages removed two manual choices:

1. the energy was no longer supplied but discovered as a polynomial first integral;
2. inside the declared coordinate family `(qx,qy)`, algebraic-image/Pareto
   search selected `qy` rather than being told to prefer it.

A prior choice remained: why should the observable family be the two coordinate
components at all?

The primitive pendulum description contains more structure than four unrelated scalar assignments.  It contains a position `q`, a velocity `v`, a fixed gravity direction `e`, and a Euclidean pairing.  The next experiment asks whether that small amount of structure can propose scalar observables before coordinates become the representation ontology.

## 2. Minimal abstraction only

This stage intentionally does **not** define a vector-space protocol.

It introduces only:

- `PairableAtom(name, components, sort)` — a named structured atom with a finite backend realization;
- `PairingSpec` — one caller-declared scalar pairing on a common sort;
- `PairingConstruction` — the retained recipe `pair(left,right)`;
- `StructuredObservableProposal` — the recipe together with its scalar backend lowering;
- `generate_pairing_observables` — bounded depth-one proposal generation;
- `nonstationary_observable_proposals` — a task filter for the present goal of finding an evolving scalar observable.

These names are owned by `process_geometry.experimental`. The historical
`process_geometry.discovery.structured` imports are compatibility shims, not
the stable Discovery surface.

No addition law, scalar multiplication, linear independence, basis, norm, matrix algebra, spectral theorem, or Fourier transform is assumed.

The point is methodological: later examples should force those structures if they are genuinely reusable.

## 3. Construction before lowering

For the pendulum calibration, the caller supplies

\[
q=(q_x,q_y),\qquad v=(v_x,v_y),\qquad e=(0,1)
\]

as three atoms of one pairable sort and supplies the Euclidean pairing.

Because the pairing is declared symmetric, the depth-one grammar contains exactly

\[
\langle q,q\rangle,
\langle q,v\rangle,
\langle q,e\rangle,
\langle v,v\rangle,
\langle v,e\rangle,
\langle e,e\rangle.
\]

Only afterwards are these lowered to the scalar backend:

\[
q_x^2+q_y^2,
\quad q_xv_x+q_yv_y,
\quad q_y,
\quad v_x^2+v_y^2,
\quad v_y,
\quad 1.
\]

Thus the observable whose backend expression is `qy` retains the construction identity

```text
pair(q,e)
```

rather than being identified ontologically with one coordinate symbol.

## 4. Task filtering is not construction equality

On the rod/tangency/energy leaf,

\[
q_x^2+q_y^2=1,
\qquad
q_xv_x+q_yv_y=0,
\qquad
v_x^2+v_y^2+2q_y=K,
\]

the constructions

\[
\langle q,q\rangle,
\langle q,v\rangle,
\langle e,e\rangle
\]

have zero process derivative modulo the constraints.

They are therefore insufficient for the **current task** of finding one
evolving first-order observable. They are not deleted from the proposal grammar
and no new equality law is inferred.

The surviving candidates are

\[
\langle q,e\rangle,
\qquad
\langle v,v\rangle,
\qquad
\langle v,e\rangle.
\]

## 5. Pendulum III

The three surviving constructions enter the public first-order
observable-presentation search.

For

\[
U=\langle q,e\rangle=q_y,
\qquad
Y=DU=v_y,
\]

exact elimination gives

\[
\boxed{Y^2=(K-2U)(1-U^2).}
\]

The speed-squared observable also closes algebraically but requires a more
expensive backend first-order pair; the vertical-velocity observable gives a
substantially larger algebraic relation. Under the transparent current
structural cost, `pair(q,e)` is therefore the unique Pareto candidate.

The important change is not the classical result.  It is the input boundary:

```text
previous stage:
    caller -> (qx,qy) -> algebraic-image search -> qy

current stage:
    caller -> (q,v,e,pairing)
           -> structured scalar proposals
           -> task filter
           -> algebraic-image search
           -> pair(q,e)
           -> backend shadow qy
```

## 6. Five-line research ledger

**Primitive assumptions.** Three named pairable atoms, their finite component realizations, one common sort, one symmetric Euclidean pairing, the previously discovered invariant leaf.

**Forbidden structures.** Preferred coordinate, angle, vector-space theory, basis-change machinery, spectrum, Fourier analysis, elliptic functions, target cubic.

**Discovered structure.** A six-element structured scalar proposal grammar;
three nonstationary candidates; `pair(q,e)` as the unique default Pareto
first-order algebraic-image presentation.

**Experimental record.** Depth-one structured pairing construction with an
explicit recipe and separate backend lowering; no stable grammar is claimed.

**Unresolved manual choice.** The atoms `q,v,e`, their common pairable sort, and the Euclidean pairing are still supplied.  Independent examples must decide which parts deserve a broader algebraic abstraction.

## 7. Why we stop here

It would be easy to generalize this file into a large typed IR or a universal mathematical-domain protocol.  That is explicitly not the current goal.

The next calibration is the harmonic oscillator.  There the new pressure is different: a finite process grammar closes under **addition and scalar combination**.  If that example requires a reusable additive-module abstraction, it should be introduced there and compared against this pairing construction afterwards.

This keeps the development order empirical:

\[
\text{example}\to\text{failure/pressure}\to\text{minimal abstraction}\to\text{next example}.
\]
