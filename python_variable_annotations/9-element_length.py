#!/usr/bin/env python3
""""A type-annotated function element_length that takes a list of strings
    as argument and returns a tuple with string and number of characters.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list of strings
    as argument and returns a tuple with string and number of characters.
    """
    return [(i, len(i)) for i in lst]
