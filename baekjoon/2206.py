from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(a, b, c):
    q = deque([(a, b, c)])
    visited[a][b][c]=1

    while q:
        x, y, flag = q.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][flag]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny]==1 and flag==0:
                q.append((nx, ny, 1))
                visited[nx][ny][1]=visited[x][y][0]+1
            if board[nx][ny]==0 and visited[nx][ny][flag]==0:
                q.append((nx, ny, flag))
                visited[nx][ny][flag]=visited[x][y][flag]+1
    return -1

print(BFS(0, 0, 0))