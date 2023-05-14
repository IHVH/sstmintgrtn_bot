from bot_func_abc import BotFunctionABC
from telebot import types
import requests

class ServerStatus(BotFunctionABC):
    def __init__(self):
        self.url = "https://steamstat.us/"

        @bot.message_handler(commands=commands)
        def check_status(message: types.Message):
            response = self.check_server_status()
            self.bot.send_message(message.chat.id, response)

    def check_server_status(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return "Серверы Steam работают в нормальном режиме"
            else:
                return "Произошла ошибка при проверке состояния серверов Steam"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при выполнении запроса: {str(e)}"
