import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {items.letter : items.code for index, items in data.iterrows()}

user_word = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in user_word if nato_dict[letter]]

print(result)