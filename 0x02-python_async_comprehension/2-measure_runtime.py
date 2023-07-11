#!/usr/bin/env python3
"""This File Contains A coroutine Function measure_tuntime"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """This Function Measures runtime"""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
