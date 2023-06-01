import typing as t

from pydantic import BaseSettings


class OdooSettings(BaseSettings):
    """
    Odoo client configuration settings
    """

    class Config:
        env_prefix = "ODOO_AIO_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    url: t.Optional[str] = None
    """
    Odoo url
    """
    database: t.Optional[str] = None
    """
    Odoo database
    """
    user: t.Optional[str] = None
    """
    Odoo user
    """
    secret: t.Optional[str] = None
    """
    Odoo user API key
    """
