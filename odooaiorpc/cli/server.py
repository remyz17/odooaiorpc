import rich

from odooaiorpc import state
from odooaiorpc.cli import AsyncTyper

cli = AsyncTyper(no_args_is_help=True)


@cli.async_command()
async def version() -> None:
    client = state.AppState().get_default_client()
    data = await client.version()
    rich.print(data)


@cli.callback()
def callback() -> None:
    """
    server managment
    """
