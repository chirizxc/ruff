"""Fixer for intern().

intern(s) -> sys.intern(s)
"""

from typing import ClassVar, Literal

from .. import fixer_base

class FixIntern(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    order: ClassVar[Literal["pre"]]
    PATTERN: ClassVar[str]
    def transform(self, node, results): ...
