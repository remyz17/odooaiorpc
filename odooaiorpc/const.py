import enum


class Protocol(str, enum.Enum):
    """
    Supported Http transport protocl
    """

    xmlrpc = "xmlrpc"
    jsonrpc = "jsonrpc"
