import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dir = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

def bfs(board, row, column):

    queue = deque()
    queue.append([row, column])
    rLength, cLength = len(board), len(board[0])
    visited = [[-1] * cLength for _ in range(rLength)]
    visited[row][column] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(8):
            sr = r + dir[i][0]
            sc = c + dir[i][1]

            if 0 <= sr < rLength and 0 <= sc < cLength:
                if visited[sr][sc] == -1 or visited[sr][sc] > visited[r][c] + 1:
                    queue.append([sr, sc])
                    visited[sr][sc] = visited[r][c] + 1

    return visited

for _ in range(t):
    length = int(input())
    startRow, startColumn = map(int, input().split(' '))
    endRow, endColumn = map(int, input().split(' '))

    board = [[0] * length for _ in range(length)]

    visited = bfs(board, startRow, startColumn)
    
    print(visited[endRow][endColumn])