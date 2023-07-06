#!/usr/bin/env python3
from typing import Callable
"""This File COntains a function make_multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This Function multiplies a Flaot and returns a Function"""
    def multiply(n) -> float:
        return n * multiplier
    return multiply
