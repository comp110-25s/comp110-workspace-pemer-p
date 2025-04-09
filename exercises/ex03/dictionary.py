"""Dictionary function practice."""

__author__: str = "730458530"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a given dictionary."""
    output: dict[str, str] = {}
    for key in input:
        value: str = input[key]
        if value in output:
            raise KeyError("Duplicate keys are not allowed.")
        output[value] = key
    return output


def count(freq: list[str]) -> dict[str, int]:
    """Count of the number of times a value appears in a list."""
    freq_count: dict[str, int] = {}
    for item in freq:
        if item in freq_count:
            freq_count[item] += 1
        else:
            freq_count[item] = 1
    return freq_count


def favorite_color(colors: dict[str, str]) -> str:
    """Color that appears the most in a given dictionary."""
    color_count: dict[str, int] = {}
    for key in colors:
        if colors[key] in color_count:
            color_count[colors[key]] += 1
        else:
            color_count[colors[key]] = 1
    max_count: int = 0
    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
    for key in colors:
        if color_count[colors[key]] == max_count:
            return colors[key]


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary."""
    bins: dict[int, set[str]] = {}
    for word in words:
        length: int = len(word)
        if length not in bins:
            new_set: set[str] = {word}
            bins[length] = new_set
        else:
            bins[length].add(word)
    return bins
