class Singleton(type):
    """
    This a Singleton pattern class.
    It's purpose is to ensure that only one instance of a class can be created.
    """

    _instances = {}  # type: ignore[var-annotated]

    def __call__(cls, *args, **kwargs):  # type: ignore[no-untyped-def]
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
