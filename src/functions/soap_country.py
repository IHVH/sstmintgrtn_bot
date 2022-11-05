import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=wsdl_url)

def country_code_from_message(message):
    str_spilt = message.text.split()
    x = str_spilt[-1]
    return x


def get_country_info(message, bot):
    params = country_code_from_message(message)
    params["state"] = "all"
    #response = requests.get(url_issues(), headers=headers(), params=params)
    #do_work_on_issues(response, bot, message.chat.id)