"""Optional function-theory layers built on Shakespeare process structures.

These modules are downstream representations, not the universal process
ontology.  ``am`` is the first concrete layer; other function theories can
coexist without changing the core history/grammar/search interfaces.
"""

from .am import AMFunctionTheory, AMPowerWeight, affine_am_frame

__all__ = ["AMFunctionTheory", "AMPowerWeight", "affine_am_frame"]
