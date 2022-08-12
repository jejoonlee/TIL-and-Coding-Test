
import sys

sys.stdin = open("_퍼펙트셔플.txt")

from collections import deque

T = int(input())

for t in range(1, T + 1):
    # 카드 개수
    N = int(input())

    # 카드 종류
    cards = list(input().split())

    # 반으로 가르기 위해
    num = N // 2

    # 임시적으로 넣어줄 리스트 생성
    temp = []
    for _ in range(num):
        p = cards.pop()
        temp.append(p)

    cards = deque(cards)

    # 결과 값을 넣어줄 리스트
    result = []
    while len(cards) != 0:
        card = cards.popleft()
        result.append(card)
        
        if len(temp) != 0:
            tem = temp.pop()
            result.append(tem)
        else:
            break

    result = ' '.join(result)
    print(f'#{t} {result}')