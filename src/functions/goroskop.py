from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from typing import List
import httpx
from bs4 import BeautifulSoup

class GoroskopFunction(BotFunctionABC):
    headers = {'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (RHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
           'accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8'
           }
    link = f'https://horo.mail.ru/prediction/'
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.kf = CallbackData('t_key_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def example_message_hendler(message: types.Message):
            
            bot.send_message(text="Привет. Выбери свой знак зодиака:", chat_id=message.chat.id, reply_markup=self.gen_markup())

        @bot.callback_query_handler(func=None, config=self.kf.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.kf.parse(callback_data=call.data)
            zodiac = callback_data['t_key_button']
            self.i = 0
            txt = self.get_text_horoscope(zodiac)
            bot.send_message(text=txt, chat_id=call.message.chat.id)

    
    def gen_markup(self):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("Овен", callback_data=self.kf.new(t_key_button="aries")),
                   types.InlineKeyboardButton("Телец", callback_data=self.kf.new(t_key_button="taurus")),
                   types.InlineKeyboardButton("Близнецы", callback_data=self.kf.new(t_key_button="gemini")), 
                   types.InlineKeyboardButton("Рак", callback_data=self.kf.new(t_key_button="cancer")),
                   types.InlineKeyboardButton("Лев", callback_data=self.kf.new(t_key_button="leo")),
                   types.InlineKeyboardButton("Дева", callback_data=self.kf.new(t_key_button="virgo")), 
                   types.InlineKeyboardButton("Весы", callback_data=self.kf.new(t_key_button="libra")),
                   types.InlineKeyboardButton("Скорпион", callback_data=self.kf.new(t_key_button="scorpio")),
                   types.InlineKeyboardButton("Стрелец", callback_data=self.kf.new(t_key_button="sagittarius")), 
                   types.InlineKeyboardButton("Козерог", callback_data=self.kf.new(t_key_button="capricorn")),
                   types.InlineKeyboardButton("Водолей", callback_data=self.kf.new(t_key_button="aquarius")),
                   types.InlineKeyboardButton("Рыбы", callback_data=self.kf.new(t_key_button="pisces")), 
                   )
      
        return markup
    
    def get_response(self, link: str, re: bool = True):
        with httpx.Client(headers=self.headers, follow_redirects=True) as htx:
            result: httpx.Response = htx.get(url=link)
            if result.status_code == 200:
                return result.text
            else:
                raise Exception('Плохой запрос: Код: ' + result.status_code)
            

    def get_text_horoscope(self, zodiac: str):
        link = self.link + f"{zodiac}/today/"
        try:
          response_result = self.get_response(link=link)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

        beautifulsoup: BeautifulSoup = BeautifulSoup(markup=response_result, features='lxml')
        text = beautifulsoup.find(name='div', class_='article__text')
        return text.text
