from collections import deque
import sys

N = int(input())
arr = deque([[] for _ in range(N)])
for i in range(N):
    arr[i] = list(sys.stdin.readline().rstrip())

visited = [[False for _ in range(N)] for _ in range(N)]
answer = []

def BFS(start):
    cnt = 1
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for adj_x, adj_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if adj_x >= 0 and adj_x < N and adj_y >= 0 and adj_y < N:
                if visited[adj_x][adj_y]==False and arr[adj_x][adj_y]=="1":
                    q.append((adj_x, adj_y))
                    visited[adj_x][adj_y]=True
                    cnt+=1
    answer.append(cnt)

start = (0, 0)
for i in range(N):
    for j in range(N):
        if visited[i][j]==False and arr[i][j]=="1":
            BFS((i, j))

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)