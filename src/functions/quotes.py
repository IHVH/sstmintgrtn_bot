from typing import List
import telebot
import requests
from telebot.callback_data import CallbackData
from bot_func_abc import BotFunctionABC

class Quotes(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.kf = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def send_welcome(message):
            response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=ru')
            self.bot.send_message(message.chat.id, response.text)
