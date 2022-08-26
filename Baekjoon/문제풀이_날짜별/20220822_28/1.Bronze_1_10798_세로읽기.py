import sys
sys.stdin = open('input.txt')

def pprint(lst):
    for row in lst:
        print(row)

words = [[False] * 15 for _ in range(5)]

for i in range(5):
    word = list(input())
    for j in range(len(word)):
        words[i][j] = word[j]

for r in range(15):
    for c in range(5):
        if words[c][r] == False:
            continue
        else:
            print(words[c][r], end ='')