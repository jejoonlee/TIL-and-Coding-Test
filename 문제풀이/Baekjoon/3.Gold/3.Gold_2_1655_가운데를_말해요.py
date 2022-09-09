import sys
sys.stdin = open('input.txt')

import math
import sys
import heapq

N = int(sys.stdin.readline())
array = []
heapq.heapify(array)

for _ in range(N):
    x = int(sys.stdin.readline())

    num = (len(array) / 2)
    mid = math.ceil(num) - 1

    heapq.heappush(array, x)




    print(array[mid])