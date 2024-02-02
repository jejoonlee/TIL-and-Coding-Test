import sys

input = sys.stdin.readline

n = int(input())

count = 0

def combi(idx, array, limit):

    global count

    if len(array) >= limit:
        count += 1
        return
    
    for i in range(idx, len(nList)):
        combi(i + 1, array + [nList[i]], limit) 

nList = list(range(1, n + 1))
combi(0, [], 2)

print(count * 2)