import sys
sys.stdin = open('input.txt', 'r')

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = A[::-1]
B = B[::-1]
# 총 점수를 구하는 것이면 상관이 없는데
# 비긴 후, 마지막으로 큰 수를 정해서 이기는 사람을
# 정해야 해서, A와 B 숫자들을 돌려준다

A_s = 0
B_s = 0

for i in range(10):
    if A[i] > B[i]:
        A_s += 3        
    elif A[i] < B[i]:
        B_s += 3
    else:
        A_s += 1
        B_s += 1
        
if A_s > B_s:
    print(A_s, B_s)
    print('A')
elif A_s < B_s:
    print(A_s, B_s)
    print('B')


for i in range(10):
    if A_s == B_s:
        if A[i] > B[i]:
            print(A_s, B_s)
            print('A')
            break
        elif A[i] < B[i]:
            print(A_s, B_s)
            print('B')
            break
        elif A == B:
            print(A_s, B_s)
            print('D')
            break
