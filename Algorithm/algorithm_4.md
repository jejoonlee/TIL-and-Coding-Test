# 📋 Algorithm - Dictionary

[해시 테이블](#%EF%B8%8F-해시-테이블)

[딕셔너리 기본 문법](#%EF%B8%8F-딕셔너리-기본-문법)

- [파이썬 딕셔너리의 특징](#파이썬-딕셔너리의-특징)
- [딕셔너리 사용해야 할 때](#딕셔너리-사용해야-할-때)

[딕셔너리 메서드](#%EF%B8%8F-딕셔너리-메서드)

## ✔️ 해시 테이블

> 딕셔너리의 원래 이름은 해시 테이블이다
>
> 파이썬에는 딕셔너리 (dict) 자료구조가 내장 되어 있다
>
> Non-sequence & Key-Value

- **순서가 없으며, Key와 Value가 내장 되어 있다**
- **순서가 없어도 iterable 하다**
- **Key는 immutable(변경 불가능) 하다 / Value는 변경 가능**
- **Value를 찾기 위해서 Key를 입력하면 된다**



#### 해시 함수

> 임의 길이의 데이터를 고정 길이를 데이터로 매핑하는 함수
>
> https://emn178.github.io/online-tools/sha256.html
>
> 위의 사이트에 들어가서 `input` 을 넣으면 `output`이 나오는데, `input` 데이터는 아무 단어나 숫자를 `output` 에서 진수, 즉 숫자로 바꿔서 저장한다

![hash_function](algorithm_4.assets/hash_function.png)



#### 해시

> 해시 함수를 통해 얻어진 값



## ✔️ 딕셔너리 기본 문법

> 기본적인 딕셔너리 사용법 (선언)

```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
}

print(a)

# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
```



> 기본 딕셔너리 사용법 (삽입 / 수정)

```python
# 딕셔너리[key] = value
내부에 해당 key가 없으면 삽입, 있으면 수정

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
}

a['job'] = 'coach'

print(a)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul', 'job': 'coach'}
```



> 기본 딕셔너리 사용법 (삭제)

```python
# 딕셔너리.pop(key)
# 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError 발생

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
}

gender = a.pop('gender')

print(a)
print(gender) # 반환 한다

# {'name': 'kyle', 'address': 'Seoul'}
# male
```



> 기본 딕셔너리 사용법 (삭제)

```python
# 딕셔너리.pop(key, default)
# 두 번째 인자로 default(기본)값을 지정하여 KeyError qkdwl rksmd

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
}

phone = a.pop('gender', '010-1234-5678')
# 꺼낸 이후 사용이 가능하다

print(a)
print(phone)

# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
# 010-1234-5678
```



> 기본 딕셔너리 사용법 (조회)

```python
# key에 해당하는 value 반환

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
}

print(a ['name'])
# key가 없으면 error 가 뜬다
print(a.get('name'))
# key가 없으면 None으로 반환
print(a.get('name', '없음'))
# default 값을 설정해서 None 대신 '없음'이 반환 된다
```



#### 파이썬 딕셔너리의 특징

> 삽입, 삭제, 수정, 조회 `연산의 속도가 리스트보다 빠르다`

| 연산 종류   | 딕셔너리 시간복잡도 | 리스트 시간 복잡도 |
| ----------- | ------------------- | ------------------ |
| Get Item    | O(1)                | O(1)               |
| Insert Item | O(1)                | O(1) or O(N)       |
| Update Item | O(1)                | O(1)               |
| Delete Item | O(1)                | O(1) or O(N)       |
| Search Item | O(1)                | O(N)               |

- 리스트는 주로 리스트 안에 있는 값들을 각자 탐색을 해야 한다 O(N)

- 하지만 파이썬 딕셔너리는 해시로 저장되어 있어서 바로 찾을 수 있다 (index 접근)
  - 키만 찾으면 됨



#### 딕셔너리 사용해야 할 때

1. 리스트를 사용하기 힘든 경우
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우
3. 현실 세계의 대부분의 데이터를 다룰 경우



## ✔️ 딕셔너리 메서드

| 연산 종류   | 딕셔너리 시간복잡도 | 기능                                           |
| ----------- | ------------------- | ---------------------------------------------- |
| `.keys()`   | O(1)                | key들의 데이터들이 나온다 (타입 dict_keys)     |
| `.values()` | O(1)                | value들의 데이터들이 나온다 (타입 dict_values) |
| `.items()`  | O(1)                | 리스트 안에 튜플 (key, value)가 나온다         |