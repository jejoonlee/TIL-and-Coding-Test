from bs4 import BeautifulSoup
import requests
import os
import dotenv

dotenv.load_dotenv()


date = "20100217"
# input("Which year do you want to travel to? Type the date in this format YYYYMMDD: \n")

response = requests.get(
    f"https://www.officialcharts.com/charts/singles-chart/20140216/7501/"
)
response.raise_for_status()
website = response.text

soup = BeautifulSoup(website, "html.parser")

musics = soup.select(selector=".title a")
artists = soup.select(selector=".artist a")

music_list = [music.getText() for music in musics]
artist_list = [artist.getText() for artist in artists]

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

for music in musics:
    result = sp.search(q=f"track: {music} year: {date[0:5]}", type="track")
    try:
        track = result["tracks"]["items"][0]["uri"]
        track_uri.append(track)
    except:
        pass

# 현재 유저 id 가지고 오기
user_id = sp.current_user()["id"]

# 스포티파이의 플레이 리스트 생성
playlist = sp.user_playlist_create(user_id, name=f"{date} top 100", public=False)

# 플래이 리스트에 음악 넣기
# 플래이 리스트는 uri 형태로되어 저장되어있는 리스트를 넣을 수 있다
sp.user_playlist_add_tracks(user_id, playlist["id"], track_uri)
