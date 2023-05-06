import urllib.request
import telebot
from telebot import types
from telebot.callback_data import CallbackData
import re
import json
import logging
from datetime import datetime
from pycbrf import ExchangeRates
from bot_func_dictionary import BOT_FUNCTIONS

from functions import gif, gravatar, weather, translate, numbers, exc_rates, http_cats, \
    swear, speller, accuweather, openweather, kinopoisk, anecdotes, wikipedia_function


def old_start(bot: telebot.TeleBot, logger: logging.Logger):

    
    @bot.message_handler(commands=BOT_FUNCTIONS['accuweather'].commands)
    def get_accuweather(message):
        accuweather.get_text_messages(message, bot)


    @bot.message_handler(commands=BOT_FUNCTIONS['get_gif'].commands)
    def get_gif(message):
        requireString = message.text[9:]
        gif_url = gif.main(requireString)
        bot.send_animation(message.chat.id, gif_url, None, "Text")


    def get_keyboard_kinopoisk(url):
        """ Кнопка на внешний ресурс """

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Ссылка", url=url))
        return keyboard

    @bot.message_handler(commands=BOT_FUNCTIONS['kinopoisk'].commands)
    def get_kinopoisk(message):
        stripped_greeting = message.text.strip("/kinopoisk ")
        print(stripped_greeting)

        search = kinopoisk.main(stripped_greeting)

        if search:
            for item in search:
                caption = f'{item.ru_name}\n\n' \
                        f'Год производства: {item.year}\n' \
                        f'Жанр: {", ".join(item.genres)}\n' \
                        f'Страна: {", ".join(item.countries)}\n' \
                        f'Время просмотра: {item.duration}\n' \
                        f'Рейтинг: {item.kp_rate}'

                bot.send_photo(message.from_user.id, item.poster,
                            caption=caption,
                            reply_markup=get_keyboard_kinopoisk(item.kp_url))
        else:
            bot.send_message(
                message.chat.id, "По вашему запросу ничего не смог найти,\n пожалуйста введите корректное название фильма.")


    @bot.message_handler(commands=BOT_FUNCTIONS['openweather'].commands)
    def get_open(message):
        stripped_greeting = message.text.strip('/openweather ')
        print(stripped_greeting, )
        open_message = openweather.get_weather(stripped_greeting)
        bot.send_message(message.chat.id, text=open_message)


    gravatar_keyboard_factory = CallbackData('grav_button', 'grav_email', prefix=BOT_FUNCTIONS['grav'].commands[0])

    @bot.message_handler(commands=BOT_FUNCTIONS['grav'].commands)
    def grav(message):
        gravatar.grav(message, bot, gravatar_keyboard_factory)

    @bot.callback_query_handler(func=None, config=gravatar_keyboard_factory.filter())
    def gravatar_keyboard_callback(call):
        callback_data: dict = gravatar_keyboard_factory.parse(callback_data=call.data)
        gravatar.main(bot, call, callback_data)


    @bot.message_handler(commands=BOT_FUNCTIONS['anecdote'].commands)
    def get_anecdote(message):
        bot.send_message(message.chat.id, text=anecdotes.get_anecdote(message))


    @bot.message_handler(commands=BOT_FUNCTIONS['weather'].commands)
    def get_weather(message):
        weather_text = weather.get_weather(message.text)
        bot.send_message(message.chat.id, text=weather_text)


    @bot.message_handler(commands=BOT_FUNCTIONS['translate'].commands)
    def get_translate(message):
        translate_result = translate.get_translate(message.text)
        bot.send_message(message.chat.id, text=translate_result)


    @bot.message_handler(commands=BOT_FUNCTIONS['excrate'].commands)
    def get_excrate(message):
        excrate_res = exc_rates.exc_rates(message.text)
        bot.send_message(message.chat.id, text=excrate_res)


    @bot.message_handler(commands=BOT_FUNCTIONS['numbers'].commands)
    def get_fact_by_number(message):
        params = message.text.split()
        if '/digit' in params and len(params) == 2:
            fact_by_digit = numbers.get_fact_by_request(
                'digit', {'digit': params[1]})
            bot.send_message(message.chat.id, text=fact_by_digit)
        elif '/date' in params and len(params) == 3:
            fact_by_date = numbers.get_fact_by_request(
                'date', {'month': params[1], 'date': params[2]})
            bot.send_message(message.chat.id, text=fact_by_date)
        elif '/random' in params and len(params) == 1:
            fact_by_random = numbers.get_fact_by_request('random')
            bot.send_message(message.chat.id, text=fact_by_random)
        else:
            bot.send_message(
                message.chat.id, text="Некорректный формат команды. Повторите попытку!")


    @bot.message_handler(commands=BOT_FUNCTIONS['http'].commands)
    def get_http(message):
        if message.text.strip() == "/http":
            http_reply = "Неверный формат ввода. Введите http код, например /http 204. Для просмотра возможных вариантов " \
                        "наберите команду /http list"
        elif message.text.strip() == "/http list":
            codes_list = http_cats.get_codes_list()
            http_reply = json.dumps(codes_list)
        else:
            http_code = re.sub(r'[^0-9.]', "", message.text)
            http_reply = http_cats.get_cat(http_code)
        bot.send_message(message.chat.id, text=http_reply)


    @bot.message_handler(commands=BOT_FUNCTIONS['insult'].commands)
    def insult_generator(message):
        swear_res = swear.insult_generator()
        bot.send_message(message.chat.id, text=swear_res)


    @bot.message_handler(commands=BOT_FUNCTIONS['speller'].commands)
    def get_spell(message):
        spell_result = speller.get_spell(message.text)
        bot.send_message(message.chat.id, text=spell_result)


    @bot.message_handler(commands=BOT_FUNCTIONS['Wikipedia'].commands)
    def test(message):
        final_message = wikipedia_function.wiki_op(message.text)
        bot.send_message(message.chat.id, text=final_message, parse_mode='html')


    @bot.message_handler(commands=['rates'])
    def start1(message):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = telebot.types.KeyboardButton('USD')
        itembtn2 = telebot.types.KeyboardButton('EUR')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id=message.chat.id, text="<b>Привет! Выбери валюту.</b>",
                        reply_markup=markup, parse_mode="html")


    @bot.message_handler(func=lambda msg: msg.text == "USD" or msg.text == "EUR")#content_types=['text'])
    def message(message):
        message_norm = message.text.strip().lower()

        if message_norm in ['usd', 'eur']:
            rates = ExchangeRates(datetime.now())
            bot.send_message(chat_id=message.chat.id,
                            text=f"<b>{message_norm.upper()} курс {float(rates[message_norm.upper()].rate)} </b>",
                            parse_mode="html")


    mks_factory = CallbackData('mks_button', prefix=BOT_FUNCTIONS['mks'].commands[0])

    @bot.message_handler(commands=BOT_FUNCTIONS['mks'].commands)
    def mks_msg_handler(message):
        key = types.InlineKeyboardMarkup()
        cord = types.InlineKeyboardButton(text="да", callback_data=mks_factory.new(mks_button="да"))
        key.add(cord)

        bot.send_message(message.chat.id, "хотите узнать местоположение мкс?", reply_markup=key)

    @bot.callback_query_handler(func=None, config=mks_factory.filter())# mks_button='да'
    def mks_callback_handler(c: types.CallbackQuery):
        callback_data: dict = mks_factory.parse(callback_data=c.data)
        mks_button = callback_data['mks_button']
        if mks_button == 'да':
            key = types.InlineKeyboardMarkup()
            req = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
            obj = json.loads(req.read())
            bot.send_message(c.message.chat.id,f"отметка времени {obj['timestamp']}", reply_markup=key)
            bot.send_message(c.message.chat.id, f"долгота {obj['iss_position']['longitude']} \nширота {obj['iss_position']['latitude']}", reply_markup=key)
