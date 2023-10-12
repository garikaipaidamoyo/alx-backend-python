#!/usr/bin/env python3
'''
Function to measure runtime of wait_n
'''

import time
from typing import List


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
