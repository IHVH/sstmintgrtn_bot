from typing import List

import telebot
import requests
from bs4 import BeautifulSoup
from telebot.callback_data import CallbackData

from src.bot_func_abc import BotFunctionABC


class Quotes(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.kf = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def send_welcome(message):
            self.bot.reply_to(message,
                              'Привет! Я бот для получения цитат и афоризмов из русских источников. Введите /quote, чтобы получить случайную цитату.')

            response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=ru')
            soup = BeautifulSoup(response.text, 'html.parser')
            quote = soup.get_text()
            self.bot.reply_to(message, quote)
