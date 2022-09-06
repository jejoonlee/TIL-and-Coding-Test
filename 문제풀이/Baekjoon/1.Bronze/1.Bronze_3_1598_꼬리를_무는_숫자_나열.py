
N, M = map(int, input().split())

# 4열로 되어 있어 4로 나눈 형태의 공식을 찾으면 된다

if N % 4 == 0:
    N = N - 4
if M % 4 == 0:
    M = M -4

x1 = N // 4
x2 = M // 4
y1 = N % 4
y2 = M % 4

if y1 == 0:
    y1 = 4
if y2 == 0:
    y2 = 4



result = abs(x1 - x2) + abs(y1 - y2)

print(result)