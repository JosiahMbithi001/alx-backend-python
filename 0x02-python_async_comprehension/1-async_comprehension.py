#!/usr/bin/env python3
"""This File Contains the coroutine function async_comprehension"""
import asyncio
# from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """This Function yields using async comprehension"""
    random_numbers = [rand_num async for rand_num in async_generator()]
    return random_numbers
