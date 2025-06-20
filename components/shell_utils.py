import subprocess
from subprocess import CREATE_NEW_CONSOLE, PIPE
import random
import asyncio

RAND_DELAY_SHELL = [30, 60]


async def random_subprocess():
    try:
        delay = random.randint(*RAND_DELAY_SHELL)
        await asyncio.sleep(delay)
        random_res = random.choice([True, False])
        if random_res:
            process = subprocess.Popen(
                random.choice["cmd", "powershell.exe"],
                creationflags=CREATE_NEW_CONSOLE,
                stdin=PIPE,
            )
            process.communicate("exit\n")
        return True
    except Exception:
        return await random_subprocess()
