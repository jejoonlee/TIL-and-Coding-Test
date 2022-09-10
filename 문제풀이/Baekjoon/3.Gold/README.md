# 🧑‍💻 Gold

## Category

[1655 가운데를 말해요](#1655-가운데를-말해요)



## 1655 가운데를 말해요

> heapq을 이용하는 문제
>
> 최대 힙과 최소 힙을 동시에 사용하는 문제다

```python
import sys
import heapq

# heap을 두개를 만든다
# 하나는 최대힙을 모으는 곳이고,
# 다른 하나는 최소 힙을 모으는 곳이다
    # 최대힙을 모으는 곳에서 제일 첫번째 숫자가 가운데 숫자가 된다!

N = int(sys.stdin.readline())

# 최대 힙 (중간 기준보다 작은 숫자들)
left = []
# 최소 힙 (중간 기준보다 큰 숫자들)
right = []

for _ in range(N):
    
    X = int(sys.stdin.readline())

    # left와 right가 개수가 같을 경우에는 left에 넣어준다
    # 최대 힙을 주기 위해서 X 값을 음수로 만든다
    if len(right) == len(left):
        heapq.heappush(left, -X)
    # 하지만 다를 경우 right에 숫자를 넣어준다
    else:
        heapq.heappush(right, X)

    # 만약에 숫자가 주어졌는데 left에 right에 있는 숫자보다 더 큰 숫자가 있을
    # 경우 if문을 만들어야 한다
    if len(right) != 0 and -left[0] > right[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)

        heapq.heappush(left, -r)
        heapq.heappush(right, -l)


    print(-left[0])
```

- 여기서 제일 중요한 것은 최대 힙을 저장할 리스트와, 최소 힙을 저장할 리스트를 각각 만드는 것
  - 최대 힙은 들어갈 값들이 중간값보다 작아야 하고
  - 최소 힙에 들어갈 값들은 중간값보다 커야 한다
- 파이썬의 heapq은 기본적으로 `최소 힙` 이다.
  - 최대 힙으로 만드려면, 입력된 값을 음수로 만들어야 한다
    - 단!!!! 출력을 할 때에는 양수로 다시 바꾸기!!!
- **답은 최대 힙에 들어가는 값들 중 제일 첫번째 값이 답이 된다**
