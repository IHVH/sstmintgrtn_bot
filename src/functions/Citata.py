import requests
import telebot
from telebot import types
from bot_func_abc import BotFunctionABC
from typing import List

class CitataGenerator(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        @bot.message_handler(commands=commands)
        def generate_and_answer(message: types.Message):
            res = requests.get('https://animechan.vercel.app/api/random')
            res_json = res.json()
            bot.send_message(message.chat.id, {res_json["anime"] + " - " + res_json["character"] + "\n" + res_json["quote"]})
