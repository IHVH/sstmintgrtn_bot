from email import header
import os
from urllib import response
import telebot
import libgravatar
import wikipedia
import re
import json
import logging
import threading
import time
from datetime import datetime
from pycbrf import ExchangeRates
from telebot import types
from bot_command_dictionary import BOT_FUNCTIONS

from functions import start, gif, github, soap_country, gravatar, weather, translate, numbers, exc_rates, http_cats, swear, speller, wikipedia, accuweather, openweather, kinopoisk, webui_interaction, config

token = os.environ["TBOTTOKEN"]
bot = telebot.TeleBot(token)

conf = config.load_telegram_setting()
msgs = config.load_telegram_msgs()
neural = config.load_neural()

logger = logging.Logger(__name__)
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=BOT_FUNCTIONS['start'].commands)
def send_welcome(message):
    bot.reply_to(
        message, start.get_start_message_from_bot_function_dictionary())

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_yes"),
               types.InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup

def get_keyboard_kinopoisk(url):
    """ Кнопка на внешний ресурс """

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Ссылка", url=url))
    return keyboard

@bot.message_handler(commands=BOT_FUNCTIONS['accuweather'].commands)
def get_accuweather(message):
    accuweather.get_text_messages(message, bot)

# DavidShariev
@bot.message_handler(commands=BOT_FUNCTIONS['get_gif'].commands)
def get_gif(message):
    requireString = message.text[9:]
    gif_url = gif.main(requireString)
    bot.send_animation(message.chat.id, gif_url, None, "Text")


@ bot.message_handler(commands=BOT_FUNCTIONS['test_keyboard'].commands)
def send_markup(message):
    bot.send_message(message.chat.id, "Да/Нет?", reply_markup=gen_markup())


@ bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    match(call.data):
        case('cb_yes'):
            bot.answer_callback_query(call.id, "Ответ ДА!")
        case('cb_no'):
            bot.answer_callback_query(call.id, "Ответ НЕТ!")
        # TODO - call.message не содержит текст изначального сообщения, необходим другой вариант решения
        case('cb_default'):
            gravatar.main('1', bot, call.message)
        case('cb_monsterid'):
            gravatar.main('2', bot, call.message)
        case('cb_identicon'):
            gravatar.main('3', bot, call.message)
        case('cb_wavatar'):
            gravatar.main('4', bot, call.message)
        case('cb_robohash'):
            gravatar.main('5', bot, call.message)
        case('cb_retro'):
            gravatar.main('6', bot, call.message)


@ bot.message_handler(commands=BOT_FUNCTIONS['country'].commands)
def get_country_info(message):
    soap_country.get_country_info(message, bot)


github.Github(bot=bot)

@ bot.message_handler(commands=BOT_FUNCTIONS['kinopoisk'].commands)
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


@bot.message_handler(commands=BOT_FUNCTIONS['grav'].commands)
def grav(message):
    gravatar.grav(message, bot)


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
    if (message.text.strip() == "/http"):
        http_reply = "Неверный формат ввода. Введите http код, например /http 204. Для просмотра возможных вариантов наберите команду /http list"
    elif (message.text.strip() == "/http list"):
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
    final_message = wikipedia.wiki_op(message.text)
    bot.send_message(message.chat.id, text=final_message, parse_mode='html')


