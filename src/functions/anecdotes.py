import requests
import random
from bs4 import BeautifulSoup as b


list_of_jokes = []
ANECDOTE_URL = 'https://www.anekdot.ru/last/anekdot/'


def par():
    global ANECDOTE_URL
    r = requests.get(ANECDOTE_URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


def get_anecdote(message):

    global list_of_jokes

    if len(list_of_jokes) < 1:
        list_of_jokes = par()
        random.shuffle(list_of_jokes)

    if message.text.lower() in '123456789':
        try:
            anecdote_id = int(message.text)
            anecdote_text = list_of_jokes[anecdote_id]
            del list_of_jokes[anecdote_id]
            return anecdote_text
        except Exception:
            return 'Нужно ввести любую цифру,а то это уже не смешно...'
    else:
        return 'Требуется числовой аргумент'
