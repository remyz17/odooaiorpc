import typer

from . import db, server

cli = typer.Typer(no_args_is_help=True)
cli.add_typer(server.cli, name="server")
cli.add_typer(db.cli, name="database")


@cli.callback()
def callback():
    """
    OdooAioRPC allow you to query Odoo via command line interface
    """
