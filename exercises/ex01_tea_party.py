"""A program to plan a cozy tea party"""

__author__: str = "730458530"


def main_planner(guests: int) -> None:
    """A function that is the main planner for the tea party that is the entry point."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """How many tea bags to bring for a certain amount of people."""
    return people * 2


def treats(people: int) -> int:
    """How many treats based on numbers of teas guests drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
