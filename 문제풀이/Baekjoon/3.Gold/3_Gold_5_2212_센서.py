import sys
sys.stdin = open('input.txt')

censor_num = int(input())
center_num = int(input())
censors = list(map(int, input().split()))
censors.sort(reverse=True)


# 설치할 수 있는 집중국이 센서보다 많거나, 같으면,
# 각 센서에게 집중국을 설치하면 된다
if censor_num <= center_num:
    print(0)
else:
    distance = [censors[i - 1] - censors[i] for i in range(1, len(censors))]
    distance.sort()

    for _ in range(center_num - 1):
        distance.pop()

    print(sum(distance))

# import heapq

# censor_num = int(input())
# center_num = int(input())
# censors = list(map(int, input().split()))

# if center_num >= censor_num:
#     print(0)
# else:
#     heapq.heapify(censors)

#     distance = []
#     temp = heapq.heappop(censors)

#     while censors:
#         current = heapq.heappop(censors)
#         heapq.heappush(distance, -(current - temp))
#         temp = current

#     for _ in range(center_num - 1):
#         heapq.heappop(distance)

#     print(-sum(distance))
