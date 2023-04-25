import telebot
import requests
from typing import List
from bot_func_abc import BotFunctionABC


class RandomDogAPIFunction(BotFunctionABC):
    def __init__(self):
        self.random_dog_data = "random_dog_breed"
        self.breed_list_data = "dog_breed_list"
        self.breed_dict = {}
        self.breed_data_prefix = "dog_breed:"

    def set_handlers(self, bot: telebot.TeleBot, commands: List[str]):
        self.bot = bot

        @bot.callback_query_handler(func=lambda call: call.data.startswith(self.breed_data_prefix) or call.data == self.random_dog_data)
        def callback_handler(call):
            chat_id = call.message.chat.id
            data = call.data

            if data.startswith(self.breed_data_prefix):
                breed = data[len(self.breed_data_prefix):]
                if chat_id in self.breed_dict and self.breed_dict[chat_id] != breed:
                    return

                self.breed_dict[chat_id] = breed
                self.send_dog_photo(chat_id, breed)
            elif data == self.random_dog_data:
                # breed = self.breed_dict.get(chat_id)
                self.send_random_dog_photo(chat_id)
                # if breed:
                #     del self.breed_dict[chat_id]
                #     self.send_dog_photo(chat_id, breed)
                # else:
                #     self.send_random_dog_photo(chat_id)

        @bot.message_handler(commands=commands)
        def random_dog_handler(message):
            chat_id = message.chat.id

            if message.text.startswith('/d'):
                breed = ""
                if len(message.text.split()) > 1:
                    breed = message.text.split()[1].lower()

                if breed:
                    response = requests.get(
                        f"https://dog.ceo/api/breed/{breed}/images/random")
                    url = response.json()["message"]
                else:
                    response = requests.get(
                        "https://dog.ceo/api/breeds/image/random")
                    url = response.json()["message"]

                markup = self.get_buttons_markup(breed)
                bot.send_photo(chat_id=chat_id, photo=url, reply_markup=markup)

            elif message.text.startswith('/breeds'):
                response = requests.get("https://dog.ceo/api/breeds/list/all")
                breeds = response.json()["message"]
                text = "list of all available dog breeds:\n\n" + \
                    "\n".join(breeds)
                bot.send_message(chat_id, text)

    def get_buttons_markup(self, breed: str) -> telebot.types.InlineKeyboardMarkup:
        markup = telebot.types.InlineKeyboardMarkup()

        if breed:
            markup.add(
                telebot.types.InlineKeyboardButton(
                    text="🐾 get random breed",
                    callback_data=self.random_dog_data
                ),
                telebot.types.InlineKeyboardButton(
                    text=f"🐶 get {breed.lower()}",
                    callback_data=f"{self.breed_data_prefix}{breed.lower()}"
                )

            )
        else:
            markup.add(
                telebot.types.InlineKeyboardButton(
                    text="🐾get random breed",
                    callback_data=self.random_dog_data
                ),
            )

        return markup

    def send_random_dog_photo(self, chat_id: int):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        url = response.json()["message"]
        markup = self.get_buttons_markup("")
        self.bot.send_photo(chat_id=chat_id, photo=url, reply_markup=markup)

    def send_dog_photo(self, chat_id: int, breed: str):
        response = requests.get(
            f"https://dog.ceo/api/breed/{breed}/images/random")
        url = response.json()["message"]
        markup = self.get_buttons_markup(breed)
        self.bot.send_photo(chat_id=chat_id, photo=url, reply_markup=markup)
