# ✍️ 문제풀이

[후기](#후기)

[1269 대칭 차집합](#1269_대칭_차집합)

[11286 절대값 힙](#11286-절대값-힙)

[81301 숫자 문자열과 영단어](#81301-숫자-문자열과-영단어)





## 후기

>



## 백준 풀이



### 1269 대칭 차집합

자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

```python
num = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = set(A)
B = set(B)

s_set = []

for a in A:
    if a not in B:
        s_set.append(a)

for b in B:
    if b not in A:
        s_set.append(b)

result = len(s_set)
print(result)
```

- `list` 값들을 `set` 에 저장한다.
- 그리고 `set B` 에 없는 `A`의 값들을 `s_set`에 넣는다
- 반대로 `set A`에 없는 `B`의 값들을 `s_set`에 넣는다
- 그리고 `s_set`의 길이를 구하면 답이 나온다



### 11286 절대값 힙

1. 배열에 정수 x (x ≠ 0)를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

```python
for n in num:
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
```

##### 🚨🚨🚨 중요 포인트 🚨🚨🚨

- `heapq.heappush(heap, (abs(n), n))` 여기에서 `(abs(n), n)` 은 절대값 `n`과 그냥 `n`을 튜플로 넣어준다
  - 그러면 `heap`이 1순위로 절대값 기준으로 정렬을 한 후
  - 2순위로 n의 값 기준으로 정렬해준다
- 그리고 출력할 때에는 `heapq.heappop(heap)[1]` 튜플의 1번 인덱스의 값을 가지고 온다



### 4949 균형잡힌 세상

`[`는 `]`로 닫을 수 있고, `(`는 `)`로 닫을 수 있다!

```python
while True:
    sen = input()
    stack_ = []

    if sen == '.':
        break

    for s in sen:
        if s == '(' or s == '[':
            stack_.append(s)
        elif s == ')':
            if len(stack_) == 0 or stack_[-1] == '[':
                stack_.append(s)
                break
            elif stack_[-1] == '(':
                stack_.pop()
        elif s == ']':
            if len(stack_) == 0 or stack_[-1] == '(':
                stack_.append(s)
                break
            elif stack_[-1] == '[':
                stack_.pop()
        
    if len(stack_) == 0:
        print('yes')
    else:
        print('no')

```

- 기본적으로 `stack_` 에 아마것도 없으면 `(` 나 `[`을 넣는다
- 만약 `)`이 나오면
  - 스택에 아무것도 없거나 스택의 마지막에 `)` 경우 `[` 가 있으면 스택에 `)` 를 넣고 중단을 한다 (왜냐하면, `[` 같은 경우 `)`로 덮을 수 없다)
    - 이후 바로 'no'가 출력된다
  - 반대로 스택 마지막에 `(`이 있으면, 스택의 마지막 값을 빼낸다
- 만약 `]`이 나오면
  - 스택에 아무것도 없거나 스택의 마지막에 `]` 경우 `(` 가 있으면 스택에 `]` 를 넣고 중단을 한다 (왜냐하면, `(` 같은 경우 `]`로 덮을 수 없다)
    - 이후 바로 'no'가 출력된다
  - 반대로 스택 마지막에 `[`이 있으면, 스택의 마지막 값을 빼낸다
- 마지막으로 `stack_` 에 값이 아무것도 없으면 `yes`를 출력하고, 아니면 `no`를 출력한다





## Programmers

### 81301 숫자 문자열과 영단어

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

- 1478 → "one4seveneight"
- 234567 → "23four5six7"
- 10203 → "1zerotwozero3"

```python
# 같은 단어가 있으면, 앞에만 바뀌고, 바로 다음 단어로 넘어간다.
# 다 다른 단어면 가능

# s = "1zerotwozero3"

# num_let = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# num = []

# for i in range(len(num_let)):
#     if num_let[i] in s:
#         num.append(str(i))
#     if str(i) in s:
#         num.append(str(i))

# print(num)
--------------------------------------------------------

def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    answer = ''
    alp = ''

    for letters in s:
        if letters.isdigit():
            answer += letters
        else:
            alp += letters
            # 한 글자씩 alp에 저장하고
            if alp in num.keys():
            # 그 글자가 모여 딕셔너리 key와 같으면
                answer += num[alp]
                # answer 문자열에 딕셔너리 value를 넣는다
                alp = ''
                # 그리고 alp는 다시 초기화
    
    return int(answer)
```

#### 🚨🚨🚨 중요 포인트 🚨🚨🚨

- **리스트**를 사용했을 때
  - 한 단어를 찾기 때문에, 뒤에 똑같은 단어가 있으면, 그 단어는 건너 뛴다. 즉 제일 먼저 나온 단어부터 찾는다
- **정답**에서는
  - 숫자가 아니면 한 문자, 한 문자 씩 다른 문자열 `alp` 에 저장을 시켰다
  - 그 문자가 딕셔너리에 있는 key와 같아지면, 해당 key의 value를 `answer`에 저장한다
  - 그 다음, 다른 단어들을 찾기 위해 `alp`를 초기화 한다
