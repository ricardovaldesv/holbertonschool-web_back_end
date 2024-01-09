#!/usr/bin/env python3
""""A type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their sum as a float.
"""


def sum_list(list: float) -> float:
    """Method that takes a list as argument
        and returns the sum as a float."""
    sum = 0
    for number in list:
        sum += number
    return float(sum)
