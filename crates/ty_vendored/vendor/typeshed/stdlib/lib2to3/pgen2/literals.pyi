"""
Safely evaluate Python string literals without using eval().
"""

from re import Match

simple_escapes: dict[str, str]

def escape(m: Match[str]) -> str: ...
def evalString(s: str) -> str: ...
def test() -> None: ...
