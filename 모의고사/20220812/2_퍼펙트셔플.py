
import sys

sys.stdin = open("_퍼펙트셔플.txt")

# from collections import deque

# T = int(input())

# for t in range(1, T + 1):
#     # 카드 개수
#     N = int(input())

#     # 카드 종류
#     cards = list(input().split())

#     # 반으로 가르기 위해
#     num = N // 2

#     # 임시적으로 넣어줄 리스트 생성
#     temp = []
#     for _ in range(num):
#         p = cards.pop()
#         temp.append(p)

#     cards = deque(cards)

#     # 결과 값을 넣어줄 리스트
#     result = []
#     while len(cards) != 0:
#         card = cards.popleft()
#         result.append(card)
        
#         if len(temp) != 0:
#             tem = temp.pop()
#             result.append(tem)
#         else:
#             break

#     result = ' '.join(result)
#     print(f'#{t} {result}')


### 리스트만 사용해서 풀이하기
# 인덱스 계산으로 해결하기

# 카드 N개를 2로 나눈다
# 그리고 N개를 2로 나눈 수를 각 인덱스와 더해준다
# 앞에 있는 카드들은 더하기를 통해 결과 값에 배치가 되고
# 뒤에 있는 카드들은 빼기를 통해 결과 값에 배치가 된다

# 예)
# 인덱스: 0, 1, 2, 3, 4
# 리스트: [A, B, C, D, E]

# 결과 인덱스: 0, 1, 2, 3, 4
# 결과 리스트: [A, D, B, E, C]

# A는 +0 / B는 +1 / C는 +2 --> 인덱스에 인덱스를 더한다
# D는 -2 / E는 -1

import math

T = int(input())

for t in range(1, T + 1):
    # 카드 개수
    N = int(input())

    # 카드 종류
    cards = list(input().split())
    
    # 결과 값들을 넣은다
    result = [0] * N

    num = math.ceil(N / 2) - 1

    cnt = num
    for i in range(len(cards)):
        if i <= num:
            result[i + i] = cards[i]
        else:
            result[i - cnt] = cards[i]
            cnt -= 1
    
    result = ' '.join(result)
    print(f'#{t} {result}')