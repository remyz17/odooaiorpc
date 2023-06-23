import typing as t

from .base import BaseDomain

if t.TYPE_CHECKING:
    from odooaiorpc.protocol import BaseProtocol


class ModelDomain(BaseDomain):
    def __init__(self, transport: "BaseProtocol") -> None:
        super().__init__(transport)

    async def execute_kw(self, *args, **kw) -> t.Any:
        return await self._execute("execute_kw", *args, **kw)

    async def execute(self, *args, **kw) -> t.Any:
        if not kw:
            raise ValueError("RPC method 'excute' require kwargs to be set")
        return await self._execute("execute", *args, **kw)

    @property
    def domain_name(self) -> str:
        return "object"
