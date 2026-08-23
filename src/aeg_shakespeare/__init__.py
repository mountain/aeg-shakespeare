"""Deprecated compatibility namespace for Process Geometry.

Use ``process_geometry`` for all new code.  This package exists only to keep the
0.0.3-era ``aeg_shakespeare`` import path working during the namespace migration.
All implementation is owned by ``process_geometry``; this module aliases the
canonical module tree rather than maintaining a second copy.
"""

from __future__ import annotations

import importlib
import pkgutil
import sys
import warnings

import process_geometry as _canonical

warnings.warn(
    "aeg_shakespeare is a deprecated compatibility namespace; use process_geometry",
    DeprecationWarning,
    stacklevel=2,
)

# Register the complete canonical module tree under the historical prefix.  This
# preserves object identity for deep imports such as
# ``aeg_shakespeare.process.history.ProcessWord`` while keeping one source owner.
for _info in pkgutil.walk_packages(
    _canonical.__path__, prefix=_canonical.__name__ + "."
):
    _module = importlib.import_module(_info.name)
    _legacy_name = __name__ + _info.name[len(_canonical.__name__) :]
    sys.modules.setdefault(_legacy_name, _module)

process = _canonical.process
presentation = _canonical.presentation
discovery = _canonical.discovery
analysis = _canonical.analysis
__version__ = _canonical.__version__
__all__ = list(_canonical.__all__)


def __getattr__(name: str):
    return getattr(_canonical, name)


def __dir__():
    return dir(_canonical)
