# 첫 제출 시간초과 -> 15~16줄 if d[now] < dist: continue 중요!

import heapq
import sys
read = sys.stdin.readline
INF = int(1e9)

def djikstra(start):
    d = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        # print(now)
        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < d[adj[0]]:
                # print(now, " to ", adj[0])
                heapq.heappush(q, (cost, adj[0]))
                d[adj[0]] = cost
        # print(d)
    return d

N = int(read().rstrip())
M = int(read().rstrip())
# bus = [list(map(int, read().rstrip().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, read().rstrip().split())
    graph[start].append((end, cost))
    # graph[end].append((start, cost))
A, B = map(int, read().rstrip().split())

d = djikstra(A)
# print(d[B])
# print(d)
print(d[B])