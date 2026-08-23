"""History rewriting, task signatures, and finite history geometry."""

from ..history_geometry import (
    BoundaryProfile,
    PrefixCode,
    PrefixCodeMetrics,
    boundary_profile,
    history_depth,
    huffman_prefix_code,
)
from ..rewrite import (
    RewriteResult,
    RewriteStep,
    WordRewriteRule,
    normalize_word,
    rewrite_once,
)
from ..signature import (
    ProcessJetSignature,
    enumerate_process_words,
    histories_task_equivalent,
    history_process_jet_signature,
    process_jet_signature,
    signatures_equivalent,
)

__all__ = [
    "RewriteResult",
    "RewriteStep",
    "WordRewriteRule",
    "normalize_word",
    "rewrite_once",
    "ProcessJetSignature",
    "enumerate_process_words",
    "histories_task_equivalent",
    "history_process_jet_signature",
    "process_jet_signature",
    "signatures_equivalent",
    "BoundaryProfile",
    "PrefixCode",
    "PrefixCodeMetrics",
    "boundary_profile",
    "history_depth",
    "huffman_prefix_code",
]
