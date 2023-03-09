import logging
import sys
import os
import telebot
from bot_callback_filter import SystemIntegrationBotCallbackFilter
from bot_func_dictionary import BOT_FUNCTIONS_2

from old_app import old_start

def get_logger()-> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f"{__name__}.log")
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

def get_bot()-> telebot.TeleBot:
    token = os.environ["TBOTTOKEN"]
    bot = telebot.TeleBot(token)
    return bot

def starter_functions():

    for bf_key, bf_value in BOT_FUNCTIONS_2.items():
        try:
            bf_value.bot_function.set_handlers(bot=bot, commands=bf_value.commands)
            logger.info(f'{bf_key} - start OK!')
        except Exception as e:
            logger.exception(e)
        
    old_start(bot, logger)

    @bot.message_handler(func=lambda message: True)
    def text_messages(message):
        bot.reply_to(message, "Text = " + message.text)
        bot.send_message(text="Ваш запрос не обработан!!!", chat_id=message.chat.id)
    
    
logger = get_logger()
bot = get_bot()

if __name__ == '__main__':
    print('-= START =-')
    logger.info('-= START =-')
    starter_functions()
    bot.add_custom_filter(SystemIntegrationBotCallbackFilter())
    bot.infinity_polling()