"""Several functions that mimic various python functions: all, max, quality."""


def all(int_list: list[int], test_numb: int) -> bool:
    """Checks whether an int input exists in a list."""
    i: int = 0
    ls_length: int = len(int_list)
    # Returns False of list length is 0
    if ls_length == 0:
        return False
    # Checks if test_numb ever doesn't equal value in int_list
    while i < ls_length:
        if test_numb != int_list[i]:
            return False
        i += 1
    return True
    

def max(int_list: list[int]) -> int:
    """Finds the maximum value within a list."""
    i: int = 0
    ls_length: int = len(int_list)

    # ValueError in case user inputs an empty list
    if ls_length == 0:
        raise ValueError("max() arg is an empty List")

    while i < ls_length:
        # Initializes max_int to first value in list
        if i == 0:
            max_int: int = int_list[i]
        elif int_list[i] > max_int:  # Keeps updating max_int if a larger value is present in the list
            max_int = int_list[i]
        i += 1
    return max_int


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Determines whether two lists hold equal values at equal indices."""
    ls1_length: int = len(int_list1)
    ls2_length: int = len(int_list2)
    # Assumes inequality for inequal list lengths
    if ls1_length != ls2_length:
        return False
    else:
        i: int = 0
        while i < ls1_length:
            # Attempts to find inequal values at the same indices
            if int_list1[i] != int_list2[i]:
                return False
            i += 1
    
    return True