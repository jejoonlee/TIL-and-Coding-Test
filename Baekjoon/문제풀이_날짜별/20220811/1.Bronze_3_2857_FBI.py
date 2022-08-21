import sys
sys.stdin = open('input.txt', 'r')


cops = []
# 5 명이 있다
for _ in range(5):
    cop = input()
    cops.append(cop)

FBI = []
for c in cops:
    if 'FBI' in c:
        FBI.append(c)

result = []
for F in FBI:
    result.append(cops.index(F) + 1)

if len(result) == 0:
    print('HE GOT AWAY!')
else:
    print(*result)