import sys
sys.stdin = open('input.txt')

count = 0
while True:
    L, P, V = map(int, input().split())
    count += 1

    if L == 0 and P == 0 and V == 0: break

    else:
        full, part = V // P, V % P

        if part <= L:
            result = (full * L) + (part)
        else:
            result = (full * L) + (L)

    print(f'Case {count}: {result}')