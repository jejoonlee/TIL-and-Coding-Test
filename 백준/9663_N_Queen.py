
import sys

input = sys.stdin.readline

N = int(input())
chess = [0] * N
result = 0

def possible(idx):

    for i in range(idx):
        if chess[i] == chess[idx] or abs(i - idx) == abs(chess[i] - chess[idx]):
            return False

    return True

def n_queen(idx):
    global result

    if idx >= N:
        result += 1
        return
    
    for row in range(N):
        chess[idx] = row

        if possible(idx):
            n_queen(idx + 1)


n_queen(0)
print(result)