"""
Constants and membership tests for ASCII characters
"""

from typing import TypeVar

_CharT = TypeVar("_CharT", str, int)

NUL: int
SOH: int
STX: int
ETX: int
EOT: int
ENQ: int
ACK: int
BEL: int
BS: int
TAB: int
HT: int
LF: int
NL: int
VT: int
FF: int
CR: int
SO: int
SI: int
DLE: int
DC1: int
DC2: int
DC3: int
DC4: int
NAK: int
SYN: int
ETB: int
CAN: int
EM: int
SUB: int
ESC: int
FS: int
GS: int
RS: int
US: int
SP: int
DEL: int

controlnames: list[int]

def isalnum(c: str | int) -> bool: ...
def isalpha(c: str | int) -> bool: ...
def isascii(c: str | int) -> bool: ...
def isblank(c: str | int) -> bool: ...
def iscntrl(c: str | int) -> bool: ...
def isdigit(c: str | int) -> bool: ...
def isgraph(c: str | int) -> bool: ...
def islower(c: str | int) -> bool: ...
def isprint(c: str | int) -> bool: ...
def ispunct(c: str | int) -> bool: ...
def isspace(c: str | int) -> bool: ...
def isupper(c: str | int) -> bool: ...
def isxdigit(c: str | int) -> bool: ...
def isctrl(c: str | int) -> bool: ...
def ismeta(c: str | int) -> bool: ...
def ascii(c: _CharT) -> _CharT: ...
def ctrl(c: _CharT) -> _CharT: ...
def alt(c: _CharT) -> _CharT: ...
def unctrl(c: str | int) -> str: ...
