from collections import deque
import sys
input = sys.stdin.readline

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
    edges[i].sort(reverse=True)

def BFS(start):
    global cnt
    q = deque([start])
    visited[start] = True
    answer[start] = cnt
    cnt+=1
    while q:
        now = q.popleft()
        for adj in edges[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj]=True
                answer[adj]=cnt
                cnt+=1

BFS(R)

for i in range(1, N+1):
    print(answer[i])