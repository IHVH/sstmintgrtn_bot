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
            authors=['BigBeatProphet'], 
            description='Тестирование функционала gravatar', 
            about='как аргумент принимает email'
        ),
        'weather': BotFunction(
            commands=['weather'],
            authors=['Kostasus'],
            about='Получение информации о погоде',
            description='Введите адрес в формате: <Название города>, <Название улицы>, <Дом>'
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
        )
}