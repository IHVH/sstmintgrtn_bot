from bot_func import BotFunction, BotFunction2

from functions.start import StartInfoBotFunction
from functions.example_bot_function import ExampleBotFunction
from functions.dadata import DadataFunctionClass
from functions.github2 import GitHubFunctions
from functions.genius import GeniusFunction
from functions.menu_with_some_functions import IndividualBotWithMenu
from functions.doggie import RandomDogAPIFunction
from functions.youtube import YoutubeFinder
from functions.soap_country import SoapCountry
from functions.animetarelka import Animetarelka,Mangatarelka
from functions.cat import CatFunction
from functions.human import HumanGenerator
from functions.goroskop import GoroskopFunction
from functions.currency_exchange_rate import GetCurrencyExchangeRate
from functions.music import Music
from functions.SteamStatus import ServerStatus

BOT_FUNCTIONS_2 = {
    "start_info": BotFunction2(
        bot_function=StartInfoBotFunction(),
        commands=["start", "help", "s", "h", "how_pass"],
        authors=["IHVH"],
        about="Старт бота и помощь по командам!",
        description="Функция предназначена для информирования пользователей о возможностях бота. \n"
        "Спросить как сдать зачёт отправь `/how_pass` ",
    ),
    "example_bot_function": BotFunction2(
        bot_function=ExampleBotFunction(),
        commands=["example", "ebf"],
        authors=["IHVH"],
        about="Пример функции бота!",
        description="В поле  *description* поместите подробную информацию о работе функции. "
        "Описание способов использования, логики работы. Примеры вызова функции - /ebf \n"
        "Возможные параметры функции `/example` ",
    ),
    "github": BotFunction2(
        bot_function=GitHubFunctions(),
        commands=["git", "commits"],
        authors=["IHVH"],
        about="Получение информации о коммитах",
        description="Получение информации из репозитория [OEMIB_PI01_19_TBOT](https://github.com/IHVH/OEMIB_PI01_19_TBOT) \n"
        "Передайте в качестве параметра количество записей. Например `/commits 5` ",
    ),
    "dadata": BotFunction2(
        bot_function=DadataFunctionClass(),
        commands=["dadata"],
        authors=["aishmurodov"],
        about="По введенному ИНН находит компанию и выводит информацию о ней",
        description=(
            "Получение информации о компаний по ИНН. \n Передайте в качестве параметра ИНН "
            "компании для получения краткой информации по имени, адресу и тд. Например /dadata 7707083893"
        ),
    ),
    "genius": BotFunction2(
        bot_function=GeniusFunction(),
        commands=["genius"],
        authors=["GradoboevPavel"],
        about="Поиск слов трека",
        description="Введите /genius исполнитель - трек",
    ),
    "menu_with_some_functions": BotFunction2(
        bot_function=IndividualBotWithMenu(),
        commands=["functionalmenu"],
        authors=["strlex-dev"],
        about="Меню с разным функционалом внутри",
        description="Введите команду - /functionalmenu и выберите любую понравившуюся функцию в меню.\n"
                    "🛰 - Место положение МКС в реальном времени,\n"
                    "👨‍🚀 - Кто находится на МКС и общее количество человек,\n"
                    "🌦 - Погода в реальном времени в любом заданом городе,\n"
                    "💸 - Вывод стоиомости запрашиваемой криптовалюты",

    ),
    "doggie": BotFunction2(
        bot_function=RandomDogAPIFunction(),
        commands=["doggie","d","breeds"],
        authors=["may-uri"],
        about="Случайная фотография собачки, способная осчастливить любого.",
        description="\n*/doggie*, */d* - вызов случайной картинки с собачкой,\n ⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀\n"
        "/doggie *{breed}*, /d *{breed}* - вызов картинки с собачкой определенной породы, которая определяется в {breed},\n⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀\n"
        "*/breeds* - вывод списка со всеми возможными породами",
    ),
    "youtube": BotFunction2(
        bot_function=YoutubeFinder(),
        commands=["YTfind"],
        authors=["ironravencrest"],
        about="Поиск названий youtube видео",
        description="Введите команду - /YTfind",
    ),
    "country": BotFunction2(
        bot_function=SoapCountry(),
        commands=["country", "cy"],
        authors=["IHVH"],
        about="Информация о странах.",
        description=("Получение информации о странах по названию, ISO коду, emoji флагу или телефонному коду. \n "
        "Передайте в качестве параметра \n - emoji флаг страны `/country \U0001F1F7\U0001F1FA` \n"
        " - название страны `/country Russia` \n" 
        " - iso код страны `/country RU` \n - или телефонный код страны `/country 7` \n"
        "Для получения доступных *ISO* кодов стран передайте в качестве параметра строку *ALL*. Например `/country ALL` ")
    ),
    "animetarelka": BotFunction2(
        bot_function=Animetarelka(),
        commands=["rndanime"],
        authors=["d1mens1"],
        about="Слуйчайное аниме",
        description=("/rndanime выдает случайное аниме с краткой иформацией о нем")
    ),
    "mangatarelka": BotFunction2(
        bot_function=Mangatarelka(),
        commands=["rndmanga"],
        authors=["d1mens1"],
        about="Слуйчайная манга",
        description=("/rndmanga выдает случайную мангу с краткой иформацией о ней")
    ),
    "cat": BotFunction2(
        bot_function=CatFunction(),
        commands=["cat"],
        authors=["Qipk"],
        about="Случайное фото кота",
        description=("Введите /cat для получения случайного фото кота")
    ),
    "human": BotFunction2(
        bot_function=HumanGenerator(),
        commands=["human"],
        authors=["IMJAV"],
        about="Случайная собачка?..\nСлучайный котик?..\nА может, случайный аНеКдОт?...\nА как насчёт...\nСЛУЧАЙНОГО ЧЕЛОВЕКА С ЕГО ЛИЧНЫМИ ДАННЫМИ, М???\n",
        description=("\nПочувствуй себя Большим Братом! ;)")
    ),
    "goroskop": BotFunction2(
        bot_function=GoroskopFunction(),
        commands=["goroskop"],
        authors=["livin161"],
        about="Выводит гороско на сегодняшний день",
        description=("/goroskop выдает гороскоп на сегодняшний день")
    ),
    "music": BotFunction2(
        bot_function=Music(),
        commands=["music"],
        authors=["cash3mod3l"],
        about="Выводит 5 последних альбомов исполнителей",
        description=("/music Нужно написать имя исполнентеля и бот тебе выведет 5 последних его альбомов")
    ),
    "currency_exchange_rate": BotFunction2(
        bot_function=GetCurrencyExchangeRate(),
        commands=["currency"],
        authors=["xeotype"],
        about="Показывает текущий курс валют к рублю",
        description="Собсна смотрим текущий курс валют, ето всё",
    ),
    "SteamStatus": BotFuction2(
        bot_function=ServerStatus(),
        commands=['status']
        authors=["eldorPulatov"],
        about="Показывает стостояние серверов Steam",
        description="Довольно часто в игре Dota 2 или CS:GO падают сервера, поэтому я создал функцию, где можно отлеживать состояние серверов",
    )
}

