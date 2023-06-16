import typing as t

from odooaiorpc import const

from .base import BaseProtocol
from .jsonrpc import JsonRpcProtocol
from .xmlrpc import XmlRpcProtocol


def pick_preferred_protocol(protocol: const.Protocol) -> t.Type[BaseProtocol]:
    if protocol == const.Protocol.jsonrpc:
        return JsonRpcProtocol
    return XmlRpcProtocol


__all__ = (
    "BaseProtocol",
    "JsonRpcProtocol",
    "XmlRpcProtocol",
    "pick_preferred_protocol",
)
