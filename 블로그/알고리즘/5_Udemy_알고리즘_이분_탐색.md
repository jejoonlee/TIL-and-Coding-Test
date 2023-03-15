# Udemy : 알고리즘 이분 탐색

*udemy 알고리즘 코딩 테스트*



## 이분 탐색

![img](https://blog.kakaocdn.net/dn/FzF4h/btrWIP861l1/YNTPdtd9kdghl9kzk1OZSK/img.png)

- 하나 하나 다 찾는 것이 아닌다 (완전 탐색으로 매우 오래 걸린다)
- **Up & Down 게임이라고 생각하면 된다**
  - 정답을 기준으로, 무작위로 고른 숫자가 정답 숫자가 무작위로 고른 숫자 기준으로 더 작은지, 또는 큰지 말해주는 것이다
  - 예) 정답 7
    - 10을 말하면 Down
    - 5를 말하면 Up
- 즉 값들을 정렬하고, 정렬한 값들 중에 중간 값을 기준으로 탐색을 하는 것이다
  - 예) 1,2,3,4,5,6,7,8,9,10 중 8 찾기
    - 먼저 5를 탐색한다, 7은 5보다 크기 때문에 6~10 중 숫자들을 찾는다
    - 6~10 의 중간값은 8



```python
from bisect import bisect_left, bisect_right

array = [0, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 9]

print(bisect_left(array, 4))
# 출력 : 6

print(bisect_right(array,5))
# 출력 : 8

print(bisect_right(array, 7) - bisect_left(array, 7))
# 7의 개수를 찾을 수 있다
# 출력 : 4
```



#### bisect_left(list, value)

- value보다 크거나 같은 첫 번째 값의 인덱스를 출력해준다



#### bisect_right(list, value)

- value보다 큰 값들 중에, 제일 먼저 나오는 값의 인덱스를 출력한다





#### 백준 10815

-  **bisect_right(my_card, i) - bisect_left(my_card, i) > 0**
  - bisect_right(my_card, i) - bisect_left(my_card, i) 이, 0보다 크다면, **my_card**에 있는 숫자가 card에 있는 것이다

```python
from bisect import bisect_left, bisect_right

N = int(input())
my_card = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

i, j = 0, 0

my_card.sort()

result = []

for i in card:
    if bisect_right(my_card, i) - bisect_left(my_card, i) > 0:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))
```







## 파라메트릭 서치 

> #### 최적화 문제를 결정 문제로 바꿔서 이진 탐색으로 푼다
