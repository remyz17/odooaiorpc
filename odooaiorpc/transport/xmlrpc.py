import typing as t

from aioxmlrpc.client import ServerProxy
from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes

from odooaiorpc.config import OdooSettings
from odooaiorpc.transport.base import BaseTransport


class XmlRpcProtocol(BaseTransport):
    _common_proxy: ServerProxy
    _object_proxy: ServerProxy
    _db_proxy: ServerProxy

    def __init__(
        self,
        url: str,
        auth: t.Optional[AuthTypes] = None,
        headers: t.Optional[HeaderTypes] = None,
        context: VerifyTypes = None,
        timeout: TimeoutTypes = 5.0,
    ) -> None:
        super().__init__(
            url=url, auth=auth, headers=headers, context=context, timeout=timeout
        )
        self._common_proxy = self.build_proxy("/xmlrpc/2/common")
        self._object_proxy = self.build_proxy("/xmlrpc/2/object")
        self._db_proxy = self.build_proxy("/xmlrpc/2/db")

    def build_proxy(self, proxy_uri: str) -> ServerProxy:
        return ServerProxy(
            uri=f"{self._url}{proxy_uri}",
            auth=self._auth,
            headers=self._headers,
            context=self._context,
            timeout=self._timeout,
        )

    @classmethod
    def from_settings(cls, settings: OdooSettings) -> "XmlRpcProtocol":
        return cls(url=settings.url, **settings.transport_config.dict())
