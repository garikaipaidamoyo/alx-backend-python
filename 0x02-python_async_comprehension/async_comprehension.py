#!/usr/bin/env python3

import asyncio
from typing import List

# Import the async_generator function from async_generator.py (without hyphen)
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous comprehension that collects 10 random numbers
    using async_generator and returns them as a list.
    """
    return [i async for i in async_generator()]


# Example of how to use it
async def main():
    print(await async_comprehension())

asyncio.run(main())
