
import libgravatar
from telebot import types

def grav(message, bot):
    markup = types.InlineKeyboardMarkup()
    default = types.InlineKeyboardButton(text='default', callback_data='cb_default')
    monsterid = types.InlineKeyboardButton(text='monsterid', callback_data='cb_monsterid')
    identicon = types.InlineKeyboardButton(text='identicon', callback_data='cb_identicon')
    wavatar = types.InlineKeyboardButton(text='wavatar', callback_data='cb_wavatar')
    robohash = types.InlineKeyboardButton(text='robohash', callback_data='cb_robohash')
    retro = types.InlineKeyboardButton(text='retro', callback_data='cb_retro')
    markup.add(default, monsterid, identicon, wavatar, robohash, retro)

    bot.send_message(message.chat.id, "Выберите тег выводимого изображения", reply_markup=markup)

def main(id, bot, message):

    print(message)

    str_spilt = message.text.split()
    arg = str_spilt[-1]
    email = libgravatar.Gravatar(arg)
    size = 200

    match(id):
            case('1'):
                bot.send_message(text=email.get_image(size=size), chat_id= message.chat.id)
            case('2'):
                bot.send_message(text=email.get_image(default='monsterid', force_default=True, size=size), chat_id= message.chat.id)
            case('3'):
                bot.send_message(text=email.get_image(default='identicon', force_default=True, size=size), chat_id= message.chat.id)
            case('4'):
                bot.send_message(text=email.get_image(default='wavatar', force_default=True, size=size), chat_id= message.chat.id)
            case('5'):
                bot.send_message(text=email.get_image(default='robohash', force_default=True, size=size), chat_id= message.chat.id)
            case('6'):
                bot.send_message(text=email.get_image(default='retro', force_default=True, size=size), chat_id= message.chat.id)