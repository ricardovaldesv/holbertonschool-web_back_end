#!/usr/bin/env python3
"""
Script to measure the runtime of the wait_n coroutine.
"""

import asyncio
import time
import random
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


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per iteration for wait_n.

    Args:
    - n (int): Number of iterations.
    - max_delay (int): Maximum value for the random delay.

    Returns:
    - float: Average time per iteration in seconds.
    """
    start_time = time.time()

    # Use asyncio.run to run the asynchronous wait_n function
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate average time per iteration
    average_time_per_iteration = total_time / n

    return average_time_per_iteration


if __name__ == "__main__":
    average_time = measure_time(n_iterations, max_delay_value)
