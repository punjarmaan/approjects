"""Some dictionary util functions (invert, count, favorite_colors) implemented."""

__author__: str = "730536657"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with inverted/reversed keys and values as the original dictionary inputted."""
    inverted_original: dict[str, str] = {}
    for key in original:
        value = original[key]
        if value not in inverted_original:  # Only reverses key-value pair if value is not a duplicate
            inverted_original[value] = key
        else:
            raise KeyError("Duplicate keys in inverted dictionary!")
    return inverted_original


def favorite_color(name_color: dict[str, str]) -> str:
    """Finds and returns the color that is the most favorite (most votes) in a dictionary with names and colors."""
    color_count: dict[str, int] = {}
    for name in name_color:
        color: str = name_color[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # Finds max_count value for colors in the list
    max_count: int = max(color_count.values())
    for color in color_count:
        if max_count == color_count[color]:
            return color
    return "None"


def count(original_ls: list[str]) -> dict[str, int]:
    """Counts and records every instance of a word in the list original_ls."""
    word_count: dict[str, int] = {}
    for word in original_ls:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count