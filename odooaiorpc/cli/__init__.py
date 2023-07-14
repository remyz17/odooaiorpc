from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec

import anyio
import sniffio
import typer

P = ParamSpec("P")


class AsyncTyper(typer.Typer):
    """Asyncronous Typer that derives from Typer.

    Use this when you have an asynchronous command you want to build, otherwise, just use Typer.
    """

    def async_command(  # type: ignore # Because we're being generic in this decorator, 'Any' is fine for the args.
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Callable[
        [Callable[P, Coroutine[Any, Any, None]]],
        Callable[P, Coroutine[Any, Any, None]],
    ]:
        """An async decorator for Typer commands that are asynchronous."""

        def decorator(  # type: ignore # Because we're being generic in this decorator, 'Any' is fine for the args.
            async_func: Callable[P, Coroutine[Any, Any, None]],
        ) -> Callable[P, Coroutine[Any, Any, None]]:
            @wraps(async_func)
            def sync_func(*_args: P.args, **_kwargs: P.kwargs) -> None:
                async def _main() -> None:
                    await async_func(*_args, **_kwargs)

                return anyio.run(_main, backend=sniffio.current_async_library())

            # Now use app.command as normal to register the synchronous function
            self.command(*args, **kwargs)(sync_func)

            # We return the async function unmodified, so its library functionality is preserved.
            return async_func

        return decorator
