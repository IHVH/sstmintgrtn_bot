# systemIntegrationBot

The Telegram bot is designed to master the practical skills of integrating information systems and gain experience in working together on a project in a distributed team.

Link to get acquainted with the capabilities of the used library [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

__Test telegram bot__ - [@sstmintgrtn_bot](https://t.me/sstmintgrtn_bot)

__To test the discord bot, you can join the group__ - [Discord group](https://discord.gg/apKWWMbUuG)

To run locally, add an `.env` file with your keys to the root of the project. Or add appropriate values to the environment variables of your operating system.
```
TBOTTOKEN=
DBOTTOKEN=
EXAMPLETOKEN=example
GITHUBTOKEN=
YAWEATHERTOKEN=
YADICTTOKEN=
KP_TOKEN=
OPENWEATHERTOKEN=
DADATA_TOKEN=
```
The prefix for the discord bot is permanently ` ! ` set to `cfx.json`


## Tokens
Links to information about tokens

[TBOTTOKEN](https://core.telegram.org/bots#how-do-i-create-a-bot)

[DBOTTOKEN](https://discord.com/developers/applications)

[GITHUBTOKEN](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

[YAWEATHERTOKEN](https://yandex.ru/dev/weather/doc/dg/concepts/about.html#about__onboarding) - Test plan required

[YADICTTOKEN](https://yandex.ru/dev/dictionary/keys/get/?service=dict)

[KP_TOKEN](https://kinopoiskapiunofficial.tech)

[DADATA_TOKEN](https://dadata.ru/profile/#info)


## Adding telegram bot functions.

Dear students, when implementing your functions, adhere to the following recommendations.
Your code should be placed in a separate file in the **src/functions/** directory.
The code must be organized in a class that inherits from the abstract class **BotFunctionABC**
For an example, take a look at the file **[example_bot_function.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/functions/example_bot_function.py)**
Then in the file **[bot_func_dictionary.py](https://github.com/IHVH/OEMIB_PI01_19_TBOT/blob/main/src/bot_func_dictionary.py)**
you need to add information about your function to the **BOT_FUNCTIONS_2** dictionary by filling in the appropriate fields

- bot_function - an object with your function inherited from BotFunctionABC
- commands - list of commands to call your function
- authors - your login on github.com
- about - short description
- description - a detailed description of the function with a description of the parameters if they are needed