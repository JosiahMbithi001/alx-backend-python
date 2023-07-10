#!/usr/bin/env python3
"""The File contains a wait_random Function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This Function Delays for a maximum number of seconds(max_delay)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
