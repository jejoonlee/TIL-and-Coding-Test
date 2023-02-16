from bs4 import BeautifulSoup
import requests
import os
import dotenv
import csv

dotenv.load_dotenv()


# response = requests.get(f"https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=503616199")
# response.raise_for_status()
# website = response.text

# print(website)

# soup = BeautifulSoup(website, "html.parser")

# musics = soup.select(selector=".title a")
# artists = soup.select(selector=".artist a")

# music_list = []
# artist_list = []


music_list = []
artist_list = []

with open("music.csv", encoding="UTF8") as file:
    file_data = csv.reader(file)

    for data in file_data:
        music_list.append(data[0])
        artist_list.append(data[1])

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("id"),
        client_secret=os.getenv("secret"),
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt",
    )
)

# 음악 이름 검색을 통해서 스포티파이의 URI 가져오
track_uri = []

for i in range(96):
    result = sp.search(q=f"track: {music_list[i]} artist: {artist_list[i]}", type="track")
    try:
        track = result["tracks"]["items"][0]["uri"]
        track_uri.append(track)
    except:
        pass


# 현재 유저 id 가지고 오기
user_id = sp.current_user()["id"]

# playlist = sp.user_playlist(user_id)
# print(playlist)

# 스포티파이의 플레이 리스트 생성
playlist = sp.user_playlist_create(user_id, name="송민호", public=False)

# 플래이 리스트에 음악 넣기
# 플래이 리스트는 uri 형태로되어 저장되어있는 리스트를 넣을 수 있다
sp.user_playlist_add_tracks(user_id, playlist["id"], track_uri)
