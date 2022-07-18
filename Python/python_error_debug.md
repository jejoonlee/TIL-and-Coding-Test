# 📋Python Error, Debug

[Debugging](#%EF%B8%8F-debugging)

[Error](#%EF%B8%8F-error)

- [Syntax Error](#syntax-error)
- [TypeError](#typeerror)
- [ValueError](#valueerror)
- [IndexError](#indexerror)
- [KeyError](#keyerror)
- [ModuleNotFoundError](#modulenotfounderror)
- [ImportError](#importerror)
- [IndentationError](#indentationerror)
- [KeyboardInterrupt](#keyboardinterrupt)

[예외 처리](#%EF%B8%8F-예외-처리)



## ✔️Debugging

> branches : 모든 조건이 원하는대로 동작하는지
>
> for loops :  반복문에 진입하는지, 원하는 횟수만큼 실행되는지
>
> while loops : for loops와 동일, 종료조건이 제대로 동작하는지
>
> function : 함수 호출시, 함수 파라미터, 함수 결과

- `print` 함수 활용
  - 나눠서 print를 활용해서, 코드가 작동하는지 확인한다. (ex. 특정 함수 결과, 반복/ 조건 결과 등 section을 나눠서 확인)
- 개발 환경 (text editor, IDE)에서 제공하는 기능 활용
- Python Tutor 활용
- 스스로 코드를 읽어보고 해결해보기



## ✔️Error

### Syntax Error

- 문법에러 때문에 프로그램이 실행하지 않는다
  - '^' 를 통해 에러의 위치를 알 수 있다
    - EOL (End of Line) / EOF (End of File)
    - Invalid Syntax : 문법이 아예 없을 때
    - assign to literal : 변수의 이름 자체가 value일 경우 (5 = 3 에서 5는 변수 이름으로 사용 못 한다) 
- Exception : 실행 중 감지되는 에러들을 예외(exception)이라고 한다
  - ZeroDivisionError : 0으로 나눌때 나타나는 에러 (0으로 나눌 수 없음)
  - NameError : 선언이 되지 않은 변수를 썼을때



### TypeError

- 타입이 불일치 할 때  / ` 1 + '1'`   `1`은 int고, `'1'`은 string이다
- arguments가 부족할 때 or 개수가 초과할 때



### ValueError

- 타입은 올바르나 값이 적절하지 않을 때

```python
int('3.5')
# '3.5'는 float를 써야 한다
```



### IndexError

- 리스트 안에 인덱스를 잘 못 입력했을 때

```python
empty_list = []
empty_list[2]
# 아무것도 없는 리스트에서, 3번째 인덱스를 찾는건 가능하지 않다
```



### KeyError

- 딕셔너리에 key를 찾았는데, 해당 key가 없을 때

```python
club = {'manutd': '7'}
club['liverpool']
# 딕셔너리에 'liverpool' 이라는 key가 없어 찾을 수 없다
```



### ModuleNotFoundError

- 존재하지 않은 module을 import할 때

```python
import noname
# 만약 noname 이라는 module이 없으면, 모듈을 import할 수 없다고 에러사항이 뜬다
```



### ImportError

- module은 존재하나 클래스/함수가 존재하지 않을 때

```python
from random import sample
# random이라는 module은 존재하나 sample 이라는 클래스/함수가 없다
```



### IndentationError

- Indentation (뛰어쓰기/ tab)이 적절하지 않을 경우
- 위치도 알려준다



### KeyboardInterrupt

- 의도적으로 프로그램을 종료했을 때
- 주로 출력이 너무 길거나, 안 멈추면 쓴다





## ✔️ 예외 처리

> try문과 except문을 이용하여 예외 처리를 할 수 있다

- try문
  - 오류가 발생할 가능성 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- except 문
  - 예외가 발생하면, except 문을 사용

```python
try:
    num = input('숫자 입력:')
    print(int(num))
except:
    print('숫자가 아닙니다') 
# 문자열을 쓰거나, 실수를 쓰면 except문을 통해 '숫자가 아닙니다'가 출력된다
---------------------------------------------------------------------------------

try:
    num = input('숫자 입력:')
    print(int(num))
except ValueError:			
    print('숫자가 아닙니다') 
# except문에 특정 에러를 넣어서, 그 에러가 뜨면, 출력을 하게 만들 수 있다
```

