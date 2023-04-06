import json
import requests as req
from geopy import geocoders

token = '5965243792:AAEZ0zKhqKbZkLGtsug0G0ucwpjZg1Bi-Nw'
token_accu = 'Iw1AmL9aiolP72cC8r6FGrzh6shcIfA3'

def code_location(latitude: str, longitude: str, token_accu: str):
    print(latitude)
    print(longitude)
    url_location_key = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' \
                       f'{token_accu}&q={latitude},{longitude}&language=ru'
    print(url_location_key)
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    print(json_data)
    code = json_data['Key']
    return code


def weather(code_loc: str, token_accu: str):
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{code_loc}?' \
                  f'apikey={token_accu}&language=ru&metric=True'
    response = req.get(url_weather, headers={"APIKey": token_accu})
    json_data = json.loads(response.text)
    dict_weather = dict()
    dict_weather['link'] = json_data[0]['MobileLink']
    time = 'сейчас'
    dict_weather[time] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range(1, len(json_data)):
        time = 'через' + str(i) + 'ч'
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    print(code_loc+" code_loc ")
    return dict_weather


def print_weather(dict_weather, message, bot):
    bot.send_message(message.from_user.id, f'Докладываю, в вашем городе'
                                           f' температура сейчас {dict_weather["сейчас"]["temp"]}!'
                                           f' А на небе {dict_weather["сейчас"]["sky"]}.'
                                           f' Температура через три часа {dict_weather["через3ч"]["temp"]}!'
                                           f' А на небе {dict_weather["через3ч"]["sky"]}.'
                                           f' Температура через шесть часов {dict_weather["через6ч"]["temp"]}!'
                                           f' А на небе {dict_weather["через6ч"]["sky"]}.'
                                           f' Температура через девять часов {dict_weather["через9ч"]["temp"]}!'
                                           f' А на небе {dict_weather["через9ч"]["sky"]}.')
    bot.send_message(message.from_user.id, f' А здесь ссылка на подробности '
                                           f'{dict_weather["link"]}')



def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude


def add_city(message):
    try:
        latitude, longitude = geo_pos(message.text.lower().split('город ')[1])
        global cities
        cities[message.from_user.id] = message.text.lower().split('город ')[1]
        with open('cities.json', 'w') as f:
            f.write(json.dumps(cities))
        return cities, 0
    except Exception as err:
        return cities, 1


# bot = telebot.TeleBot(token)
#
# with open('cities.json', encoding='utf-8') as f:
#     cities = json.load(f)


def get_text_messages(msg, bot):
    msg.text = msg.text.strip("/accuweather ")
    message = msg
    global cities
    if message.text.lower() == 'привет' or message.text.lower() == 'начать':
        bot.send_message(message.from_user.id,
                         f'Доброго времени суток {message.from_user.first_name}! Позвольте рассказать '
                         f' Вам о погоде! Напишите  слово "погода" и я напишу погоду в Вашем'
                         f' "стандартном" городе или напишите название города в готором Вы сейчас')
    elif message.text.lower() == 'погода':
        if message.from_user.id in cities.keys():
            city = cities[message.from_user.id]
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Твой город {city}')
            latitude, longitude = geo_pos(city)
            code_loc = code_location(latitude, longitude, token_accu)
            you_weather = weather(code_loc, token_accu)
            print_weather(you_weather, message, bot)

        else:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Я не знаю Ваш город! Просто напиши:'
                                                   f'"Мой город *****" и я запомню твой стандартный город!')
    elif message.text.lower()[:9] == 'мой город':
        cities, flag = add_city(message)
        if flag == 0:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Теперь я знаю Ваш город! это'
                                                   f' {cities[message.from_user.id]}')
        else:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Что то пошло не так :(')
    else:
        try:
            city = message.text
            bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}! Твой город {city}')
            latitude, longitude = geo_pos(city)
            code_loc = code_location(latitude, longitude, token_accu)
            you_weather = weather(code_loc, token_accu)
            print_weather(you_weather, message, bot)

        except AttributeError as err:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Я не знаю такого города,'
                                                   f'{err}, попробуй другой город')

#
# bot.polling()