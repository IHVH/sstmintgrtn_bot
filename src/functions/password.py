import telebot
import requests
from typing import List
from bot_func_abc import BotFunctionABC

class RandomPassword(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def password_generator_handler(message):
            chat_id = message.chat.id
            response = requests.get("https://passwordinator.onrender.com/password")
            data = response.json()
            password = data['data']
            message_text = f"Here's your new password: {password}"
            bot.send_message(chat_id=chat_id, text=message_text)

