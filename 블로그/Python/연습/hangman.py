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