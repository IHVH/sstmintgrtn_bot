import os
import requests
import json

#Словарь для подстановки в url нужных параметров lang
lang_dict = {"ru" : "en-ru", "en" : "ru-en"}

def get_translate(text):
    #Получаем токен
    token = os.environ["YADICTTOKEN"]

    #Если пользователь ввел только команду без аргументов
    if (text.strip() == "/translate"):
        return "Задайте параметр выбора языка перевода как en или ru, а затем введите слово для перевода!"

    #Убираем команду из строки и получаем список с аргументами
    response = text.replace('/translate ', '').split(" ")

    #Должно быть два аргумента, если 1 то вернем ошибку
    if (len(response) < 2):
        return "Недостаточное параметров в команде! Задайте параметр выбора языка перевода как en или ru, а затем введите слово для перевода!"

    #Если пользователь неверно указал аргумент перевода (en или ru)
    if response[0] not in lang_dict: 
        return "Задайте параметр выбора языка перевода как en или ru!"

    #Собираем url, получаем ответ от сервиса
    url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang={}&text={}".format(token, lang_dict[response[0]], response[1])
    request = requests.get(url)

    #Делаем проверку кода состояния, если начинается на 4 - вернем ошибку
    if (str(request.status_code)[0] == "4"): 
        return "Получена ошибка при выполнении запроса!"

    #Получаем json
    json_ya = json.loads(request.text)
    
    #Если элемент def пустой, значит сервис не смог перевести слово - возвращаем ошибку
    try:
        orig_text = json_ya["def"][0]["text"]
    except IndexError:
        return "Попытка перевести слово на тот же язык либо неверный формат слова! Слово должно быть в начальной форме!"

    #Может случится так, что синонимов не будет найдено, тогда элемента syn не будет
    #В таком случае в конечном результате будет "Синонимы: не найдены"
    try:
        syn_dist = json_ya["def"][0]["tr"][0]["syn"]
        syn_dist_text = ""
        for syn in syn_dist:
            syn_dist_text += syn["text"] + ", "
    except KeyError:
        syn_dist_text = "не найдены  "  

    #Собираем финальную строку с результатами
    dictionary_text = "".join(("Реализовано с помощью сервиса «Яндекс.Словарь:\n",
                                "Искомое слово: {}\n".format(orig_text),
                                "Перевод: {}\n".format(json_ya["def"][0]["tr"][0]["text"]),
                                "Синонимы: {}".format(syn_dist_text[:-2])))

    return dictionary_text