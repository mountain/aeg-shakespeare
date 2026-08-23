"""History rewriting, task distinguishability, and finite history geometry."""

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
    TaskContinuationSignature,
    enumerate_process_words,
    histories_task_equivalent,
    history_process_jet_signature,
    history_task_continuation_signature,
    process_jet_signature,
    signatures_equivalent,
    task_continuation_signature,
)

__all__ = [
    "RewriteResult",
    "RewriteStep",
    "WordRewriteRule",
    "normalize_word",
    "rewrite_once",
    "TaskContinuationSignature",
    "task_continuation_signature",
    "history_task_continuation_signature",
    "enumerate_process_words",
    "histories_task_equivalent",
    "signatures_equivalent",
    # Historical 0.0.x aliases; ``jet`` is reserved for later differential use.
    "ProcessJetSignature",
    "process_jet_signature",
    "history_process_jet_signature",
    "BoundaryProfile",
    "PrefixCode",
    "PrefixCodeMetrics",
    "boundary_profile",
    "history_depth",
    "huffman_prefix_code",
]