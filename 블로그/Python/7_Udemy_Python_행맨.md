# Udemy : Python 행맨 프로젝트

> 행맨은 알파벳을 입력하면서, 단어를 찾아내는 것이다.
>
> 알파벳을 고를 수 있는 차례는 주어져 있다

<img src="7_Udemy_Python_행맨.assets/dominatehangman-1600-768x384.jpg" alt="dominatehangman-1600-768x384" style="zoom:50%;" />



```python
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

word = random.choice(word_list)

result = ["_"] * len(word)
letter_choice = []
count = 6
flag = False

while count != 0:
    letter = input("Guess a letter: ").lower()

    if letter.isalpha():
        if letter in word:
            if letter not in letter_choice:
                letter_choice.append(letter)
            else:
                print("You have already chosen the letter")
            
            for i in range(len(word)):
                if letter == word[i]:
                    result[i] = letter
        else:
            if letter not in letter_choice:
                letter_choice.append(letter)
                count -= 1
                print(stages[count])
            else:
                print("You have already chosen the letter")
        
        if "_" not in result:
            flag = True
            break
    else:
        print("Please type a letter")
    
    result_show = ' '.join(result)
    print(result_show)

if flag == False:
    print(f"Answer was {word}")
    print("Game Over")
else:
    print("You win!")
```

- 문자 리스트에서 랜덤으로 유저가 맞춰야 할 문자를 가지고 온다
- while문을 돈다. 여기서 유저가 6번 안에 문자를 못 맞추면, while문이 끝나게 된다
  - 유저는 문자를 입력을 해야 한다
  - 그리고 문자를 중복으로 입력을 하면 안 된다
  - 입력한 문자가 맞춰야 하는 단어에 포함되어 있으면, 어디에 그 문자가 들어가는지 보여준다 (`result`)
  - 6번 이내에 맞출 경우, `result`에 "_" 가 없다는 것이다.
    - 그때 while문을 빠져나간다
- `flag`를 통해 유저의 성공 여부를 알려준다
