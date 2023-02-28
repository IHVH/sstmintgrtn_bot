
import libgravatar
from telebot import types
from telebot.callback_data import CallbackData

def grav(message, bot, callData: CallbackData):
    str_spilt = message.text.split()
    arg = str_spilt[-1]
    markup = types.InlineKeyboardMarkup()
    default = types.InlineKeyboardButton(text='default', callback_data=callData.new(grav_button="default", grav_email=arg))
    monsterid = types.InlineKeyboardButton(text='monsterid', callback_data=callData.new(grav_button="monsterid", grav_email=arg))
    identicon = types.InlineKeyboardButton(text='identicon', callback_data=callData.new(grav_button="identicon", grav_email=arg))
    wavatar = types.InlineKeyboardButton(text='wavatar', callback_data=callData.new(grav_button="wavatar", grav_email=arg))
    robohash = types.InlineKeyboardButton(text='robohash', callback_data=callData.new(grav_button="robohash", grav_email=arg))
    retro = types.InlineKeyboardButton(text='retro', callback_data=callData.new(grav_button="retro", grav_email=arg))
    markup.add(default, monsterid, identicon, wavatar, robohash, retro)

    bot.send_message(message.chat.id, "Выберите тег выводимого изображения", reply_markup=markup)

def main(bot, call, callback_data: dict):
    grav_button = callback_data['grav_button']
    grav_email = callback_data['grav_email']
    email = libgravatar.Gravatar(grav_email)
    size = 200
    if(grav_button == "default"):
        bot.send_message(text=email.get_image(size=size), chat_id=call.message.chat.id)
    else:
        bot.send_message(text=email.get_image(default=grav_button, force_default=True, size=size), chat_id=call.message.chat.id)
    