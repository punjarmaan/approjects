"""Unit tests testing dictionary utilities."""

__author__: str = "730536657"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_keyerrored() -> None:
    """Test to see if a KeyError is raised if duplicate values are present in the original dictionary."""
    with pytest.raises(KeyError):
        dup_dictionary = {'Armaan': 'Punj', 'Ashwin': 'Punj'}
        invert(dup_dictionary)


def test_invert_use_alphabet() -> None:
    """Tests to see if it can invert some letters with words associated with them."""
    letters_words: dict[str, str] = {'a': 'apple', 'b': 'banana', 'c': 'clementine', 'd': 'dragonfruit'}
    assert invert(letters_words) == {'apple': 'a', 'banana': 'b', 'clementine': 'c', 'dragonfruit': 'd'}


def test_invert_use_clothes_sizes() -> None:
    """Tests to see if invert can invert dict with clothes and associated sizes."""
    clothes_sizes: dict[str, str] = {'shirt': 'small', 'pants': 'medium', 'shorts': 'large', 'sweater': 'xlarge'}
    assert invert(clothes_sizes) == {'small': 'shirt', 'medium': 'pants', 'large': 'shorts', 'xlarge': 'sweater'}


def test_favorite_color_only_dups() -> None:
    """Tests to see if the same color (blue) will print when all names pick same color."""
    name_colors: dict[str, str] = {'Armaan': 'white', 'Adam': 'white', 'Matt': 'white'}
    assert favorite_color(name_colors) == 'white'


def test_favorite_color_majority_green() -> None:
    """Tests to see if green is returned when majority of names pick green."""
    name_colors: dict[str, str] = {'Armaan': 'green', 'Adam': 'yellow', 'Matt': 'green'}
    assert favorite_color(name_colors) == 'green'


def test_favorite_color_equal_majority() -> None:
    """Tests to see if first color in dict will print if two colors have the same vote count."""
    name_colors: dict[str, str] = {'Armaan': 'yellow', 'Adam': 'yellow', 'Matt': 'blue', 'Sydney': 'blue'}
    assert favorite_color(name_colors) == 'yellow'


def test_count_all_same_words() -> None:
    """Tests to see if dictionary counts all identical words in input dict."""
    words: list[str] = ['dog', 'dog', 'dog', 'dog', 'dog']
    assert count(words) == {'dog': 5}


def test_count_mixed_words() -> None:
    """Tests to see if count function will accurately count words with various occurrences in the list."""
    words: list[str] = ['dog', 'red', 'red', 'cat', 'red', 'cat', 'bird', 'dog', 'red']
    assert count(words) == {'dog': 2, 'red': 4, 'cat': 2, 'bird': 1}


def test_count_mixed_words_again() -> None:
    """Tests to see if count function will accurately count words with various occurrences in the list, again."""
    words: list[str] = ['wolf', 'panda', 'trex', 'cheetos', 'panda', 'wolf', 'green', 'trex']
    assert count(words) == {'wolf': 2, 'panda': 2, 'trex': 2, 'cheetos': 1, 'green': 1}