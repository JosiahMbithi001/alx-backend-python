#!/usr/bin/env python3
"""This File contains An Asyncronous Routine Function wait_n"""
from heapq import nsmallest
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This Function spans wait_random n times for concurrent execution"""
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return nsmallest(n, delays)
