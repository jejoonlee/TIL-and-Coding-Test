import sys
sys.stdin = open("input.txt")

# t는 농부가 하루를 시작하는 시간이다
# t를 0부터 시작해서 1씩 더해가면서 존이 제 시간에 일을 끝낼 수 있는지 구한다
# 여기서 일은, 끝내야 하는 시간의 기준으로 오름차순으로 정렬을 한다

N = int(input())
work = []
for _ in range(N):
    work.append(tuple(map(int, input().split())))

work.sort(key=lambda x: x[1])
hour = 0
flag = True

while True:
    time = hour
    
    for i in range(len(work)):
        time += work[i][0]

        if time > work[i][1]:
            flag = False
            break
    
    if flag == True:
        hour += 1
    else:
        break

if hour != 0:
    print(hour - 1)
else:
    print(-1)