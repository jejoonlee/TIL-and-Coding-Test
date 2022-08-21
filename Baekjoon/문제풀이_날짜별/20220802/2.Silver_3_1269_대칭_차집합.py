
num = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = set(A)
B = set(B)

s_set = []

for a in A:
    if a not in B:
        s_set.append(a)

for b in B:
    if b not in A:
        s_set.append(b)

result = len(s_set)
print(result)