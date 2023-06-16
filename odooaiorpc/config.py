import typing as t
from urllib.parse import urlparse

from httpx._types import AuthTypes, HeaderTypes, TimeoutTypes, VerifyTypes
from pydantic import AnyUrl, BaseSettings, validator

from odooaiorpc import const


class OdooSettings(BaseSettings):
    """
    Odoo client configuration settings
    """

    class Config:
        env_prefix = "ODOO_AIO_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    url: AnyUrl
    """
    Odoo url
    """
    database: t.Optional[str] = None
    """
    Odoo database
    """
    user: str
    """
    Odoo user
    """
    secret: str
    """
    Odoo user API key
    """
    protocol: const.Protocol = const.Protocol.jsonrpc
    """
    RPC protocol used to communicate. Default to jsonrpc
    """
    auth: t.Optional[AuthTypes] = None
    headers: t.Optional[HeaderTypes] = None
    context: t.Optional[VerifyTypes] = None
    timeout: TimeoutTypes = 5.0

    @validator("database", pre=True, always=True)
    def extract_db_name(cls, v, values, **kwargs):
        """
        Extract database name from url if not specified
        """
        if v is None and "url" in values:
            parsed_url = urlparse(values["url"])
            return parsed_url.hostname.split(".")[0]
        return v
