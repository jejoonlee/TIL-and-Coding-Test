a, b, c = map(int, input().split())

for i in a, b, c:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')