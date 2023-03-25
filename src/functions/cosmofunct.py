from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import os
import requests
import datetime
from datetime import datetime

class CosmoBotFunction(BotFunctionABC):
    API_POSITION = "http://api.open-notify.org/iss-now.json"
    API_ASTRO = "http://api.open-notify.org/astros.json"


    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.example_keyboard_factory = CallbackData('t_key_button', prefix=commands[0])
        self.example_keyboard_factory2 = CallbackData('cosmo_weather', prefix=f'{commands[0]}cosmo')

        
        @bot.message_handler(commands=commands)
        def example_message_hendler(message: types.Message):
            
            bot.send_message(message.chat.id, 'Please, choose option ⬇️', reply_markup=self.gen_markup())



        @bot.callback_query_handler(func=None, config=self.example_keyboard_factory.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.example_keyboard_factory.parse(callback_data=call.data)
            t_key_button = callback_data['t_key_button']

            
            if t_key_button == "🛰":
                self.mks_position(call.message)
            if t_key_button == "👨‍🚀":
                self.mks_squad(call.message)
            if t_key_button == "🌦":
                self.get_agreement(call.message)
            if t_key_button == "💸":
                pass #get_currency(message)
            if t_key_button == "🔄":
                pass #menu(message)
        
        @bot.callback_query_handler(func=None, config=self.example_keyboard_factory2.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.example_keyboard_factory2.parse(callback_data=call.data)
            cosmo_weather = callback_data['cosmo_weather']
            self.say_yes_no(call.message, cosmo_weather)
            
            

    def gen_markup(self):
        

        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("🛰", callback_data=self.example_keyboard_factory.new(t_key_button="🛰")),
                   types.InlineKeyboardButton("👨‍🚀", callback_data=self.example_keyboard_factory.new(t_key_button="👨‍🚀")),
                   types.InlineKeyboardButton("🌦", callback_data=self.example_keyboard_factory.new(t_key_button="🌦")),
                   types.InlineKeyboardButton("💸", callback_data=self.example_keyboard_factory.new(t_key_button="💸")),
                   types.InlineKeyboardButton("🔄", callback_data=self.example_keyboard_factory.new(t_key_button="🔄")))
        return markup


    def mks_position(self, message: types.Message):
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

    def mks_squad(self, message):
        request = requests.get(url=self.API_ASTRO)
        response = request.json()

        for item in response['people']:
            self.bot.send_message(message.chat.id, "🚀: {} | 🧑‍🚀: {}".format(item['craft'], item['name']))

        self.bot.send_message(message.chat.id, f"Total amount of 👨‍🚀 in space ➡️ {response['number']}❕")

    def get_agreement(self, message):
        
        message_from_bot = self.bot.send_message(message.chat.id, "Do you request weather information?", reply_markup=self.gen_markup_weather())
        #self.bot.register_next_step_handler(message_from_bot, self.say_yes_no)

    def gen_markup_weather(self):
        

        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        
        markup.add(types.InlineKeyboardButton("🟢", callback_data=self.example_keyboard_factory2.new(cosmo_weather="🟢")),
                   types.InlineKeyboardButton("🔴", callback_data=self.example_keyboard_factory2.new(cosmo_weather="🔴"))
                   )
        return markup

    def say_yes_no(self, message, txt):
        if txt == "🟢":
            message_from_bot = self.bot.send_message(message.chat.id, "🏢 Write the name of сity: ")
            self.bot.register_next_step_handler(message_from_bot, self.get_weather)
        elif txt == "🔴":
            self.bot.send_message(message.chat.id, "📛 Process has been stoped! 📛")
            #menu(message)
        elif txt != "🟢" or txt != "🔴":
            self.bot.send_message(message.chat.id, "⛔️ Incorrect input! ⛔ \n"
                                            "Press 🟢 or 🔴 only!")
            self.get_agreement(message)

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
            #menu(message)
        except Exception as _error:
            print(_error)

            error_on_city_r = self.bot.send_message(message.chat.id, "⛔️ City not found! ⛔️\nWrite city name again: ")
            self.bot.register_next_step_handler(error_on_city_r, self.get_weather)


    

    def get_example_token(self):
        token = os.environ["WEATHER_TOKEN"]
        return token
