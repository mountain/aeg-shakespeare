"""Process Geometry: process-first representation and analysis infrastructure.

The public surface is organized into four semantic namespaces:

``process`` -> what the process is,
``presentation`` -> how process history is represented and compared,
``discovery`` -> how better presentations are searched,
``analysis`` -> what analytic/geometric language a presentation supports.

Legacy root-level symbol imports from the early 0.0.x research-preview API remain
available lazily during the namespace migration, but they are no longer part of
``__all__`` and emit ``DeprecationWarning``.
"""

from __future__ import annotations

import importlib
import warnings

from . import analysis, discovery, presentation, process

__version__ = "0.0.5.dev0"

__all__ = [
    "process",
    "presentation",
    "discovery",
    "analysis",
    "__version__",
]


def __getattr__(name: str):
    legacy = importlib.import_module("._legacy_api", __name__)
    if name in getattr(legacy, "__all__", ()):
        warnings.warn(
            f"{__name__}.{name} is a legacy root-level import; "
            "use the process/presentation/discovery/analysis namespaces instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return getattr(legacy, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(set(__all__))
