#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create multiple asyncio tasks to wait
    for random delays and return them sorted.

    Args:
        n (int): The number of asyncio tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of random delays, sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)


# Test the task
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
