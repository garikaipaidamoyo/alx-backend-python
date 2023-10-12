#!/usr/bin/env python3
'''
Function to measure runtime of wait_n
'''

import asyncio
import time
from typing import List

# Import the wait_n function from your module
from basic_async_syntax import wait_random


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay) and
    returns total_time / n as a float.
    '''
    start_time = time.perf_counter()
    delays = asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
