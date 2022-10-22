from email import header
import os
from urllib import response
import telebot
import requests
from telebot import types
from bot_command_dictionary import BOT_FUNCTIONS
from functions import start
from functions import github

token = os.environ["TBOTTOKEN"]
bot = telebot.TeleBot(token)

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_yes"), types.InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup

@bot.message_handler(commands=BOT_FUNCTIONS['commits'].commands)
def get_commits(message):
    github.get_commits(message, bot)

@bot.message_handler(commands=BOT_FUNCTIONS['test1'].commands)
def send_test(message):
    params = {"state": "all"}
    headers = {"Accept":"application/vnd.github+json", 
    "Authorization": f'Bearer {os.environ["GITHUBTOKEN"]}'}
    response = requests.get("https://api.github.com/repos/IHVH/OEMIB_PI01_19_TBOT/issues", headers=headers, params=params)
    
    if(response):
        bot.send_message(text=f'{response}', chat_id= message.chat.id)
        issues = response.json()
        for iss in issues:
            login = iss["user"]["login"]
            state = iss["state"]
            title = iss["title"]
            body = iss["body"]
            bot.send_message(text=f'{state} - {login} - {title} - {body}', chat_id= message.chat.id)

    else: 
        bot.send_message(text=f'{response}', chat_id= message.chat.id)
    

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
    bot.send_message(text="Ваш запрос не обработан!!!", chat_id= message.chat.id)

bot.infinity_polling()
