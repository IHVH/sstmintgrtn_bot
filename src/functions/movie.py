from typing import List
import telebot
from telebot import types
import requests
from bot_func_abc import BotFunctionABC


class imdbFinder(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def start_command(message: types.Message):
            bot.send_message(message.chat.id, "Напиши название фильма или сериала")
            bot.register_next_step_handler(message, get_movie) 

        def get_movie(message: types.Message):
            try:
                r = requests.get(f"http://www.omdbapi.com/?t={message.text}&apikey=9fae2b5c")
                data = r.json()

                if (data["Type"] == "movie"):
                    bot.send_photo(message.chat.id, data["Poster"])
                    movie_info = {
                        "Название: " + data["Title"] + "\n" +
                        "Тип: " + data["Type"] +"\n" +
                        "Дата релиза: " + data["Released"] +"\n" +
                        "Продолжительность: " + data["Runtime"] +"\n" +
                        "Жанр: " + data["Genre"] +"\n" +
                        "Рейтинг на imdb: " + data["imdbRating"] +"\n" +
                        "Описание: " + data["Plot"] +"\n"
                    }

                    bot.send_message(message.from_user.id, movie_info)

                if (data["Type"] == "series"):
                    bot.send_photo(message.chat.id, data['Poster'])
                    series_info = {
                        "Название: " + data["Title"] + "\n" +
                        "Тип: " + data["Type"] +"\n" +
                        "Сезонов: " + data["totalSeasons"] +"\n" +
                        "Дата релиза: " + data["Released"] +"\n" +
                        "Продолжительность одной серии: " + data["Runtime"] +"\n" +
                        "Жанр: " + data["Genre"] +"\n" +
                        "Рейтинг на imdb: " + data["imdbRating"] +"\n" +
                        "Описание: " + data["Plot"] +"\n"
                    }

                bot.send_message(message.from_user.id, series_info)
    
            except:
                bot.send_message(message.chat.id, "Неверное название")
