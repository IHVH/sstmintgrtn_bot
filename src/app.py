from email import header
import os
from urllib import response
import telebot
import requests
import libgravatar
import re
import json
import telebot, wikipedia, re
from telebot import types
from bot_command_dictionary import BOT_FUNCTIONS
from functions import start, github, soap_country, weather, translate, exc_rates, numbers, http_cats, swear, getwiki


token = os.environ["TBOTTOKEN"]
bot = telebot.TeleBot(token)
wikipedia.set_lang("ru")

@bot.message_handler(commands=BOT_FUNCTIONS['start'].commands)
def send_welcome(message):
    bot.reply_to(message, start.get_start_message_from_bot_function_dictionary())

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_yes"), types.InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup

@bot.message_handler(commands=BOT_FUNCTIONS['test_keyboard'].commands)
def send_markup(message):
    bot.send_message(message.chat.id, "Да/Нет?", reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Ответ ДА!")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Ответ НЕТ!")

@bot.message_handler(commands=BOT_FUNCTIONS['country'].commands)
def get_country_info(message):
    soap_country.get_country_info(message, bot)

@bot.message_handler(commands=BOT_FUNCTIONS['commits'].commands)
def get_commits(message):
    github.get_commits(message, bot)

@bot.message_handler(commands=BOT_FUNCTIONS['issues'].commands)
def get_issues(message):
    github.get_issues(message, bot)

@bot.message_handler(commands=BOT_FUNCTIONS['grav'].commands)
def grav(message):
    str_spilt = message.text.split()
    arg = str_spilt[-1]
    email = libgravatar.Gravatar(arg)
    size = 200
    bot.send_message(text=email.get_image(size=size), chat_id= message.chat.id)
    bot.send_message(text=email.get_image(default='monsterid', force_default=True, size=size), chat_id= message.chat.id)
    bot.send_message(text=email.get_image(default='identicon', force_default=True, size=size), chat_id= message.chat.id)
    bot.send_message(text=email.get_image(default='wavatar', force_default=True, size=size), chat_id= message.chat.id)
    bot.send_message(text=email.get_image(default='robohash', force_default=True, size=size), chat_id= message.chat.id)
    bot.send_message(text=email.get_image(default='retro', force_default=True, size=size), chat_id= message.chat.id)

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
        fact_by_digit = numbers.get_fact_by_request('digit', {'digit': params[1]})
        bot.send_message(message.chat.id, text=fact_by_digit)
    elif '/date' in params and len(params) == 3:
        fact_by_date = numbers.get_fact_by_request('date', {'month': params[1], 'date': params[2]})
        bot.send_message(message.chat.id, text=fact_by_date)
    elif '/random' in params and len(params) == 1:
        fact_by_random = numbers.get_fact_by_request('random')
        bot.send_message(message.chat.id, text=fact_by_random)
    else:
        bot.send_message(message.chat.id, text="Некорректный формат команды. Повторите попытку!")

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
    
@bot.message_handler(commands=["getwiki"])

def wikipedia(m, res=False):

    bot.send_message(m.chat.id, 'Введите любое слово, чтобы узнать, что это такое!')

@bot.message_handler(content_types=["text"])

def handle_text(message):
    bot.send_message(message.chat.id, getwiki.getwiki(message.text))

bot.infinity_polling()
