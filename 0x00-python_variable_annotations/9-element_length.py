#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences,
    returns a list of tuples with sequences and their lengths.
    """
    return [(i, len(i)) for i in lst]
