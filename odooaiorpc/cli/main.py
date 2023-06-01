import typer

cli = typer.Typer(no_args_is_help=True)


@cli.callback()
def callback():
    """
    OdooAioRPC allow you to query Odoo via command line interface
    """
