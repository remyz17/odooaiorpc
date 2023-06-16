import abc
import typing as t

if t.TYPE_CHECKING:
    from odooaiorpc.protocol import BaseProtocol


class BaseDomain(abc.ABC):
    def __init__(self, transport: "BaseProtocol") -> None:
        self._transport = transport

    @abc.abstractmethod
    async def _execute(self, method: str, *args, **kw) -> any:
        ...

    @abc.abstractproperty
    def domain_name(self) -> str:
        ...
