"""A program to play a fun word game called Wordle."""

__author__: str = "730458530"


def contains_char(a_str: str, char: str) -> bool:
    """A function to determine if a character is found in a string."""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    # Loop to check if the character given is the same of the string's index
    while idx < len(a_str):
        if a_str[idx] == char:  # Index in string matches character
            return True
        idx += 1  # Increases index variable by 1 to check next index in string
    return False


# Symbols to represent the different boxes in Wordle guesses
WHITE_BOX: str = "\U00002B1C"  # Incorrect Letter
GREEN_BOX: str = "\U0001F7E9"  # Correct Letter
YELLOW_BOX: str = "\U0001F7E8"  # Letter in word but wrong position


def emojified(guess: str, secret: str) -> str:
    """A function to codify the player's guess word into secret word emojis."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""  # String storing emoji representation of word
    # Loop to return colored symbols to show which letters in guess are found in secret
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX  # Builds the return string with a correct box
        elif contains_char(secret, guess[idx]):
            result = (
                result + YELLOW_BOX
            )  # Builds return string with correct letter out of position
        else:
            result = result + WHITE_BOX  # Builds return string with incorrect letter
        idx += 1
    return result


def input_guess(n: int) -> str:
    """A function prompting user for guess until expected length given."""
    guess = input(f"Enter a {n} character word:")
    if len(guess) == n:
        return guess  # Returns the guess if same length of n length word
    # Loop to prompt user to continue inputting word until matches n length
    while len(guess) != n:
        guess = input(f"That wasn't {n} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    # Loop to run the game, giving user 6 turns to guess the secret word
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            n=len(secret)
        )  # Assigns guess to be word inputted by user
        print(
            emojified(guess, secret)
        )  # Prints the emoji representation of each guess turn
        if guess == secret:
            print(
                f"You won in {turn}/6 turns!"
            )  # Prints winning message if secret and guess match
            return  # Ensures does not prompt user another input
        turn = turn + 1
        if turn > 6 and guess != secret:
            print(
                "X/6 - Sorry, try again tomorrow!"
            )  # Losing message if did not guess secret in 6 turns


if __name__ == "__main__":
    main(secret="codes")
