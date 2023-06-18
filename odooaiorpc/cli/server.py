import rich
import typer

from odooaiorpc import state

cli = typer.Typer(no_args_is_help=True)


@cli.async_command()
async def version():
    client = state.AppState().get_default_client()
    data = await client.version()
    rich.print(data)


@cli.callback()
def callback():
    """
    server managment
    """
