from bot_command_dictionary import BOT_FUNCTIONS

def get_start_message_from_bot_function_dictionary():
    result = 'Привет! \nВот список функций:'
    result += f'\n \n'
    for key in BOT_FUNCTIONS:
        result += f'{BOT_FUNCTIONS[key].about} \n    - /'
        result += "\n    - /".join(BOT_FUNCTIONS[key].commands)
        result += f'\n{BOT_FUNCTIONS[key].description} '
        result += f'\nНад функцией работают: \n    - https://github.com/'
        result += "\n    - https://github.com/".join(BOT_FUNCTIONS[key].authors)
        result += f'\n ------------------------------------------------------------ \n'
    
    return result