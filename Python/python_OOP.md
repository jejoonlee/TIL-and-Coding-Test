# 📋 Python OOP

### Category

[Object Oriented Program](#%EF%B8%8F-object-oriented-program)

[Class](#%EF%B8%8F-class)

- [init](#init)
- [Object Methods](#object-methods)
- [Self](#self)
- [Modify](#modify)
- [Delete](#delete)





## ✔️ Object Oriented Program

> 파이썬은 객체지향 프로그램이다.
>
> 객체지향 프로그램 (Object Oriented Program, OOP)
>
> 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그램 방법

객체 (Object)는 **특정 타입 (Class)**의 **인스턴스 (Instance)**이다.

파이썬은 거의 모든 것이 **속성(Properties)과 메서드(Method)를 포함한 객체(Object)**이다

- **객체의 특징**
  - 타입 (Type) : 어떤 연산자 (operator)와 조작 (method)이 가능한가?
  - 속성 (Attribute) : 어떤 상태 (데이터)를 가지는가?
  - 조작법 (Method) : 어떤 행위 (함수)를 할 수 있는가?
    - 타입에 따라 속성과 조작법이 존재



### 예시)

#### List : 클라스

#### [1, 2, 3] : instance (인스턴스)

#### [1, 2, 3].sort() : .sort() 는 메서드(Method)



## ✔️ Class

> A Class is like an object constructor, or a 'blueprint' for creating objects. (w3schools)
>
> 클라스는 객체 제작자 또는 객체를 만드는 블루프린트 같다.

클래스를 정의할 때는 CamalCase를 쓴다. ex) MyFavTeam

```python
# x라는 속성(Properties)을 가진 클래스를 생성
class MyFavNum:
    x = 7
    
print(MyFavNum)		# <class '__main__.MyFavNum'>

# create_obj 라는 객체를 만들고, 'x'의 값을 출력한다
create_obj = MyFavNum()
print(create_obj.x)		# 7 
```



### init

- **모든 클래스**들은 `__init__()` 이라는 기능이 있고, 제일 처음 클래스를 실행할 때 쓴다

```python
# 'Person'이라는 class를 생성하고, __init__() 기능을 사용해 'name'과 'age'의 값들을 부여한다

class Person:
    def __init__(self.name.age):
        self.name = name
        self.age = age

p1 = Person('Alex', 26)

print(p1.name)		# Alex
print(p1.age)		# 26
```



### Object Methods

- 객체들은 method도 포함 할 수 있다

```python
class Person:
    def __init__(self.name.age):
        self.name = name
        self.age = age
    
# 메서드 (Method) 생성하기
    def myfunc(self):
        print('My English name is ' + self.name)

p1 = Person('Alex', 26)
p1.myfunc			# My English name is Alex
```



### Self

- `self` 파라미터는 현재 class의 instance이다
- class에 속한 변수를 이용하는데 쓰인다

```python
class Person:
    def __init__(self.name.age):
        self.name = name
        self.age = age
        
    def myfunc(abc)		# self는 이름이 달라도 된다
    	print('My English Name is' + abc.name)

p1 = Person('Alex', 26)
p1.myfunc		# My English Name is Alex
```



### Modify

- 속성들을 수정할 수 있다

```python
class Person:
    def __init__(self.name.age):
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



