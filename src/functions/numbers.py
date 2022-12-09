import requests

#словарь с месяцами для отправки запросов по дате (в запросе используется номер месяца)
MONSTH = {
    'Январь': 1,
    'Февраль': 2,
    'Март': 3,
    'Апрель': 4,
    'Май': 5,
    'Июнь': 6,
    'Июль': 7,
    'Август': 8,
    'Сентябрь': 9,
    'Октябрь': 10,
    'Ноябрь': 11,
    'Декабрь': 12,
}

def is_check_date(month, date):
    if month in ['Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь'] and int(date) in range(1, 32):
        return True
    elif month in ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь'] and int(date) in range(1, 31):
        return True
    elif month == 'Февраль' and int(date) in range(1, 30):
        return True

    return False

def get_fact_by_request(type_request, params_request=None):
    if type_request == 'digit':
        response = requests.get('http://numbersapi.com/' + params_request['digit'])  # отправка запроса для получения факта по числу
    elif type_request == 'date':
        if is_check_date(params_request['month'], params_request['date']):
            response = requests.get('http://numbersapi.com/' + str(MONSTH[params_request['month']]) + '/'
                                    + params_request['date'] + '/date')  # отправка запроса для получения факта по дате
        else:
            return 'Некорректный формат. Повторите попытку!'
    elif type_request == 'random':
        response = requests.get('http://numbersapi.com/random/year')  # отправка запроса для получения случайного факта (можно получить случайный факт только по году)

    if response.status_code == 200:
        return response.content
    else:
        return 'Запрос выполнился с ошибкой. Повторите попытку!'