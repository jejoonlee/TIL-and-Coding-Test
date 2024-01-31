
import sys
import math

prime = [0] * (123457 * 2)
prime[0], prime[1] = 1, 1

for i in range(2, int(math.sqrt(123457 * 2)) + 1):
    for j in range(i + i, 123457 * 2, i):
        if prime[j] == 0: prime[j] = 1

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    else:
        count= 0

        for i in range(n + 1, n * 2 + 1):
            if prime[i] == 0:
                count += 1

    print(count)