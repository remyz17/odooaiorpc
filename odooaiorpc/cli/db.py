import typing as t

import rich
import typer

from odooaiorpc import state
from odooaiorpc.cli import AsyncTyper

cli = AsyncTyper(no_args_is_help=True)


@cli.async_command()
async def list() -> None:
    client = state.AppState().get_default_client()
    data = await client.db.list()
    rich.print(data)


@cli.async_command()
async def list_lang() -> None:
    client = state.AppState().get_default_client()
    data = await client.db.list_lang()
    rich.print(data)


@cli.async_command()
async def exist(dbname: t.Annotated[str, typer.Argument()]) -> None:
    client = state.AppState().get_default_client()
    exist = await client.db.db_exist(db_name=dbname)
    rich.print(exist)


@cli.callback()
def callback() -> None:
    """
    db managment
    """
