import requests
import xmltodict

# Creating dictionary with http codes
def get_codes_list():
    response = requests.get("https://www.iana.org/assignments/http-status-codes/http-status-codes.xml")
    xml_dict = xmltodict.parse(response.content)
    http_arr = xml_dict["registry"]["registry"]["record"]
    http_list = {}
    for elm in http_arr:
        http_list[elm['value']] = elm['description']
    return http_list

# Checking if code Exists. Creating a link to an image
def get_cat(http_code):
    codes_list = get_codes_list()
    if (http_code in codes_list):
        cat_url = f"https://httpcats.com/{http_code}.jpg"
        return cat_url
    else:
        return "Введенный http код не существует. Введите http код, например /http 204. Для просмотра возможных вариантов наберите команду /http list"
