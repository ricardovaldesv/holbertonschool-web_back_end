#!/usr/bin/env python3
'''measure_runtime coroutine that will execute
async_comprehension four times in parallel
using asyncio.gather'''

import asyncio
import random
from typing import Generator, List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime coroutine that will execute
    async_comprehension four times in parallel
    using asyncio.gather'''
    start_time = time.time()
    result = await asyncio.gather(async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
