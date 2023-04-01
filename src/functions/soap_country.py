from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import zeep

class SoapCountry(BotFunctionABC):
    
    def __init__(self) -> None:
        wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
        self.client = zeep.Client(wsdl=wsdl_url)

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.country_keyboard_factory = CallbackData('code_button', prefix=commands[0])

        @bot.message_handler(commands=commands)
        def country_handler(message: types.Message):
            self.get_country_info(message)
            
        @bot.callback_query_handler(func=None, config=self.country_keyboard_factory.filter())
        def example_keyboard_callback(call: types.CallbackQuery):
            callback_data: dict = self.country_keyboard_factory.parse(callback_data=call.data)
            code = callback_data['code_button']
            country_info = self.client.service.FullCountryInfo(code)
            self.do_work_on_service_response(code, country_info, call.message.chat.id)
    
            


    def gen_markup(self, arrStr):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 20
        buttons = []
        for val in arrStr:
            buttons.append(types.InlineKeyboardButton(val, 
            callback_data=self.country_keyboard_factory.new(code_button=val)))

        markup.add(*buttons)
        return markup



    @staticmethod
    def country_code_from_message(message):
        str_spilt = message.text.split()
        x = str_spilt[-1]
        return x.upper()

    def do_work_on_service_response(self, param, obj, chat_id):
        send_msg = f'param={param} \n {obj}'
        self.bot.send_message(text=send_msg, chat_id=chat_id)
        


    def get_country_info(self, message):
        code = SoapCountry.country_code_from_message(message)
        if (code == "ALL"):
            countryes = self.client.service.ListOfCountryNamesByCode()
            codes = []
            for country in countryes:
                codes.append(country.sISOCode)


            self.bot.send_message(text="Выбор страны!", chat_id=message.chat.id, reply_markup=self.gen_markup(codes))
            #self.do_work_on_service_response(code, codes, message.chat.id)
        else:
            country_info = self.client.service.FullCountryInfo(code)
            self.do_work_on_service_response(code, country_info, message.chat.id)
    