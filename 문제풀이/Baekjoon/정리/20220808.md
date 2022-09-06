# ✍️ 문제풀이

[2798 블랙잭](#2798-블랙잭)

[2309 일곱 난쟁이](#2309-일곱-난쟁이)

[1436 영화감독 숌](#1436-영화감독-숌)

[1543 문서 검색](#1543-문서-검색)







## 백준 풀이



### 2798 블랙잭

```python
N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_num = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            # 3중문으로 한번씩 더해준다
            num = cards[i] + cards[j] + cards[k]

            # M보다 작을 경우는 계속 위의 공식을 진행한다
            if max_num < num <= M:
                # num이 max_num보다 크면 max_num은 num의 값이 된다
                max_num = num

print(max_num)
```




### 2309 일곱 난쟁이

```python
# 7명의 난쟁이 키의 합이 100이다
# 9명 중 2명을 빼야한다
# 9명의 키의 총 합은 140이다
# 즉 9명 중 2명을 해야하고, 40을 빼야한다
# 2명의 합이 40일 때, 그 둘을 찾아서 뺀다

# 9 난쟁이들의 키
H = []

# 주어진 입력 값들을 H 리스트 변수에 저장
for h in range(9):
    height = int(input())
    H.append(height)
    
total = sum(H)

# 2명을 찾는 것
# 즉 9명의 합이 빼야할 2명의 합에 100이 된다면
# 빼야할 2명을 구하고
# 그 2명을 H 리스트에서 빼낸다
for i in range(len(H) - 1):
    for j in range(i + 1, len(H)):
        rm = H[i] + H[j]
        if total - rm == 100:
            H.remove(H[j])
            # 앞에서부터 빼버리면, 뒤에 인덱스가 한칸씩 땡겨진다
            H.remove(H[i])
        if len(H) == 7:
        # 앞에서 두명을 빼고, 7명을 구했기 때문에
        # 7명이 나오면 for문을 끝내는 조건문을 넣는다
            result = sorted(H)
            break

for i in result:            
    print(i)
```



### 1436 영화감독 숌

```python
# 666이 적어도 6이 3개 이상

N = int(input())

num = 665
cnt = 0

while cnt != N:
    # num에 cnt가 N이랑 같아질 때까지, 1을 누적시킨다
    num += 1
    nums = str(num)

    # 666이 연속으로 있으면, cnt에 1을 누적시킨다
    if '666' in nums:
        cnt += 1

# 최종 숫자를 출력하는 것이라서, num을 출력
print(num)
```

- 666이 숫자에 3개 이상이 있어야 하는게 매인 포인트
- while문을 이용해서 665부터 1씩 증가하면서 비교한다
- 만약 666이 연속으로 3개 이상이 있을 시 cnt에 1을 누적시킨다
  - cnt가 입력한 숫자와 같아지면 while문은 끝나는 것이고
  - cnt와 N번이 같아질 때의 숫자가 정답이 된다



### 1543 문서 검색

```python
N = input()
M = input()

# N에 있는 입력값에, M이 몇개 있는지 숫자를 샌다
cnt = N.count(M)

print(cnt)
```



