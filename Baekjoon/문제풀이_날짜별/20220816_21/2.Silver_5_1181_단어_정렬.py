
import sys
sys.stdin = open('input.txt')

# 길이가 짧은 것부터

# 길이가 같으면 사전 순으로

N = int(input())

words = set()
for n in range(N):
    word = input()
    words.add(word)

words = list(words)

words.sort()
words.sort(key = len)

for i in words:
    print(i)
