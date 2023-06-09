import telebot
import requests
from typing import List
from bot_func_abc import BotFunctionABC

class kanyequote(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def kanye_handler(message):
            chat_id = message.chat.id
            response = requests.get("https://api.kanye.rest/")
            data = response.json()
            password = data['quote']
            message_text = f"☆KANYE☆:\n\n {password}"
            bot.send_message(chat_id=chat_id, text=message_text,parse_mode="Markdown")

