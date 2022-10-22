import os
import requests

URL = "https://api.github.com/repos/IHVH/OEMIB_PI01_19_TBOT/"

def headers():
    githubtoken = os.environ["GITHUBTOKEN"]
    return  {"Accept":"application/vnd.github+json", 
    "Authorization": f'Bearer {githubtoken}'}

def params(message):
    str_spilt = message.text.split()
    x = str_spilt[-1]
    pp = 1
    if(x.isdigit()):
        pp = x
    return {"per_page": f'{pp}'}

def url_commits():
    return URL + "commits" 

def do_work(response, bot, chat_id):
    if(response):
        commits = response.json()
        for cmt in commits:
            msg = cmt["commit"]["message"]
            url = cmt["html_url"]
            name = cmt["commit"]["committer"]["name"]
            date = cmt["commit"]["committer"]["date"]
            send_msg = f'{name} - {msg} - {date} - {url}'
            bot.send_message(text=send_msg, chat_id=chat_id)
    else:
        bot.send_message(text=f'Ошибка - {response.status_code}', chat_id=chat_id)

def get_commits(message, bot):
    response = requests.get(url_commits(), headers=headers(), params=params(message))
    do_work(response, bot, message.chat.id)
