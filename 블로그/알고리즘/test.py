import sys
sys.stdin = open("input.txt")

import heapq

array = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(array) != 0:
            print(heapq.heappop(array)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(array, (abs(num), num))