import requests
import xml.etree.ElementTree as ET

def exc_rates(param):
    #обрабатываю ситуацию если юзер ввел пустую команду
    try:
        param = param.split()[1]
    except IndexError:
        return 'Введите код валюты в формате ISO 4217. Для просмотра возможных вариантов наберите команду /excrate list'

    #делаю запрос на получение данных в XML и с помощью библиотеки ET получаю дерево из объектов Elemet
    request = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(request.text)
    result = ''

    #вывожу все доступные коды валют и их названия
    if (param == 'list'): 
        for Valute in tree.findall('Valute'):
            result += Valute.find('CharCode').text + ' - ' + Valute.find('Name').text + '\n'
        return result[:-1]

    #перебираю дерево в поиске нужной валюты и вывожу ее значение
    for Valute in tree.findall('Valute'):
        if (Valute.find('CharCode').text == param):
            valuteName = Valute.find('Name').text
            valuteValue = Valute.find('Value').text
            return f'Курс валюты "{valuteName}" равен {valuteValue}'

    #если такой валюты не нашел, значит юзер ввел неверный код валюты
    return 'Введено неверное обозначение валюты! Введите код валюты в формате ISO 4217. ' \
                     'Для просмотра возможных вариантов наберите команду /excrate list'