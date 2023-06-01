import typing as t

from config import OdooSettings
from pydantic import AnyUrl


class OdooAioRPC:
    def __init__(
        self, url: t.Union[str, AnyUrl], database: str, user: str, secret: str
    ) -> None:
        """
        _summary_

        Args:
            url (t.Union[str, AnyUrl]): Odoo URL
            database (str): Database name
            user (str): User used to communicate
            secret (str): API key or password
        """
        self._url = url
        self._database = database
        self._user = user
        self._secret = secret

    @classmethod
    def from_settings(cls, settings: OdooSettings) -> "OdooAioRPC":
        return cls(
            url=settings.url,
            database=t.cast(str, settings.database),
            user=settings.user,
            secret=settings.secret,
        )
