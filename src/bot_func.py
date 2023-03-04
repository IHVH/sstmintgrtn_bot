from dataclasses import dataclass
from bot_func_abc import BotFunctionABC

@dataclass
class BotFunction:
    commands: list[str]
    authors: list[str]
    about: str
    description: str

@dataclass
class BotFunction2(BotFunction):
    bot_function: BotFunctionABC
    