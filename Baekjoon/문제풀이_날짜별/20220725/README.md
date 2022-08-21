# ✍️ 문제풀이

[후기](#후기)

[숫자의 개수](#숫자의-개수)

[상수](#상수)

[두개뽑아서더하기](#두개뽑아서더하기)

[OX퀴즈](#OX퀴즈)



## 후기

> 전체적으로 아직 많이 부족한 것을 느꼈다. 주로 전에 풀었던 문제들을 응용해서 많이 풀었다.
>
> 문제를 먼저 정의하는 것까지는 할 수 있겠는데, 아직 코드로 쓰는 것이 많이 부족했다.
>
> 특히 코드 리뷰가 많이 어려웠다. 머리로는 어떻게 코드를 짰는지 알았지만, 막상 설명하려고 하니, 생각이 안 났다.
>
> 계속 주석을 걸어서 코드를 쓰지만, 이제는 주석으로 만족하지 않고, 혼자서 말로 설명하는 훈련도 해야 할 것 같다.





## 숫자의 개수

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

```python
a = int(input())
b = int(input())
c = int(input())
# a, b, c 라는 정수를 입력하는 변수를 만든다

mult = a * b * c
# 'mult'라는 변수를 만들어, a,b,c를 모두 곱했습니다

li = [0] * 10
# 인덱스가 0부터 9의 리스트를 만들었음 (모든 인덱스의 값은 0)
# 인덱스 값을 통해 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지 구하기 위함

mult_list = list(map(int, str(mult)))
# 'mult'를 map을 통해서 리스트로 만드는 작업

for i in range(len(mult_list)):
# mult_list의 값들을 인덱스로 변환한 것이 i
    li[mult_list[i]] += 1
	# li의 리스트 안에 mult_list[i] 라는 인덱스가 나타날 때
    # +1을 한다

for result in li:
    print(result)
    
```





## 상수

상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

```python
a, b = map(int, input().split())

reverse_num_a = 0

while a:
    leftover = a % 10
    reverse_num_a = reverse_num_a * 10 + leftover
    a = a // 10
# a의 10으로 나눈 나머지를
# 일의 숫자에 더한다
# a와 10의 나눈 몫을 가지고 오면, a의 자릿수는 하나 줄어든다

# 줄어든 a를 다시 10으로 나누고
# 전에 숫자를 10으로 곱하고, 새로운 a의 나머지를 더한다
# 그리고 a의 나눈 몫을 가지고 오면 또 a 자릿수는 하나 줄어들고
# 이후 계속 반복하면 숫자가 거꾸로 되어 있다


reverse_num_b = 0

while b:
    leftover = b % 10
    reverse_num_b = reverse_num_b * 10 + leftover
    b = b // 10

if reverse_num_a > reverse_num_b:
    print(reverse_num_a)
else:
    print(reverse_num_b)
    
---------------------------------------------------------------------------------------

a, b = input().split()

reverse_a = int(a[::-1])
reverse_b = int(b[::-1])
# 각 str을 [::-1] 통해 거꾸로 반환한후, int 정수로 만든다

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)
```







## 두개뽑아서더하기

정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.



 ```python
 def solution(numbers):
     answer = []
     num_set = set()
     # set을 만들어서 나중에 겹치는 숫자는 빼준다
 
     for i in range(len(numbers)):
     # i는 리스트 안에 있는 숫자들의 '인덱스'이다
         for j in range(i+1, len(numbers)):
         # j도 리스트 안에 있는 숫자들의 '인덱스'이지만
         # i보다 1씩 더 큰 인덱스를 가지고 있는 J
         # 서로 다른 인덱스의 두 수를 뽑아 더하는 것이라서!
             num_set.add(numbers[i] + numbers[j])
             # number[i] 와 number[j]는 '인덱스'의 해당 '값'이다
             # .add()를 통해 num_set에 더해진 숫자들을 넣어준다
             answer = list(num_set)
             # set을 list로 변환하기
             answer.sort()
             # sort 함수를 써서 오름차순으로 반환해준다
     return answer
 
 
 print(solution([2, 1, 3, 4, 1]))
 print(solution([5, 0, 2, 7]))
 ```
`for i in range(len(numbers)):` 
`for j in range(i + 1, (len(numbers))):`
- 서로 다른 인덱스에 있는 두 수를 더하기 때문에 `for J` 문에 `i + 1`을 한다
- 만약에 `i + 1`이 없다면, 같은 인덱스 수까지 같이 더해준다


## OX퀴즈

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

```python
t = int(input())

# 'num'과 'result'를 0으로 설정
# 'X' 값이면 'num'은 바로 0으로 반환된다
# 'O' 값이면 'num += 1' 을 통해 O는 1이 되고
# 'O' 값이 반복하면 'num += 1' 을 통해 1씩 더해진다
# 'result += num' 은 'num' 변수를 더하고 나온 결과 값이다
for i in range(1, t + 1):
    a = list(input()) # O x를 리스트에 넣기
    num = 0
    result = 0
    for i in a:
    # a에 있는 iterable i로 반환
        if i == 'O':
            num += 1
            result += num
        elif i == 'X':
            num = 0
        # O가 나올때까지 num은 0으로 리셋된다
    
    print(result)
```

