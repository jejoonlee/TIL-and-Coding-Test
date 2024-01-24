
num = int(input())

for _ in num:
    word = input()

    wordDict = {}

    for i in range(1, len(word)):
        if (word[i] == word[i - 1]):
            
            wordDict[word[i]] = 1