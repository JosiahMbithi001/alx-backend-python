#!/usr/bin/env python3
"""This File contains coroutine async_generator"""
import random
import asyncio


async def async_generator():
    """This Function yields random numbers from 0-10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
