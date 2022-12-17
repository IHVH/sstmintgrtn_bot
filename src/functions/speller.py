import requests
import json

def get_spell(message):
    params_list = message.split()
    #Проверка что пользователь ввел что-то кроме команды /speller
    if (len(params_list) < 2):
        return "Введите команду в формате /speller СЛОВО, например /speller Превет"

    #Посылаем запрос к сервису, получаем ответ в виде json и преобразуем его
    url = "https://speller.yandex.net/services/spellservice.json/checkText?text=%s" % params_list[1]
    response = requests.get(url)
    response_list = json.loads(response.text)

    #Если сервис вернул пустой список, значит он не нашел ошибок, либо такого слова не существует
    try:
        result = response_list[0]["s"]
    except IndexError:
        return 'Слово "%s" написано правильно, либо не существует!' % params_list[1]

    #Выводим пользователю все слова, подходящие для исправления
    error_text = 'В слове "%s" обнаружены ошибки!\nВозможные варианты написания:\n' % params_list[1]
    for word in result:
        error_text += word + "\n"

    return error_text[:-1]