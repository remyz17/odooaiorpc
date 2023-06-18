import typing as t

from .base import BaseDomain

if t.TYPE_CHECKING:
    from odooaiorpc.protocol import BaseProtocol


class DBDomain(BaseDomain):
    def __init__(self, transport: "BaseProtocol") -> None:
        super().__init__(transport)

    async def db_exist(self, db_name: str) -> dict:
        return await self._execute("db_exist", [db_name])

    async def list(self) -> dict:
        return await self._execute("list")

    async def list_lang(self) -> t.Optional[int]:
        return await self._execute("list_lang")

    @property
    def domain_name(self) -> str:
        return "db"
