# ✍️ 문제풀이

[후기](#후기)

[1652 누울 자리 찾아라](#1652-누울-자리-찾아라)

[5533 유니크](#5533-유니크)





## 후기

>
>



## 백준 풀이



### 1652 누울 자리 찾아라

```python
# 완전 혼자서 할 때.
# vs 코드에서는 값이 같지만, 백준에서는 틀리다고 나온다

N = int(input())

room = [list(input()) for _ in range(N)]
# 입력값의 개수와 N의 숫자에 따라 행렬이 만들어진다

# 열 row 비교
r_result = []
for i in range(len(room)):
    space = 0
    row = []
    for j in range(N):
        if room[i][j] == '.':
        # '.'이 있을 때마다 space에 1을 더한다
            space += 1
        else:
        # '.'이 아닌 경우 row 리스트에 그냥 숫자를 넣은다
            row.append(space)
            space = 0
    row.append(space)
    # 열을 한번 돌때 '.'만 있을 수 있으니 리스트에 한번 더 space를 넣는다
    r_result.append(max(row))
    # 그리고 row에 숫자 중 제일 큰 수를 r_result에 넣는다

# 행도 위와 같이
c_result = []
for i in range(N):
    space = 0
    column = []
    for j in range(len(room)):
        if room[j][i] == '.':
            space += 1
        else:
            column.append(space)
            space = 0
    column.append(space)
    c_result.append(max(column))



# 마지막에는 만약에 result 리스트에 값들이
# 1보다 크면 final 변수에 1씩 누적시킨다
# 1보다 크다는 말은, 연속으로 공간이 있다는 것
r_final = 0
for i in r_result:
    if i > 1:
        r_final += 1

c_final = 0
for i in c_result:
    if i > 1:
        c_final += 1

print(r_final, c_final)

------------------------------------------------------------------
N = int(input())

room = [list(input()) for _ in range(N)]
# 입력값의 개수와 N의 숫자에 따라 행렬이 만들어진다

# 열과 행에 누울 수 있는 공간의 결과를 result에 넣어준다
result = [0, 0]
# 정사각형이기 때문에 똑같이 써도 됨
for i in range(N):
    row, column = 0, 0
    for j in range(N):
        if room[i][j] == '.': # 열 먼저
            row += 1
        else:
            row = 0
        if row == 2:    # 2개 연속으로 공간이 있으면
            result[0] += 1  # result에 바로 1을 누적시키기
        
        if room[j][i] == '.':
            column += 1
        else:
            column = 0
        if column == 2:
            result[1] += 1

print(*result)
```

- 정사각형은 `range`가 같기 때문에 하나의 이중 for문에 사용해도 됨
  - 단 기준점이 다르기 때문에 `matrix[i][j]` 와 `matrix[j][i]`의 차이를 잘 구분 해야 한다
    - 주로, 내가 쓸 때에는, 전자는 열을 기준, 후자가 행을 기준으로 순회한다

