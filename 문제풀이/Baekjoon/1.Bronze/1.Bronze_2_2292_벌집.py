
N = int(input())

cnt = 1
n_room = 6
start = 1

while N > start:
    cnt += 1
    # 시작은 1에서 시작한다
    # 그리고 그 지점에서 n_room을 더해준다
    start += n_room
    # n_room은 한 칸 갈때마다 6이 늘어난다
    n_room += 6

print(cnt)