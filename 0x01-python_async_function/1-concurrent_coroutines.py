#!/usr/bin/env python3
'''
Async routine to execute multiple coroutines
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs multiple instances of wait_random concurrently and returns a list
    of the delays in ascending order.
    '''
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
