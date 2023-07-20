"""
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
"""
"""
4 4
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
"""
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def BFS(board, x, y):
    q = deque([(x, y)])
    board[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<M  and (board[nx][ny] == -1 or board[nx][ny] > board[x][y]+1):
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

N, M = map(int, input().split())
board = [[-1]*M for _ in range(N)]
shark = [[0]*M for _ in range(N)]

for i in range(N):
    shark[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if shark[i][j] == 1:
            BFS(board, i, j)

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > answer:
            answer = board[i][j]
print(answer - 1)