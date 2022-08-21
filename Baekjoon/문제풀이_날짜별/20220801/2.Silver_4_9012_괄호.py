
import sys
sys.stdin = open('input.txt', 'r')

# num = int(input())

# for n in range(num):
#     sum = 0
#     VPS = list(input())
#     for vps in VPS:
#         if vps == '(':
#             sum += 1
#         elif vps == ')':
#             sum -= 1
#         elif sum < 0:
#             print('NO')
#             break
#     if sum == 0:
#         print('YES')
#     elif sum == 0:
#         print('NO')


num = int(input())

for n in range(num):
    stack = []
    brk = input()
    for b in brk:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')