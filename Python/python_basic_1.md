# 📋Python Basic 1

#### Category

[컴퓨터 프로그랭 언어](#-컴퓨터-프로그래밍-언어)

[파이썬이란](#-파이썬이란)

[코드 스타일 가이드](#-코드-스타일-가이드)

[변수](#-변수-variable)

[식별자 (Identifiers)](#-식별자-identifiers) 

[사용자 입력 (input)](# -사용자-입력-input)

[주석 (Comment)](#-주석-comment)

[파이썬 기본 자료형](#-파이썬-기본-자료형)    → 불린형, 수치형, 문자열, None

[형 변환](#-형-변환)

[컨테이너 (Container)](#-컨테이너-container)

[시퀀스 (Sequence Container)](#-시퀀스-sequence-container)

[비시퀀스형 컨테이너 (Associative Container)](#-비시퀀스형-컨테이너-associative-container))





## ✔️ 컴퓨터 프로그래밍 언어

> **컴퓨터 Computer** : Calculation + Remember
>
> **프로그래밍 Programming** : 명령어의 모음(집합)을 이용하는 것
>
> **언어** : 자신의 **생각을 나타내고 전달하기** 위해 사용하는 체계 (**문법적**으로 맞는 말의 집합)



**컴퓨터 프로그래밍 언어** : 컴퓨터에게 명령하는 말 

- 명령적 지식 (imperative knowledge) : 'How-to'





## ✔️ 파이썬이란

**Easy to learn**

- 문법 표현이 매우 간결
- 동적 타이핑 언어



**인터프리터 언어 (Interpreter)**

- 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인이 가능



**객체 지향 프로그램 (Object Oriented Programming)**

- 객체 (Object): 숫자, 문자 클래스 등 값을 가지고 있는 모든 것
- 물건, 대상 (어떠한 것, ~ 것)





## ✔️코드 스타일 가이드

```python
print('Hello')
print('World')

a = 'apple'

if True:
    print(True)
else:
    print(False)
    
b = 'banana'
```

**🚨 다른 사람들이 알아볼 수 있도록, 일관성 있게 작성**

- **들여쓰기**
  - 4칸 (space 키 4번) 혹은 1탭 (tab 1번)을 입력





## ✔️ 변수 (Variable)

> 변할 수 있는 수
>
> 변수는 할당 연산자 (=)를 통해 값을 할당 (assignment)
>
> **type()** 을 통해 변수에 할당된 값의 타입을 확인할 수 있다

```python
a = 7
a = a + 10
print(a)
# 17로 출력이 된다

x = y = 7
print(x, y)
# 같은 값을 동시에 할당할 수 있다

x, y = 1, 2
print(x, y)
# 다른 값을 동시에 할당 할 수 있음 (multiple assignment)
-----------------------------------------------------------------------------

x, y = 10, 20					# 각각 값을 바꿔서 저장하는 코드

tmp = x							# x 값이 tmp라는 임시 공간에 들어간다
x = y							# y 값이 x로 들어간다
y = tmp							# tmp에 있던 x 값이 y로 들어간다

print(x, y)						# 20 10 이 출력이 된다
-----------------------------------------------------------------------------

x = 10
y = 20

y, x = x, y

print(x, y)						# 20 10 이 출력된다
```

**🚨 (기본) 코드는 위에서부터 아래로 실행**





## ✔️ 식별자 (Identifiers)

> 파이썬 객체 (변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름

**🚨규칙🚨**

- 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
- 첫 글자에 숫자가 올 수 없음
- 대소문자를 구별
- 예약어들은 사용할 수 없음

```python
# 예약어/키워드 확인 방법

import keyword
print(keyword.kwlist)
```





## ✔  사용자 입력 (input)

> 사용자로부터 즉시 입력 받을 수 있는 내장함수
>
> Input()은 기본적으로 문자열의 형태다. 따라서 숫자로 바꾸려면 'int' 또는 'float' 를 입력해야한다

```python
name = input('이름을 입력해주세요: ')
print(name)
# 이름을 입력해주세요: ~~~

type(name)
# str → string
```





## ✔️ 주석 (Comment)

> 컴퓨터가 읽지 못 한다

```python
# 컴퓨터가 읽지 못 한다. 주로 코드 내용을 쓸 수 있다
```



## ✔️ 파이썬 기본 자료형

> **불린형 (Boolean Type)**, **수치형 (Numeric Type)**, **문자열 (String Type)**, **None** 이 있다



#### 👉 None

- 값이 없음을 표현한다



#### 👉 불린형 (Boolean Type)

- `True` / `False` 값을 가진 타입을 `bool` 또는 불린이라고 한다
  - 0, 0.0 , (), [], {}, ", None 은 모두 `False`

| 연산자  |                             내용                             |
| :-----: | :----------------------------------------------------------: |
| A and B |      A와 B 모두 True시, `True` / 그렇지 않으면 `False`       |
| A or B  | A와 B 중 하나만이라도 True면, `True` / A와 B 모두 False시, `False` |
|   Not   |                True를 False로, False를 True로                |

```python
num = 100
num >= 100 and num % 3 == 1
# num은 100이고 100과 3을 나누면 1이 남으므로, 둘 다 True이므로 True 다
```



#### 👉 수치형 (Numeric Type)

- **Integer (int, 정수)**
  - 모든 정수의 타입은 int
  - 오버플로우가 발생하지 않음
- **Float (실수)**
  - 정수가 아닌 모든 실수 (real number), 즉 소수도 Float
  - Floating point rounding error를 주의
- 복소수 (Complex)
  - 실수부와 허수부로 구성된 복소수는 모두 complex 타입

| 연산자  |    내용    |
| :-----: | :--------: |
|   `+`   |    덧셈    |
|   `-`   |    뺄셈    |
|   `*`   |    곱셈    |
|   `%`   |   나머지   |
|   `/`   |   나눗셈   |
|  `//`   |     몫     |
|  `**`   |  거듭제곱  |
|         |            |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a// b  |
|  a%=b   | a = a % b  |
| a **=b  | a = a ** b |
|         |            |
|    <    |    미만    |
|   <=    |    이하    |
|    >    |    초과    |
|   >=    |    이상    |
|   ==    |    같음    |
|   !=    | 같지 않음  |



#### 👉 문자열 (String)

- 모든 문자는 str 타입

- 문자열은 작은 따옴표('')나 큰 따옴표("")를 활용

  - 하나로 통일하기
  - 중첩따옴표

  ```python
  print('문자열 안에"큰 따옴표"를 사용하려면 작은 따옴표로 묶는다')
  print("문자열 안에'작은 따옴표'를 사용하려면 큰 따옴표로 묶는다")
  ```

  - 삼중따옴표

  ```python
  print('''문자열 안에 '작은 따옴표'나 "큰 따옴표를"를 사용할 수 있고
  여러 줄을 사용할 때도 편리하다''')
  ```

- **인덱싱/ 슬라이싱**
  - 인덱스를 통해 특정 값에 접근할 수 있음

```python
a = 5 						# int
b = '5' 					# str, '따옴표' 안에 들어가서 5는 문자열로 구분
print(a, type(a))			# 5, <class 'int'>
print(b, type(b))			# 5, <class 'str'>

# 길이 - len
fruit = 'abcde'
print(len(fruit)) 			# 5, fruit의 value는 abcde고 5개의 문자로 이루어져있음

# 접근/인덱싱
print(fruit[1]) 			# b, abcde 중 1번째는 b이다. 컴퓨터에서 숫자는 0부터 

# 슬라이싱
print(fruit[1:3]) 			# bc, 1 이상 3 미만
								# a b c d e
								# 0 1 2 3 4

print(fruit[1:4:2])			# bd, 1이상 4 미만 중 2씩 점프

print(fruit[4:1:-1])		# edc, 4이하 1초과 (-1) 뒤로

print(fruit[:2])			# ab, 0이상 2 미만

print(fruit[3:])			# de, 3이상
        
# 파이썬은 음의 인덱스도 가지고 있다!
print(fruit[len(fruit)-1])		# e, 
print(fruit[-1])				# e, -1 맨 마지막 단어라는 뜻
```



- 기타

```python
# 결합 (concatenation)
'hello, ' + 'python!'		# 'hello, python!'

# 반복 (Repetition)
'hi' * 3					# 'hihihi'

# 포함 (Membership)
'a' in 'apple'				# True
'app' in 'apple'			# True
'b' in 'apple'				# False
```



- **Escape Sequence**

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|   `\n`   |     줄 바꿈     |
|   `\t`   |       탭        |
|   `\r`   |   캐리지리턴    |
|   `\0`   | 널 (null, none) |
|   `\\`   |       `\`       |
|   `\'`   | 단일인용부호(') |
|   `\"`   | 이중인용부호(") |

```python
print('Alex \'Hello\'')
# Alex 'Hello'

print('Next is enter.\nand tab\ttab')
# Next is enter.
# And tab	tab
```





## ✔️ 형 변환

> 파이썬에서 데이터 형태는 서로 변환할 수 있음
>
> - 암시적 형 변환 (파이썬 내부적으로 자료형을 변환하는 경우)
> - 명시적 형 변환 (사용자가 직접 형식에 맞는 문자열을 변환하는 경우)

- 암시적 형 변환
  - bool / numeric type (int, float, complex)
- 명시적 형 변환
  - int : str, float  → int
  - float: str, int  → float
  - str: int, float, list, tuple, dict → str





## ✔️ 컨테이너 (Container)

> 여러 개의 값을 담을 수 있는 것으로, 서로 다른 자료형을 저장할 수 있음

**컨테이너 분류**

- 시퀀스: 순서가 있음 (index로 접근, 0으로 시작)
  - 문자열 (immutable) : 문자들의 나열
  - 리스트 (mutable) : 변경 가능한 값들의 나열
  - 튜플 (immutable) : 변경 불가능한 값들의 나열
  - 레인지 (immutable) : 숫자의 나열
- 컬렉션/ 비시퀀스: 순서가 없음
  - 세트 : 유일한 값들의 모음 (중복이 있으면, 하나로 만들어 준다)
  - 딕셔너리 : 키-값들의 모음



### 👉 시퀀스 (Sequence Container)

**시퀀스형 주요 공통 연산자**

| 연산             | 결과                                                     |
| ---------------- | -------------------------------------------------------- |
| s[i]             | s의 i 번째 항목, 0에서 시작                              |
| s[i:j]           | s의 i 에서 j까지의 슬라이스                              |
| s[i:j:k]         | s 의 i 에서 j까지 스탭 k의 슬라이스                      |
| s + t            | s와 t의 이어 붙이기                                      |
| s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                            |
| x in s           | s 의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
| x not in s       | s 의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
| len(s)           | s 의 길이                                                |
| min(s)           | s 의 가장 작은 항목                                      |
| max(s)           | s 의 가장 큰 항목                                        |



**리스트(List)의 정의**

- 변경 가능한 값들의 나열된 자료형 / 대괄호 `[0, 1, 2]` 형태로 정의하며, 콤마로 구분
- 변경 가능 + 반복 가능

```python
Li = ['a', 'b', 'c', 'd', 'e', 'f']			# 리스트 생성

print(list[0])								# 리스트의 0번째 출력, a

Li[0] = 'g'									# 0번째 값 변경
print(list)									# ['g', 'b', 'c', 'd', 'e', 'f']

Li.append('h')								# .append를 이용해 리스트에 'h' 추가

Li.pop(0)									# .pop를 이용해 리스트에 'g' 삭제

len(list)		# 6

Li[2]			# 'c'

Li[3][0]		# 'd'
```



**튜플 (Tuple)**

- 불변한 값들의 나열 
- 리스트랑 똑같지만, *변경이 불가* (추가, 삭제도 불가능)



**레인지 (Range)** - 변경 불가능, 반복 가능

- 기본형 : range(n)
  - 0 부터 n-1 까지의 숫자의 시퀀스
- 범위 지정 : range(n, m)
  - n 부터 m-1 까지의 숫자의 시퀀스
- 범위 및 스텝 지정 : range(n, m, s)
  - n 부터 m-1 까지 s만큼 증가시키며 숫자의 시퀀스

```python
list(range(3))
# [0, 1, 2]

list(range(1, 5))
# [1, 2, 3, 4]

list(range(1, 5, 2))
# [1, 3]

list(range(6, 1, -1))
# [6, 5, 4, 3, 2]

list(range(6, 1, 1))
#[]
```



### 👉 비시퀀스형 컨테이너 (Associative Container)

> 세트 (Set) 와 딕셔너리 (Dictionary)가 있다

**세트 (Set)**

- 유일한 값들의 모음
- 순서가 없고, 중복된 값은 하나로 만들어진다

```python
{1, 2, 3, 1, 4}				# {1, 2, 3, 4} 중복 값인 1을 제거
set(1, 2, 3, 1, 4)			# {1, 2, 3, 4}, set()를 통해서도 세트를 생성할 수 있다
-----------------------------------------------------------------------------

numbers = {1, 2, 3}
numbers.add(7)				# 숫자를 .add 를 통해 추가할 수 있다
numbers. remove(1)			# .remove를 통해 값을 뺄 수 있다
#{2, 3, 7}

len(set(numbers))			# 고유한 숫자의 개수를 확인
set(numbers)				# {2, 3, 7}
```



**딕셔너리 (Dictionary)**

- 키 (key)와 값 (value) 쌍으로 이루어진 모음
  - 키 : 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능)
  - 값 : 어떠한 형태든 관계 없음
- 키와 값은 `:` 로 구분되며, 개별 요소는 `,` 로 구분 된다

```python
student = {'Alex': 77, 'Bob': 27}
student['Alex']						# 77

#추가 및 변경
student['Alex'] = 7						# {'Alex': 7, 'Bob': 27}
student['Chris'] = 17					# {'Alex': 7, 'Bob': 27, 'Chris': 17}

#삭제
student.pop('Bob')						# .pop을 이용해 'Bob'을 삭제
student									# {'Alex': 7, 'Chris': 17}
```

