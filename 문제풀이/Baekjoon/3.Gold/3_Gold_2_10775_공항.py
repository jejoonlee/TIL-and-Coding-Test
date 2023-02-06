import sys
sys.stdin = open('input.txt')

G = int(input())
P = int(input())

gates = [False] * G
cnt = 0
flag = True

for _ in range(P):
    airplane = int(input()) - 1

    for j in range(airplane, -1, -1):
        if gates[j] == False:
            flag = True
            gates[j] = True
            cnt += 1
            break
        else:
            flag = False

    if flag == False:
        break

print(cnt)