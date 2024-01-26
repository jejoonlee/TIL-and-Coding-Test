
left, right = {}, {}

for _ in range(3):
    A, B = map(int, input().split(' '))

    if A not in left:
        left[A] = 1
    else:
        left.pop(A)
    
    if B not in right:
        right[B] = 1
    else:
        right.pop(B)

print(f'{list(left.keys())[0]} {list(right.keys())[0]}')