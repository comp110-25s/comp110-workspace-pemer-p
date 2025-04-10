"""File to define River class."""

__author__: str = "730458530"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River class creation with fish and bears."""

    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages of fish and bears to see if they are alive."""
        alive_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        self.fish = alive_fish

        alive_bears: list[Bear] = []
        for bears in self.bears:
            if bears.age <= 5:
                alive_bears.append(bears)
        self.bears = alive_bears
        return None

    def bears_eating(self) -> None:
        """Removes fish from river if bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self) -> None:
        """Checks to see if bears are dying of hunger."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
            self.bears = alive_bears
        return None

    def repopulate_fish(self) -> None:
        """Determines reproduction of fish."""
        offspring = (len(self.fish) // 2) * 4
        while offspring > 0:
            self.fish.append(Fish())
            offspring -= 1
        return None

    def repopulate_bears(self) -> None:
        """Determines reproduction of bears."""
        offspring = len(self.bears) // 2
        while offspring > 0:
            self.bears.append(Bear())
            offspring -= 1
        return None

    def view_river(self) -> None:
        """View of the river at a given day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bearrepopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """View of the river at a given week."""
        while self.day < 7:
            self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes a given amount of fish from the river."""
        count = 0
        while count < amount and self.fish:
            self.fish.pop(0)
            count += 1
        return None
