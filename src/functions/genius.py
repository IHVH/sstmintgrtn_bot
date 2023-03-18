import os
from lyricsgenius import Genius

class GeniusFunction(BotFunctionABC):
	def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
		self.bot = bot 
		@bot.message_handler(commands=commands)
		def example_message_hendler(message: types.Message):
			self.get_lyrics(message):

	def get_lyrics(self, message):
		temp = message.split('-')
		if len(temp) != 2:
			return "Напиши запрос в формате /genius исполнитель - трек"
		genius = Genius(os.environ["GENIUS_TOKEN"])
		song = genius.search_song(temp[0].strip(), temp[1].strip())
		if song is None:
			bot.send_message(text="К сожалению, я не смог найти нужный трек", chat_id=message.chat.id, reply_markup=self.gen_markup())
		else:
			bot.send_message(text=song.lyrics, chat_id=message.chat.id, reply_markup=self.gen_markup())
		