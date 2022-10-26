"""Dictionary related utility functions."""

__author__ = "730536657"

from csv import DictReader


# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a CSV file into a 'table'."""
    table: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")  # Handles File
    csv_reader = DictReader(file_handle)  # Reads file handle
    for row in csv_reader:
        table.append(row)
    file_handle.close()  # Closes file

    return table


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns list of values in a provided column name of a 'table."""
    values: list[str] = []
    # Finds each value within column and appens to values list
    for row in table:
        value: str = row[column]
        values.append(value)

    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Converts 'row table' to a dict with columns as keys."""
    column_dict: dict[str, list[str]] = {}
    col_vals: dict[str, str] = table[0]
    # Uses column_values to get list of items for each key in resuling key
    for column in col_vals:
        column_dict[column] = column_values(table, column)

    return column_dict


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Copies first n items of each column to form the 'head'."""
    head_result: dict[str, list[str]] = {}
    for column in column_table:
        current_vals: list[str] = column_table[column]
        if rows > len(current_vals):
            rows = len(current_vals)
        values: list[str] = []
        i: int = 0
        while i < rows:
            # Saves and appends each item within first n items
            item: str = current_vals[i]
            values.append(item)
            i += 1
        head_result[column] = values
    
    return head_result


def select(column_table: dict[str, list[str]], col_list: list[str]) -> dict[str, list[str]]:
    """Returns new column-table with certain subset of original column-table."""
    select_result: dict[str, list[str]] = {}
    for column in col_list:
        if column in column_table:  # First checks if item in col_list is a key name in column table
            select_result[column] = column_table[column]  # Assigns new key-value pair in select_result
    
    return select_result


def concat(col_table1: dict[str, list[str]], col_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables of data."""
    combined_dict: dict[str, list[str]] = {}
    for column in col_table1:
        combined_dict[column] = col_table1[column]  # Adds all of the first table to combined_dict
    for column in col_table2:
        if column in combined_dict:
            #  If column exists, it appends each value to the end of the existing list of column values
            value_list: list[str] = combined_dict[column]
            i: int = 0
            while i < len(col_table2[column]):
                value_list.append(col_table2[column][i])
                i += 1
        else:
            combined_dict[column] = col_table2[column]

    return combined_dict


def count(values: list[str]) -> dict[str, int]:
    """Counts frequencies of strings in a list and returns a dictionary with that info."""
    freqs: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in freqs:
            freqs[values[i]] += 1
        else:
            freqs[values[i]] = 1
        i += 1
    return freqs