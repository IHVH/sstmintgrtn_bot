from bot_func_abc import BotFunctionABC
import telebot
import webbrowser
from typing import List
import requests
import json

API = '5e364448-2bb1-4f9d-9395-a6b8a19fb20c'

class PlaneSearchClass(BotFunctionABC):

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands=[commands[0]])
        def main(message):
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} введите номер рейса')

            bot.register_next_step_handler(message, get_flight)

        @bot.message_handler(commands=[commands[1], commands[2]])
        def site(message):
            webbrowser.open(f'https://ru.flightaware.com/live/')

        def get_flight(message):
            flight_list = message.text.strip().split()
            flight = ''.join(flight_list)
            res = requests.get(f'https://airlabs.co/api/v9/flight?flight_iata={flight}&api_key={API}')
            data = json.loads(res.text)

            if "error" in data and data['error']:
                bot.reply_to(message, data['error']['message'])

                return

            bot.reply_to(message, f'Рейс: {data["response"]["flight_number"]}\n'
                                  f'Время прибытия(местное): {data["response"]["arr_time"]}\n'
                                  f'Аэропорт прилета: {data["response"]["arr_iata"]}\n'
                                  f'Самолет: {data["response"]["airline_icao"]}\n'
                                  f'Авиалинии:{data["response"]["airline_iata"]}'
                                  f'')


