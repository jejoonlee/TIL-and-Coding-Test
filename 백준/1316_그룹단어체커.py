
num = int(input())

count = 0

for _ in range(0, num):
    word = input()

    wordDict = {}

    i, flag = 1, True

    wordDict[word[0]] = True

    while i < len(word):

        if word in wordDict and word[i] == word[i - 1]:
            continue
        elif word[i] != word[i - 1] and word[i] in wordDict:
            flag = False
            break
        elif word not in wordDict and word[i] != word[i - 1]:
            wordDict[word[i]] = True
        
        i += 1

    if flag: count += 1

print(count)