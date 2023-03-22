import os
import telebot
from bot_func_abc import BotFunctionABC
from lyricsgenius import Genius
from telebot import types
from typing import List

class GeniusFunction(BotFunctionABC):
	def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
		self.bot = bot 
		@bot.message_handler(commands=commands)
		def example_message_hendler(message: types.Message):
			bot.send_message(text=self.get_lyrics(message), chat_id=message.chat.id)
			
	def get_lyrics(self, message):
		temp = message.text[len("/genius "):].split('-')
		if len(temp) != 2:
			return "Напиши запрос в формате /genius исполнитель - трек"
		genius = Genius(os.environ["GENIUS_TOKEN"])
		song = genius.search_song(temp[1].strip(), temp[0].strip())
		if song is None:
			return "К сожалению, я не смог найти нужный трек"
		else:
			return song.lyrics
		