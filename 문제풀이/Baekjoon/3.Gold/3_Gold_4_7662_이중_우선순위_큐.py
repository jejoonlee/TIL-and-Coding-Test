import sys
sys.stdin = open("input.txt")
import heapq

T = int(input())

for _ in range(T):

    N = int(input())

    max_heap, min_heap = [], []
    removed = [False] * N

    for n in range(N):
        command, num = map(str, input().split())

        if command == 'I':
            heapq.heappush(max_heap, (-int(num), n))
            heapq.heappush(min_heap, (int(num), n))
            
            # True면 숫자가 max_heap, min_heap에 모두 있다는 것
            removed[n] = True

        if command == 'D':
            if num == '-1':
                # min_heap에 아이템이 있을 때에
                # removed에서 True가 있으면, min_heap에서 빼고, False로 바꾼다
                while min_heap:
                    number, index = heapq.heappop(min_heap)

                    if removed[index] == True:
                        removed[index] = False
                        break
            
            else:
                while max_heap:
                    number, index = heapq.heappop(max_heap)

                    if removed[index] == True:
                        removed[index] = False
                        break


    while min_heap and removed[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    while max_heap and removed[max_heap[0][1]] == False:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")