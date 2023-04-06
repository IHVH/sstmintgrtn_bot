import requests
import random
from bs4 import BeautifulSoup as b

list_of_jokes = []

def par():
    ANECDOTE_URL = 'https://www.anekdot.ru/last/anekdot/'
    r = requests.get(ANECDOTE_URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

def get_anecdote(message):

    global list_of_jokes

    if len(list_of_jokes) < 1:
        list_of_jokes = par()
        random.shuffle(list_of_jokes)

    str_spilt = message.text.split()
    x = str_spilt[-1]

    if x in '123456789':
        try:
            anecdote_id = int(x)
            anecdote_text = list_of_jokes[anecdote_id]
            del list_of_jokes[anecdote_id]
            return anecdote_text
        except Exception:
            return 'Нужно ввести любую цифру,а то это уже не смешно...'
    else:
        return 'Требуется числовой аргумент'
