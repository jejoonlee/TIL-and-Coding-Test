import sys
sys.stdin = open('input.txt')

# 나이가 증가하는 순으로
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서

N = int(input())

info = []
for n in range(N):
    age, name = input().split()
    age = int(age)
    info.append([age, name])

# age 만 정렬을 하면 된다
info.sort(key = lambda x: x[0])

for i in info:
    print(i[0], i[1])