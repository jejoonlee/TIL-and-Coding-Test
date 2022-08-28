# 20220816 ~ 20220821



## 집합과 맵



### 10815 숫자 카드

상근이가 가지고 있는 카드와 주어진 카드들을 비교

주어진 카드 중 상근이가 해당 카드가 있으면, `1` 없으면 `0` 을 출력

리스트로 이중 for문을 사용하면 시간 초과

그래서 딕셔너리로 해결 / 딕셔너리로 풀이를 하는 것이 더 빠르다

```python
N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

result = {}
for i in range(N):
    result[cards[i]] = 0

for j in range(M):
    if check[j] in result:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
```

- result 딕셔너리에 상근이가 가지고 있는 카드를 key로 저장
- 주어진 카드들을 순회하면서 상근이가 카드를 가지고 있으면 `1`을 출력, 아니면 `0`을 출력