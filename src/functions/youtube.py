import os
from bot_func_abc import BotFunctionABC
import requests
import json


class YoutubeFinder(BotFunctionABC):
    def YTFinder(self):
        api_key = os.environ["YTFINDERTOKEN"]
        word = self.strip("/YTfind").lower()
        query = word
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={query}&key={api_key}'
        response = requests.get(url)
        data = json.loads(response.text)

        for item in data['items']:
            result = f"Название видео: {item['snippet']['title']}"
            return result
