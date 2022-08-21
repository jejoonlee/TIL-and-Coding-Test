# ✍️ 문제풀이

[후기](#후기)

[1371 가장 많은 글자](#1371-가장-많은-글자)

[1526 가장 큰 금민수](#1526-가장-큰-금민수)

[2897 몬스터 트럭](#2897-몬스터-트럭)



## 백준 풀이



### 1371 가장 많은 글자

```python
code = [0] * 26

# try : 정상적으로 실행될 때 (오류가 없을 때)
# except: 오류가 발생할 때 실행되는 코드 블럭

while True:
    try:
        sen = input()
        for s in sen:
            if s == ' ':
                continue
            else:
                code[ord(s) - 97] += 1

        # code에서 제일 큰 값을 가지고 온다
        max_value = max(code)

        final = []
        for c in range(len(code)):
            # 코드의 c 번째에 있는 값이 max_value와 같다면
            if code[c] == max_value:
                # final 리스트에 유니코드에서 알파벳으로 변형된 값을 넣은다
                final.append(chr(c + 97))

    except EOFError:
        break

result = ''.join(final)
print(result)
---------------------------------------------------------------------

# x는 dict_.items()에 의해 만들어진 각 튜플
# x[0] 는 각 튜플의 인덱스
# -x[1] 튜플의 1번째 인덱스를 내림차순으로 정렬
# sorted_dict = sorted(dict_.items(), key = lambda x: (-x[1], x[0]))
```





### 1526 가장 큰 금민수

```python
N = int(input())

gms = []
# 작거나 같은 => + 1

num = 40

while num != N:
    flag = True
    num += 1

    nums = str(num)

    for i in range(len(nums)):
        if nums[i] == '4' or nums[i] == '7':
            pass
        else:
            # 4, 7이 아예 없다면 flag는 False로 저장된다
            # 그렇게 저장되면, 아래 if 조건문과 성사가 안 되서
            # 다시 while문 시작점으로 돌아간다
            flag = False

    if flag:
        gms.append(num)

print(max(gms))

----------------------------------------------------------------
# 제일 큰 수에서 'N' 아래로 내려가면서 최대값을 구하는 코드


N = int(input())

# 작거나 같은 => + 1

while True:
    flag = True

    nums = str(N)

    for i in range(len(nums)):
        if nums[i] == '4' or nums[i] == '7':
            pass
        else:
            # 4, 7이 아예 없다면 flag는 False로 저장된다
            # 그렇게 저장되면, 아래 if 조건문과 성사가 안 되서
            # 다시 while문 시작점으로 돌아간다
            flag = False
            N -= 1
            # 최대값을 구하기 때문에, 내려오면서 계산한다
            # 예를 들어 100부터 시작해서, flag가 False이면
            # N에 1일 빼준다

    if flag:
        print(N)
        break
```



### 2897 몬스터 트럭

```python
R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]

dr = [1, 1, 0]
dc = [0, 1, 1]

destroy = [0, 0, 0, 0, 0]
empty = '.'
car = 'X'
building = '#'

for x in range(R):
    for y in range(C):
        flag = True
        cnt = 0

        # 만약 해당 좌표에 건물이 있으면 아무것도 할 수 없다
        if parking[x][y] == building:
            continue

        if parking[x][y] == car:
            cnt += 1
            
            # 델타 탐색
        for i in range(3):
            sr = dr[i] + x
            sc = dc[i] + y

            if 0 <= sr < R and 0 <= sc < C:

                if parking[sr][sc] == building:
                    flag = False
                    break

                elif parking[sr][sc] == car:
                    cnt += 1
            
            else:
                flag = False
                # 2 X 2 라서, 끝 부분에 들어가면,
                # flag를 false로 변환되어,
                # 좌표로 들어간다
            
        if flag == True:
            destroy[cnt] += 1

for i in destroy:
    print(i)
```

- `Flag` 를 이용해서 참과 거짓에 따라서, 값을 저장을 하고 안 하는 것 
