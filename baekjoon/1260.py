from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
edges = deque([[] for _ in range(N+1)])
v_dfs = [False] * (N+1)
v_bfs = [False] * (N+1)
a_dfs = []
a_bfs = []

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    edges[i].sort()

def DFS(start):
    a_dfs.append(start)
    v_dfs[start] = True
    for adj in edges[start]:
        if not v_dfs[adj]:
            DFS(adj)

def BFS(start):
    q = deque([start])
    v_bfs[start]=True
    a_bfs.append(start)
    while q:
        now = q.popleft()
        for adj in edges[now]:
            if not v_bfs[adj]:
                q.append(adj)
                v_bfs[adj]=True
                a_bfs.append(adj)

DFS(V)
BFS(V)

for a in a_dfs:
    print(a, end=" ")
print("")
for a in a_bfs:
    print(a, end=" ")
