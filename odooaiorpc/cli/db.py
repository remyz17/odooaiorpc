import typing as t

import rich
import typer

from odooaiorpc import state

cli = typer.Typer(no_args_is_help=True)


@cli.async_command()
async def list():
    client = state.AppState().get_default_client()
    data = await client.db.list()
    rich.print(data)


@cli.async_command()
async def list_lang():
    client = state.AppState().get_default_client()
    data = await client.db.list_lang()
    rich.print(data)


@cli.async_command()
async def exist(dbname: t.Annotated[str, typer.Argument()]):
    client = state.AppState().get_default_client()
    exist = await client.db.exist(db_name=dbname)
    rich.print(exist)


@cli.callback()
def callback():
    """
    db managment
    """
