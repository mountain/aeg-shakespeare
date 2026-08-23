# Canonical completion of marked process carriers — T1 theory record

**Theory record:** TR-0001  
**Status:** T1 — Precise Conjecture  
**Role:** foundational candidate  
**Code/API status:** no generic completion API; existing algebraic/Abelian code remains concrete analysis machinery  
**Map effect:** candidate connection inside H4 / global analysis; **does not yet modify Core Theory**

This record is intentionally conservative. The pendulum, genus hierarchy, Abelian-history, and observer-quotient work now suggest a larger structural possibility, but the evidence does not justify promoting that possibility into a framework law or package ontology.

Relevant current repository evidence includes:

- [`08-function-theory-genus-hierarchy.md`](08-function-theory-genus-hierarchy.md);
- [`13-abelian-history-periods.md`](13-abelian-history-periods.md);
- [`18-abel-jacobi-history-quotient.md`](18-abel-jacobi-history-quotient.md);
- [`20-observer-quotient-selection.md`](20-observer-quotient-selection.md);
- [`36-classical-reexpression-audit.md`](36-classical-reexpression-audit.md).

---

## 1. Claim under investigation

A class of process reductions appears to produce not merely an algebraic relation but a **marked process carrier**

\[
(C,D,\omega),
\qquad
\omega(D)=1,
\]

where:

- \(C\) is an algebraic or geometric carrier produced after declared constraint / invariant / observer reduction;
- \(D\) is the induced process direction on that carrier, at least locally or in its function field;
- \(\omega\) is a distinguished process differential whose pullback is the local process clock.

The candidate larger chain is

\[
\text{process}
\longrightarrow
\text{task-sufficient quotient / carrier}
\longrightarrow
(C,D,\omega)
\longrightarrow
\text{global period / obstruction data}
\longrightarrow
\text{group or completion layer}
\longrightarrow
\text{uniformizing process functions}.
\]

The T1 conjecture is **not** that this chain already exists canonically for every Process Geometry object. The conjecture is that there may be a mathematically natural class of inputs and equivalences for which the later arrows become canonical or minimal in a precise sense.

---

## 2. Existing concrete pressure

### 2.1 Pendulum observable quotient

The pendulum discovery line produces a first-order observable carrier of the form

\[
Y^2=P(U),
\qquad
Y=DU.
\]

The associated differential

\[
\omega=\frac{dU}{Y}
\]

satisfies

\[
\omega(D)=1.
\]

Thus the algebraic relation is not only a static curve: it carries a distinguished local process clock.

### 2.2 Period obstruction

The Abelian-history line shows that closed state return may carry a nonzero integrated history residual. The local clock therefore need not descend to a global single-valued coordinate on the reduced carrier.

This creates genuine pressure for a separate global-completion layer rather than treating a local quadrature as the end of the theory.

### 2.3 Genus pressure

The even-power oscillator calibration already distinguishes generic genus zero, one, and higher-genus algebraic quotients. The higher-genus work produces multiple natural Abelian differential channels and higher-rank homology data.

This suggests—but does not prove—that the dimension and form of a useful global completion may be forced by the marked carrier rather than chosen from a catalogue of special functions.

---

## 3. Competing hypotheses

The repository should keep several explanations alive until experiments distinguish them.

### H-A — Problem-local function theory

Each classical integrable problem happens to admit its own useful function theory. The common process-first narrative is explanatory but does not define a reusable completion mechanism.

### H-B — Marked-carrier hierarchy

The stable object is \((C,D,\omega)\) or a related marked geometric carrier. Genus, singularities, punctures, and period data classify useful analytic languages, but there is no further universal completion object required by Process Geometry.

### H-C — Canonical completion

For an admissible class of marked process carriers, there exists a canonical or minimal global completion under a precisely declared equivalence / universal property, and process-adapted function theory is a coordinate realization or inversion of that completion.

**Current governance status:** H-C is the motivating T1 conjecture. H-A and H-B remain live alternatives.

---

## 4. Required structure and scope

Before H-C can be promoted, the input class must specify at least:

