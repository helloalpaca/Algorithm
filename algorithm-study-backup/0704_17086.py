"""
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
"""

# BFS
# 1. 상어가 있는 위치마다 BFS를 돌려서 안전거리를 찾는다.
# 2. 가장 작은 값을 return

from collections import deque
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
def BFS(graph, x, y):
    global d
    n = len(graph)
    m = len(graph[0])
    q = deque([(x, y)])
    d[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and (d[nx][ny] == -1 or d[nx][ny] > d[x][y]+1):
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [[-1 for _ in range(M)] for _ in range(N)]
max = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            BFS(graph, i, j)

for i in range(N):
    for j in range(M):
        if d[i][j] > max:
            max = d[i][j]

print(max - 1)