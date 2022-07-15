a, b, c = map(int, input().split())
min = (a, b, c)[0]

for i in a, b, c:
    if i < min:
        min = i
print(min)

a, b, c = map(int, input().split())
mini = min(a, b, c)

print(mini)