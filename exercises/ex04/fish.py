"""File to define Fish class."""

__author__: str = "730458530"


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        """Increases age of fish by one day."""
        self.age += 1
        return None
