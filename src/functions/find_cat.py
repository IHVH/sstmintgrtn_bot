import json
from typing import List

import telebot
import requests

from bot_func_abc import BotFunctionABC
from telebot.callback_data import CallbackData


class FindCat(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        FIND_CAT_TOKEN = '6068655722:AAH-8jQPyRhBxc_fO-Tp1eHnelDmx7f8iJY'
        self.bot = bot
        self.kf = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def start_message(message):
            self.bot.send_message(message.chat.id,
                                  "Привет! Я бот для поиска фотографий котов по породам. Введи /find_cat, для поиска породы кота. ")

            # Отправляем сообщение с запросом породы кота
            self.bot.send_message(message.chat.id, "Введите название породы кота:")

            # Ожидаем ответ от пользователя
            @bot.message_handler(func=lambda message: True)
            def process_message(message):
                try:
                    # Формируем запрос к API TheCatAPI
                    query = message.text.lower()
                    url = 'https://api.thecatapi.com/v1/breeds/search'
                    headers = {'x-api-key': 'live_CEkzkNtTPsfZKsefEFBYiXpyBkGtq2cPRRQG6NnkhqctfW8xnSuKYBNKw33JTgVo'}
                    params = {'q': query}

                    # Отправляем запрос к API
                    response = requests.get(url, headers=headers, params=params)

                    # Обрабатываем ответ API
                    data = json.loads(response.text)
                    if len(data) == 0:
                        self.bot.send_message(message.chat.id, "К сожалению, я не нашел информацию о данной породе кота")
                    else:
                        breed = data[0]
                        name = breed['name']
                        description = breed['description']
                        photo_url = f"https://cdn2.thecatapi.com/images/{breed['reference_image_id']}.jpg"

                        # Отправляем фото и информацию о породе
                        self.bot.send_photo(message.chat.id, photo_url, caption=f"<b>{name}</b>\n{description}",
                                       parse_mode="HTML")
                except Exception as e:
                    self.bot.send_message(message.chat.id, "Произошла ошибка при обработке запроса")
                    print(f"Error: {e}")
