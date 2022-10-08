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
    'test1': BotFunction(
            commands=['test1', 'test2'], 
            authors=['IHVH'], 
            about='TEST Func',
            description='Тестовая функция!' 
        ),
}