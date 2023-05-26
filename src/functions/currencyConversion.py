from typing import List
from unittest.mock import call
import telebot
from telebot import types
from bot_func_abc import BotFunctionABC

class CurrencyConversion(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        amount = 0
        @bot.message_handler(commands=commands)
        def start(message):
            bot.send_message(message.chat.id, 'Привет,введите сумму')
            bot.register_next_step_handler(message, summa)

        def summa(message):
            global amount
            try:
                amount = int(message.text.strip())
            except ValueError:
                bot.send_message(message.chat.id, 'Неверный формат,введите сумму')
                bot.register_next_step_handler(message, summa)
                return
            if amount > 0:
                markup = types.InlineKeyboardMarkup(row_width=2)
                btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
                btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
                btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
                btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
                markup.add(btn1, btn2, btn3, btn4)
                bot.send_message(message.chat.id, 'Выбирите пару валют', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Чило должно быть больше 0 ,введите сумму')
                bot.register_next_step_handler(message, summa)

        @bot.callback_query_handler(func=lambda call: True)
        def callback(call, currency=None):
            if call.data != 'else':
                values = call.data.upper().split('/')
                res = currency.convert(amount, values[0], values[1])
                bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}.Можете заново вписать сумму')
                bot.register_next_step_handler(call.message, summa)
            else:
                bot.send_message(call.message.chat.id, 'Введите пару значений через слэш')
                bot.register_next_step_handler(call.message, mycurrency)

        def mycurrency(message, currency=None):
            try:
                values = message.text.upper().split('/')
                res = currency.convert(amount, values[0], values[1])
                bot.send_message(message.chat.id, f'Получается: {round(res, 2)}  .Можете заново вписать сумму')
                bot.register_next_step_handler(call.message, summa)
            except Exception:
                bot.send_message(message.chat.id, 'Что-то не так. Впишите сумму')
                bot.register_next_step_handler(message, summa)
