from bot_func_abc import BotFunctionABC
import telebot
from telebot import types
from telebot.callback_data import CallbackData, CallbackDataFilter
from typing import List
import zeep

from emot.emo_unicode import UNICODE_EMOJI, UNICODE_EMOJI_ALIAS, EMOTICONS_EMO, EMOJI_ALIAS_UNICODE


class SoapCountry(BotFunctionABC):
    
    def __init__(self) -> None:
        wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
        self.client = zeep.Client(wsdl=wsdl_url)
        


    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot 
        self.country_keyboard_factory = CallbackData('code_button', prefix=commands[0])
        self.country_name_dict = {}
        self.country_phone_dict = {}
        countryes = self.client.service.FullCountryInfoAllCountries()
        for country in countryes:
            self.country_name_dict[country.sISOCode] = country.sName
            self.country_phone_dict[country.sISOCode] = country.sPhoneCode

        

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
        markup.row_width = 8
        buttons = []
        for val in arrStr:
            buttons.append(types.InlineKeyboardButton(val, 
            callback_data=self.country_keyboard_factory.new(code_button=val)))

        markup.add(*buttons)
        return markup



    def country_code_from_message(self, message):
        str_spilt = message.text.split()
        len_str = len(str_spilt)
        if len_str == 1:
            return "ALL"
        
        x = str_spilt[-1]

        if x in UNICODE_EMOJI.keys():
            country_name = UNICODE_EMOJI[x].strip(":").replace("_"," ")
            country_iso_code = self.client.service.CountryISOCode(country_name)
            return country_iso_code

        if x.upper() in self.country_name_dict.keys():
            return x.upper()

        if x in self.country_name_dict.values():
            name_code = {x: y for y, x in self.country_name_dict.items()}
            return name_code[x]

        if x in self.country_phone_dict.values():
            phone_code = {x: y for y, x in self.country_phone_dict.items()}
            return phone_code[x]

        for c_code, c_name in self.country_name_dict.items():
            if x.lower() in c_name.lower(): 
                return c_code
            

    def do_work_on_service_response(self, param, obj, chat_id):
        send_msg = f'ISOCode = {param} \n {obj}'
        self.bot.send_message(text=send_msg, chat_id=chat_id)
        

    def get_country_info(self, message):
        code = self.country_code_from_message(message)
        if code is None or code.upper() == "ALL" or code == "No country found by that name":
            countryes = self.client.service.ListOfCountryNamesByCode()
            codes = []
            for country in countryes:
                codes.append(country.sISOCode)
            self.bot.send_message(text="Выбор страны!", chat_id=message.chat.id, reply_markup=self.gen_markup(codes))
        else:
            country_info = self.client.service.FullCountryInfo(code)
            self.do_work_on_service_response(code, country_info, message.chat.id)
    