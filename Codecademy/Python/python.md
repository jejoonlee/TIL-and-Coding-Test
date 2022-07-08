# 📝 Python 



## ✔️ Category

[Comment](#comment)

[Print](#print)

[Variables](#variables)

[Error](#error)

[Number](#number)

[Calculation](#calculation)

[Concatenation](#concatenation) 문자열 접합



## ✔️ Content



#### Comment

```python
# Here computer will ignore texts written in the program. This is called comment used with '# hashtag'
```



#### Print

```python
print('Hello World!')		# 'Hello World!' will be printed.
```

- `print()` function is used to tell a computer to talk



#### Variables

```python
have_a_good_day = 'sunny_day'
print='have_a_good_day'

# this will print 'sunny_day'
```

- We assign variables by using `=` 



#### Error

> When there is an error `^` character will point to the location of the error
>
> `SyntaxError` : something wrong with the way program is written 
>
> `NameError` : word it does not recognize



#### Number

> `int`, integer, contains all numbers without decimal points
>
> `float`, float, can be used for fractional quantities (decimal) as well as precise measurements (1~10)



#### Calculation

> `+` `-` `*` `/` 
>
> `**` exponent (제곱) 		ex) 2^3 → print(2 ** 3)
>
> `%` Modulo Operator (remainder of a division calculation) / 나눈 이후 남는 숫자

```python
print(25 * 2)
	# prints '50'
    
print(25 * 2 + 5)
	# prints '55'
```

```python
A = 1.5
B = 2
print(A * B)
	#prints '3'
```

```python
#제곱
print(2 ** 3)
	# prints '8' which is 2*2*2
```

```python
#modulo operator
print(11 % 2)
	# prints '1' → 11 나누기 2는 5---1, 1이 남아서 '1'이 출력된다
    
my_team = 27 % 4
print(my_team)
	# prints '3'
```



#### Concatenation

```python
string1 = 'I love football.'
string2 = 'I play football every week.'
string3 = 'My position is winger'

message = string1 + " " + string2 + " " + string3

print(message)
# prints 'I love football. I play football every week. My position is winger'
```

- `" "` 사이에 공간을 만들어준다. (spacebar 같은 기능). 아니면 변수에 마지막에 공간을 준다.



```python
string1 = 'I love '
string2 = 'lucky number '
number = '7'

message = string1 + string2 + str(number)
# message를 변수로 두는 경우 숫자를 문자열로 만들어야 한다. 그래서 str(number) 가 있는 것

print(message)
# prints 'I love lucky number 7'

-----------------------------------------------------------------------------------------------------------

# message 변수가 없는 경우, 숫자를 문자열로 안 만들어도 됨

string1 = 'I love '
string2 = 'lucky number '
number = '7'

print(string1, number, string2)
```





