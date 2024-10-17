#!/usr/bin/env python3
""" Basic annotations - to_kv module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of the string and the square of the int/float.
    """
    return (k, float(v**2))
