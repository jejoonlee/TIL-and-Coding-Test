word = input()

wordCount = {}

for letter in word:
    l = letter.upper()

    if l in wordCount :
        wordCount[l] += 1
    else:
        wordCount[l] = 1

answer = ''
maxNum = 0

for key, value in wordCount.items():
    if value > maxNum:
        answer = key
        maxNum = value
    elif value == maxNum:
        answer = '?'

print(answer)