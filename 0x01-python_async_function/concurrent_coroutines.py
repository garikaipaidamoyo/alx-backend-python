#!/usr/bin/env python3


import asyncio
from typing import List
from 0-basic_async_syntax import wait_random  # Import the wait_random function correctly


async def wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return results
