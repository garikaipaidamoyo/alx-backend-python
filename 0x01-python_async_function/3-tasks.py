#!/usr/bin/env python3


import asyncio
import random  # Add this import statement
from typing import List


async def wait_random(max_delay: int) -> float:
    """
    Return a random float between 0 and max_delay.
    """
    return random.uniform(0, max_delay)


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task to execute the wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
