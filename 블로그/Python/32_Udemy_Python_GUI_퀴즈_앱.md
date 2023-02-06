# Udemy : 파이썬 API / HTML unescape / datatype



## HTML unescape

> #### 데이터 안에 기호들을, 읽지 못 할 때에, 특정 코드로 기호들을 표시한다
>
> #### 그 특정 코드를 기호로 다시 바꾸고 싶을 때에 HTML의 unescape 메서드를 사용한다



#### `&amp;`를 `&`로 바꾸기

```python
import html

html.unescape("Kim &amp; Lee")
```



## Datatype 설정하기

> 변수마다 데이터를 저장할 때에, 각 원소마다 정수, 문자열, 불리언 등으로 설정을 직접했다
>
> 미리 변수에 데이터 타입을 설정을 하여, 변수 안에 데이터를 저장할 수 있

```python
age: int
name: str
height: float
is_human: bool
```

- `age`는 모두 int가 된다
- `name`은 모두 str 형태로 입력해야 한다
- `height`은 모두 float 형태로 입력해야 한다
- `is_human`은 모두 bool 형태로 입력해야 한다



```python
def police_check(age:int):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

police_check(12)
# False
police_check("twelve")
# Error
```

- 위처럼 (age:int)를 넣으면, argument에 정수가 들어올 것을 예상한다



```python
def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
```

- `def police_check(age:int) -> bool:`  :  `-> bool`은 `return` 값이 불리언이라는 것을 미리 설정을 하는 것이다
  - 즉 코드를 짜는데, return값이 불리언이 안 나오면, 에러가 뜨게 된
