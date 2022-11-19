import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=wsdl_url)

def country_code_from_message(message):
    str_spilt = message.text.split()
    x = str_spilt[-1]
    return x.upper()

def do_work_on_service_response(param, obj, bot, chat_id):
    send_msg = f'param={param} \n {obj}'
    bot.send_message(text=send_msg, chat_id=chat_id)
    


def get_country_info(message, bot):
    code = country_code_from_message(message)
    if (code == "ALL"):
        countryes = client.service.ListOfCountryNamesByCode()
        result_str = ""
        for country in countryes:
            result_str = result_str + f'{country.sISOCode}, '

        do_work_on_service_response(code, result_str, bot, message.chat.id)
    else:
        country_info = client.service.FullCountryInfo(code)
        do_work_on_service_response(code, country_info, bot, message.chat.id)
    