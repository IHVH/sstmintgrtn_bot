import requests
import telebot
from telebot import types
from bot_func_abc import BotFunctionABC
from typing import List

class GetBotHostIP(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        @bot.message_handler(commands=commands)
        def generate_and_answer(message: types.Message):

            input_str = message.text.split()
            ip = input_str[-1]

            res_loc = requests.get('https://ipinfo.io/' + ip + '/geo')
            res_json = res_loc.json()

            if "status" in res_json:
                bot_loc_info = {"Неверно введённый IP-адрес!"}
            else:
                bot_loc_info = {
                            "IP-адрес хоста бота: " + res_json["ip"] + ";\n" +
                            "Временной пояс: " + res_json["timezone"] + ";\n" +
                            "Страна: " + res_json["country"] + ";\n" +
                            "Регион: " + res_json["region"] + ";\n" +
                            "Город: " + res_json["city"] + ";\n" +
                            "Провайдер: " + res_json["org"] + ";\n" +
                            "GEO: " + res_json["loc"] + ";\n"
                            }

            bot.send_message(message.chat.id, bot_loc_info)
