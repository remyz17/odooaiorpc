import typing as t

from .base import BaseDomain

if t.TYPE_CHECKING:
    from odooaiorpc.protocol import BaseProtocol


class CommonDomain(BaseDomain):
    def __init__(self, transport: "BaseProtocol") -> None:
        super().__init__(transport)

    async def version(self) -> dict:
        return await self._execute("version")

    async def about(self) -> dict:
        return await self._execute("about")

    async def authenticate(self, *args, **kw) -> t.Optional[int]:
        return await self._execute("authenticate", *args, **kw)

    @property
    def domain_name(self) -> str:
        return "common"
