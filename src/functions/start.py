from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import bot_func_dictionary 
from bot_func import BotFunction
import time

class StartInfoBotFunction(BotFunctionABC):
    slip_time = 0.2

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.start_keyboard_factory = CallbackData('start_f_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def start_message_hendler(message: types.Message):
            msg = f'Привет {message.from_user.full_name}! \nВот список доступных функций:'
            bot.send_message(text=msg, chat_id=message.chat.id)
            self.send_messages_bf2(message)
            self.send_messages_bf(message)

        @bot.callback_query_handler(func=None, config=self.start_keyboard_factory.filter())
        def start_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.start_keyboard_factory.parse(callback_data=call.data)
            start_f_button = callback_data['start_f_button']
            function = self.find_function_info(start_f_button)
            self.send_detail_messages(call.message, function)

    def send_messages_bf2(self, message: types.Message):
        for key, val in bot_func_dictionary.BOT_FUNCTIONS_2.items():
            if val.state:
                txt = f'{val.about} \n'
                for command in val.commands:
                    txt += f' - `/{command}` \n'
                #txt += "\n  - /".join(val.commands)
                self.bot.send_message(text=txt, chat_id=message.chat.id, reply_markup=self.gen_markup(key), parse_mode='Markdown')
                time.sleep(self.slip_time)

    def send_messages_bf(self, message: types.Message):
        for key, val in bot_func_dictionary.BOT_FUNCTIONS.items():
            txt = f'{val.about} \n'
            for command in val.commands:
                txt += f' - `/{command}` \n'
            self.bot.send_message(text=txt, chat_id=message.chat.id, reply_markup=self.gen_markup(key), parse_mode='Markdown')
            time.sleep(self.slip_time)

    def find_function_info(self, key: str) -> BotFunction:
        if key in bot_func_dictionary.BOT_FUNCTIONS_2:
            return bot_func_dictionary.BOT_FUNCTIONS_2[key]
        
        if key in bot_func_dictionary.BOT_FUNCTIONS:
            return bot_func_dictionary.BOT_FUNCTIONS[key]
        
    def send_detail_messages(self, message: types.Message, bot_function: BotFunction):
        txt = f'*{bot_function.about}* \n'
        for command in bot_function.commands:
            txt += f' - `/{command}` \n'
        txt += f'{bot_function.description} \n\n*Contributors:* \n'
        for author in bot_function.authors:
            txt += f' - [{author}](https://github.com/{author}) \n'

        self.bot.send_message(text=txt, chat_id=message.chat.id, parse_mode='Markdown')

    def gen_markup(self, key: str):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(types.InlineKeyboardButton("Подробнее", callback_data=self.start_keyboard_factory.new(start_f_button=key)))
        return markup