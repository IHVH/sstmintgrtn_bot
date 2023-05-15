from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import requests

class NYTimes_science(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        api_key = "JOv1U7L6ISqj8jAWPIS3SUHAv33sNfEn"
        self.url = f"https://api.nytimes.com/svc/topstories/v2/science.json?api-key={api_key}"
        self.example_keyboard_factory = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def check_status(message: types.Message):
            response = self.Top_stories()
            bot.send_message(message.chat.id, response)

    def Top_stories(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                
                # Получение списка новостей
                articles = data['results']
                headlines = ""
                
                # Перебор новостей и добавление заголовков в переменную
                for article in articles:
                    title = article['title']
                    headlines += title + '\n'
                    
                # Заголовки новостей в области науки NYTiems
                return headlines
            else:
                return "Произошла ошибка при проверке состояния серверов NYTimes"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при выполнении запроса: {str(e)}"
