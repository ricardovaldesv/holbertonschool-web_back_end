#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random
delay between 0 and max_delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Generate a random delay using random.uniform(0, max_delay)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """
    Asynchronous coroutine that calls wait_random.
    """
    result = await wait_random()


if __name__ == "__main__":
    asyncio.run(main())