@bot.message_handler(commands=['rates'])
def start1(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    markup.add(itembtn1, itembtn2)
    bot.send_message(chat_id=message.chat.id, text="<b>Привет! Выбери валюту.</b>",
                     reply_markup=markup, parse_mode="html")


@bot.message_handler(commands=[conf.get_value("gen_cmd")])
def generate_handler(message):
    global loading_image_id
    try:
        msgtext = message.text

        if not msgtext:
            bot.send_message(message.chat.id, reply_to_message_id=message.id, text=msgs.get_value("error_text"))
            return

        array = msgtext.split(" ", maxsplit=1)
        if len(array) < 2:
            bot.send_message(message.chat.id, reply_to_message_id=message.id, text=msgs.get_value("error_text"))
            return

        prompt_user = array[1]

        logger.info(f"Generate with prompt {prompt_user}")
        status_msg = __send_waiting(message)

        filename = f"img_{prompt2filename(prompt_user)}_{time.time()}.png"

        logger.info(f"Img name - {filename}")

        # GENERATING
        img = __generate(prompt_user, status_msg)

        # UPSCALE
        if neural.get_neural_setting_value(config.UPSCALE):
            img = __upscale(img, status_msg)

        img.save(os.path.join(conf.get_value(config.SAVE_FOLDER), filename))

        bot.edit_message_media(
            message_id=status_msg.message_id,
            chat_id=status_msg.chat.id,
            media=types.InputMediaPhoto(img.to_reader(), caption=msgs.get_value("completed")))

        logger.info(f"Completed")

    except Exception as e:
        __logFatal(e, message.chat.id, message.id)


@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id,
                         text=f"<b>{message_norm.upper()} курс {float(rates[message_norm.upper()].rate)} </b>", parse_mode="html")


def __send_waiting(message: types.Message) -> types.Message:
    global loading_image_id

    sent_msg = None
    if not loading_image_id:
        with open(f"../../res/loading.png", "rb") as ph:
            sent_msg = bot.send_photo(photo=ph, chat_id=message.chat.id, reply_to_message_id=message.id,
                                      caption=msgs.get_value("working"))
            if sent_msg.photo:
                loading_image_id = sent_msg.photo[0].file_id
    else:
        sent_msg = bot.send_photo(photo=loading_image_id, chat_id=message.chat.id, reply_to_message_id=message.id,
                                  caption=msgs.get_value("working"))

    return sent_msg


def __generate(prompt_user, sent: types.Message) -> webui_interaction.Base64Img:
    global negative
    ret = []

    logger.info(f"Generating, prompt = {prompt_user}")

    def gen_func():
        img = webui_interaction.gen_img(conf.get_value("url"), prompt_user, neural.get_neural_setting_value(config.NEGATIVE), neural.get_neural_setting_value(config.WIDTH), neural.get_neural_setting_value(config.HEIGHT),
                          steps=neural.get_neural_setting_value(config.STEPS))
        ret.append(img)

    th_creator = threading.Thread(target=gen_func)
    th_creator.start()

    while th_creator.is_alive():
        if neural.get_neural_setting_value(config.SHOW_PROGRESS):
            progress = webui_interaction.get_progress(conf.get_value("url"), not neural.get_neural_setting_value(config.SHOW_PROGRESS_PREVIEW))

            banner = msgs.get_value("progress").format(progress=progress.progress, eta=int(progress.eta_relative))

            if progress.current_image:
                bot.edit_message_media(
                    message_id=sent.message_id,
                    chat_id=sent.chat.id,
                    media=types.InputMediaPhoto(progress.current_image.to_reader(), caption=banner))
            else:
                bot.edit_message_caption(
                    message_id=sent.message_id,
                    chat_id=sent.chat.id,
                    caption=banner)
        time.sleep(2)

    return ret[0]


def __upscale(img: webui_interaction.Base64Img, sent: types.Message) -> webui_interaction.Base64Img:
    ret = []
    logger.info(f"Upscaling...")

    bot.edit_message_caption(
        message_id=sent.message_id,
        chat_id=sent.chat.id,
        caption=msgs.get_value("upscaling"))

    def gen_func_ups():
        img_big = webui_interaction.upscale(conf.get_value("url"), img, 2)
        ret.append(img_big)

    th_upscaler = threading.Thread(target=gen_func_ups)
    th_upscaler.start()
    th_upscaler.join()
    return ret[0]


def __logFatal(e: Exception, chat_id, message_id):
    logger.exception(e)
    bot.send_message(chat_id, reply_to_message_id=message_id, text=msgs.get_value("error"))


def prompt2filename(prompt: str):
    repl_prompt = prompt.replace("/", "_").replace("\\", "_")
    if len(repl_prompt) > 100:
        return repl_prompt[:100]
    return repl_prompt


@bot.message_handler(func=lambda message: True)
def text_messages(message):
    bot.reply_to(message, "Text = " + message.text)
    bot.send_message(text="Ваш запрос не обработан!!!",
                     chat_id=message.chat.id)


bot.infinity_polling()
