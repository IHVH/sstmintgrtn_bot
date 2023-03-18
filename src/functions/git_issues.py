from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import os
import requests

class GitIssues(BotFunctionABC):
    OWNER = "IHVH"
    REPO = "OEMIB_PI01_19_TBOT"
    URL = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

    HEADER = {"Accept":"application/vnd.github+json", 
          "X-GitHub-Api-Version": "2022-11-28" } 

    PARAM = {"per_page":5, "page":1}


    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.issue_keyboard_factory = CallbackData('issue_key_button', prefix=commands[0])


        @bot.message_handler(commands=commands)
        def issues_message_hendler(message: types.Message):
            self.get_issues(message)

        @bot.callback_query_handler(func=None, config=self.issue_keyboard_factory.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.issue_keyboard_factory.parse(callback_data=call.data)
            data = callback_data['issue_key_button']
            self.bot.send_message(text=f"{data}", chat_id=call.message.chat.id)

    def get_issues(self, message: types.Message):
        response = requests.get(self.URL, params=self.PARAM, headers=self.HEADER)
        if(response.ok):
            resp = response.json()
            for issue in resp:
                html = issue["html_url"]
                title = issue["title"]
                body = issue["body"]
                user = issue["user"]
                login = user["login"]
                
                txt = f"User - *{login}* \n*{title}* - _{body}_ \n"
                txt = txt + f"[url]({html})"

                self.bot.send_message(text=txt, 
                                      chat_id=message.chat.id, 
                                      parse_mode="Markdown")

            self.bot.send_message(text="Выполнить действие?", 
                                  chat_id=message.chat.id, 
                                  reply_markup=self.gen_markup())
        else:
            txt = f'{response.status_code} - {response.reason}'
            self.bot.send_message(text=txt, chat_id=message.chat.id)
        

    def gen_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(types.InlineKeyboardButton("TEXT1", callback_data=self.issue_keyboard_factory.new(issue_key_button="DATA1")),
                   types.InlineKeyboardButton("TEXT2", callback_data=self.issue_keyboard_factory.new(issue_key_button="DATA2")))
        return markup