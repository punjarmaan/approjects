"""Testing more list utility functions!"""

__author__: str = "730536657"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests an empty list for even ints."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_only_evens_only_odds() -> None:
    """Tests a list with only odd ints for even ints."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_pos_vals() -> None:
    """Tests a list with positive values for even ints."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert only_evens(xs) == [2, 4, 6, 8, 10, 12, 14]


def test_only_evens_mixed_vals() -> None:
    """Tests a list of negative and positive values for even ints."""
    xs: list[int] = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert only_evens(xs) == [-4, -2, 0, 2, 4]


def test_concat_empty_lists() -> None:
    """Tests concatenation of empty lists."""
    xs: list[int] = list()
    ys: list[int] = list()
    assert concat(xs, ys) == []


def test_concat_two_reg_lists() -> None:
    """Tests concatenation of two regular lists with many items."""
    xs: list[int] = [1, 7, 23, 54, 84, 3]
    ys: list[int] = [87, 34, 36, 23, 65, 2, 6]
    assert concat(xs, ys) == [1, 7, 23, 54, 84, 3, 87, 34, 36, 23, 65, 2, 6]


def test_concat_two_reg_lists_again() -> None:
    """Tests concatenation of two regular lists with many items, again."""
    xs: list[int] = [34, 23, 65, 99, 2, 4, 5, 6, 1]
    ys: list[int] = [3, 102, 68, 70, 53, 26, 37]
    assert concat(xs, ys) == [34, 23, 65, 99, 2, 4, 5, 6, 1, 3, 102, 68, 70, 53, 26, 37]


def test_sub_start_index_too_big() -> None:
    """Tests for sub_list to be created with too-high start index."""
    xs: list[int] = [5, 10, 15, 20, 25, 30, 35, 40]
    i: int = 9
    end_i: int = 5
    assert sub(xs, i, end_i) == []


def test_sub_reg_indices() -> None:
    """Tests a sub list with regular-valued indices."""
    xs: list[int] = [0, 3, 6, 9, 12, 15, 18, 21]
    i: int = 3
    end_i: int = 7
    assert sub(xs, i, end_i) == [9, 12, 15, 18]


def test_sub_reg_indices_again() -> None:
    """Tests a sub list with regular-valued indices, again."""
    xs: list[int] = [20, 40, 60, 80, 100, 120, 140, 160, 180]
    i: int = 0
    end_i: int = 6
    assert sub(xs, i, end_i) == [20, 40, 60, 80, 100, 120]