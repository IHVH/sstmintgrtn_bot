import requests
import telebot
from telebot import types
from bot_func_abc import BotFunctionABC
from typing import List

class HumanGenerator(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        @bot.message_handler(commands=commands)
        def generate_and_answer(message: types.Message):
            res = requests.get('https://randomuser.me/api/')
            res_json = res.json()
            content = res_json["results"][0]

            answer = {
                "==========\n" +
                "ФИО: "
                        + content["name"]["first"] + " " 
                        + content["name"]["last"] + "\n==========\n" +
                "Пол: "
                        + ("мужской" if content["gender"] == "male" else "женский") + "\n==========\n" +
                "Местоположение: "
                        + content["location"]["city"] + " city, "
                        + content["location"]["street"]["name"] + " st., "
                        + str(content["location"]["street"]["number"]) + "\n==========\n" +
                "Email: "
                        + content["email"] + "\nLogin: "
                        + content["login"]["username"] + "\nPassword: "
                        + content["login"]["password"] + "\n==========\n" +
                "Дата рождения: "
                        + content["dob"]["date"][:10] + " ("
                        + str(content["dob"]["age"]) + " y.o.)\n==========\n" +
                "Номер телефона: "
                        + content["phone"] + "\n==========\n"
            }

            bot.send_photo(message.chat.id, photo=content["picture"]["large"], caption=answer)