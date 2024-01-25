
chess = list(map(int, input().split(' ')))

need = []

for i in range(0, len(chess)):

    if 0 <= i < 2:
        need.append(1 - chess[i])
    
    elif i < 5:
        need.append(2 - chess[i])
    
    else:
        need.append(8 - chess[i])

print(' '.join(list(map(str, need))))