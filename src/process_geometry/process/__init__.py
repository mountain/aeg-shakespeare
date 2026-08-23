"""Process ontology: histories, finite process families, and local generators."""

from . import finite, history, local
from .finite import ProcessFamily
from .history import ProcessWord
from .local import ProcessFrame, ProcessSystem

__all__ = [
    "history",
    "finite",
    "local",
    "ProcessWord",
    "ProcessFamily",
    "ProcessSystem",
    "ProcessFrame",
]
