# Udemy : Python 반복문



## For 문으로 평균 구하기

```python
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
student_num = 0

for height in student_heights:
    total_height += height
    student_num += 1


print(round(total_height / student_num))
```

- `sum()` 과 `len()`을 사용하지 않고 구하기
- total_height : 학생들의 키를 구하기
- student_num : 학생들의 수를 구하기
- student_height 라는 리스트에 있는 학생들의 키를 for문으로 통해 하나씩 꺼내 더해서 total_height에 누적을 시키는 것이다



## For문으로 제일 큰 수 구하기

```python
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
```

- student_scores : 학생들의 점수를 입력을 통해 리스트로 구한다
- max_score : 학생들의 점수를 for문으로 통해 순회하면서, `max_score` 보다 큰 점수가 있으면, `max_score`에 그 점수를 저장한다



## For문과 range()를 사용해서 덧샘하기

100까지의 짝수를 모두 더하기

```python
result = 0
for i in range(2, 102, 2):
    result += i

print(result)
```

- range(2, 102, 2) : 2부터 100까지의 숫자를 가지고 온다. 대신 숫자들의 사이는 2씩 증가해야 한다.
  - 102는 포함이 안 된다



## For문 사용하기

숫자가 3으로 나누어 떨어지면 "Fizz"를 출력

숫자가 5로 나누어 떨어지면 "Buzz"를 출력

숫자가 3과 5로 동시에 나누어 떨어지면 "FizzBuzz" 출력

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```



## 비밀번호 생성하기

각 문자, 숫자, 기호의 개수를 입력받고, 입력받은 개수만큼 무작위로 문자, 숫자, 기호를 가지고 와서 비밀번호를 만드는 것

### random.sample을 이용해서, 간단하게 만든 버전

```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ---------------- 위는 공통적으로 사용 -------------------------

password_letters = random.sample(letters, nr_letters)
password_symbols = random.sample(symbols, nr_symbols)
password_numbers = random.sample(numbers, nr_numbers)

password = password_letters  + password_symbols + password_numbers
password = random.sample(password, len(password))

print(''.join(password))
```



### for문으로 만든 버전

> 입력은 위와 같음

```python
password = ""

for _ in range(nr_letters):
    password += random.choice(letters)

for _ in range(nr_symbols):
    password += random.choice(symbols)

for _ in range(nr_numbers):
    password += random.choice(numbers)

final_password = random.sample(password, len(password))

print(''.join(final_password))
```



