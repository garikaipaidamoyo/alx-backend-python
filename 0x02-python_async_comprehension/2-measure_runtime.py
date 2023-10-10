#!/usr/bin/env python3

import asyncio
import time  # Import the time module
from async_comprehension import async_comprehension  # Replace with the correct import statement


async def measure_runtime():
    start_time = time.perf_counter()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()

    return end_time - start_time


async def main():
    return await measure_runtime()

print(asyncio.run(main()))
