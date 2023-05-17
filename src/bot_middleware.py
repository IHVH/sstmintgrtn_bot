import os
import logging
import telebot
from telebot.handler_backends import BaseMiddleware
from db.storage_worker import StorageWorker
from db.models_msg_log import User, Chat, Message

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
        self.storage_worker = self.get_storage_worker()

    def pre_process_message(self, message: telebot.types.Message, data):
        self.logger.info(Middleware.create_text_from_message(message))
        
    def post_process_message(self, message: telebot.types.Message, data, exception=None):
        self.save_message(message, None)
        if exception:
            self.logger.exception(exception)
    
    @staticmethod
    def create_text_from_message(message: telebot.types.Message)-> str:
        return f'| {message.chat.id} | {message.from_user.username} {message.from_user.full_name} --> {message.text}'

    def pre_process_callback_query(self, call: telebot.types.CallbackQuery, data):
        self.logger.info(Middleware.create_text_from_callback_query(call))
    
    def post_process_callback_query(self, call: telebot.types.CallbackQuery, data, exception=None):
        self.save_message(call.message, f"{call.from_user.username} --> {call.data}")
        if exception:
            self.logger.exception(exception)

    @staticmethod
    def create_text_from_callback_query(call: telebot.types.CallbackQuery)-> str:
        return f'| {call.message.chat.id} | {call.message.from_user.username} {call.message.from_user.full_name} --> {call.message.text} \
             | {call.from_user.username} {call.from_user.full_name} --> {call.data}'

    def get_storage_worker(self)-> StorageWorker | None:
        conection_string = os.environ.get("CONECTION_PGDB")
        if(conection_string):
            storage_worker = StorageWorker(conection_string)
            self.logger.info(f"Added storage_worker with CONECTION_PGDB = {conection_string}")
            return storage_worker
        else:
            self.logger.info("Not added storage_worker")
            return None

    def save_message(self, message: telebot.types.Message, data: str | None):
        if self.storage_worker:
            user = self.storage_worker.get_user(message.from_user.id)
            if user is None:
                user = self.new_user_from_tgmessage(message)
                user = self.storage_worker.save_user(user)
            chat = self.storage_worker.get_chat(message.chat.id)
            if chat is None:
                chat = self.new_chat_from_tgmessage(message)
                chat = self.storage_worker.save_chat(chat)
            message = self.new_message(user, chat, message.text, data)
            self.storage_worker.save_message(message)

    def new_user_from_tgmessage(self, message: telebot.types.Message)-> User:
        user = User()
        user.id = message.from_user.id
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.last_name = message.from_user.last_name
        user.full_name = message.from_user.full_name
        user.language_code = message.from_user.language_code
        user.is_bot = message.from_user.is_bot
        return user

    def new_chat_from_tgmessage(self, message: telebot.types.Message)-> Chat:
        chat = Chat()
        chat.id = message.chat.id
        chat.bio = message.chat.bio
        chat.description = message.chat.description
        return chat

    def new_message(self, user: User, chat: Chat, txt: str, data: str | None)-> Message:
        message = Message()
        message.user = user
        message.chat = chat
        message.full_user_name = f"{user.username} - {user.full_name}"
        message.text = txt
        message.call_data = data
        return message