#!/usr/bin/env python3

import asyncio
import time
from typing import List


# Import wait_random correctly
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random coroutine n times and return a list of delays.
    """
    return [await wait_random(max_delay) for _ in range(n)]


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and
    return total_time / n as a float.
    """
    start_time = time.perf_counter()
    delays = asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
