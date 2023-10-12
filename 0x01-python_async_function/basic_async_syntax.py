#!/usr/bin/env python3

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time (up to max_delay) and return it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
