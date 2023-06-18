import abc
import typing as t

if t.TYPE_CHECKING:
    from odooaiorpc.protocol import BaseProtocol


class BaseDomain(abc.ABC):
    def __init__(self, transport: "BaseProtocol") -> None:
        self._transport = transport

    async def _execute(self, method: str, *args, **kw) -> any:
        return await self._transport.execute(self.domain_name, method, *args, **kw)

    @abc.abstractproperty
    def domain_name(self) -> str:
        ...
