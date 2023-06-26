"""
OdooAioRPC is an aync Odoo remote procedure call
"""

from .client import OdooAioRPC
from .config import OdooSettings

__all__ = ("OdooAioRPC", "OdooSettings")

__version__ = "0.1.0-alpha1"
