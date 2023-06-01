import enum


class Transport(str, enum.Enum):
    """
    Supported Http transport
    """

    xmlrpc = "xmlrpc"
    jsonrpc = "jsonrpc"
