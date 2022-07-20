# 📋 Python OOP

### Category

[Object Oriented Program](#%EF%B8%8F-object-oriented-program)

[OOP 기초](#%EF%B8%8F-oop-기초)

- [init](#init)
- [Object Methods](#object-methods)
- [Self](#self)
- [Modify](#modify)
- [Delete](#delete)
- [객체 비교하기](#객체-비교하기)

[로또](#%EF%B8%8F-로또)

[클래스(Class)](#%EF%B8%8F-클래스-class)

[메서드 Method](#%EF%B8%8F-메서드-method)

[객체 지향의 핵심개념](#%EF%B8%8F-객체-지향의-핵심개념)



## ✔️ Object Oriented Program

> 파이썬은 객체지향 프로그램이다.
>
> 객체지향 프로그램 (Object Oriented Program, OOP)
>
> 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그램 방법

객체 (Object)는 **특정 타입 (Class)**의 **인스턴스 (Instance)**이다.

- 🚨🚨**객체는 속성과 메서드가 존재한다**🚨🚨



파이썬은 거의 모든 것이 **속성(Properties)과 메서드(Method)를 포함한 객체(Object)**이다

- **객체의 특징**
  - 타입 (Type) : 어떤 연산자 (operator)와 조작 (method)이 가능한가?
  - 속성 (Attribute) : 어떤 상태 (데이터)를 가지는가?
  - 조작법 (Method) : 어떤 행위 (함수)를 할 수 있는가?
    - 타입에 따라 속성과 조작법이 존재



#### 속성

```python
class Person:		# 클래스 'Person'으로 정의
    pass
p1 = Person()		# 인스턴스 생성
p1.name = '홍길동'	  # 인스턴스 속성
print(p1.name)
# 홍길동
```

#### 메서드

```python
class Person:
    species = '사람'		# species는 클래스의 변수
    
    def greeting(self):		# 인스턴스 메서드
        print('안녕하세요!')  #인스턴스가 활용할 메서드

Yang = Person()			# () 메서드 호출
Yang.greeting()			# 메스드 실행 (인스턴스를 통해)

print(Person.species)
```





### 예시)

#### List : 클라스

#### [1, 2, 3] : instance (인스턴스)

#### [1, 2, 3].sort() : .sort() 는 메서드(Method)



## ✔️ OOP 기초

> A Class is like an object constructor, or a 'blueprint' for creating objects. (w3schools)
>
> 클라스는 객체 제작자 또는 객체를 만드는 블루프린트 같다.

- **객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성한다**

  - 클래스 : 객체들의 분류 (Class)

  - 인스턴스 : 하나하나의 실체 / 예 (Instance)
    - 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스, 즉 '값'이다



클래스를 정의할 때는 CamalCase를 쓴다. ex) MyFavTeam

```python
# x라는 속성(Properties)을 가진 클래스를 생성
class MyFavNum:
    x = 7
    
print(MyFavNum)		# <class '__main__.MyFavNum'>

# create_obj 라는 인스턴스를 만들고, 'x'의 값을 출력한다
create_obj = MyFavNum()
print(create_obj.x)		# 7
```

- 속성: 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터의 의미



### init

- **모든 클래스**들은 `__init__()` 이라는 기능이 있고, 제일 처음 클래스를 실행할 때 쓴다

```python
# 'Person'이라는 class를 생성하고, __init__() 기능을 사용해 'name'과 'age'의 값들을 부여한다

class Person:
    def __init__(self,name,age):
        self.name = name	# 인스턴스 변수 정의
        self.age = age

p1 = Person('Alex', 26)		# 인스턴스 생성

print(p1.name)		# Alex
print(p1.age)		# 26
```



### Object Methods

- 객체들은 method도 포함 할 수 있다
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- **호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨**

```python
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
# 메서드 (Method) 생성하기
    def myfunc(self):
        print('My English name is ' + self.name)

p1 = Person('Alex', 26)
p1.myfunc			# My English name is Alex
```



### Self

- `self` 파라미터는 현재 class의 instance이다 / 인스턴스 자기자신
- 호출하는 instance를 파이썬 내부적을 전달해줌 (내부적으로는 다른 형태)
  - 모든 인스턴스 메서드 중, 첫 번째 self를 넘겨준다라는 약속이 되어 있음

- class에 속한 변수를 이용하는데 쓰인다

```python
class Person:
    def __init__(self,name,age):
    # 개별 인스턴스에 각각 name과 age 속성을 지정
        self.name = name
        self.age = age
    
    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달
    def myfunc(self)	
    	print('My English Name is' + self.name)
		# self.name: 인스턴스(self)의 이름(name)

# 인스턴스 만드는 것
p1 = Person('Alex', 26)
p1.myfunc		# My English Name is Alex
```



### Modify

- 속성들을 수정할 수 있다

```python
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(abc)		
    	print('My English Name is' + abc.name)

p1 = Person('Alex', 26)

p1.age = 27	# 26에서 27로 age 값을 바꾸기		
```



### Delete

- `del` 을 이용해서 객체의 속성 또는 객체 자체를 삭제할 수 있다

```python
del p1.age 		# p1의 age(나이) 삭제
del p1			# p1 자체를 삭제
```



### 객체 비교하기

- `==` : 동등한(equal) / 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
- `is` : 동일한(identical) / 두 변수가 동일한 객체를 가리키는 경우 True

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)
# True, False / 두 변수에 값들의 내용은 같지만, 다른 객체를 가리키고 있다
--------------------------------------------------------------
a = [1, 2, 3]
b = a
print(a == b, a is b)
# True, True / 두 변수이 값도 같고, 같은 객체를 가리키고 있음
# b는 a라는 변수의 객체를 가리키고 있다
```





## ✔️ 로또

```python
import random 

for i in range(5):		# 5번 반복
    numbers = range(1, 46)	# 1 ~ 45번까지
    result = random.sample(numbers, 6) 
    # result는 6개의 랜덤 번호
    result.sort() 
    print(result)
```



#### lotto_function.py 라는 로또 뽑는 함수를 만든 파일

- 이 파일에서 `generate_lotto(n)`는 n번만큼의 로또 번호들을 출력해준다

```python
import random 

# n을 넣으면 그 횟수만큼 반복해준다 
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1, 46)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
    return result

# 내가 산 번호와, 결과가 맞아 떨어진 여부를 알려주는 함수
def check(buy_numbers, result_numbers):
    return 0

# print(generate_lotto(5))
```

```python
import lotto_function
# lotto_function에서 generate_lotto(n)이란 함수와
# check 이라는 함수를 가지고 왔다
			  # 로또 번호들의 리스트
buy_numbers = lotto_function.generate_lotto(5)

lotto_function.check(buy_number, [1, 2, 3, 4, 5, 6])
```

- input을 넣으면 output 밖에 못 한다



#### 클래스를 이용한 로또 추첨기

```python
import random

class Lotto: 
    name = '로또추첨기'

    def generate_lotto(self):
        self.numbers = sorted(random.sample(range(1, 46), 6))

    def get_money(self, real_numbers):
        print('당신의 숫자는', self.numbers)
        print('당첨 숫자는', real_numbers)
        if self.numbers == real_numbers:
            return 10000000000
        else:
            return 0

lotto = Lotto()
lotto.generate_lotto()
print(lotto.numbers)	# 로또 랜덤 번호 출력
```

```python
import lotto_class

lotto = lotto_class.Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1, 2, 3, 4, 5, 6]))
```

- 코드를 '확장'시킬 수 있음.
- `lotto`라는 인스턴스로 속성도 볼 수 있고 (numbers), 내가 생성도 하고, 확인 (get_money)도 가능하다



## ✔️ 클래스 (Class)

#### 클래스 속성 (Attribute)

- 클래스 선언 내부에서 정의
- `<classname>.<name>` 으로 접근 및 할당

```python
class Circle:
    pi = 3.14
    
c1 = Circle()

print(Circle.pi)	# 3.14
print(c1.pi)		# 3.14
```



#### 인스턴스와 클래스 간의 이름 공간 (namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색





## ✔️메서드 Method

#### 클래스 메서드 `@classmethod` `cls`

- 클래스를 호출을 할 것인데, 내부적으로 매서드 내부에 클래스 자체가 필요할 때

- 클래스가 사용할 메서드 /  `@classmethod` 데코레이터를 사용하여 정의

- 클래스를 의미하는 `cls` 매개 변수를 통해 클래스를 조작

#### 인스턴스 메서드 `self`

- 인스턴스를 호출하면서 메서드 내부에, 인스턴스가 필요할 때

- 호출한 인스턴스를 의미하는 `self` 매개 변수를 통해 인스턴스를 조작

#### 스태틱 메서드 `@staticmethod` 

- 내부적으로 클래스와 인스턴스가 필요가 없을 때에
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때, 사용
- 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨
  - 주로 해당 클래스로 한정하는 용도로 사용



```python
# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스변수'

    # 메서드들을 정의했습니다. 
    def __init__(self): 
        self.instance_variable = '인스턴스 변수'
    
    # 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
# 인스턴스 메서드 호출 (<__main__.MyClass object at 0x00000244E6E53F10>, '인스턴스 변수')
    
    # 클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable
# 클래스 메서드 호출 (<class '__main__.MyClass'>, '클래스변수')
    
    # 스태틱 메서드 정의
    @staticmethod
    def static_method():
        return '스태틱'
# 스태틱 메서드 호출 스태틱 / 아무것도 없음

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())
```





## ✔️ 객체 지향의 핵심개념

> 핵심 4가지

1. 추상화 : 어떠한 기능을 만들어 놓고, user는 아무것도 모르지만 메서드를 이요
2. 상속 : 똑같은 요소를 상속을 받아 재활용 가능
   - super() : 상위 클래스를 상송 받고, 추가 코드를 작성 가능
   - Overriding : 매서드를 덮어쓸 수 있음
3. 다향성 : 여러 모양 (메서드를 덮어쓸 수 있다)
4. 캡슐화 : 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스 차단
   1. Public Access Modifier
   2. Protected Access Modifier
   3. Private Access Modifier