1. whether the process is algebraic, analytic, Hamiltonian, integrable, or merely admits a finite algebraic observable closure;
2. what task or observer semantics justify the quotient;
3. whether \(D\) is globally regular, meromorphic, or only rational on the carrier;
4. whether \(\omega\) is holomorphic, meromorphic, logarithmic, or another declared differential type;
5. what singularities / punctures / boundary data belong to the marked object;
6. what class of representation changes counts as admissible;
7. what information about the original process is intentionally forgotten.

Until these are fixed, the word **canonical** is only shorthand for a research target.

---

## 5. Information contract

### Candidate preserved structure

A successful completion should preserve enough data to recover, for the declared task:

- the reduced process direction;
- the process clock represented by \(\omega(D)=1\);
- global period / monodromy information relevant to state continuation;
- declared invariants of the marked carrier.

### Known or expected information loss

The current observable-quotient machinery may forget:

- discrete state branches;
- gauge/lift information;
- noncommutative ordered process history;
- distinctions irrelevant to the selected observer/task.

A commutative global completion must not be presented as a complete ontology of the original process unless reconstruction of those distinctions is separately proved.

---

## 6. Controlled vocabulary

### `canonical`

**Not yet earned globally.** Promotion requires a uniqueness statement under a declared equivalence or a genuine universal property.

### `completion`

Currently means a candidate enlargement needed to globalize/linearize the marked process representation. It does **not** yet mean one generic Process Geometry `Completion` object.

### `forced`

Not currently claimed. Existing examples show pressure, not exclusion of all competing adequate representations.

### `minimal`

Not currently claimed. A future statement must name the preorder, dimension criterion, information order, presentation cost, or universal property under which minimality is meant.

---

## 7. Kill conditions

The current H-C formulation must be rejected, split, or materially weakened if any of the following survives careful audit:

1. **Observer nonuniqueness:** equally admissible task-sufficient observers produce marked carriers whose proposed completions have no declared natural equivalence.
2. **Clock nonnaturality:** an allowed presentation change does not preserve \(\omega\) up to the declared normalization/equivalence.
3. **Wrong boundary behavior:** degeneration of a calibrated process does not approach the boundary completion predicted by the theory.
4. **Higher-genus failure:** a higher-genus calibration has a natural process representation whose required global linearization is not captured by the proposed completion class.
5. **Noncommutative necessity:** task-relevant ordered history cannot be reconstructed or separately represented after the proposed commutative completion.
6. **Nonintegrable false positive:** the theory manufactures a completion for a process where no adequate finite/global linearization exists, without recording the obstruction as failure data.
7. **Dominated representation:** a substantially smaller task-sufficient representation exists and the proposed completion has no universal/minimal property explaining why it remains canonical.

A counterexample to universality is not automatically a failure of the local marked-carrier theory. It may instead force a split between H-B and H-C.

---

## 8. T1 -> T2 promotion plan

Before promotion to T2, require a deliberately heterogeneous calibration set.

### Positive / boundary calibrations

- a genus-zero case where the local/global clock structure is elementary;
- the generic pendulum genus-one carrier;
- a different genus-one system such as the quartic oscillator;
- a higher-genus case such as the sextic oscillator;
- at least one singular/degenerate limit where the carrier changes type.

### Negative controls

At least one of:

- a nonconservative process with no invariant energy leaf;
- a nonintegrable process where first-order algebraic closure fails or is inadequate;
- a task that requires history information known to be lost by the observable quotient.

### Comparison obligation

The calibration must compare at least H-A, H-B, and H-C rather than only accumulating evidence for H-C.

---

## 9. No current software promotion

This theory record creates **no immediate generic API requirement**.

In particular, it does not justify adding public or experimental classes named:

```text
CanonicalCompletion
GeneralizedJacobian
ProcessJacobian
Uniformization
GlobalProcessGroup
```

Existing concrete algebraic and Abelian modules should remain concrete until the theory identifies a repeated forced distinction and the software governance in [`GOVERNANCE.md`](GOVERNANCE.md) is independently satisfied.

The intended discipline is:

```text
T1 theory hypothesis
    -> red-team calibration
    -> possible T2 theory
    -> only then consider a minimal Experimental software probe
```

---

## 10. Promotion criterion in one sentence

> Promote this line only when independent processes and explicit failure cases show that the same marked-carrier-to-global-completion role is being forced from different mathematical directions, and when `canonical` can be replaced by a precise uniqueness, naturality, obstruction, or universal-property statement.
