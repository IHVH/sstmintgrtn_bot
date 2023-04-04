import telebot
from typing import List
import requests
from bot_func_abc import BotFunctionABC

class RandomDogAPIFunction(BotFunctionABC):
    def __init__(self):
        self.random_dog_data = "random_dog"

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def random_dog_command(message: telebot.types.Message):
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            url = response.json()["message"]
            markup = self.get_buttons_markup()
            bot.send_photo(chat_id=message.chat.id, photo=url, reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: call.data == self.random_dog_data)
        def random_dog_callback(call: telebot.types.CallbackQuery):
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            url = response.json()["message"]
            markup = self.get_buttons_markup()
            bot.send_photo(chat_id=call.message.chat.id, photo=url, reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id)

    def get_buttons_markup(self) -> telebot.types.InlineKeyboardMarkup:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton(
                text="🐶", callback_data=self.random_dog_data
            )
        )
        return markup
