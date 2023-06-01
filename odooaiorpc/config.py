import typing as t
from urllib.parse import urlparse

from pydantic import AnyUrl, BaseSettings, validator


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

    @validator("database", pre=True, always=True)
    def extract_db_name(cls, v, values, **kwargs):
        """
        Extract database name from url if not specified
        """
        if v is None and "url" in values:
            parsed_url = urlparse(values["url"])
            return parsed_url.hostname.split(".")[0]
        return v
