x, y, w, h = map(int, input().split(" "))

print(min(abs(0 - x), abs(0 - y), abs(x - w), abs(y - h)))
