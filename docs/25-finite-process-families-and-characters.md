# Finite process families and characters: API closure after Translation / Dilation / A/M

**Status:** first stable finite-family API slice; deliberately stops before general representation theory.

## 1. Why this layer exists

Shakespeare already had two different process objects:

- `ProcessWord` for literal ordered histories;
- `ProcessSystem` / `ProcessFrame` for local infinitesimal generators.

Translation, dilation, and Galilean calibrations require a third object: a
**finite parameterized process family** such as

\[
T_a,\qquad S_b,\qquad B_v.
\]

The API added here is intentionally smaller than a group or harmonic-analysis
framework.  It records only the structures forced by the first calibration
sequence.

## 2. `ProcessFamily`

A `ProcessFamily` contains

\[
\boxed{\text{name} + \text{parameter composition law}}
\]

and optionally an identity/equivalence policy.

Examples:

\[
T_aT_b=T_{a+b},
\]

\[
S_aS_b=S_{ab}.
\]

The public object does **not** require inverses, topology, Haar measure, Lie
algebra, commutativity, or even a group structure.  Those are later capabilities
if future examples force them.

`FamilyStep` is a lightweight history token, so parameterized finite steps can
still participate in the existing history ontology without turning the family
itself into a word-rewriting system.

## 3. `ProcessCharacter`

The first response object is deliberately one-dimensional and SymPy-valued.
For a family with parameter composition `combine`, a response candidate `chi`
is tested by

\[
\chi(a\star b)=\chi(a)\chi(b).
\]

`verify_process_character` returns exact residual certificates on caller-supplied
symbolic/sample pairs.  It does not claim completeness over an unbounded domain.

### Translation calibration

For

\[
T_aT_b=T_{a+b},
\]

the familiar realization

\[
\chi_\xi(a)=e^{i\xi a}
\]

passes the same character law.  Fourier synthesis is not part of this API.

### Dilation calibration

For

\[
S_aS_b=S_{ab},\qquad a,b>0,
\]

the same API verifies

\[
\eta_\tau(a)=e^{i\tau\log a}=a^{i\tau}.
\]

Thus the multiplicative/Mellin calibration requires no second family or
character abstraction; only a backend simplifier respecting the positive-scale
logarithm law is supplied.

This is the first important closure result:

\[
\boxed{\text{Dilation I adds no new core API.}}
\]

## 4. `FamilyAction`

Addition and multiplication together require structure between two families.
For scales acting on translations,

\[
a:b\mapsto ab.
\]

`FamilyAction` stores exactly such parameter transport.  Its bounded verifier
checks two laws:

1. each acting parameter preserves the target-family composition;
2. composition in the acting family agrees with repeated parameter transport.

No semidirect-product or affine-group class is introduced.

## 5. Character transport and the A/M obstruction

A `FamilyAction` on target parameters induces transport of target-family
characters by pullback.

For

\[
\chi_\xi(b)=e^{i\xi b},
\qquad
b\mapsto ab,
\]

one gets

\[
\chi_\xi(ab)=\chi_{a\xi}(b).
\]

So multiplication acts on the additive response label:

\[
\boxed{\xi\mapsto a\xi.}
\]

`character_invariance_residual` measures whether a scalar target character is
unchanged by that action.  For a generic nonzero `xi` and nontrivial scale this
residual is nonzero.

This deliberately exposes a limitation:

> one-dimensional scalar characters are not sufficient to encode the full A/M
> interaction while preserving a nontrivial translation character.

The API stops at the obstruction.  It does not yet introduce operator-valued
representations, Hilbert spaces, wavelets, or noncommutative spectra.

## 6. Independent mechanics acceptance: Galilean I

The first independent test uses spacetime translations

\[
N_{(a,s)}N_{(b,r)}=N_{(a+b,s+r)}
\]

and boosts

\[
B_vB_w=B_{v+w}.
\]

Boosts act on spacetime-translation parameters by the shear

\[
(a,s)\mapsto(a+vs,s).
\]

No API change is required even though the target parameter space is now
2-dimensional rather than scalar.

A translation character

\[
\chi_{p,E}(a,s)=e^{i(pa-Es)}
\]

is transported to

\[
e^{i(pa-(E-vp)s)}.
\]

So the bare response labels transform as

\[
(p,E)\mapsto(p,E-vp).
\]

This is an important acceptance result:

\[
\boxed{
\text{ProcessFamily + ProcessCharacter + FamilyAction}
\text{ survives a nontrivial mechanics shear unchanged.}
}
\]

## 7. The Galilean failure is retained, not patched

The physical Galilean momentum-energy transformation contains mass-dependent
terms.  Those terms are absent from the bare spacetime-family action above.

This is intentional.  The current vignette therefore records:

**unresolved residual:** the finite visible action does not contain the central
mass information that appears in the Hamiltonian/projective description.

A later Galilean vignette may find pressure for a central residual or cocycle,
for example through the classical generator relation

\[
\{K,P\}=m.
\]

But this API slice does not introduce `ProcessCocycle`, `CentralExtension`, or a
projective-representation hierarchy on the strength of one example.

## 8. Current public contract

The finite-family layer therefore closes at

```text
ProcessFamily
FamilyStep
ProcessCharacter
CharacterVerification
FamilyAction
FamilyActionVerification
verify_process_character(...)
verify_family_action(...)
transport_process_character(...)
character_invariance_residual(...)
```

and no further.

In conceptual form:

\[
\boxed{
\text{finite operation law}
\to
\text{scalar response law}
\to
\text{family action}
\to
\text{response-space transport / obstruction}.
}
\]

## 9. What is deliberately not in the API

There is currently no public:

- `Group` / `LieGroup` hierarchy;
- general `Representation` / `IrreducibleRepresentation` hierarchy;
- `Spectrum` or `EigenMode` ontology;
- `FourierTransform`, `MellinTransform`, or `WaveletTransform` object;
- topology or measure protocol;
- automatic character discovery/completeness theorem;
- central extension/cocycle object.

Each of these may become justified later, but only after an executable vignette
requires it.

## 10. Research ledger

**Primitive assumptions.** Explicit finite family-composition laws, scalar
symbolic response candidates, and explicit actions between family parameter
spaces.

**Forbidden structures.** General group/representation theory, spectral
ontology, Fourier/Mellin/wavelet synthesis, and Galilean central-extension
machinery.

**Discovered structure.** Additive and multiplicative laws share one family and
character API; A/M requires only a family action and exposes a scalar-response
obstruction; Galilean shear reuses the same API unchanged.

**New reusable abstraction.** `ProcessFamily`, `ProcessCharacter`, and
`FamilyAction`, with bounded exact verification/transport utilities.

**Unresolved manual choice.** What response object should replace scalar
characters when the A/M obstruction matters, and how should the Galilean mass
residual be represented if it reappears in an independent calibration?
