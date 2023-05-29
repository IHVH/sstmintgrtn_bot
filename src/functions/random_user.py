import telebot
import requests
from telebot import types
from typing import List
from src.bot_func_abc import BotFunctionABC


class RandomUser(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=commands)
        def example_message_handler(message: types.Message):
            res = requests.get('https://randomuser.me/api/')
            res_json = res.json()

            bot.send_photo(message.chat.id, res_json["results"][0]["picture"]["large"])

            user_info = {
                "Пол: " + res_json["results"][0]["gender"] + "\n" +
                "Имя: " + res_json["results"][0]["name"]["first"] + "\n" +
                "Фамилия: " + res_json["results"][0]["name"]["last"] + "\n" +
                "Email: " + res_json["results"][0]["email"] + "\n" +
                "Телефон: " + res_json["results"][0]["phone"] + "\n" +
                "Страна: " + res_json["results"][0]["location"]["country"] + "\n" +
                "Город: " + res_json["results"][0]["location"]["city"] + "\n"
            }
            bot.send_message(message.chat.id, user_info)
