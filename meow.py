import telebot
import requests
from typing import List
from bot_func_abc import BotFunctionABC

class meowfact(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
             
        @bot.message_handler(commands=commands)
        def cat_fact_handler(message):
            chat_id = message.chat.id
            
            response = requests.get("https://catfact.ninja/fact")
            data = response.json()
            fact = data['fact']
            message_text = "💓Meow fact💓\n\n" + fact 
            bot.send_message(chat_id=chat_id, text=message_text)
    
