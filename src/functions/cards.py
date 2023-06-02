import requests
import telebot
from bot_func_abc import BotFunctionABC
from telebot import types
from typing import List

class RandomCard(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        
        @bot.message_handler(commands=commands)
        def example_message_handler(message: types.Message):
            url = "https://deckofcardsapi.com/api/deck/new/draw/?count=2"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                cards = data['cards']
                bot.send_photo(message.from_user.id, cards[0]['image'])