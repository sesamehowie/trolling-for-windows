import random
import tkinter as tk
import asyncio
from tkinter import messagebox as mbox
from utils.generate_random_message import message_gen

RAND_DELAY_MBOX = [2, 5]


async def display_error(root, messagebox):
    try:
        message = message_gen()
        title = message.title
        text = message.text
        messagebox.showerror(title, text)
    except Exception as e:
        print(f"Error displaying message: {e}")
        return


async def run_loop():
    delay = random.randint(*RAND_DELAY_MBOX)
    await asyncio.sleep(delay)
    try:
        root = tk.Tk()
        root.attributes("-alpha", 0)
        root.iconify()
        await display_error(root, mbox)
        root.destroy()
        await asyncio.sleep(1)
    except Exception as e:
        print(f"Error in run_loop: {e}")
        await asyncio.sleep(1)
        return
