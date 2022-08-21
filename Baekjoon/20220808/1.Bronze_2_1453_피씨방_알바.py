import sys
sys.stdin = open('input.txt', 'r')
# 피씨방에는 1부터 100까지 자리가 있다

# 사람 수


N = int(input())

# 앉고 싶은 자리의 숫자
seat = list(map(int, input().split()))

use = []
reject = 0

# s는 들어오는 순부터 순회한다
for s in seat:
    # 만약 use에 s가 없으면
    # use 리스트에 s를 저장하는 것
    if s not in use:
        use.append(s)
    # 그게 아니면 거절 변수에 1을 더한다
    else:
        reject += 1

print(reject)