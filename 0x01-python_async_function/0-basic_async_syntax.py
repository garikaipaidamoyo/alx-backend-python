#!/usr/bin/env python3
'''
Module for asynchronous coroutine
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay as a float.
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
