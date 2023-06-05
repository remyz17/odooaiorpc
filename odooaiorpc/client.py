import typing as t

from pydantic import AnyUrl

from odooaiorpc import const, transport
from odooaiorpc.config import OdooSettings


class OdooAioRPC:
    def __init__(
        self,
        url: t.Union[str, AnyUrl],
        database: str,
        user: str,
        secret: str,
        http_transport: transport.BaseTransport,
    ) -> None:
        """
        Initialize OdooAioRPC client
        A transport must be provided

        Args:
            url (t.Union[str, AnyUrl]): Odoo URL
            database (str): Odoo database
            user (str): Odoo user to connect with
            secret (str): Odoo user generated api key or password (discouraged)
            http_transport (transport.BaseTransport): Http Transport
        """
        self._url = url
        self._database = database
        self._user = user
        self._secret = secret
        self._transport = http_transport

    @staticmethod
    def get_transport_from_settings(settings: OdooSettings) -> transport.BaseTransport:
        if settings.protocol == const.Protocol.xmlrpc:
            return transport.XmlRpcProtocol.from_settings(settings)
        return transport.JsonRpcProtocol.from_settings(settings)

    @classmethod
    def from_settings(cls, settings: OdooSettings) -> "OdooAioRPC":
        return cls(
            url=settings.url,
            database=t.cast(str, settings.database),
            user=settings.user,
            secret=settings.secret,
            http_transport=cls.get_transport_from_settings(settings),
        )
