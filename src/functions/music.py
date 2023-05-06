import os
from typing import List

import telebot
import requests
from telebot.callback_data import CallbackData

from src.bot_func_abc import BotFunctionABC


class Music(BotFunctionABC):

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.kf = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def send_welcome(message):
            message_from_bot = bot.send_message(message.chat.id, 'Привет! Введите имя артиста или название альбома, о котором хотите узнать.')
            bot.register_next_step_handler(message_from_bot, search_artist_or_album)


        @bot.message_handler(func=lambda message: True)
        def search_artist_or_album(message):
            query = message.text
            search_url = f'http://ws.audioscrobbler.com/2.0/?method=album.search&album={query}&api_key={self.get_music_token()}&format=json'
            search_result = requests.get(search_url).json()
            albums = search_result['results']['albummatches']['album']
            if len(albums) == 0:
                self.bot.reply_to(message, 'Не удалось найти информацию об этом артисте или альбоме.')
            else:
                for album in albums[:5]:
                    album_name = album['name']
                    artist_name = album['artist']
                    album_url = album['url']
                    reply_text = f'🎵 {artist_name} - {album_name}\n\nТреклист:\n{album_url}'
                    self.bot.send_message(message.chat.id, reply_text)

    def get_music_token(self):
        token = os.environ["API_MUSIC"]
        return token
