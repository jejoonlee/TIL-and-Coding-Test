# 🧑‍💻 문제 풀이

전체는 아님

[10798 세로 일기 (리스트)](#%EF%B8%8F-10798-세로-일기)

[10816 숫자카드 (딕셔너리)](#%EF%B8%8F-10816-숫자카드)

[1302 베스트 셀러 (딕셔너리)](#%EF%B8%8F-1302-베스트-셀러)

[1110 더하기 사이클 (while문)](#%EF%B8%8F-1110-더하기-사이클)

[1065 한수 (for문, if문)](#%EF%B8%8F-1065-한수)



### ✔️ 10798 세로 읽기

```python
arr = []

# 입력을 하고, 입력한 문자열들을
# arr 변수 리스트에 넣는다
for i in range(5):
    input_ = input()
    arr.append(input_)

# 리스트 안에 있는 문자열들의 길이 중
# 제일 큰 길이를 구한다 max_len (max length)
len_list = []
for leng in arr:
    length = len(leng)
    len_list.append(length)
    max_len = max(len_list)

# 2 중 문자열을 이용한다
for i in range(max_len):
# max_len, 길이게 제일 긴 길이를 range로 둔다
    for j in range(5):
    # j는 5개의 입력 값들이다
        if i < len(arr[j]):
        # 만약 i 가 입력한 값의 단어의 길이보다 작으면
            print(arr[j][i], end='')
            # arr[j][i]를 출력한다
```

#### **🚨중요 포인트**

- `if i < len(arr[j])` 의 경우, 문자열 중 길이가 `i`보다 짧은 문자열들이 있다.
  - 그 문자열들을 건너 뛰고, `i`보다 긴 문자열들의 문자를 출력한다

- `print(arr[j][i])` 경우, 위에 if문이 참일 때,
  - 입력된 문자 중 `j`번째 문자의 `i`번째 알파벳을 출력한다




### ✔️  10816 숫자카드

```python
# 가지고 있는 카드의 정수
N = int(input())
N_card = input().split()
# 구해야할 카드 M개의 정수
M = int(input())
M_card = input().split()

# 방식 1. M_card를 먼저 딕셔너리에 넣고
# N_card랑 같은 숫자면 1을 더하고, 없으면 그냥 놔두기

# card = {}
# for i in M_card:
#     if i not in card:
#         card[i] = 0

# for i in N_card:
#     if i in card:
#         card[i] += 1
#     else:
#         continue

# result = list(card.values())

# for i in result:
#     print(i, end = ' ')


card = {}
for n in N_card:
    if n not in card:
        card[n] = 1
    else:
        card[n] += 1

for m in M_card:
    if m in card:
        print(card[m], end = ' ')
    else:
        print(0, end =' ')
```

#### **🚨중요 포인트**

- 둘 다, 주어진 숫자들을 `key` 로 넣고 숫자들의 개수를 `value`로 딕셔너리에 넣었다
- 그리고 같은 `key` 면 카드의 value를 출력하고, 아니면 0을  출력했다



- 첫 번째 (답은 같은데, 틀렸음...)
  - `M` (구해야할 숫자)들을 `key`로 지정하고, `value`는 모두 0으로 기본값을 만들었다
  - `N` 의 숫자들과 일치하는 `key` 가 있으면 `value`에 1씩 누적 시켰다
  - 그리고 마지막으로 구해진 `value` 만 출력했음



### ✔️ 1302 베스트 셀러

```python
sell = int(input())

books = {}
name_list = []

for i in range(sell):
    names = input()
    name_list.append(names)

for name in name_list:
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

max_num = max(books.values())

best = []
for key, value in books.items():
    if value == max_num:
       best.append(key)

best.sort()

print(best[0]) 
```

#### 🚨중요 포인트 

- 딕셔너리에 `key`와 `value`를 넣는다 
- `for문` `key, value`와 `.items()`를 통해서 value 값을 찾아, key 값을 리스트에 넣는다!



### ✔️ 1110 더하기 사이클

```python
input_ = int(input())

num = input_

cnt = 1

while True:
        a = num // 10
        # 숫자의 십의 자리를 일의 자리로 변환
        b = num % 10
        # 숫자의 일의 자리를 가져오기
        c = a + b
        # c는 a와 b를 더한 것
        num = b * 10 + c % 10
        if num != input_:
            cnt += 1
        elif num == input_:
            break

print(cnt)
```

#### 🚨중요 포인트 

- while문을 이용해서, 입력한 숫자 `input_` 값과 더하기를 통해 나온 `num`의 값이 똑같을 때까지 계산을 한다
- 그리고 한번 돌 때마다 `cnt`에 1을 더해 준다. 기본값은 1이다.



### ✔️ 1065 한수

```python
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 즉 주어진 정수에서 각 숫자들을 나열하고, 등차수열로 이루어진다면, 그게 한수이다

# 1000보다 작은 자연수가 주어진다 ***
# 그리고 1부터 99까지는 모든 수가 한수이다

nums = int(input())

cnt = 0

for num in range(1, nums + 1):
    # 100 미만은 모두 한수이기 때문에, 카운트를 해준다
    if num < 100:
        cnt += 1

    else: 
        # 100부터는 주어진 수에서, 숫자들을 리스트를 통해 분리한다
        num = list(map(int, str(num)))
        # 그리고 숫자들의 차이가 일정하면, 한수이고, 아니면 한수가 아니다
        if num[0] - num[1] == num[1] - num[2]:
            cnt += 1

print(cnt)
```

#### 🚨중요 포인트 

- 1부터 99까지는 한수다
- 1000 까지의 정수이기 때문에 `num[0] - num[1] == num[1] - num[2` 를 해준다
