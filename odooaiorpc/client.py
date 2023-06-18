import typing as t

from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes
from pydantic import AnyUrl

from odooaiorpc import const
from odooaiorpc.config import OdooSettings
from odooaiorpc.domain import CommonDomain, DBDomain, ModelDomain
from odooaiorpc.protocol import BaseProtocol, pick_preferred_protocol


class OdooAioRPC:
    def __init__(
        self,
        url: t.Union[str, AnyUrl],
        database: str,
        user: str,
        secret: str,
        protocol: const.Protocol = const.Protocol.jsonrpc,
        auth: t.Optional[AuthTypes] = None,
        headers: t.Optional[HeaderTypes] = None,
        context: t.Optional[VerifyTypes] = None,
        timeout: TimeoutTypes = 5.0,
        transport: t.Optional[BaseProtocol] = None,
    ) -> None:
        """
        Initialize OdooAioRPC client

        Args:
            url (t.Union[str, AnyUrl]): Odoo http URL
            database (str): Odoo database
            user (str): Odoo user to connect with
            secret (str): Odoo user generated api key or password (discouraged)
            protocol (const.Protocol, optional): Communication protocol. Defaults to const.Protocol.jsonrpc.
            auth (t.Optional[AuthTypes], optional): Auth options. Defaults to None.
            headers (t.Optional[HeaderTypes], optional): Custom http headers. Defaults to None.
            context (t.Optional[VerifyTypes], optional): SSL context. Defaults to None.
            timeout (TimeoutTypes, optional): Connection timeout. Defaults to 5.0.
            transport (t.Optional[BaseProtocol], optional): _description_. Defaults to None.
        """
        self._url = url
        self._database = database
        self._user = user
        self._secret = secret
        self._uid = None
        self._common_proxy = None
        self._object_proxy = None
        self._db_proxy = None

        if transport:
            self._transport = transport
        else:
            self._transport = pick_preferred_protocol(protocol=protocol)(
                url=url,
                auth=auth,
                headers=headers,
                context=context,
                timeout=timeout,
            )

    @staticmethod
    def get_protocol_from_settings(settings: OdooSettings) -> BaseProtocol:
        """
        Get configured protocol class from OdooSettings

        Args:
            settings (OdooSettings): settings to get config from

        Returns:
            BaseProtocol: Protocol instance
        """
        return pick_preferred_protocol(protocol=settings.protocol).from_settings(
            settings=settings
        )

    @classmethod
    def from_settings(cls, settings: OdooSettings) -> "OdooAioRPC":
        """
        Initialize OdooAioRPC client from OdooSettings

        Args:
            settings (OdooSettings): settings

        Returns:
            OdooAioRPC: RPC client instance
        """
        return cls(
            url=settings.url,
            database=t.cast(str, settings.database),
            user=settings.user,
            secret=settings.secret,
            protocol=settings.protocol,
            auth=settings.auth,
            headers=settings.headers,
            context=settings.context,
            timeout=settings.timeout,
        )

    async def authenticate(self) -> t.Optional[int]:
        """
        Authenticate configured user with Odoo
        Return uid if auth process success

        Returns:
            t.Optional[int]: User uid
        """
        uid = await self.common.authenticate(
            self._database, self._user, self._secret, {}
        )
        if uid:
            self._uid = uid
        return uid

    async def version(self) -> dict:
        """
        Return Odoo server version informations

        Returns:
            dict: Version infos
        """
        return await self.common.version()

    @property
    def is_auth(self) -> bool:
        """
        Check if auth has been done

        Returns:
            bool: auth state
        """
        return self._uid is not None

    @property
    def common(self) -> CommonDomain:
        """
        Return common RPC domain
        Initialize if not already done

        Returns:
            CommonDomain: Common RPC domain
        """
        if self._common_proxy is None:
            self._common_proxy = CommonDomain(transport=self._transport)
        return self._common_proxy

    @property
    def models(self) -> ModelDomain:
        """
        Return object/models RPC domain
        Initialize if not already done

        Returns:
            ModelDomain: Object RPC domain
        """
        if self._object_proxy is None:
            self._object_proxy = ModelDomain(transport=self._transport)
        return self._object_proxy

    @property
    def db(self) -> DBDomain:
        """
        Return db RPC domain
        Initialize if not already done

        Returns:
            DBDomain: DB RPC domain
        """
        if self._db_proxy is None:
            self._db_proxy = DBDomain(transport=self._transport)
        return self._db_proxy
