import sys
sys.stdin = open('input.txt')

import heapq

N, K = map(int, input().split())

treasure = []
bag = []
result = 0


for _ in range(N):
    treasure.append(tuple(map(int, input().split())))

for _ in range(K):
    bag.append(int(input()))

# 보석과 가방은 오름차순으로 정렬이 되어 있다
treasure.sort()
bag.sort()

print(bag)
print(treasure)

# 가방을 순회를 한다

# 순회하면서, 보석의 제일 첫번째 보석과 비교를 한다
# 가방에 들어갈 수 있는 보석의 무게가, 원래 보석의 무게보다 무겁거나, 같을 때, 임시 리스트에 넣는다
# 임시 리스트에 넣을 때는, 보석의 가치를 넣는다 (가치를 넣을 때는 heapq으로 넣는다)
# heapq으로 넣게 된다면 임시 리스트에 자동으로 보석의 가치가 큰것부터 나열이 된다

temp = []

for b in bag:

    while treasure and treasure[0][0] <= b:
        heapq.heappush(temp, -heapq.heappop(treasure)[1])
    
    if temp:
        result += heapq.heappop(temp)

print(-result)



# treasure_list = []

# print(treasure)

# while bag:
#     bag_weight = bag.pop()
#     i = 0

#     while i < len(treasure):
#         if treasure[i][0] <= bag_weight:
#             result += treasure[i][1]
#             treasure.pop(i)
#             break

#         elif treasure[i][0] > bag_weight:
#             i += 1

# print(result)