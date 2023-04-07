import telebot
import requests
from bot_func_abc import BotFunctionABC
from telebot import types
from typing import List

class CatFunction(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        @bot.message_handler(commands=commands)
        def example_message_handler(message: types.Message):
            res = requests.get('https://api.thecatapi.com/v1/images/search')
            res_json = res.json()
            bot.send_photo(message.from_user.id, res_json[0]['url'])
  