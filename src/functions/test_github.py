from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import requests

class TestGitFunction(BotFunctionABC):
    OWNER = 'IHVH'
    REPO = 'OEMIB_PI01_19_TBOT'
    URL = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'

    HEADER = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    PARAM = {'page': 1, 'per_page': '5'}


    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.git_keyboard_factory = CallbackData('git_key_button', prefix=commands[0])



        @bot.message_handler(commands=commands)
        def test_hendler(message):
            words = message.text.split()
            if(len(words) > 1): 
                per_page = words[-1]
                if(per_page.isdigit()):

                    if(int(per_page) < 101):
                        self.PARAM['per_page'] = per_page

            self.request(message.chat.id)

        @bot.callback_query_handler(func=None, config=self.git_keyboard_factory.filter())
        def test_keyboard_callback(call):
            callback_data: dict = self.git_keyboard_factory.parse(callback_data=call.data)
            git_key_button = callback_data['git_key_button']
            match (git_key_button):
                case ('next_page'):
                    self.PARAM['page'] = self.PARAM['page'] + 1
                    self.request(call.message.chat.id)
                case _:
                    bot.answer_callback_query(call.id, call.data)
            

    def request(self, chat_id):
        r = requests.get(self.URL, headers=self.HEADER, params=self.PARAM)    

        if(r.status_code == 200):
            obj = r.json()
            for comit in obj:
                url = comit['html_url']
                msg = comit['commit']['message']
                author = comit['commit']['author']['name']
                txt = f'{author} \n {msg} \n {url}'

                self.bot.send_message(text=txt, chat_id=chat_id)
            
            self.bot.send_message(text="NEXT ?", chat_id=chat_id, reply_markup=self.gen_markup())
            
        else: 
            print(r.text)
    
    def gen_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(types.InlineKeyboardButton("Да ->", callback_data=self.git_keyboard_factory.new(git_key_button="next_page")))
        return markup