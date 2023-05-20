from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import os
import requests

news_list = []
current_news_index = 0


class NewsFeed(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.menu_buttons = CallbackData('menu_buttons', prefix=commands[0])
        self.switch_buttons = CallbackData('switch_buttons', prefix=f'{commands[0]}switch')

        @bot.message_handler(commands=commands)
        def welcome_message(message: types.Message):
            bot.send_message(message.chat.id, 'Добро пожаловать в Новостную Ленту!\nВыберите категорию поиска ⬇️',
                             reply_markup=self.create_menu_buttons())

        @bot.callback_query_handler(func=None, config=self.menu_buttons.filter())
        def menu_buttons_callback(call: types.CallbackQuery):
            callback_data: dict = self.menu_buttons.parse(callback_data=call.data)

            button_menu = callback_data['menu_buttons']

            if button_menu == "🌍 Страна":
                self.get_country_code(call.message)
            if button_menu == "⌨️ Ключевое слово":
                self.get_keyword(call.message)

        @bot.callback_query_handler(func=None, config=self.switch_buttons.filter())
        def switch_buttons_callback(call: types.CallbackQuery):
            global news_list
            global current_news_index
            callback_data: dict = self.switch_buttons.parse(callback_data=call.data)

            switch_buttons_news = callback_data['switch_buttons']

            if switch_buttons_news == "➡️":
                current_news_index = (current_news_index + 1) % len(news_list)
                self.search_by_country(call.message)
            if switch_buttons_news == "⬅️":
                current_news_index = (current_news_index - 1) % len(news_list)
                self.search_by_country(call.message)

    def create_menu_buttons(self):
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🌍 Страна", callback_data=self.menu_buttons.new(menu_buttons="🌍 Страна")),
                   types.InlineKeyboardButton("⌨️ Ключевое слово",
                                              callback_data=self.menu_buttons.new(menu_buttons="⌨️ Ключевое слово")))
        return markup

    def get_country_code(self, message: types.Message):
        global news_list
        news_list.clear()

        message_from_bot = self.bot.send_message(message.chat.id, "Введите название страны (прим. 'ru'): ")
        self.bot.register_next_step_handler(message_from_bot, self.search_by_country)

    def search_by_country(self, message: types.Message):
        global news_list
        global current_news_index

        if len(news_list) == 0:
            request = requests.get(
                f'https://newsapi.org/v2/top-headlines?country={message.text}&apiKey={self.get_news_token()}'
            )
            response = request.json()
            news_list = response['articles']
            current_news_index = 0

        articles = news_list[current_news_index]
        self.bot.send_message(message.chat.id, articles['url'])
        self.bot.send_message(message.chat.id, 'Переключение новостей', reply_markup=self.create_switch_buttons())

    def get_keyword(self, message: types.Message):
        global news_list
        news_list.clear()

        message_from_bot = self.bot.send_message(message.chat.id, "Введите ключевое слово (прим. 'Биткоин'): ")
        self.bot.register_next_step_handler(message_from_bot, self.search_by_keyword)

    def search_by_keyword(self, message: types.Message):
        global news_list
        global current_news_index

        if len(news_list) == 0:
            request = requests.get(
                f'https://newsapi.org/v2/everything?q={message.text}&language=ru&apiKey={self.get_news_token()}'
            )
            response = request.json()
            news_list = response['articles']
            current_news_index = 0

        articles = news_list[current_news_index]
        self.bot.send_message(message.chat.id, articles['url'])
        self.bot.send_message(message.chat.id, 'Переключение новостей', reply_markup=self.create_switch_buttons())

    def create_switch_buttons(self):
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("⬅️", callback_data=self.switch_buttons.new(switch_buttons="⬅️")),
            types.InlineKeyboardButton("➡️", callback_data=self.switch_buttons.new(switch_buttons="➡️")))
        return markup

    def get_news_token(self):
        token = os.environ['NEWS_API_TOKEN']
        return token
<<<<<<< HEAD
=======

>>>>>>> origin/Amulenko_News_Feed
