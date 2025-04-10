"""File to define Bear class."""

__author__: str = "730458530"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases age of bear by one day."""
        self.age += 1
        return None
