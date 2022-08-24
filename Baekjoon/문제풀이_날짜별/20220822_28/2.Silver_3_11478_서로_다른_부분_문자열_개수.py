import sys
sys.stdin = open('input.txt')

word = list(input())

words = []

while len(word) != 0:
    letter = ''
    for i in range(len(word)):
        let = word[i]
        letter += let
        words.append(letter)
    word.pop(0)

print(len(set(words)))