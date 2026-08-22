"""Evidence-bearing transformations between process presentations.

Mathematical pressure
---------------------
Three independent research calibrations now force the same minimal shape.

* KdV: a tau presentation and a parametric scattering-history presentation can
  encode the same pair/three-body interaction data, while a locally confluent
  rewrite can still be incomplete for the tau task.
* Resistor networks: Schur/Y-Delta transformations can produce syntactically
  different graphs with exactly the same declared boundary response.
* Braids: Markov stabilization can preserve closure semantics while changing
  braid index and therefore the dimension/type of the chosen representation.

The shared object is not a universal rewrite rule.  It is an evidence-bearing
arrow between a source presentation and a target presentation, whose validity is
always relative to an explicitly declared task semantics.

Boundary
--------
``PresentationMorphism`` deliberately does *not* define:

* a universal equality or verification method;
* composition, inverses, identities, or a category/groupoid structure;
* a normal-form relation;
* a requirement that source and target have the same Python type;
* a requirement that certificates be exact rather than numerical/bounded.

Those structures should be promoted only when further independent calibrations
show what information composition and verification must retain.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

SourceT = TypeVar("SourceT")
TargetT = TypeVar("TargetT")
TaskSemanticsT = TypeVar("TaskSemanticsT")
CertificateT = TypeVar("CertificateT")


@dataclass(frozen=True)
class PresentationMorphism(
    Generic[SourceT, TargetT, TaskSemanticsT, CertificateT]
):
    """A task-relative, certificate-carrying presentation transformation.

    ``source`` and ``target`` may be entirely different representation types.
    ``task_semantics`` records what meaning is claimed to be preserved.
    ``certificate`` is caller-defined evidence for that claim; Shakespeare does
    not interpret it generically.  ``witness`` may record a rewrite trace,
    construction history, parameter map, or other provenance for how the target
    was obtained.
    """

    source: SourceT
    target: TargetT
    task_semantics: TaskSemanticsT
    certificate: CertificateT
    witness: object | None = None
    label: str = ""


__all__ = ["PresentationMorphism"]
