r = int(input())
a = input().split()

for i in range(r):
    a[i] = int(a[i])

min = a[0]
for i in range(0,r):
    if a[i] < min:
        min = a[i]

print(min)

# mini = min(a) 함수를 써도 된다
