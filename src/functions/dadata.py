import os
from telebot import TeleBot, types
from bot_func_abc import BotFunctionABC
import requests
import json
import re


class SuggestionDto:
    def __init__(self, payload: dict) -> None:
        data: dict[str, dict[str, str] | str] = payload.get('data')

        self.full_name: str = data.get('name').get('full')
        self.short_name: str = data.get('name').get('short')
        self.full_with_opf: str = data.get('name').get('full_with_opf')
        self.short_with_opf: str = data.get('name').get('short_with_opf')
        self.ogrn: str = data.get('ogrn')
        self.okpo: str = data.get('okpo')
        self.okato: str = data.get('okato')
        self.address: str = data.get('address').get('value')

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        payload: dict[str, str] = {
            'full_name': self.full_name,
            'short_name': self.short_name,
            'full_with_opf': self.full_with_opf,
            'short_with_opf': self.short_with_opf,
            'ogrn': self.ogrn,
            'okpo': self.okpo,
            'okato': self.okato,
            'address': self.address,
        }

        return json.dumps(payload, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


class DadataClientClass:

    def __init__(self, token: str | None = None) -> None:
        self.__token: str
        self.__base_url: str = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"

        if token is not None:
            self.__token = token

    @staticmethod
    def get_env_token() -> str:
        token = os.environ.get("DADATA_TOKEN")

        if not token or token is None or len(token) < 1:
            raise Exception("You must provide dadata token. Get it from https://dadata.ru/api/")

        return token

    def get_token(self) -> str:
        if self.__token:
            return self.__token

        self.__token = DadataClientClass.get_env_token()

        return self.__token

    def get_suggestions(self, inn: str) -> list[SuggestionDto]:
        payload = json.dumps({
            "query": inn
        })

        headers = {
            'Authorization': 'Token ' + self.get_token(),
            'Content-Type': 'application/json',
        }

        response = requests.request(method="POST", url=self.__base_url, headers=headers, data=payload)

        response_suggestions: list[dict] = json.loads(s=response.text).get('suggestions')

        try:
            to_return: list[SuggestionDto] = []

            for item in response_suggestions:
                to_return.append(SuggestionDto(item))

            return to_return
        except:
            print("Got exception")

        return []


class DadataFunctionClass(BotFunctionABC):
    def __init__(self):
        self.bot: TeleBot | None = None
        self.client = DadataClientClass()

    @staticmethod
    def get_inn_from_text(payload: str):
        regex = r"\/dadata\W+(\d+)"

        matches = re.finditer(regex, payload, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            inn = match.group(1)

            return inn

        return None

    @staticmethod
    def get_suggest_text(suggestion: SuggestionDto):
        return ("Полное наименование: <code>{name}</code>"
                "\nКраткое наименование: <code>{short_name}</code>"
                "\nАдрес: <code>{address}</code>"
                "\nОГРН: <code>{ogrn}</code>"
                "\nОКПО: <code>{okpo}</code>").format(
            name=suggestion.full_name,
            short_name=suggestion.short_name,
            address=suggestion.address,
            ogrn=suggestion.ogrn,
            okpo=suggestion.okpo
        )

    def set_handlers(self, bot: TeleBot, commands: list[str]):
        self.bot = bot

        @self.bot.message_handler(commands=commands)
        def welcome(message: types.Message):
            bot.reply_to(
                message=message,
                text="Приветствую в модуле Dadata. Напишите команду <code>/dadata 7707083893</code>, чтобы найти компанию по ИНН",
                parse_mode='HTML'
            )

        @self.bot.message_handler(func=lambda m: True)
        def get_all_messages(message: types.Message):
            inn = DadataFunctionClass.get_inn_from_text(message.text)

            if inn is not None:
                suggestions = self.client.get_suggestions(inn=inn)

                if len(suggestions) > 0:
                    bot.reply_to(
                        message=message,
                        text="Не удалось найти по ИНН <code>{inn}</code> никаких компаний".format(inn=inn),
                        parse_mode='HTML'
                    )
                elif len(suggestions) == 1:
                    text = DadataFunctionClass.get_suggest_text(suggestions[0])
                    bot.reply_to(
                        message=message,
                        text="Удалось найти одну компанию по ИНН <code>{inn}</code>\n\n{text}".format(inn=inn,
                                                                                                      text=text),
                        parse_mode='HTML'
                    )
                else:
                    bot.reply_to(
                        message=message,
                        text="Удалось найти {len} компанию по ИНН <code>{inn}</code>".format(inn=inn,
                                                                                             len=len(suggestions)),
                        parse_mode='HTML'
                    )

                    for item in suggestions:
                        bot.send_message(
                            chat_id=message.chat.id,
                            text=DadataFunctionClass.get_suggest_text(item),
                            parse_mode='HTML'
                        )


if __name__ == '__main__':
    client = DadataClientClass("d5f4a57f467f96970691d43e23fca9f49475f297")
    suggests = client.get_suggestions("7707083893")

    print(DadataFunctionClass.get_suggest_text(suggests[0]))
