from bot_func_abc import BotFunctionABC
import telebot
import requests
from telebot import types
from telebot.callback_data import CallbackData
from typing import List


class GetCurrencyExchangeRate(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.ex_kf = CallbackData('t_key_button', prefix=commands[0])
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'

        @bot.message_handler(commands=commands)
        def currency_exchange_handler(message: types.Message):
            bot.send_message(
                text="Привет! Курс какой валютной пары вы хотите узнать?",
                chat_id=message.chat.id,
                reply_markup=self.generate_markup()
            )

        @bot.callback_query_handler(func=None, config=self.ex_kf.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            currency_code = self.ex_kf.parse(callback_data=call.data)['t_key_button']
            bot.send_message(text=self.currency_request_processing(currency_code), chat_id=call.message.chat.id)

    def generate_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 4
        markup.add(
            types.InlineKeyboardButton("USD/RUB", callback_data=self.ex_kf.new(t_key_button="USD")),
            types.InlineKeyboardButton("EUR/RUB", callback_data=self.ex_kf.new(t_key_button="EUR")),
            types.InlineKeyboardButton("CNY/RUB", callback_data=self.ex_kf.new(t_key_button="CNY")),
            types.InlineKeyboardButton("TRY/RUB", callback_data=self.ex_kf.new(t_key_button="TRY")),
            types.InlineKeyboardButton("GBP/RUB", callback_data=self.ex_kf.new(t_key_button="GBP")),
            types.InlineKeyboardButton("BYN/RUB", callback_data=self.ex_kf.new(t_key_button="BYN")),
            types.InlineKeyboardButton("KZT/RUB", callback_data=self.ex_kf.new(t_key_button="KZT")),
            types.InlineKeyboardButton("JPY/RUB", callback_data=self.ex_kf.new(t_key_button="JPY")),
        )
        return markup

    def currency_request_processing(self, currency_code: str) -> str:
        json = requests.get(self.url).json()

        currency_full_name = json['Valute'][currency_code]['Name']
        rub_to_currency = json['Valute'][currency_code]['Value']
        currency_to_rub = 1. / rub_to_currency if rub_to_currency > 0. else 0.

        text_response = f"""
            Текущая цена за единицу валюты {currency_full_name} составляет {rub_to_currency} рублей\n
            Текущая цена за 1 рубль составляет {currency_to_rub} {currency_full_name}
        """

        return text_response