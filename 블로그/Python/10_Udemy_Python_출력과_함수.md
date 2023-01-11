# Udemy : Python 출력과 함수



## Functions with Output

```python
def my_function() :
    result = 3 * 2
    return result

my_function()
# result가 출력된다

output = my_function()
# result가 output으로 저장된다
```

- 함수를 정의하고, 함수를 사용할 때에 출력하는 값이 나오도록 만들고 싶을 때에 `return`을 사용한다





## 실습 1

> 년도와 달을 입력 받는다
>
> 년도가 윤년인지 확인하고, 해당 연도의 달에 날 수를 출력한다

```python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if is_leap(year) == True:
        month_days[1] = 29
        return month_days[month - 1]
    else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

- `is_leap()` 함수에서, 윤년인지 아닌지 확인한다
- `days_in_month()` 함수에서 윤년이면 2월을 29일로 만든 후, 입력한 달의 일 수를 출력한다
  - 반대로 윤년이 아니면 `month_days`를 그대로 사용하고, 입력한 달의 일 수를 출력한다

