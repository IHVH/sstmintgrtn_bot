from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import os
import requests
import datetime
from datetime import datetime


class IndividualBotWithMenu(BotFunctionABC):
    API_POSITION = "http://api.open-notify.org/iss-now.json"
    API_ASTRO = "http://api.open-notify.org/astros.json"

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.menu_buttons = CallbackData('menu_buttons', prefix=commands[0])
        self.agreement_buttons = CallbackData('agreement_buttons', prefix=f'{commands[0]}cosmo')

        @bot.message_handler(commands=commands)
        def welcome_message(message: types.Message):
            bot.send_message(message.chat.id, 'Welcome!\nPlease, choose the option ⬇️', reply_markup=self.create_menu_buttons())

        @bot.callback_query_handler(func=None, config=self.menu_buttons.filter())
        def menu_buttons_callback(call: types.CallbackQuery):
            callback_data: dict = self.menu_buttons.parse(callback_data=call.data)

            button_menu = callback_data['menu_buttons']

            if button_menu == "🛰":
                self.iss_position(call.message)
            if button_menu == "👨‍🚀":
                self.iss_squad(call.message)
            if button_menu == "🌦":
                self.get_weather_agreement(call.message)
            if button_menu == "💸":
                pass

        @bot.callback_query_handler(func=None, config=self.agreement_buttons.filter())
        def agree_buttons_callback(call: types.CallbackQuery):
            callback_data: dict = self.agreement_buttons.parse(callback_data=call.data)
            agreement_button = callback_data['agreement_button']
            self.get_agreement(call.message, agreement_button)

    def create_menu_buttons(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("🛰", callback_data=self.menu_buttons.new(menu_buttons="🛰")),
                   types.InlineKeyboardButton("👨‍🚀", callback_data=self.menu_buttons.new(menu_buttons="👨‍🚀")),
                   types.InlineKeyboardButton("🌦", callback_data=self.menu_buttons.new(menu_buttons="🌦")),
                   types.InlineKeyboardButton("💸", callback_data=self.menu_buttons.new(menu_buttons="💸")))
        return markup

    def iss_position(self, message: types.Message):
        request = requests.get(url=self.API_POSITION)
        response = request.json()

        timestamp = response['timestamp']
        cur_time = (datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S'))

        longitude_r = response['iss_position']['longitude']
        latitude_r = response['iss_position']['latitude']

        self.bot.send_message(message.chat.id, f"Longitude: {longitude_r},\n"
                                               f"Latitude: {latitude_r},\n"
                                               f"Online time: {cur_time}")

        self.bot.send_location(message.chat.id, longitude=longitude_r, latitude=latitude_r)

    def iss_squad(self, message):
        request = requests.get(url=self.API_ASTRO)
        response = request.json()

        for item in response['people']:
            self.bot.send_message(message.chat.id, "🚀: {} | 🧑‍🚀: {}".format(item['craft'], item['name']))

        self.bot.send_message(message.chat.id, f"Total amount of 👨‍🚀 in space ➡️ {response['number']}❕")

    def get_weather_agreement(self, message):
        self.bot.send_message(message.chat.id, "Do you request weather information?", reply_markup=self.create_agreement_buttons())

    def create_agreement_buttons(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("🟢", callback_data=self.agreement_buttons.new(agreement_button="🟢")),
                   types.InlineKeyboardButton("🔴", callback_data=self.agreement_buttons.new(agreement_button="🔴")))
        return markup

    def get_agreement(self, message, txt):
        if txt == "🟢":
            message_from_bot = self.bot.send_message(message.chat.id, "🏢 Write the name of сity: ")
            self.bot.register_next_step_handler(message_from_bot, self.get_weather)
        elif txt == "🔴":
            self.bot.send_message(message.chat.id, "📛 Process has been stoped! 📛")
        elif txt != "🟢" or txt != "🔴":
            self.bot.send_message(message.chat.id, "⛔️ Incorrect input! ⛔ \n"
                                                   "Press 🟢 or 🔴 only!")
            self.get_agreement(message, txt)

    def get_weather(self, message):
        try:
            request = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={self.get_example_token()}&units=metric"
            )
            response = request.json()

            name_of_city = response["name"]
            curr_temperature = response["main"]["temp"]
            temp_feels_like = response["main"]["feels_like"]
            humidity = response["main"]['humidity']
            speed_of_wind = response["wind"]["speed"]
            sunrise = response["sys"]["sunrise"]
            sunrise_timestamp = (datetime.utcfromtimestamp(sunrise).strftime('%H:%M'))
            sunset = response["sys"]["sunset"]
            sunset_timestamp = (datetime.utcfromtimestamp(sunset).strftime('%H:%M'))
            date_time = response["dt"]
            date_time_timestamp = (datetime.utcfromtimestamp(date_time).strftime('%d-%m-%Y %H:%M:%S'))

            self.bot.send_message(message.chat.id, f"⏰ {date_time_timestamp} \n"
                                                   f"🏢 City: {name_of_city} \n"
                                                   f"🌡 Current temperature: {curr_temperature}°C \n"
                                                   f"🌬 Feels like: {temp_feels_like}°C \n"
                                                   f"💧 Humidity: {humidity}% \n"
                                                   f"💨 Wind speed: {speed_of_wind} m/s \n"
                                                   f"🌇 Sunrise: {sunrise_timestamp} \n"
                                                   f"🌃 Sunset: {sunset_timestamp} \n\n"
                                                   f"Have a great day! 😎☀️")
        except Exception as _error:
            print(_error)

            error_on_city_r = self.bot.send_message(message.chat.id, "⛔️ City not found! ⛔️\nWrite city name again: ")
            self.bot.register_next_step_handler(error_on_city_r, self.get_weather)

    def get_example_token(self):
        token = os.environ["WEATHER_TOKEN"]
        return token
