# Udemy : Python 흐름 제어와 논리 연산자



### 짝수 또는 홀수 구하기

```python
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

- 입력값을 정수로 받고, 2를 나눠준다
- 여기서 `%` 는 숫자를 나누고, 나오는 나머지를 구해준다



### BMI를 사용해서, 몸 상태를 출력하기 (elif)

```python
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / (height ** 2))

# < 18.5 
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
    
# 18 <= BMI < 25
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")

# 25 <= BMI < 30
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")

# 30 <= BMI < 35
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")

# 35 이상
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
```



#### 윤년

```python
year = int(input("Which year do you want to check? "))

if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
```

- 먼저 년도가 400을 나누었을 때, 나누어 떨어지면, **윤년**이 된다
- 400으로 나누어 떨어지지 않으면, 그 다음 `elif`문으로 넘어가 100으로 나눈다
  - 100으로 나눴을 때, 나누어 떨어지면, **윤년이 아니게** 된다
- 그리고 100으로도 나누어 떨어지지 않으면, 그 다음 `elif`문으로 넘어가 4로 나눈다
  - 4로 나누어 떨어지면 **윤년**이 된다
- 그리고 그 외에 모든 숫자들은 **윤년이 아니다**

> 윤년은 4로 나누어 떨어져야 한다
>
> 단 100으로 나누어 떨어지면 윤년이 아니다
>
> - 단 400으로 나누어 떨어지면 윤년이다



#### 선택형 계산

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    pizza = 15
    if add_pepperoni == "Y":
        pizza += 2
    if extra_cheese == "Y":
        pizza += 1

elif size == "M":
    pizza = 20
    if add_pepperoni == "Y":
        pizza += 3
    if extra_cheese == "Y":
        pizza += 1

elif size == "L":
    pizza = 25
    if add_pepperoni == "Y":
        pizza += 3
    if extra_cheese == "Y":
        pizza += 1

print(f"Your final bill is : ${pizza}.")
```

- 먼저 사이즈 별로 피자를 `if`문과 `elif`문으로 구분한다
- 그리고 각 사이즈마다 `if`문을 통해 페퍼로니를 더 추가하거나, 치즈를 더 추가하면 추가 금액을 `+=`을 통해 누적시켜준다



#### Love Calculator

> 이름에 t r u e 와 l o v e가 몇 개인지 찾는 것
>
> t r u e 의 개수는 숫자의 앞의 자리 / l o v e는 숫자의 뒷자리다

```python
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()

true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
```

- `.count()`를 통해 해당 알파벳이 단어에 몇 개가 있는지 알 수 있다
- `.lower()`를 통해 대문자를 소문자로 바꾼다



#### 선택형 게임을 만들기

```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input("Do you want to go 'left' or 'right'? ").lower()

if direction == "left":
    location = input("Select a location. 'Dessert' or 'City' ").lower()

    if location == 'dessert':
        print("Game Over. You've lost your way :(")
    elif location == 'city':
        cave = input("You found a cave! Do you go into the cave? 'Yes' or 'No' ").lower()

        if cave == "yes":
            print("Game Over. It was not a cave. It was a sink hole XD")
        elif cave == 'no':
            print("Game Over. You've been sent to jail for looking suspicious")
        else:
            print("Game Over. You didn't write correctly!")

    else:
        print("Game Over. There's only 'Dessert' and 'City' to choose!")


elif direction == "right":
    location = input("Select a location. 'Forest' or 'Lake' ").lower()

    if location == 'lake':
        print("Game Over. You've drowned :(")

    elif location == 'forest':
        cave = input("You found a cave! Do you go into the cave? 'Yes' or 'No' ").lower()

        if cave == "yes":
            print("Game Over. It started raining and you got trapped inside the cave.")
        elif cave == 'no':
            print("You have found the teasure next to the cave!")
        else:
            print("Game Over. You didn't write correctly!")

    else:
        print("Game Over. There's only 'Dessert' and 'City' to choose!")


else:
    print("Game Over. There's only 'left' or 'right' directions!")
```

- if / elif / else를 이용해서 게임을 만들기
- direction == right 면 lake 와 forest 선택권을 주기
  - lake를 선택하면 바로 게임이 끝난다
  - forest를 선택하면 동굴을 본다
    - 동굴에 들어가면 게임이 끝나고
    - 동굴에 들어가지 않으면 보물을 찾게 된다
- directoin == left 면 dessert 와 city 선택권을 주기
  - 사막에 들어가면 게임이 끝난다
  - 도시를 선택하면 동굴을 찾게 된다
    - 동굴에 들어가든, 안 들어가든 실패라고 뜬다

