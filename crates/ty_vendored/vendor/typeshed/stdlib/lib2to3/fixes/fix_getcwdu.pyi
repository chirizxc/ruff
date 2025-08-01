"""
Fixer that changes os.getcwdu() to os.getcwd().
"""

from typing import ClassVar, Literal

from .. import fixer_base

class FixGetcwdu(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    def transform(self, node, results) -> None: ...
