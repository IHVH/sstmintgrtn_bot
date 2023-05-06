from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from typing import List
import httpx
import json

from bs4 import BeautifulSoup

API_BOT_URL = 'https://jeporab409.pagekite.me/api/'


class FileEditBotClass(BotFunctionABC):

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(content_types=['text'])
        def message_handler(message: types.Message):
            r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
            data = self.getJsonResponse(response=r)
            text = data['result']

            bot.send_message(text=text, chat_id=message.chat.id)

        @bot.message_handler(commands=['registration'])
        def registration(message: types.Message):
            r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
            data = self.getJsonResponse(response=r)
            text = data['result']

            bot.send_message(text=text, chat_id=message.chat.id) \

        @bot.message_handler(commands=['menu'])
        def menu(message: types.Message):
            r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
            data = self.getJsonResponse(response=r)
            text = data['result']
            buttons = self.getMenuButtons(json.loads(data['buttons'])['keyboard'])
            # print(buttons)
            bot.send_message(text=text, chat_id=message.chat.id, reply_markup=buttons)

    def getJsonResponse(self, response):
        return json.loads(response.text)

    def getMenuButtons(self, buttons):
        menuButtons = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for buttonRow in buttons:
            markupRow = []

            if len(buttonRow) < 2:
                menuButtons.add(types.KeyboardButton(buttonRow[0]['text']))

                continue

            for button in buttonRow:
                markupRow.append(types.KeyboardButton(button['text']))

            menuButtons.row(*markupRow)

        return menuButtons