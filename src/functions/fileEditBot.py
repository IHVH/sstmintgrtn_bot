from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from typing import List
import httpx
import json

API_BOT_URL = 'https://jeporab409.pagekite.me/api/'

class FileEditBotClass(BotFunctionABC):

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot
        self.isActive = False

        @bot.message_handler(commands=[commands[0]])
        def registration(message: types.Message):
            r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
            data = self.getJsonResponse(response=r)
            text = data['result']

            bot.send_message(text=text, chat_id=message.chat.id)

            self.isActive = True

        @bot.message_handler(commands=[commands[1]])
        def menu(message: types.Message):
            r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
            data = self.getJsonResponse(response=r)
            text = data['result']
            buttons = self.getMenuButtons(json.loads(data['buttons'])['keyboard'])

            bot.send_message(text=text, chat_id=message.chat.id, reply_markup=buttons)
            bot.register_next_step_handler(message, commandRoute)

            self.isActive = True

        def commandRoute(message):

            if message.text == '/' + commands[2]:
                self.isActive = False

                bot.send_message(
                    text='Ну чтож, пока! Чтоб начать со мной общение снова - используй команду /menu!',
                    chat_id=message.chat.id
                )

            if message.text != '/' + commands[2] and self.isActive:
                r = httpx.post(API_BOT_URL, data=json.dumps(message.json))
                data = self.getJsonResponse(response=r)
                text = data['result']
                bot.send_message(text=text, chat_id=message.chat.id)

                bot.register_next_step_handler(message, commandRoute)

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