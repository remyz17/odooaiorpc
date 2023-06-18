from pathlib import Path

import typer

from odooaiorpc import OdooAioRPC, OdooSettings
from odooaiorpc.utils import Singleton


class AppState(metaclass=Singleton):
    def __init__(self) -> None:
        self._clients = {}
        self._config_path = typer.get_app_dir("odooaiorpc", force_posix=True)
        self._search_paths = []
        self._default_settings = {}

    def add_search_path(self, path: Path) -> None:
        """
        Add provided path to search path list

        Args:
            path (Path): path to Add

        Raises:
            ValueError: If path does not exist or is not a directory
        """
        if not path.exists():
            raise ValueError("Path does not exist")
        if not path.is_dir:
            raise ValueError("Path is not a directory")
        self._search_paths.append(path)

    def get_default_client(self) -> OdooAioRPC:
        """
        Get default client with env vars

        Returns:
            OdooAioRPC: Client instance
        """
        return OdooAioRPC.from_settings(settings=OdooSettings())
