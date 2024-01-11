#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random
delay between 0 and max_delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> int:
    """Generate a random delay using random.uniform(0, max_delay)"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    """
    Asynchronous coroutine that calls wait_random.
    """
    result: int = await wait_random()


if __name__ == "__main__":
    asyncio.run(main())
