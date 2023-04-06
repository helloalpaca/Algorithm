from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())
board = deque([])
q = deque([])
answer = 0

for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    board.append(inp)
    for j in range(M):
        if inp[j] == 1:
            q.append((i, j))

## BEGIN BFS
while q:
    nx, ny = q.popleft()
    for i in range(4):
        tx = nx + dx[i]
        ty = ny + dy[i]
        if 0 <= tx < N and 0 <= ty < M and board[tx][ty] != -1:
            if board[nx][ny] + 1 < board[tx][ty] or board[tx][ty] == 0:
                board[tx][ty] = board[nx][ny] + 1
                q.append((tx, ty))
## END BFS

if all(0 not in bo for bo in board):
    print(max(map(max, board))-1)
else:
    print(-1)