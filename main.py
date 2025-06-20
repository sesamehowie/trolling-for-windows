import random
import asyncio
from components.messagebox import run_loop
from components.shell_utils import random_subprocess

RAND_CONSOLE_EXEC = [1, 3]


async def main():
    shells_amt = random.randint(*RAND_CONSOLE_EXEC)
    tasks = []

    for _ in range(shells_amt):
        tasks.append(asyncio.ensure_future(random_subprocess()))

    tasks.append(asyncio.ensure_future(run_loop()))
    random.shuffle(tasks)
    await asyncio.sleep(1)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_forever(asyncio.run(main()))
