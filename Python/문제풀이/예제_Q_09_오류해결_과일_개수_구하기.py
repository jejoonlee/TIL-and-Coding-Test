# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1     
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# dict (fruit_count)에 key를 넣으려면 fruit_count[fruit] = 1을 해야한다
# 여기서 fruit는 과일 리스트들 중 하나씩 꺼내 key로 만들고
# 그 key의 초기값을 1로 만들어 준다

# 만약, fruit_count 안에 과일이 중복이 되면 else문으로 가서, 해당 과일의
# value는 1을 더한다