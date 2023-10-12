#!/usr/bin/env python3
'''
Function to create an asyncio.Task for wait_n
'''

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs multiple instances of wait_random concurrently using asyncio.Task
    and returns a list of the delays in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
