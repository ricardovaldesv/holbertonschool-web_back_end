#!/usr/bin/env python3
""""A type-annotated function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple.
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Method that takes a string k and an int OR float
        v as arguments and returns a tuple."""
    return [k, v*v]
