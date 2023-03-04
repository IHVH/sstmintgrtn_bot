import telebot
from telebot import types
import urllib.request
import json

tgtoken=json.load(open("token.json"))
bot = telebot.TeleBot(tgtoken['token'])


@bot.message_handler(commands=["mks"])
def inline(message):
 key = types.InlineKeyboardMarkup()
 cord = types.InlineKeyboardButton(text="да", callback_data="да")
 key.add(cord)
 bot.send_message(message.chat.id, "хотите узнать местоположение мкс?", reply_markup=key)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'да':
     key = types.InlineKeyboardMarkup()
     req = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
     obj = json.loads(req.read())
     bot.send_message(c.message.chat.id,f"отметка времени {obj['timestamp']}", reply_markup=key)
     bot.send_message(c.message.chat.id, f"долгота {obj['iss_position']['longitude']} и широта  {obj['iss_position']['latitude']}", reply_markup=key)

bot.polling(none_stop=True)
