# 🧑‍💻 Errors in Python

> When programs throw errors that we didn't expect to encounter, we call those errors `bugs`
>
> Programmers call the process of updating the program so that it no longer produces bugs `debugging`

[SyntaxError](#syntaxerror)

[NameError](#nameerror)

[TypeError](#typeerror)



## Common Errors

`SyntaxError` : Error caused by not following the proper structure (syntax) of the language

`NameError` : Errors reported when the interpreter detects a variable that is unknown

`TypeError` : Errors thrown when an operation is applied to an object of an inappropriate type



#### SyntaxError

> Something wrong with the way your program is written

```python
File "script.py", line 1
  print(Hello world!)
                  ^
SyntaxError: invalid syntax
# no quotation marks around 'Hello World!'
```

- The interpreter tell us where the trouble is with `^`  or by explaining file name and line number

- Some common SyntaxErrors are:
  - Misspelling a Python keyword
  - Missing colon `:`
  - Missing closing parenthesis `)`, square bracket `]`, or curly bracket `}`



#### NameError

> Reported when it detects a **variable that is unknown**

```python
File "script.py", line 1, in <module>
    print(score)
NameError: name 'score' is not defined
# there's no variable such as 'score'
```

- Some common name errors are:
  - Misspelling a variable name
  - Forgetting to define a variable



#### TypeError

> Reported when an operation is **applied to a variable of an inappropriate type**

```python
piggy_bank = '2' + 0.25
# this won't work because '2' is 'str' not 'int'
```

```python
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    piggy_bank = '2' + 0.25
TypeError: must be str, not float
# what you will get
```

