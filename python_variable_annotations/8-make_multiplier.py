#!/usr/bin/env python3
""""A type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float 'multiplier' as an argument
         and returns a function that multiplies a float by 'multiplier'.
    """
    def multiply(x: float) -> float:
        """
        Takes a float 'x' and multiplies it by the 'multiplier'.
        Returns the result as a float.
        """
        return x * multiplier
    return multiply
