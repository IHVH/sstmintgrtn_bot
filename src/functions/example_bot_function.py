from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import os

class ExampleBotFunction(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.example_keyboard_factory = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def example_message_hendler(message: types.Message):
            msg = f'Ваш запрос обработан в ExampleBotFunction! EXAMPLETOKEN={self.get_example_token()}'
            print(msg)
            bot.send_message(text=msg, chat_id=message.chat.id, reply_markup=self.gen_markup())

        @bot.callback_query_handler(func=None, config=self.example_keyboard_factory.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.example_keyboard_factory.parse(callback_data=call.data)
            t_key_button = callback_data['t_key_button']
    
            match (t_key_button):
                case ('cb_yes'):
                    bot.answer_callback_query(call.id, "Ответ ДА!")
                case ('cb_no'):
                    bot.answer_callback_query(call.id, "Ответ НЕТ!")
                case _:
                    bot.answer_callback_query(call.id, call.data)


    def get_example_token(self):
        token = os.environ["EXAMPLETOKEN"]
        return token

    def gen_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("Да", callback_data=self.example_keyboard_factory.new(t_key_button="cb_yes")),
                   types.InlineKeyboardButton("Нет", callback_data=self.example_keyboard_factory.new(t_key_button="cb_no")))
        return markup
