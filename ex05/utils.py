"""Continuation of building list utility functions!"""

__author__: str = "730536657"


def only_evens(full_list: list[int]) -> list[int]:
    """Returns even values from a list of ints."""
    # even_list  only adds the even values from full_list
    even_list: list[int] = list()
    i: int = 0
    while i < len(full_list):
        if full_list[i] % 2 == 0:
            even_list.append(full_list[i])
        i += 1

    return even_list


def concat(first_list: list[int], sec_list: list[int]) -> list[int]:
    """Concatenates two lists of ints together."""
    # total_list houses first_list and sec_list values
    total_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        total_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(sec_list):
        total_list.append(sec_list[i])
        i += 1
    
    return total_list


def sub(int_list: list[int], i: int, end_i: int) -> list[int]:
    """Returns a sub list between two specified indices."""
    # Bounds-checking for i and end_i
    if i < 0:
        i = 0
    if end_i > len(int_list):
        end_i = len(int_list)
    # Sub_list houses the values from int_list between i and end_i
    sub_list: list[int] = list()
    while i < end_i:
        sub_list.append(int_list[i])
        i += 1
    
    return sub_list