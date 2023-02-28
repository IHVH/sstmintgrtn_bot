from dataclasses import dataclass


@dataclass
class BotFunction:
    commands: list[str]
    authors: list[str]
    about: str
    description: str


BOT_FUNCTIONS = {
    'start': BotFunction(
        commands=['start', 'help'],
        authors=['IHVH'],
        about='Старт бота и помощь по командам!',
        description='Функция предназначена для информирования пользователей о возможностях бота.'
    ),
    "get_gif": BotFunction(
        commands=["get_gif"],
        authors=["DavidShariev"],
        description="Подбор подходящей гивки. /get_gif [строка для поиска гивки]",
        about="Гивки"
    ),
    'test_keyboard': BotFunction(
        commands=['keyboard', 'testkeyboard'],
        authors=['IHVH'],
        description='Тестовая клавиатура',
        about='Тестовая клавиатура'
    ),
    'issues': BotFunction(
        commands=['issues', 'gi'],
        authors=['IHVH'],
        about='Получение информации о issues',
        description='Получение информации о issues для репозитария https://github.com/IHVH/OEMIB_PI01_19_TBOT \n ' +
        'Передайте в качестве параметра число для получения информации об указаном количестве последних issues. Например "/issues 5" '
    ),
    'commits': BotFunction(
        commands=['commits', 'gc'],
        authors=['IHVH'],
        about='Получение информации о коммитах.',
        description='Получение информации о коммитах для репозитария https://github.com/IHVH/OEMIB_PI01_19_TBOT \n ' +
        'Передайте в качестве параметра число для получения информации об указаном количестве последних коммитов. Например "/gc 5" '
    ),
    'kinopoisk': BotFunction(
        commands=['kinopoisk'],
        authors=['kagayato'],
        about='Получение информации о фильмах в кинопоиске',
        description='Получение информации о о фильмах для репозитария https://github.com/IHVH/OEMIB_PI01_19_TBOT \n ' +
        'Передать информацию о фильме . Например "/kinopoisk фильм" '
    ),

    'openweather': BotFunction(
        commands=['openweather'],
        authors=['doppler'],
        about='Получение информации о погоде',
        description='Получение информации о погоде для репозитария https://github.com/IHVH/OEMIB_PI01_19_TBOT \n ' +
        'Передать информацию о погоде . Например "/openweather город" '
    ),

    'country': BotFunction(
        commands=['country', 'cy'],
        authors=['IHVH'],
        about='Информация о странах.',
        description='Получение информации о странах по коду страны \n ' +
        'Передайте в качестве параметра ISO код страны. Например "/country RU" \n ' +
        'Передайте в качестве параметра строку all для получения доступных ISO кодов стран. Например "/country ALL" '
    ),
    'grav': BotFunction(
        commands=['grav', 'gravatar'],
        authors=['BigBeatProphet', 'IHVH'],
        description='Получить аватар из сервиса gravatar',
        about='Как аргумент принимает email. Например "/grav test@mail.ru"'
    ),
    'weather': BotFunction(
        commands=['weather'],
        authors=['Kostasus'],
        about='Получение информации о погоде',
        description='Введите адрес в формате: <Название города>, <Название улицы>, <Дом>'
    ),
    'accuweather': BotFunction(
        commands=['accuweather'],
        authors=['PR0YA'],
        about='Получение информации о погоде с источника Accuweather',
        description='Введите команду в формате: <Мой город ...>'
    ),
    'translate': BotFunction(
        commands=['translate'],
        authors=['lanaveta0104 '],
        about='Перевод слова на английский или русский язык, а также вывод синонимов слова',
        description='Введите язык перевода в виде "en" - английский или "ru" - русский и затем необходимое "слово"\n' +
        'Слово должно быть в начальной форме!\n' +
        'Например, для перевода на английский - /translate en Привет\n' +
        'Для перевода на русский - /translate ru Hello\n' +
        'Остальные символы после введенного слова игнорируются!'
    ),
    'excrate': BotFunction(
        commands=['excrate'],
        authors=['redjuk'],
        about='Отображение курса валют на сегодняшний день',
        description='Введите код валюты в формате ISO 4217. Для просмотра возможных вариантов наберите команду /excrate list'
    ),
    'numbers': BotFunction(
        commands=['digit', 'date', 'random'],
        authors=['myrlifox'],
        about='Забавные факты о числах и датах',
        description='Получение факта по числу или дате \n ' +
        'Для получения факта по числу в качестве параметра укажите число. Например "/digit 15" \n ' +
        'Для получения факта по дате в качестве параметра укажите название месяца и число из этого месяца. Например "/date Август 14" \n ' +
        'Для получения случайного факта укажите команду /random'
    ),
    'http': BotFunction(
        commands=['http'],
        authors=['ostrichsmile'],
        about='По котику на каждый http статус',
        description='Введите http код, например /http 204. Для просмотра возможных вариантов наберите команду /http list'
    ),
    'insult': BotFunction(
        commands=['insult'],
        authors=['ectmeyou'],
        about='Получить ругательство из сервиса',
        description='Получить ругательство из сервиса'
    ),
    'speller': BotFunction(
        commands=['speller'],
        authors=['maria21-hub'],
        about='Проверка орфографии',
        description='Введите слово после команды /speller, например "/speller Превет"\n' +
        'Бот выдаст исправленное слово. Остальные слова после первого игнорируются.'
    ),
    'Wikipedia': BotFunction(
        commands=['Wikipedia'],
        authors=['iznopa'],
        about='Быстрый поиск определения с помощью Wikipedia',
        description='Введи любое слово после /Wikipedia, например "/Wikipedia Java"\n' +
        'Бот выдаст определение которое нашел.'
    ),
    'mks': BotFunction(
        commands=['mks'],
        authors=['f1mca'],
        about='Получение информации о нахождение мкс',
        description='Введите /mks'
    ),
    'anecdote': BotFunction(
        commands=['anecdote'],
        authors=['alekseikornyushko'],
        about='Рандомный анекдот специально для Вас',
        description='Введите /anecdote с числовым аргументом'
    ),
}
