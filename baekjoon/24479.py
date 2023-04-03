from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
edges = deque([[] for _ in range(N+1)])
visited = [False] * (N+1)
answer = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    edges[i].sort()

def DFS(start):
    global cnt
    visited[start] = True
    answer[start] = cnt
    cnt+=1
    for adj in edges[start]:
        if not visited[adj]:
            DFS(adj)

DFS(R)

for i in range(1, N+1):
    print(answer[i])