import logging
import telebot
from telebot.handler_backends import BaseMiddleware
import os

class Middleware(BaseMiddleware):
    
    def pre_process(self, message, data):
        raise NotImplementedError

    def post_process(self, message, data, exception):
        raise NotImplementedError

    def __init__(self, logger: logging.Logger, bot: telebot.TeleBot):
        self.update_types = ['message', 'callback_query']
        self.logger = logger
        self.update_sensitive = True
        self.bot = bot
        self.admt = self.get_admt()

    def pre_process_message(self, message: telebot.types.Message, data):
        self.logger.info(Middleware.create_text_from_message(message))
        
    def post_process_message(self, message: telebot.types.Message, data, exception=None):
        if self.admt != None:
            self.bot.send_message(text=Middleware.create_text_from_message(message), chat_id=self.admt)
        if exception:
            self.logger.exception(exception)
    
    @staticmethod
    def create_text_from_message(message: telebot.types.Message)-> str:
        return f'| {message.chat.id} | {message.from_user.username} {message.from_user.full_name} --> {message.text}'

    def pre_process_callback_query(self, call: telebot.types.CallbackQuery, data):
        self.logger.info(Middleware.create_text_from_callback_query(call))
    
    def post_process_callback_query(self, call: telebot.types.CallbackQuery, data, exception=None):
        if self.admt != None:
            self.bot.send_message(text=Middleware.create_text_from_callback_query(call), chat_id=self.admt)
        if exception:
            self.logger.exception(exception)

    @staticmethod
    def create_text_from_callback_query(call: telebot.types.CallbackQuery)-> str:
        return f'| {call.message.chat.id} | {call.message.from_user.username} {call.message.from_user.full_name} --> {call.message.text} \
             | {call.from_user.username} {call.from_user.full_name} --> {call.data}'

    def get_admt(self):
        if "ADMT" in os.environ:
            return os.environ["ADMT"]
        return None