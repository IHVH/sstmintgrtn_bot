from geopy import geocoders
import requests
import json
import os

conditions = {"clear": "ясно", "partly-cloudy": "малооблачно", "cloudy": "облачно с прояснениями",
                "overcast": "пасмурно", "drizzle": "морось", "light-rain": "небольшой дождь",
                "rain": "дождь", "moderate-rain": "умеренно сильный", "heavy-rain": "сильный дождь",
                "continuous-heavy-rain": "длительный сильный дождь", "showers": "ливень",
                "wet-snow": "дождь со снегом", "light-snow": "небольшой снег", "snow": "снег",
                "snow-showers": "снегопад", "hail": "град", "thunderstorm": "гроза",
                "thunderstorm-with-rain": "дождь с грозой", "thunderstorm-with-hail": "гроза с градом"}

wind_dir = {"nw": "северо-западное", "n": "северное", "ne": "северо-восточное", "e": "восточное",
                "se": "юго-восточное", "s": "южное", "sw": "юго-западное", "w": "западное", "с": "штиль"}

# Функция для получения координат по адресу
def get_geo_pos(adress):
    geolocator = geocoders.Nominatim(user_agent="yandex_weather")
    geo = geolocator.geocode(adress)
    latitude = geo.latitude
    longitude = geo.longitude
    return latitude, longitude

# Получение ответа от сервиса Яндекса в формате json и его обработка
def get_weather(message):
    token = os.environ["YAWEATHERTOKEN"]

    if (message.strip() == "/weather"): 
        return "Введите адрес в формате: <Название города>, <Название улицы>, <Дом>"
    adress = (message.replace('/weather ', ''))

    try:
        location = get_geo_pos(adress)
    except AttributeError:
        return "Введен несуществующий адрес!"

    yandex_url = f"https://api.weather.yandex.ru/v2/forecast?lat={location[0]}&lon={location[1]}&[limit=1]&[lang=ru_RU]&[hours=false]"
    yandex_request = requests.get(yandex_url, headers={"X-Yandex-API-Key": token})
    if (str(yandex_request.status_code)[0] == "4"): 
        return "Получена ошибка при выполнении запроса!"

    yandex_json = json.loads(yandex_request.text)

    weather_text = "По данным сервиса Яндекс.Погода:\n" \
                            f'Температура: {yandex_json["fact"]["temp"]} \u2103\n' \
                            f'Ощущается как: {yandex_json["fact"]["feels_like"]} \u2103\n' \
                            f'Погодные условия: {conditions[yandex_json["fact"]["condition"]]}\n' \
                            f'Скорость ветра {yandex_json["fact"]["wind_speed"]} м/с, направление {wind_dir[yandex_json["fact"]["wind_dir"]]}\n' \
                            f'Давление: {yandex_json["fact"]["pressure_mm"]} мм рт. ст.\n' \
                            f'Влажность воздуха: {yandex_json["fact"]["humidity"]}%'

    return weather_text