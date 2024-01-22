import typing
from typing import Generic, TypeAlias, TypeVar

from puyapy import Account, UInt64

_T = TypeVar("_T")

AccountIndex: TypeAlias = UInt64 | int

class LocalState(Generic[_T]):
    def __init__(self, type_: type[_T], /) -> None: ...
    def __getitem__(self, account: Account | AccountIndex) -> _T: ...
    def __setitem__(self, account: Account | AccountIndex, value: _T) -> None: ...
    def __delitem__(self, account: Account | AccountIndex) -> None: ...
    def __contains__(self, account: Account | AccountIndex) -> bool: ...
    def get(self, account: Account | AccountIndex, default: _T) -> _T: ...
    def maybe(self, account: Account | AccountIndex) -> tuple[_T, bool]: ...

class GlobalState(Generic[_T]):
    @typing.overload
    def __init__(self, type_: type[_T], /) -> None: ...
    @typing.overload
    def __init__(self, initial_value: _T, /) -> None: ...
    @property
    def value(self) -> _T: ...
    @value.setter
    def value(self, value: _T) -> None: ...
    @value.deleter
    def value(self) -> None: ...
    def __bool__(self) -> bool: ...
    """Returns True if the key has a value set, regardless of the truthiness of that value"""
    def get(self, default: _T) -> _T: ...
    def maybe(self) -> tuple[_T, bool]: ...