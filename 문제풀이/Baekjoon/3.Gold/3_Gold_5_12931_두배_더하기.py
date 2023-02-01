
# 메인은 A에서 B를 만드는게 아니라 B에서 A를 만드는 것
# 즉 B에서 모든 수를 0으로 만드는게 제일 중요하다

import sys
sys.stdin = open("input.txt")

N = int(input())
B = list(map(int, input().split()))
count = 0

temp = [0] * N


while sum(B) != 0:
    command = "multiply"
    for i in range(N):
        if B[i] % 2 != 0:
            command = "add"
            break
        else:
            temp[i] = B[i] // 2
    
    if command == "multiply":
        B = temp
        temp = [0] * N
        count += 1
    else:
        for i in range(N):
            if B[i] % 2 != 0:
                B[i] -= 1
                count += 1

print(count)