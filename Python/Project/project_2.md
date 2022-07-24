# 📋 Project 1

[00. API 문서와 requests 활용 (연습)](#00-api-문서와-requests-활용-연습)

[01. 인기 영화 조회](#01-인기-영화-조회)

[02. 특정 조건에 맞는 인기 영화 조회](#02-특정-조건에-맞는-인기-영화-조회)

[03. 특정 조건에 맞는 인기 영화 조회](#03-특정-조건에-맞는-인기-영화-조회)

[04. 영화 조회 및 추천 영화 조회](#04-영화-조회-및-추천-영화-조회)

[05. 출연진 및 연출진 데이터 조회](#05-출연진-및-연출진-데이터-조회)





## ✔️ 파이썬 기반 데이터 활용

### 목표

- Python 기본 문법(조건문, 반복문) 활용
- Python 외부 라이브러리 활용
- API와 JSON 데이터의 활용



#### TMDB 활용 https://www.themoviedb.org/settings/api





## 00. API 문서와 requests 활용 (연습)

- 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력
- https://apidocs.bithumb.com/reference/현재가-정보-조회

```python
# pip install requests 
import requests
# URL로
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)

# print(response.json())  response를 json으로 열기

data = response.json()
print(data.get('data').get('prev_closing_price'))
```

- `.get` 은 딕셔너리에 있는 key의 value를 가지고 오는 것



## 01. 인기 영화 조회

```python
import requests

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params ={
    'api_key': '652241f716c0f8b8f5006465a644f600',
    'language': 'en-en'
}
# popular는 TMDB에서 있는 영화 중 유명한 영화를 JSON 형태로 가지고 온 것
response = requests.get(Base_URL+path, params = params).json()

def popular_count():
    pass
    mov_list = []                           # list를 만들어준다
    results = response.get('results')       # 1. Page와 Results라는 key 2개가 먼저 있는데, Results를 꺼내온다
    for r in results:                       # 2. results는 리스트이라서, 딕셔너리로 타입 변환을 해준다
        movies = r.get('original_title')    # 3. 딕셔너리에 있는 key들 중 'original_title'을 가지고 온다
        mov_list.append(movies)             # 4. 영화 제목들을 만들어 놓은 리스트에 넣어 둔다
    return len(mov_list)                    # 5. 리스트의 길이를 구하면, 그것이 유명한 영화 개수이다


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
print(popular_count())
```

- base_URL는 기본 URL이다. 나중에 `path`가 2개 이상일 때에, 계속 사용할 수 있다.
- JSON 형태를 가지고 올때, 리스트 안에 딕셔너리가 있는지 확인 (리스트 안에 있으면, 딕셔너리를 리스트 밖으로 꺼내야 한다)





## 02. 특정 조건에 맞는 인기 영화 조회

```python
import requests
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
  'api_key': '652241f716c0f8b8f5006465a644f600',
  'language': 'en-en'
}

response = requests.get(Base_URL+path, params = params).json()


def vote_average_movies():
    pass 
    l = []
    result = response.get('results')
    for i in result:
      if i['vote_average'] >= 8:
        l.append(i)
    
    return(l)

pprint(vote_average_movies())
```

- `ㅣ=[]` 은 리스트 만드는 것
- `result = response.get('results')` 는 `response` 라는 리스트 안에 `results`라는 리스트를 가지고 오는 것

```python
for i in result:
  if i['vote_average'] >= 8:
    l.append(i)
```

- `i` 는 `result` 안에 있는 딕셔너리들을 하나씩 반환하는 것
- 그 중 `i['vote_average']` 를 통해 `i`의 key 중 `'vote_average'`라는 키의 값을 가지고 온다
- 그 후 값이 8 이상이면 `l` 리스트에 넣은다

```python
response = requests.get(Base_URL+path, params = params).json().get('results')
# .get('results')를 써서 'results'라는 리스트를 반환한다

def vote_average_movies():
# 위에 'result'가 'response'로 바뀐다
    l = []
    for i in response:
      if i['vote_average'] >= 8:
        l.append(i)
    
    return(l)

pprint(vote_average_movies())
```





## 03. 특정 조건에 맞는 인기 영화 조회

```python
import requests
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '652241f716c0f8b8f5006465a644f600',
    'language': 'en-en'
}

response = requests.get(Base_URL+path, params = params).json().get('results')

def ranking():
    ranking = []
    for i in response:
      ranking.append(i)
      rank = sorted(ranking, key = lambda r: r['vote_average'], reverse = True)
    return rank[0:5]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
```

- response는 최근 인기 많은 영화들의 정보이다.
- 그 정보들을 `sorted` 통해 나열한 후, [0:5]를 해서 평점이 좋은 5개의 영화들을 반환 한다



**`rank = sorted(ranking, key = lambda r: r['vote_average'], reverse = True)`**

- rank == 변수
- sorted == 낮은 수 부터 정렬하는 변수 (오름차순)
- `ranking`을 정렬하고, `reverse = True` 는 반대로 정렬을 한다
- `key = lambda r: r['vote_average']`
  - lambda라는 이름 없는 함수를 만든다
  - key 인자에 함수를 넘겨주면 우선순위가 정해진다
  - 이 코드에 경우 `['vote_average']`의 숫자들을 비교해서 순서를 정해준다



**`rank = sorted(ranking, key = lambda r: -r['vote_average'])`**

- `reverse = True` 대신 `key = lambda r: -r['vote_average']` 처럼 `r`을 `-r` 로 바꾸면 내림차순으로 바뀐다



## 04. 영화 조회 및 추천 영화 조회

```python
import requests
from pprint import pprint

def recommendation(title):
    base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'

    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query': f'{title}'      
        # query가 필수이고, title을 넣으면 영화 제목을 검색할 수 있다
        # recommendation(title) 함수를 만든 후 괄호 안에 영화 제목을 입력하면 된다
    }
    
    # 마지막에 .get('results')라고 하는 것은, response 자체가 현재 List이기 때문이다
    # List에 있는 dict 중 'result' dictionary를 가져오는 것
    response = requests.get(base_URL + path, params = params).json().get('results')

    # response에 아무것도 없으면 None을 반환한다
    if len(response) == 0:
        return None
    # response는 리스트, 첫번째 리스트 element 중 'id'라는 key의 value를 가져온다
    else:
        id = response[0]['id']

    # f-string을 안 쓰면 위에서 찾은 id와 연결이 안 된다
    path = f'/movie/{id}/recommendations'

    response = requests.get(base_URL + path, params = params).json().get('results')

    result = []
    for i in response:
        result.append(i['title'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
#     """
#     제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
#     추천 영화가 없을 경우 []를 반환
#     영화 id 검색에 실패할 경우 None을 반환
#     (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
#     """
    pprint(recommendation('기생충'))
#     # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
#     # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
```

- **path** 안에 넣는 정보가, 그 전에 찾은 정보와 일치하는지 확인하면서 진행!!!



## 05. 출연진 및 연출진 데이터 조회

```python
import requests
from pprint import pprint


def credits(title):

    # 영화 제목을 통해 영화 ID 가져오기
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query' : title
    }

    response = requests.get(base_url + path, params = params).json().get('results')

    if len(response) == 0:
        return None
    else:
        id = response[0]['id']

    # 여기서부터는 영화 credits 관련
    path = f'/movie/{id}/credits'
    
    response = requests.get(base_url + path, params = params).json()
    
    # response_cast (타입: 리스트)를 'i' 딕셔너리로 만든 후,
    # 딕셔너리 안에 있는 key 중 'cast_id'의 value를 찾고
    # 그 value가 10미만이면
    # 'cast', 리스트 변수 안에 배우 이름 'name' 들을 넣은다.
    cast = []
    response_cast = response.get('cast')

    for i in response_cast:
        if i['cast_id'] < 10:
            cast.append(i['name'])
    
    # response_crew (타입: 리스트)를 'i' 딕셔너리로 만든 후,
    # 딕셔너리 안에 있는 key 중 'department'의 value를 찾고
    # 문자열이 ('Directing') 동일하면 
    # 'crew', 리스트 변수 안에 연출진 이름 'name' 들을 넣은다.
    crew = []
    response_crew = response.get('crew')
    for i in response_crew:
        if i['department'] == 'Directing':
            crew.append(i['name'])

    return {
        'cast': cast,
        'crew': crew
    }


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None

```

