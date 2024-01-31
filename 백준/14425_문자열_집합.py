
import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

wordDict = {}
for _ in range(n):
    wordDict[input().strip()] = 1

result = 0
for _ in range(m):
    if input().strip() in wordDict:
        result += 1

print(result)