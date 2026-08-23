"""Compatibility shim for the pre-refactor finite-family module path.

New code should import from ``process_geometry.process.finite``. The
implementation physically lives under that semantic namespace.
"""

from .process.finite.families import (
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
]
