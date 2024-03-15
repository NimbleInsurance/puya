# This file is auto-generated, do not modify
# flake8: noqa
# fmt: off
import typing

import puyapy


class Greeter(puyapy.arc4.ARC4Client, typing.Protocol):
    @puyapy.arc4.abimethod
    def test_method_selector_kinds(
        self,
        app: puyapy.Application,
    ) -> None: ...

    @puyapy.arc4.abimethod
    def test_arg_conversion(
        self,
        app: puyapy.Application,
    ) -> None: ...

    @puyapy.arc4.abimethod
    def test_15plus_args(
        self,
        app: puyapy.Application,
    ) -> None: ...

    @puyapy.arc4.abimethod
    def test_void(
        self,
        app: puyapy.Application,
    ) -> None: ...

    @puyapy.arc4.abimethod
    def test_ref_types(
        self,
        app: puyapy.Application,
        asset: puyapy.Asset,
    ) -> None: ...