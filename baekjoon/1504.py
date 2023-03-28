import heapq
import sys

def djikstra(start):
    distance = [INF for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance

INF = sys.maxsize
N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().rstrip().split())

d_start = djikstra(1)
d_v1 = djikstra(v1)
d_v2 = djikstra(v2)

cnt = min(d_start[v1] + d_v1[v2] + d_v2[N], d_start[v2] + d_v2[v1] + d_v1[N])
print(cnt if cnt < INF else -1)