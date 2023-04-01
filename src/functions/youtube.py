import os
import telebot
import requests
import json
from telebot import types
from typing import List
from bot_func_abc import BotFunctionABC


class YoutubeFinder(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def message_handler(message: types.Message):
            bot.send_message(text=self.YTFinder(message), chat_id=message.chat.id)

    def YTFinder(self, message):
        api_key = os.environ["YTFINDERTOKEN"]
        word = message.text("/YTfind").lower()
        query = word
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={query}&key={api_key}'
        response = requests.get(url)
        data = json.loads(response.text)

        for item in data['items']:
            result = f"Название видео: {item['snippet']['title']}"
            return result

