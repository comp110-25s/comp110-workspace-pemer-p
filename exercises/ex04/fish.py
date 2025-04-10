"""File to define Fish class."""

__author__: str = "730458530"


class Fish:
    """Fish class creation."""

    age: int

    def __init__(self):
        """Initializing fish class values."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Increases age of fish by one day."""
        self.age += 1
        return None
