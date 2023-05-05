from bot_func_abc import AtomicBotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import os

class ExampleBotFunction(AtomicBotFunctionABC):
    commands: List[str] = ["example", "ebf"]
    authors: List[str] = ["IHVH"]
    about: str = "Пример функции бота!"
    description: str = """В поле  *description* поместите подробную информацию о работе функции. 
    Описание способов использования, логики работы. Примеры вызова функции - /ebf 
    Возможные параметры функции `/example`  """
    state: bool = True

    def set_handlers(self, bot: telebot.TeleBot):
        self.bot = bot 
        self.example_keyboard_factory = CallbackData('t_key_button', prefix=self.commands[0])

        @bot.message_handler(commands=self.commands)
        def example_message_hendler(message: types.Message):
            msg = f"Ваш запрос обработан в ExampleBotFunction! \nUSER ID = {message.from_user.id} \nEXAMPLETOKEN = {self.get_example_token()}"
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
                case ('force_reply'):
                    force_reply = types.ForceReply(selective=False)
                    bot.send_message(call.message.chat.id, "Отправьте текст для обработки в process_next_step", reply_markup=force_reply)
                    bot.register_next_step_handler(call.message, self.process_next_step)
                case _:
                    bot.answer_callback_query(call.id, call.data)

    def get_example_token(self):
        token = os.environ.get("EXAMPLETOKEN")
        return token

    def gen_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("Да", callback_data=self.example_keyboard_factory.new(t_key_button="cb_yes")),
                   types.InlineKeyboardButton("Нет", callback_data=self.example_keyboard_factory.new(t_key_button="cb_no")),
                   types.InlineKeyboardButton("ForceReply", callback_data=self.example_keyboard_factory.new(t_key_button="force_reply")), )
        return markup

    def process_next_step(self, message):
        try:
            chat_id = message.chat.id
            txt = message.text
            if txt != "exit":
                force_reply = types.ForceReply(selective=False)
                msg = self.bot.send_message(message.chat.id, f"text = {txt}; chat.id = {chat_id}; \n Для выхода из диалога введите - exit", reply_markup=force_reply)
                self.bot.register_next_step_handler(msg, self.process_next_step)
        except ValueError:
            raise
        except Exception as e:
            self.bot.reply_to(message, f"Exception - {e}")