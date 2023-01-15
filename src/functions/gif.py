import json
import requests

API = "https://api.giphy.com/v1/gifs/search"
api_key = "CXM2Bu2wkGTnWOc6zX9PnD3qjHJVfj4Q"
headers = {
    "api_key": api_key,
    "q": "",
    "limit": 1
}

def main(query):
    headers["q"] = query
    if (headers["q"] == ""):
        headers["q"] = "nothing"

    response = requests.get(API, headers).json()
    gif_url = response["data"][0]["images"]["original"]["url"]
    return gif_url
