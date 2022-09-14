# 📝 Python (Basic 2)



## ✔️ Category

[Boolean Expressions](#boolean-expressions)

[Relational Operators](#relational_operators)

[Boolean Variables](#boolean-variables)

[If Statement](#if-statement)

[Relational Operators II](#relational-operators-ii)

[Boolean Operators: and](#boolean-operators-and)

[Boolean Operators: or](#boolean-operators-or)

[Boolean Operators: not](#boolean-operators-not)



## ✔️ Content



#### Boolean Expression

> It is a statement that can either be `true` or `false`
>
> ex) Dogs are Mammal (O Boolean Expression)
>
> ex) Dogs are cute (X Boolean Expression)



#### Relational Operators 

> Compare two items and return either `True` or `False` 
>
> `==` : equal
>
> `!=` : not equal

```python
1 == 1		# 1 is equal to 1 (True)
2 != 4      # 2 is not equal to 4 (True)
3 == 5		# 3 is equal to 5 (False)
'7' == 7	# '7' is equal to 7 (False, '7' is a string while 7 is integer)
```





#### Boolean Variables

> `True` and `False` appear different color to strings or other variables
>
> This is because they are special type of `bool` (The only `bool` types)

```python
set_to_true = True
set_to_false = False
# True and False have different color

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
# These are variables that contain 'Boolean Values'
print(bool_one)    # True
print(bool_two)    # False
print(bool_three)  # True
# If printed, these variables will only reference  'True' or 'False' 
-------------------------------------------------

my_baby_bool = 'true'
print(type(my_baby_bool)) 
# <class 'str'> will be printed

my_baby_bool_two = True
print(my_baby_bool_two)
# if 'type' is included, <class 'bool'> will be printed
# for this variable, 'True' will be printed
```





#### If Statement

```python
if is_raining:
	print('bring an umbrella')
# 'If it is raining, then bring an umbrella'
# ':'  tells the computer what's coming next is what should be exectued if the condition is met
-------------------------------------------------

if 2 == 4 - 2:
    print('Double')
# 'Double' will be printed because statement '2 == 4 - 2' is TRUE
# If it is FALSE, 'Double' will not be printed
```





#### Relational Operators II

```python
if age <= 13:
    print('Sorry, parental control required')
# If age is 13 or less, print 'Sorry, parental control required'
-------------------------------------------------

credits = 125

if credits >= 120:
  print('You have enough credits to graduate!')

if credits < 120:
  print('You have failed to graduate...')

# Since the credit earned is more than 125, it will print 'You have enough credits to graduate'
```





#### Boolean Operators: and

> `and` : two boolean expressions need to be `TRUE` to be `TRUE`, otherwise all `FALSE`

```python
(1 + 1 == 2) and (2 + 2 == 4)   
# True (both TRUE)
 
(1 > 9) and (5 != 6)            
# False (only one is TRUE)
 
(1 + 1 == 2) and (2 < 1)        
# False (only one is TRUE)
    
(0 == 10) and (1 + 1 == 1)      
# False (both are FALSE)
-------------------------------------------------

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
# Since both standards were met, it will print 'You meet the requirements to graduate!' 
```





#### Boolean Operators: or

> `or` : if one or both of the expressions are TRUE, it is TRUE

```python
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False
--------------------------------------------------

credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >= 2.0):
  print('You have met at least one of the requirements.')
# Since one of the following standard is met, it will print 'You have met at least one of the requirements'
```





#### Boolean Operators: not

> `not` when applied to boolean expression, it reverses the value

```python
not True == False
not False == True

not 1 + 1 == 2  
# False

not 7 < 0       
# True (7<0 is FALSE, if you reverse this with 'not' operator, it is TRUE)
```





### Else Statements

> `else` statements allow us to elegantly describe what we want our code to do when certain conditions are not met
>
> It always appear in conjunction with `if` statement

```python
if a <= 5 :
    print('low')
else:
    print('high')
    
# if 'a' is lower or equal to 5, print 'low'
# else, 'a' is greater than 5, print 'high'
```

