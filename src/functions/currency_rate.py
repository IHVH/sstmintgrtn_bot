from bot_func_abc import BotFunctionABC
import requests
from bs4 import BeautifulSoup


class CurrencyRateFunction(BotFunctionABC):
    # Отправляем GET запрос на страницу с курсами валют ЦБ РФ
    response = requests.get('https://www.cbr.ru/currency_base/daily/')

    # Извлекаем HTML-код страницы
    html = response.content
    # Создаем объект BeautifulSoup для парсинга
    soup = BeautifulSoup(html, 'html.parser')
    # Находим нужный элемент, содержащий курс доллара
    # print(soup.prettify())
    usd_rate = soup.find('div', class_='table').find_all_next('td')[69].string
    print(f"Курс Доллара: {usd_rate}")
    eur_rate = soup.find('div', class_='table').find_all_next('td')[74].string
    print(f"Курс Евро: {eur_rate}")
