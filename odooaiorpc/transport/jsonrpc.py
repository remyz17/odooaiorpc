import typing as t

from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes

from odooaiorpc.config import OdooSettings
from odooaiorpc.transport.base import BaseTransport


class JsonRpcProtocol(BaseTransport):
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

    @classmethod
    def from_settings(cls, settings: OdooSettings) -> "JsonRpcProtocol":
        return cls(url=settings.url, **settings.transport_config.dict())
