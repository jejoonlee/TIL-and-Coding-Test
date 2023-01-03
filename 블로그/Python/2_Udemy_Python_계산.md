# Udemy : Python 계산, 반올림



## Calculation

```python
+
# 더하기

-
# 빼기

*
# 곱하기

**
# 제곱

/
# 나누기

//
# 나눈 후 몫 계산

%
# 나눈 후 나머지
```



#### Rounding numbers (반올림)

```python
print(round(8 / 3))
# 3

print(round(8/3, 2))
print(round(2.666666666, 2))
# 2.67

print("{:.2f}".format(33.599999))
# 원래 round를 쓰면 33.6이 나온다
# 위를 쓰게 되면 33.60이 나온다 (소수 2자리 수까지 반환하는 것)
```



#### f-string 사용하기

```python
# f 를 문자열 앞에다가 쓰고 난 후, 문자열 외에 다른 종류 (정수 같이)를 써야 한다면 {} 안에 넣는다

name = "제준"
age = 26

print(f"내 이름은 { name }이고, { age }살이야")
# output : 내 이름은 제준이고, 26살이야
```



#### 실습

```python
print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

split = input("How many people to split the bill? ")

total = (float(total_bill) * ((100 + int(percentage)) / 100)) / int(split)
total = "{:.2f}".format(total)

print(f"Each person should pay : ${ total }")
```

- 총 금액, 팁 그리고 인원 수를 가지고 계산하는 코드다
  - 총 금액은 float, 실수로
  - 팁은 퍼센트다
- `input`을 통해 숫자들을 입력을 받는다
- 그리고 `total` 변수에 최종 금액을 저장하는데, `"{:.2f}".format(total)`를 통해서 소수 2자리 수까지 반올림한다

