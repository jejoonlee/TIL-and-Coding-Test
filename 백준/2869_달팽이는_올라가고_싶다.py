A, B, V = map(int, input().split(" "))

top = V - B

climb = top // (A - B)
leftToClimb = top % (A - B)

if leftToClimb > 0:
    print(climb + 1)
else:
    print(climb)
