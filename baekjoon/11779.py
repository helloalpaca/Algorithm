# 첫 제출 시간초과 -> 15~16줄 if d[now] < dist: continue 중요!

import heapq
import sys
read = sys.stdin.readline
INF = int(1e9)

def djikstra(start):
    d = [INF] * (N+1)
    w = [start] * (N+1)
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
                w[adj[0]] = now
        # print(d)
    return d, w

N = int(read().rstrip())
M = int(read().rstrip())
# bus = [list(map(int, read().rstrip().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, read().rstrip().split())
    graph[start].append((end, cost))
    # graph[end].append((start, cost))
A, B = map(int, read().rstrip().split())

d, w = djikstra(A)
# print(w)
# print(d)
# print(w)
# # print(d[B])
# # print(d)
# print(d[B])

answer = []
tmp = B
while tmp != A:
    answer.append(str(tmp))
    tmp = w[tmp]

# print(A)
answer.append(str(A))
answer.reverse()
# print(answer)

print(d[B])
print(len(answer))
print(' '.join(answer))