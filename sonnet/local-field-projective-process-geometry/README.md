# Local-field projective process geometry

**Status:** T0 research-local calibration; Phase 1 finite standard-root
lattice ball complete; no infinite Bruhat--Tits completion, no preferred
\(p\)-adic continued fraction, and no Experimental or Public API proposal.

This Sonnet asks whether one rational arithmetic history can acquire two
genuinely different but strictly comparable geometries when the observer
changes place:

\[
\text{rational Addition/Multiplication/inversion histories}
\longrightarrow
\begin{cases}
|\cdot|_\infty & \text{Archimedean scale and real continued-fraction coding},\\
|\cdot|_p & \text{valuation scale and non-Archimedean refinement}.
\end{cases}
\]

The algebraic carrier is already forced by the bilateral AEG lineage.  Pure
left-slot histories remain in the affine/Borel sector stabilizing infinity;
right-slot division introduces inversion and the full projective language.
The new question is not whether \(PGL_2(K)\) can be written down, but whether
the current Process Geometry foundation can explain how an observer, ruler,
and task select an effective local-field presentation without erasing history
or declaring a global canonical form by fiat.

Read in order:

1. [00-problem-frontier.md](00-problem-frontier.md) freezes the primitive
   audit, observer semantics, hypotheses, forbidden imports, and kill
   conditions;
2. [01-phase0-finite-certificates.md](01-phase0-finite-certificates.md)
   records the exact first certificates, the digit-section red team, and the
   next evidence gates;
3. [02-phase1-finite-lattice-ball.md](02-phase1-finite-lattice-ball.md)
   constructs the complete finite lattice-class ball, embeds the earlier
   residues as an affine contact chart, and records the inversion red team;
4. [test_local_field_projective_process_geometry.py](../../tests/research/test_local_field_projective_process_geometry.py)
   and [test_local_field_projective_lattice_ball.py](../../tests/research/test_local_field_projective_lattice_ball.py)
   are the seconds-scale executable arguments.

## Current result

Phase 0 proves only the following finite or algebraic facts:

- the same rational multiplication history \(1\mapsto p^n\) escapes in the
  Archimedean ruler and approaches zero in the \(p\)-adic ruler;
- residue observations modulo \(p^n\) form a nested \(p\)-ary refinement;
- Addition preserves \(p\)-adic separation while Multiplication transports it
  by the exact valuation cocycle;
- left affine maps fix the projective point at infinity and right inversion
  exchanges zero with infinity;
- finite right-reciprocal histories lower exactly to chronological
  \(2\times2\) matrix products and continued-fraction convergents;
- Möbius maps transport \(p\)-adic resolution by an exact denominator law;
- standard and balanced digit sections reconstruct the same finite semantic
  residue but are preferred by different cost rulers.

The last item is a negative certificate against an observer-free claim of
canonical digits.  It is not evidence against task-relative canonicalization.

Phase 1 adds a classical but exact lattice-class calibration. Primitive
covectors modulo \(p^n\), quotiented by units, enumerate the radius-\(n\)
sphere as

\[
\mathbb P^1(\mathbb Z/p^n\mathbb Z)
=
\{[r:1]\}\sqcup\{[1:pt]\}.
\]

Parent reduction builds the complete standard-root ball with the expected
\((p+1)\)-regular interior. The Phase 0 residue \(r\bmod p^n\) is recovered as
the affine class \([r:1]\), with the exact contact law

\[
x\equiv r\pmod {p^n}
\iff
(1,-x)\in L_{[r:1]}.
\]

The missing \(p^{n-1}\) infinity-chart vertices are necessary: right inversion
exchanges them with affine residues divisible by \(p\). Thus the affine
residue tree is a task-sufficient patch for integral observation, but is not
closed under the bilateral projective alphabet.

## Claim boundary

Phase 1 now constructs the complete **finite ball around the standard
vertex**, using normalized representatives of lattice homothety classes. It
does not construct the infinite tree or its boundary completion. The
continued-fraction certificate still concerns finite right-reciprocal
histories; it does not select among competing \(p\)-adic digit algorithms or
claim their convergence, finiteness, or Lagrange periodicity.

At this stage the study **supports** H0/H1 and **refines** its H2
interpretation: observer residue refinement is an affine chart, while
inversion forces projective completion. It leaves the Theory Map file
unchanged. The residue-resolution tower remains horizontal observer
refinement, not a vertical arithmetic process-rank transition.
