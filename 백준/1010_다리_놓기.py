import sys, math

input = sys.stdin.readline

def combi(idx, array, limit):

    global count

    if len(array) == limit:
        count += 1
        return
    
    for i in range(idx, len(mList)):
        combi(i + 1, array + [mList[i]], limit)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(" "))
    print(int(math.factorial(m)) // int(math.factorial(n) * math.factorial(m - n)))

    count = 0

    mList = list(range(1, m+1))
    combi(0, [], n)

    print(count)
