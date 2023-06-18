import functools

import anyio
import typer


# allow to run Typer command with asyncio
def async_command(app, *args, **kwargs):
    def decorator(async_func):
        @functools.wraps(async_func)
        def sync_func(*_args, **_kwargs):
            async def _main():
                await async_func(*_args, **_kwargs)

            return anyio.run(_main)

        app.command(*args, **kwargs)(sync_func)
        return async_func

    return decorator


typer.Typer.async_command = async_command
