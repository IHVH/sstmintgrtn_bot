import requests

url = "https://evilinsult.com/generate_insult.php?lang=ru&type=json"

def insult_generator():
    Data = requests.get(url)
    json_Data = Data.json()
    insult = json_Data["insult"]
    return insult
