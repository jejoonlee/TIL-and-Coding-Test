
num = int(input())

sum = 0
store = list(map(int, input().split()))

for i in range(num):
    if store[i] == sum % 3:
        sum += 1

print(sum)
