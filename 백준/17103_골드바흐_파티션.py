
import sys
import math

prime = [0] * 1000001
prime[0], prime[1] = 1, 1
for i in range(2, int(math.sqrt(1000001)) + 1):
    for j in range(i + i, 1000001, i):
        if prime[j] == 0:
            prime[j] = 1

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    count = 0

    for i in range(2, (n//2) + 1):
        if prime[i] == 0:
            if i * 2 == n: count += 1
            elif prime[n - i] == 0: count += 1

    print(count)