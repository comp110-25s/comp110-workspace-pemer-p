"""File to define Bear class."""

__author__: str = "730458530"


class Bear:
    """Class for a bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing the bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Increases age of bear by one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases hunger score if bear eats fish."""
        self.hunger_score += num_fish
