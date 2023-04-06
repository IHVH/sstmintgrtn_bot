import time
import requests
import json
import os

def get_kinopoisk_token():
    if "KP_TOKEN" in os.environ:
        return os.environ["KP_TOKEN"]
    return None
#KINOPOISK = #os.environ["KP_TOKEN"]
API = 'https://kinopoiskapiunofficial.tech/api/v2.1/'
headers = {"X-API-KEY": get_kinopoisk_token()}

class SEARCH:
    def __init__(self, data: dict):
        self.kp_id = data['filmId']
        self.name = data['nameRu'] if data['nameEn'] == '' else data['nameEn']
        self.ru_name = data['nameRu']
        self.year = data['year'].split('-')[0]
        self.duration = data['filmLength']
        self.genres = [genre['genre'] for genre in data['genres']]
        self.countries = [country['country'] for country in data['countries']]
        self.kp_rate = data['rating']
        self.kp_url = f'https://www.kinopoisk.ru/film/{data["filmId"]}/'
        self.poster = data['posterUrl']
        self.poster_preview = data['posterUrlPreview']


def main(query):

    response = requests.get(API + 'films/search-by-keyword', headers=headers,
                                       params={"keyword": query, "page": 1})

    if(response.status_code != 200):
        print(response.text)
        return None

    request_json = response.json()
    output = []
    for film in request_json['films']:
        try:
            if len(output) == 4:
                return output
            output.append(SEARCH(film))
        except json.decoder.JSONDecodeError:
            time.sleep(0.5)
        except Exception:
            continue

    return output
