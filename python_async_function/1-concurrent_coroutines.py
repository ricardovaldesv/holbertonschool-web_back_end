#!/usr/bin/env python3
"""
Asynchronous Python script that provides coroutine functions for simulating
random delays and managing concurrent execution.
"""

import asyncio
import random  # Import the random module
from typing import List


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that simulates a random delay.

    Args:
    - max_delay (float): Maximum value for the random delay.

    Returns:
    - float: The generated random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns 'wait_random' n times.

    Args:
    - n (int): Number of times to spawn 'wait_random'.
    - max_delay (int): Maximum value for the random delay.

    Returns:
    - List[float]: List of generated random delays, sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
