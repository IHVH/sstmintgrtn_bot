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
        'graw': BotFunction(
        commands=['grav', 'gravatar'], 
            authors=['BBP'], 
            description='Тестирование функционала gravatar', 
            about='как аргумент принимает email'
        ),
}