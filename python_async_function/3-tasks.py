#!/usr/bin/env python3
"""
Creating an asyncio.Task from an asynchronous coroutine.
"""

import asyncio
import importlib
import random
from typing import Any

# Import wait_random using importlib
module = importlib.import_module('0-basic_async_syntax')
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
    - max_delay (int): Maximum delay for wait_random.

    Returns:
    - asyncio.Task: Task representing the execution of wait_random.
    """
    return asyncio.ensure_future(wait_random(max_delay))


if __name__ == "__main__":
    asyncio.run()
