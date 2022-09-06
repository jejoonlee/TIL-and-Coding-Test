import sys
sys.stdin = open('input.txt', 'r')

# 1분에 1대당 A원, 2대당 B원, 3대당 C원

A, B, C = map(int, input().split())

# 1~100 인데 인덱스는 0부터 시작이라서
# 인덱스를 하나 더 만든다
park = [0] * 101

for _ in range(3):
    En, Ex = map(int, input().split())

    # 주차장에 도착 시간과 떠난 시간을 range를 두고
    # i 를 park, 리스트 변수에 저장시킨다
    for i in range(En, Ex):
        park[i] += 1

total_cost = 0

for num in park:
    if num == 1:
        cost_A = num * A
        total_cost += cost_A
    if num == 2:
        cost_B = num * B
        total_cost += cost_B
    if num == 3:            
        cost_C = num * C
        total_cost += cost_C

print(total_cost)