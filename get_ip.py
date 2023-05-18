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
            res_ip = requests.get('https://api.ipify.org/?format=json')
            res_json = res_ip.json()
            bot_host_ip = res_json["ip"]

            res_loc = requests.get('https://ipinfo.io/' + bot_host_ip + '/geo')
            res_json = res_loc.json()
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