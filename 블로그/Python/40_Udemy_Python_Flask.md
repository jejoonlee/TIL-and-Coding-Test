# Udemy : Python Flask / 터미널 명령어 / `__name__` `__main__`

*Udemy Python*



## Flask

> #### 파이썬 기반 프레임워크다
>
> #### 장고보다 소규모의 웹 개발을 할 때에 사용한다



### 백엔드

- 클라이언트, 서버, DB, 세 요소가 맞물려 백엔드를 작동시킨다
- **클라이언트**
  - 브라우저를 이용하는 사용자
- **서버**
  - 사용자의 요청 사항을 받을 준비가 되어 있는 곳
- **DB**
  - 사이트의 모든 정보를 담아두는 곳이다



> #### 즉 클라이언트에서 서버로 요청을 보낸다
>
> #### 서버에서 클라이언트가 요청한 데이터를 찾아서 클라이언트에 응답을 해준다



## Flask 시작하기

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```



#### Flask를 다운로드 받기

- `pip install Flask`



#### Flask를 통해 웹 실행하기

`flask --app hello run`

- 여기서 `hello`는 앱의 이름, 즉 `hello.py`





## 명령어 (터미널)

```terminal
pwd
# print working directory / 현재 경로를 찾아주는 것

ls
# list / 현재 위치에 있는 폴더와 파일을 보여준다

cd '폴더 이름'
# change directory / '폴더 이름'으로 들어가는 것

cd ..
# change directory .. / 현재 위치 전으로 가는 것

cd ../..
# 현재 위치 전, 전 위치로 가는 것

mkdir '폴더 이름'
# make directory / 폴더를 생성하는 것

touch '파일명'
# 새로운 파일을 생성하는 것

rm '파일명'
# 파일을 삭제하는 것

rm -rf '폴더명'
# 폴더를 삭제하는 것
```





## `__name__` & `__main__`

> #### `if __name__ = "__main__"`



#### hello.py

```python
def hello(name):
    return f'hello {name}'
    
print(hello("Alex"))
# hello Alex
```



#### index.py

```python
import hello

print(hello.hello("Jay Jay"))
# hello Alex
# hello Jay Jay

print(__name__)
# __main__

print(hello.__name__)
# hello
```

- `hello` 모듈, 파일을 import 했다
- 근데 `hello.py`에는 함수, `def hello(name)` 만 있는 것이 아닌 프린트 메서드까지 있다
- 즉 `index.py`에서 `hello()` 메서드를 실행했을 때에, `hello.py`에서의 프린트와, `index.py`의 프린트가 출력이 된다



#### hello.py

```python
def hello(name):
    return f'hello {name}'

if __name__ == "__main__":
	print(hello("Alex"))
    
print(__name__)
# __main__
```

- `hello.py` 에 `if __name__ == "__main__":`를 넣어주면, 다른 파일에서, `hello.py`를 import 해서 `hello(name)`을 사용할 때에, `hello.py`에서 출력한 `print(hello("Alex"))`은 빼낸다
- 즉 `hello.py`의 `if __name__ == "__main__":`는, `hello.py` 내에서만 해당 메서드를 실행했을 때에, 실행시켜 준다





## 파이썬 데코레이터

> #### 함수는 특정한 기능과 입출력을 가질 수 있다
>
> #### 일급 객체로서 인자로 전달될 수 있다
>
> #### 다른 함수 안에 중첩될 수 있다
>
> #### 다른 함수의 출력으로 반환될 수 있다



### 함수 안에  함수가 중첩된 것

```python
def outer_function():
    print("I'm outer")
    
    def inner_function():
        print("I'm inner")
        
    inner_function()
    
outer_function()

# I'm outer
# I'm inner
```



### 파이썬 데코레이터

```python
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("bye")

def say_greeting():
    print("How are you?")
    
say_hello() # 2초 뒤에 Hello가 출력된다
say_greeting() # 바로 How are you?가 출력된다
```

- `@delay_decorator`를 함수 위에 넣는다 그러면, 그 함수는 `delay_decorator`의 `function()`이 되는 것이



```python
import time

def speed_calc_decorator(function):
  def wrapper_function():
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'run time: {end_time - start_time}s')
  return wrapper_function
  

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
```









