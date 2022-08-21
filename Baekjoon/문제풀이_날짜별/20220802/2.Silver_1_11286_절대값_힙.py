import heapq

T = int(input())

nums =[]
heap = []

for t in range(T):
    num = int(input())
    nums.append(num)

for n in nums:
    if n != 0:
        heapq.heappush(heap,(abs(n), n))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])