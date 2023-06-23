import typing as t
from pathlib import Path

import typer

from odooaiorpc import OdooAioRPC, OdooSettings
from odooaiorpc.utils import Singleton


class AppState(metaclass=Singleton):
    def __init__(self) -> None:
        self._clients: dict[str, OdooAioRPC] = {}
        self._config_path = typer.get_app_dir("odooaiorpc", force_posix=True)
        self._search_paths: list[Path] = []
        self._default_settings: dict[str, t.Any] = {}

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
        if path.is_dir is False:
            raise ValueError("Path is not a directory")
        self._search_paths.append(path)

    def get_default_client(self) -> OdooAioRPC:
        """
        Get default client with env vars

        Returns:
            OdooAioRPC: Client instance
        """
        return OdooAioRPC.from_settings(settings=OdooSettings())  # type: ignore[call-arg]
