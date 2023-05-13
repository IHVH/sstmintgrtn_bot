Необходимо в общий проект [OEMIB_PI01_19_TBOT](https://github.com/IHVH/OEMIB_PI01_19_TBOT)
добавить свою функцию которая используя какие либо из изученных технологий 
реализует взаимодействие с внешней системой. Необходимо использовать только общедоступные api. 
Функция должна выполнять какое то осмысленное (желательно полезное) действие. 

Для этого в вашем аккаунте на github.com делаете fork репозитария 
Добавляете вашу функцию отдельным фалом в папку `/src/functions/ `
Весь код функции должен быть внутри класса унаследованного от абстрактного класса BotFunctionABC
В репозитории есть пример `example_bot_function.py`  как организовать наследование и код внутри класса 
[example_bot_function.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/functions/example_bot_function.py)
Затем в фале `bot_func_dictionary.py` необходимо добавить информацию о вашей функции в словарь `BOT_FUNCTIONS_2`
[bot_func_dictionary.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/bot_func_dictionary.py)
Если необходимы какие-то токены или другие аутентификационные данные то добавляете информацию о них в файл `README.md`
[README.md](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/README.md)
Протестировав всё локально отправляете Pull request в основной репозиторий.

Вопросы можно задавать, обсуждать в общем телеграм чате [sstmintgrtn](https://t.me/sstmintgrtn).
Список общедоступных api можно посмотреть в [project](https://github.com/users/IHVH/projects/1) 
либо найти подходящий в репозитории [public-apis](https://github.com/IHVH/public-apis) 