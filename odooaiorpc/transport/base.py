import abc
import typing as t

from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes

from odooaiorpc import config


class BaseTransport(abc.ABC):
    def __init__(
        self,
        url: str,
        auth: t.Optional[AuthTypes] = None,
        headers: t.Optional[HeaderTypes] = None,
        context: VerifyTypes = None,
        timeout: TimeoutTypes = 5.0,
    ) -> None:
        self._url = url
        self._auth = auth
        self._headers = headers
        self._context = context
        self._timeout = timeout

    @abc.abstractclassmethod
    def from_settings(cls, settings: config.OdooSettings) -> "BaseTransport":
        ...
