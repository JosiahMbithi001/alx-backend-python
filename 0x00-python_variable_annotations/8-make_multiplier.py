#!/usr/bin/env python3
from typing import Callable
"""This File Contains a function make_multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This Function multiplies a Flaot and returns a Function"""
    def multiply(n) -> float:
        """This Function multiplies n by multilier"""
        return n * multiplier
    return multiply
