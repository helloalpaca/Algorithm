from collections import deque
import sys

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1: #해당 노드를 처음 방문할 때만 최단 거리 기록
                board[nx][ny] = board[x][y]+1
                q.append((nx, ny))

    return board[N-1][M-1]

print(BFS(0, 0))