BOT_FUNCTIONS = {
    "get_gif": BotFunction(
        commands=["get_gif"],
        authors=["DavidShariev"],
        about="Подбор подходящей гивки",
        description="Подбор подходящей гивки. `/get_gif` <строка для поиска гивки>",
    ),
    "kinopoisk": BotFunction(
        commands=["kinopoisk"],
        authors=["kagayato"],
        about="Получение информации о фильмах в кинопоиске",
        description="Получение информации о фильмах \n "
        + 'Передать информацию о фильме . Например "/kinopoisk фильм" ',
    ),
    "openweather": BotFunction(
        commands=["openweather"],
        authors=["doppler"],
        about="Получение информации о погоде",
        description="Получение информации о погоде \n "
        + 'Передать информацию о погоде . Например "/openweather город" ',
    ),
    "grav": BotFunction(
        commands=["grav", "gravatar"],
        authors=["BigBeatProphet", "IHVH"],
        description="Получить аватар из сервиса gravatar",
        about='Как аргумент принимает email. Например "/grav test@mail.ru"',
    ),
    "weather": BotFunction(
        commands=["weather"],
        authors=["Kostasus"],
        about="Получение информации о погоде",
        description="Введите адрес в формате: <Название города>, <Название улицы>, <Дом>",
    ),
    "accuweather": BotFunction(
        commands=["accuweather"],
        authors=["PR0YA"],
        about="Получение информации о погоде с источника Accuweather",
        description="Введите команду в формате: <Мой город ...>",
    ),
    "translate": BotFunction(
        commands=["translate"],
        authors=["lanaveta0104"],
        about="Перевод слова на английский или русский язык, а также вывод синонимов слова",
        description='Введите язык перевода в виде "en" - английский или "ru" - русский и затем необходимое "слово"\n'
        + "Слово должно быть в начальной форме!\n"
        + "Например, для перевода на английский - /translate en Привет\n"
        + "Для перевода на русский - /translate ru Hello\n"
        + "Остальные символы после введенного слова игнорируются!",
    ),
    "excrate": BotFunction(
        commands=["excrate"],
        authors=["redjuk"],
        about="Отображение курса валют на сегодняшний день",
        description="Введите код валюты в формате ISO 4217. Для просмотра возможных вариантов наберите команду /excrate list",
    ),
    "numbers": BotFunction(
        commands=["digit", "date", "random"],
        authors=["myrlifox"],
        about="Забавные факты о числах и датах",
        description="Получение факта по числу или дате \n "
        + 'Для получения факта по числу в качестве параметра укажите число. Например "/digit 15" \n '
        + 'Для получения факта по дате в качестве параметра укажите название месяца и число из этого месяца. Например "/date Август 14" \n '
        + "Для получения случайного факта укажите команду /random",
    ),
    "http": BotFunction(
        commands=["http"],
        authors=["ostrichsmile"],
        about="По котику на каждый http статус",
        description="Введите http код, например /http 204. Для просмотра возможных вариантов наберите команду /http list",
    ),
    "insult": BotFunction(
        commands=["insult"],
        authors=["meyouect"],
        about="Получить ругательство из сервиса",
        description="Получить ругательство из сервиса",
    ),
    "speller": BotFunction(
        commands=["speller"],
        authors=["maria21-hub"],
        about="Проверка орфографии",
        description='Введите слово после команды /speller, например "/speller Превет"\n'
        + "Бот выдаст исправленное слово. Остальные слова после первого игнорируются.",
    ),
    "Wikipedia": BotFunction(
        commands=["Wikipedia"],
        authors=["iznopa"],
        about="Быстрый поиск определения с помощью Wikipedia",
        description='Введи любое слово после /Wikipedia, например "/Wikipedia Java"\n'
        + "Бот выдаст определение которое нашел.",
    ),
    "mks": BotFunction(
        commands=["mks"],
        authors=["f1mca"],
        about="Получение информации о нахождение мкс",
        description="Введите /mks",
    ),
    "anecdote": BotFunction(
        commands=["anecdote"],
        authors=["alekseikornyushko"],
        about="Рандомный анекдот специально для Вас",
        description="Введите /anecdote с числовым аргументом",
    ),
}
