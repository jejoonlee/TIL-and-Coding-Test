
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연서 x를 return

n = 12
x = 0

while True:
    x += 1
    if n % x == 1:
        break

print(x)