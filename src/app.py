import logging
import sys
import os
import telebot
from bot_middleware import Middleware
from bot_callback_filter import SystemIntegrationBotCallbackFilter
from bot_func_dictionary import BOT_FUNCTIONS_2
from load_atomic import LoadAtomic

from old_app import old_start

def get_log_level(env_key: str):
    str_level = os.environ.get(env_key)
    if str_level in logging._nameToLevel.keys():
        return logging._nameToLevel[str_level]
    else:
        return logging._nameToLevel["INFO"]
            
def get_logger()-> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(get_log_level("LOGLEVEL"))
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
    telebot.logger.setLevel(get_log_level("TBOT_LOGLEVEL"))
    bot = telebot.TeleBot(token, use_class_middlewares=True)
    return bot

def starter_functions():
    
    for funct in atom_functions_list:
        try:
            if(funct.state):
                logger.info("SKIP")
                #funct.set_handlers(bot)
                #logger.info(f'{funct} - start OK!')
            else:
                logger.info(f'{funct} - state FALSE!')
        except Exception as e:
            funct.state = False
            logger.warning(f'{funct} - start EXCEPTION!')

    for bf_key, bf_value in BOT_FUNCTIONS_2.items():
        try:
            if(bf_value.state):
                bf_value.bot_function.set_handlers(bot=bot, commands=bf_value.commands)
                logger.info(f'{bf_key} - start OK!')
            else:
                logger.info(f'{bf_key} - state FALSE!')
        except Exception as e:
            BOT_FUNCTIONS_2[bf_key].state = False
            logger.warning(f'{bf_key} - start EXCEPTION!')
            logger.exception(e)
        
    # old_start(bot, logger)

    @bot.message_handler(func=lambda message: True)
    def text_messages(message):
        bot.reply_to(message, "Text = " + message.text)
        bot.send_message(text="Ваш запрос не обработан!!!", chat_id=message.chat.id)


logger = get_logger()
bot = get_bot()
atom_functions_list = LoadAtomic.load_functions()

if __name__ == '__main__':
    logger.critical('-= START =-')
    starter_functions()
    bot.setup_middleware(Middleware(logger, bot))
    bot.add_custom_filter(SystemIntegrationBotCallbackFilter())
    bot.infinity_polling()
