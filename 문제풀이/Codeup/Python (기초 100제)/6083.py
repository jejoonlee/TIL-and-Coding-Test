red, green, blue = map(int, input().split())
cnt = 0

for r in range(0, red):
    for g in range(0, green):
        for b in range(0, blue):
            print(r, g, b)
            cnt += 1
print(cnt)

# cnt를 넣어 하나가 출력이 될때, 1을 더해준다