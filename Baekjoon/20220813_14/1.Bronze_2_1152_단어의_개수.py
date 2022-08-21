import sys
sys.stdin = open('input.txt')

# 문자열에 있는 단어 세는 것
# 딕셔너리에 넣어서 key들의 개수를 구하기!

sentence = list(input().split())

print(len(sentence))