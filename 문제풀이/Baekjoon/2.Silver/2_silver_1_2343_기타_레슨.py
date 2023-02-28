import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def count_cd(time):

    count = 0
    temp = 0

    for lecture in lectures:
        if temp + lecture <= time:
            temp += lecture
        else:
            count += 1
            temp = lecture
    
    return count + 1


lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)

while left <= right:
    
    mid = (left + right) // 2

    blueray = count_cd(mid)

    if blueray <= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)