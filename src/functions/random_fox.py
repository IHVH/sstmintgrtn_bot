import telebot
import requests
from telebot import types
from typing import List
from src.bot_func_abc import BotFunctionABC


class RandomFox(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def example_message_handler(message: types.Message):
            res = requests.get('https://randomfox.ca/floof')
            res_json = res.json()

            bot.send_photo(message.chat.id, res_json["image"])
            bot.send_message(message.chat.id, "Лис рандомный обыкновенный")
