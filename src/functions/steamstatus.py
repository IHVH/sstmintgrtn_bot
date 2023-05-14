from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import requests

class ServerStatus(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.url = "https://steamstat.us/"
        self.example_keyboard_factory = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def check_status(message: types.Message):
            response = self.check_server_status()
            bot.send_message(message.chat.id, response)

    def check_server_status(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return "Серверы Steam работают в нормальном режиме"
            else:
                return "Произошла ошибка при проверке состояния серверов Steam"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при выполнении запроса: {str(e)}"
