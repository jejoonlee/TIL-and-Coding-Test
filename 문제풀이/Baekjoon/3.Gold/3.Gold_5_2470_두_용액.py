import sys

sys.stdin = open("input.txt")

# 모든 수를 한번 씩 다 도는 것 

# N = int(input())

# liquid = sorted(list(map(int, input().split())))


# ans1 = 0
# ans2 = 0
# mid = abs(liquid[0] + liquid[-1])

# for i in range(N):
#     j = N - 1
#     while j != i:
#         temp = abs(liquid[i] + liquid[j])

#         if temp == 0:
#             ans1 = liquid[i]
#             ans2 = liquid[j]
#             break

#         elif temp < mid:
#             mid = temp
#             ans1 = liquid[i]
#             ans2 = liquid[j]
#             break
        
#         j -= 1
            
# print(ans1, ans2)


# 투 포인터를 사용해야 한다
# 투 포인터를 사용할 때에, 먼저 제일 왼쪽과 오른쪽 수들을 더한다
# 그리고 더했을 때에 음수가 나오면 왼쪽에서 한 칸을 옮기고
# 양수가 나오면 오른쪽에서 한 캉 앞으로 옮긴다

N = int(input())

liquid = sorted(list(map(int, input().split())))

start = 0
end = N - 1

ans1 = liquid[0]
ans2 = liquid[-1]
mid = abs(liquid[0] + liquid[-1])

while start != end:

    dif = liquid[start] + liquid[end]

    if dif < 0:
        if abs(dif) < mid:
            mid = abs(dif)
            ans1 = liquid[start]
            ans2 = liquid[end]
        start += 1

    elif dif > 0 :
        if abs(dif) < mid:
            mid = abs(dif)
            ans1 = liquid[start]
            ans2 = liquid[end]
        end -= 1

    else:
        ans1 = liquid[start]
        ans2 = liquid[end]
        break

print(ans1, ans2)