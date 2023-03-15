import os
from lyricsgenius import Genius

def get_lyrics(query):
	temp = query.split('-')
	if len(temp) != 2:
		return "Напиши запрос в формате /genius исполнитель - трек"
	genius = Genius(os.environ["GENIUS_TOKEN"])
	song = genius.search_song(temp[0].strip(), temp[1].strip())
	if song is None:
		return "К сожалению, я не смог найти нужный трек"
	else:
		return (song.lyrics)