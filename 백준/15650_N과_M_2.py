import sys

input = sys.stdin.readline

def combi(array, result, idx, limit):
    
    if len(result) >= limit:
        print(' '.join(list(map(str, result))))
        return
    
    for i in range(idx, len(array)):
        combi(array, result + [array[i]], i + 1, limit)

n, m = map(int, input().split(' '))

combi(list(range(1, n + 1)), [], 0, m)