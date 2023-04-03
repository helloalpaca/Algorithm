from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
E = int(input())
edges = [[] for i in range(N+1)]
visited = [False] * (N+1)
answer = -1

for _ in range(E):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def BFS(start):
    q = deque([start])
    visited[start]=True
    while q:
        now = q.popleft()
        for adj in edges[now]:
            if visited[adj] == False:
                q.append(adj)
                visited[adj]=True

BFS(1)

for v in visited:
    if v:
        answer+=1

print(answer)