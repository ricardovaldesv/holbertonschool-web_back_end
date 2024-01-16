#!/usr/bin/env python3
"""
Creating an asyncio.Task from an asynchronous coroutine.
"""

import asyncio
import importlib
from typing import List

# Import wait_random using importlib
module = importlib.import_module('0-basic_async_syntax')
wait_random = module.wait_random


async def task_wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that creates an asyncio.Task for wait_random.

    Args:
    - max_delay (int): Maximum delay for wait_random.

    Returns:
    - float: The generated random delay.
    """
    task = asyncio.ensure_future(wait_random(max_delay))
    await task
    return task.result()


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns 'task_wait_random' n times.

    Args:
    - n (int): Number of times to spawn 'task_wait_random'.
    - max_delay (int): Maximum value for the random delay.

    Returns:
    - List[float]: List of generated random delays, sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
