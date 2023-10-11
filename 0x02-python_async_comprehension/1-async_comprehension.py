#!/usr/bin/env python3

import asyncio
import random  # Import the random module
from async_generator import async_generator


async def async_comprehension():
    results = [value async for value in async_generator()]
    return results
