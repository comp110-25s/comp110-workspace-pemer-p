"""Testing the dictionary function."""

__author__: str = "730458530"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_use_1() -> None:
    """First use case test for invert function."""
    in_1: dict[str, str] = {"cat": "dog", "rat": "mouse"}
    assert invert(in_1) == {"dog": "cat", "mouse": "rat"}


def test_invert_use_2() -> None:
    """Second use case test for invert function."""
    in_2: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(in_2) == {"b": "a", "d": "c", "f": "e"}


def test_invert_edge() -> None:
    """Edge case test for invert function."""
    with pytest.raises(KeyError):
        in_3: dict[str, str] = {"a": "b", "c": "b"}
        invert(in_3)


def test_count_use_1() -> None:
    """First use case test for count function."""
    list_1: list[str] = ["meow", "meow", "hiss"]
    assert count(list_1) == {"meow": 2, "hiss": 1}


def test_count_use_2() -> None:
    """Second use case test for count function."""
    list_2: list[str] = ["hi", "hi", "hi", "hello", "hello", "goodbye"]
    assert count(list_2) == {"hi": 3, "hello": 2, "goodbye": 1}


def test_count_edge() -> None:
    """Edge case test for count function."""
    list_3: list[str] = []
    assert count(list_3) == {}


def test_favorite_color_use_1() -> None:
    """First use case test for favorite color function."""
    dict_1: dict[str, str] = {"Isaac": "green", "Payton": "green", "Josh": "yellow"}
    assert favorite_color(dict_1) == "green"


def test_favorite_color_use_2() -> None:
    """Second use case test for favorite color function."""
    dict_2: dict[str, str] = {
        "John": "blue",
        "Amy": "red",
        "Mary": "blue",
        "Mark": "red",
    }
    assert favorite_color(dict_2) == "blue"


def test_favorite_color_edge() -> None:
    """ "Edge case test for favorite color function."""
    dict_3: dict[str, str] = {}
    assert favorite_color(dict_3) == None


def test_bin_len_use_1() -> None:
    """First use case test for bin len function."""
    word_list_1: list[str] = ["frog", "toad", "kitty"]
    assert bin_len(word_list_1) == {4: {"frog", "toad"}, 5: {"kitty"}}


def test_bin_len_use_2() -> None:
    """Second use case test for bin len function."""
    word_list_2: list[str] = ["bat", "hate", "kraken"]
    assert bin_len(word_list_2) == {3: {"bat"}, 4: {"hate"}, 6: {"kraken"}}


def test_bin_len_edge() -> None:
    """Edge case test for bin len function"""
    word_list_3: list[str] = []
    assert bin_len(word_list_3) == {}
