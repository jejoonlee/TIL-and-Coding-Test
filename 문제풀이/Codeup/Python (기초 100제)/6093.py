r = int(input())
a = input().split()

for i in range(r):
    a[i] = int(a[i])
# print(a)        [10, 4, 2, 3, 6, 6, 7, 9, 8, 5]

for i in range(r-1, -1, -1):    # r-1번째에서 0까지 뒤로 1씩
    print(a[i], end =' ')