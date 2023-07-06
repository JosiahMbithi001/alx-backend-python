#!/usr/bin/env python3
"""This File contains element_length """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This Function receives iterable"""
    return [(i, len(i)) for i in lst]
