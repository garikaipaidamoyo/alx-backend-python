#!/usr/bin/env python3
'''
Function to create an asyncio.Task
'''

import asyncio
from basic_async_syntax import wait_random


async def task_wait_random(max_delay: int) -> float:
    '''
    Creates an asyncio.Task for wait_random and returns it.
    '''
    return asyncio.create_task(wait_random(max_delay))
