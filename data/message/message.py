from dataclasses import dataclass
from ..enums.levels import Level


@dataclass
class Message:
    level: Level
    text: str
    title: str
