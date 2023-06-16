import typing as t

from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes

from odooaiorpc.protocol.base import BaseProtocol


class JsonRpcProtocol(BaseProtocol):
    def __init__(
        self,
        url: str,
        auth: t.Optional[AuthTypes] = None,
        headers: t.Optional[HeaderTypes] = None,
        context: t.Optional[VerifyTypes] = None,
        timeout: TimeoutTypes = 5.0,
    ) -> None:
        super().__init__(
            url=url, auth=auth, headers=headers, context=context, timeout=timeout
        )

    async def execute(self, domain: str, methood: str, *args, **kw) -> any:
        raise NotImplementedError()
