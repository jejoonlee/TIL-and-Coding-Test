
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

words = {}

for _ in range(n):
    word = input().strip()

    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

answer = []

for key, value in words.items(): answer.append([key, value])

answer.sort(key=lambda x : (x[0]))
answer.sort(key=lambda x : (-len(x[0])))
answer.sort(key=lambda x : (-x[1]))

for a in answer:
    print(a[0])