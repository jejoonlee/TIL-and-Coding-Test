# ✍️ 문제풀이

[후기](#후기)

[SASA 모형을 만들기](#SASA 모형을 만들기)

[나머지](#나머지)

[다이얼](#다이얼)

[쉽게 푸는 문제](#쉽게-푸는-문제)

[뒤집힌 덧셈](#뒤집힌-덧셈)



## 후기

>이번주 실습 중에서 제일 쉬웠던 것 같다. 확실히 잘 정리하고 문제를 풀다 보니깐 많이 도움이 되었다.



## 백준 풀이



### SASA 모형 만들기

당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 M개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.

SASA 모형 1개를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

```python
# SASA를 만들 때에 S 2개, A 2개씩 필수적으로 필요하다.
# 즉 S 2개, A 2개가 하나의 세트가 되는 것
# 세트를 구하는 문제라서, S와 A를 각자 2로 나눈 후, 더 작은 몫이 답이 된다.

# 예를 들어 S 4개가 있고 A 5개가 있는데, SASA 2세트를 만들 수 있고, A가 하나 남는다.

n, m = map(int,input().split())

if n // 2 == m // 2:
# 둘이 나눠서 몫이 같으면, n, m 중 아무거나 출력
    print(n // 2)
elif n // 2 < m // 2:
# 나눠서 몫이 n이 적으면 n의 몫이 답이다
    print(n // 2)
elif n // 2 > m // 2:
# 나눠서 몫이 m이 적으면 m의 몫이 답이다
    print(m // 2)
    
-------------------------------------------------------------

n, m = map(int,input().split())

ans = min(n // 2, m // 2)
# n과 m을 2로 나눈 후의 몫 중에 작은 것을 반환해야 해서
# min을 써서, 최솟값을 가지고 온다

print(ans)
```

- min을 써도 된다



### 나머지

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

```python
# set을 이용해 같은 나머지들을 제거한 후
# list로 변환해서, len을 통해 개수를 구했따

nums = set()

for i in range(10):
    num = int(input())
    leftover = num % 42
    nums.add(leftover)
    # set 안에 42를 나누고 남은 나머지 넣기
    lst = list(nums)
    # set을 list로 변환

print(len(lst))
# len을 통해 list의 개수를 구함
```





### 다이얼

```python
# a의 각 문자열의 알파벳을 순회하고
# if문을 통해, 알파벳이 해당 그룹에 속하면
# 정해진 번호로 .replace 되고, 마지막에 그것들을 다 더한다

# a = input()

# for i in a:
#     if i in ['A', 'B', 'C']:
#         a = a.replace(i, '3')
#     elif i in ['D', 'E', 'F']:
#         a = a.replace(i, '4')    
#     elif i in ['G', 'H', 'I']:
#         a = a.replace(i, '5')
#     elif i in ['J', 'K', 'L']:
#         a = a.replace(i, '6')
#     elif i in ['M', 'N', 'O']:
#         a = a.replace(i, '7')
#     elif i in ['P', 'Q', 'R', 'S']:
#         a = a.replace(i, '8')
#     elif i in ['T', 'U', 'V']:
#         a = a.replace(i, '9')
#     elif i in ['W', 'X', 'Y', 'Z']:
#         a = a.replace(i, '10')

# result = sum(map(int, list(a)))

# print(result)

----------------------------------------------------------------

a = input()

phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 알파벳을 리스트 안에 넣은다

result = 0

# 중복 for문 이용
for i in a:
# 입력 문자열의 알파벳을 순회
    for j in phone:
    # phone 변수 안에 저장 되어 있는 리스트를 순회한다
        if i in j:
        # 알파벳이 phone 변수 안에 저장 되어 있는 값에 있으면
            result = result + phone.index(j) + 3
            # 해당하는 j의 인덱스를 가져오고, 그것에 3을 더한 후
            # 숫자를 누적시키다

print(result)
------------------------------------------------------------------
# 딕셔너리로 풀이

dict_ = {
    'A': 3, 'B': 3, 'C': 3,
    'D': 4, 'E': 4, 'F': 4,
    'G': 5, 'H': 5, 'I': 5,
    'J': 6, 'K': 6, 'L': 6,
    'M': 7, 'N': 7, 'O': 7,
    'P': 8, 'Q': 8, 'R': 8, 'S': 8,
    'T': 9, 'U': 9, 'V': 9,
    'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

result = 0
key = 'UNUCIC'

for i in key:
    if i in dict_:
        result += dict_[i]

print(result)
```





### 쉽게 푸는 문제

동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

 ```python
 a, b = map(int, input().split())
 
 
 nums =[]
 for i in range(1, b + 1):
 # !수열의 길이가 B보다 작을 때까지 구한다!
 # 1부터 b + 1을 순회
 # b가 7이면 1 2 3 4 5 6 7 호출
     for j in range(i):
     # j는 횟수, i는 크기
     # 즉 j로 i미만의 숫자까지 센다
         nums.append(i)
         # 순회를 할 때마다, i를 nums 리스트 안에 넣는다
 
         
 result = sum(nums[a - 1 : b])
     
 print(result)
 ```





### 뒤집힌 덧셈

어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

```python
def rev(number):
    result = 0
    
    while number:
        num = number % 10
        result = result * 10 + num
        number = number // 10
    
    return result
# 뒤집어지는 함수를 만든다
# number의 나머지를 계속 구하고,
# number의 값이 0일때까지, result에 10을 곱하며, number의 나머지를 더해준다

X, Y = map(int, input().split())

ans = rev(X) + rev(Y)
# 뒤집어진 X와 Y를 더하고

final = rev(ans)
# 값을 다시 뒤집으면 답이 된다

print(final)
```

