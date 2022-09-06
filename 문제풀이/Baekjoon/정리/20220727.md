# ✍️ 문제풀이

[후기](#후기)

[programmers 음양더하기](#programmers-음양더하기)

[단어공부](#단어공부)

[크로아티아 알파벳](#크로아티아-알파벳)

[슈퍼마리오](#슈퍼마리오)

[덩치](#덩치)



## 후기

> 오늘은 구글링을 최대한 안 하고, 먼저 정의에 대해 많이 고민하고 풀어보았습니다.
>
> 확실히, 코드가 더 이해 쉽게 쓰여지는 느낌을 받았습니다. 중간 중간에, 어떤 식으로 코드를 작성하는지는, 구글링을 통해 작성하기는 했지만, 확실히 성취감이 더 있었습니다.



## programmers 음양더하기

어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

```python
def solution(absolutes, signs):
# absolutes 와 signs의 리스트 안의 값들의 개수는 같다

    result = 0
    for i in range(len(absolutes)):
    # range(len(abolutes))를 for문을 통해 인덱스 가져오기
        if signs[i] == True:
        # signs에 i 인덱스가 True면
            result = result + absolutes[i]
            # 결과 값에 absolutes 인덱스 i번째를 더해준다
        elif signs[i] == False:
        # signs에 i 인덱스가 False면
            result = result - absolutes[i]
            # result 결과 값에 absolutes 인덱스 i번째를 빼준다
    
    return result

print(solution([4, 7, 12], [True, False, True]))
```





## 단어공부

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 

단, 대문자와 소문자를 구분하지 않는다.



#### 딕셔너리를 이용해서, 딕셔너리의 값을 비교해서, 2개 이상이면 물음표 '?' 를 출력하고, 하나면, 해당 값의 키를 출력하는 방식

```python
word = input()

cap = word.upper()
# 출력할 때에 모든 문자를 대문자로 변경을 해야하기 때문에,
# 모든 문자를 먼저 대문자로 변경

char = {}
# char라는 딕셔너리 초기값을 만들었음

for i in cap:
# 변수, cap, 이라는 문자열을 순회하는 for문을 써서
    if i in char:
    # i 값이 이미 딕셔너리에 존재하면, value에 1씩 더하고
        char[i] += 1
    else:
    # i 값이 딕셔너리에 없으면, value를 1로 하고, key도 새로 넣어준다
        char[i] = 1


max_value = max(char.values())
# max_value를 만들어서, char, 딕셔너리에 들어가 있는
# key들의 값들 중 제일 큰 값을 max를 통해 가지고 온다

char_list = []
# char_list 라는 리스트를 만드는데
# 여기에는 value 값이 제일 큰 key를 넣는다
for key,value in char.items():
# char.items()를 통해 키, 값의 쌍을 담은 뷰를 반환하고
# for문을 통해 순회한다
    if value == max_value:
    # value 쯕 딕셔너리의 value가 아까 구했던 max_value 값과 같으면
        char_list.append(key)
        # char_list에 딕셔너리의 key를 넣는다

if len(char_list) >= 2:
    print('?')
    # 마지막으로 만약 리스트의 길이가 2개 이상이면 ?를 출력하고
else:
    print(''.join(char_list))
    # 그게 아니면 리스트에서 그냥 문자열로 변환한 문자열을 출력한다
```





## 크로아티아 알파벳

```python
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 알파벳가 변경된 단어들을 리스트에 넣는다

word = input()

for i in cro:
# 변경된 단어들을 순회하면서 반환한다
    if i in word:
    # 만약 순회하는 단어(i) 중 입력한 단어 안에 알파벳과 같으면
        cro_word = word.replace(i, '1')
        # .replace를 통해 단어를 '1'로 변환시켰다
        # 그 값은 cro_word 변수로 반환되고
        word = cro_word
        # cro_word에 반환된 단어를, 다시 word로 반환시켜준다

cnt = 0
for i in word:
# 다시 for문을 통해 단어를 순회하며
# 나오는 알파벳마다 1씩 더해서, 단어의 길이를 구한다
    cnt += 1

print(cnt)

```







## 슈퍼마리오

슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.

슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.

마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.

버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

 ```python
 # 더한 값들을 리스트에 넣고, 그 중 100과 제일 가까운 수를 구했다
 
 score = []
 # 입력한 값들을 리스트에 넣기 위해 'score'이라는 리스트 변수를 만듬
 
 for i in range(10):
     a = int(input())
     score.append(a)
     # 값들이 입력되면, ''.append'를 통해 'score' 리스트에 값들을 넣음
 
 result = 0
 # 더하기를 누적해야하기 때문에 'result' 기본 변수값을 만들었고
 lst = []
 # 리스트를 하나 더 만들었다
 
 for i in score:
     result = i + result
     lst.append(result)
     # score 리스트에 있는 값들을 꺼내서, 더하기로 result를 누적시키고
     # result가 만들어질 때마다 'lst'라는 또 다른 리스트에 값들을 넣는다
 
 ans = min(lst[::-1], key = lambda x: abs(x - 100))
 # 마지막으로 100과 가장 가까운 값을 구하는 코드
 # 'key' 파라미터와 lambda 함수를 통해, 
 # 'lst'에 있는 모든 값들을 100으로 뺀 후, 0과 가장 가까운 값
 # 즉 'min'을 통해 0과 가장 가까운 값을 구했다
 # 여기서 abs() 함수를 써서 100으로 뺀 수들을 절대값으로 만들었습니다
 # 'lst'에 100과 가까운 값이 두개가 존재할 때, 더 큰 값을 출력하기 위해서
 # 'lst' 맨 앞이 아닌, 맨 뒤에서부터 100을 빼준다.
 
 print(ans)
 ```

```python
import sys

sys.stdin = open('input.txt', 'r')

# 키와 몸무게가 모두 커야 덩치가 더 큰 것
# 자신보다 더 덩치가 큰 사람들이 있으면 k + 1

N = int(input())
# 사람 수

lst = []
for i in range(N):
    x, y = map(int, input().split())
    #키와 몸무게
    lst.append((x, y))
    #[(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

rank = 1
rank_list = [0] * N

# 모든 사람들을 비교하기 위한 이중 반복문
for a in range(N):
# N명 중 각자의 키와 몸무게를 가지고 온다
    A = lst[a] # 기준이 되는 사람
    for b in range(N):
    # N명 안에 각자의 키와 몸무게를 또 가지고 온다
    # 비교를 하기 위해
        B = lst[b] # 비교하는 사람
        if A[0] > B[0] and A[1] > B[1]:
        # 각자의 키는 키끼리, 몸무게는 몸무게끼리 비교한다
        # B보다 덩치가 큰 사람이 1명이 더 있다
            rank_list[b] += 1


print(rank_list)
for rank in rank_list:
    print(rank + 1, end = ' ')
```



## 덩치

```python
N = int(input())

lst = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    lst.append((x, y))
    # 키 x 와 몸무게 y를 리스트 안에 넣는다
    # [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

rank = [] * N
    
for a in lst:
# 리스트 안에 있는 값을 비교하기 위한 `기준점`
    A = lst[a]
	for b in lst:
    # 리스트 안에 있는 값을 비교하기 위한 비교 숫자
    	B = lst[b]
            if A[0] > B[0] and A[1] > B[1]:
			# 키와 몸무게가 모두 B가 작으면
            	rank[b] += 1
                # rank의 b 인덱스에 1을 더하기
                # 덩치가 큰 사람이 나보다 몇명 더 있는지 찾는 것
                
for result in rank:
    print(result + 1, end = ' ')
    # 마지막에 1씩 더해준다. 1부터 시작임
    # 즉 값이 1이면, 해당 사람보다 덩치가 큰 사람이 없는 것
```

