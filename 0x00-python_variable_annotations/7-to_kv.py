#!/usr/bin/env python3

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int/float v,
    returns a tuple with k and v squared.
    """
    return (k, v ** 2)
