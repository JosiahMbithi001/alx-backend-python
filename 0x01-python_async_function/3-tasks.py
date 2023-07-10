#!/usr/bin/env python3
"""This File contains the function task_await_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """This Function Creates a Task"""
    return asyncio.create_task(wait_random(max_delay))
