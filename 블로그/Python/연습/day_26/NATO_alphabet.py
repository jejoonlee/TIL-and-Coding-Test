import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {items.letter: items.code for index, items in data.iterrows()}


while True:
    user_word = input("Enter a word: ").upper()

    try:
        result = [nato_dict[letter] for letter in user_word if nato_dict[letter]]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(result)
        break
