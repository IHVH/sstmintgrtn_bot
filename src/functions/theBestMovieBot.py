from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from typing import List
import requests
import json


class TheBestMovieBot(BotFunctionABC):

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        # Функция для получения информации о фильме из API
        def get_movie_info(title):
            api_key = "9dd91112"
            url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
            res = requests.get(url)
            data = json.loads(res.text)

            return data

        @bot.message_handler(commands=[commands[0]])
        def start(message):
            bot.send_message(message.chat.id,
                             "Привет! Хотите узнать, какой фильм самый лучший? Вот, это САМЫЙ ЛУЧШИЙ фильм:")

            movie_handler(message, True)

        @bot.message_handler(commands=[commands[1]])
        def recommendation(message):
            bot.send_message(message.chat.id,
                             "Вы действительно хотите посмотреть что-то другое? Ну ладно. Вводите название (На английском):")

            bot.register_next_step_handler(message, movie_handler)

        @bot.message_handler(commands=[commands[2]])
        def theBestMovieList(message):
            bot.send_message(message.chat.id, "Вот список лучших фильмов:"
                             + "\n 1. Драйв (Drive)"
                             + "\n 2. Бегущий по лезвию 2049 (Blade runner 2049)"
                             + "\n 3. Американский психопат (American psycho)"
                             + "\n 4. Нападение на рио браво (gunfight at rio bravo)"
                             )

        # Обработчик сообщений с названием фильма
        def movie_handler(message, theBestFilm=False):
            movie_title = message.text

            if theBestFilm:
                movie_title = 'Drive'

            movie_info = get_movie_info(movie_title)

            if movie_info['Response'] != 'False':
                title = movie_info["Title"]
                year = movie_info["Year"]
                plot = movie_info["Plot"]
                rating = movie_info["imdbRating"]
                imdb_id = movie_info["imdbID"]
                imdb_url = f"https://www.imdb.com/title/{imdb_id}/"

                response = f"Фильм: {title}\nГод: {year}\nРейтинг: {rating}\n\n{plot}\n\n{imdb_url}"

                keyboard = types.InlineKeyboardMarkup(row_width=1)
                button = types.InlineKeyboardButton(text="Подробнее", url=imdb_url)
                keyboard.add(button)

                bot.send_message(message.chat.id, text=response, reply_markup=keyboard)
            else:
                response = "Не удалось получить информацию о фильме."
                message.reply(response)
