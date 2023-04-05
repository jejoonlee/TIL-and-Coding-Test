import sys
sys.stdin = open('input.txt')

N = int(input())

board = [0] * N
result = 0

def is_possible(c):
    
    for column in range(c):
        if board[c] == board[column] or abs(c - column) == abs(board[c] - board[column]):
            return False
    
    return True


def backtracking(start):

    global result

    if start == N:
        result += 1
        print(board)
        return
    
    for column in range(N):

        board[start] = column

        if is_possible(start):
            backtracking(start + 1)    


backtracking(0)

print(result)