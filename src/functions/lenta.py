import requests
from bs4 import BeautifulSoup
from bot_func_abc import BotFunctionABC
from telebot import telebot, types
from typing import List

def get_news():
    uri = 'https://lenta.ru/'
    req = requests.get(uri)
    answer = {
        "status_code": False,
        "news" : []
    }

    if req.status_code == 200:
        answer['status_code'] = True
        soup = BeautifulSoup(req.text, "html.parser")
        top_news = soup.findAll('a', class_='card-mini _topnews')

        for topick in top_news:
            cur_d = {
                "title": topick.span.text,
                "href": uri + topick['href']
                }
            answer['news'].append(cur_d)
    return answer

class Lenta_news(BotFunctionABC):
    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.message_handler(commands = commands)
        def activate_gpt(message: types.Message):

            news = get_news()
            if news['status_code']:
                nl = len(news['news'])
                counter = 0
                for n1 in news['news'][:10]:
                    counter += 1
                    url = n1["href"]
                    message_text = f'<a href="{url}">{counter}: {n1["href"]}</a>'
                    bot.send_message(text = message_text, chat_id = message.chat.id, parse_mode = 'HTML')
            else:
                message_text = '''Ошибка при подключении к "lenta.ru"'''
                bot.send_message(text = message_text, chat_id = message.chat.id)
