import os
import random
from data.message.message import Message
from data.enums.levels import Level
from data.config import (
    WINDOWS_ERROR_CODES,
    WINDOWS_SYS_FILENAMES,
    DISKNAME,
    FOLDER_NAMES,
    COMMANDS,
)


def generate_random_path():
    from pathlib import Path

    random_folder = random.choice(FOLDER_NAMES)
    starting_path = os.path.join(Path(DISKNAME), Path(random_folder))
    random_filename = random.choice(WINDOWS_SYS_FILENAMES)
    return os.path.join(starting_path, random_filename)


def generate_random_command():
    return random.choice(COMMANDS)


def message_gen():
    random_message = random.choice(WINDOWS_ERROR_CODES)
    message_type = random_message["type"]
    new_message_text = random_message["text"]
    message_level = Level.ERROR

    match message_type:
        case "path":
            new_message_text = new_message_text.format(generate_random_path())
        case "command":
            new_message_text = new_message_text.format(generate_random_command())
        case "_":
            new_message_text = new_message_text

    random_message["text"] = new_message_text
    return Message(message_level, random_message["text"], random_message["title"])
