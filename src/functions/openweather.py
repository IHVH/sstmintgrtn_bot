import requests

tg_bot_token = "5924119361:AAFYiCEq89FAIdnqr56Sm7TvK4utGpCo278"

def get_weather(city):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'adf1d0cab1a5fcf4bfcee5e32bb85d80'}&units=metric"
            )
        date = r.json()
        city = date["name"]
        cur_weather = date["main"]["temp"]
        humidity = date["main"]["humidity"]
        pressure = date["main"]["pressure"]
        temp_max = date["main"]["temp_max"]
        temp_min = date["main"]["temp_min"]
        wind = date["wind"]["speed"]

        a = (f"Погода в городе {city}\n Температура {cur_weather}C\n"
                                              f"Влажность составляет {humidity}%\n Давление {pressure} мм.рт.ст\n Минимальная температура {temp_min}С\n Максимальная температура{temp_max}С\n"
                                              f"Скорость ветра {wind} метра в сек\n")
        return a
    except:
        return "Проверте название города"
