import os
import requests
import telebot
from bot_command_dictionary import BOT_FUNCTIONS

class Github:
    URL = "https://api.github.com/repos/IHVH/OEMIB_PI01_19_TBOT/"
    
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot 

        @bot.message_handler(commands=BOT_FUNCTIONS['issues'].commands)
        def hendler(message):
            self.get_issues(message)

    def get_issues(self, message):
        print(message.text)
        self.bot.send_message(text=f'TEST - {message.text}', chat_id=message.chat.id)
        params = Github.params_per_page(message)
        params["state"] = "all"
        #response = requests.get(self.url_issues(), headers=self.headers(), params=params)
        #self.do_work_on_issues(response, bot, message.chat.id)

    def headers():
        githubtoken = os.environ["GITHUBTOKEN"]
        return  {"Accept":"application/vnd.github+json", 
        "Authorization": f'Bearer {githubtoken}'}

    def params_per_page(message):
        str_spilt = message.text.split()
        x = str_spilt[-1]
        pp = 1
        if(x.isdigit()):
            pp = x
        return {"per_page": f'{pp}'}

    def url_commits(self):
        return self.URL + "commits" 

    def url_issues(self):
        return self.URL + "issues"

    def do_work_on_commits(response, bot, chat_id):
        if(response):
            commits = response.json()
            for cmt in commits:
                msg = cmt["commit"]["message"]
                url = cmt["html_url"]
                name = cmt["commit"]["committer"]["name"]
                date = cmt["commit"]["committer"]["date"]
                send_msg = f'{name} - {msg} \n {date} \n {url}'
                bot.send_message(text=send_msg, chat_id=chat_id)
        else:
            bot.send_message(text=f'Ошибка - {response.status_code}', chat_id=chat_id)

    def do_work_on_issues(response, bot, chat_id):
        if(response):
            issues = response.json()
            for iss in issues:
                login = iss["user"]["login"]
                state = iss["state"]
                title = iss["title"]
                body = iss["body"]
                url = iss["html_url"]
                send_msg = f'{state} - {login} \n {title} \n {body} \n {url}'
                bot.send_message(text=send_msg, chat_id=chat_id)
        else: 
            bot.send_message(text=f'Ошибка - {response.status_code}', chat_id=chat_id)

    def get_commits(self, message, bot):
        response = requests.get(self.url_commits(), headers=self.headers(), params=self.params_per_page(message))
        self.do_work_on_commits(response, bot, message.chat.id)








