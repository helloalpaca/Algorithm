from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

loop = int(input())
for _ in range(loop):
    M, N ,K = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == False:
                BFS(i, j)
                answer += 1

    print(answer)