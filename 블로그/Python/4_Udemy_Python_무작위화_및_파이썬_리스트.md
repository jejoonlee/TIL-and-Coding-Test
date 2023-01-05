# Udemy : Python 모듈 / 리스트



## Module, 모듈이란?

> 차를 생성할 때, 한 사람이 차 한대를 혼자 만들지 않는다
>
> 각 사람들이 부품 별로, 차의 부품들을 생성을 해서, 하나의 차를 만든다
>
> 이처럼, 개발을 할 때에, 한 프로젝트의 Module, 모듈은 차의 부품이라고 생각하면 된다
>
> - Module의 사전적 의미는, 소프트웨어 묘듈 프로그램의 기능을 독립적인 부품으로 분리한 것이 모듈이라고 한다



#### Random 모듈 사용하기

> 무작위로 동전의 앞면, 또는 뒷면을 출력하기

```python
import random

coin = ["Heads", "Tails"]

print(random.choice(coin))
```

- `import random` 을 통해서 `random`이라는 모듈을 가지고 온다



> 그 외에 무작위로 숫자 뽑기

```python
import random

random_integer = random.randint(1, 10)
# 무작위로 1과 10에 있는 숫자를 출력한다

random_float = random.random() * 5
# 0 < random_float < 5 : 사이의 모든 실수를 출력한다
```



## 리스트 (List)

> #### 리스트는 데이터 구조이다
>
> #### 리스트는 여려 개의  데이터를 저장하는 것이다

`names = ["Alex", "Lee", "Jay", "Joon"]`

- 리스트는 `[ ]` 안에 데이터가 들어가야 한다



```python
# index    0       1      2      3
names = ["Alex", "Lee", "Jay", "Joon"]

print(names[0])
# Output : Alex
# names의 [] 안에 리스트 안에 몇 번째 데이터를 출력하고 싶은지 넣는다
# 리스트는 0부터 숫자를 센다

print(names[-1])
# Output : Joon
# 음수를 쓰면 맨 뒤에서 부터 데이터를 구한다

names[1] = "Je Joon"
print(names[1])
# Output : Je Joon
# names[1] = "Je Joon" 을 통해서 "Lee"의 값을 바꿔서, "Je Joon"을 출력한다
```



`list_1.extend( list_2 )` : list_1에 list_2를 넣는다



## 누가 계산해야 할까요?

> random의 `.choice()`를 사용 안 하고 코드를 짜기

```python
import random

names_string = input("Give me everybody's names, separated by a comma. ")

# .split(", ") 을 통해 comma가 있으면, 이름들을 각자의 데이터로 넣어준다
names = names_string.split(", ")

# 입력된 이름들의 개수를 찾는다
names_length = len(names)

# 리스트는 0부터 시작한다. 즉 0부터 입력된 이름들의 개수 사이의 번호를 찾는다
# names_length - 1 을 한 것은, 리스트는 0부터 숫자를 세기 때문이다
result = random.randint(0, names_length - 1)

# 그 번호는 인덱스로, 리스트의 몇 번째 이름인지 알 수 있다
final = names[result]

print(f"{ final } is going to buy the meal today!")
```



## 이중 리스트

> 숫자를 입력하면, 그 위치에 "X"를 넣는다
>
> 32를 입력하면, column 3 / row 2 에 "X"를 넣는 것이다

![img](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

```python
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")

# position은 문자열이라서 인덱스로 값을 가지고 올 수 있다
# 그 값을 가지고 와서 1을 빼준다
# 이유는 리스트는 0부터 숫자를 세기 때문이다
map[int(position[1]) - 1][int(position[0]) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
```



## 컴퓨터와 가위바위보

> 컴퓨터의 결과만 `random`으로 뽑아낸 후, if문을 통해 내가 고른 결과와 비교하기만 하면 된다!

```python
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

flag = True

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

RPS = [rock, paper, scissors]

computer = int(random.randint(0, 2))

if user == 0:
    if computer == 0:
        result = "Draw!"
    elif computer == 1:
        result = "You lose :("
    else:
        result = "You win! XD"

elif user == 1:
    if computer == 0:
        result = "You win! XD"
    elif computer == 1:
        result = "Draw!"
    else:
        result = "You lose :("

elif user === 2:
    if computer == 0:
        result = "You lose :("
    elif computer == 1:
        result = "You win! XD"
    else:
        result = "Draw!"

else:
	flag = False
    print("You typed in invalid number. You lose!")

if flag == True:
    print(RPS[user - 1])
    print("Computer choose:")
    print(RPS[computer])
    print(result)

```





