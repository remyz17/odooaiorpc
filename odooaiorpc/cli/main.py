from . import AsyncTyper, db, server

cli = AsyncTyper(no_args_is_help=True)
cli.add_typer(server.cli, name="server")
cli.add_typer(db.cli, name="database")


@cli.callback()
def callback() -> None:
    """
    OdooAioRPC allow you to query Odoo via command line interface
    """
