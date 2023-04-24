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
            if(message.text.startswith("/how_pass")):
                self.send_how_pass(message)
            else:
                msg = f"Привет {message.from_user.full_name}! \nВот список доступных функций: \n"
                st = self.get_slep_time(message)
                if(self.slip_time != st):
                    msg += f"В группе установлен slow_mode_delay = {st} \n"
                    msg += "Сообщения доставляются с задержкой, некоторые функции могут работать неправильно!"
                bot.send_message(text=msg, chat_id=message.chat.id)
                self.send_messages_bf2(message)
                self.send_messages_bf(message)
                msg_how_pass = "Спросить как сдать зачёт отправь /how_pass "
                time.sleep(st)
                bot.send_message(text=msg_how_pass, chat_id=message.chat.id)

        @bot.callback_query_handler(func=None, config=self.start_keyboard_factory.filter())
        def start_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.start_keyboard_factory.parse(callback_data=call.data)
            start_f_button = callback_data['start_f_button']
            function = self.find_function_info(start_f_button)
            self.send_detail_messages(call.message, function)

    def send_how_pass(self, message: types.Message):
        txt = '''
        Необходимо в общий проект [OEMIB_PI01_19_TBOT](https://github.com/IHVH/OEMIB_PI01_19_TBOT)
добавить свою функцию которая используя какие либо из изученных технологий 
реализует взаимодействие с внешней системой. Необходимо использовать только общедоступные api. 
Функция должна выполнять какое то осмысленное (желательно полезное) действие. 

Для этого в вашем аккаунте на github.com делаете fork репозитария 
Добавляете вашу функцию отдельным фалом в папку `/src/functions/ `
Весь код функции должен быть внутри класса унаследованного от абстрактного класса BotFunctionABC
В репозитории есть пример `example_bot_function.py`  как организовать наследование и код внутри класса 
[example_bot_function.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/functions/example_bot_function.py)
Затем в фале `bot_func_dictionary.py` необходимо добавить информацию о вашей функции в словарь `BOT_FUNCTIONS_2`
[bot_func_dictionary.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/bot_func_dictionary.py)
Если необходимы какие-то токены или другие аутентификационные данные то добавляете информацию о них в файл `README.md`
[README.md](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/README.md)
Протестировав всё локально отправляете Pull request в основной репозиторий.

Вопросы можно задавать, обсуждать в общем телеграм чате [sstmintgrtn](https://t.me/sstmintgrtn).
Список общедоступных api можно посмотреть в [project](https://github.com/users/IHVH/projects/1) 
либо найти подходящий в репозитории [public-apis](https://github.com/IHVH/public-apis)  
        '''        
        
        self.bot.send_message(text=txt, chat_id=message.chat.id, parse_mode='Markdown')


    def send_messages_bf2(self, message: types.Message):
        ts = self.get_slep_time(message=message)
        for key, val in bot_func_dictionary.BOT_FUNCTIONS_2.items():
            if val.state:
                txt = f'{val.about} \n'
                for command in val.commands:
                    txt += f' - `/{command}` \n'
                #txt += "\n  - /".join(val.commands)
                time.sleep(ts)
                self.bot.send_message(text=txt, chat_id=message.chat.id, reply_markup=self.gen_markup(key), parse_mode='Markdown')
                
    def send_messages_bf(self, message: types.Message):
        ts = self.get_slep_time(message=message)
        for key, val in bot_func_dictionary.BOT_FUNCTIONS.items():
            txt = f'{val.about} \n'
            for command in val.commands:
                txt += f' - `/{command}` \n'
            time.sleep(ts)
            self.bot.send_message(text=txt, chat_id=message.chat.id, reply_markup=self.gen_markup(key), parse_mode='Markdown')

    def find_function_info(self, key: str) -> BotFunction:
        if key in bot_func_dictionary.BOT_FUNCTIONS_2:
            return bot_func_dictionary.BOT_FUNCTIONS_2[key]
        
        if key in bot_func_dictionary.BOT_FUNCTIONS:
            return bot_func_dictionary.BOT_FUNCTIONS[key]
        
    def get_slep_time(self, message: types.Message) -> float:
        chat = self.bot.get_chat(message.chat.id)
        ts = self.slip_time
        if(chat.slow_mode_delay):
            ts += chat.slow_mode_delay
        return ts

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