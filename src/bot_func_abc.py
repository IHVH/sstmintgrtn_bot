from typing import List
from abc import ABC, abstractmethod
import telebot

class BotFunctionABC(ABC):
    @abstractmethod
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        @bot.message_handler(commands=commands)
        def hendler(message):
            msg = "Ваш запрос обработан в базовом абстрактном класе!!!"
            print(msg)
            bot.send_message(text=msg, chat_id=message.chat.id)