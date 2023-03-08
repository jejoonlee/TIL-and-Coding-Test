# Udemy : 알고리즘 완전탐색

*udemy 알고리즘 코딩 테스트*



## 완전탐색

> #### 존재하는 모든 경우의 수를 탐색을 하며 결과를 도출해 낸다



#### 장점

- 모든 경우의 수를 탐색하는 것이라서 반드시 답을 찾을 수 있다



#### 단점

- 모든 경우의 수를 탐색하는 것이라서, 계산하는 시간이 느리다



## 브루트포스

> #### 완전 탐색 방법론을 사용하는 알고리즘이다
>
> #### 무차별 대입이라고도 한다



#### 시간이 오래 걸려도, 답을 구할 수 있는 방법이라서, 많이 사용이 된다



## 순열 itertools

`from itertools import permutations`

`from itertools import combinations`

- 모든 경우의 수를 순서대로 살펴볼 때 용이하다



```python
from itertools import permutations

v = [0, 1, 2, 3]

for i in permutations(v, 4):
    print(i)
    
# 0 1 2 3
# 0 1 3 2
# 0 2 1 3
# ...
# 3 2 0 1
# 3 2 1 0
```



#### permutations(list, num)

- list : 배열의 이름
- num : 몇 개의 수를 뽑을지 전달한다

```python
from itertools import permutations

array = ["A", "B", "C"]

for a in permutations(array, 2):
    print(a)
    
# 여기서 ("A", "B")와 ("B", "A")은 다르게 취급한다
# ("A", "B") ("A", "C") ("B", "A") ("B", "C") ("C", "A") ("C", "B")가 출력된다
```





#### combinations(list, num)

- 같은 조합은 하나로 취급한다

```python
from itertools import combinations

array = ["A", "B", "C"]

for a in combinations(array, 2):
    print(a)
    
# 여기서 ("A", "B")와 ("B", "A")는 같은 값이다
# 즉 ("A", "B") ("A", "C") ("B", "C") 가 출력된다
```





