"""Finite parameterized process structure.

This namespace groups families, scalar responses, actions, and additive central
composition residuals.  It deliberately stops before a universal group,
representation, cohomology, topology, or measure hierarchy.
"""

from ..central import (
    CocycleVerification,
    ProcessCocycle,
    central_commutator_residual,
    verify_process_cocycle,
)
from ..families import (
    CharacterVerification,
    FamilyAction,
    FamilyActionVerification,
    FamilyStep,
    ProcessCharacter,
    ProcessFamily,
    character_invariance_residual,
    transport_process_character,
    verify_family_action,
    verify_process_character,
)

__all__ = [
    "ProcessFamily",
    "FamilyStep",
    "ProcessCharacter",
    "CharacterVerification",
    "verify_process_character",
    "FamilyAction",
    "FamilyActionVerification",
    "verify_family_action",
    "transport_process_character",
    "character_invariance_residual",
    "ProcessCocycle",
    "CocycleVerification",
    "verify_process_cocycle",
    "central_commutator_residual",
]
