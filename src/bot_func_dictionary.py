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
from functions.animetarelka import Animetarelka, Mangatarelka
from functions.cat import CatFunction
from functions.human import HumanGenerator
from functions.goroskop import GoroskopFunction
from functions.currency_exchange_rate import GetCurrencyExchangeRate
from functions.fileEditBot import FileEditBotClass
from functions.music import Music
from functions.Citata import CitataGenerator
from functions.nytimes import NYTimes_science
from functions.Jokes import Joke
from functions.get_ip import GetBotHostIP
from functions.Plane_Search import PlaneSearchClass
from functions.movie import imdbFinder
from functions.find_cat import FindCat
from functions.quotes import Quotes
from functions.theBestMovieBot import TheBestMovieBot
from functions.news_bot import NewsFeed
from functions.randomactivity import Randomactivity 
from functions.meow import meowfact
from functions.password import RandomPassword
from functions.random_fox import RandomFox
from functions.cards import RandomCard
from functions.kanye import kanyequote

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
        state=True,
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

    "meow": BotFunction2(
        bot_function=meowfact(),
        commands=["meow"],
        authors=["may-uri"],
        about="Различные факты о котиках на английском языке",
        description="Введите /meow чтобы прочитать удивительный факти о котиках",
    ),
    "kanyequote": BotFunction2(
        bot_function=kanyequote(),
        commands=["kanye"],
        authors=["Captain21Owl"],
        about="Случайная цитата Kanye West",
        description="Введите /kanye для получения случайной цитаты",
    ),
    "password": BotFunction2(
        bot_function=RandomPassword(),
        commands=["password"],
        authors=["SamSouls"],
        about="Генерация случайного пароля",
        description="Введите /password для получения случайного пароля",
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
    "news_bot": BotFunction2(
        bot_function=NewsFeed(),
        commands=["worldnews"],
        authors=["asaamlnk"],
        about="Новостной буревестник!",
        description="Введите команду - /worldnews и выберите категорию поиска новостей. \n"
                    "🌍 Страна - Поиск по аббревиатуре страны \n"
                    "⌨️ Ключевое слово - Поиск по ключевому слову",
    ),
    "doggie": BotFunction2(
        bot_function=RandomDogAPIFunction(),
        commands=["doggie", "d", "breeds"],
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
    "сitata": BotFunction2(
        bot_function=CitataGenerator(),
        commands=["citata"],
        authors=["Lizapopa40"],
        about="Выводит случайную цитату 'Из Японских комиксов'",
        description=("радуйся жизни")
    ),
    "goroskop": BotFunction2(
        bot_function=GoroskopFunction(),
        commands=["goroskop"],
        authors=["livin161"],
        about="Выводит гороско на сегодняшний день",
        description=("/goroskop выдает гороскоп на сегодняшний день")
    ),
     "Activity": BotFunction2(
        bot_function=Randomactivity(),
        commands=["Activity"],
        authors=["YoruNoru"],
        about="Выводит случайную активность если незнаешь чем заняться",
        description=("давай делай")
    ),
    "find_cat": BotFunction2(
        state=False,
        bot_function=FindCat(),
        commands=["find_cat"],
        authors=["Kyozzetsu"],
        about="Выводит информацию о породе кота",
        description=("`/find_cat`, показывает информацию о породе кота и фотографию")
    ),
    "music": BotFunction2(
        bot_function=Music(),
        commands=["music"],
        authors=["cash3mod3l"],
        about="Выводит 5 последних альбомов исполнителей",
        description=("/music Нужно написать имя исполнентеля и бот тебе выведет 5 последних его альбомов")
    ),
    "quotes": BotFunction2(
        bot_function=Quotes(),
        commands=["quotes"],
        authors=["AnnaKonoplya"],
        about="Выводит рандомные цитаты",
        description=("Нужно ввести команду /quotes, чтобы вывелась рандомная цитата")
    ),
    "currency_exchange_rate": BotFunction2(
        bot_function=GetCurrencyExchangeRate(),
        commands=["currency"],
        authors=["xeotype"],
        about="Показывает текущий курс валют к рублю",
        description="Собсна смотрим текущий курс валют, ето всё",
    ),
    "file_edit_bot": BotFunction2(
        bot_function=FileEditBotClass(),
        commands=["registration", "menu", "freExit"],
        authors=["KurzerName"],
        about="Бот для работы с заметкой",
        description="Позволяет работать со своей заметочкой. "
                    + "\n Для начала работы используйте команду /menu или /registration"
                    + "\n Для выхода используйте коммандку /exit",
    ),
    "NYTimes": BotFunction2(
        bot_function=NYTimes_science(),
        commands=["news"],
        authors=["eldorPulatov"],
        about="Показывает заголовки новостей в области науки",
        description="Новости в области науки из газеты New York Times",
    ),
    "Joke": BotFunction2(
        bot_function=Joke(),
        commands=["Chack"],
        authors=["Leonnid111"],
        about="Выдает крутую шутку о Чак Норрисе",
        description="Шутеечка о непобидимом Чак Норрисее йиха",
    ),
    "Get bot host IP address": BotFunction2(
        bot_function=GetBotHostIP(),
        commands=["get_loc"],
        #authors=["ino943"], #Page not available test fails (return this string when the page is available)
        authors=["IHVH"],
        about="Гео данные по ip адресу",
        description="Да, оно вычисляет по IP. Буквально. Передайте в качестве параметра ip адрес например `/get_loc 192.168.0.1`",
    ),
    "Plane search": BotFunction2(
        bot_function=PlaneSearchClass(),
        commands=["goGuguGagaGugu", "site", "website"],
        authors=["GuguGagaGugu"],
        about="Выводит информацию по рейсам",
        description= "Выполняет поиск рейсов по названию рейса и вывод информации о рейсе, редиректит на сайт ru.flightaware.com",
    ),
    "imdbFinder": BotFunction2(
        bot_function=imdbFinder(),
        commands=["find"],
        authors=["Lokadv"],
        about="Выводит информацию с imdb по введенному названию фильма или сериала",
        description="/find продолжительность, жанр, описание и т.д. интересующего фильма или сериала",
    ),
    "TheBestMovieBot": BotFunction2(
        bot_function=TheBestMovieBot(),
        commands=["findTheBestMovie", "findOtherMovie", "theBestMovieList"],
        authors=["defaultxddd"],
        about="Бот выводит самый лучший фильм",
        description="Бот выводит самый лучший фильм, ну может и остальные вывести",
    ),
    "random_fox": BotFunction2(
        bot_function=RandomFox(),
        commands=["random_fox"],
        authors=["Bogpiva"],
        about="Генерация случайной лисы",
        description="Бот выводит фотографию случайной лисы",
    ),
    "Cards": BotFunction2(
        bot_function=RandomCard(),
        commands=["card"],
        authors=["polfckz"],
        about="Мини-игра с картами",
        description="Два игрока, каждый должен взять карту(выдается рандомно), у кого карта больше, тот победил",
    ),
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
