#!/usr/bin/env python3
"""This file contains a Function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This Function takes in a list of int or float return their sum of float"""
    return sum(mxd_lst)
