import typing as t

from aioxmlrpc.client import ServerProxy
from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes
from pydantic import AnyUrl

from odooaiorpc.protocol.base import BaseProtocol


class XmlRpcProtocol(BaseProtocol):
    def __init__(
        self,
        url: t.Union[str, AnyUrl],
        auth: t.Optional[AuthTypes] = None,
        headers: t.Optional[HeaderTypes] = None,
        context: t.Optional[VerifyTypes] = None,
        timeout: TimeoutTypes = 5.0,
    ) -> None:
        super().__init__(
            url=url, auth=auth, headers=headers, context=context, timeout=timeout
        )
        self._common_proxy, self._object_proxy, self._db_proxy = self._build_proxies()

    def _build_proxy(self, proxy_uri: str) -> ServerProxy:
        """
        Buuld xmlrpc ServerProxy with params

        Args:
            proxy_uri (str): URI to domain

        Returns:
            ServerProxy: xmlrpc proxy instance
        """
        return ServerProxy(
            uri=f"{self._url}{proxy_uri}",
            auth=self._auth,
            headers=self._headers,
            context=self._context,
            timeout=self._timeout,
        )

    def _build_proxies(self) -> t.Tuple[ServerProxy, ...]:
        """
        Build required xmlrpc proxies

        Returns:
            t.Tuple[ServerProxy, ...]: List of rpc proxies for each domain
        """
        return tuple(
            self._build_proxy(proxy_uri=f"/xmlrpc/2/{domain}")
            for domain in ("common", "object", "db")
        )

    async def execute(self, domain: str, methood: str, *args, **kw) -> t.Any:
        if domain not in ("db", "object", "common"):
            raise ValueError(f"RPC {domain=} does not exist")
        # TODO manage exceptions
        return await getattr(getattr(self, f"_{domain}_proxy"), methood)(*args, **kw)
