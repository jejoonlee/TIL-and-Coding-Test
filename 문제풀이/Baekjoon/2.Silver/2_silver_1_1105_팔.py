import sys
sys.stdin = open("input.txt")

L, R = input().split()

cnt = 0

if len(L) != len(R):
    cnt = 0
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == "8":
                cnt += 1
        else:
            break

print(cnt)

