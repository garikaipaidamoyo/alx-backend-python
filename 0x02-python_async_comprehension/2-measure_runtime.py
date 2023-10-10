#!/usr/bin/env python3

import asyncio

# Import the async_comprehension function from async_comprehension.py (without hyphen)
from async_comprehension import async_comprehension

# Rest of your code remains the same


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension
    four times in parallel.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time


async def main():
    """
    Asynchronously print the total runtime.
    """
    print(await measure_runtime())

print(asyncio.run(main()))
