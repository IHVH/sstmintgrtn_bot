#TEST

import os
import telebot
from telebot import types
from bot_command_dictionary import BOT_FUNCTIONS
from functions import start

token = os.environ["BOTTOKEN"]
bot = telebot.TeleBot(token)

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_yes"), types.InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup

@bot.message_handler(commands=BOT_FUNCTIONS['start'].commands)
def send_welcome(message):
    bot.reply_to(message, start.get_start_message_from_bot_function_dictionary())

@bot.message_handler(commands=BOT_FUNCTIONS['test_keyboard'].commands)
def send_markup(message):
    bot.send_message(message.chat.id, "Да/Нет?", reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Ответ ДА!")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Ответ НЕТ!")


@bot.message_handler(func =lambda message:True)
def text_messages(message):
    bot.reply_to(message, "Text = " + message.text)
    bot.send_message(text="Ваш запрос не обработан!", chat_id= message.chat.id)

bot.infinity_polling()
