import requests
import telebot
from telebot import types
from bot_func_abc import BotFunctionABC
from typing import List

class Joke(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        @bot.message_handler(commands=commands)
        def generate_and_answer(message: types.Message):
            res = requests.get('https://api.chucknorris.io/jokes/random')
            res_json = res.json()
            
            
            bot.send_message(message.chat.id, res_json['value'])