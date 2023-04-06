from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import requests
import os

class GitHubFunctions(BotFunctionABC):
    OWNER = 'IHVH'
    REPO = 'OEMIB_PI01_19_TBOT'
    BASE_URL = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'

    HEADER = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    PARAM_DEF = {'page': 1, 'per_page': '5'}

    CHAT_STATE = {}

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.git_keyboard_factory = CallbackData('git_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def git_msg_hendler(message: types.Message):
            self.set_user_per_page(message)
            resp = self.request(message)
            self.proces_response(message, resp)

        @bot.callback_query_handler(func=None, config=self.git_keyboard_factory.filter())
        def git_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.git_keyboard_factory.parse(callback_data=call.data)
            git_key_button = callback_data['git_key_button']
            param = self.get_user_param(call.message.chat.id)
            url = param['links'][git_key_button]['url']
            resp = self.request(call.message, url)
            self.proces_response(call.message, resp)
           
            
    def get_user_param(self, chat_id):
        if chat_id in self.CHAT_STATE:
            return self.CHAT_STATE[chat_id]
        else:
            self.CHAT_STATE[chat_id] = self.PARAM_DEF.copy()
            return self.CHAT_STATE[chat_id]

    def set_user_per_page(self, message: types.Message):
        param = self.get_user_param(message.chat.id)
        words = message.text.split()
        if(len(words) > 1): 
            per_page = words[-1]
            if(per_page.isdigit()):
                if(int(per_page) < 101):
                    
                    param['per_page'] = per_page

    def set_user_page(self, message: types.Message, step: int):
        param = self.get_user_param(message.chat.id)
        param['page'] = param['page'] + step


    def request(self, message: types.Message, url: str | None = None)-> requests.Response:
        if(url is not None):
            return requests.get(url, headers=self.HEADER)
        else:
            param = self.get_user_param(message.chat.id)
            return requests.get(self.BASE_URL, headers=self.HEADER, params=param)    
        
    
    def proces_response(self, message: types.Message, resp: requests.Response):
        if(resp.status_code == 200):
            obj = resp.json()
            for comit in obj:
                avatar_url = comit['committer']['avatar_url']
                committer_url = comit['committer']['html_url']
                url = comit['html_url']
                msg = comit['commit']['message']
                author = comit['commit']['author']['name']
                email = comit['commit']['author']['email']
                date = comit['commit']['author']['date']
                txt = f'_Author_      - [{author}]({committer_url}) \n' + \
                    f'_Message_   -  *{msg}* \n' + \
                    f'_Date_          -  *{date}* \n' + \
                    f'[Open commit in browser]({url})'
                
                self.bot.send_message(text=txt, chat_id=message.chat.id, parse_mode='Markdown')
            
            self.bot.send_message(text="Go to another page?", chat_id=message.chat.id, reply_markup=self.gen_markup(resp.links))
            param = self.get_user_param(message.chat.id)
            param['links'] = resp.links
        else: 
            print(resp.text)

    def gen_markup(self, links):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = len(links)
        buttons = []
        for key, val in links.items():
            buttons.append(types.InlineKeyboardButton(val['rel'], callback_data=self.git_keyboard_factory.new(git_key_button=val['rel'])))

        markup.add(*buttons)
        return markup