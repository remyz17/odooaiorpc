import enum
import typing as t

RpcDomainName: t.TypeAlias = t.Literal["common", "object", "db"]


class Protocol(str, enum.Enum):
    """
    Supported Http transport protocl
    """

    xmlrpc = "xmlrpc"
    jsonrpc = "jsonrpc"
