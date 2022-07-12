# 📋 Python Control Statements

#### Category

[제어문 (Control Statement)](#%EF%B8%8F-제어문-control-statement)

[조건문](#%EF%B8%8F-조건문)

- [복수 조건문 (elif: else if)](#복수-조건문-elif-else-if)
- [중첩 조건문](#중첩-조건문)
- [조건 표현식 (Conditional Expression)](#조건-표현식-conditional-expression)

[반복문](#%EF%B8%8F-반복문)

- [while문](#while문)
- [for문](#for문)
- [반복제어](#반복제어)



## ✔️ 제어문 (Control Statement)

> 제어문에는 조건문과 반복문이 있다

### 조건문	

- `if___:`
- `else:`  직접 조건 X / 남은 모든 나머지들

### 반복문

- `while___:` 참일때까지 실행
- `for _변수이름_ in _반복가능한_:`  container (통)에서 처음부터 끝까지 꺼내준다
- 제어
  - `break` : 종료
  - `continue` : 다음 실행
  - `for-else` : 모든 반복을 하게 되면 실행



## ✔️ 조건문

> 참/거짓을 판단할 수 있는 조건식과 함께 사용한다
>
> Expression에는 True/False에 대한 조건식이 들어간다



**조건문 예시**

```python
num = int(input())

if num >= 0:			# 'num >= 0:' 은 expression 이다
    print('양수')		   # expression이 참이면 '양수'가 출력이 된다
else:
    print('음수')		   # expression이 거짓이면 '음수'가 출력 된다
```

조건문 expression 뒤에 `:` 콜론이 꼭 들어가야 한다



- #### **복수 조건문 (elif: else if)**

```python
score = int(input()) # int를 설정하여 정수로 만든다

if score >= 90:
    print('World Class')
elif 90 > score >= 80:			# elif <expression>:
    print('Professional')
elif score > 70:				# 순차적으로 위에서 아래로 비교하는 것이라서 간단하게 작성해도 됨
    print('Semi-pro')
else:							# else는 위의 모든 조건에 해당하지 않는 나머지
    print('Amateur')
# else는 조건문에서 생략이 가능하다
# elif = else if = 복수 조건문을 사용할 때에 elif를 쓴다
```



- #### **중첩 조건문**

  - 조건문 안에 조건문을 사용할 수 있다. 즉 `if`는 꼭 한번만 쓰는 것이 아니다

```python
score = int(input()) # int를 설정하여 정수로 만든다

if score >= 90:
    if score > 100:					# 중첩 조건문, 조건문 안에 조건문을 사용
        print('Impossible Score')
    else:
    	print('World Class')
elif 90 > score >= 80:				# elif <expression>:
    print('Professional')
elif score > 70:				# 순차적으로 위에서 아래로 비교하는 것이라서 간단하게 작성해도 됨
    print('Semi-pro')
else:							# else는 위의 모든 조건에 해당하지 않는 나머지
    if score < 50:
        print('Need More Work')
    print('Amateur')
    
# 중첩 조건문에서 if 이후, else가 없어서 50 미만이면 'Need More Work'와 'Amateur'가 출력 됨
# 'print('Need More Work')' 이후 'else'가 들어가면, 70점과 50점 사이에 는 'Need More Work'가 없어진다
```



- #### **조건 표현식 (Conditional Expression)**

  - 조건문을 다르게 표현한 것이다. (자주 사용 안 함)

```python
<true인 경우 값> if <expression> else <false인 경우 값>

num = int(input())
value = num if num >= 0 else -num
print(value)

# 원래 조건문
num = int(input())
if num >= 0:
	value = num
else:
    valeu = -num
print(value)    
```





## ✔️ 반복문

> while문, for문, 반복제어가 있다



#### while문

- 조건식(expression)이 `참이면` 반복적으로 실행한다. 반대로 `거짓`이면 실행이 안 된다
- 즉 `while`문은 `거짓`이 될 때까지 반복적으로 실행한다

```python
a = 0
while a < 5:		# 'a < 5' 는 종료 조건
    print(a)
    a += 1			# 반복 시행시 a가 계속 증가
print('끝')

# 1부터 n까지 합을 구하여 출력하는 코드

n = 0
result = 0						# 'n'과 'result'를 초기 값 '0'으로 설절
user_input = int(input())
    
while n <= user_input:			# while문은 'while <expression>:' 으로 시작한다
    result += n					# 'result'와 'n'을 계속 더한다
    n += 1						# 한번 더해질 때마다 'n'을 1로 더한다
print(result)					# 'n'이 'user_input'의 이하일때까지 반복한다
```



#### for문

- for문은 시퀀스 (str, tuple, list, range)를 포함한 순회가능한 객체 (iterable) 요소를 모두 순회함
- 통 안에 있는 list를 각각 출력하는 것이다
- 즉 처음부터 끝까지 순회하여 종료조건이 필요하지 않음

`for <변수명> in <iterable>:` 이후 코드 블록을 작성

- **iterable**
  - 순회할 수 있는 자료형 (str, list, dict 등)
  - 순회형 함수 (range, enumerate)

```python
name = ['Alex', 'Yang', 'Yushi']
for i in name:
    print(i)
print('끝')							# 위에서 아래로 'Alex Yang Yushi 끝' 이 출력 됨
-----------------------------------------------------------------------------------------

n = 1
result = 1
user_input = int(input())

for i in range(1, user_input + 1):	# range를 이용
    result *= n
    n += 1
print(result)
-----------------------------------------------------------------------------------------

chars = input()		# hi
for idx in range(len(chars)):			# range를 활용하는것 → index를 활용해서 접근
    print(chars[idx])					# index 기준으로 순회
# h
# i
```



- **Enumerate**
  - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
names = ['Alex', 'Yang', 'Yushi']

for i,name in enumerate(names):
    print(i, name)

# 0 Alex
# 1 Yang
# 2 Yushi

print(list(enumerate(names)))
# [(0, 'Alex'), (1, 'Yang'), (2, 'Yushi')]
```



- **딕셔너리 순회**
  - `Key`를 순회하며, `Key`를 통해 값을 활용
  - `Key`가 출력된다

```python
likes = {'football': 100, 'basketball': 95, 'weight': 0}	

for sport in likes:
    print(sport)
# football										# key 순회
# basketball
# weight

for sport in likes:
    print(sport, likes[sport])
# football 100									# key를 통해 값을 활용
# basketball 95
# weight 0
```





#### 반복제어

> `break` , `continue` , `for-else` 가 있다

- **break**
  - 반복문 종료

```python
n = 0
while True:
    if n == 3:
        break			# 'n'의 값이 3이 되면 종료
    print(n)
    n += 1
# 0, 1, 2 까지
-----------------------------------------------------------------------------------------

for i in range(10):					# 0 부터 9까지
    if i > 1:					
        print('0과 1만 필요해!')			
        break						# i 가 1 초과일때 '0과 1만 필요해!'를 출력하고 종료
    print(i)
# 0, 1, '0과 1만 필요해!'
```



- **continue**
  - `continue` 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행 한다

```python
for i in range(6):				# 0~5
    if i % 2 == 0:				
        continue				# 짝수면 출력하지 않고, 홀수면 출력해라
    print(i)
# 1, 3, 5
```



- **for-else**
  - 끝까지 반복문을 실행한 이후에 else문 실행

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break				# apple 에 'b'가 없으므로, 끝까지 진행한다
else:
    print('b가 없습니다')	 # 끝까지 진행한 후, 'b가 없습니다'를 출력한다
# b가 없습니다
-----------------------------------------------------------------------------------------

for char in 'banana':
    if char == 'b':
        print('b!')
        break				# banana에 'b'가 있으므로, 'b!'를 출력하고 종료한다
else:
    print('b가 없습니다')
# b!
```

