#!/usr/bin/env python3
"""This File contains A Function to_kv"""
from typing import Union, Tuple

def to_kv(k:str, v:Union[int, float]) -> Tuple[str, float]:
    """This Function concatnates str, int,float and returns a Tuple"""
    return (k , float(v ** 2)) 
