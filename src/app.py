from email import header
import os
from urllib import response
import telebot
import requests
import libgravatar
from telebot import types
from bot_command_dictionary import BOT_FUNCTIONS
from functions import start, github, soap_country

token = os.environ["TBOTTOKEN"]
bot = telebot.TeleBot(token)

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

@bot.message_handler(func =lambda message:True)
def text_messages(message):
    bot.reply_to(message, "Text = " + message.text)
    bot.send_message(text="Ваш запрос не обработан!!!", chat_id= message.chat.id)

bot.infinity_polling()
